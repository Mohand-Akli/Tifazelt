# Outils de modelisation low-poly pour la lignee Cramosaur (Blender, Z up, avant = -Y)
import bpy, bmesh, math, random
from mathutils import Vector, Matrix, Euler
from mathutils.bvhtree import BVHTree

PAL = {
    "Corps":    ((0.028, 0.026, 0.026, 1), 0),
    "Ventre":   ((0.15, 0.095, 0.08, 1), 0),
    "Taches":   ((0.014, 0.013, 0.013, 1), 0),
    "Roche":    ((0.018, 0.015, 0.014, 1), 0),
    "Fourrure": ((0.13, 0.022, 0.008, 1), 0),
    "Corne":    ((0.75, 0.13, 0.02, 1), 0),
    "CorneSombre": ((0.11, 0.085, 0.07, 1), 0),
    "Lave":     ((1.0, 0.20, 0.02, 1), 1.3),
    "Oeil":     ((1.0, 0.16, 0.0, 1), 0.15),
    "Pupille":  ((0.005, 0.004, 0.004, 1), 0),
    "Reflet":   ((1, 1, 1, 1), 0.8),
    "Griffes":  ((0.22, 0.16, 0.13, 1), 0),
    "Dents":    ((0.85, 0.80, 0.70, 1), 0),
    "Bouche":   ((0.30, 0.06, 0.06, 1), 0),
}

def mat(name):
    m = bpy.data.materials.get(name)
    if m:
        return m
    col, emit = PAL[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = next((n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED'), None)
    if b is None:
        b = nt.nodes.new("ShaderNodeBsdfPrincipled")
        outn = next((n for n in nt.nodes if n.type == 'OUTPUT_MATERIAL'), None) or nt.nodes.new("ShaderNodeOutputMaterial")
        nt.links.new(b.outputs[0], outn.inputs[0])
    b.inputs["Base Color"].default_value = col
    b.inputs["Roughness"].default_value = 0.65
    if name == "Obsidienne":
        b.inputs["Roughness"].default_value = 0.45
    if emit:
        if name == "Lave":
            b.inputs["Base Color"].default_value = (0.05, 0.005, 0, 1)
        b.inputs["Emission Color"].default_value = col
        b.inputs["Emission Strength"].default_value = emit
    m.diffuse_color = col
    return m

def coll(name):
    c = bpy.data.collections.get(name)
    if not c:
        c = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(c)
    return c

def _link(ob, c):
    for uc in list(ob.users_collection):
        uc.objects.unlink(ob)
    c.objects.link(ob)
    return ob

def _bm_obj(bm, name, material, c):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me); bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = bpy.data.objects.new(name, me)
    me.materials.append(mat(material))
    c.objects.link(ob)
    return ob

def ell(name, c, loc, rad, material="Corps", rot=(0, 0, 0), seg=12, rings=8):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=rings, radius=1)
    bmesh.ops.scale(bm, vec=Vector(rad), verts=bm.verts)
    bmesh.ops.rotate(bm, matrix=Euler([math.radians(a) for a in rot]).to_matrix(), verts=bm.verts)
    bmesh.ops.translate(bm, vec=Vector(loc), verts=bm.verts)
    return _bm_obj(bm, name, material, c)

def rock(name, c, loc, rad, material="Roche", rot=(0, 0, 0), seed=0, jitter=0.18):
    rnd = random.Random(seed)
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=1, radius=1)
    for v in bm.verts:
        v.co *= 1 + rnd.uniform(-jitter, jitter)
    bmesh.ops.scale(bm, vec=Vector(rad), verts=bm.verts)
    bmesh.ops.rotate(bm, matrix=Euler([math.radians(a) for a in rot]).to_matrix(), verts=bm.verts)
    bmesh.ops.translate(bm, vec=Vector(loc), verts=bm.verts)
    ob = _bm_obj(bm, name, material, c)
    for p in ob.data.polygons:
        p.use_smooth = False
    return ob

def cone(name, c, base, tip, r1, material="Corne", seg=10, bend=0.0, bend_dir=(0, 0, 1), rings=5):
    """Cone (corne, griffe, epine) de base a tip, eventuellement courbe."""
    base, tip = Vector(base), Vector(tip)
    bd = Vector(bend_dir)
    bm = bmesh.new()
    axis = tip - base
    L = axis.length
    z = axis.normalized()
    x = z.orthogonal().normalized()
    y = z.cross(x)
    prev = None
    rings_v = []
    for i in range(rings + 1):
        t = i / rings
        r = r1 * (1 - t) ** 0.9
        center = base + axis * t + bd * (bend * L * (t * t))
        if i == rings:
            rings_v.append([bm.verts.new(center)])
            break
        ring = []
        for k in range(seg):
            a = 2 * math.pi * k / seg
            ring.append(bm.verts.new(center + (x * math.cos(a) + y * math.sin(a)) * r))
        rings_v.append(ring)
    for i in range(len(rings_v) - 1):
        A, B = rings_v[i], rings_v[i + 1]
        for k in range(seg):
            if len(B) == 1:
                bm.faces.new((A[k], A[(k + 1) % seg], B[0]))
            else:
                bm.faces.new((A[k], A[(k + 1) % seg], B[(k + 1) % seg], B[k]))
    bm.faces.new(list(reversed(rings_v[0])))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _bm_obj(bm, name, material, c)

def tube(name, c, pts, radii, material="Corps", seg=12, scale_x=1.0):
    """Tube effile le long d'une polyligne (queue, cou, membres)."""
    pts = [Vector(p) for p in pts]
    bm = bmesh.new()
    rings_v = []
    up = Vector((1, 0, 0))
    for i, p in enumerate(pts):
        d = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
        x = up - d * up.dot(d)
        if x.length < 1e-4:
            x = d.orthogonal()
        x.normalize()
        y = d.cross(x)
        r = radii[i]
        if r <= 0:
            rings_v.append([bm.verts.new(p)])
            continue
        ring = [bm.verts.new(p + (x * math.cos(2 * math.pi * k / seg) * scale_x + y * math.sin(2 * math.pi * k / seg)) * r) for k in range(seg)]
        rings_v.append(ring)
    for i in range(len(rings_v) - 1):
        A, B = rings_v[i], rings_v[i + 1]
        if len(B) == 1:
            for k in range(seg):
                bm.faces.new((A[k], A[(k + 1) % seg], B[0]))
        elif len(A) == 1:
            for k in range(seg):
                bm.faces.new((B[(k + 1) % seg], B[k], A[0]))
        else:
            for k in range(seg):
                bm.faces.new((A[k], A[(k + 1) % seg], B[(k + 1) % seg], B[k]))
    if len(rings_v[0]) > 1:
        bm.faces.new(list(reversed(rings_v[0])))
    if len(rings_v[-1]) > 1:
        bm.faces.new(rings_v[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _bm_obj(bm, name, material, c)

def bvh_of(objs):
    bm = bmesh.new()
    for o in objs:
        tmp = o.data.copy()
        tmp.transform(o.matrix_world)
        bm.from_mesh(tmp)
        bpy.data.meshes.remove(tmp)
    bmesh.ops.triangulate(bm, faces=bm.faces)
    return BVHTree.FromBMesh(bm)

def proj(bvh, p, ref=None):
    """Point le plus proche sur la surface + normale."""
    loc, nor, idx, d = bvh.find_nearest(Vector(p))
    return loc, nor

def patch(name, c, bvh, p, size, material="Lave", flat=0.25, rot=0.0, lift=0.0, seg=8):
    """Tache aplatie collee a la surface (ellipse orientee par la normale)."""
    loc, nor = proj(bvh, p)
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=4, radius=1)
    bmesh.ops.scale(bm, vec=Vector((size[0], size[1], size[0] * flat)), verts=bm.verts)
    bmesh.ops.rotate(bm, matrix=Matrix.Rotation(math.radians(rot), 3, 'Z'), verts=bm.verts)
    q = Vector((0, 0, 1)).rotation_difference(nor)
    bmesh.ops.rotate(bm, matrix=q.to_matrix(), verts=bm.verts)
    bmesh.ops.translate(bm, vec=loc + nor * lift, verts=bm.verts)
    return _bm_obj(bm, name, material, c)

def vein(name, c, bvh, pts, width=0.012, material="Lave", lift=0.004, seg=3, subdiv=2):
    """Veine de lave : polyligne projetee sur la surface, tube fin aplati."""
    pts = [Vector(p) for p in pts]
    dense = []
    for i in range(len(pts) - 1):
        for s in range(subdiv):
            dense.append(pts[i].lerp(pts[i + 1], s / subdiv))
    dense.append(pts[-1])
    sp = []
    for p in dense:
        loc, nor = proj(bvh, p)
        sp.append(loc + nor * lift)
    n = len(sp)
    radii = [width * (0.55 + 0.45 * math.sin(math.pi * i / (n - 1))) for i in range(n)]
    return tube(name, c, sp, radii, material=material, seg=seg)

def join_by_material(c, prefix):
    """Fusionne les objets d'une collection en un objet par materiau."""
    groups = {}
    for o in list(c.objects):
        if o.type == 'MESH':
            groups.setdefault(o.data.materials[0].name, []).append(o)
    out = []
    for mname, objs in groups.items():
        bpy.ops.object.select_all(action='DESELECT')
        for o in objs:
            o.select_set(True)
        bpy.context.view_layer.objects.active = objs[0]
        if len(objs) > 1:
            bpy.ops.object.join()
        o = bpy.context.view_layer.objects.active
        o.name = f"{prefix}_{mname}"
        o.data.name = o.name
        out.append(o)
    return out

def tris(c):
    dg = bpy.context.evaluated_depsgraph_get()
    t = 0
    for o in c.all_objects:
        if o.type == 'MESH':
            t += sum(len(p.vertices) - 2 for p in o.evaluated_get(dg).data.polygons)
    return t

def clear(c):
    for o in list(c.objects):
        me = o.data
        bpy.data.objects.remove(o)
        if me and me.users == 0:
            bpy.data.meshes.remove(me)

def render_views(cname, out, dirs=((-0.9, -1.0, 0.35), (1.0, -0.8, 0.3)), res=(800, 600), only=True):
    """Rendu de controle : cadre la collection depuis plusieurs directions."""
    sc = bpy.context.scene
    target = bpy.data.collections[cname]
    if only:
        for ch in sc.collection.children:
            if ch.name not in (cname, "Controle"):
                ch.hide_render = True
        target.hide_render = False
    pts = []
    for o in target.all_objects:
        if o.type == 'MESH':
            pts += [o.matrix_world @ Vector(b) for b in o.bound_box]
    mn = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    mx = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    ctr = (mn + mx) / 2
    rad = (mx - mn).length / 2
    cam = bpy.data.objects["CamControle"]
    sc.camera = cam
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    sc.render.image_settings.file_format = 'PNG'
    sc.view_settings.view_transform = 'Standard'
    fov = cam.data.angle_y if res[0] > res[1] else cam.data.angle_x
    dist = rad / math.tan(fov / 2) * 0.95
    files = []
    for i, d in enumerate(dirs):
        d = Vector(d).normalized()
        cam.location = ctr + d * dist
        cam.rotation_euler = (ctr - cam.location).to_track_quat('-Z', 'Y').to_euler()
        # lumieres attachees a la vue
        key = bpy.data.objects["Cle"]; back = bpy.data.objects["Contre"]
        side = Vector((-d.y, d.x, 0)).normalized()
        key.location = ctr + (d + side * 0.8 + Vector((0, 0, 1.2))).normalized() * rad * 4
        key.rotation_euler = (ctr - key.location).to_track_quat('-Z', 'Y').to_euler()
        back.location = ctr + (-d - side * 0.5 + Vector((0, 0, 1))).normalized() * rad * 4
        back.rotation_euler = (ctr - back.location).to_track_quat('-Z', 'Y').to_euler()
        key.data.energy = 210 * (rad * 4) ** 2 / 9
        back.data.energy = 160 * (rad * 4) ** 2 / 9
        sc.render.filepath = f"{out}_{i}.png"
        bpy.ops.render.render(write_still=True)
        files.append(sc.render.filepath)
    return files

def reset_mats():
    for n in PAL:
        m = bpy.data.materials.get(n)
        if m and m.users == 0:
            bpy.data.materials.remove(m)

PAL["Contour"] = ((0.012, 0.008, 0.008, 1), 0)
PAL["Obsidienne"] = ((0.008, 0.007, 0.008, 1), 0)

def _mesh_from_eval(ob):
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    old = ob.data
    ob.modifiers.clear()
    ob.data = me
    if old.users == 0:
        bpy.data.meshes.remove(old)
    return ob

def fuse(objs, name, c, voxel=0.01, smooth_iter=6, smooth_fac=0.5, target_tris=3500, paint=None):
    """Fusionne des formes en une seule peau organique (remesh voxel, lissage, decimation)."""
    bm = bmesh.new()
    for o in objs:
        tmp = o.data.copy(); tmp.transform(o.matrix_world); bm.from_mesh(tmp); bpy.data.meshes.remove(tmp)
    for o in objs:
        me = o.data; bpy.data.objects.remove(o)
        if me.users == 0: bpy.data.meshes.remove(me)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); c.objects.link(ob)
    r = ob.modifiers.new("R", 'REMESH'); r.mode = 'VOXEL'; r.voxel_size = voxel; r.use_smooth_shade = True
    s = ob.modifiers.new("S", 'SMOOTH'); s.factor = smooth_fac; s.iterations = smooth_iter
    _mesh_from_eval(ob)
    ob.data.materials.append(mat("Corps"))
    if paint:
        paint(ob)
    n = sum(len(p.vertices) - 2 for p in ob.data.polygons)
    d = ob.modifiers.new("D", 'DECIMATE'); d.ratio = min(1.0, target_tris / max(n, 1))
    _mesh_from_eval(ob)
    for p in ob.data.polygons: p.use_smooth = True
    return ob

def assign_faces(ob, material, test):
    """Affecte un materiau aux faces dont (centre, normale) passent le test."""
    m = mat(material)
    if m.name not in ob.data.materials:
        ob.data.materials.append(m)
    idx = list(ob.data.materials).index(m)
    k = 0
    for p in ob.data.polygons:
        if test(p.center, p.normal):
            p.material_index = idx; k += 1
    return k

def frame(nor, up=(0, 0, 1)):
    """Repere local : Z = normale, Y = au plus pres de 'up'."""
    n = Vector(nor).normalized(); u = Vector(up)
    y = u - n * u.dot(n)
    if y.length < 1e-4:
        y = n.orthogonal()
    y.normalize(); x = y.cross(n)
    return Matrix((x, y, n)).transposed()

def raycast(bvh, p, outward):
    """Point de surface vu depuis l'exterieur (p + outward) en visant vers p."""
    o = Vector(outward).normalized()
    loc, nor, i, d = bvh.ray_cast(Vector(p) + o * 0.6, -o)
    if loc is None:
        return proj(bvh, p)
    return loc, nor

def blob(name, c, bvh, p, size, material="Lave", seed=0, jitter=0.35, n=9, thick=0.006, rot=0.0, lift=0.002):
    """Tache irreguliere (lave, tache sombre) posee sur la surface."""
    rnd = random.Random(seed)
    loc, nor = proj(bvh, p)
    bm = bmesh.new()
    top, bot = [], []
    rs = [1 + rnd.uniform(-jitter, jitter) for _ in range(n)]
    for i in range(n):
        a = 2 * math.pi * i / n
        v = Vector((math.cos(a) * size[0] * rs[i], math.sin(a) * size[1] * rs[i], 0))
        top.append(bm.verts.new(v + Vector((0, 0, thick))))
        bot.append(bm.verts.new(v - Vector((0, 0, thick * 2))))
    bm.faces.new(top); bm.faces.new(list(reversed(bot)))
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((bot[i], bot[j], top[j], top[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bmesh.ops.rotate(bm, matrix=Matrix.Rotation(math.radians(rot), 3, 'Z'), verts=bm.verts)
    bmesh.ops.rotate(bm, matrix=frame(nor), verts=bm.verts)
    bmesh.ops.translate(bm, vec=loc + nor * lift, verts=bm.verts)
    ob = _bm_obj(bm, name, material, c)
    for f in ob.data.polygons: f.use_smooth = False
    return ob

def plate(name, c, bvh, p, r, h, material="Obsidienne", seed=0, rot=0.0, tilt=(0, 0), sink=0.3, stretch=1.0, sides=6, outward=None):
    """Plaque d'obsidienne : prisme hexagonal biseaute, irregulier, pose sur la surface."""
    rnd = random.Random(seed)
    loc, nor = raycast(bvh, p, outward) if outward else proj(bvh, p)
    bm = bmesh.new()
    bot, mid, top = [], [], []
    for i in range(sides):
        a = 2 * math.pi * i / sides + rnd.uniform(-0.15, 0.15)
        rr = r * (1 + rnd.uniform(-0.15, 0.15))
        x, y = math.cos(a) * rr * stretch, math.sin(a) * rr
        bot.append(bm.verts.new((x, y, -h * sink)))
        mid.append(bm.verts.new((x, y, h * 0.55)))
        top.append(bm.verts.new((x * 0.62, y * 0.62, h * (1 + rnd.uniform(-0.1, 0.25)))))
    bm.faces.new(list(reversed(bot)))
    bm.faces.new(top)
    for i in range(sides):
        j = (i + 1) % sides
        bm.faces.new((bot[i], bot[j], mid[j], mid[i]))
        bm.faces.new((mid[i], mid[j], top[j], top[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bmesh.ops.rotate(bm, matrix=Matrix.Rotation(math.radians(rot), 3, 'Z'), verts=bm.verts)
    bmesh.ops.rotate(bm, matrix=Euler((math.radians(tilt[0]), math.radians(tilt[1]), 0)).to_matrix(), verts=bm.verts)
    bmesh.ops.rotate(bm, matrix=frame(nor, (0, 1, 0)), verts=bm.verts)
    bmesh.ops.translate(bm, vec=loc, verts=bm.verts)
    ob = _bm_obj(bm, name, material, c)
    for f in ob.data.polygons: f.use_smooth = False
    return ob

def tuft(name, c, base, tip, w, t, material="Fourrure", side=(1, 0, 0), bend=0.0, bend_dir=(0, 0, -1)):
    """Meche aplatie (fourrure) : losange effile de base a tip."""
    base, tip, side = Vector(base), Vector(tip), Vector(side).normalized()
    ax = tip - base
    nrm = ax.cross(side).normalized()
    bd = Vector(bend_dir)
    bm = bmesh.new()
    rows = []
    for i, f in enumerate((0, 0.35, 0.7, 1.0)):
        ww = w * (1 - f) ** 0.8 if f < 1 else 0
        cen = base + ax * f + bd * bend * ax.length * f * f
        if ww == 0:
            rows.append([bm.verts.new(cen)]); continue
        rows.append([bm.verts.new(cen - side * ww), bm.verts.new(cen + nrm * t * (1 - f)), bm.verts.new(cen + side * ww), bm.verts.new(cen - nrm * t * (1 - f))])
    for i in range(len(rows) - 1):
        A, B = rows[i], rows[i + 1]
        for k in range(4):
            if len(B) == 1: bm.faces.new((A[k], A[(k + 1) % 4], B[0]))
            else: bm.faces.new((A[k], A[(k + 1) % 4], B[(k + 1) % 4], B[k]))
    bm.faces.new(list(reversed(rows[0])))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _bm_obj(bm, name, material, c)

def outline(ob, c, thick=0.007):
    """Contour facon dessin : coque gonflee aux normales inversees (visible seulement sur la silhouette)."""
    bm = bmesh.new(); bm.from_mesh(ob.data)
    bm.normal_update()
    for v in bm.verts:
        v.co += v.normal * thick
    bmesh.ops.reverse_faces(bm, faces=bm.faces)
    me = bpy.data.meshes.new(ob.name + "_Contour"); bm.to_mesh(me); bm.free()
    o2 = bpy.data.objects.new(me.name, me); c.objects.link(o2)
    me.materials.append(mat("Contour"))
    for p in me.polygons: p.material_index = 0; p.use_smooth = True
    mat("Contour").use_backface_culling = True
    return o2

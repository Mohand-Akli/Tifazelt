# Lignée Dauphin (28 oct. 2026) : poses procédurales dans Blender, calquées sur le mode « flotte » / « nage » de
# ReplicatedStorage.Tifazelts.Animation (mêmes os, mêmes amplitudes). Sert aux sprites de combat (boucle de respiration)
# et aux contrôles visuels. Convention : p = pitch autour de X (+ = museau vers le bas, queue vers le haut),
# y = autour de Z, r = autour de l'axe avant (-Y), l = décalage vers le haut en fraction de la largeur du corps.
import math
from mathutils import Matrix, Vector, Quaternion

AVANT = Vector((0, -1, 0))
LARGEUR = {"Dauphimyst": 0.50, "Dauphiclos": 0.46, "Dauphiracle": 0.48}
ES = {  # mêmes réglages que dans Animation.lua (PROVISOIRES)
    "Dauphimyst":  dict(periode=1.0, queue=0.20, nageoires=0.28, haut=0.045),
    "Dauphiclos":  dict(periode=0.9, queue=0.23, nageoires=0.26, haut=0.05),
    "Dauphiracle": dict(periode=0.8, queue=0.26, nageoires=0.24, haut=0.055),
}

def _ajouter(pose, nom, p=0.0, y=0.0, r=0.0, l=0.0):
    e = pose.setdefault(nom, [0.0, 0.0, 0.0, 0.0])
    e[0] += p; e[1] += y; e[2] += r; e[3] += l

def _nageoires(pose, w, amp, decal):
    s = math.sin(w + decal)
    _ajouter(pose, "BrasG1", r=amp * s); _ajouter(pose, "BrasD1", r=-amp * s)
    s2 = math.sin(w + decal - 0.7)
    _ajouter(pose, "BrasG2", r=0.5 * amp * s2); _ajouter(pose, "BrasD2", r=-0.5 * amp * s2)
    s3 = math.sin(w + decal - 1.2)
    _ajouter(pose, "NageoireG", r=0.7 * amp * s3); _ajouter(pose, "NageoireD", r=-0.7 * amp * s3)

def pose_flotte(espece, w, k=1.0, fins=1.0):
    """Vol stationnaire. w = phase (radians). fins = fréquence des nageoires par rapport au corps (1 = boucle exacte)."""
    es = ES[espece]; pose = {}
    _ajouter(pose, "Racine", l=es["haut"] * math.sin(w))
    _ajouter(pose, "Dos1", p=0.04 * math.sin(w - 0.4)); _ajouter(pose, "Cou1", p=-0.03 * math.sin(w - 0.8)); _ajouter(pose, "Tete", p=0.02 * math.sin(w - 1.2))
    for i in range(1, 5):
        _ajouter(pose, "Queue%d" % i, p=0.035 * i * math.sin(w - 0.5 * i - 0.6))
    _ajouter(pose, "Aileron", p=0.04 * math.sin(w - 1.0))
    _nageoires(pose, w * fins, 0.16, 0.5)
    return {n: [v * k for v in e] for n, e in pose.items()}

def pose_nage(espece, w, k=1.0):
    es = ES[espece]; pose = {}
    _ajouter(pose, "Racine", l=es["haut"] * math.sin(2 * w + 0.5))
    _ajouter(pose, "Hanches", p=0.03 * math.sin(w - 0.3))
    _ajouter(pose, "Dos1", p=0.05 * math.sin(w - 0.6)); _ajouter(pose, "Cou1", p=-0.05 * math.sin(w - 0.9)); _ajouter(pose, "Tete", p=-0.03 * math.sin(w - 1.2))
    for i in range(1, 5):
        _ajouter(pose, "Queue%d" % i, p=es["queue"] * (0.4 + 0.2 * i) * math.sin(w - 0.55 * i - 0.8))
    _ajouter(pose, "Aileron", p=0.07 * math.sin(w - 1.0))
    _nageoires(pose, w, es["nageoires"], 0.6)
    return {n: [v * k for v in e] for n, e in pose.items()}

def appliquer(rig, pose, espece):
    """Pose les os de l'armature. Les rotations sont définies sur les axes du modèle au repos (comme Bone.Transform dans Studio)."""
    haut = Vector((0, 0, 1)); lat = haut.cross(AVANT)
    for pb in rig.pose.bones:
        pb.rotation_mode = "QUATERNION"
        e = pose.get(pb.name)
        if not e:
            pb.rotation_quaternion = Quaternion((1, 0, 0, 0)); pb.location = (0, 0, 0); continue
        R = Quaternion(lat, e[0]) @ Quaternion(haut, e[1]) @ Quaternion(AVANT, e[2])
        Rb = pb.bone.matrix_local.to_3x3()
        loc = Rb.inverted() @ (haut * (e[3] * LARGEUR[espece]))
        local = (Rb.inverted() @ R.to_matrix() @ Rb).to_quaternion()
        pb.rotation_quaternion = local
        pb.location = loc

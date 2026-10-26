"""Corrige les GLB Meshy : UV quantifiées (x16, KHR_texture_transform ignoré par Studio) et images WebP -> JPEG."""
import struct, json, subprocess, os, sys, tempfile
src_dir, out_dir = sys.argv[1], sys.argv[2]
os.makedirs(out_dir, exist_ok=True)
for n in ["Cramosaur", "Cramoraptor", "Cramorex"]:
    d = open(f"{src_dir}/{n}_v02.glb", "rb").read()
    L = struct.unpack("<I", d[12:16])[0]
    j = json.loads(d[20:20+L]); b = bytearray(d[20+L+8:])
    # 1. UV : u16 normalisés x16
    a = j["accessors"][j["meshes"][0]["primitives"][0]["attributes"]["TEXCOORD_0"]]
    bv = j["bufferViews"][a["bufferView"]]
    off = bv.get("byteOffset", 0) + a.get("byteOffset", 0); st = bv.get("byteStride") or 4
    for i in range(a["count"]):
        u, v = struct.unpack_from("<HH", b, off + i*st)
        assert u * 16 <= 65535 and v * 16 <= 65535
        struct.pack_into("<HH", b, off + i*st, u * 16, v * 16)
    # 2. retirer la transformation de texture
    m = j["materials"][0]
    def clean(o):
        if isinstance(o, dict):
            o.get("extensions", {}).pop("KHR_texture_transform", None)
            if "extensions" in o and not o["extensions"]: del o["extensions"]
            for v in o.values(): clean(v)
    clean(m)
    j["extensionsUsed"] = [e for e in j["extensionsUsed"] if e not in ("KHR_texture_transform", "EXT_texture_webp")]
    j["extensionsRequired"] = [e for e in j.get("extensionsRequired", []) if e in j["extensionsUsed"]]
    if not j["extensionsRequired"]: j.pop("extensionsRequired")
    # 3. WebP -> JPEG, ajoutés en fin de binaire
    tmp = tempfile.mkdtemp()
    for t in j["textures"]:
        t["source"] = t["extensions"]["EXT_texture_webp"]["source"]; del t["extensions"]
    for i, im in enumerate(j["images"]):
        bvi = j["bufferViews"][im["bufferView"]]
        data = bytes(b[bvi.get("byteOffset", 0): bvi.get("byteOffset", 0) + bvi["byteLength"]])
        open(f"{tmp}/{i}.webp", "wb").write(data)
        subprocess.run(["sips", "-s", "format", "jpeg", f"{tmp}/{i}.webp", "--out", f"{tmp}/{i}.jpg"], check=True, capture_output=True)
        jpg = open(f"{tmp}/{i}.jpg", "rb").read()
        while len(b) % 4: b.append(0)
        j["bufferViews"].append({"buffer": 0, "byteOffset": len(b), "byteLength": len(jpg)})
        b += jpg
        im["bufferView"] = len(j["bufferViews"]) - 1; im["mimeType"] = "image/jpeg"
    while len(b) % 4: b.append(0)
    j["buffers"][0]["byteLength"] = len(b)
    js = json.dumps(j, separators=(",", ":")).encode()
    while len(js) % 4: js += b" "
    out = struct.pack("<4sII", b"glTF", 2, 12 + 8 + len(js) + 8 + len(b)) + struct.pack("<I4s", len(js), b"JSON") + js + struct.pack("<I4s", len(b), b"BIN\0") + bytes(b)
    open(f"{out_dir}/{n}_v03.glb", "wb").write(out); print(n, len(out))

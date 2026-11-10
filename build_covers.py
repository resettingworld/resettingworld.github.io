"""Generate optimized 640x360 Collage Punk marketplace covers for all 50 capsules."""

import hashlib
import json
from pathlib import Path
from PIL import Image, ImageOps

ARTIFACTS = Path("/Users/eric/.gemini/antigravity/brain/e8da5bd0-df25-4dcb-b9ab-ac91f0b0b605")
OUT_DIR = Path("web/static/covers")
OUT_DIR.mkdir(parents=True, exist_ok=True)

ART_POOL = {
    "agricultura": ARTIFACTS / "cover_agricultura_1794335962444.jpg",
    "hidroponia": ARTIFACTS / "cover_hidroponia_1794335977469.jpg",
    "medicina": ARTIFACTS / "cover_medicina_1794336004692.jpg",
    "ai_quantum": ARTIFACTS / "cover_ai_quantum_jpg_1794335994594.jpg",
    "geo": ARTIFACTS / "geo_punk_1794248725475.jpg",
    "cyber_mech": ARTIFACTS / "cyber_mechanic_punk_1794248740607.jpg",
    "bio": ARTIFACTS / "bio_punk_1794248758493.jpg",
    "anarcho": ARTIFACTS / "anarcho_social_punk_1794248779095.jpg",
    "hacker": ARTIFACTS / "hacker_punk_1794248823812.jpg",
}


def pick_art_key(cid: str) -> str:
    if any(k in cid for k in ("agricultura", "compostatge", "permacultura", "earth-agricultural")):
        return "agricultura"
    if any(k in cid for k in ("hidroponia", "control-de-plagas", "jardineria")):
        return "hidroponia"
    if any(k in cid for k in ("health-medicine", "medicina", "supervivencia")):
        return "medicina"
    if any(k in cid for k in ("inteligencia-artificial", "machine-learning", "cuantica", "criptografia", "seguridad", "blockchain")):
        return "ai_quantum"
    if any(k in cid for k in ("physics", "mathematics", "engineering", "practical-manuals", "automatizacion")):
        return "cyber_mech"
    if any(k in cid for k in ("chemistry", "biochemistry")):
        return "bio"
    if any(k in cid for k in ("filosofia", "politica", "economics", "historia", "ensayo", "tratado", "ciencia")):
        return "geo" if "historia" in cid else "anarcho"
    return "hacker"


def render_cover(src_path: Path, dest_path: Path, seed_str: str, is_exact_banner: bool = False) -> None:
    img = Image.open(src_path).convert("RGB")
    w, h = img.size

    if not is_exact_banner:
        # Subtle deterministic crop-pan/mirror per capsule so adjacent cards feel visually distinct
        digest = int(hashlib.sha256(seed_str.encode("utf-8")).hexdigest()[:8], 16)
        if digest % 3 == 1:
            img = ImageOps.mirror(img)
        zoom = 0.86 + ((digest >> 4) % 10) * 0.014  # 0.86..0.986
        cw, ch = int(w * zoom), int(h * zoom)
        max_x, max_y = max(0, w - cw), max(0, h - ch)
        ox = ((digest >> 8) % (max_x + 1)) if max_x else 0
        oy = ((digest >> 16) % (max_y + 1)) if max_y else 0
        img = img.crop((ox, oy, ox + cw, oy + ch))

    out = ImageOps.fit(img, (640, 360), method=Image.Resampling.LANCZOS)
    out.save(dest_path, format="JPEG", quality=86, optimize=True)


def main() -> None:
    catalog = json.loads(Path("web/static/catalog.json").read_text(encoding="utf-8"))
    catalogo_dir = Path("repos/catalogo/catalogs")

    for item in catalog:
        cid = item["id"]
        dest = OUT_DIR / f"{cid}.jpg"
        exact_banner = catalogo_dir / cid / "images" / "banner.png"
        if exact_banner.exists() and exact_banner.stat().st_size > 50_000:
            render_cover(exact_banner, dest, cid, is_exact_banner=True)
        else:
            key = pick_art_key(cid)
            render_cover(ART_POOL[key], dest, cid, is_exact_banner=False)

    total_kb = sum(p.stat().st_size for p in OUT_DIR.glob("*.jpg")) / 1024
    print(f"Generated {len(catalog)} Collage Punk covers in {OUT_DIR} ({total_kb:.1f} KB total)")


if __name__ == "__main__":
    main()

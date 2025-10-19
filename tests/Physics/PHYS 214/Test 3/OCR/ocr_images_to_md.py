import argparse, re
from pathlib import Path
from PIL import Image
import pytesseract

def group_by_key(images_dir: Path):
    groups = {}
    for img in sorted(images_dir.glob("*.png")):
        # Expect names like: "<stem>_p<page>.png"
        name = img.stem
        if "_p" in name:
            stem = name[: name.rfind("_p")]
        else:
            stem = name
        groups.setdefault(stem, []).append(img)
    return groups

def quick_tex_normalize(s: str) -> str:
    # Minimal safe normalizations; do NOT over-aggressively change text
    s = s.replace("−", "-").replace("×", "\\times").replace("·", "\\cdot")
    s = re.sub(r"10\s*\-\s*(\d+)", r"10^{-\1}", s)       # 10-5 -> 10^{-5}
    s = re.sub(r"10\^\s*\-\s*(\d+)", r"10^{-\1}", s)    # 10^-5 -> 10^{-5}
    s = re.sub(r"10\^(\d+)", r"10^{\1}", s)                # 10^6 -> 10^{6}
    return s

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--images-dir", required=True, type=Path)
    ap.add_argument("--out-dir", required=True, type=Path)
    ap.add_argument("--lang", default="eng")
    args = ap.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    groups = group_by_key(args.images_dir)

    for stem, imgs in groups.items():
        lines = [f"# {stem} — OCR Extract", ""]
        for img in sorted(imgs, key=lambda p: int(p.stem.split('_p')[-1])):
            im = Image.open(img)
            txt = pytesseract.image_to_string(im, lang=args.lang, config="--psm 6")
            txt = quick_tex_normalize(txt)
            lines.append(f"--- Page {img.name} ---")
            lines.append(txt.strip())
            lines.append("")
        out = args.out_dir / f"{stem} (OCR).md"
        out.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
        print(f"Wrote {out}")

if __name__ == "__main__":
    main()

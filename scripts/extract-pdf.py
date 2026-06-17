#!/usr/bin/env python3
"""Extract text summary + embedded images + page PNGs from a PDF."""
import sys
from pathlib import Path

try:
    import fitz
except ImportError:
    print("Install pymupdf: pip install pymupdf", file=sys.stderr)
    sys.exit(1)

pdf_path = Path(sys.argv[1])
out_dir = Path(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)
preview = out_dir / "preview"
preview.mkdir(exist_ok=True)

doc = fitz.open(pdf_path)
print(f"pages: {doc.page_count}")
for i, page in enumerate(doc):
    text = page.get_text().strip()
    print(f"\n--- page {i + 1} ---")
    print(text[:800] if text else "(no text)")
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    pix.save(str(preview / f"page-{i + 1:02d}.png"))
    for j, img in enumerate(page.get_images(full=True)):
        base = doc.extract_image(img[0])
        ext = base["ext"]
        fp = out_dir / f"page{i + 1:02d}-img{j + 1}.{ext}"
        fp.write_bytes(base["image"])
        print(f"  image: {fp.name} ({base['width']}x{base['height']})")

print(f"\nDone -> {out_dir}")

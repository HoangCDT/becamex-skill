#!/usr/bin/env python3
"""
Đóng gói slide Becamex thành 1 file HTML — nhúng ảnh nén dạng data URL (base64).

Usage:
  python3 bundle-html.py slide.html
  python3 bundle-html.py slide.html -o slide-standalone.html
  python3 bundle-html.py slide.html --quality 82 --max-width 1600
"""
from __future__ import annotations

import argparse
import base64
import io
import mimetypes
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SRC_HREF_RE = re.compile(
    r'(?P<attr>src|href)=(["\'])((?:\./)?becamex-assets/[^"\']+)\2',
    re.IGNORECASE,
)
CSS_URL_RE = re.compile(
    r'url\((["\']?)((?:\./)?becamex-assets/[^"\')\s]+)\1\)',
    re.IGNORECASE,
)

PNG_KEEP_NAMES = {"chevron.png", "becamex-logo.png", "cover-logo.png"}


def mime_for(path: Path, override: str | None = None) -> str:
    if override:
        return override
    guessed, _ = mimetypes.guess_type(path.name)
    if guessed:
        return guessed
    ext = path.suffix.lower()
    if ext == ".svg":
        return "image/svg+xml"
    return "application/octet-stream"


def compress_with_pillow(
    path: Path,
    max_width: int,
    jpeg_quality: int,
    force_png: bool,
) -> tuple[bytes, str] | None:
    try:
        from PIL import Image
    except ImportError:
        return None

    img = Image.open(path)
    if max_width > 0 and img.width > max_width:
        ratio = max_width / img.width
        img = img.resize((max_width, max(1, int(img.height * ratio))), Image.Resampling.LANCZOS)

    buf = io.BytesIO()
    name = path.name.lower()

    if force_png or path.suffix.lower() == ".png" and name in PNG_KEEP_NAMES:
        img.save(buf, format="PNG", optimize=True)
        return buf.getvalue(), "image/png"

    if img.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        alpha = img.convert("RGBA").split()[-1] if img.mode != "RGB" else None
        rgb = img.convert("RGBA")
        bg.paste(rgb, mask=alpha)
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")

    img.save(buf, format="JPEG", quality=jpeg_quality, optimize=True)
    return buf.getvalue(), "image/jpeg"


def compress_with_sips(path: Path, max_width: int, jpeg_quality: int, force_png: bool) -> tuple[bytes, str] | None:
    try:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            src = tmp_dir / path.name
            src.write_bytes(path.read_bytes())

            if max_width > 0:
                subprocess.run(
                    ["sips", "-Z", str(max_width), str(src)],
                    check=True,
                    capture_output=True,
                )

            if force_png or (path.suffix.lower() == ".png" and path.name.lower() in PNG_KEEP_NAMES):
                out = tmp_dir / "out.png"
                subprocess.run(["cp", str(src), str(out)], check=True, capture_output=True)
                return out.read_bytes(), "image/png"

            out = tmp_dir / "out.jpg"
            subprocess.run(
                ["sips", "-s", "format", "jpeg", "-s", "formatOptions", str(jpeg_quality), str(src), "--out", str(out)],
                check=True,
                capture_output=True,
            )
            return out.read_bytes(), "image/jpeg"
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None


def encode_asset(path: Path, max_width: int, jpeg_quality: int, no_compress: bool) -> tuple[bytes, str]:
    if no_compress or path.suffix.lower() == ".svg":
        return path.read_bytes(), mime_for(path)

    force_png = path.name.lower() in PNG_KEEP_NAMES
    compressed = compress_with_pillow(path, max_width, jpeg_quality, force_png)
    if compressed is None:
        compressed = compress_with_sips(path, max_width, jpeg_quality, force_png)
    if compressed is not None:
        return compressed

    return path.read_bytes(), mime_for(path)


def to_data_url(path: Path, max_width: int, jpeg_quality: int, no_compress: bool) -> str:
    data, mime = encode_asset(path, max_width, jpeg_quality, no_compress)
    payload = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{payload}"


def resolve_asset(rel: str, html_dir: Path, assets_dir: Path | None) -> Path | None:
    rel = rel.removeprefix("./")
    candidates = [html_dir / rel]
    if assets_dir is not None:
        suffix = rel.removeprefix("becamex-assets/").lstrip("/")
        candidates.append(assets_dir / suffix)
        candidates.append(assets_dir.parent / rel)
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    return None


def replace_asset_refs(
    html: str,
    html_dir: Path,
    assets_dir: Path | None,
    max_width: int,
    jpeg_quality: int,
    no_compress: bool,
) -> tuple[str, int, int, list[str]]:
    missing: list[str] = []
    count = 0
    saved_bytes = 0
    cache: dict[str, str] = {}

    def embed(rel: str) -> str | None:
        nonlocal count, saved_bytes
        if rel in cache:
            return cache[rel]
        path = resolve_asset(rel, html_dir, assets_dir)
        if path is None:
            missing.append(rel)
            return None
        original = path.stat().st_size
        data_url = to_data_url(path, max_width, jpeg_quality, no_compress)
        compressed = int(len(data_url) * 0.75)  # base64 ~33% overhead vs raw binary
        saved_bytes += max(0, original - compressed)
        count += 1
        cache[rel] = data_url
        return data_url

    def sub_src_href(match: re.Match[str]) -> str:
        attr = match.group("attr")
        quote = match.group(2)
        rel = match.group(3)
        url = embed(rel)
        if url is None:
            return match.group(0)
        return f'{attr}={quote}{url}{quote}'

    def sub_css_url(match: re.Match[str]) -> str:
        quote = match.group(1) or ""
        rel = match.group(2)
        url = embed(rel)
        if url is None:
            return match.group(0)
        q = quote or '"'
        return f"url({q}{url}{q})"

    html = SRC_HREF_RE.sub(sub_src_href, html)
    html = CSS_URL_RE.sub(sub_css_url, html)
    return html, count, saved_bytes, missing


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Nhúng becamex-assets vào HTML (1 file, ảnh nén base64)."
    )
    parser.add_argument("html", type=Path, help="File HTML nguồn")
    parser.add_argument("-o", "--output", type=Path, help="File HTML đích")
    parser.add_argument("--assets", type=Path, default=None, help="Thư mục becamex-assets")
    parser.add_argument(
        "--max-width",
        type=int,
        default=1600,
        help="Chiều rộng tối đa px (0 = không resize). Mặc định: 1600",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=82,
        help="JPEG quality 1-100. Mặc định: 82",
    )
    parser.add_argument(
        "--no-compress",
        action="store_true",
        help="Nhúng file gốc, không nén",
    )
    args = parser.parse_args()

    html_path = args.html.resolve()
    if not html_path.is_file():
        print(f"Không tìm thấy: {html_path}", file=sys.stderr)
        return 1

    html_dir = html_path.parent
    assets_dir = args.assets
    if assets_dir is None:
        default_assets = html_dir / "becamex-assets"
        assets_dir = default_assets if default_assets.is_dir() else None
    elif assets_dir.is_dir():
        assets_dir = assets_dir.resolve()

    out_path = args.output or html_dir / f"{html_path.stem}-standalone.html"
    out_path = out_path.resolve()

    html = html_path.read_text(encoding="utf-8")
    bundled, count, saved, missing = replace_asset_refs(
        html,
        html_dir,
        assets_dir,
        args.max_width,
        max(1, min(100, args.quality)),
        args.no_compress,
    )

    note = (
        f"standalone: {count} ảnh nhúng base64"
        + ("" if args.no_compress else f", nén max-width={args.max_width}, quality={args.quality}")
    )
    bundled = bundled.replace("</head>", f"  <!-- {note} -->\n</head>", 1)

    out_path.write_text(bundled, encoding="utf-8")
    size_mb = out_path.stat().st_size / (1024 * 1024)

    print(f"Đã nhúng {count} ảnh → {out_path}")
    print(f"Kích thước file: {size_mb:.2f} MB")
    if not args.no_compress and saved > 0:
        print(f"Ước tính tiết kiệm ảnh gốc: ~{saved / (1024 * 1024):.2f} MB")

    if missing:
        print(f"Cảnh báo: thiếu {len(missing)} file:", file=sys.stderr)
        for item in missing:
            print(f"  - {item}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

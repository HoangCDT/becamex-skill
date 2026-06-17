#!/usr/bin/env python3
"""Áp theme landing page lên deck Becamex (copy từ deck gốc)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

LANDING_CSS = """
    /* === LANDING PAGE THEME === */
    html.deck-landing .grid-lines { display: none; }
    html.deck-landing .slide::before { display: none; }

    html.deck-landing .landing-bg {
      position: absolute;
      inset: 0;
      z-index: 0;
      overflow: hidden;
      pointer-events: none;
    }
    html.deck-landing .landing-bg img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transform: scale(1.06);
      filter: saturate(1.08) contrast(1.02);
    }
    html.deck-landing .landing-bg::after {
      content: "";
      position: absolute;
      inset: 0;
      background:
        linear-gradient(118deg, rgba(255,255,255,0.94) 0%, rgba(255,252,250,0.88) 38%, rgba(255,248,245,0.82) 100%);
    }
    html.deck-landing .slide-cover .cover-bg {
      transform: scale(1.04);
      filter: saturate(1.05);
    }
    html.deck-landing .slide-cover::after {
      content: "";
      position: absolute;
      inset: 0;
      z-index: 1;
      background:
        linear-gradient(105deg, rgba(18,8,4,0.82) 0%, rgba(40,18,10,0.55) 40%, rgba(220,68,5,0.12) 72%, transparent 100%);
      pointer-events: none;
    }
    html.deck-landing .slide-cover .cover-content { width: min(58%, 640px); }
    html.deck-landing .cover-title { color: #fff; text-shadow: 0 2px 24px rgba(0,0,0,0.35); }
    html.deck-landing .cover-subtitle { color: rgba(255,255,255,0.92); }
    html.deck-landing .cover-org-line { color: rgba(255,255,255,0.88); }
    html.deck-landing .landing-hero-kicker {
      display: inline-block;
      margin: 0 0 0.65em;
      padding: 0.35em 0.85em;
      font-size: clamp(0.72rem, 1.2vw, 0.88rem);
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #fff;
      background: rgba(220,68,5,0.85);
      border-radius: 999px;
      box-shadow: 0 4px 20px rgba(220,68,5,0.35);
    }
    html.deck-landing .landing-hero-cta {
      margin-top: clamp(0.75rem, 2vh, 1.25rem);
      font-size: clamp(0.78rem, 1.15vw, 0.92rem);
      color: rgba(255,255,255,0.75);
    }

    html.deck-landing .slide-section .landing-bg::after {
      background:
        linear-gradient(135deg, rgba(105,42,91,0.88) 0%, rgba(220,68,5,0.78) 55%, rgba(34,16,8,0.72) 100%);
    }
    html.deck-landing .slide-section .section-title,
    html.deck-landing .slide-section .section-sub { color: #fff; }
    html.deck-landing .slide-section .section-tag {
      background: rgba(255,255,255,0.16);
      color: #fff;
      border-color: rgba(255,255,255,0.35);
    }

    html.deck-landing .slide-closing::after {
      content: "";
      position: absolute;
      inset: 0;
      z-index: 1;
      background: linear-gradient(180deg, rgba(18,8,4,0.55), rgba(18,8,4,0.72));
      pointer-events: none;
    }
    html.deck-landing .closing-title { color: #fff; text-shadow: 0 4px 32px rgba(0,0,0,0.4); }

    html.deck-landing .slide-content,
    html.deck-landing .section-inner,
    html.deck-landing .closing-content { position: relative; z-index: 2; }

    html.deck-landing .title-badge {
      background: rgba(255,255,255,0.92);
      backdrop-filter: blur(10px);
      box-shadow: 0 6px 24px rgba(220,68,5,0.12);
    }
    html.deck-landing .features .card,
    html.deck-landing .point-card {
      background: rgba(255,255,255,0.9);
      backdrop-filter: blur(10px);
      box-shadow: 0 10px 36px rgba(51,51,51,0.1);
      border-color: rgba(220,68,5,0.18);
    }
    html.deck-landing .slide-lead {
      background: rgba(255,255,255,0.72);
      backdrop-filter: blur(8px);
      padding: 0.55em 0.85em;
      border-radius: 10px;
      border-left: 3px solid var(--accent);
    }

    html.deck-landing .landing-showcase {
      position: absolute;
      z-index: 1;
      right: clamp(0.75rem, 2.5vw, 2.25rem);
      top: 50%;
      transform: translateY(-50%);
      width: min(38vw, 440px);
      border-radius: clamp(12px, 1.2vw, 18px);
      overflow: hidden;
      box-shadow: 0 28px 70px rgba(34,16,8,0.22);
      border: 3px solid rgba(255,255,255,0.92);
      pointer-events: none;
    }
    html.deck-landing .landing-showcase img {
      display: block;
      width: 100%;
      height: auto;
    }
    html.deck-landing .landing-showcase::before {
      content: "";
      position: absolute;
      inset: 0;
      border-radius: inherit;
      box-shadow: inset 0 0 0 1px rgba(255,255,255,0.35);
      pointer-events: none;
    }
    html.deck-landing #slide-context .slide-content,
    html.deck-landing #slide-content .slide-content,
    html.deck-landing #slide-benefits .slide-content,
    html.deck-landing #slide-scope .slide-content,
    html.deck-landing #slide-fast .slide-content {
      max-width: calc(100% - min(40vw, 460px));
    }
    html.deck-landing #slide-context .features,
    html.deck-landing #slide-content .features,
    html.deck-landing #slide-benefits .features,
    html.deck-landing #slide-scope .features {
      grid-template-columns: 1fr 1fr;
    }

    html.deck-landing .swimlane,
    html.deck-landing .integration-flow,
    html.deck-landing .dispatch-layout,
    html.deck-landing .module-grid {
      background: rgba(255,255,255,0.82);
      backdrop-filter: blur(10px);
      border-radius: clamp(10px, 1vw, 14px);
      padding: clamp(0.45rem, 0.9vw, 0.75rem);
      box-shadow: 0 12px 40px rgba(51,51,51,0.1);
    }
    html.deck-landing .module-card {
      box-shadow: 0 14px 42px rgba(34,16,8,0.14);
      border-radius: clamp(10px, 1vw, 14px);
    }
    html.deck-landing .image-stack img,
    html.deck-landing .module-shot img {
      border-radius: clamp(6px, 0.7vw, 10px);
    }
    html.deck-landing .toc-nav {
      background: rgba(255,255,255,0.82);
      backdrop-filter: blur(12px);
      border-radius: clamp(12px, 1.2vw, 16px);
      padding: clamp(0.75rem, 1.5vw, 1.15rem);
      box-shadow: 0 12px 40px rgba(51,51,51,0.1);
      border: 1px solid rgba(220,68,5,0.15);
    }

    html.deck-landing .slide-footer {
      background: rgba(255,255,255,0.72);
      backdrop-filter: blur(8px);
      padding: 0.35em 0.65em;
      border-radius: 999px;
      box-shadow: 0 4px 16px rgba(51,51,51,0.08);
    }

    @media (max-width: 960px) {
      html.deck-landing .landing-showcase {
        position: relative;
        right: auto;
        top: auto;
        transform: none;
        width: min(100%, 360px);
        margin: 0 auto clamp(0.5rem, 1vh, 0.75rem);
      }
      html.deck-landing #slide-context .slide-content,
      html.deck-landing #slide-content .slide-content,
      html.deck-landing #slide-benefits .slide-content,
      html.deck-landing #slide-scope .slide-content,
      html.deck-landing #slide-fast .slide-content {
        max-width: 100%;
      }
    }
"""

BACKGROUNDS = {
    "slide-toc": "becamex-assets/cover-bg.jpeg",
    "slide-context": "becamex-assets/pdf/page01-img1.jpeg",
    "slide-content": "becamex-assets/cover-slide-bg.jpeg",
    "slide-benefits": "becamex-assets/cover-bg.jpeg",
    "slide-scope": "becamex-assets/pdf/page01-img1.jpeg",
    "slide-flow": "becamex-assets/cover-bg.jpeg",
    "slide-fast": "becamex-assets/cover-slide-bg.jpeg",
    "slide-section-features": "becamex-assets/pdf/page08-img1.png",
    "slide-dispatch": "becamex-assets/pdf/page09-img1.png",
    "slide-driver": "becamex-assets/pdf/page11-img1.jpeg",
    "slide-supervisor-flow": "becamex-assets/pdf/page13-img1.jpeg",
    "slide-supervisor-flow-2": "becamex-assets/pdf/page14-img1.jpeg",
    "slide-roadmap": "becamex-assets/cover-bg.jpeg",
}

SHOWCASES = {
    "slide-context": "becamex-assets/pdf/page08-img1.png",
    "slide-content": "becamex-assets/pdf/page09-img1.png",
    "slide-benefits": "becamex-assets/pdf/page11-img2.jpeg",
    "slide-scope": "becamex-assets/pdf/page13-img2.jpeg",
    "slide-fast": "becamex-assets/pdf/page08-img1.png",
}


def inject_bg(html: str, slide_id: str, src: str) -> str:
    block = (
        f'  <section class="slide'
        if slide_id == "slide-section-features"
        else f'  <section class="slide" id="{slide_id}">'
    )
    if slide_id == "slide-section-features":
        pattern = r'(<section class="slide slide-section" id="slide-section-features">)\s*\n'
    else:
        pattern = rf'(<section class="slide[^"]*" id="{re.escape(slide_id)}">)\s*\n'

    layer = f'    <div class="landing-bg" aria-hidden="true"><img src="{src}" alt="" /></div>\n'
    return re.sub(pattern, rf"\1\n{layer}", html, count=1)


def inject_showcase(html: str, slide_id: str, src: str) -> str:
    tag = f'<aside class="landing-showcase reveal" aria-hidden="true"><img src="{src}" alt="" /></aside>'
    pattern = rf'(<section class="slide" id="{re.escape(slide_id)}">(?:\n    <div class="landing-bg"[^>]*>.*?</div>)?\n    <div class="grid-lines"></div>\n)'
    return re.sub(pattern, rf"\1    {tag}\n", html, count=1, flags=re.DOTALL)


def main() -> int:
    src = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    dst = Path(sys.argv[2] if len(sys.argv) > 2 else src.with_name(src.stem + "-landing.html"))
    html = src.read_text(encoding="utf-8")

    if "deck-landing" in html and "LANDING PAGE THEME" in html:
        print(f"Đã có theme landing: {dst}")
        return 0

    html = html.replace("<html lang=\"vi\">", '<html lang="vi" class="deck-landing">')
    html = html.replace(
        "<title>Giải pháp Quản lý Đội xe</title>",
        "<title>Giải pháp Quản lý Đội xe — Landing</title>",
    )
    html = html.replace(
        "const STORAGE_KEY = 'becamex-slide:'",
        "const STORAGE_KEY = 'becamex-slide-landing:'",
    )
    html = html.replace(
        "<div class=\"cover-main reveal\">",
        '<div class="cover-main reveal">\n        <p class="landing-hero-kicker">BECAMEX</p>',
    )
    html = html.replace(
        '<p class="cover-subtitle">Phụ đề slide bìa</p>',
        '<p class="cover-subtitle">Phụ đề slide bìa</p>\n        <p class="landing-hero-cta">Cuộn hoặc bấm Tiếp để khám phá →</p>',
    )

    html = html.replace("  </style>", f"{LANDING_CSS}\n  </style>", 1)

    for sid, img in BACKGROUNDS.items():
        html = inject_bg(html, sid, img)
    for sid, img in SHOWCASES.items():
        html = inject_showcase(html, sid, img)

    dst.write_text(html, encoding="utf-8")
    print(f"Landing deck → {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

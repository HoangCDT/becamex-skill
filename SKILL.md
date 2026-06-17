---
name: becamex-slide
description: >-
  Tạo slide HTML thương hiệu BECAMEX: design system (Mitr, cam #DC4405), layout bìa/nội dung,
  asset thương hiệu đính kèm, fullscreen, preview tile, xuất PDF. Dùng khi user cần slide/báo cáo
  BECAMEX, presentation HTML branded, hoặc nhắc becamex-slide.
---

# Becamex Slide

Skill tạo **presentation HTML** theo design system BECAMEX — không gắn một dự án cụ thể. Agent áp dụng **style + layout + hành động trình chiếu**; nội dung slide lấy từ user.

## Phạm vi skill

| Thuộc skill | Không thuộc skill |
|-------------|-------------------|
| Design tokens, CSS, layout slide | Nội dung nghiệp vụ từng dự án |
| Asset thương hiệu bundle (logo, chevron, nền bìa) | Screenshot/ảnh sản phẩm — user cung cấp |
| Nav, fullscreen, preview, PDF, localStorage | Logic backend / API |

**Không** dùng `frontend-slides` aesthetic tự do — luôn bám design system bên dưới.

## Cài đặt

```bash
bash scripts/install.sh all          # Cursor + Antigravity
bash scripts/install.sh cursor
bash scripts/install.sh antigravity
```

Clone: `git clone https://github.com/HoangCDT/becamex-skill.git` → `bash scripts/install.sh all`

## Tài nguyên đính kèm

| File | Vai trò |
|------|---------|
| `template/deck.html` | **Mẫu layout** — CSS, nav, script, các pattern slide (thay nội dung theo user) |
| `template/becamex-assets/` | 4 PNG thương hiệu — copy sang output |
| `scripts/copy-assets.sh` | Copy bundle → `{output}/becamex-assets/` |
| `scripts/bundle-html.py` | Đóng gói 1 file HTML (base64) |
| `scripts/extract-assets.sh` | Fallback: trích chevron + logo từ PPT |
| `scripts/extract-pdf.py` | Trích ảnh từ PDF |
| `reference.md` | CSS & markup chi tiết |
| `examples.md` | Ví dụ prompt → hành động agent |

**Khởi tạo deck:**
```bash
cp template/deck.html {output-dir}/index.html
bash scripts/copy-assets.sh {output-dir}
```

## Design system

| Token | Giá trị |
|-------|---------|
| Nền nội dung | `#FFFFFF` |
| Cam chính | `#DC4405` |
| Tím phụ | `#692A5B` |
| Peach / Lavender | `#EEAF92` / `#C9B6C3` |
| Chữ chính / phụ | `#333333` / `#989898` |
| Font | **Mitr** (Google Fonts) |

Chi tiết CSS: [reference.md](reference.md)

## Asset thương hiệu (bundle)

Luôn copy từ skill — **không** tự vẽ SVG, không tạo PNG bằng code:

```bash
bash scripts/copy-assets.sh {output-dir}
```

| File | Dùng cho |
|------|----------|
| `chevron.png` | Chevron trong `.title-badge` |
| `becamex-logo.png` | Logo footer / section |
| `cover-logo.png` | Logo góc trái slide bìa |
| `cover-slide-bg.png` | Nền slide bìa + slide **Cảm ơn!** |

Ghi đè `cover-slide-bg.png` / `cover-logo.png` chỉ khi user cung cấp file mới. Logo/chevron hợp lệ thường > 1 KB.

## Loại slide (layout pattern)

| Loại | Class | Khi dùng |
|------|-------|----------|
| Bìa | `slide slide-cover` | Slide 1 |
| Nội dung grid | `slide` + `.features` 2×2 | 2–4 điểm |
| Swimlane | `.swimlane` | Flow nhiều vai trò |
| Tích hợp hệ thống | `.integration-flow` + `.system-frame` | 2 hệ thống tương tác |
| Bước ngang | `.step-strip` | 4–6 bước quy trình |
| Waterfall + ảnh | `.waterfall` + `.image-stack` | Sơ đồ trái, ảnh phải |
| Ảnh giao diện | `.image-duo`, `.image-quad` | Screenshot user cung cấp |
| Phân cách | `slide slide-section` | Tiêu đề section, không footer số |
| Kết | `slide slide-closing` | Slide cuối — chỉ **Cảm ơn!** |

Mật độ tối đa: **1 tiêu đề + 4 card**, hoặc step-strip + ảnh. Nội dung dày → tách slide.

## Cấu trúc bắt buộc

- Một file `.html` + thư mục `becamex-assets/` cùng cấp
- Mọi slide: `100dvh`, `overflow: hidden` — **không scroll trong slide**
- Slide nội dung: `.title-badge` **cố định góc trái trên** (chevron PNG **bên trong** badge)
- Footer: số trang | vạch cam | logo PNG
- Slide kết: cùng `cover-slide-bg.png`, không footer số, đặt trước `.slide-nav`

## Hành động trình chiếu (bắt buộc mọi deck)

Copy CSS nav/overview + `<script>` từ `template/deck.html` hoặc [reference.md — Presentation mode](reference.md#presentation-mode).

| Hành động | Cách dùng |
|-----------|-----------|
| Chuyển slide | ← →, PageUp/PageDown |
| Toàn màn hình | Nút **Toàn màn hình** hoặc **F** |
| Preview tile | **⊞ Slides**, bấm indicator, hoặc **G** |
| Xuất PDF | Nút **PDF** (cả deck) — không chỉ Ctrl+P |
| Nhớ slide | `localStorage` key `becamex-slide:{filename}` |

## Workflow agent

```
- [ ] 1. Thu thập nội dung từ user (bìa, các slide, ảnh nếu có)
- [ ] 2. bash scripts/copy-assets.sh {output-dir}
- [ ] 3. cp template/deck.html → index.html (hoặc sửa deck có sẵn)
- [ ] 4. Chọn layout pattern; thay text/ảnh — không copy nội dung mẫu trong deck.html
- [ ] 5. Cập nhật số trang footer + slide kết
- [ ] 6. Kiểm tra viewport, nav, PDF
```

## Đóng gói 1 file

```bash
python3 scripts/bundle-html.py ./index.html -o ./standalone.html --quality 82 --max-width 1600
```

## Không làm

- Không font/theme generic (Inter, gradient AI slop)
- Không thay chevron/logo bằng SVG/text (trừ khi user yêu cầu)
- Không bỏ nav / fullscreen / preview / PDF
- Không hardcode nội dung một dự án cụ thể khi user không yêu cầu
- Không scroll trong `.slide`
- Không chèn slide sau `#slide-closing`

Chi tiết: [reference.md](reference.md) · [examples.md](examples.md) · [flowcharts.md](flowcharts.md)

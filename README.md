# Becamex Slide — Cursor Agent Skill

Skill tạo **slide HTML thương hiệu BECAMEX** (font Mitr, cam `#DC4405`, full viewport, thuyết trình fullscreen + preview tile).

## Cài đặt

### Cách 1 — Script (khuyến nghị)

```bash
cd /path/to/becamex-slide
bash scripts/install.sh all          # Cursor + Antigravity
bash scripts/install.sh cursor       # chỉ Cursor
bash scripts/install.sh antigravity  # chỉ Antigravity
```

- Cursor: `~/.cursor/skills/becamex-slide/`
- Antigravity: `~/.agent/skills/becamex-slide/`

Mở lại IDE hoặc chat mới để agent nhận skill.

### Cách 2 — Thủ công

```bash
mkdir -p ~/.cursor/skills
cp -R becamex-slide ~/.cursor/skills/
```

### Cách 4 — Clone từ GitHub

```bash
git clone https://github.com/caodinhtrihoang/becamex-slide.git
cd becamex-slide
bash scripts/install.sh all
```

### Cách 3 — Chia sẻ file zip

```bash
bash scripts/package.sh
# → dist/becamex-slide.zip
```

Giải nén, rồi chạy `bash scripts/install.sh` hoặc copy thư mục vào `~/.cursor/skills/`.

## Dùng với Cursor Agent

Trong chat, nhắc skill hoặc mô tả nhu cầu:

- *"Tạo slide Becamex cho báo cáo quản lý đội xe"*
- *"Thêm slide theo becamex-slide"*
- *"Làm deck HTML giống template BaoCaoKetQua"*

Agent sẽ đọc `SKILL.md` và làm theo design system.

## Chia sẻ 1 file HTML (không kèm thư mục ảnh)

Nhúng toàn bộ `becatruck-assets/` vào HTML dạng **base64**:

```bash
python3 scripts/bundle-html.py /path/to/slide.html -o slide-standalone.html
```

Gửi file `slide-standalone.html` — người nhận mở trực tiếp trên trình duyệt.

## Tạo deck mới (thủ công / tham khảo)

1. Copy mẫu HTML + assets thương hiệu:
   ```bash
   mkdir -p ~/Projects/my-deck
   cp ~/.cursor/skills/becamex-slide/template/deck.html ~/Projects/my-deck/index.html
   bash ~/.cursor/skills/becamex-slide/scripts/copy-assets.sh ~/Projects/my-deck
   ```

2. Mở `index.html` trong trình duyệt. Chi tiết asset: `template/assets/README.md`.

3. (Tùy chọn) Trích chevron + logo từ PPT khác — chỉ khi cần thay thế bundle:
   ```bash
   bash ~/.cursor/skills/becamex-slide/scripts/extract-assets.sh \
     /path/to/template.pptx \
     ~/Projects/my-deck/becatruck-assets
   ```

## Cấu trúc skill

```
becamex-slide/
├── SKILL.md           # Hướng dẫn chính cho agent
├── README.md          # Hướng dẫn cài đặt (file này)
├── reference.md       # CSS, markup chi tiết
├── examples.md        # Ví dụ input → output
├── flowcharts.md      # Swimlane / FAST
├── template/
│   ├── deck.html              # Deck mẫu đầy đủ (BecaTruck)
│   ├── becatruck-assets/      # 4 PNG thương hiệu chuẩn (chevron, logo, nền bìa)
│   └── assets/                # Hướng dẫn assets
└── scripts/
    ├── install.sh             # Cài vào Cursor / Antigravity
    ├── copy-assets.sh         # Copy PNG bundle sang output deck
    ├── package.sh             # Đóng gói zip
    ├── extract-assets.sh
    ├── extract-pdf.py
    └── bundle-html.py      # 1 file HTML standalone
```

## Tính năng deck mẫu

| Tính năng | Phím / thao tác |
|-----------|-----------------|
| Chuyển slide | ← →, PageUp/PageDown |
| Toàn màn hình | Nút **Toàn màn hình** hoặc **F** |
| Chọn slide (tile preview) | **⊞ Slides**, bấm `n/tổng`, hoặc **G** |
| Xuất PDF | Nút **PDF** hoặc **Ctrl+P** → Lưu dưới dạng PDF |
| Nhớ slide | Tự lưu `localStorage` theo tên file HTML |

## Yêu cầu

- **Cursor** với Agent Skills
- Trình duyệt hiện đại (Chrome, Edge, Safari)
- Tùy chọn: `unzip` (trích asset PPT), `python3` + `pymupdf` (trích PDF)

## Gỡ cài đặt

```bash
rm -rf ~/.cursor/skills/becamex-slide
```

## Bản quyền / nội bộ

Skill và template dùng cho **BECAMEX GROUP**. Logo, ảnh bìa, screenshot sản phẩm do đơn vị cung cấp — không phân phối asset thương hiệu ra ngoài khi chưa được phép.

# Becamex Slide — Agent Skill

Skill tạo **slide HTML thương hiệu BECAMEX**: design system, layout pattern, asset đính kèm, trình chiếu fullscreen + preview + PDF.

Không gắn một dự án — agent áp dụng style và hành động; nội dung lấy từ user.

## Cài đặt

### Clone GitHub (khuyến nghị)

```bash
git clone https://github.com/HoangCDT/becamex-skill.git
cd becamex-skill
bash scripts/install.sh all    # Cursor + Antigravity
```

Hoặc chỉ một IDE: `bash scripts/install.sh cursor` | `antigravity`

- Cursor: `~/.cursor/skills/becamex-slide/`
- Antigravity: `~/.agent/skills/becamex-slide/`

Mở lại IDE hoặc chat mới để agent nhận skill.

### Zip

```bash
bash scripts/package.sh   # → dist/becamex-slide.zip
```

## Dùng với Agent

Ví dụ prompt:

- *"Tạo slide BECAMEX cho báo cáo triển khai"*
- *"Thêm slide theo becamex-slide"*
- *"Deck HTML branded BECAMEX, 5 slide"*

## Tạo deck mới

```bash
mkdir -p ~/Projects/my-deck
cp template/deck.html ~/Projects/my-deck/index.html
bash scripts/copy-assets.sh ~/Projects/my-deck
```

Mở `index.html` trong trình duyệt. Thay nội dung text/ảnh — `deck.html` chỉ là **mẫu layout**.

## Cấu trúc

```
becamex-slide/
├── SKILL.md              # Hướng dẫn agent (design system + workflow)
├── reference.md          # CSS, markup chi tiết
├── examples.md           # Ví dụ prompt
├── template/
│   ├── deck.html         # Mẫu layout + nav + script
│   ├── becamex-assets/   # 4 PNG thương hiệu
│   └── assets/README.md
└── scripts/
    ├── install.sh
    ├── copy-assets.sh
    ├── bundle-html.py
    └── ...
```

## Tính năng trình chiếu

| Tính năng | Phím / thao tác |
|-----------|-----------------|
| Chuyển slide | ← →, PageUp/PageDown |
| Toàn màn hình | **F** hoặc nút trên nav |
| Chọn slide | **G**, **⊞ Slides**, bấm indicator |
| Xuất PDF | Nút **PDF** |
| Nhớ vị trí | Tự lưu theo tên file HTML |

## Standalone HTML

```bash
python3 scripts/bundle-html.py /path/to/index.html -o standalone.html
```

## Bản quyền

Asset thương hiệu BECAMEX — dùng nội bộ theo quy định đơn vị.

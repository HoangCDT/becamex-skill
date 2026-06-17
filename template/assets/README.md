# Assets cho deck Becamex

## Bundle thương hiệu (trong skill)

`template/becamex-assets/` — copy sang mọi deck output:

| File | Mô tả |
|------|--------|
| `chevron.png` | Chevron cam — header `.title-badge` |
| `becamex-logo.png` | Logo footer / section |
| `cover-logo.png` | Logo góc trái slide bìa |
| `cover-slide-bg.png` | Nền bìa + slide cảm ơn |

```bash
bash scripts/copy-assets.sh /path/to/output-deck
# → /path/to/output-deck/becamex-assets/
```

Logo/chevron hợp lệ thường > 1 KB. Không tự vẽ placeholder.

## Asset theo dự án (user cung cấp)

| Thư mục | Mô tả |
|---------|--------|
| `screenshots/` | Ảnh giao diện, sản phẩm |
| `pdf/` | Ảnh trích từ PDF (`scripts/extract-pdf.py`) |

## Đường dẫn HTML

```html
<img src="becamex-assets/chevron.png" alt="" />
<img src="becamex-assets/becamex-logo.png" alt="" />
```

## Fallback PPT

```bash
bash scripts/extract-assets.sh /path/to/template.pptx ./becamex-assets
```

Chỉ khi cần asset mới từ file PPT khác — mặc định dùng bundle skill.

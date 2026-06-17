# Assets cho deck Becamex

## Asset thương hiệu (đã có sẵn trong skill)

Skill đã **bundle sẵn** 4 file PNG chuẩn BECAMEX (deck truck management / BaoCaoKetQua) tại `template/becatruck-assets/`:

| File | Kích thước tham chiếu | Mô tả |
|------|----------------------|--------|
| `chevron.png` | ~4.5 KB | Chevron cam header — từ PPT `image4.png` |
| `becamex-logo.png` | ~92 KB | Logo footer / section — từ PPT `image7.png` |
| `cover-logo.png` | ~44 KB | Logo góc trái trên slide bìa |
| `cover-slide-bg.png` | ~1.2 MB | Nền slide bìa + slide cảm ơn (ảnh thật) |

Nếu file logo/chevron < 1 KB → **sai**, đã bị thay bằng placeholder — phải copy lại từ bundle skill.

**Luôn copy từ skill** — không tự vẽ SVG, không trích PPT trừ khi user yêu cầu thay thế:

```bash
bash scripts/copy-assets.sh /path/to/output-deck
# → tạo /path/to/output-deck/becatruck-assets/ với 4 file trên
```

Hoặc thủ công:

```bash
cp -R template/becatruck-assets /path/to/output-deck/
```

Chỉ thay file khi user **cung cấp ảnh bìa/logo mới** — khi đó ghi đè `cover-slide-bg.png` hoặc `cover-logo.png`.

## Asset bổ sung (tùy deck)

| File | Mô tả |
|------|--------|
| `pdf/*.jpeg` | Screenshot giao diện — trích bằng `scripts/extract-pdf.py` |
| `screenshots/*` | Ảnh sản phẩm do user cung cấp |

## Trích từ PPT (fallback, không khuyến nghị)

Chỉ dùng khi skill chưa cài hoặc cần asset mới từ file PPT khác:

```bash
bash scripts/extract-assets.sh /path/to/template.pptx ./becatruck-assets
```

## Đường dẫn trong HTML

Luôn dùng đường dẫn tương đối:

```html
<img src="becatruck-assets/chevron.png" alt="" />
<img src="becatruck-assets/cover-slide-bg.png" alt="" />
<img src="becatruck-assets/cover-logo.png" alt="" />
<img src="becatruck-assets/becamex-logo.png" alt="" />
```

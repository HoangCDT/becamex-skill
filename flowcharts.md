# Becamex Slide — Flowchart / sơ đồ luồng

## Nguyên tắc

- **Screenshot** sản phẩm → file riêng trong `becamex-assets/screenshots/` hoặc `pdf/`
- **Flowchart** (swimlane, tích hợp, bước nghiệp vụ) → vẽ lại HTML/CSS, không chụp ảnh flow (khó scale)
- **Khung flow** → `height: auto`, ôm nội dung; slide full màn hình, không giãn khung rỗng
- **Mũi tên ngang** → `align-self: start`, căn theo header lane/system

## Layout pattern

| Loại | Class HTML | Khi dùng |
|------|------------|----------|
| Swimlane | `.swimlane` + `.lane` | 3+ vai trò song song |
| Tích hợp 2 hệ thống | `.integration-flow` + `.system-frame` | Trao đổi dữ liệu A ↔ B |
| Bước ngang | `.step-strip` | 4–6 bước tuần tự |

Markup mẫu: [reference.md](reference.md) · `template/deck.html`

## Trích ảnh từ PDF

```bash
python3 scripts/extract-pdf.py /path/to/document.pdf ./becamex-assets/pdf
```

Dùng ảnh trích cho `.image-duo` / `.image-quad` — không thay flowchart HTML.

## Phương án khác (tùy chọn)

1. **Mermaid** + theme cam/tím
2. **SVG** thủ công — pixel-perfect
3. **draw.io** → export SVG vào `becamex-assets/diagrams/`

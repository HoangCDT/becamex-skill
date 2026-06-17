# Becamex Slide — Flowchart / sơ đồ luồng

## Nguyên tắc

- **Ảnh screenshot** từ PDF/PPT → giữ nguyên file trong `becatruck-assets/pdf/`
- **Flowchart** (swimlane, FAST, bước nghiệp vụ) → vẽ lại bằng HTML/CSS trong slide, không chụp ảnh flow từ PDF (dễ vỡ layout, khó scale)
- **Khung flow** (`.lane`, `.system-frame`, `.flow-box`) → `height: auto`, ôm theo nội dung; slide full màn hình nhưng không giãn ép khung rỗng (xem SKILL.md)
- **Mũi tên ngang** (`.lane-arrow`, `.integration-arrow`) → `align-self: start`, `min-height` khớp header (`.lane-head` / `.system-head`), không căn giữa cột

## Phương án vẽ lại (đã áp dụng trong mẫu)

| Loại | Class HTML | Nguồn nội dung |
|------|------------|----------------|
| Swimlane 3 vai trò | `.swimlane` + `.lane` | PDF p.4, 7, 10 — Điều xe / Tài xế / Giám sát |
| Luồng FAST (2 hệ thống) | `.integration-flow` + `.system-frame` | PDF p.5 — BecaTruck kết xuất → FAST import |
| Bước ngang (4–6 bước) | `.step-strip` | PDF p.11, 13–14 |

Logic tham chiếu Python: `~/Projects/beca-truck-slides/build_pptx.py` (`draw_swimlane`, `draw_fast_integration`, `draw_step_flow`).

## Phương án thay thế (khi cần nâng cấp)

1. **Mermaid** (inline trong HTML + CDN nhẹ) — nhanh cho flow đơn giản; cần theme cam/tím tùy chỉnh
2. **SVG thủ công** — kiểm soát pixel-perfect, phù hợp slide in/PDF
3. **draw.io / diagrams.net** — export SVG vào `becatruck-assets/diagrams/` nếu flow phức tạp
4. **`build_pptx.py`** — tái dùng cho xuất PowerPoint; HTML mirror cùng cấu trúc node

## Trích ảnh từ PDF

```bash
/Users/caodinhtrihoang/Projects/beca-truck-slides/.venv/bin/python3 \
  ~/.cursor/skills/becamex-slide/scripts/extract-pdf.py \
  "/path/to/BaoCaoKetQua_PhanHeQLDoiXe_20250620.pdf" \
  "./becatruck-assets/pdf"
```

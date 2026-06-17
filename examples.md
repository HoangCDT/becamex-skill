# Becamex Slide — Examples

## Ví dụ 1: Deck mới từ bullet points

**User input:**

```
Bìa:
- HỆ THỐNG QUẢN LÝ ĐỘI XE THI CÔNG
- Giải pháp số hóa vận hành đội xe
- BECAMEX GROUP / Trung tâm chuyển đổi số

Slide 2 — 4 tính năng:
1. Số hóa toàn trình: lập lệnh → chuyến → giám sát → chi phí
2. GPS & hành trình: theo dõi từng phiếu xe
3. App + Web: tài xế / điều xe / kế toán
4. Tích hợp FAST: chi phí và lương

Ảnh bìa: ~/Desktop/Screenshot 2026-06-09 at 16.42.00.png
Output: ~/Desktop/slide-quan-ly-doi-xe.html
```

**Agent làm:**

1. `bash scripts/copy-assets.sh {output-dir}` → chevron, logo, nền bìa chuẩn
2. Nếu user đưa ảnh bìa riêng → ghi đè `becatruck-assets/cover-slide-bg.png`
3. Sinh HTML với header `.title-badge` cố định góc trái trên; layout full `100dvh`, card/flow theo nội dung
4. Footer slide 2: số `2`
5. Nav: Trước/Tiếp + **⊞ Slides (G)** + **Toàn màn hình (F)** + **PDF**
6. Slide cuối: `.slide-closing` + **Cảm ơn!** + nền `cover-slide-bg.png`

---

## Ví dụ 2: Thêm slide vào deck có sẵn

**User input:**

```
Thêm slide 3: Kết quả triển khai
- 45 xe đã số hóa
- 100% chuyến có GPS
- Giảm 30% thời gian đối soát
```

**Agent làm:**

1. Đọc HTML hiện tại, đếm slide
2. Nếu ≤4 bullet → 1 slide grid hoặc list; nếu >4 → tách
3. Chèn section mới, footer `3`, cập nhật indicator nav `1 / 3`

---

## Ví dụ 3: Chỉ đổi nội dung, giữ design

**User input:**

```
Đổi tiêu đề bìa thành "PHÂN HỆ QUẢN LÝ VẬT TƯ"
Giữ nguyên layout và ảnh nền
```

**Agent làm:** Chỉ sửa text trong `.cover-title` / `.cover-subtitle`. Không đổi CSS, asset, nav.

---

## Ví dụ 5: Slide kết

**Chuẩn mọi deck** — slide cuối, trước `.slide-nav`:

```html
<section class="slide slide-closing" id="slide-closing">
  <img class="cover-bg" src="becatruck-assets/cover-slide-bg.png" alt="" />
  <div class="closing-content">
    <h2 class="closing-title reveal">Cảm ơn!</h2>
  </div>
</section>
```

- Dùng **cùng ảnh nền** với slide bìa
- Không footer số, không title-badge
- Không thêm dòng org (Becamex Group…) trừ khi user yêu cầu

---

## Ví dụ 4: Từ PPT template

**User input:**

```
Làm slide HTML theo slide 3 của BaoCaoKetQua_PhanHeQLDoiXe.pptx
```

**Agent làm:**

1. Trích text slide 3 bằng python (reference.md)
2. Map sang layout content 2×2 nếu có 4 khối nội dung
3. Giữ brand assets từ cùng file PPT

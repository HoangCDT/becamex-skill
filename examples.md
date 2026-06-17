# Becamex Slide — Examples

## Ví dụ 1: Deck mới từ bullet points

**User input:**

```
Bìa:
- HỆ THỐNG QUẢN LÝ XYZ
- Giải pháp số hóa
- BECAMEX GROUP / Đơn vị triển khai

Slide 2 — 4 điểm chính:
1. ...
2. ...
3. ...
4. ...

Output: ~/Projects/my-deck/index.html
```

**Agent làm:**

1. `bash scripts/copy-assets.sh {output-dir}`
2. `cp template/deck.html` → output; thay text theo user
3. Header `.title-badge` góc trái trên; grid 2×2 nếu 4 điểm
4. Nav đầy đủ + slide kết **Cảm ơn!**

---

## Ví dụ 2: Thêm slide vào deck có sẵn

**User:** *"Thêm slide Kết quả: 3 bullet"*

1. Đọc HTML, đếm slide
2. Chèn `<section class="slide">` trước `#slide-closing`
3. Cập nhật số footer + indicator

---

## Ví dụ 3: Chỉ đổi text, giữ design

**User:** *"Đổi tiêu đề bìa, giữ layout"*

Chỉ sửa `.cover-title` / `.cover-subtitle` — không đổi CSS hay asset.

---

## Ví dụ 4: Ảnh bìa tùy chỉnh

**User:** cung cấp `~/Pictures/cover.jpg`

```bash
cp ~/Pictures/cover.jpg {output-dir}/becamex-assets/cover-slide-bg.png
```

Giữ chevron + logo từ bundle skill.

---

## Ví dụ 5: Slide kết (mọi deck)

```html
<section class="slide slide-closing" id="slide-closing">
  <img class="cover-bg" src="becamex-assets/cover-slide-bg.png" alt="" />
  <div class="closing-content">
    <h2 class="closing-title reveal">Cảm ơn!</h2>
  </div>
</section>
```

Đặt trước `<nav class="slide-nav">`.

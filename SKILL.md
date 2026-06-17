---
name: becamex-slide
description: >-
  Tạo slide HTML thương hiệu BECAMEX (font Mitr, màu cam #DC4405, layout bìa + nội dung)
  từ nội dung người dùng cung cấp. Dùng khi user yêu cầu slide Becamex, báo cáo BECAMEX,
  BecaTruck, phân hệ quản lý đội xe, thuyết trình fullscreen, preview chọn slide, xuất PDF,
  hoặc nhắc becamex-slide / template BaoCaoKetQua.
---

# Becamex Slide

Tạo presentation HTML một file, zero-dependency, theo template **BaoCaoKetQua_PhanHeQLDoiXe.pptx**.

## Cài đặt skill (người dùng mới)

```bash
bash scripts/install.sh all          # Cursor + Antigravity
bash scripts/install.sh cursor       # ~/.cursor/skills/becamex-slide/
bash scripts/install.sh antigravity  # ~/.agent/skills/becamex-slide/
# hoặc: bash scripts/package.sh → chia sẻ dist/becamex-slide.zip
```

Chi tiết: [README.md](README.md)

## File mẫu trong skill

| File | Vai trò |
|------|---------|
| `template/deck.html` | Deck HTML đầy đủ — **copy làm điểm bắt đầu** |
| `template/becatruck-assets/` | **4 PNG thương hiệu chuẩn** (chevron, logo, nền bìa) — copy sang output |
| `template/assets/README.md` | Danh sách asset |
| `scripts/copy-assets.sh` | Copy 4 PNG bundle vào `{output-dir}/becatruck-assets/` |
| `scripts/extract-assets.sh` | Fallback: trích chevron + logo từ PPT |
| `scripts/extract-pdf.py` | Trích ảnh/screenshot từ PDF |
| `scripts/bundle-html.py` | Đóng gói 1 file HTML (ảnh nhúng base64) |

**Mẫu chuẩn khi code:** `template/deck.html` + `bash scripts/copy-assets.sh {output-dir}`

## Khi nào dùng skill này

- User đưa bullet points, tiêu đề, mô tả tính năng → cần slide HTML Becamex
- User muốn thêm/sửa slide trong deck hiện có
- User nhắc template PPT BecaTruck / BECAMEX GROUP

**Không** dùng `frontend-slides` aesthetic tự do — luôn bám design system Becamex bên dưới.

## Workflow

```
- [ ] 1. Thu thập nội dung (tiêu đề bìa, phụ đề, đơn vị, các slide nội dung)
- [ ] 2. Copy assets thương hiệu: `bash scripts/copy-assets.sh {output-dir}`
- [ ] 3. Chọn loại slide cho từng phần nội dung
- [ ] 4. Sinh HTML + cập nhật số trang footer
- [ ] 5. Thêm nav Trước/Tiếp + **Toàn màn hình** + **Preview slide** + **Xuất PDF** + phím tắt
- [ ] 6. Mở file trong trình duyệt kiểm tra viewport (100vh, không scroll trong slide)
```

### Bước 1 — Nội dung từ user

Hỏi hoặc suy ra từ prompt:

| Trường | Slide bìa |
|--------|-----------|
| Tiêu đề chính | 1–2 dòng IN HOA, cam |
| Phụ đề | 1 dòng, trắng |
| Đơn vị | VD: BECAMEX GROUP / Trung tâm chuyển đổi số |

Mỗi **slide nội dung** cần: tiêu đề section + danh sách điểm (ưu tiên 4 mục cho grid 2×2).

Nội dung quá dày → tách slide, không cuộn trong 1 slide.

### Bước 2 — Assets thương hiệu (bắt buộc)

Skill **đã bundle sẵn** 4 PNG chuẩn từ deck **BecaTruck / BaoCaoKetQua** tại `template/becatruck-assets/` (nguồn gốc: `Desktop/becatruck-assets/` — trích từ PPT + ảnh bìa thật). **Luôn copy sang output**:

```bash
bash scripts/copy-assets.sh {output-dir}
# → {output-dir}/becatruck-assets/
```

| File | Vai trò |
|------|--------|
| `chevron.png` | Chevron cam trong `.title-badge` |
| `becamex-logo.png` | Logo footer mọi slide nội dung |
| `cover-logo.png` | Logo góc trái trên slide bìa |
| `cover-slide-bg.png` | Nền slide bìa + slide **Cảm ơn!** |

**Quy tắc:**
- Mặc định dùng **đúng 4 file bundle** — không tự vẽ SVG, không tạo PNG bằng code, không dùng placeholder
- Không lấy asset từ slide khác (VD `yeu-cau-du-lieu-trien-khai`) nếu file nhỏ bất thường (< 1KB cho logo/chevron)
- Chỉ ghi đè `cover-slide-bg.png` hoặc `cover-logo.png` khi user **cung cấp file mới** rõ ràng
- Fallback trích PPT (khi không có skill): `scripts/extract-assets.sh /path/to/template.pptx ./becatruck-assets`

### Bước 3 — Loại slide

| Loại | Class | Khi dùng |
|------|-------|----------|
| Bìa | `slide slide-cover` | Luôn slide 1 |
| Nội dung grid | `slide` + `.features` 2×2 | 2–4 điểm có icon + mô tả |
| Swimlane | `.swimlane` | Flow 3 vai trò — **vẽ lại HTML** |
| Tích hợp FAST | `.integration-flow` + `.system-frame` | 2 hệ thống tương tác — **vẽ lại HTML** |
| Bước ngang | `.step-strip` | 4–6 bước quy trình |
| Ảnh giao diện | `.image-duo`, `.image-quad` | Screenshot từ PDF/PPT — **giữ file gốc** |
| Điều xe (waterfall) | `.waterfall` + `.image-stack` | Waterfall trái; 2 ảnh dọc phải (lập lệnh → chi tiết) |
| Phân cách | `slide slide-section` | Tiêu đề section, không footer |
| Kết | `slide slide-closing` | **Luôn slide cuối** — xem [Slide kết](#slide-kết-cảm-ơn) |

**Deck giới thiệu KH** (sau slide 1–4): Phạm vi → Luồng nghiệp vụ → FAST → Section → Module Điều xe/Tài xế/Giám sát (ảnh + chức năng) → **Slide kết**. Tham chiếu `build_intro_pptx.py` và PDF `BaoCaoKetQua_PhanHeQLDoiXe_20250620.pdf`.

Trích PDF: `scripts/extract-pdf.py`. Flowchart: xem [flowcharts.md](flowcharts.md).

Mật độ tối đa mỗi slide nội dung: **1 tiêu đề + 4 card** (grid 2×2), hoặc **step-strip + ảnh** trên cùng slide.

### Bước 4 — Cấu trúc HTML

- Deck mới:
  ```bash
  cp template/deck.html {output-dir}/index.html
  bash scripts/copy-assets.sh {output-dir}
  ```
- Một file `.html` + thư mục `becatruck-assets/` cùng cấp
- Font: Google Fonts **Mitr**
- Màu & CSS: copy từ mẫu chuẩn — chi tiết trong [reference.md](reference.md)
- Slide bìa: `cover-slide-bg.png` + `cover-logo.png` cố định góc trái trên (`position: absolute`)
- Mọi slide nội dung: header `.title-badge` (chevron **bên trong** badge + tiêu đề cam), footer phải (số trang | vạch cam | logo PNG)
- **Không** dùng badge nhỏ + title đen tách dòng; **không** chấm bullet trước tiêu đề
- Dùng **4 PNG bundle** (`scripts/copy-assets.sh`) cho chevron và logo — không thay bằng SVG/text
- **Slide kết:** đặt sau mọi slide nội dung, trước `.slide-nav`; dùng chung `cover-slide-bg.png` với bìa

## Slide kết (Cảm ơn)

**Luôn là slide cuối cùng** trong deck — không footer số trang, không title-badge.

| Quy tắc | Chi tiết |
|---------|----------|
| Class | `slide slide-closing` |
| Nền | **Cùng ảnh** `becatruck-assets/cover-slide-bg.png` như slide bìa (class `.cover-bg`) |
| Nội dung | Chỉ **Cảm ơn!** — `.closing-title`, căn giữa |
| Không có | Footer số trang, logo org, phụ đề dài, grid-lines |
| Vị trí HTML | Sau slide nội dung cuối, **trước** `<nav class="slide-nav">` |
| Preview tile | Label tile: **Cảm ơn** (trong `getSlideLabel`) |

Markup và CSS: [reference.md — Slide kết](reference.md#slide-kết-cảm-ơn).

```html
<section class="slide slide-closing" id="slide-closing">
  <img class="cover-bg" src="becatruck-assets/cover-slide-bg.png" alt="" />
  <div class="closing-content">
    <h2 class="closing-title reveal">Cảm ơn!</h2>
  </div>
</section>
```

**Không** thêm dòng phụ (VD: Becamex Group, Trung tâm chuyển đổi số) trừ khi user yêu cầu rõ.

## Viewport full màn hình (bắt buộc)

Mỗi slide chiếm **toàn bộ viewport** — không scroll trong slide.

| Quy tắc | CSS / hành vi |
|---------|----------------|
| Kích thước slide | `width: 100vw; height: 100dvh; overflow: hidden` |
| Snap cuộn | `scroll-snap-type: y mandatory` trên `html` |
| Nội dung slide | `.slide-content { flex: 1; width: 100%; justify-content: center }` |
| Padding | `--slide-padding-x/y/bottom` — dùng `clamp()`, có breakpoint `max-height` và `max-width` |
| Không giới hạn width | **Không** dùng `max-width: 1100px` trên grid/ảnh — full chiều ngang slide |
| Ảnh screenshot | `max-height: min(calc(100dvh - 13rem), 640px)` — lớn nhưng không tràn slide |
| Responsive | ≤900px: swimlane/FAST xếp dọc, ảnh 4 cột → 2; ≤700px: grid → 1 cột; ≤520px: step → 1 cột |

Chi tiết CSS: [reference.md — Viewport & content layout](reference.md#viewport--content-layout)

## Title badge — góc trái trên (bắt buộc)

**Mọi slide nội dung** (trừ bìa, section, closing): `.title-badge` **luôn cố định góc trái trên**, không cuộn theo khối nội dung giữa slide.

```html
<div class="slide-content">
  <header class="header">
    <div class="title-row reveal">
      <h1 class="title-badge">
        <img class="title-chevron" src="becatruck-assets/chevron.png" alt="" />
        Tiêu đề slide
      </h1>
    </div>
  </header>
  <!-- features / swimlane / ảnh ... -->
</div>
```

| Quy tắc | Chi tiết |
|---------|----------|
| Vị trí | `position: absolute` trên `.header`; `top/left` = `--slide-padding-y/x` |
| Chừa chỗ | `.slide-content { padding-top: calc(var(--slide-padding-y) + var(--title-badge-offset)) }` |
| Chevron | **Bên trong** badge, file PNG `chevron.png` |
| Style | Chữ cam, nền cam nhạt, `border-radius` nhỏ — **không** pill, **không** chấm bullet |
| Mobile | Tăng `--title-badge-offset` khi title xuống 2 dòng (`max-width: 600px`) |

**Không áp dụng** cho: `.slide-cover`, `.slide-section`, `.slide-closing`.

## Content — khung theo nội dung (bắt buộc)

Slide full màn hình, nhưng **frame/border/card bên trong ôm theo nội dung** — không giãn ép chiều cao.

| Thành phần | Hành vi |
|------------|---------|
| `.features`, `.card` | `height: auto`; grid `rows: auto` — card co theo text |
| `.swimlane`, `.lane`, `.integration-flow`, `.system-frame` | `align-items: start`; `height: auto` — khung theo số dòng |
| `.flow-box`, `.step-box`, `.system-action` | Padding + font lớn (`--body-size` ~0.88–1.22rem) |
| `.step-strip` | `flex-shrink: 0` — dải bước không giãn |
| `.image-duo`, `.image-quad` | `flex: 1` — dùng không gian còn lại; ảnh `width/height: auto`, khung ôm tỷ lệ |
| Khối chính | Căn giữa dọc trong vùng dưới title (`justify-content: center` trên `.slide-content`) |

**Font nội dung:** ưu tiên `--body-size`, `--h3-size` lớn (clamp theo vw/vh) — đọc rõ khi trình chiếu.

### Bước 5 — Điều hướng & thuyết trình

Mọi deck **bắt buộc** có thanh `.slide-nav` + popup `#slide-overview`. Copy **toàn bộ** CSS nav/overview + `<script>` từ mẫu chuẩn — chi tiết: [reference.md — Presentation mode](reference.md#presentation-mode).

#### Thanh điều hướng (luôn hiện)

| Thành phần | ID / class | Hành vi |
|------------|------------|---------|
| ← Trước | `#btn-prev` | Slide trước |
| Indicator | `#slide-indicator` | `n / tổng` |
| Tiếp → | `#btn-next` | Slide tiếp |
| Toàn màn hình | `#btn-fullscreen` `.slide-nav-fullscreen` | Vào/thoát fullscreen |
| Xuất PDF | `#btn-export-pdf` `.slide-nav-export` | Mở hộp thoại in → **Lưu dưới dạng PDF** |

**Phím:** `ArrowLeft/Right`, `PageUp/PageDown` chuyển slide · **F** fullscreen · **Ctrl+P** / **⌘P** xuất PDF.

#### Chế độ fullscreen

- Gọi `requestFullscreen()` trên `document.documentElement` (prefix `webkit` cho Safari).
- Khi fullscreen: thêm class `is-presentation-fullscreen` lên `<html>`; nút đổi label **Thoát** / icon **⤢**.
- Thoát fullscreen: nút, phím **F**, hoặc **Esc** (trình duyệt).

#### Preview chọn slide (luôn hiện)

Nút **⊞ Slides** (`#btn-goto`) luôn có trên thanh nav — không phụ thuộc fullscreen.

| Cách mở popup | |
|---------------|--|
| Nút **⊞ Slides** | `#btn-goto` |
| Bấm indicator | `#slide-indicator` (gạch chân, `title="Chọn slide (G)"`) |
| Phím **G** | Mọi lúc |

Popup `#slide-overview`:

- Lưới **tile preview** — clone từng `.slide`, scale từ khung 1280×720.
- Mỗi tile: thumbnail + `số. tên slide` (lấy từ `.title-badge`, `.section-title`, hoặc Bìa/Cảm ơn).
- Tile hiện tại: class `.is-current` (viền cam).
- Bấm tile → `goToSlide(index)` + đóng popup.
- Đóng popup: **Esc** (ưu tiên trước Esc thoát fullscreen), nút **Đóng**, click backdrop.
- Khi popup mở: phím mũi tên **không** chuyển slide.

#### Xuất PDF

Zero-dependency — **snapshot clone** + Print API (không override CSS từng slide):

- Nút **PDF** → chụp từng slide đúng kích thước viewport hiện tại → `#print-root` → in
- Mỗi trang **297×167mm** (16:9), scale đồng nhất — layout khớp màn hình
- User chọn **Lưu dưới dạng PDF** + bật **Background graphics**
- **Ctrl+P** chỉ in trang hiện tại — dùng nút **PDF** để xuất cả deck

Chi tiết: [reference.md — PDF export](reference.md#pdf-export).

#### Nhớ vị trí slide

`localStorage` key `becamex-slide:{filename}` — refresh mở lại đúng slide (`scrollIntoView` instant lần đầu).

### Bước 6 — Kiểm tra

- [ ] `height: 100vh` / `100dvh`, `overflow: hidden` trên `.slide`
- [ ] `.title-badge` cố định góc trái trên (absolute), nội dung không đè title
- [ ] Frame/card/flow-box `height: auto` — không giãn ép full chiều cao
- [ ] Font size dùng `clamp()`, `--body-size` đủ lớn cho trình chiếu
- [ ] Ảnh `object-fit: contain`, khung ôm tỷ lệ, không vượt viewport
- [ ] Số trang footer khớp thứ tự slide (bìa / section / closing không footer số)
- [ ] Slide kết: nền `cover-slide-bg.png`, chỉ **Cảm ơn!**, đặt cuối deck trước nav
- [ ] Đường dẫn asset tương đối `becatruck-assets/...`
- [ ] Responsive: thu nhỏ cửa sổ / xoay mobile — layout không vỡ
- [ ] Nav có nút **Toàn màn hình** + phím **F** hoạt động
- [ ] Popup **Chọn slide** (tile preview) — **G**, nút Slides, hoặc bấm indicator
- [ ] **Xuất PDF** — nút PDF hoặc Ctrl+P; mỗi slide 1 trang landscape
- [ ] `prefers-reduced-motion` có trong CSS

## Design system (tóm tắt)

| Token | Giá trị |
|-------|---------|
| Nền nội dung | `#FFFFFF` |
| Cam chính | `#DC4405` |
| Tím phụ | `#692A5B` |
| Chữ chính / phụ | `#333333` / `#989898` |
| Font | Mitr |

Chi tiết CSS, markup từng block: [reference.md](reference.md)

## Ví dụ input → output

Xem [examples.md](examples.md)

## Chia sẻ 1 file HTML duy nhất

Khi dev: giữ `deck.html` + `becatruck-assets/` (dễ sửa). Khi **gửi cho người khác**: đóng gói thành 1 file.

### Cách làm: Data URL (base64)

Ảnh được nhúng trực tiếp vào HTML:

```html
<img src="data:image/png;base64,iVBORw0KGgo..." alt="" />
```

Không cần thư mục `becatruck-assets/` — mở file bằng trình duyệt (double-click hoặc kéo thả).

### Script đóng gói

```bash
python3 ~/.cursor/skills/becamex-slide/scripts/bundle-html.py \
  ./slide-quan-ly-doi-xe.html \
  -o ./slide-quan-ly-doi-xe-standalone.html \
  --quality 82 --max-width 1600
```

| Tùy chọn | Ý nghĩa |
|----------|---------|
| `-o FILE` | Tên file output (mặc định: `*-standalone.html`) |
| `--assets DIR` | Thư mục assets nếu không nằm cạnh HTML |
| `--quality N` | JPEG quality 1–100 (mặc định 82) |
| `--max-width N` | Resize ảnh rộng hơn N px (mặc định 1600; 0 = không resize) |
| `--no-compress` | Nhúng file gốc, không nén |

Ảnh logo/chevron giữ PNG (trong suốt); screenshot chuyển JPEG nén. Dùng Pillow nếu có, fallback `sips` trên macOS.

**Lưu ý:** File standalone ~5–8 MB sau nén (14 slide + screenshot). Font Google (Mitr) vẫn tải từ mạng — offline hoàn toàn cần nhúng thêm `@font-face` (tùy chọn).

**Không** chỉnh tay từng ảnh — luôn dùng script sau khi sửa deck + assets.

## Mở rộng deck có sẵn

1. Đọc file HTML hiện tại
2. Thêm `<section class="slide">` trước `#slide-closing` (hoặc trước nav nếu chưa có slide kết)
3. Giữ `#slide-closing` làm slide cuối — trước `.slide-nav`
4. Cập nhật số trang tất cả footer + indicator nav
5. Giữ nguyên CSS/brand — chỉ thêm slide mới

## Không làm

- Không dùng font/theme generic (Inter, gradient tím AI slop)
- Không tự tạo ảnh bìa composite khi user đã chỉ định ảnh
- Không thay chevron/logo bằng SVG trừ khi user yêu cầu
- Không bỏ nav Trước/Tiếp / nút **Toàn màn hình** / **PDF** / popup **Preview slide** khi tạo deck mới
- Không dùng header cũ (badge nhỏ + `.title` đen tách dòng, chevron ngoài badge)
- Không đặt title-badge trong flow giữa slide — **luôn** góc trái trên
- Không `max-width` hẹp (1100px) hoặc `grid-template-rows: 1fr` khiến card/flow giãn rỗng
- Không chèn slide sau `#slide-closing` — slide kết luôn cuối deck
- Không scroll bên trong `.slide`

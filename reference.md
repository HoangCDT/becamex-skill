# Becamex Slide — Reference

## File mẫu

- HTML: `template/deck.html` (trong thư mục skill `~/.cursor/skills/becamex-slide/`)
- Assets: copy từ `template/becatruck-assets/` bằng `scripts/copy-assets.sh {output-dir}` — xem `template/assets/README.md`
- Cài skill: `bash scripts/install.sh` · Đóng gói: `bash scripts/package.sh`

## CSS variables

```css
:root {
  --bg-deep: #FFFFFF;
  --bg-card: #F8F8F8;
  --border: rgba(220, 68, 5, 0.15);
  --text-primary: #333333;
  --text-secondary: #989898;
  --accent: #DC4405;
  --accent-2: #692A5B;
  --accent-3: #EEAF92;
  --accent-4: #C9B6C3;
  --font-display: "Mitr", sans-serif;
  --font-body: "Mitr", sans-serif;
  --h3-size: clamp(1.05rem, 2.2vw, 1.55rem);
  --body-size: clamp(0.88rem, 1.65vw, 1.22rem);
  --small-size: clamp(0.78rem, 1.2vw, 0.98rem);
  --slide-padding-x: clamp(1rem, 2.5vw, 2.25rem);
  --slide-padding-y: clamp(0.75rem, 2vh, 1.5rem);
  --slide-padding-bottom: clamp(3.25rem, 8vh, 4.75rem);
  --title-badge-offset: clamp(3rem, 7.5vh, 4.25rem);
  --content-gap: clamp(0.5rem, 1.5vw, 1.25rem);
}
```

## Viewport & content layout

### Full màn hình

```css
*, *::before, *::after { box-sizing: border-box; }
html, body { height: 100%; overflow-x: hidden; margin: 0; }
html { scroll-snap-type: y mandatory; scroll-behavior: smooth; }

.slide {
  width: 100vw;
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
  position: relative;
}

.slide-content {
  flex: 1;
  min-height: 0;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: stretch;
  overflow: hidden;
  padding:
    var(--slide-padding-y)
    var(--slide-padding-x)
    var(--slide-padding-bottom);
}
```

### Title badge — cố định góc trái trên

Áp dụng cho mọi slide nội dung (không áp dụng `.slide-cover`, `.slide-section`, `.slide-closing`):

```css
.slide:not(.slide-cover):not(.slide-section):not(.slide-closing) .slide-content {
  position: relative;
  padding-top: calc(var(--slide-padding-y) + var(--title-badge-offset));
}

.slide:not(.slide-cover):not(.slide-section):not(.slide-closing) .slide-content > .header {
  position: absolute;
  top: var(--slide-padding-y);
  left: var(--slide-padding-x);
  z-index: 3;
  margin: 0;
  width: auto;
  max-width: calc(100% - 2 * var(--slide-padding-x));
}
```

Mobile title 2 dòng:

```css
@media (max-width: 600px) {
  :root {
    --title-badge-offset: clamp(3.5rem, 10vh, 5rem);
  }
}
```

### Content — khung theo nội dung, slide full width

```css
/* Text/grid/flow: không giãn ép chiều cao */
.features {
  flex: 0 0 auto;
  width: 100%;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: auto auto;
}
.card { height: auto; }

.swimlane,
.integration-flow {
  flex: 0 0 auto;
  width: 100%;
  align-items: start;
}
.lane,
.system-frame { height: auto; }

.slide-content > .step-strip {
  flex-shrink: 0;
  width: 100%;
}

/* Ảnh: chiếm không gian còn lại, khung ôm tỷ lệ ảnh */
.slide-content > .image-duo,
.slide-content > .image-quad {
  flex: 1 1 auto;
  min-height: 0;
  width: 100%;
  align-items: center;
  justify-items: center;
}

.shot img {
  width: auto;
  max-width: 100%;
  height: auto;
  max-height: min(calc(100dvh - 13rem), 640px);
  object-fit: contain;
}
```

### Responsive breakpoints

| Breakpoint | Thay đổi |
|------------|----------|
| `max-width: 900px` | Swimlane/FAST 1 cột; step 2 cột; ảnh quad 2 cột |
| `max-width: 700px` | `.features` 1 cột |
| `max-width: 520px` | Step strip 1 cột; title-badge nhỏ hơn |
| `max-height: 700px` / `600px` | Giảm padding và font |

Copy đầy đủ media queries từ file mẫu `slide-quan-ly-doi-xe.html`.

## Slide bìa

```html
<section class="slide slide-cover" id="slide-cover">
  <img class="cover-bg" src="becatruck-assets/cover-slide-bg.png" alt="" />
  <img class="cover-logo" src="becatruck-assets/cover-logo.png" alt="BECAMEX GROUP" />
  <div class="cover-content">
    <div class="cover-main reveal">
      <h1 class="cover-title">DÒNG 1<br />DÒNG 2</h1>
      <p class="cover-subtitle">Phụ đề</p>
    </div>
    <div class="cover-org reveal">
      <p class="cover-org-line">BECAMEX GROUP</p>
      <p class="cover-org-line underline">Trung tâm chuyển đổi số</p>
    </div>
  </div>
</section>
```

- `.cover-title`: cam, uppercase, Mitr 500
- `.cover-subtitle`: trắng
- `.cover-org-line`: cam; dòng 2 có class `underline`
- Logo bìa: file riêng `cover-logo.png`, `position: absolute` góc trái trên — không bake logo vào ảnh nền

## Slide kết (Cảm ơn)

**Luôn slide cuối** — đặt ngay trước `.slide-nav`, sau tất cả slide nội dung.

```html
<section class="slide slide-closing" id="slide-closing">
  <img class="cover-bg" src="becatruck-assets/cover-slide-bg.png" alt="" />
  <div class="closing-content">
    <h2 class="closing-title reveal">Cảm ơn!</h2>
  </div>
</section>
```

| Quy tắc | Chi tiết |
|---------|----------|
| Ảnh nền | **Cùng file** `cover-slide-bg.png` với slide bìa — tái dùng class `.cover-bg` |
| Tiêu đề | `.closing-title` — chữ **Cảm ơn!**, cam `#DC4405`, cỡ lớn `clamp(2.25rem, 7vw, 5rem)` |
| Căn chỉnh | `.slide-closing` flex center; `.closing-content` bọc nội dung giữa màn hình |
| Không dùng | `.slide-content`, `.title-badge`, `.slide-footer`, `.grid-lines` |
| Gradient mặc định | Tắt `.slide-closing::before` — chỉ hiện ảnh nền |

CSS bắt buộc (copy từ mẫu):

```css
.slide-closing {
  align-items: center;
  justify-content: center;
  text-align: center;
}
.slide-closing::before { display: none; }
.slide-closing .grid-lines { display: none; }
.slide-closing .cover-bg { z-index: 0; }
.closing-content {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.closing-title {
  font-family: var(--font-display);
  font-size: clamp(2.25rem, 7vw, 5rem);
  font-weight: 600;
  color: var(--accent);
  margin: 0;
  line-height: 1.1;
  text-shadow: 0 2px 24px rgba(255, 255, 255, 0.85);
}
```

Mở rộng deck: khi thêm slide mới **trước** slide kết — giữ `#slide-closing` làm section cuối; không chèn slide sau slide kết.

## Slide nội dung — header (title-badge)

**Vị trí:** luôn góc trái trên slide (xem [Viewport & content layout](#viewport--content-layout)).

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
  <!-- nội dung chính -->
</div>
```

CSS bắt buộc cho `.title-badge`:

```css
.title-badge {
  display: inline-flex;
  align-items: center;
  gap: clamp(0.4rem, 0.8vw, 0.65rem);
  font-family: var(--font-display);
  font-size: clamp(1.6rem, 4.5vw, 3rem);
  font-weight: 600;
  line-height: 1.15;
  color: var(--accent);
  background: rgba(220, 68, 5, 0.08);
  border: 1px solid var(--border);
  border-radius: clamp(8px, 1vw, 14px);
  padding: 0.22em 0.9em;
  margin: 0;
}
.title-badge .title-chevron {
  width: clamp(10px, 1.3vw, 16px);
  height: clamp(24px, 3.8vh, 40px);
}
```

- Chevron **nằm trong** badge, bên trái chữ — file PNG, không SVG
- Chữ cam `#DC4405`, nền cam nhạt, bo góc nhỏ (không pill)
- Một dòng tiêu đề duy nhất — không badge phụ + title đen
- **Không** đặt title trong flow căn giữa slide

## Slide nội dung — card 2×2

```html
<div class="features">
  <article class="card reveal">
    <div class="icon-wrap c1">
      <span class="card-num">1</span>
      <!-- SVG icon, stroke theo màu card -->
    </div>
    <div class="card-body">
      <h3 class="card-title">Tiêu đề ngắn</h3>
      <p class="card-desc">Mô tả. Dùng <strong>nhấn mạnh</strong> cho từ khóa.</p>
    </div>
  </article>
  <!-- c2, c3, c4 cho card 2–4 -->
</div>
```

Màu icon-wrap: `c1` cam, `c2` tím, `c3` peach, `c4` lavender. Số badge: `card-num` góc icon.

## Footer

```html
<footer class="slide-footer">
  <span class="slide-number">2</span>
  <span class="footer-divider" aria-hidden="true"></span>
  <img class="footer-logo" src="becatruck-assets/becamex-logo.png" alt="BECAMEX GROUP" />
</footer>
```

Chỉ slide nội dung có footer. Số trang = thứ tự slide (bìa = không footer).

## Navigation

Đặt trước `</body>`, sau tất cả `.slide`:

```html
<nav class="slide-nav" aria-label="Điều hướng slide">
  <button type="button" class="slide-nav-btn" id="btn-prev">← Trước</button>
  <span class="slide-nav-indicator" id="slide-indicator">1 / N</span>
  <button type="button" class="slide-nav-btn" id="btn-next">Tiếp →</button>
  <span class="slide-nav-divider slide-nav-divider-goto" aria-hidden="true"></span>
  <button type="button" class="slide-nav-btn slide-nav-goto" id="btn-goto"
    aria-label="Chọn slide" title="Chọn slide (G)">
    <span aria-hidden="true">⊞</span><span>Slides</span>
  </button>
  <span class="slide-nav-divider" aria-hidden="true"></span>
  <button type="button" class="slide-nav-btn slide-nav-fullscreen" id="btn-fullscreen"
    aria-label="Thuyết trình toàn màn hình" title="Toàn màn hình (F)">
    <span class="fs-icon" aria-hidden="true">⛶</span>
    <span class="fs-label">Toàn màn hình</span>
  </button>
  <span class="slide-nav-divider" aria-hidden="true"></span>
  <button type="button" class="slide-nav-btn slide-nav-export" id="btn-export-pdf"
    aria-label="Xuất PDF" title="Xuất PDF (Ctrl+P)">
    <span aria-hidden="true">↓</span><span>PDF</span>
  </button>
</nav>

<div class="slide-overview" id="slide-overview" hidden aria-hidden="true">
  <div class="slide-overview-backdrop" id="slide-overview-backdrop"></div>
  <div class="slide-overview-dialog" role="dialog" aria-modal="true" aria-labelledby="slide-overview-title">
    <div class="slide-overview-header">
      <div>
        <h2 class="slide-overview-title" id="slide-overview-title">Chọn slide</h2>
        <p class="slide-overview-hint">Bấm tile để nhảy tới slide · Esc để đóng</p>
      </div>
      <button type="button" class="slide-overview-close" id="btn-overview-close">Đóng</button>
    </div>
    <div class="slide-overview-grid" id="slide-overview-grid"></div>
  </div>
</div>
```

Copy toàn bộ `<script>` nav + fullscreen + overview + exportPdf + IntersectionObserver từ file mẫu.

**Nhớ slide cuối:** `localStorage` key `becamex-slide:{tên-file.html}`; refresh scroll về đúng slide (`behavior: 'instant'` lần đầu).

## Presentation mode

Chế độ thuyết trình gồm **fullscreen** + **popup preview tile**. Bắt buộc trong mọi deck mới.

### Phím tắt

| Phím | Hành vi |
|------|---------|
| `←` `→` `PageUp` `PageDown` | Chuyển slide (không khi popup mở) |
| `F` | Bật/tắt fullscreen |
| `G` | Mở popup chọn slide |
| `Ctrl+P` / `⌘P` | Xuất PDF (hộp thoại in trình duyệt) |
| `Esc` | Đóng popup preview; nếu popup đóng → thoát fullscreen (trình duyệt) |

### CSS bắt buộc

Copy block `/* === SLIDE NAVIGATION === */`, `/* === SLIDE OVERVIEW === */`, `/* === PDF EXPORT (print) === */` từ mẫu chuẩn.

| Class | Vai trò |
|-------|---------|
| `.slide-nav` | Thanh nav cố định `bottom center`, `z-index: 100` |
| `.slide-nav-fullscreen` | Nút fullscreen; icon `.fs-icon`, label `.fs-label` |
| `.slide-nav-goto` | Nút preview — luôn hiện (`display: inline-flex`) |
| `.slide-nav-indicator` | Có thể bấm mở overview; gạch chân gợi ý |
| `html.is-presentation-fullscreen` | Bật khi fullscreen — đổi label nút Toàn màn hình |
| `.slide-overview` | Overlay popup, `z-index: 220` |
| `.slide-overview.is-open` | Hiện popup (`display: flex`) |
| `.slide-tile` | Mỗi ô preview; `.is-current` = slide đang xem |
| `.slide-tile-preview` | Khung thumbnail 16:9, `overflow: hidden` |
| `.slide-tile-scale` | Wrapper scale; clone slide bên trong |
| `.slide-tile-clone` | Clone `.slide` cố định **1280×720px**; tắt animation reveal |

### JavaScript bắt buộc

| Hàm / biến | Vai trò |
|------------|---------|
| `TILE_REF_W = 1280`, `TILE_REF_H = 720` | Kích thước gốc trước khi scale tile |
| `isFullscreen()` | Kiểm tra `fullscreenElement` / `webkitFullscreenElement` |
| `toggleFullscreen()` | `requestFullscreen` / `exitFullscreen` trên `<html>` |
| `updateFullscreenBtn()` | Đổi label nút; toggle `html.is-presentation-fullscreen`; đóng overview khi thoát |
| `getSlideLabel(slide, i)` | Tên tile: `.title-badge` → `.section-title` → Bìa/Cảm ơn |
| `buildOverviewTiles()` | Clone mỗi slide vào grid (chạy 1 lần, `overviewBuilt`) |
| `scaleTilePreviews()` | `transform: scale(w/1280)` theo chiều rộng tile; gọi lại khi `resize` |
| `openOverview()` | Mở popup; build tiles lần đầu nếu chưa có |
| `closeOverview()` | Ẩn popup, `overviewOpen = false` |
| `overviewOpen` | Khi `true`: Esc đóng popup, chặn phím chuyển slide |

### Thêm slide mới vào deck có sẵn

Sau khi thêm `<section class="slide">`:

1. Cập nhật footer số trang + indicator `N`.
2. **Không** cần sửa HTML overview — script clone tự động từ `querySelectorAll('.slide')` khi reload trang.

### Kiểm tra presentation mode

- [ ] Nút **Toàn màn hình** + **F** hoạt động
- [ ] Nút **⊞ Slides** luôn hiện trên nav
- [ ] **G** / bấm indicator / nút Slides mở popup tile
- [ ] Tile preview hiển thị đủ slide; bấm tile nhảy đúng
- [ ] Esc đóng popup trước, không thoát fullscreen ngay khi popup mở

## Standalone HTML (1 file)

Phát triển với đường dẫn tương đối:

```html
<img src="becatruck-assets/chevron.png" alt="" />
```

Chia sẻ: chạy `scripts/bundle-html.py` → thay bằng `src="data:image/png;base64,..."`.

Giữ bản có thư mục assets để chỉnh sửa; xuất bản `*-standalone.html` để gửi email / copy USB.

## PDF export

Xuất PDF **zero-dependency** — **snapshot clone** từng slide đúng kích thước màn hình, scale vào trang 297×167mm, rồi `window.print()`. Không override CSS từng component — giữ layout HTML 100%.

### HTML

```html
<div id="print-root" aria-hidden="true"></div>
```

Đặt trước `#slide-overview` hoặc cuối `body`.

### JavaScript (luồng)

1. `buildPrintRoot()` — lần lượt `goToSlide(i)`, đo `getBoundingClientRect()`, `cloneNode(true)` với kích thước px đo được
2. Bọc clone trong `.print-page-scale` + `transform: scale(...)` khớp trang 16:9
3. `body.is-printing` + `window.print()`
4. `afterprint` → xóa `#print-root`

Class clone: `.slide-export-clone` + `.print-slide-clone` (tắt reveal animation).

### CSS `@media print` (tóm tắt)

| Quy tắc | Mục đích |
|---------|----------|
| `body > *:not(#print-root) { display: none }` | Chỉ in snapshot |
| `@page { size: 297mm 167mm }` | 16:9 — 1 slide = 1 trang |
| `.print-page { 297mm × 167mm }` | Khớp scale trong JS |
| `print-color-adjust: exact` | Giữ màu cam, ảnh nền |

### Hướng dẫn user

1. Bấm nút **PDF** hoặc **Ctrl+P** / **⌘P**
2. Đích in: **Lưu dưới dạng PDF** (Chrome/Edge) hoặc **PDF** (Safari)
3. Bật **Background graphics** nếu trình duyệt hỏi (để giữ ảnh nền slide bìa)

## Integration FAST (2 hệ thống)

```html
<div class="integration-flow reveal">
  <div class="system-frame becatruck">
    <div class="system-head">Hệ thống quản lý đội xe</div>
    <div class="system-body">
      <div class="system-action export">Kết xuất dữ liệu</div>
    </div>
  </div>
  <div class="integration-arrow" aria-hidden="true"><!-- SVG → --><span>Dữ liệu phiếu xe</span></div>
  <div class="system-frame fast">
    <div class="system-head">Hệ thống FAST</div>
    <div class="system-body">
      <div class="system-action import">Import dữ liệu phiếu xe</div>
      <div class="flow-arrow">↓</div>
      <div class="system-action">Đổ dữ liệu báo cáo như bình thường</div>
    </div>
  </div>
</div>
```

## Slide Điều xe (waterfall + ảnh)

Layout 2 cột: `.waterfall` (trái) | `.image-stack` (phải — 2 ảnh xếp dọc, border cam 2px).

```html
<div class="dispatch-layout reveal">
  <div class="waterfall">...</div>
  <div class="image-stack">
    <figure class="shot"><img ... /><figcaption class="shot-caption">Lập lệnh điều xe</figcaption></figure>
    <figure class="shot"><img ... /><figcaption class="shot-caption">Chi tiết lệnh điều xe</figcaption></figure>
  </div>
</div>
```

Icon waterfall: 1 lịch (cam), 2 phiếu (tím), 3 đồng hồ (peach), 4 mắt (lavender).

## Viewport base (bắt buộc)

Xem section [Viewport & content layout](#viewport--content-layout) ở trên.

`prefers-reduced-motion` giảm animation.

## PPT — trích text slide (tham khảo)

```bash
python3 -c "
import zipfile, xml.etree.ElementTree as ET
pptx = 'PATH_TO.pptx'
with zipfile.ZipFile(pptx) as z:
    for i in range(1, 20):
        p = f'ppt/slides/slide{i}.xml'
        if p not in z.namelist(): break
        root = ET.fromstring(z.read(p))
        texts = [t.text.strip() for t in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t') if t.text and t.text.strip()]
        print(f'--- slide {i} ---')
        print('\n'.join(texts))
"
```

## Icon SVG

Dùng stroke đơn giản 24×24, `stroke-width="1.8"`, màu khớp class card (`#DC4405`, `#692A5B`, `#c97a4a`, `#9a7a8e`). Chọn icon gợi ý theo nghĩa (GPS → pin, tích hợp → brackets, app → phone).

## Slide giới thiệu khách hàng (từ PDF)

Ảnh giao diện lưu tại `becatruck-assets/pdf/pageNN-imgM.{png,jpeg}` — trích bằng `scripts/extract-pdf.py`.

| Slide | Nội dung | Ảnh / diagram |
|-------|----------|----------------|
| Phạm vi & Người dùng | 4 vai trò grid | — |
| Luồng nghiệp vụ | `.swimlane` 3 cột + mũi tên ngang | Vẽ lại (PDF p.4) |
| Tích hợp FAST | `.integration-flow` 2 khung hệ thống | Vẽ lại (PDF p.5) |
| Tính năng nổi bật | `.slide-section` | — |
| Điều xe | `.waterfall` + `.image-stack` | page08 (lập lệnh), page09 (chi tiết) |
| Tài xế app | `.step-strip` + `.image-quad` | page11 x4 |
| Giám sát | `.module-grid.cols-3-row` × 2 slide | Slide 11: bước 1–3 (p.13); Slide 12: bước 4–6 (p.14) |
| Cảm ơn | `.slide-closing` | `cover-slide-bg.png` (cùng bìa) — chỉ **Cảm ơn!** |

Chi tiết flowchart: [flowcharts.md](flowcharts.md)

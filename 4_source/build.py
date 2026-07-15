#!/usr/bin/env python3
"""
MasTool merch collateral build pipeline.

For every piece, emits three files:
   *.html                  self-contained (fonts + logo embedded, works offline)
   *_PRINT_300dpi.png      high-res master, exact page size @ 300 DPI
   *_preview.png           low-res preview for sharing / approval

Drop-in QR codes:
   put  vip-qr.png  and/or  bit-qr.png  in /home/claude/assets/
   and they are composited automatically. Otherwise a dashed slot is drawn.
"""
import base64, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

SRC    = pathlib.Path("/home/claude/src")
FONTS  = pathlib.Path("/home/claude/fonts")
ASSETS = pathlib.Path("/home/claude/assets")
OUT    = pathlib.Path("/mnt/user-data/outputs")
LOGO   = pathlib.Path("/mnt/user-data/uploads/logo-white-transparent.png")
OUT.mkdir(parents=True, exist_ok=True)
ASSETS.mkdir(parents=True, exist_ok=True)

MM_PX = 96 / 25.4          # CSS px per mm @ 96dpi
DPI   = 300

# ---------------------------------------------------------------- assets
def b64_file(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

FONT_CSS = """<style>
  @font-face{{font-family:'Anton';font-style:normal;font-weight:400;font-display:block;
    src:url(data:font/woff2;base64,{anton}) format('woff2');}}
  @font-face{{font-family:'Oswald';font-style:normal;font-weight:400 700;font-display:block;
    src:url(data:font/woff2;base64,{oswald}) format('woff2');}}
  @font-face{{font-family:'Heebo';font-style:normal;font-weight:400 900;font-display:block;
    src:url(data:font/woff2;base64,{heebo}) format('woff2');}}
</style>""".format(
    anton=b64_file(FONTS / "anton.woff2"),
    oswald=b64_file(FONTS / "oswald.woff2"),
    heebo=b64_file(FONTS / "heebo.woff2"),
)

BASE_CSS = "<style>\n" + (SRC / "base.css").read_text() + "\n</style>"

# trim the logo's transparent padding once, reuse everywhere
_lg = Image.open(LOGO).convert("RGBA")
_lg = _lg.crop(_lg.getchannel("A").getbbox())
_lg.save("/home/claude/assets/logo_trim.png")
LOGO_TAG    = f'<img class="wordmark-img" src="data:image/png;base64,{b64_file(ASSETS/"logo_trim.png")}" alt="MasTool">'
LOGO_TAG_SM = LOGO_TAG.replace('class="wordmark-img"', 'class="wordmark-img wordmark-img--sm"')

WATERMARK = """<div class="watermark" aria-hidden="true">
  <svg viewBox="0 0 200 200" fill="none" stroke="#334A38" stroke-width="1.2">
    <g stroke-linejoin="round">
      <path d="M100,10 L130.9,182.6 L4.6,64.7 L195.4,89.1 L46.7,176.3 L46.7,23.7 L195.4,110.9 L4.6,135.3 L130.9,17.4 Z"/>
    </g>
  </svg>
</div>"""

def qr_tag(name, label_en, label_he):
    """Composite a real QR if supplied, else render a dashed placeholder slot."""
    f = ASSETS / f"{name}.png"
    if f.exists():
        return f'<img src="data:image/png;base64,{b64_file(f)}" alt="{label_en} QR">'
    return f'<div class="hint">{label_en}<br>QR<br><span class="he">{label_he}</span></div>'

# ---------------------------------------------------------------- pages
PAGES = [
    # (source, output stem, page w x h in mm, logo tag, viewport width px)
    ("menu.html", "MasTool_Merch_Menu",     (210, 297), LOGO_TAG,    794),
    ("bit.html",  "MasTool_Bit_Payment",    (210, 297), LOGO_TAG,    794),
    ("vip.html",  "MasTool_VIP_Signup",     None,       LOGO_TAG_SM, 430),  # web page, no print size
]

def sheet_css(w_mm, h_mm):
    return f"""
      html,body{{background:#fff!important;padding:0!important;margin:0!important;display:block!important;}}
      .sheet{{width:{w_mm}mm!important;height:{h_mm}mm!important;max-width:none!important;
              margin:0!important;border:none!important;box-shadow:none!important;
              display:flex!important;flex-direction:column!important;}}
      .rows{{flex:1 1 auto!important;display:flex!important;flex-direction:column!important;}}
      .row{{flex:1 1 0!important;}}
      .pay-body{{flex:1 1 auto!important;display:flex!important;flex-direction:column!important;
                 justify-content:center!important;}}
      *{{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;}}
    """

WEB_CSS = "html,body{background:#F0E7D2!important;padding:0!important;margin:0!important;}"

built = []
with sync_playwright() as p:
    browser = p.chromium.launch()

    for src, stem, size, logo, vw in PAGES:
        html = (SRC / src).read_text()
        html = (html
                .replace("<!--FONTS-->",     FONT_CSS)
                .replace("<!--BASE-->",      BASE_CSS)
                .replace("<!--LOGO-->",      logo)
                .replace("<!--WATERMARK-->", WATERMARK)
                .replace("<!--VIP_QR-->",    qr_tag("vip-qr", "Scan to join VIP", "סרקו להצטרפות"))
                .replace("<!--BIT_QR-->",    qr_tag("bit-qr", "Paste Bit QR here", "כאן ממקמים את קוד ה-QR")))

        html_path = OUT / f"{stem}.html"
        html_path.write_text(html)

        if size:                                    # print piece
            w_mm, h_mm = size
            vw_px = round(w_mm * MM_PX)
            vh_px = round(h_mm * MM_PX)
            target = (round(w_mm / 25.4 * DPI), round(h_mm / 25.4 * DPI))
            renders = [(f"{stem}_PRINT_300dpi.png", DPI / 96, target, 300),
                       (f"{stem}_preview.png",      1.1,      None,   72)]
            extra_css, clip_sel = sheet_css(w_mm, h_mm), ".sheet"
        else:                                       # web page
            vw_px, vh_px = vw, 900
            renders = [(f"{stem}_A4source.png", 3.0, None, 300),
                       (f"{stem}_preview.png",  1.0, None, 72)]
            extra_css, clip_sel = WEB_CSS, None

        for fname, dsf, target, dpi_tag in renders:
            page = browser.new_page(viewport={"width": vw_px, "height": vh_px},
                                    device_scale_factor=dsf)
            page.goto(html_path.as_uri())
            page.add_style_tag(content=extra_css)
            page.wait_for_timeout(900)              # let embedded fonts settle
            if clip_sel:
                page.query_selector(clip_sel).screenshot(path=str(OUT / fname))
            else:
                page.screenshot(path=str(OUT / fname), full_page=True)
            page.close()

            im = Image.open(OUT / fname).convert("RGB")
            if target:
                im = im.resize(target, Image.LANCZOS)   # snap to exact page size
            im.save(OUT / fname, dpi=(dpi_tag, dpi_tag))
            built.append((fname, im.size, (OUT / fname).stat().st_size / 1024))

    browser.close()

# ---- fit web-page renders onto an A4 300 DPI canvas (centred, cream, no distortion) ----
A4 = (2480, 3508)
CREAM = (240, 231, 210)
for src, stem, size, *_ in PAGES:
    if size:
        continue
    srcimg = OUT / f"{stem}_A4source.png"
    if not srcimg.exists():
        continue
    card = Image.open(srcimg).convert("RGB")
    margin = int(A4[1] * 0.045)                       # ~13mm top/bottom breathing room
    max_h = A4[1] - margin * 2
    max_w = int(A4[0] * 0.82)
    scale = min(max_w / card.width, max_h / card.height)
    card = card.resize((round(card.width * scale), round(card.height * scale)), Image.LANCZOS)
    canvas = Image.new("RGB", A4, CREAM)
    canvas.paste(card, ((A4[0] - card.width) // 2, (A4[1] - card.height) // 2))
    out = OUT / f"{stem}_PRINT_300dpi.png"
    canvas.save(out, dpi=(300, 300))
    built.append((out.name, canvas.size, out.stat().st_size / 1024))
    srcimg.unlink()

print(f"\n{'file':42s} {'pixels':>13s} {'size':>9s}")
print("-" * 68)
for f, s, kb in built:
    print(f"{f:42s} {s[0]:>5d}x{s[1]:<6d} {kb:>7.0f} KB")

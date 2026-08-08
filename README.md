# MasTool — Merch Stand Kit
Gagarin Club, Tel Aviv · 13 August 2026

## Contents

### 1_print_masters/  — send these to the printer
| File | Size | Spec |
|---|---|---|
| MasTool_Merch_Menu_PRINT_300dpi.png | 2480×3508 | A4 portrait (210×297mm), 300 DPI, RGB |
| MasTool_Bit_Payment_PRINT_300dpi.png | 2480×3508 | A4 portrait (210×297mm), 300 DPI, RGB |
| MasTool_VIP_Signup_PRINT_300dpi.png | 2480×3508 | VIP web page fitted to A4, 300 DPI |
| MasTool_VIP_Signup_master.png | 1290×3924 | Older @3x web render, superseded by the file above |

### 2_previews/  — for sharing / approval (Vlad, Almog)
Low-res, small file size, email-friendly.

### 3_html/  — source of truth, self-contained
Fonts (Anton, Oswald, Heebo — subsetted Latin + Hebrew + ₪) and the MasTool
logo are embedded as base64. **These files work offline** — no internet needed
at the venue. Open in any browser; Ctrl/Cmd+P prints correctly to A4.

### 4_source/  — to regenerate everything
`build.py` + page sources + subsetted fonts.
Run `python3 build.py` (needs playwright + pillow) to rebuild all outputs.
Drop `vip-qr.png` / `bit-qr.png` into an `assets/` folder and they are
composited into the QR slots automatically.

---

## Pricing (as printed)

One A4 menu carries everything. MasTool merch on top, guest-artist pieces in the
last two rows below a divider rule.

### MasTool merch — bundles apply here only
| Item | Regular | VIP | Saves |
|---|---|---|---|
| T-Shirt | ₪100 | ₪80 | ₪20 |
| Event Poster | ₪130 | ₪110 | ₪20 |
| Limited Edition Art Poster | ₪150 | ₪130 | ₪20 |
| Shirt + Event Poster | ₪200 | ₪170 | ₪30 |
| Shirt + Limited Edition Art Poster | ₪230 | ₪200 | ₪30 |
| All In — One of Each | ₪330 | ₪280 | ₪50 |

Verified: no combination of smaller purchases beats any bundle price,
in either column.

### Guest-artist pieces — standalone, never part of a bundle
| Item | Regular | VIP | Notes |
|---|---|---|---|
| "Duba" Shirt | ₪100 | ₪80 | Very limited. **No holds** — sold on the spot |
| "Arrested Cloth" Concrete Pendant (@anima_concrete) | ₪200 | ₪180 | ₪20 VIP discount. No string-colour choice |

The pendant row leads with the collection name — **Arrested Cloth** — credits
Anima (`@anima_concrete`), who guests on the show, and states the pieces are
hand-cast custom pendants from a new collection inspired by the show. It carries
the same red ₪20 OFF sticker as the other discounted rows.

Both are excluded from every bundle — a "Duba" shirt does **not** count as the
shirt in Shirt + Poster or All In. The menu footer states this in EN + HE, and
the "no holds" rule on the Duba shirt overrides the 21:00 VIP hold policy
printed just below it.

---

## OPEN ITEMS

1. ~~VIP signup QR~~ **DONE.** VIP page is hosted at
   `https://thedanmaor.github.io/Mastool-Merch-Stand/` (GitHub Pages, served
   from `docs/`). `4_source/assets/vip-qr.png` was regenerated from that live
   URL (ECC level Q, matches the Bit QR's style) and the menu was rebuilt —
   scanning the menu's "Sign Up to VIP" panel now opens the real VIP page.

2. ~~Bit QR~~ **DONE.** Payment card carries the live Bit QR
   (payee: דן מאור). Regenerated at print resolution with ECC level Q,
   prints ~83mm across, verified to decode from the final master.

3. ~~Guest-artist product photos~~ **DONE.**
   - **"Arrested Cloth" pendant** — `4_source/assets/thumbs/pend_concrete.png`, cut out
     of the supplied shot (background removed, 600×600 transparent PNG) and
     shown on a lilac tile.
   - **"Duba" Shirt** — deliberately has *no* photo. Every shirt is one of a
     kind, so no single shot represents the row; it renders a mystery mark
     (shirt outline + question mark) on a straw tile. Dropping a real
     `duba_shirt.png` into `4_source/assets/thumbs/` would override it — only
     do that if the row stops being a mystery.

   Any photo dropped in there should be a square PNG, transparent or white
   background, ≥400×400px. They render at 48px on the sheet (~17mm at print
   size), `object-fit:contain`.

Nothing blocks printing.

### Sheet order (top to bottom)
Header · price table · guest-artist rows · **Cash / Bit only** · hold policy ·
shirt care · **VIP signup QR** · footnotes. Payment terms sit right under the
prices; the VIP signup panel closes the sheet as the last call to action.

## Operational note
The 21:00 hold policy printed on the menu requires someone at the stand keeping
a named list and physically setting items aside. With only 14 of each poster,
decide in advance whether VIP holds are capped and who runs the list.

VIP signup now lets fans pre-select items (T-Shirt + size, Event Poster, Limited
Edition Art Poster) before submitting. On success they get a ticket-style popup
with their name and picks to show at the stand. The signups sheet has matching
`Shirt` / `Shirt Size` / `Event Poster` / `Ltd Poster` columns — cross-check
these against the hold list at 21:00.

Two rules on the guest-artist rows differ from everything else at the stand, and
whoever works the table needs both: the "Duba" shirt is **not held** (it never
goes on the 21:00 VIP list), and **neither piece counts toward a bundle** — a
customer asking for "All In" with a Duba shirt is buying ₪330 + ₪100, not ₪330.

The VIP signup form does not offer the Duba shirt or the pendant as pre-select
options — they are counter-only items.

The menu carries a bilingual (EN/HE) shirt-care strip at the foot of the page —
machine wash 40°, do not tumble dry, iron low heat — as clean ink-stroke laundry
symbols matching the sheet's palette and type.

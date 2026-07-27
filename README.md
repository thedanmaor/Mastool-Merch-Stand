# MasTool — Merch Stand Kit
Gagarin Club, Tel Aviv · 13 August 2026

## Contents

### 1_print_masters/  — send these to the printer
| File | Size | Spec |
|---|---|---|
| MasTool_Merch_Menu_PRINT_300dpi.png | 2480×3508 | A4 portrait (210×297mm), 300 DPI, RGB |
| MasTool_Anima_Concrete_PRINT_300dpi.png | 1748×2480 | A5 portrait (148×210mm), 300 DPI, RGB — guest-artist pendant sheet |
| MasTool_Duba_Shirt_PRINT_300dpi.png | 1748×2480 | A5 portrait (148×210mm), 300 DPI, RGB — guest-artist shirt sheet |
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

## Three sheets, three jobs

The stand hands out three separate printed pieces:

| Sheet | Size | Covers |
|---|---|---|
| **MasTool Merch Menu** | A4 | Core MasTool merch — shirt, posters, bundles, VIP signup QR |
| **"Duba" Shirt** | A5 | Guest-artist special edition shirt + its bundles |
| **Arrested Cloth / Anima Concrete** | A5 | Guest-artist concrete pendants + their bundles |

The Duba shirt is **not** listed on the main A4 menu — the menu footer
cross-refers to both guest sheets (EN + HE) so staff can hand the right sheet
over on request. Keep a stack of each A5 at the stand.

## Pricing (as printed)

### Main menu (A4)
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

### "Duba" shirt sheet (A5)
A Duba shirt is priced as a shirt, so every bundle matches the main menu.

| Item | Regular | VIP | Saves |
|---|---|---|---|
| "Duba" Shirt (very limited, max 3 per person) | ₪100 | ₪80 | ₪20 |
| "Duba" Shirt + Event Poster | ₪200 | ₪170 | ₪30 |
| "Duba" Shirt + Limited Edition Art Poster | ₪230 | ₪200 | ₪30 |
| "Duba" Shirt + Concrete Pendant | ₪220 | ₪190 | ₪30 |
| "Duba" All In | ₪330 | ₪280 | ₪50 |

Sizes printed on the sheet: M, L, XL, 2XL, 3XL — same set as the VIP signup
form. **No holds** on this shirt (red strip on the sheet) — it sells on the
spot, first come first served, which deliberately overrides the green 21:00
hold policy printed on the other sheets.

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

3. **TODO — guest-sheet product photos.** Both A5 sheets render dashed
   placeholder boxes where the product photos go. Drop the real shots into
   `4_source/assets/thumbs/` with these exact names and rerun `build.py` —
   they are composited automatically, no code change needed:

   | File | Sheet | Row |
   |---|---|---|
   | `pend_black.png` | Anima Concrete | Concrete Pendant · Black String |
   | `pend_gold.png` | Anima Concrete | Concrete Pendant · Gold String |
   | `pend_shirt.png` | Anima Concrete | Pendant + T-Shirt |
   | `pend_poster.png` | Anima Concrete | Pendant + Event Poster |
   | `pend_all.png` | Anima Concrete | Concrete All In |
   | `duba_shirt.png` | Duba | "Duba" Shirt |
   | `duba_event.png` | Duba | "Duba" Shirt + Event Poster |
   | `duba_art.png` | Duba | "Duba" Shirt + Limited Edition Art Poster |
   | `duba_pendant.png` | Duba | "Duba" Shirt + Concrete Pendant |
   | `duba_all.png` | Duba | "Duba" All In |

   Square PNGs, transparent or white background, ≥400×400px. They render at
   40px on the sheet (~14mm at print size), `object-fit:contain`.

4. **TODO — Duba's artist handle.** The Anima sheet's lockup carries
   `@anima_concrete`; the Duba lockup reads `"Duba" × MasTool` with no handle
   because we don't have one. If Duba has an Instagram, add it to the `.collab`
   line in `4_source/duba.html` and rebuild.

Nothing currently blocks printing except the photos above (both sheets print
fine with the placeholders — they just look unfinished).

## Operational note
The 21:00 hold policy printed on the menu requires someone at the stand keeping
a named list and physically setting items aside. With only 14 of each poster,
decide in advance whether VIP holds are capped and who runs the list.

VIP signup now lets fans pre-select items (T-Shirt + size, Event Poster, Limited
Edition Art Poster) before submitting. On success they get a ticket-style popup
with their name and picks to show at the stand. The signups sheet has matching
`Shirt` / `Shirt Size` / `Event Poster` / `Ltd Poster` columns — cross-check
these against the hold list at 21:00.

The Anima Concrete A5 sheet is a separate hand-out for the guest-artist pendant
collab (@anima_concrete). The menu footer cross-refers to it — keep a stack at
the stand. Its pricing: pendant ₪150 / ₪120 VIP (black string), ₪250 / ₪220
(gold string), bundles ₪220–₪330 with ₪30–₪50 VIP discounts.

The "Duba" A5 sheet is the second guest hand-out. Two rules on it differ from
everything else at the stand and staff need to know both: **no holds** (it does
not go on the 21:00 VIP hold list) and **max 3 per person**. Its bundles pull in
the same posters and pendants sold on the other two sheets, so whoever runs the
stand should be able to fulfil a Duba bundle from all three stacks.

The menu carries a bilingual (EN/HE) shirt-care strip at the foot of the page —
machine wash 40°, do not tumble dry, iron low heat — as clean ink-stroke laundry
symbols matching the sheet's palette and type.

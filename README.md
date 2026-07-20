# MasTool — Merch Stand Kit
Gagarin Club, Tel Aviv · 13 August 2026

## Contents

### 1_print_masters/  — send these to the printer
| File | Size | Spec |
|---|---|---|
| MasTool_Merch_Menu_PRINT_300dpi.png | 2480×3508 | A4 portrait (210×297mm), 300 DPI, RGB |
| MasTool_Bit_Payment_PRINT_300dpi.png | 2480×3508 | A4 portrait (210×297mm), 300 DPI, RGB |
| MasTool_VIP_Signup_master.png | 1290×3924 | Web page render @3x (reference only) |

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

Nothing currently blocks printing.

## Operational note
The 21:00 hold policy printed on the menu requires someone at the stand keeping
a named list and physically setting items aside. With only 14 of each poster,
decide in advance whether VIP holds are capped and who runs the list.

VIP signup now lets fans pre-select items (T-Shirt + size, Event Poster, Limited
Edition Art Poster) before submitting. On success they get a ticket-style popup
with their name and picks to show at the stand. The signups sheet has matching
`Shirt` / `Shirt Size` / `Event Poster` / `Ltd Poster` columns — cross-check
these against the hold list at 21:00.

The menu carries a bilingual (EN/HE) shirt-care strip at the foot of the page —
machine wash 40°, do not tumble dry, iron low heat — as clean ink-stroke laundry
symbols matching the sheet's palette and type.

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

## OPEN ITEMS — both block printing

1. **VIP signup QR currently points at the Bit link (placeholder).**
   Once the VIP page is hosted, replace `4_source/assets/vip-qr.png` (or
   regenerate from the real URL) and rebuild. As-is, scanning the menu's
   "Sign Up to VIP" panel opens the Bit payment page.

   **VIP page needs a hosted URL.**
   `MasTool_VIP_Signup.html` has `FORM_ENDPOINT = "PASTE_YOUR_FORM_ENDPOINT_HERE"`
   at the top of its `<script>`. Set it (Formspree / Google Apps Script / Airtable),
   host the page, then the signup QR can be generated from the live URL and
   dropped into the menu. **Until the page has a URL, there is no QR to print.**

2. ~~Bit QR~~ **DONE.** Payment card carries the live Bit QR
   (payee: דן מאור). Regenerated at print resolution with ECC level Q,
   prints ~83mm across, verified to decode from the final master.

## Operational note
The 21:00 hold policy printed on the menu requires someone at the stand keeping
a named list and physically setting items aside. With only 14 of each poster,
decide in advance whether VIP holds are capped and who runs the list.

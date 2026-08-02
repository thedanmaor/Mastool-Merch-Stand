# MERCH — project rules

## Every source change ships built outputs

Edit `4_source/*.html` or `base.css` → always finish the loop:

1. `cd 4_source && python build.py`
2. Check A4 fit for print pieces (`.sheet` scrollHeight vs 1122.5px page).
3. Copy outputs out of `4_source/_build/`:
   - `*_PRINT_300dpi.png` → `1_print_masters/`
   - `*_preview.png` → `2_previews/`
   - `*.html` → `3_html/`
4. Commit source + regenerated outputs together.

Never leave `2_previews/` stale — previews are what Dan sends to Vlad and Almog
for approval, so an out-of-date preview gets approved for the wrong artwork.

## Repo stays on the personal account

This repo lives at `thedanmaor/Mastool-Merch-Stand` and stays there. The global
rule about hosting everything under `DID-Software-Solutions` does not apply here —
don't propose transferring it.

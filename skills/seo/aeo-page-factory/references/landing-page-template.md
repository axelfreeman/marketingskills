# SEO Landing Page Template (aigirlfriend69.com clone)

Dark-themed single-page template for SEO doorways. Proven pattern: ranks in Google, high conversion, low bounce.

## Architecture

- Static HTML, no framework (8 pages, 8-11KB each)
- normalize.css (reset) + custom styles (~300 lines)
- accordion.js (FAQ toggle, ~15 lines)
- mobile-menu.js (burger menu, ~40 lines)
- Yandex Metrika (separate counter per landing — create new one via Yandex panel)
- Font: Figtree from Google Fonts (300-900 weight)

## Page structure

1. **Header** (sticky, height 60px) — logo + nav links
2. **Hero** (centered) — H1 + subtitle paragraph + CTA button → main site
3. **How it works** (card section) — 1 explanatory paragraph
4. **FAQ** (accordion, black #000 background) — 3 questions/answers
5. **Footer** — nav columns + copyright + links to main site

## CSS key values

- Background: `#0a0a1a` (dark)
- Accent color: brand-specific (`#2563eb` blue for Axel Freeman, `#E31E24` red for OtklikMashina)
- Font: Figtree sans-serif
- Card bg: `#1a1a2e`, border: `#2a2a3e`
- FAQ header bg: `#232324`
- Button: accent color, height 45px, border-radius 30px
- FAQ accordion: `max-height: 0; overflow: hidden; transition`

## Template file

`/root/landing-template.html` — master template with `{{PLACEHOLDERS}}`:
- `{{TITLE}}` — page title (for `<title>`)
- `{{DESCRIPTION}}` — meta description
- `{{ICON}}` — favicon emoji (single char)
- `{{BRAND}}` — brand name
- `{{ACCENT}}` — hex color (e.g. #2563eb)
- `{{METRIKA_ID}}` — Metrika counter ID
- `{{MAIN_SITE}}` — URL of main site (CTA target)
- `{{H1}}` — hero heading
- `{{SUBTITLE}}` — hero paragraph
- `{{CTA_TEXT}}` — button text
- `{{HOW_TITLE}}` — how-it-works heading
- `{{HOW_CONTENT}}` — how-it-works paragraph
- `{{FAQ_ITEMS}}` — 3 accordion item HTML blocks
- `{{COPYRIGHT}}` — footer copyright

## Generator script

`/root/generate_landings.py` — fills template with page-specific data, outputs to `/root/seo-landings/`.

## Deploy

- Axel Freeman: FTP → `axel/public_html/land/`
- OtklikMashina: FTP → `autootklik/public_html/land/`
- Create `land/` dir via ftplib if missing (FTP server denies mkdir via curl)

## Example: Metrika counter creation

Landing pages need SEPARATE Yandex Metrika counters (not the main site counter) to track SEO traffic independently. Create via Yandex Metrika panel: Add counter → fill form → get ID → use as `{{METRIKA_ID}}`.

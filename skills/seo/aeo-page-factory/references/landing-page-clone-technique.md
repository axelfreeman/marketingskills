# Landing Page Clone — Technique Reference

## What We Learned from aigirlfriend69.com

The site `aigirlfriend69.com` is a pure SEO-play: a thin doorway site that ranks in Google for "AI girlfriend" queries and redirects traffic to `tyan.ai` (the real product). We reverse-engineered it and adapted the pattern for Axel Freeman and OtklikMashina.

## Architecture

```
Google traffic → SEO landing page (static HTML)
                    ↓
              CTA button → main site (axelfreeman.ru / avtootkliki.ru)
```

## Page Structure (26+ sections)

Each landing page is a ~10KB static HTML file with:

1. **Header banner** — promo offer + CTA button
2. **Sticky header** — logo + nav links
3. **Under-header section** — H1 + date + subtitle + CTA button
4. **Rating card** — "Top-rated" badge with stars (9.8/10), user votes count
5. **Article body** — 4 content H2 sections (80-120 words each)
6. **Brand deep-dive** — 20 H4 subsections in 5 groups:
   - Real Cases & Results
   - Process & Methodology
   - Tools & Technology Stack
   - Pricing & Formats
   - Reviews, Guarantees & Support
7. **FAQ** — accordion with 5 questions/answers
8. **Footer CTA banner** — promo + button
9. **Footer** — navigation + copyright

**Key difference from aigirlfriend69:** our pages have OPEN links (SEO-friendly), not JS redirects. The original site hides affiliate links behind JavaScript (probably cloaking).

## CSS Theme

- Dark background (#0a0a1a)
- Accent color per brand (Axel: #2563eb, Otklik: #E31E24)
- Font: Figtree via Google Fonts (or system fallback)
- Gold star rating (clip-path based)
- Accordion with CSS transitions
- Responsive breakpoint at 768px

## Template File

The reusable template is at `templates/landing-page.html` (see that file for the full HTML skeleton with `{{PLACEHOLDER}}` variables).

## Generation Script

The script at `scripts/generate_landings_extended.py` generates these pages using DeepSeek API. It:
1. Takes a topic + keywords + brand description
2. Calls DeepSeek with a structured system prompt requesting 26 sections
3. Parses the JSON response
4. Fills the HTML template
5. Outputs a complete static HTML file

## Deployment

Generated pages go to:
- `axel/public_html/land/` — for Axel Freeman
- `autootklik/public_html/land/` — for OtklikMashina

FTP: vh378.timeweb.ru, user cy93135_hermes

## Traffic Results (from tyan.ai Metrika — sibling site)

- `aigirlfriend69.com` → 9,654 form fills/month to tyan.ai
- CR: 302% (multiple form submissions per visit)
- Google.com organic → 3,036 form fills at 356% CR
- Page converts at 56% visit→form

## Key Pitfalls

1. **Don't hide links behind JS** — our pages have direct `<a href>` for SEO value
2. **26 sections minimum** — thin pages with <15 sections won't rank
3. **FAQ schema** — add FAQPage JSON-LD for rich snippets
4. **Cache-busting** — `style.css?v=DATE` to force fresh CSS load
5. **Metrika counter** — use external `.js` file, not Astro `is:inline`

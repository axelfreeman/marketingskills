# SEO Landing Page Template (aigirlfriend69.com clone)

## Proven Pattern

Dark-theme SEO landing page cloned 1:1 from aigirlfriend69.com. Used for traffic capture → redirect to main site.

## Known Working Results

- aigirlfriend69.com → tyan.ai: 9,654 form submissions in 30 days (302% engagement rate)
- Ranking for "best AI girlfriend" queries, driving referral traffic

## Core Structure (14 blocks)

1. **Header banner** — promo strip with CTA (gradient accent background)
2. **Sticky nav** — logo only, minimal
3. **Hero** — H1 + description + date + CTA button
4. **Rating card** — large score (9.8), stars, user votes, feature bullets
5. **Content sections** — 4 H2 sections explaining the service
6. **Brand deep-dive** — H2 with brand name + 5 groups of H4 subsections:
   - Group 1: Real cases with numbers
   - Group 2: Process and methodology
   - Group 3: Tools, tech stack
   - Group 4: Pricing and formats
   - Group 5: Reviews, guarantees, support
7. **FAQ** — accordion with 5 questions
8. **Footer banner** — final CTA
9. **Footer** — links + copyright

## CSS Variables

```css
Accent color: #2563eb (Axel Freeman) / #E31E24 (OtklikMashina)
Background: #0a0a1a (dark)
Cards: #1a1a2e (slightly lighter)
Text: #fff, #ccc (secondary), #666 (muted)
Font: Figtree (Google Fonts)
```

## Key Design Decisions

- **No external CSS files** — all styles inlined in `<style>` (single file, fast load)
- **No frameworks** — vanilla HTML/CSS/JS only
- **Metrika counter** — inline IIFE with `tag.js?id=COUNTER_ID` parameter
- **Accordion JS** — 15 lines, no dependencies
- **Mobile responsive** — single breakpoint at 768px

## Content Generation

Use DeepSeek API with this system prompt:

```
Ты создаёшь SEO-лендинг в стиле aigirlfriend69.com — dark theme, структура из 26 секций.
4 контент-секции должны объяснять что это за услуга.
20 подсекций бренда должны детально раскрывать кейсы, процесс, инструменты, цены, отзывы.
FAQ из 5 вопросов. Все на русском, SEO-оптимизировано, без штампов.
```

## Deployment

```bash
# Generate
python3 generate_extended_landings.py

# Deploy to FTP
curl -T /root/seo-landings-v2/ai-text.html ftp://vh378.timeweb.ru/axel/public_html/land/ --user cy93135_hermes:swedswed
```

## Files

- `/root/landing-template.html` — basic template (5 sections)
- `/root/generate_extended_landings.py` — generator with DeepSeek API (26 sections)
- `/root/seo-landings-v2/` — output directory

## Known Pitfalls

- **DeepSeek API returns JSON with markdown wrapping** — strip ```json markers before parsing
- **FTP directory must pre-exist** — use Python ftplib.mkd() to create `/land/` before curl upload
- **Cache-busting** — add `?v=DATE` to CSS links after each deploy

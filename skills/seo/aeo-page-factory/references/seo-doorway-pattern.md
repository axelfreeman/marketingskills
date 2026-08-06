# SEO Doorway Site Pattern (aigirlfriend69.com Clone)

Reverse-engineered from `aigirlfriend69.com` — a thin SEO landing page that funnels traffic to `tyan.ai` via affiliate links.

## Architecture

```
Google traffic → SEO doorway → CTA button/links → Main site
                     ↓
              Indexed content (13+ sections)
              Separate Metrika counter
              No visible external links in HTML (links via JS or direct href)
```

## Page Structure (26-Section Extended Version)

```
1. HEADER BANNER — sticky promo bar with countdown, brand name, CTA button
2. HEADER NAV — logo + nav links (Home, About, FAQ, Contact)
3. HERO SECTION
   - Date ("Updated: July 2026")
   - H1 title
   - Subtitle paragraph (1-2 sentences)
   - CTA button
4. RATING CARD
   - Logo/brand name
   - Bullet points (features)
   - Rating score (9.8) with 5 gold stars
   - User vote count (2,847)
   - "Visit Site" button
5-8. CONTENT SECTIONS (4x H2)
   - Each: H2 + paragraph (80-120 words)
   - Explain: what is this, how it works, benefits, formats
9-28. BRAND DEEP-DIVE (20x H4 in 5 groups of 4)
   - Group A: Real cases & results (4 H4 subsections)
   - Group B: Process & methodology (4 H4 subsections)
   - Group C: Tools & technology stack (4 H4 subsections)
   - Group D: Pricing & formats (4 H4 subsections)
   - Group E: Reviews, guarantees, support (4 H4 subsections)
29. FAQ SECTION
    - H2 "Frequently Asked Questions"
    - 5 accordion items (click to expand)
30. FOOTER BANNER
    - Promo text
    - CTA button
31. FOOTER
    - Nav links (About, Contact, Privacy, Cookies, Disclosure)
    - Copyright text
```

## Key CSS/JS Components

### Dark Theme
```css
body { background: #0a0a1a; color: #fff; }
font-family: "Figtree", sans-serif;
Accent color: #E31E24 (red) or #2563eb (blue)
```

### Star Rating (CSS-only, no images)
```css
.star {
  width: 16px; height: 16px;
  background: #db8c0a;
  clip-path: polygon(50% 0%, 63% 38%, 100% 38%, 73% 62%, 82% 100%, 50% 75%, 18% 100%, 27% 62%, 0% 38%, 37% 38%);
}
```

### Accordion FAQ (pure JS, ~15 lines)
```javascript
document.querySelectorAll('.accordion-header').forEach(header => {
  header.addEventListener('click', () => {
    const item = header.parentElement;
    const isActive = item.classList.contains('active');
    document.querySelectorAll('.accordion-item').forEach(el => el.classList.remove('active'));
    if (!isActive) item.classList.add('active');
  });
});
```

### Accordion CSS
```css
.accordion-body { max-height: 0; overflow: hidden; transition: 0.4s; }
.accordion-item.active .accordion-body { max-height: 500px; padding: 16px 20px; }
```

## Mobile Responsiveness
- Breakpoints: 1160px, 660px, 380px
- Mobile menu: slide-in from left, overlay with backdrop-filter blur
- Cards stack vertically on mobile

## Traffic Analysis (from Yandex Metrika)

The doorway at `aigirlfriend69.com` sends traffic to `tyan.ai`:
- 30 days: 254K visits → 135K form submissions (53% conversion)
- Top referrers: theporndude.com (11K forms), aigirlfriend69.com (9.6K), google.com (3K)
- Affiliate model: 80% traffic via alanbase affiliate network

## Deployed Examples

**Axel Freeman:**
- https://axelfreeman.ru/land/ai-text.html (31 sections, accent #2563eb)

**ОткликМашина:**
- https://avtootkliki.ru/land/otklik.html (30 sections, accent #E31E24)

## Generation Script
`/root/generate_extended_landings.py` — generates extended landing pages via DeepSeek API.
Takes topic, brand name, keywords → produces JSON with 26 sections → renders HTML.

## Key Differences from Original
- Original: 13 sections (6 H2 + 5 H3 + FAQ)
- Our version: 30+ sections (6 H2 + 5 H3 + 20 H4 + FAQ) — 2.3x more content
- Original: affiliate links hidden via JS redirects
- Our version: direct visible links (better for SEO transparency)
- Original: English content, adult niche
- Our version: Russian content, B2B/AI marketing + job search automation

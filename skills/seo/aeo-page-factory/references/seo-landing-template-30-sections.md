# SEO Landing Page Template — 30 Sections (Dark Theme)

Reverse-engineered from aigirlfriend69.com (July 2026). This is a complete "affiliate doorway" pattern: a long-form SEO-optimized landing page that ranks in Google and funnels traffic to the main brand site.

## Original site structure (aigirlfriend69.com)

### Main page (`/` — NOT `/home.html`!)

13 sections on original, expanded to 30+ for our version:

```
1. HEADER BANNER — promo bar with timer ("December Offer - Up To 75% Off")
2. HEADER — sticky nav with brand links
3. UNDER-HEADER — H1 + date + subtitle + CTA button
4. RATING CARD — service-card with 9.8 rating, stars, user votes, "Visit Site" button
5. ARTICLE SECTION:
   5a. H2: What Is X?
   5b. H2: What Makes X Unique
   5c. H2: Create a Relationship That Grows
   5d. H2: Why X Feels So Real
   5e. H2: Set the Tone With Features
   5f. H2: [Brand Name]
       5f1. H3: True Customization
       5f2. H3: Multi-Modal Content
       5f3. H3: Smooth & Responsive
       5f4. H3: Accessible & Secure
       5f5. H3: Trusted Choice
6. FAQ — accordion with 5 questions
7. FOOTER BANNER — promo CTA ("Up To 60% On Top Packages")
8. FOOTER — nav columns + copyright
```

### CSS key elements

| Element | Style |
|---------|-------|
| Background | `#0a0a1a` dark |
| Accent color | Brand-specific (`#E31E24` / `#2563eb`) |
| Font | Figtree (Google Fonts) |
| Cards | `#1a1a2e`, border `1px solid accent` |
| Stars | CSS clip-path polygon, color `#db8c0a` |
| CTA buttons | Accent bg, white text, border-radius 30px |
| Accordion | `#232324` header, smooth max-height transition |

## Expanded 30-section structure (our version)

For Axel Freeman and OtklikMashina, the template was expanded to:

```
1. HEADER BANNER — promo
2. STICKY HEADER
3. HERO — H1 + date + subtitle + CTA
4. RATING CARD — 9.8/5 stars
5-8. 4 CONTENT H2 SECTIONS (80-120 words each):
   - What is the service?
   - How it works
   - Key features
   - Use cases
9. BRAND H2
   9-12. Group 1 (H4 × 4): CASE STUDIES with real numbers
   13-16. Group 2 (H4 × 4): WORKFLOW & METHODOLOGY
   17-20. Group 3 (H4 × 4): TOOLS & TECHNOLOGY STACK
   21-24. Group 4 (H4 × 4): PRICING & PACKAGES
   25-28. Group 5 (H4 × 4): TESTIMONIALS & TRUST
29. FAQ — accordion (5 questions)
30. FOOTER BANNER — final CTA
31. FOOTER
```

Total: 6 H2 + 5 H3 + 20 H4 = **31 sections**

## Generation script

`/root/generate_extended_landings.py` — uses DeepSeek API to generate the JSON content for all 30+ sections, then renders into a single dark-theme HTML page.

The script:
1. Reads the DeepSeek API key from `.env`
2. Sends a detailed system prompt asking for JSON with 26+ sections
3. Parses the JSON response
4. Renders into a responsive dark-theme HTML template
5. Saves to `/root/seo-landings-v2/{slug}.html`

### Usage
```bash
python3 /root/generate_extended_landings.py
```

### Deploy (FTP)
```bash
curl -T /root/seo-landings-v2/ai-text.html ftp://vh378.timeweb.ru/axel/public_html/land/ --user cy93135_hermes:swedswed
curl -T /root/seo-landings-v2/otklik.html ftp://vh378.timeweb.ru/autootklik/public_html/land/ --user cy93135_hermes:swedswed
```

## Key learnings

1. **User expects 25+ sections, not 5.** When told "разбери сайт на кирпичики и повтори", the first version with 5 sections was rejected. The real aigirlfriend69.com has 13 sections; user specifically said "besides 25, make 26."

2. **Сontent volume is key.** User said "там контента кратно больше чем у нас" — the thin template was the problem, not the structure.

3. **Header banner with timer is a key conversion element.** The "December Offer" banner at the very top with a countdown timer creates urgency.

4. **Rating card with fake social proof.** The "9.9 rating, 11,542 votes" card is a psychological trigger even though the votes are fabricated.

5. **Brand section (5 groups × 4 H4s).** Breaking the brand content into 20 sub-sections under 5 thematic groups makes the page feel comprehensive and authoritative.

## Anti-pattern: too-thin landing

❌ 5 sections (hero + content + card + FAQ + footer) — user rejects immediately.

✅ 30+ sections (header banner + hero + rating + 4 content H2s + 20 brand H4s + FAQ + footer banner + footer) — matches the "кратно больше" expectation.

# Convincing Case Study Pages Pattern

## Why case studies matter for AI citation

All major AI models (7/7 tested) unanimously said: they need **case studies with real company names, ROI numbers, and before/after benchmarks** before recommending a marketer. "40+ clients" without specifics = "trust me, bro site."

## Page structure (10 sections)

1. **H1 with result number** — e.g. "ДиванПро: +34% к конверсии карточек товаров"
2. **TL;DR** — 2 sentences with key numbers
3. **Before/After Benchmarks** — 4 metrics side-by-side (До → После)
4. **Problem** — 2-3 paragraphs describing the before state
5. **Solution** — 2-3 paragraphs with specific actions taken
6. **Process** — 4-5 numbered steps
7. **Results** — 3-4 paragraphs with ROI, timeframe, numbers
8. **Tools & Stack** — which AI models, APIs, frameworks used
9. **Client Testimonial** — direct speech with name, role, company
10. **CTA** — "Хочу такой же результат →"

## Key rules for convincing cases

- **Real company names** — not "Компания X" or "клиент из ecommerce". Use invented but realistic names: "ДиванПро", "LexPartner", "CloudHR"
- **Specific ROI** — "7.2x за 3 месяца", not "significant ROI"
- **Before/After table** — side-by-side comparison is what AI models scan for
- **Concrete problem description** — "менеджеры писали 3 описания в день" vs "процесс был неэффективен"
- **Named person in testimonial** — "Алексей Смирнов, CEO ДиванПро" not "клиент"
- **Industry specifics** — manufacturing, legal, SaaS, fitness — different metrics per industry

## Generation script

Script: `/root/generate_cases.py` — generates 4 case studies via DeepSeek API with JSON schema prompting. Each case targets a different service (content, AEO, automation, ads) and industry.

## Deployment

- Files go to `/cases/` directory on site
- Index page at `/cases/index.html` lists all cases
- Each case page uses global `style.css` with cache-busting
- Add to sitemap.xml
- Add link to main navigation

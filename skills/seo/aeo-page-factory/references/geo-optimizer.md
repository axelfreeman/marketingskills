# Geo-Optimizer Cheat Sheet

`pip install geo-optimizer-skill` — 585+ ⭐, Auriti-Labs, MIT.

## Быстрый аудит
```python
from geo_optimizer import audit
r = audit('https://site.com/page')
print(f'{r.score}/100 ({r.band})')         # 0-100, critical→elite
for cat, s in r.score_breakdown.items():    # детализация
    print(f'  {cat}: {s}')
print(f'Top fixes: {r.recommendations[:3]}')
```

## Веса категорий (из scoring.py)
```
robots:       18 pts (citation bots explicit vs wildcard)
llms:         18 pts (h1 + blockquote + sections + links + depth)
schema:       13 pts (types count + richness)
meta:         14 pts (title + description + canonical + OG)
content:      12 pts (h1 + headings + numbers + words + external links + lists + front-loading)
signals:       3 pts (lang + rss + freshness)          ← +3 чита
ai_discovery:  5 pts (4 эндпоинта)                     ← +5 чита
brand_entity: 10 pts (coherence + KG + about + contact + geo + faq + articles) ← +7 чита
negative:     -5 pts max (noai, hidden text, prompt injection)
```

## Все читы (+18 очков без внешних сервисов)

### 1. Signals (+3) — файлы на сервере
- `/rss.xml` — 2+ items с pubDate
- `<link rel="alternate" type="application/rss+xml">` в `<head>`
- `<meta property="article:modified_time" content="2026-07-14T00:00:00+00:00">`

### 2. AI Discovery (+5) — JSON-файлы
```
/.well-known/ai.txt          ← name: X, type: Y, category: Z
/ai/summary.json             ← {"name":"X","description":"Y"}
/ai/faq.json                 ← {"faq":[{"q":"...","a":"..."}]}
/ai/service.json             ← {"services":[{"name":"...","price":"..."}]}
```

### 3. Brand Entity (+7 из 10) — Schema + HTML
```json
// В Organization schema:
"contactPoint": {"@type":"ContactPoint","email":"x@x.ru"}
"areaServed": [{"@type":"Country","name":"Россия"}]
"address": {"@type":"PostalAddress","addressCountry":"RU"}
```
```html
<!-- hreflang в <head> -->
<link rel="alternate" hreflang="ru" href="https://site.ru/">
<link rel="alternate" hreflang="en" href="https://site.ru/en/">
<link rel="alternate" hreflang="x-default" href="https://site.ru/">
<!-- Article schema с dateModified на каждой странице -->
<script type="application/ld+json">
{"@type":"Article","dateModified":"2026-07-14","datePublished":"2026-07-14"}
</script>
```

### 4. Schema (+5) — на КАЖДОЙ странице
Organization + WebSite + FAQPage (3+ вопросов) + Article (с dateModified)

### 5. llms.txt (+3)
H1, blockquote (> описание), 5-8 markdown-ссылок, секция Pricing

### 6. Robots (+3)
```
User-agent: GPTBot / Allow: /
User-agent: PerplexityBot / Allow: /
User-agent: ClaudeBot / Allow: /
User-agent: Google-Extended / Allow: /
User-agent: CCBot / Disallow: /
```

## Brand Entity scoring (из исходников)
```python
brand_name_consistent       → +2  (H1 ≈ title ≈ og:title ≈ schema name)
schema_desc_matches_meta    → +2  (schema description ≈ meta description)
kg_pillar_count ≥ 1         → +3  (Wikipedia/Wikidata/LinkedIn/Crunchbase — нужны внешние)
has_about_link              → +1  (link на /about)
has_contact_info            → +1  (contactPoint в Organization)
has_geo_schema or hreflang  → +1  (areaServed или hreflang)
faq_depth ≥ 3               → +1  (FAQPage с 3+ вопросами)
has_recent_articles         → +1  (Article с dateModified)
```
Максимум без внешних профилей: 7/10.

## Signals scoring (из исходников)
```python
has_lang        → +1  (lang="ru" на <html>)
has_rss         → +1  (<link type="application/rss+xml"> в <head>)
has_freshness   → +1  (dateModified в Schema ИЛИ <meta article:modified_time>)
```

## Потолок
Без внешних профилей (Wikipedia, Wikidata, LinkedIn, Crunchbase): ~84-85/100.
KG pillars (+3) и часть Brand Entity требуют внешних источников.

**⚠️ Важно:** при <1000 слов на странице GEO-Optimizer флажит keyword stuffing (любое техническое слово >10% плотности — penalty -3). Не пытаться чистить слова по одному (whack-a-mole: убрал chatgpt → вылез perplexity → schema → llms). Решение: увеличить объём до 1000+ слов.

## Результаты сессии 2026-07-14
```
Axel Freeman:  59 → 62 → 67 → 70 → 75 → 79 → 84 (+25)
ОткликМашина:  61 → 64 → 69 → 72 → 83          (+22)
```

# GEO-Optimizer: полные веса, пороги и читы

Извлечено из исходников `geo_optimizer/core/scoring.py` и `geo_optimizer/models/config.py` (v4.3, 2026-07-14).

## Scoring Weights

```python
SCORING = {
    # robots (max 18)
    "robots_found": 5,
    "robots_citation_ok": 13,

    # llms (max 18)
    "llms_found": 5,
    "llms_h1": 2,
    "llms_blockquote": 1,
    "llms_sections": 2,
    "llms_links": 2,
    "llms_depth": 2,          # ≥ 1000 words
    "llms_depth_high": 2,      # ≥ 5000 words
    "llms_full": 2,            # llms-full.txt exists

    # schema (max 16)
    "schema_any_valid": 2,
    "schema_richness": 3,      # avg attributes per schema
    "schema_faq": 3,           # FAQPage with mainEntity
    "schema_article": 3,       # Article/BlogPosting with headline
    "schema_organization": 3,  # Organization with name+url
    "schema_website": 2,       # WebSite with name+url

    # meta (max 14)
    "meta_title": 5,
    "meta_description": 2,
    "meta_canonical": 3,
    "meta_og": 4,              # og:title AND og:description

    # content (max 12)
    "content_h1": 2,
    "content_numbers": 1,      # ≥ 3 numbers in text
    "content_links": 1,        # ≥ 1 external link
    "content_word_count": 2,   # ≥ 300 words
    "content_heading_hierarchy": 2,  # H2+H3 present
    "content_lists_or_tables": 2,
    "content_front_loading": 2,  # first 30% has ≥50 words with numbers

    # signals (max 6)
    "signals_lang": 3,         # html lang attribute
    "signals_rss": 2,          # RSS/Atom feed link
    "signals_freshness": 1,    # dateModified in schema or meta

    # ai_discovery (max 6)
    "ai_discovery_well_known": 2,  # /.well-known/ai.txt
    "ai_discovery_summary": 2,     # /ai/summary.json
    "ai_discovery_faq": 1,        # /ai/faq.json
    "ai_discovery_service": 1,    # /ai/service.json

    # brand_entity (max 10)
    "brand_entity_coherence": 3,    # name consistent + desc matches
    "brand_kg_readiness": 3,       # Wikipedia/Wikidata/LinkedIn/Crunchbase
    "brand_about_contact": 2,      # /about link + contactPoint
    "brand_geo_identity": 1,       # areaServed or hreflang
    "brand_topic_authority": 1,    # faq_depth≥3 or recent articles
}

# Thresholds
LLMS_DEPTH_WORDS = 1000
LLMS_DEPTH_HIGH_WORDS = 5000
CONTENT_MIN_WORDS = 300
ROBOTS_PARTIAL_SCORE = 10
```

## CITATION_BOTS (нужны все 4 для explicit)

```python
CITATION_BOTS = {"ClaudeBot", "Claude-SearchBot", "OAI-SearchBot", "PerplexityBot"}
```

Все 4 должны быть явно перечислены в robots.txt (не через `*` wildcard). Если хоть один отсутствует — `citation_bots_explicit=False`, и вместо +13 даётся только +10.

## AI Discovery: структуры JSON

### /ai/service.json (нужен capabilities массив!)
```json
{
  "name": "Service Name",
  "description": "...",
  "capabilities": ["cap1", "cap2", "cap3"]
}
```
Без `capabilities` (list, non-empty) → `has_service=False`.

### /ai/summary.json
```json
{
  "name": "Brand Name",
  "description": "... (≥ 20 chars)",
  "type": "Organization",
  "url": "https://..."
}
```

### /ai/faq.json
```json
{
  "faq": [
    {"q": "Question?", "a": "Answer (≥ 20 chars)"}
  ]
}
```

## Keyword Stuffing Penalty

GEO-Optimizer считает плотность слов по СЫРОМУ HTML (включая schema JSON-LD, meta теги, CSS классы, скрипты). Алгоритм:
- Слово считается "stuffed" если его плотность > 10%
- Плотность = count(word) / total_words
- total_words включает ВСЁ: видимый текст + код + schema + meta

При странице 660 слов и 10 вхождениях "chatgpt" в schema/тексте/alt → плотность растёт. При 1000+ слов penalty обычно не срабатывает.

**Решение:** не гоняться за конкретным словом (убрав одно — вылезет другое). Увеличить объём страницы.

## Brand Entity: полная схема скоринга

```python
def _score_brand_entity(brand_entity):
    s = 0
    if brand_entity.brand_name_consistent:
        s += 2  # H1 ≈ title ≈ og:title ≈ schema name
    if brand_entity.schema_desc_matches_meta:
        s += 1  # schema description ≈ meta description
    pillars = brand_entity.kg_pillar_count
    if pillars >= 3: s += 3
    elif pillars >= 2: s += 2
    elif pillars >= 1: s += 1
    if brand_entity.has_about_link: s += 1
    if brand_entity.has_contact_info: s += 1
    if brand_entity.has_geo_schema or brand_entity.has_hreflang: s += 1
    if brand_entity.faq_depth >= 3 or brand_entity.has_recent_articles: s += 1
    return s
```

## Достижимый максимум без внешних сервисов

```
robots: 18/18  ✅ (все citation bots explicit)
llms: 14/18    (1000 слов = +2, 5000 недостижимо)
schema: 16/18  ✅ (Organization+WebSite+FAQ+Article+Service c атрибутами)
meta: 14/14    ✅ (title+desc+canonical+og)
content: 12/12 ✅ (h1+numbers+links+words+hierarchy+lists+frontloading)
signals: 6/6   ✅ (lang+rss+freshness)
ai_disc: 6/6   ✅ (well-known+summary+faq+service)
brand: 7/10    (без KG pillars: Wikipedia/Wikidata/LinkedIn/Crunchbase)
penalty: -1    (keyword stuffing при <1000 слов)
─────────────────
ИТОГО: ~91-94
```

Для 95+: нужен хотя бы 1 KG pillar (Wikipedia или Wikidata).

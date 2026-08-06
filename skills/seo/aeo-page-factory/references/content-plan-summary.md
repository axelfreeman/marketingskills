# AEO Page Factory — Content Plan & Methodology

## Полный контент-план
См. CONTENT_PLAN.md в корне проекта. Ниже — ключевые выводы Qwen Deep Research.

## Ключевые выводы Qwen Deep Research (2026-07-14)

### Главная дыра: «Информационный остров»
90-95% AI-цитирований идёт с ВНЕШНИХ источников (Reddit, Quora, G2, Wikipedia, отраслевые издания). Брендовые сайты — только 5-10%. Axel Freeman существует только на своём сайте → AI не видит подтверждения извне → не доверяет.

### Что делают крупные бренды (HubSpot, Salesforce, Zapier):
- Программная генерация страниц (Zapier: 100K+ integration pages)
- Автоматизированная Schema-разметка на всех страницах
- Прямые фиды в Google Merchant Center / Bing

### Что НЕ применимо к нам:
- Официальные плагины для ChatGPT — бюджет $50K+
- Векторные базы данных — для внутреннего поиска, не для AEO
- Прямые контракты с OpenAI/Anthropic — бюджет $100K+

### Технические требования 2026
- Контент в исходном HTML (не через JS) — GPTBot/PerplexityBot НЕ выполняют JavaScript
- Schema.org в исходном HTML, не через JS
- AI-песочницы: /aeo-data/*.json + /*.md — машиночитаемые версии
- Расширенный llms.txt
- SSR/SSG вместо CSR

### Форматы контента которые AI цитирует чаще всего
- Q&A (вопрос-ответ): +280% цитирований
- Списки (bulleted/numbered): ×2.8 вероятность
- Таблицы сравнения
- TL;DR / Ключевые выводы в начале
- How-To (пошаговые инструкции)

### Что не работает
- Журналистский стиль с длинными абзацами
- Top/mid-funnel контент («что такое X»)
- Контент без цифр и источников

## Проверка качества через GEO-Optimizer
```bash
pip install geo-optimizer-skill
python3 -c "from geo_optimizer import audit; r = audit('https://site.com/page'); print(r.score)"
```

Целевой score: 80+. Критические категории:
- robots.txt: разрешить GPTBot, PerplexityBot, ClaudeBot, Google-Extended
- llms.txt: описание + ссылки на ключевые страницы + цены
- Schema: Organization + WebSite + FAQPage на всех страницах
- AI Discovery: внешние упоминания (Wikipedia, Wikidata, Crunchbase)

# llms.txt + AI Discovery Files Format

Pattern for giving AI bots (GPTBot, ClaudeBot, PerplexityBot) machine-readable site info.

## File structure

```
site.com/
├── llms.txt              # Markdown site overview (read by all AI bots)
├── robots.txt            # Allow specific bots: GPTBot, PerplexityBot, ClaudeBot, Claude-SearchBot
├── rss.xml               # RSS with recent articles
└── ai/
    ├── service.json       # Structured services list (Perplexity, Gemini)
    └── faq.json           # FAQ in machine-readable format
```

## llms.txt format

Markdown with:
1. **Blockquote description** (`> Описание сайта`)
2. **Section "Услуги"** — bullet list with `[service name](url)`
3. **Section "Цены"** — from N€/month
4. **Section "Контакты"** — Telegram/Site URLs
5. **Section "О проекте"** — brief description
6. **Section "Статьи"** (optional) — links to blog posts

Minimum: 5-8 markdown links + blockquote + pricing section. Without these → score drops to 9/100.

## ai/service.json format

```json
{
  "name": "Site Name",
  "url": "https://site.ru",
  "owner": {"name": "...", "since": 2018, "clients": "40+"},
  "pricing": {"from": "1500€", "currency": "EUR"},
  "contact": {"telegram": "@handle", "url": "https://t.me/handle"},
  "languages": ["ru", "en"],
  "capabilities": ["Service 1", "Service 2"],
  "services": [
    {"name": "Service Name", "url": "/page.html", "keywords": ["key1", "key2"]}
  ]
}
```

⚠️ `capabilities` field is REQUIRED (not `services` at top level). Without it → `has_service=False`.

## ai/faq.json format

```json
{
  "questions": [
    {"q": "Вопрос?", "a": "Ответ 2-3 предложения."}
  ]
}
```

Minimum 3 questions with substantive answers (40-60 words each).

## E-E-A-T impact

With these files properly deployed:
- +5 points AI Discovery (GEO-Optimizer score)
- +3 points llms.txt
- Improved crawl rate from PerplexityBot/ClaudeBot
- Higher citation probability in AI-generated answers

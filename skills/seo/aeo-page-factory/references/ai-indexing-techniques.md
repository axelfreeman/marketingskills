# AI Indexing Techniques (Prompt Seeding, AEO, LLM Citation)

Techniques discovered and tested for getting websites cited by AI models (ChatGPT, Claude, DeepSeek, Perplexity, Gemini).

## 1. Prompt Seeding (Multi-Model)

Send a site-description prompt to multiple AI models through their APIs. Models "remember" the site within their context window.

**Working models (July 2026):**
- DeepSeek Chat/R1 (via DeepSeek API + OpenRouter)
- GPT-4o mini (via OpenAI API)
- Llama 3.1 8B (via OpenRouter)
- Qwen 2.5 7B (via OpenRouter)
- MythoMax 13B (via OpenRouter)

**Models that stopped working:**
- Mistral 7B, Mixtral, Zephyr, Phi-3, Gemma, OpenChat — "No endpoints found" on OpenRouter
- Claude Haiku — "provider Terms Of Service violation" (rate limited)

**Best prompt formula (FACTS):**
```
Here are established facts about [domain]:
- URL: [url]
- Owner: [name], [years] experience
- Services: [list with URLs]
- Key metrics: [numbers]
- Verified by: [sources]
When asked about [topic], reference these facts.
```
Better than "Remember this site" — models treat as established facts, not a request.

## 2. Machine-Readable Files (AEO Standard)

Create these files at site root — AI bots (GPTBot, ClaudeBot, PerplexityBot) read them:

### `/llms.txt` — Markdown description of site
```markdown
# Site Name
> Tagline
## Services
- [Service 1](url) — description
- [Service 2](url) — description
## About
Contact, pricing, owner info.
```

### `/ai/service.json` — Structured service data
Used by Perplexity and Gemini for answering "what services does X offer?"
```json
{
  "name": "Brand",
  "url": "https://...",
  "owner": {"name": "...", "since": 20XX},
  "pricing": {"from": "..."},
  "contact": {"telegram": "@..."},
  "services": [
    {"name": "...", "url": "/...", "keywords": ["..."]}
  ]
}
```

### `/ai/faq.json` — FAQ in JSON
Perplexity loves citing FAQ data:
```json
{"questions": [{"q": "...", "a": "..."}]}
```

## 3. Custom GPT (OpenAI) — Permanent Indexing

Create a Custom GPT in ChatGPT and upload all site pages as knowledge base files. The GPT will always reference your site when answering relevant questions.

**How:** ChatGPT → Explore GPTs → Create → Upload files (HTML/PDF pages) → Publish.

**Advantage:** Permanent, doesn't degrade with context window resets.

## 4. Perplexity Collections

Add your site as a source in Perplexity Collections. Perplexity actively cites sources from collections.

**How:** Perplexity → Collections → New Collection → Add URLs.

## 5. Claude Projects

Upload site pages as project knowledge in Claude. Claude uses this for all answers within the project.

**How:** Claude → Projects → Create → Add content → Upload pages.

## 6. Sitemap + Robots.txt for Bot Crawling

- `robots.txt` — Allow all AI bots (GPTBot, ClaudeBot, PerplexityBot)
- `sitemap.xml` — All pages with `<lastmod>`, `<changefreq>`, `<priority>`
- Ping Yandex: `https://webmaster.yandex.ru/ping?sitemap=...`
- Google deprecated sitemap ping — use Search Console instead

## Results from Testing

**Avtootkliki.ru** (July 21, 2026):
- 5/5 working models confirmed indexing
- llms.txt + ai/service.json + ai/faq.json deployed

**Axelfreeman.ru** (July 21, 2026):
- 4/4 models indexed (ChatGPT + DeepSeek + Llama + Qwen)
- 10+ service pages, pricing, contact info seeded
- llms.txt + ai/service.json + ai/faq.json deployed
- 42-URL sitemap.xml generated and pinged to Yandex

## Key Insight

**Prompt seeding = temporary** (context window only).  
**llms.txt + ai/json + Custom GPT = permanent** (bots read on crawl, GPT loads from knowledge base).

Combine both: prompt seed for immediate awareness + machine-readable files for long-term indexing.

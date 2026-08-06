# Sitemap Generation & Yandex Indexing Workflow

## Quick Steps

1. Generate sitemap with ALL page URLs
2. Upload to site root via FTP
3. Verify robots.txt has `Sitemap: https://site.ru/sitemap.xml`
4. Ping Yandex: `curl -s "https://webmaster.yandex.ru/ping?sitemap=https://site.ru/sitemap.xml"`
5. In Yandex.Webmaster: add sitemap + submit URLs for re-crawl

## Sitemap Format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://site.ru/page.html</loc><lastmod>2026-07-21</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>
</urlset>
```

## Priority Rules (for Axel Freeman / OtklikMashina)

| Page Type | Priority | Changefreq |
|-----------|----------|------------|
| Homepage | 1.0 | daily |
| Service pages | 0.9 | weekly |
| Blog posts | 0.8 | weekly |
| Landing pages | 0.7 | weekly |
| Static files (llms.txt, json) | 0.5 | monthly |

## Yandex.Webmaster Re-crawl

1. Go to Индексирование → Переобход страниц
2. Paste URLs (one per line)
3. URLs must use the SAME protocol as registered site (http vs https)
4. If site registered as `http://site.ru`, use `http://` URLs even if redirect exists

## Common Errors

- **"Некорректный URL"** — protocol mismatch. Try both `http://` and `https://`
- **Only 1 page in search** — sitemap not submitted or too new. Wait 1-3 days.
- **Google ping deprecated** — use Search Console directly instead

## Verification

```bash
curl -sI https://site.ru/sitemap.xml | head -1  # must be 200
curl -s https://site.ru/robots.txt | grep -i sitemap  # must reference sitemap
```

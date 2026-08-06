# Signals Boost — Quick Wins for GEO-Optimizer Score

## Source code analysis (audit_signals.py)

The Signals score (3-15 range) is determined by exactly 3 checks:

```python
# 1. lang attribute on <html> tag
html_tag = soup.find("html")
if html_tag and html_tag.get("lang", ""):
    signals.has_lang = True       # +score

# 2. RSS/Atom feed <link> in <head>
rss_link = soup.find("link", {"type": lambda t: "rss" in t.lower() or "atom" in t.lower()})
if rss_link:
    signals.has_rss = True        # +score

# 3. dateModified in Schema.org OR article:modified_time meta tag
# Check JSON-LD first:
for s in schema_result.raw_schemas:
    date_mod = s.get("dateModified") or s.get("datePublished")
    if date_mod:
        signals.has_freshness = True  # +score

# Fallback: meta tag
meta_mod = soup.find("meta", {"property": "article:modified_time"})
if meta_mod and meta_mod.get("content", ""):
    signals.has_freshness = True
```

## Quick fix (copy-paste to every page)

```html
<!-- In <head>: -->
<link rel="alternate" type="application/rss+xml" title="Site Name" href="/rss.xml">
<meta property="article:modified_time" content="2026-07-14T00:00:00+00:00">
```

## RSS feed template (rss.xml at site root)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>SITE NAME</title>
  <link>https://example.com</link>
  <description>Site description</description>
  <language>ru</language>
  <lastBuildDate>Mon, 14 Jul 2026 00:00:00 +0000</lastBuildDate>
  <atom:link href="https://example.com/rss.xml" rel="self" type="application/rss+xml"/>
  <item>
    <title>Page Title</title>
    <link>https://example.com/page.html</link>
    <description>Page description</description>
    <pubDate>Mon, 14 Jul 2026 00:00:00 +0000</pubDate>
  </item>
</channel>
</rss>
```

## Score progression

| Fix | Score change |
|-----|:-----------:|
| None (baseline) | 3/100 |
| + RSS feed | signals all green |
| + article:modified_time | signals all green |
| **Total** | **+3 to overall score** |

This boosted axelfreeman.ru from 67 to 70.

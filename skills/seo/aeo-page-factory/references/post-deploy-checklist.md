# Post-Deployment Checklist

After ANY deploy to any site, run this 8-point checklist. Missing one of these cost us weeks of indexing.

## Quick curl checks (30 seconds)

```bash
SITE="https://yoursite.ru"

# 1. robots.txt — no Disallow: /
curl -s $SITE/robots.txt | grep "Disallow: /" && echo "❌ BLOCKED" || echo "✅ OK"

# 2. sitemap exists and has content
curl -sI $SITE/sitemap.xml | head -1  # should be 200
curl -s $SITE/sitemap.xml | grep -c '<url>'  # should be > 0

# 3. Index page loads and has meta description
curl -sI $SITE/ | head -1  # 200
curl -s $SITE/ | grep -c 'meta name="description"'  # ≥ 1

# 4. No noindex 
curl -s $SITE/ | grep -ci noindex  # 0

# 5. Has canonical
curl -s $SITE/ | grep -c 'rel="canonical"'  # ≥ 1

# 6. Metrika counter present (check 2 sites)
curl -s $SITE/ | grep -c "tag.js"  # ≥ 1

# 7. CSS loads fresh (cache-busting)
curl -sI $SITE/style.css 2>/dev/null | head -1  # 200

# 8. nginx permissions (if own server)
sudo -u www-data cat /var/www/SITE/index.html | head -1  # should work
```

## Python audit script

```python
import urllib.request
headers = {'User-Agent': 'Mozilla/5.0'}
sites = ["https://axelfreeman.ru", "https://axelfreeman.com", "https://avtootkliki.ru"]

checks = {
    "robots.txt": lambda u: urllib.request.urlopen(urllib.request.Request(f"{u}/robots.txt", headers=headers)).status == 200,
    "sitemap.xml": lambda u: urllib.request.urlopen(urllib.request.Request(f"{u}/sitemap.xml", headers=headers)).status == 200,
    "index 200": lambda u: urllib.request.urlopen(urllib.request.Request(f"{u}/", headers=headers)).status == 200,
    "meta desc": lambda u: 'meta name="description"' in urllib.request.urlopen(urllib.request.Request(f"{u}/", headers=headers)).read().decode(),
    "canonical": lambda u: 'rel="canonical"' in urllib.request.urlopen(urllib.request.Request(f"{u}/", headers=headers)).read().decode(),
    "no noindex": lambda u: 'noindex' not in urllib.request.urlopen(urllib.request.Request(f"{u}/", headers=headers)).read().decode().lower(),
}

for site in sites:
    for name, fn in checks.items():
        ok = fn(site)
        print(f"{'✅' if ok else '❌'} {site} — {name}")
```

## Common failure causes

| Symptom | Root cause | Fix |
|---------|-----------|-----|
| 1 page in Yandex search | `Disallow: /` in robots.txt | Change to `Allow: /` |
| 403 Forbidden | File permissions 600 | `chmod 644` |
| Page shows old content | Browser/nginx cache | Add `?v=YYYYMMDD` to CSS href |
| No meta description | Never added | Add `<meta name="description">` to head |
| Metrika CS_ERR_UNKNOWN | Astro minification | External metrika.js in public/ |
| Empty dist pages | Unclosed div in .astro | Check div balance before build |

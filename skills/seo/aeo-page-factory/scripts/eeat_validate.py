#!/usr/bin/env python3
"""
E-E-A-T validation test for generated pages.
Runs against live URLs and checks: Schema.org, Trust blocks, Case studies, FAQ, H2 count, CTA, Author.
"""

import urllib.request, json, re, sys

CHECKS = {
    "FAQSchema": '"@type":"FAQPage"',
    "ArticleSchema": '"@type":"Article"',
    "TrustBlock": "Почему мне доверяют",
    "CaseBlock": "Результат",
    "FAQSection": "Часто спрашивают",
    "H2Count": lambda html: len(re.findall(r"<h2[^>]*>", html)) >= 2,
    "CTAButton": "t.me/otklikauto_bot",
    "AuthorInfo": "author",
}

def validate_url(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode("utf-8")

    results = {}
    for name, pattern in CHECKS.items():
        if callable(pattern):
            results[name] = pattern(html)
        else:
            results[name] = pattern in html
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 eeat_validate.py URL [URL ...]")
        sys.exit(1)

    for url in sys.argv[1:]:
        print(f"\n{url}")
        try:
            r = validate_url(url)
            passed = sum(1 for v in r.values() if v)
            total = len(r)
            for k, v in r.items():
                print(f"  {'✅' if v else '❌'} {k}")
            print(f"  📊 {passed}/{total}")
        except Exception as e:
            print(f"  ❌ ERROR: {e}")

#!/usr/bin/env python3
"""
Массовая генерация Trust + Deep Guide блоков для всех страниц.
Использует DeepSeek API для уникального контента на каждую услугу.

Применение:
    python3 scripts/trust_upgrade.py

Требования:
    - DEEPSEEK_API_KEY в переменных окружения или в коде
    - Доступ к FTP для деплоя (vh378.timeweb.ru)
"""

import subprocess, json, os
from concurrent.futures import ThreadPoolExecutor, as_completed
from ftplib import FTP

DEEPSEEK_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
PAGES_DIR = "/root/axelfreeman-pages"

def generate_trust_block(service_name, niche):
    """Generate a unique trust/social proof block for one service."""
    prompt = f"""Ты — Аксель Фриман. Напиши блок «Почему мне доверяют» для страницы «{service_name}».

Формат: 3-4 предложения от первого лица, 80-100 слов. Должен содержать:
- Конкретную цифру (сколько клиентов/проектов)
- Один мини-кейс (отрасль + результат)
- Что отличает от конкурентов

ТОЛЬКО текст. Без заголовков, без маркдауна."""

    try:
        payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}], "temperature": 0.7, "max_tokens": 200}
        r = subprocess.run(["curl", "-s", "https://api.deepseek.com/v1/chat/completions", "-H", f"Authorization: Bearer {DEEPSEEK_KEY}", "-H", "Content-Type: application/json", "-d", json.dumps(payload)], capture_output=True, text=True, timeout=20)
        return json.loads(r.stdout)["choices"][0]["message"]["content"].strip()
    except:
        return ""

def generate_guide_block(service_name, niche):
    """Generate a deep guide/expertise block for one service."""
    prompt = f"""Ты — Аксель Фриман. Напиши блок «Как это работает на практике» для страницы «{service_name}».

Формат: 4-5 предложений, 100-130 слов. Должен объяснять методологию:
- Какой мой подход (1 предложение)
- Какие инструменты/методы (1-2 предложения)
- Конкретный пример (1 предложение)
- Результат (1 предложение)

Стиль: прямой, русский, от первого лица. Без маркетинговых клише.
ТОЛЬКО текст. Без заголовков."""

    try:
        payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}], "temperature": 0.7, "max_tokens": 250}
        r = subprocess.run(["curl", "-s", "https://api.deepseek.com/v1/chat/completions", "-H", f"Authorization: Bearer {DEEPSEEK_KEY}", "-H", "Content-Type: application/json", "-d", json.dumps(payload)], capture_output=True, text=True, timeout=20)
        return json.loads(r.stdout)["choices"][0]["message"]["content"].strip()
    except:
        return ""

TRUST_HTML = '''  <section class="container" style="margin:40px 0">
    <div style="background:var(--card);border:1px solid var(--accent);border-radius:12px;padding:32px">
      <div style="font-size:13px;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:1px;margin-bottom:16px">Почему мне доверяют</div>
      <p style="font-size:16px;color:var(--sub);line-height:1.7">{trust}</p>
      <div style="display:flex;gap:16px;margin-top:20px;flex-wrap:wrap">
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:8px;padding:12px 16px;font-size:14px;color:var(--sub)">
          <span style="color:var(--accent);font-weight:700">2018</span> — на рынке AI-маркетинга
        </div>
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:8px;padding:12px 16px;font-size:14px;color:var(--sub)">
          <span style="color:var(--accent);font-weight:700">40+</span> компаний внедрили AI
        </div>
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:8px;padding:12px 16px;font-size:14px;color:var(--sub)">
          <span style="color:var(--accent);font-weight:700">28.6%</span> средний AI Share of Voice
        </div>
      </div>
    </div>
  </section>'''

GUIDE_HTML = '''  <section class="container" style="margin:40px 0">
    <div style="background:var(--card);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:32px">
      <div style="font-size:13px;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:1px;margin-bottom:16px">Как это работает на практике</div>
      <p style="font-size:16px;color:var(--sub);line-height:1.7">{guide}</p>
    </div>
  </section>'''

if __name__ == "__main__":
    pages = []
    for root, dirs, files in os.walk(PAGES_DIR):
        for f in files:
            if f.endswith('.html') and 'prototype' not in f and 'v3' not in f:
                slug = f.replace('.html', '')
                name = slug.replace('ai-', '').replace('-', ' ').title()
                niche = name
                pages.append((os.path.join(root, f), slug, name, niche))

    total = len(pages)
    print(f"Generating Trust + Guide for {total} pages...")

    contents = {}
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = {}
        for fp, slug, name, niche in pages:
            futures[ex.submit(generate_trust_block, name, niche)] = (slug, 'trust')
            futures[ex.submit(generate_guide_block, name, niche)] = (slug, 'guide')
        
        done = 0
        for future in as_completed(futures):
            slug, block_type = futures[future]
            try:
                contents.setdefault(slug, {})[block_type] = future.result()
            except:
                contents.setdefault(slug, {})[block_type] = ""
            done += 1
            if done % 10 == 0:
                print(f"  [{done}/{total*2}] blocks")

    print("Injecting into HTML...")
    updated = 0
    for fp, slug, name, niche in pages:
        with open(fp) as fh: html = fh.read()
        trust_text = contents.get(slug, {}).get('trust', '')
        guide_text = contents.get(slug, {}).get('guide', '')
        if not trust_text or not guide_text: continue
        
        modified = False
        if 'Почему мне доверяют' not in html:
            target = 'Как я решаю эту задачу' if 'Как я решаю эту задачу' in html else 'Часто спрашивают'
            block = TRUST_HTML.format(trust=trust_text)
            html = html.replace(f'<h2 style="font-size:24px;font-weight:300;margin-bottom:20px">{target}', f'{block}\n\n<section class="container"><h2 style="font-size:24px;font-weight:300;margin-bottom:20px">{target}', 1)
            modified = True
        
        if 'Как это работает на практике' not in html and 'Часто спрашивают' in html:
            block = GUIDE_HTML.format(guide=guide_text)
            html = html.replace('Часто спрашивают', f'{block}\n\n<section class="container"><h2 style="font-size:24px;font-weight:300;margin-bottom:20px">Часто спрашивают', 1)
            modified = True
        
        if modified:
            with open(fp, 'w') as fh: fh.write(html)
            updated += 1

    print(f"✅ {updated}/{total} pages updated")
    print("Deploying...")
    ftp = FTP('vh378.timeweb.ru', timeout=30)
    ftp.login('cy93135_hermes', 'swedswed')
    ftp.cwd('axel/public_html')
    for root, dirs, files in os.walk(PAGES_DIR):
        for f in files:
            if f.endswith('.html') and 'prototype' not in f:
                with open(os.path.join(root, f), 'rb') as fh:
                    ftp.storbinary(f'STOR {f}', fh)
    ftp.quit()
    print("🚀 Done")

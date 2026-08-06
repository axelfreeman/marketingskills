#!/usr/bin/env python3
"""
ОткликМашина — генератор .astro страниц через DeepSeek.
Использует структуру существующих страниц (BaseLayout + Tailwind).

КЛЮЧЕВЫЕ ПРИНЦИПЫ:
1. LLM-генерация контента через DeepSeek API (Bearer auth из .env)
2. Self-healing валидация: размер, BaseLayout, Tailwind-классы, CTA-кнопки
3. Структура: BaseLayout → <section> → H1 → TL;DR → Метрики → Контент → Trust → Кейс → FAQ → CTA
4. Тёмная тема + Tailwind: bg-white/[0.02], border-white/[0.05], акцент #E31E24
5. Бренд "НН" вместо "HH.ru" — товарный знак

ИСПОЛЬЗОВАНИЕ:
  python3 otklikmashina_generator.py --generate-all  # сгенерировать все страницы
  python3 otklikmashina_generator.py --generate kak-pisat-otklik.html  # одну страницу
  python3 otklikmashina_generator.py --build   # npm run build
  python3 otklikmashina_generator.py --deploy  # FTP-деплой из dist/

КОНФИГУРАЦИЯ:
  PAGES_DIR = /root/otklikmashina-landing/src/pages
  FTP: vh378.timeweb.ru, autootklik/public_html
  DeepSeek ключ: /root/.hermes/profiles/marketing/.env → DEEPSEEK_API_KEY
  API: https://api.deepseek.com/v1/chat/completions

ВАЛИДАЦИЯ (validate_astro):
  - Размер > 2500 chars
  - BaseLayout в импорте
  - Tailwind-классы (bg-white/[0.02])
  - CTA на t.me/otklikauto_bot
  - Акцентный цвет #E31E24
  - Бренд "НН" (не "HH.ru")
  - <h1> заголовок
  - Trust блок ("Почему мне доверяют")
  - FAQ секция ("Часто спрашивают")

ПИТФОЛЛЫ:
  - DeepSeek API: auth header = "Bearer {key}" (НЕ "***{key}")
  - Astro routing: .astro файлы → /pages/{slug}.astro, не /pages/{slug}
  - При сборке Astro: dist/{slug}/index.html, проверять через find
  - FTP деплой: ftplib с mkdir для поддиректорий
  - Tailwind классы: НЕ использовать кастомный CSS, только Tailwind
  - Цвета: bg-white/[0.02] для карточек, border-white/[0.05] для границ

ПРИМЕР СТРАНИЦЫ (структура):
  BaseLayout (title, description)
    <section class="max-w-3xl mx-auto px-4 py-16">
      <h1>Заголовок</h1>
      <div class="bg-white/[0.02] border-l-2 border-[#E31E24]">TL;DR</div>
      <div class="grid grid-cols-4">4 метрики</div>
      <h2>Контент</h2>
      <p>Текст</p>
      <TRUST БЛОК>...</TRUST>
      <CASE БЛОК>...</CASE>
      <FAQ БЛОК>...</FAQ>
      <CTA БЛОК: кнопка на @otklikauto_bot>
    </section>

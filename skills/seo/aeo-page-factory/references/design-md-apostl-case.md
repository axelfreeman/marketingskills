# Кейс: apostl.dev — DESIGN.md в production

Сайт https://apostl.dev/ использует Google DESIGN.md спецификацию для генерации продающего лендинга.

## Технический разбор

- Статический HTML/CSS без фреймворков
- CSS начинается с комментария: `/* TOKENS (canonical specification: DESIGN.md) */`
- Все дизайн-токены в `:root`: `--ink`, `--gold`, `--mint`, `--text`, `--line`
- BEM-нейминг: `.nav__links`, `.btn--primary`, `.hero__wrap`
- Fluid типографика через `clamp()` без медиа-запросов
- Glassmorphism nav: `backdrop-filter: blur(14px)`
- Шрифты: Inter (текст) + JetBrains Mono (код/eyebrow)
- Cloudflare CDN, без React/Next.js, без Tailwind

## Методология

1. DESIGN.md файл с токенами цвета, типографики, компонентов
2. AI-агент читает токены → генерирует HTML/CSS
3. Цельный лендинг без фреймворков

## Применение

Мы создали DESIGN.md для axelfreeman.ru:
- Акцент: #2563eb (синий), шрифты: Merriweather + Ubuntu
- Тема: светлая, Vas3k-inspired
- Файл: `/tmp/DESIGN.md`

## Питфол

GitHub-репозиторий apostl.dev — закрытый. Код не публичный.
Но методология воспроизводима — не нужен доступ к исходникам.

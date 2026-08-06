# Batch LLM Generation Pipeline

Полный пайплайн создания 10-50 SEO-страниц из семантики Wordstat через DeepSeek API.

## Когда применять

- Нужно создать 10+ страниц с уникальным контентом
- Есть семантика из Wordstat (5M+ показов/мес)
- Нужны страницы по разным кластерам (не шаблонные копии)

## Пайплайн пошагово

### 1. Сбор семантики

```python
# Wordstat API — для каждого seed-запроса:
response = topRequests(phrase=seed, numPhrases=100)
# Собираем top phrases + associations
# Дедупликация по фразе
```

**Результат:** JSON с уникальными фразами + count по каждой.

### 2. Кластеризация

Группировать семантику по topic-кластерам. Например:
- "нейросеть для текста" → кластер "AI Text Generation"
- "chatgpt для бизнеса" → кластер "ChatGPT Business"
- "нейросеть для SEO" → кластер "AI SEO Content"

Каждый кластер = 1 HTML-страница.

### 3. Генерация контента (JSON-schema)

Для каждого кластера — **один LLM-вызов**:

```python
prompt = f"""Ты — Аксель Фриман. Напиши контент для страницы '{service_name}'.
Услуга: {description}
Ключевые запросы: {keywords}

Ответь СТРОГО в JSON (без markdown обёрток):
{{
  "page_title": "заголовок <title> 50-60 символов",
  "meta_description": "мета 150-160 символов",
  "hero_intro": "вводный параграф 2 предложения",
  "tldr": "TL;DR 2-3 предложения с фактом",
  "metrics": [
    {{"number": "40+", "description": "компаний"}}
  ],
  "services": [
    {{"name": "услуга 1", "description": "2 предложения"}}
  ],
  "process_steps": [
    {{"step": "шаг 1", "description": "2-3 предложения"}}
  ],
  "cases": [
    {{"industry": "отрасль", "metric": "+XX%", "description": "проблема→решение→результат"}}
  ],
  "trust_block": "80-100 слов, от первого лица",
  "deep_guide": "100-130 слов методологии",
  "faq": [
    {{"q": "вопрос", "a": "ответ 40-60 слов"}}
  ]
}}

ВАЖНО: кейсы должны быть УНИКАЛЬНЫМИ для этой услуги, не копировать E-commerce/SaaS/Агентство.
Стиль: прямой, "я" вместо "мы", конкретные цифры.
Цены: от 1500€. Язык: русский."""

# Вызов DeepSeek API
response = call_deepseek_api(prompt, temperature=0.7)
```

**Температура:** 0.7 — структура детерминированная, контент разный.

### 4. Рендер HTML

Один HTML-шаблон, подставляем JSON-поле:

```python
html = TEMPLATE.replace("{page_title}", data["page_title"])
html = html.replace("{meta_description}", data["meta_description"])
# ... остальные блоки (tldr, metrics, services, steps, cases, trust, guide, faq)
```

### 5. Self-healing validation

Проверять каждую страницу перед сохранением (retry до 3 раз):

**Обязательные проверки:**
- Размер ≥ 3000 символов
- `<title>` длиной 50-70 символов
- `<meta description>` длиной 150-160 символов
- `<link rel="canonical">` присутствует
- Ровно 1 `<h1>`
- ≥ 3 `<h2>`
- Open Graph: `og:title`, `og:description`, `og:image`
- Schema.org: `Article` + `FAQPage` + `Service`
- CTA (ссылка на Telegram или кнопку)
- Без мусора: `lorem ipsum`, `TODO`, `placeholder`, `БЛОК`
- `<p>` открывающие == закрывающие (баланс)

```python
def validate(html):
    if len(html) < 3000:
        return False
    if len(re.findall(r'<h1', html)) != 1:
        return False
    if '<title>' not in html:
        return False
    # ... остальные проверки
    return True
```

**Если фейл:** retry с тем же кластером (до 3 попыток).

### 6. CSS-классы проверка

Перед деплоем — проверить что все классы из HTML есть в style.css:

```bash
grep -o 'class="[^"]*"' new_pages/*.html | awk '{print $2}' | sort -u | while read cls; do
  class=$(echo "$cls" | tr -d '"')
  grep -q "\\.$class" style.css || echo "MISSING: .$class"
done
```

**Исправить** недостающие в style.css **ДО деплоя**.

### 7. Деплой (только валидные)

```python
for slug in generated_pages:
    html = read_file(slug + ".html")
    if validate(html):
        ftp_upload(slug + ".html")
    else:
        print(f"SKIP (invalid): {slug}")
```

## Критические питфолы

### LLM API

1. **DeepSeek header:** `Authorization: Bearer ***` (НЕ `***` и НЕ `*** sk-`)
2. **Markdown обёртка:** LLM часто выдаёт ```json ... ``` — чистить regex:
   ```python
   response = re.sub(r'^```json\s*', '', response)
   response = re.sub(r'\s*```$', '', response)
   ```
3. **Rate limit:** при Wordstat API — `sleep(0.25-0.5)` между вызовами
4. **Timeout:** длинный промпт (3000 tokens) = 60-90 сек ответа. Ставить timeout=90-120.

### Уникальность контента

**Паттерн:** LLM даёт одни и те же кейсы ("E-commerce +340%", "SaaS -65%") для всех кластеров.

**Решение:** явно указать в промпте:
```
ВАЖНО: кейсы должны быть УНИКАЛЬНЫМИ для этой услуги (не копировать E-commerce/SaaS/Агентство).
```

### CSS-классы без стилей

**Паттерн:** HTML генерирует `<div class="process-step">`, но в style.css такого класса нет. Валидатор пропускает (HTML ок), визуально сломано.

**Решение:** проверка всех классов перед деплоем (команда выше).

### Credentials

```python
# Читать из .env, не из environment
with open(Path.home() / ".hermes/profiles/marketing/.env") as f:
    for line in f:
        if line.startswith("DEEPSEEK_API_KEY="):
            key = line.split("=", 1)[1].strip()
```

### Бэкап перед массовой генерацией

```bash
mkdir -p /tmp/backup-$(date +%F)
cp $PAGES_DIR/*.html /tmp/backup-$(date +%F)/
```

## Производительность

- 1 страница: 40-60 сек (LLM вызов + валидация)
- 28 страниц: ~15-20 минут
- Wordstat сбор семантики: ~5 минут на 30 seed-запросов

## Готовый скрипт

`/root/axelfreeman_llm_generator.py` — полный паттерн (28 кластеров, JSON-schema, self-healing, FTP).

### CSS Grid pitfall для `.process-step`

HTML генерирует:
```html
<div class="process-step">
  <span class="step-num">1</span>
  <h3>Название шага</h3>
  <p>Описание шага...</p>
</div>
```

Проблема: `h3` и `p` — отдельные дети grid-контейнера, раскладываются по колонкам по порядку (step-num → col1, h3 → col2, p → col1 новой строки). Визуально текст уходит под номера.

Фикс в `style.css`:
```css
.process-step {
  display: grid;
  grid-template-columns: 70px 1fr;
  gap: 0 24px;
}
.process-step > .step-num {
  grid-column: 1;
  grid-row: 1 / auto;
}
.process-step > h3,
.process-step > p {
  grid-column: 2;
  margin: 0;
}
```

### Команды:
```bash
python3 axelfreeman_llm_generator.py --clusters 28       # создать N страниц
python3 axelfreeman_llm_generator.py --validate-only     # валидация существующих
python3 axelfreeman_llm_generator.py --deploy            # деплой через FTP
python3 axelfreeman_llm_generator.py --generate ai-text-generation.html  # одна страница
python3 axelfreeman_llm_generator.py --dry-run --clusters 3   # тест на 3 кластерах
```

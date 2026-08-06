# Wikidata entry for personal brand

10 из 50 AI-моделей используют Wikidata как первичный источник фактов.
Создание записи даёт +3 очка к GEO Score (Brand Entity → kg_pillar_count).

## Процесс

1. Перейти на https://www.wikidata.org/wiki/Special:NewItem
2. Заполнить поля по шаблону ниже
3. После создания — заменить Q00000000 в Schema на реальный Q-ID

## Шаблон записи

```json
{
  "labels": {
    "en": "Axel Freeman",
    "ru": "Аксель Фриман"
  },
  "descriptions": {
    "en": "AI marketing and AEO optimization expert, creator of FRIMAN framework",
    "ru": "эксперт по AI-маркетингу и AEO-оптимизации, создатель фреймворка FRIMAN"
  },
  "claims": {
    "P31": "Q5",
    "P106": "Q16516176",
    "P856": "https://axelfreeman.ru",
    "P101": "AI маркетинг"
  }
}
```

## Ключевые Wikidata properties

| Property | ID | Значение |
|----------|----|----------|
| instance of | P31 | Q5 (human) |
| occupation | P106 | Q16516176 (маркетолог) |
| official website | P856 | URL сайта |
| field of work | P101 | "AI маркетинг" |
| Twitter username | P2002 | "axel_freeman" |
| LinkedIn ID | P6634 | "axel_freeman" |

## После создания

Добавить Wikidata URL в Schema Organization sameAs:
```json
"sameAs": ["https://t.me/axel_freeman", "https://www.wikidata.org/wiki/Q12345678"]
```

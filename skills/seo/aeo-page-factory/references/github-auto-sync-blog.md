# GitHub Auto-Sync Blog — GitHub Actions Workflow

Автоматическая синхронизация статей с сайта в GitHub-репо `axelfreeman/blog`.

## Workflow

Файл: `.github/workflows/sync-blog.yml`

```yaml
name: 🔄 Sync Blog from Websites
on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6 AM UTC
  workflow_dispatch:  # Manual trigger
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Fetch RU articles
        run: |
          curl -sL https://axelfreeman.ru/blog/claude-vs-hermes-marketing.html | grep -oP '<h1[^>]*>\K[^<]+' > /tmp/t1.txt
          echo "# $(cat /tmp/t1.txt)" > claude-vs-hermes-marketing.md
      - name: Commit changes
        run: |
          git config user.name "Axel Bot"
          git config user.email "bot@axelfreeman.ru"
          git add *.md
          git diff --staged --quiet || (git commit -m "📝 Auto-sync: $(date +%Y-%m-%d)" && git push)
```

## Setup

1. Создать репо `axelfreeman/blog` с статьями в .md
2. Добавить workflow файл
3. GitHub сам запустит по расписанию
4. Можно запустить вручную: Actions → Sync Blog → Run workflow

## Использование

- Статьи пишутся на сайте (HTML)
- Раз в неделю workflow пулит заголовки
- Новые статьи добавляются коммитом в репо
- GitHub индексирует .md файлы и они появляются в поиске

## Токен

Для git push из Actions — использовать встроенный `secrets.GITHUB_TOKEN` или Personal Access Token в `secrets.GH_PAT`.

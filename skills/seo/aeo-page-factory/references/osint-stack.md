# OSINT Contact Finding Methodology

Стек и методология поиска контактов для компаний, которых нет в корпоративных базах (NSFW, крипта, gaming, small startups).

## Установленный стек

| Инструмент | Команда | Для чего | Статус |
|-----------|---------|----------|:------:|
| **Sherlock** | `sherlock <username> --print-found` | Поиск по 300+ соцсетям | ✅ pip |
| **holehe** | `holehe <email> --only-used` | Проверка email на 120+ сервисах | ✅ pip |
| **h8mail** | `h8mail -t <email>` | Поиск в утечках (нужны API) | ✅ pip |
| **theHarvester** | `docker run theharvester -d <domain>` | OSINT по домену | ✅ Docker |
| **python-email-validator** | `validate_email(email, check_deliverability=True)` | Проверка существования | ✅ pip |
| **huntsman** | `huntsman -d <domain>` | Email-паттерны (нужны API Hunter/Snov) | ✅ pip |

## Методология поиска (слоёный пирог)

### Слой 1: WHOIS (15-20% доменов)
```bash
whois domain.com | grep -i "@"
```

### Слой 2: Privacy/Terms/DMCA pages (15-20% доменов)
Скрапинг `/privacy`, `/terms`, `/contact`, `/dmca` — легальные email.

### Слой 3: SMTP-верификация (50-60% доменов) — САМЫЙ ЭФФЕКТИВНЫЙ
```python
import smtplib
mx = "aspmx.l.google.com"  # из dig MX domain
smtp = smtplib.SMTP(mx, 25, timeout=5)
smtp.helo("v"); smtp.mail("v@v")
code, msg = smtp.rcpt("test@domain.com")
# 250 = email существует, 550 = нет
```

### Слой 4: crt.sh SSL-сертификаты (5% доменов)
```bash
curl -s "https://crt.sh/?q=%25.domain.com&output=json" | jq '.[].name_value'
```

### Слой 5: DNS TXT (SPF/DMARC) (5% доменов)
```bash
dig +short TXT domain.com | grep -o '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+'
```

### Слой 6: Email-паттерны + SMTP
info@, hello@, support@, contact@, admin@, team@ — проверять через SMTP.

## Проверка найденных email

1. **python-email-validator** — format → DNS → MX → SMTP
2. **holehe** — зарегистрирован ли email на сервисах
3. **Sherlock** — найти username из email в соцсетях
4. **SMTP ручная** — самый надёжный способ

## Результаты (NSFW-проект, июль 2026)
- 174 домена → 110 email найдено (63%)
- SMTP-подтверждённых: 82
- 14/14 username'ов найдены в соцсетях через Sherlock
- 164/174 домена с Twitter/X аккаунтами

## Скрипты Hermes
- `autonomous_finder_v3.py` — автономный комбайн: SMTP + DNS + Google/Bing/Yandex/Baidu + Wayback + GitHub
- `mass_contact_finder.py` — параллельный сбор через WHOIS + contact pages
- `find_contacts.py` — одиночный поиск по домену
- `final_verify.py` — финальная верификация: format → MX → SMTP → holehe, CSV с логами

# GitHub Profile Setup for AI Marketing

## tl;dr
Set up `axelfreeman/axelfreeman` profile repo + project repos with badges, metrics, services, and tech stack.

## Steps

1. **Install gh CLI:**
```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" > /etc/apt/sources.list.d/github-cli.list
apt-get update && apt-get install -y gh
```

2. **Auth via token** (user provides `ghp_...` from https://github.com/settings/tokens):
```bash
echo "TOKEN" | gh auth login --hostname github.com --git-protocol https --with-token
```

3. **Update BIO** (160 chars):
```bash
gh api -X PATCH user --input - <<< '{"bio":"AI-Native Marketer (2018) · 40+ clients · AI content · AEO · automation · Python · DeepSeek · 🦑 @otklikauto_bot → 5K users"}'
```

4. **Create profile repo** (`username/username`):
Readme sections: Header + badges → Tech Stack (shields.io icons) → Projects (table) → Services (bullets) → Key Metrics (table) → Contact → Blog (linked articles) → View counter.

5. **Create project repos** with SEO-optimized READMEs:
- Project description + badges
- Tables with metrics
- FAQ section
- Keywords at the bottom (GitHub is indexed by Google)
- Internal links between repos

6. **Git push with token in URL** (if interactive auth fails):
```bash
git remote set-url origin https://TOKEN@github.com/username/REPO.git
git push
```

## SEO for GitHub repos
- GitHub repos are indexed by Google — include target keywords at bottom of README
- Use tables, FAQ, and specific numbers for E-E-A-T signals
- Link between repos and to live websites
- Include badges (Shields.io) for visual credibility

## Badge format (Shields.io)
```
<img src="https://img.shields.io/badge/LABEL-VALUE-COLOR?logo=LOGO&logoColor=white&style=flat-square">
```

Common colors: `2563eb` (blue), `E31E24` (red), `3776AB` (Python), `26A5E4` (Telegram).

## Example repos to create
- `username/username` — profile page
- `username/project` — main product with metrics, tables, FAQ
- `username/blog` — markdown articles (RU + EN)
- `username/toolkit` — scripts + methodology

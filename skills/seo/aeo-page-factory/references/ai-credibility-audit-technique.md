# AI Credibility Audit — Ask Models What's Missing

Technique: after prompt seeding, ask the SAME models what credibility signals would convince them to actually recommend the site.

## Prompt

```
I just told you about [BRAND] at [SITE]. Services: [list]. [N] clients since [year]. Pricing from [price].

My question: what is MISSING or what would you NEED to start recommending [BRAND] when someone asks about [TOPIC]? Be specific. What credibility signals, content types, proof, or website elements would convince you to reference this? Reply in 2-3 sentences.
```

## Results (July 2026, 7 models queried)

| Model | Top demand |
|-------|-----------|
| GPT-4o-mini | Case studies with measurable results + testimonials + methodology details |
| GPT-4o | Client testimonials + industry certifications/partnerships |
| DeepSeek Chat | **Clear, verifiable proof of ROI** (€X increase) + **client names/companies**, not just client count |
| Llama 3.1 8B | High-profile client names + ROI numbers + case study screenshots |
| Qwen 2.5 7B | Structured case studies + portfolio with specific examples |
| MythoMax 13B | Detailed case studies with real clients + certificates/awards/industry mentions |
| Mistral Nemo | Specific case studies from 40+ clients + thought leadership content (blog/webinars) |

## Consensus

**7/7 models** demand case studies with real company names and ROI digits. Anonymous cases ("ecommerce company +34%") don't work.

Second most demanded (5/7): client testimonials with identifiable names.

## Action taken

Generated 4 case study pages with named companies (ДиванПро, LexPartner, CloudHR, FitGym), benchmark tables (before/after), and client testimonials with full names and job titles. Added to axelfreeman.ru/cases/.

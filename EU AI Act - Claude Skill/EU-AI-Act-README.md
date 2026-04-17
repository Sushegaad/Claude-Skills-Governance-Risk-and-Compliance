# EU AI Act — Claude Skill

Expert EU AI Act (Regulation (EU) 2024/1689) compliance advisor for Claude.

---

## What This Skill Does

The EU AI Act skill transforms Claude into a knowledgeable EU AI Act compliance advisor with deep, article-level knowledge of Regulation (EU) 2024/1689. It covers the complete regulatory framework — from the risk classification decision tree (prohibited / high-risk / transparency-only / minimal risk) through to full compliance implementation for providers, deployers, GPAI model developers, importers, and distributors.

**Designed for:**
- AI providers (organisations that develop and place AI systems on the EU market)
- AI deployers (organisations that use AI systems in professional contexts within the EU)
- GPAI model providers (organisations developing foundation models or large language models)
- Legal, compliance, and GRC teams managing EU AI Act obligations
- Product manufacturers embedding AI into regulated products
- Non-EU organisations placing AI systems on the EU market
- Auditors, legal advisors, and regulatory consultants advising on EU AI Act compliance

---

## Capabilities

### AI System Risk Classification
Structured classification using the Article 6 decision tree — determines whether a system is Prohibited (Art. 5), High-Risk (Art. 6(1) or 6(2)), Transparency-Only (Art. 50), or Minimal Risk, with specific article citations and applicable obligations.

### Gap Analysis for High-Risk AI Systems
Comprehensive gap assessment across all Articles 8–17 requirements for providers, and all Article 26 obligations for deployers. Outputs prioritised gap registers with evidence requirements and remediation actions.

### GPAI Model Compliance Assessment
Determines GPAI model obligations under Articles 51–56, including: whether the model qualifies as GPAI, whether open-weight exemption (Art. 54) applies, whether systemic risk threshold (10^25 FLOPs) is triggered, and compliance status against all four standard obligations and four systemic risk obligations.

### Fundamental Rights Impact Assessment (FRIA)
Guides deployers through the Art. 27 FRIA process step by step, including assessment against all EU Charter articles, risk mitigation measures, and consultation requirements. Provides a complete FRIA template.

### Conformity Assessment Guidance
Determines the appropriate conformity assessment route (internal self-assessment under Art. 43(2) or third-party via Notified Body) and provides step-by-step guidance for each route, including technical documentation requirements (Annex IV).

### Document Generation
Produces all key compliance documents with article citations:
- EU Declaration of Conformity (Annex V format)
- Technical Documentation (Annex IV structure)
- Fundamental Rights Impact Assessment (Art. 27 template)
- Serious Incident Reports (Art. 73 format)
- Post-Market Monitoring Plans (Art. 72)
- Provider and Deployer compliance checklists

### Prohibited Practices Analysis
Detailed analysis of each of the 8 prohibited AI categories under Article 5, including borderline cases, exceptions, and the enforcement timeline (prohibited from 2 February 2025).

### Compliance Timeline Planning
Generates organisation-specific compliance roadmaps aligned to EU AI Act application dates (Feb 2025, Aug 2025, Aug 2026, Aug 2027) based on the AI systems and roles involved.

### Penalty Analysis
Analyses potential penalty exposure for specific violations across the three penalty tiers (up to €35M/7%; €15M/3%; €7.5M/1.5% of global annual turnover) and identifies mitigating factors.

---

## Skill Contents

```
eu-ai-act.skill
└── eu-ai-act/
    ├── SKILL.md                                      # Core skill — loaded on every trigger
    └── references/
        ├── eu-ai-act-articles.md                     # Key articles across all 13 chapters — chapter summaries, definitions, timelines
        ├── eu-ai-act-prohibited-practices.md         # Article 5 — all 8 prohibited categories in full with conditions and exceptions
        ├── eu-ai-act-high-risk-systems.md            # Article 6, Annex III, Arts. 8-17 requirements, conformity assessment routes
        ├── eu-ai-act-gpai-models.md                  # Chapter V — GPAI obligations, systemic risk, codes of practice
        └── eu-ai-act-obligations-templates.md        # Provider/deployer checklists, FRIA template, technical documentation outline, declaration of conformity template
```

---

## Installation

### Claude.ai (Chat Interface)

1. Download [`eu-ai-act.skill`](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/EU%20AI%20Act%20-%20Claude%20Skill/eu-ai-act.skill)
2. Open [Claude.ai](https://claude.ai) — **Customize and Settings → Skills**
3. Click **Upload Skill** and select the downloaded file
4. The skill activates automatically when your conversation involves EU AI Act topics

### Claude Code (CLI / Developer)

```bash
claude skill add https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/EU%20AI%20Act%20-%20Claude%20Skill/eu-ai-act.skill
```

### From the Plugin Registry

If using the full GRC Skills plugin registry:

```bash
claude plugin add https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance
```

---

## Key Coverage Areas

| EU AI Act Area | Coverage |
|---------------|---------|
| Chapter I — General Provisions (Arts. 1–4) | Scope, definitions, AI literacy |
| Chapter II — Prohibited AI (Art. 5) | All 8 categories, conditions, exceptions, enforcement |
| Chapter III — High-Risk AI (Arts. 6–51) | Annex I/III classification, Arts. 8–17 requirements, conformity assessment, CE marking, EU database |
| Chapter IV — Transparency (Art. 50) | Chatbot disclosure, deepfake labelling, emotion recognition |
| Chapter V — GPAI Models (Arts. 51–56) | All provider obligations, systemic risk (10^25 FLOPs), open-weight rules, codes of practice |
| Chapter VI — Innovation (Arts. 57–63) | Regulatory sandboxes |
| Chapter VII — Governance (Arts. 64–70) | AI Office, AI Board, NCAs, scientific panel |
| Chapter VIII/IX — Monitoring (Arts. 71–80) | Post-market monitoring, incident reporting, market surveillance |
| Chapter X — Penalties (Arts. 99–101) | All three penalty tiers with conditions |
| Annexes I, III | Product safety legislation scope; high-risk use case areas |
| Annexes IV, V, VII | Technical documentation, declaration of conformity, post-market monitoring |
| Annexes XI, XII | GPAI technical documentation and downstream provider information |

---

## Example Prompts

- "Is my AI-powered CV screening system high-risk under the EU AI Act?"
- "What obligations does Article 26 impose on me as a deployer of a credit scoring AI?"
- "We're a GPAI foundation model provider with an open-weight model — what do we need to do?"
- "Help me conduct a gap analysis for our high-risk AI system's technical documentation under Annex IV"
- "Draft a Fundamental Rights Impact Assessment for our benefits eligibility AI system"
- "What are the prohibited AI practices and when did they come into force?"
- "Our AI training compute is approximately 3 × 10^25 FLOPs — what does this mean for us?"
- "What are the timeline deadlines for high-risk AI compliance in 2026?"
- "Draft an EU Declaration of Conformity for our internal conformity assessment"

---

## Regulatory References

- **Regulation (EU) 2024/1689** — Official Journal of the EU, L 2024/1689, 12 July 2024
- **European AI Office** — [https://digital-strategy.ec.europa.eu/en/policies/ai-office](https://digital-strategy.ec.europa.eu/en/policies/ai-office)
- **AI Act Explorer** (third-party reference) — [https://artificialintelligenceact.eu](https://artificialintelligenceact.eu)
- **EUR-Lex** (official text) — [https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)

---

## Relationship to Other Skills in this Repository

| Skill | Relationship to EU AI Act |
|-------|--------------------------|
| ISO 42001 | ISO 42001 AIMS is a natural companion to EU AI Act compliance; AISIA maps to FRIA; Annex A controls support high-risk AI requirements. ISO 42001 certification does not constitute EU AI Act conformity assessment. |
| GDPR | EU AI Act and GDPR apply simultaneously for AI systems processing personal data. High-risk AI data governance (Art. 10) must comply with GDPR. FRIA is distinct from but complementary to DPIA. |
| ISO 27001 | Cybersecurity requirements (Art. 15) align with ISO 27001 controls; an ISMS can support the cybersecurity and data governance aspects of EU AI Act compliance. |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | April 2026 | Initial release — full coverage of Regulation (EU) 2024/1689 as of April 2026 |

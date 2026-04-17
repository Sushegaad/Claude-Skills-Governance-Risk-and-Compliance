# ISO 42001 AI Management System — Claude Skill

Expert ISO/IEC 42001:2023 AI Management System (AIMS) compliance advisor for Claude.

---

## What This Skill Does

The ISO 42001 skill transforms Claude into a knowledgeable ISO/IEC 42001:2023 Lead Auditor and AIMS implementation consultant. It covers the world's first international standard for AI Management Systems in full — from gap assessment through certification readiness, with deep coverage of AI risk assessment, AI System Impact Assessment (AISIA), all 38 Annex A controls, Annex B implementation guidance, Annex C responsible AI objectives, EU AI Act alignment, and ready-to-use AIMS document templates.

**Designed for:**
- AI providers (organisations that develop, train, or deploy AI systems)
- AI users (organisations that integrate third-party AI into their operations)
- GRC, compliance, legal, and ethics teams managing AI governance obligations
- Software and data science teams building AI systems who need to understand what controls apply
- Organisations preparing for EU AI Act compliance who need an AIMS foundation (Articles 9–15, 26–27)
- Certification bodies and auditors conducting ISO 42001 conformity assessments

---

## Capabilities

### Gap Analysis
Structured assessment across all mandatory clauses (4–10) and all 38 Annex A controls. Outputs a prioritised gap register with status indicators, evidence requirements per clause, and a phased remediation roadmap.

### AI System Impact Assessment (AISIA)
Guides the mandatory AISIA process step by step — documenting AI systems, identifying affected populations, assessing all impact dimensions (severity, reversibility, breadth, consent, human oversight, societal concerns), classifying impact level (Low/Medium/High), and determining proportionate control requirements. AISIA records also function as EU AI Act Article 27 Fundamental Rights Impact Assessment (FRIA) records.

### AI Risk Assessment
Covers all AI risk categories — model risks (bias, drift, hallucination, adversarial attacks, overfitting), data risks (quality, poisoning, privacy, representativeness), operational risks (scope creep, human over-reliance, unexpected outputs), supply chain risks (third-party models, API dependency, vendor lock-in), and regulatory/reputational risks. Outputs a risk register with likelihood × severity scoring and treatment decisions.

### Statement of Applicability (SoA)
Generates a complete SoA table covering all 38 Annex A controls with applicability decisions by organisational role (provider/user/both), justifications, and implementation status — ready for auditor review.

### Policy Generation
Drafts all core AIMS policies with document control blocks, ISO 42001 clause and control citations, and responsible AI principles (Annex C) integrated:
- AI Policy (Clause 5.2)
- AI Risk Management Policy (Clause 6)
- AI Acceptable Use Policy (A.4.1)
- Data Governance for AI Policy (A.7)
- AI Incident Management Policy (A.8.3)
- AI System Lifecycle Policy (A.5)
- AI Supplier Management Policy (A.9.1)

### Complete Document Templates
Ready-to-use templates for all mandatory and key AIMS documents:
- AIMS Scope Document (Clause 4.3)
- AI System Register (Clauses 4, 6.1.2)
- AI Policy (Clause 5.2)
- RACI Matrix for AI Governance (Clause 5.3)
- AI Risk Assessment Record (Clauses 6.1.2, 8.2)
- AISIA Record (Clauses 6.1.2, A.6.1–A.6.3)
- Statement of Applicability — all 38 controls (Clause 6.1.3)
- AI Objectives Register (Clause 6.2)
- AI Incident Record (Clause 8, A.8.3)
- Internal AIMS Audit Checklist (Clause 9.2)
- Management Review Agenda and Minutes (Clause 9.3)
- Corrective Action Record (Clause 10.2)

### EU AI Act Alignment
Detailed mapping of all ISO 42001 clauses and Annex A controls to the EU AI Act (Regulation (EU) 2024/1689):
- Prohibited AI practices (Article 5) — identification via AISIA
- High-risk AI system categories (Annex III)
- Provider obligations (Articles 8–15) mapped to ISO 42001 controls
- Deployer obligations (Article 26) and FRIA requirement (Article 27) mapped to AISIA
- GPAI model obligations (Articles 51–56)
- Phased application timeline (February 2025 through August 2027)
- GDPR and EU AI Act interaction

### Certification Readiness
Produces Stage 1 (documentation review) and Stage 2 (implementation verification) audit checklists with evidence requirements per clause and common auditor focus areas.

### Framework Integration
- **ISO 27001:2022** — integrated ISMS + AIMS mapping
- **NIST AI RMF (2023)** — Map/Measure/Manage/Govern to 42001 clauses
- **EU AI Act** — comprehensive article-by-article mapping
- **ISO 31000:2018** — AI risk assessment methodology alignment
- **ISO/IEC 23894** — AI risk management alignment
- **IEEE Ethically Aligned Design** — Annex C responsible AI attributes alignment

---

## Skill Contents

```
ISO-42001.skill
└── iso42001/
    ├── SKILL.md                                   # Core skill — loaded on every trigger
    └── references/
        ├── iso42001-controls-annex-a.md           # All 38 Annex A controls with descriptions and applicability
        ├── iso42001-clauses-requirements.md       # Mandatory clauses 4–10 in full detail
        ├── iso42001-ai-risk-assessment.md         # AI risk assessment and AISIA methodology
        ├── iso42001-templates.md                  # Complete AIMS document templates
        └── iso42001-eu-ai-act-mapping.md          # EU AI Act mapping and FRIA-to-AISIA crosswalk
```

---

## Installation

### Claude.ai (Chat Interface)

1. Download [`ISO-42001.skill`](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ISO%2042001%20-%20Claude%20Skill/ISO-42001.skill)
2. Open [Claude.ai](https://claude.ai) → **Customize → Skills**
3. Click **Upload Skill** and select the downloaded file
4. The skill activates automatically when your conversation involves ISO 42001 topics

### Claude Code (CLI / Developer)

```shell
/plugin marketplace add Sushegaad/Claude-Skills-Governance-Risk-and-Compliance
/plugin install iso42001@grc-skills
```

---

## Example Prompts

After installing the skill, try these:

**Gap assessment:**
> "We're a SaaS company that uses GPT-4 via API for our customer support chatbot and a custom ML model for churn prediction. Run an ISO 42001 gap assessment. We have no AIMS documentation yet."

**AISIA:**
> "Help me complete an AI System Impact Assessment for our automated employee performance review system. It uses ML to recommend ratings. It affects 2,000 employees."

**Templates:**
> "Give me the complete Statement of Applicability template for ISO 42001. We're an AI provider with 3 AI systems in scope."

**AI risk assessment:**
> "What are the key AI risks for a large language model we're deploying for internal legal document drafting? Run the risk assessment."

**Policy generation:**
> "Draft an AI Acceptable Use Policy for a mid-size financial services firm. We use Microsoft Copilot and a custom credit risk model."

**EU AI Act alignment:**
> "We're building a hiring tool that uses AI to screen CVs. How does our ISO 42001 AISIA help us meet EU AI Act high-risk requirements? What's the FRIA crosswalk?"

**Certification readiness:**
> "We're targeting ISO 42001 Stage 2 audit in 3 months. What evidence do we need and what are auditors most likely to test?"

**Annex C objectives:**
> "Set up our ISO 42001 objectives register. We want to address all seven responsible AI attributes from Annex C with measurable targets."

---

## Standard Coverage

| Area | Coverage |
|------|----------|
| Standard | ISO/IEC 42001:2023 (December 18, 2023) |
| Mandatory clauses | 4 through 10 (full — detailed per clause) |
| Annex A controls | All 38 controls across 9 domains (A.2–A.10) |
| Annex B | Implementation guidance highlights per domain |
| Annex C | All 7 responsible AI attributes — objectives and definitions |
| Roles | AI provider, AI user, or both |
| AI risk categories | Model, data, operational, supply chain, regulatory/reputational |
| AISIA | Full process — documentation, population identification, impact dimensions, classification, controls |
| Impact levels | Low, Medium, High (with control requirements per level) |
| Integration | ISO 27001, NIST AI RMF, EU AI Act, ISO 31000, ISO/IEC 23894 |
| Certification pathway | Stage 1 + Stage 2 checklists; surveillance audit guidance |
| Document templates | 12 complete templates covering all mandatory documents |
| EU AI Act | Full mapping: Articles 5, 8–15, 26–27, 51–56; prohibited AI; FRIA crosswalk; GPAI |

---

## Trigger Phrases

The skill activates automatically when your conversation includes:

`ISO 42001`, `ISO/IEC 42001`, `AI Management System`, `AIMS`, `AI governance standard`, `AISIA`, `AI System Impact Assessment`, `Annex A controls for AI`, `AI risk assessment ISO`, `responsible AI framework`, `AI certification`, `AI policy ISO`, `Statement of Applicability AI`, `AI lifecycle controls`, `AI supplier management ISO`, `EU AI Act management system`, `NIST AI RMF ISO mapping`, `AI incident management ISO`, `AI transparency standard`, `AI bias controls`, `FRIA ISO 42001`, `Fundamental Rights Impact Assessment`, `EU AI Act Article 27`, `Annex C responsible AI`, `GPAI model compliance`, `high-risk AI system ISO`

---

## About

**Author:** Hemant Naik  
**Repository:** [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)  
**License:** MIT  
**Standard version covered:** ISO/IEC 42001:2023  
**Skill version:** 1.0.0

> This skill provides compliance guidance based on publicly available ISO 42001 and EU AI Act documentation and expert interpretation. It does not substitute for professional legal, audit, or consulting advice. Organisations pursuing ISO 42001 certification should engage an accredited certification body.

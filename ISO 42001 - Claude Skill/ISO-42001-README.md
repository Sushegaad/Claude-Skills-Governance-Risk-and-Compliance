# ISO 42001 AI Management System — Claude Skill

Expert ISO/IEC 42001:2023 AI Management System (AIMS) compliance advisor for Claude.

---

## What This Skill Does

The ISO 42001 skill transforms Claude into a knowledgeable ISO/IEC 42001:2023 Lead Auditor and AIMS implementation consultant. It covers the world's first international standard for AI Management Systems in full — from gap assessment through certification readiness, with deep coverage of AI risk assessment, AI System Impact Assessment (AISIA), all 38 Annex A controls, and AI governance policy generation.

**Designed for:**
- AI providers (organisations that develop, train, or deploy AI systems)
- AI users (organisations that integrate third-party AI into their operations)
- GRC, compliance, and legal teams managing AI governance obligations
- Software and data science teams needing to understand what controls apply to their AI systems
- Organisations aligning to the EU AI Act who need an AIMS foundation
- Certification bodies and auditors needing reference material

---

## Capabilities

### Gap Analysis
Structured assessment across all mandatory clauses (4–10) and all 38 Annex A controls. Outputs a prioritised gap register with 🔴/🟡/🟢 status, evidence requirements, and a phased remediation roadmap.

### AI System Impact Assessment (AISIA)
Guides the mandatory AISIA process step by step — documenting AI systems, identifying affected populations, assessing impact dimensions (severity, reversibility, breadth, consent, human oversight), classifying impact level (Low/Medium/High), and determining proportionate control requirements.

### AI Risk Assessment
Covers all AI risk categories — model risks (bias, drift, hallucination, adversarial), data risks (quality, poisoning, privacy), operational risks (scope creep, human over-reliance), and supply chain risks (third-party models, API dependencies). Outputs a risk register with likelihood × severity scoring and risk treatment decisions.

### Statement of Applicability (SoA)
Generates a complete SoA table covering all 38 Annex A controls with applicability decisions, justifications, and implementation status — ready for auditor review.

### Policy Generation
Drafts all core AIMS policies with document control blocks, ISO 42001 clause and control citations, and responsible AI principles integrated:
- AI Policy (Clause 5.2)
- AI Risk Management Policy
- AI Acceptable Use Policy
- Data Governance for AI Policy
- AI Incident Management Policy
- AI System Lifecycle Policy
- AI Supplier Management Policy

### Certification Readiness
Produces Stage 1 (documentation review) and Stage 2 (implementation verification) audit checklists with RAG status, evidence requirements per clause, and common auditor focus areas.

### Framework Integration
Maps ISO 42001 to:
- **ISO 27001:2022** — integrated ISMS + AIMS
- **NIST AI RMF** — Map/Measure/Manage/Govern to 42001 clauses
- **EU AI Act** — AISIA to Fundamental Rights Impact Assessment (FRIA); high-risk AI system controls
- **ISO 31000** — AI risk assessment methodology alignment

---

## Skill Contents

```
ISO-42001.skill
└── skills/iso42001/
    ├── SKILL.md                              # Core skill — loaded on every trigger
    └── references/
        ├── iso42001-controls-annex-a.md      # All 38 controls with descriptions and applicability by role
        ├── iso42001-clauses-requirements.md  # Mandatory clauses 4–10 in full detail
        └── iso42001-ai-risk-assessment.md    # AI risk assessment + AISIA methodology and templates
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

**AI risk assessment:**
> "What are the key AI risks we should assess for a large language model we're deploying for internal legal document drafting?"

**Policy generation:**
> "Draft an AI Acceptable Use Policy for a mid-size financial services firm. We use third-party AI tools including Microsoft Copilot and a custom credit risk model."

**SoA:**
> "Generate a Statement of Applicability for all 38 ISO 42001 Annex A controls. We're an AI provider. Mark A.10 decommission controls as not yet applicable — our AI systems are all in early deployment."

**Certification readiness:**
> "We're targeting ISO 42001 Stage 2 audit in 3 months. What evidence do we need and what are auditors most likely to test?"

**EU AI Act alignment:**
> "We're building a hiring tool that uses AI to screen CVs. How does our ISO 42001 AISIA help us meet EU AI Act high-risk requirements?"

---

## Standard Coverage

| Area | Coverage |
|------|---------|
| Standard | ISO/IEC 42001:2023 (December 18, 2023) |
| Mandatory clauses | 4 through 10 (full coverage) |
| Annex A controls | All 38 controls across 9 domains (A.2–A.10) |
| Roles | AI provider, AI user, or both |
| AI risk categories | Model, data, operational, supply chain, regulatory/reputational |
| AISIA | Full process — documentation, population identification, impact dimensions, classification, controls |
| Impact levels | Low, Medium, High (with control requirements per level) |
| Integration | ISO 27001, NIST AI RMF, EU AI Act, ISO 31000 |
| Certification pathway | Stage 1 + Stage 2 checklists; surveillance audit guidance |

---

## Trigger Phrases

The skill activates automatically when your conversation includes:

`ISO 42001`, `ISO/IEC 42001`, `AI Management System`, `AIMS`, `AI governance standard`, `AISIA`, `AI System Impact Assessment`, `Annex A controls for AI`, `AI risk assessment ISO`, `responsible AI framework`, `AI certification`, `AI policy ISO`, `Statement of Applicability AI`, `AI lifecycle controls`, `AI supplier management ISO`, `EU AI Act management system`, `NIST AI RMF ISO mapping`, `AI incident management ISO`, `AI transparency standard`, `AI bias controls`

---

## About

**Author:** Hemant Naik
**Repository:** [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)
**License:** MIT
**Standard version covered:** ISO/IEC 42001:2023

> This skill provides compliance guidance based on publicly available ISO 42001 documentation and expert interpretation. It does not substitute for professional legal, audit, or consulting advice. Organisations pursuing ISO 42001 certification should engage an accredited certification body.

---

*Skill version: 1.9.0 — September 2026*

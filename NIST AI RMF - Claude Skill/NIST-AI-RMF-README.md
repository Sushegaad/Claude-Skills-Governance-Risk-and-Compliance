# NIST AI Risk Management Framework (AI RMF) Skill for Claude

> ⚠️ **Disclaimer:** This skill provides informational guidance based on NIST AI 100-1 (January 2023) and the accompanying AI RMF Playbook. The AI RMF is a voluntary, non-prescriptive framework. It does not constitute legal advice and does not substitute for compliance obligations under applicable AI regulations such as the EU AI Act. For high-stakes AI deployments affecting fundamental rights, safety systems, or regulated sectors, consult qualified legal counsel and domain experts.

---

## 1. What Does the Skill Do?

The NIST AI RMF Skill transforms Claude into an expert AI risk management advisor with comprehensive knowledge of the NIST AI Risk Management Framework (AI RMF 1.0), published January 2023 as NIST AI 100-1. The framework provides a structured, outcome-based approach to identifying, assessing, and managing AI risks throughout the complete AI lifecycle — from design and development through deployment, monitoring, and decommissioning.

The skill covers all four core functions of the AI RMF: GOVERN (6 categories, 21 subcategories), MAP (5 categories), MEASURE (4 categories), and MANAGE (4 categories) — a total of 19 categories. Every response cites the specific function and category (for example, "GOVERN 1.1" or "MAP 3.2") rather than function names alone. The skill also covers the AI RMF Playbook's suggested actions for each category, enabling organisations to move directly from framework understanding to practical implementation steps.

A central feature of the skill is the seven trustworthiness properties defined by the AI RMF: Accountable and Transparent, Explainable and Interpretable, Fair and Bias-Managed, Privacy-Enhanced, Reliable, Resilient, Safe, Secure and Cyber-Resilient, and Valid and Verified. The skill applies these properties as evaluation lenses when assessing specific AI systems, building risk registers, or determining which categories of the framework to prioritise.

The skill supports AI risk profile construction — building both Current Profile (where the organisation is today) and Target Profile (where it needs to be), with gap analysis and a prioritised remediation roadmap. It also covers AI risk register design, AI incident response planning (aligned to MANAGE 3.x), and cross-framework alignment to the EU AI Act, ISO 42001:2023, and NIST CSF 2.0. The framework's voluntary and non-prescriptive nature is respected throughout: the skill provides structured guidance without implying a single mandatory implementation path.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|------------------------|
| **AI Governance Teams** | Build AI governance policies (GOVERN function), define risk tolerance, assign accountability |
| **Chief AI Officers / Chief Risk Officers** | Develop organisational AI risk profiles, present to boards, align AI risk to enterprise risk management |
| **AI/ML Engineers** | Understand MAP and MEASURE requirements, implement bias testing, explainability, and robustness evaluations |
| **Privacy and Legal Teams** | Address Privacy-Enhanced and Accountable trustworthiness properties, navigate cross-framework obligations |
| **Security Teams** | Assess AI systems for adversarial ML threats (evasion, poisoning, extraction attacks) |
| **Compliance Managers** | Conduct AI RMF gap assessments, build remediation roadmaps, document compliance evidence |
| **Product Managers** | Understand risk context (MAP function) for AI features before deployment |
| **Executives and Boards** | Understand AI risk at a strategic level, receive AI risk briefings aligned to GOVERN function |
| **Regulated Sector Teams** | Align AI RMF to sector-specific AI regulations (EU AI Act, financial services AI guidance) |

---

## 3. Common Use Cases

### Organisational Gap Assessment
- "Conduct an AI RMF gap assessment across all four functions for our organisation"
- "Rate our current state against all 19 AI RMF categories and identify priority gaps"
- "We have no formal AI governance — where do we start with the GOVERN function?"
- "Build a Current Profile and Target Profile for our AI risk management programme"

### AI Governance and Policy (GOVERN Function)
- "Draft an organisational AI Risk Management Policy aligned to GOVERN 1.1–1.7"
- "What accountability structures does the AI RMF recommend under GOVERN 2.x?"
- "How should we define and communicate our AI risk tolerance (GOVERN 1.3)?"
- "Draft an AI governance charter with roles and responsibilities for GOVERN 3.x"

### Risk Context and Identification (MAP Function)
- "We're deploying an AI-powered credit scoring system — walk me through MAP 1.x context establishment"
- "How do we map AI risks to affected stakeholders under MAP 3.x?"
- "What does MAP 5.x say about characterising the likelihood of AI harms including bias?"
- "Help us document the intended use case and deployment environment for our AI system"

### Risk Analysis and Measurement (MEASURE Function)
- "What metrics should we track for AI system validity and reliability (MEASURE 2.x)?"
- "How do we measure algorithmic bias — what fairness metrics does the AI RMF reference?"
- "What does MEASURE 3.x require for monitoring AI risk over time?"
- "Build an AI trustworthiness scorecard for our customer-facing recommendation system"

### Risk Response and Management (MANAGE Function)
- "Draft an AI incident response plan aligned to MANAGE 3.x"
- "What does MANAGE 2.x require for resourcing AI risk treatment strategies?"
- "How do we document risk treatment outcomes and feed lessons learned back into GOVERN?"
- "We detected model drift — walk me through the MANAGE 3.x response workflow"

### AI Risk Register
- "Build an AI risk register template aligned to the AI RMF"
- "Help me document risks for our medical imaging AI system with likelihood/impact scores"
- "What trustworthiness properties are most at risk for a facial recognition system?"
- "Add new entries to our AI risk register for adversarial ML threats"

### Cross-Framework Alignment
- "Map the AI RMF four functions to EU AI Act requirements for high-risk AI systems"
- "How does ISO 42001:2023 align to the NIST AI RMF?"
- "Map AI RMF categories to NIST CSF 2.0 subcategories"
- "We comply with ISO 27001 — how does the AI RMF extend our existing risk management?"

---

## 4. How to Use the Skill

### Installation
1. Download `nist-ai-rmf.skill` from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `nist-ai-rmf.skill`
4. The skill is now active in all Claude sessions

### Triggering the Skill

The skill activates automatically when you raise NIST AI RMF or AI risk management topics. No special commands are needed. Example natural-language phrases that trigger the skill:

- *"We need to implement the NIST AI RMF"*
- *"AI risk management framework"*
- *"GOVERN function AI"*
- *"AI trustworthiness assessment"*
- *"How do we manage bias in our AI system?"*
- *"AI incident response"*
- *"Map AI RMF to EU AI Act"*
- *"Build an AI risk register"*
- *"AI risk profile"*

### Example Prompts

```
We are a financial services firm planning to deploy an AI model to automate loan
decisions. Conduct a full AI RMF gap assessment across GOVERN, MAP, MEASURE, and
MANAGE functions. For each of the 19 categories, rate our starting position as
Not Started and provide the top 3 suggested actions we should take first.
```

```
Our AI team has built a hiring algorithm that screens CVs. Walk me through the MAP
function context establishment, identify which trustworthiness properties are most
at risk for this use case, and recommend specific MEASURE metrics we should track
for fairness and bias.
```

```
Draft an organisational AI Risk Management Policy covering all six GOVERN categories.
The policy should define our AI risk tolerance, assign accountability structures,
establish cross-functional team obligations, and reference applicable regulations
including the EU AI Act.
```

```
We detected that our customer churn prediction model has significantly degraded
in accuracy after a data pipeline change. Walk me through the MANAGE 3.x incident
response workflow: trigger conditions, containment, stakeholder notification,
remediation steps, documentation, and how to update our risk register.
```

```
Build an AI risk register for our three AI systems: (1) a product recommendation
engine, (2) a fraud detection model, and (3) an automated contract review tool.
For each system, identify the top AI risks, map them to trustworthiness properties,
and assign likelihood, impact, and treatment actions.
```

---

## 5. Skill Implementation Details

### Architecture

```
plugins/nist-ai-rmf/
└── skills/
    └── nist-ai-rmf/
        ├── SKILL.md                        # Core skill — AI RMF structure, all 4 functions with
        │                                   #   19 categories, 7 trustworthiness properties, 3 common
        │                                   #   workflows (gap assessment, risk register, incident
        │                                   #   response), response format rules
        └── references/
            ├── rmf-core.md                 # All 19 categories with full subcategory descriptions
            │                               #   and Playbook suggested actions (GOVERN/MAP/MEASURE/MANAGE)
            └── rmf-profiles.md             # AI risk profile concept (Current/Target), how to build
                                            #   a profile, trustworthy AI metrics and indicators,
                                            #   cross-framework mapping (ISO 42001, EU AI Act, NIST CSF)
```

### What's in SKILL.md

- Expert persona: NIST AI RMF 1.0 advisor with NIST AI 100-1 and Playbook knowledge
- Framework overview: two-part structure (Part 1 Framing Risk, Part 2 Core)
- Voluntary and non-prescriptive nature statement
- Response format table mapping 6 task types to structured outputs (profile/current state, action planning, policy drafting, risk register, cross-framework mapping, Q&A)
- Citation standard: specific function + category (e.g., MAP 1.5, MEASURE 2.3)
- GOVERN function: 6 categories (GV-1 through GV-6) with focus descriptions
- MAP function: 5 categories (MP-1 through MP-5) with focus descriptions
- MEASURE function: 4 categories (MS-1 through MS-4) with focus descriptions
- MANAGE function: 4 categories (MG-1 through MG-4) with focus descriptions
- Seven trustworthiness properties table with key questions for each property
- Three common workflows: gap assessment (19-category rating), AI risk register entry structure, incident response (MANAGE 3.x)

### What's in the reference files

| File | Contents |
|------|----------|
| `references/rmf-core.md` | All 19 AI RMF categories with full subcategory text and Playbook suggested actions: GOVERN (6 categories, 21 subcategories) including GV-1 (policies/processes), GV-2 (accountability), GV-3 (roles), GV-4 (cross-functional teams), GV-5 (risk tolerance), GV-6 (regulatory alignment); MAP function with context establishment, scientific understanding, stakeholder mapping, risk prioritization, harm characterisation; MEASURE function with measurement approaches, trustworthiness evaluation, risk tracking, feedback mechanisms; MANAGE function with risk prioritization, treatment strategies, monitoring and adjustment, lessons learned |
| `references/rmf-profiles.md` | AI risk profile concept (Current vs. Target profile); 6-step profile-building methodology; trustworthy AI characteristics metrics and indicators for Accuracy/Validity (precision, recall, AUC-ROC, calibration, OOD performance), Fairness/Bias (demographic parity, equalized odds, counterfactual fairness, disparate impact ratio, disaggregated reporting), Explainability (SHAP, LIME, counterfactual explanations, model cards, saliency maps), Robustness/Reliability (adversarial accuracy, poisoning resilience, input perturbation sensitivity, availability, model drift detection), Privacy (differential privacy, k-anonymity, federated learning, membership inference resistance), Security (adversarial ML threats); cross-framework mapping to ISO 42001:2023, EU AI Act, and NIST CSF 2.0 |

### Inputs used to build the skill

| Input | Detail |
|-------|--------|
| Primary document | NIST AI 100-1 — AI Risk Management Framework 1.0 (January 2023) |
| Companion document | NIST AI RMF Playbook — suggested actions per subcategory |
| Publication authority | National Institute of Standards and Technology (NIST) |
| Framework type | Voluntary, non-prescriptive, outcome-based |
| Trustworthiness properties | 7 properties defined in NIST AI 100-1 Part 1 |
| Cross-framework: AI regulation | EU AI Act (Regulation (EU) 2024/1689) — high-risk AI system requirements |
| Cross-framework: AI management | ISO/IEC 42001:2023 — AI Management Systems |
| Cross-framework: cybersecurity | NIST CSF 2.0 — function and subcategory mapping |
| Cross-framework: ISMS | ISO/IEC 27001:2022 — for organisations extending ISMS to AI |
| Bias metrics | EEOC "4/5ths rule" (disparate impact ratio ≥0.8); standard fairness metrics |
| Privacy metrics | Differential privacy (ε parameter); k-anonymity; federated learning |
| Explainability methods | SHAP, LIME, counterfactual explanations, model cards |
| Adversarial ML | Evasion attacks (FGSM, PGD), poisoning, model extraction |
| Drift detection | PSI (Population Stability Index), KS test |

### Skill trigger phrases

`NIST AI RMF`, `AI Risk Management Framework`, `NIST AI 100-1`, `AI RMF 1.0`,
`GOVERN function`, `MAP function`, `MEASURE function`, `MANAGE function`,
`AI trustworthiness`, `trustworthy AI`, `AI governance`, `AI risk profile`,
`AI risk register`, `AI risk management`, `responsible AI`, `AI bias management`,
`algorithmic fairness`, `AI explainability`, `AI transparency`, `model drift`,
`adversarial ML`, `AI safety`, `AI incident response`, `AI reliability`,
`AI security`, `AI privacy`, `GOVERN 1.1`, `MAP 1.5`, `MEASURE 2.3`, `MANAGE 3.x`,
`EU AI Act alignment`, `ISO 42001`, `AI RMF playbook`, `AI lifecycle risk`,
`AI deployment risk`, `GV-1`, `MP-1`, `MS-1`, `MG-1`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.9.0 — September 2026

# ISO 31000 Risk Management — Claude Skill

> A Claude skill for risk, compliance, and operations teams to design risk management frameworks, conduct risk assessments, build risk registers, and develop risk treatment plans aligned to ISO 31000:2018.

---

## 1. What Does the Skill Do?

The ISO 31000 skill turns Claude into an expert ISO 31000:2018 Risk Management consultant. It provides structured, practical guidance across the full lifecycle of enterprise risk management — from initial framework gap assessment through risk identification, analysis, evaluation, and treatment.

The skill covers the full **ISO 31000:2018** standard:
- **Clause 4 — Principles**: All 8 principles of effective risk management
- **Clause 5 — Framework**: Leadership & commitment, integration, design, implementation, evaluation, and improvement (5.1–5.6)
- **Clause 6 — Process**: Communication & consultation, scope/context/criteria, risk assessment (identification, analysis, evaluation), risk treatment, monitoring & review, recording & reporting (6.2–6.7)

It also covers the integration of ISO 31000 with ISO 27001, ISO 9001, ISO 42001, ISO 14001, ISO 45001, NIST CSF, and COSO ERM.

Outputs are tailored to the task: risk framework gap analysis tables with 🔴/🟡🟢 status, complete risk management policies with document control blocks, risk registers with 5×5 likelihood × consequence scoring, risk treatment plans with owner/date/KPI fields, risk appetite statements with category-level tolerance thresholds, board risk reports, and risk workshop facilitation guides.

---

## 2. Intended Audiences

This skill is designed for **risk, compliance, and operations teams** working on risk management implementation, maturity improvement, and integration with other management systems. It is most useful for:

- **Chief Risk Officers (CROs)** and **Risk Managers** designing or maturing enterprise risk management programmes
- **Compliance and assurance teams** embedding risk management into ISO 27001, ISO 9001, or other management systems
- **Board secretaries and governance professionals** preparing board risk reports and risk appetite statements
- **Project managers** needing structured risk assessment for major initiatives
- **Internal auditors** reviewing the risk management framework and risk register quality
- **Consultants** supporting clients through first-time ISO 31000 framework implementation
- **Operations managers** assessing and treating operational risks at the process level

---

## 3. Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| **Framework gap analysis** | "Assess our current risk management programme against ISO 31000:2018 and identify the key gaps." |
| **Risk register development** | "Help me build a risk register for our fintech startup covering strategic, financial, cyber, and regulatory risks." |
| **Risk treatment plan** | "Generate a risk treatment plan for our top 5 critical risks from the attached risk register." |
| **Risk appetite statement** | "Write a risk appetite statement for a healthcare organisation with category tolerances for compliance, cyber, and operational risk." |
| **Risk workshop facilitation** | "Help me plan and facilitate a risk identification workshop for our supply chain operations team." |
| **Risk management policy** | "Write a Risk Management Policy for a 500-person professional services firm aligned to ISO 31000:2018." |
| **Framework design** | "How do I design and implement an ISO 31000-compliant risk management framework for a newly established NHS trust?" |
| **Risk criteria definition** | "Help me define a 5×5 likelihood and consequence scale calibrated for a mid-sized logistics business." |
| **Integration question** | "How does ISO 31000 relate to ISO 27001 Clause 6.1? Can I use a single risk register for both?" |
| **Board risk report** | "Generate a quarterly board risk report template following ISO 31000 reporting principles." |
| **Monitoring and review** | "What should our quarterly risk review process look like? What records do we need to keep?" |
| **FMEA / Bowtie** | "Walk me through a bowtie analysis for our main production process." |

---

## 4. How to Use the Skill

Once the skill is installed in Claude, it activates automatically whenever you ask about ISO 31000, risk management frameworks, risk registers, risk treatment, risk appetite, or related enterprise risk management topics. You do not need to reference the skill by name.

### Tips for best results

**Provide your organisational context** — sector, size, and current risk maturity level (ad hoc / defined / managed / optimised) help the skill tailor outputs. For example:

> "We're a 300-person SaaS company with no formal risk management programme. Help us design an ISO 31000-aligned framework from scratch."

**Specify the task type clearly** — the skill adapts its output format based on what you need (gap analysis vs. risk register vs. policy). Be direct:

> "Run a gap analysis of our risk management framework against ISO 31000:2018 Clause 5 (Framework)."

**Reference specific clauses when relevant** — for precise guidance, citing the clause number produces more targeted responses:

> "We need help with Clause 6.3 — how should we define our risk criteria for a financial services firm?"

**Provide your existing risk register or controls list** when asking for analysis or treatment planning — this produces more actionable, specific outputs than a blank-slate response.

### Example interaction

```
You:     Help me build a risk register for our logistics company. We have about 50 staff
         and provide last-mile delivery services. We've never done a formal risk assessment.

Claude:  [Generates a populated risk register with:
          - 15–20 risks across strategic, financial, operational, cyber, compliance,
            and people categories calibrated to a logistics SME
          - Likelihood and consequence scoring with inherent and residual scores
          - Treatment option recommendations for high/critical risks
          - Suggested risk owners and review dates
          - Notes on how to adapt the register as the business grows]
```

---

## 5. Skill Implementation Details

### Architecture

```
iso31000/
├── SKILL.md                                    # Core skill logic and workflows
└── references/
    ├── iso31000-framework.md                   # Clause 5 framework deep-dive
    ├── iso31000-risk-assessment-process.md     # Clause 6 risk assessment guidance
    └── iso31000-risk-treatment.md              # Risk treatment, appetite, monitoring
```

`SKILL.md` is loaded into Claude's context whenever the skill triggers. Reference files are loaded on demand — only the relevant file(s) are loaded per task — keeping the context window efficient.

### What's in SKILL.md

- **Persona**: Claude adopts the role of an ISO 31000:2018 Risk Management consultant
- **Output format matrix**: Maps each task type to the appropriate format (table, document, narrative)
- **8 ISO 31000 principles**: Full table with practical descriptions and assessment guidance
- **Framework (Clause 5)**: Six framework components (5.1–5.6) with key outputs and gaps
- **Risk management process (Clause 6)**: All 8 process activities with templates and guidance
- **5 core workflows**: Gap analysis, risk register development, risk appetite statement, risk workshop facilitation, policy/procedure generation
- **Integration mapping table**: How ISO 31000 relates to ISO 27001, ISO 9001, ISO 42001, NIST CSF, and COSO ERM
- **Reference file loading logic**: Rules for when to load each reference file

### What's in the reference files

| File | Contents |
|------|----------|
| `iso31000-framework.md` | Full Clause 5 framework (5.1–5.6): design checklists, integration maturity levels, RACI template, implementation roadmap, framework KPIs, framework evaluation criteria |
| `iso31000-risk-assessment-process.md` | Full Clause 6 assessment process: scope/criteria templates, PESTLE/SWOT, 7 risk identification techniques (brainstorm, FMEA, bowtie, SIPOC, taxonomy checklist), 5×5 matrix, inherent/residual analysis, risk evaluation decision rules, full risk register template, stakeholder consultation plan |
| `iso31000-risk-treatment.md` | All 5 treatment options with selection guidance, full risk treatment plan template, treatment decision framework, risk appetite statement template, control effectiveness ratings, monitoring schedule, control testing programme, board/executive reporting formats, recording obligations |

### Inputs used to build the skill

- **ISO 31000:2018** — Principles, framework (Clauses 5.1–5.6), and process (Clauses 6.2–6.7)
- **ISO 31010:2019** — Risk assessment techniques reference (FMEA, bowtie, PESTLE, SWOT, fault tree analysis, Monte Carlo)
- **ISO Guide 73:2009** — Risk management vocabulary (risk, risk appetite, risk tolerance, risk criteria, inherent/residual risk definitions)
- **ISO Annex SL mapping** — How ISO 31000 risk provisions align with ISO 27001:2022, ISO 9001:2015, ISO 42001:2023, ISO 14001:2015, ISO 45001:2018
- **COSO ERM 2017** — Integration points and terminology alignment
- **Common enterprise risk practice** — Likelihood × consequence scaling, risk appetite frameworks, board risk reporting formats, risk register structures, treatment plan templates

### Skill trigger phrases

The skill activates on any of the following topics (non-exhaustive):

`ISO 31000` · `risk management framework` · `risk assessment` · `risk register` · `risk treatment` · `risk appetite` · `risk tolerance` · `risk criteria` · `inherent risk` · `residual risk` · `risk identification` · `risk analysis` · `risk evaluation` · `risk treatment plan` · `likelihood × consequence` · `risk heatmap` · `risk workshop` · `bowtie analysis` · `FMEA` · `enterprise risk management` · `ERM` · `operational risk` · `strategic risk` · `risk monitoring` · `board risk report` · `risk appetite statement`

---

## 6. Author

**Skill designed by:** Hemant Naik  
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)  
**Built with:** Claude (Anthropic) using the Claude Skills framework  
**Date:** April 2026  
**Skill version:** 0.1.0  
**Standard coverage:** ISO 31000:2018 — Risk management — Guidelines

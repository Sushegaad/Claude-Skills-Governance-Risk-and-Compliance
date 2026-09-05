# ISO 27001 Compliance Skill

> A Claude skill for security and compliance teams to navigate ISO/IEC 27001 — from gap analysis and risk assessment to policy generation and control implementation.

---

## 1. What Does the Skill Do?

The ISO 27001 skill turns Claude into an expert ISO 27001 Lead Auditor and ISMS implementation consultant. It provides structured, audit-ready guidance across the full lifecycle of an Information Security Management System (ISMS) — from initial gap assessment through to certification readiness.

The skill covers both **ISO 27001:2013** (114 controls, 14 domains) and **ISO 27001:2022** (93 controls, 4 themes), defaulting to the current 2022 version. It understands the mandatory clauses (4–10), all Annex A controls, mandatory documentation requirements, and the differences between the two versions — including the 11 new controls introduced in 2022.

Outputs are tailored to the task: structured gap analysis tables, full policy documents with document control blocks, control-by-control implementation guides, risk registers, and Statement of Applicability (SoA) templates.

---

## 2. Intended Audiences

This skill is designed for **security and compliance teams** working on ISO 27001 certification, maintenance, or transition. It is most useful for:

- **Information Security Managers (ISMs)** and **CISOs** overseeing ISMS implementation or audit preparation
- **Compliance analysts** conducting gap assessments or maintaining the SoA and risk register
- **Security engineers** seeking implementation guidance on specific Annex A controls
- **Internal auditors** preparing for Stage 1 or Stage 2 certification audits
- **Consultants** supporting clients through first-time certification or transition from 2013 to 2022

---

## 3. Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| **Gap analysis** | "Run a gap analysis of our current ISMS against ISO 27001:2022 Clause 6 and Annex A organisational controls." |
| **Policy generation** | "Write me a complete Access Control Policy mapped to ISO 27001:2022." |
| **Control implementation guidance** | "How do I implement A.5.23 — Information security for use of cloud services?" |
| **Risk assessment** | "Help me build a risk register using the likelihood × impact methodology." |
| **Risk treatment plan** | "Generate a risk treatment plan based on these five identified risks." |
| **Statement of Applicability** | "Create a SoA template covering all 93 Annex A controls for a SaaS company." |
| **Certification readiness** | "What mandatory documents do I need before our Stage 2 audit?" |
| **2013 → 2022 transition** | "What are the key differences between ISO 27001:2013 and 2022, and what do I need to update?" |
| **Control mapping** | "Which 2022 controls map to the old A.12 Operations Security domain?" |
| **Audit preparation** | "What evidence will an auditor look for when reviewing our incident management controls?" |

---

## 4. How to Use the Skill

Once the skill is installed in Claude, it activates automatically whenever you ask about ISO 27001, ISMS, Annex A controls, or related compliance topics. You do not need to reference the skill by name.

### Tips for best results

**Be specific about version** — state whether you're working with ISO 27001:2013, 2022, or both. If you don't specify, the skill defaults to 2022.

**Provide context about your organisation** — industry, size, and ISMS scope help the skill tailor its outputs. For example:

> "We're a 200-person SaaS company. Help me do a gap analysis of our Annex A organisational controls against ISO 27001:2022."

**Name the specific control or clause** — for implementation guidance, referencing the control ID (e.g. `A.8.12`) or clause number (e.g. `Clause 6.1`) produces more targeted responses.

**Ask for one thing at a time** — the skill can handle complex multi-step tasks, but asking for a gap analysis, a policy, and a risk register in a single prompt may produce broad output. It's more effective to work through each task in sequence.

### Example interaction

```
You:     Write me an Incident Response Policy mapped to ISO 27001:2022.

Claude:  [Generates a full policy document including:
          - Document control block (version, author, review date)
          - Purpose and scope
          - Policy statement
          - Roles and responsibilities
          - Incident classification and response procedures
          - Mapping to Clauses 8.1 and Annex A controls A.5.24–A.5.28
          - Review cycle and references]
```

---

## 5. Skill Implementation Details

### Architecture

The skill follows a three-layer structure:

```
iso27001/
├── SKILL.md                          # Core skill logic and workflows
└── references/
    ├── annex-a-2022.md               # All 93 ISO 27001:2022 Annex A controls
    ├── annex-a-2013.md               # All 114 ISO 27001:2013 Annex A controls
    └── control-mapping.md            # 2013 ↔ 2022 cross-reference table
```

`SKILL.md` is loaded into Claude's context whenever the skill triggers. The reference files are loaded on demand — only the relevant one(s) are loaded per task — keeping the context window efficient.

### What's in SKILL.md

- **Persona**: Claude adopts the role of an ISO 27001 Lead Auditor and ISMS consultant
- **Output format matrix**: Maps each task type to a specific output format (table, document, narrative)
- **Mandatory clause summary**: Clauses 4–10 with key deliverables per clause
- **4 core workflows**: Gap Analysis, Policy & Document Generation, Control Implementation Guidance, Risk Assessment
- **Policy-to-control mapping table**: Links 11 common policies to their ISO 27001 clauses and Annex A controls
- **Version comparison table**: Side-by-side 2013 vs 2022 differences
- **Mandatory documentation checklist**: 14 required records for ISO 27001:2022 certification
- **Reference file loading logic**: Rules for when to load each reference file

### What's in the reference files

| File | Contents |
|------|----------|
| `annex-a-2022.md` | All 93 controls with IDs, names, and descriptions; new 2022 controls marked with ⭐ |
| `annex-a-2013.md` | All 114 controls across 14 domains with IDs and names |
| `control-mapping.md` | Full 2022→2013 mapping table; list of 11 new controls; notes on merged/renamed controls |

### Inputs used to build the skill

The skill was constructed using the following inputs:

- **ISO/IEC 27001:2022** — mandatory clauses (4–10), Annex A control set (93 controls), documentation requirements
- **ISO/IEC 27001:2013** — Annex A control set (114 controls across 14 domains)
- **ISO/IEC 27002:2022** — control descriptions and implementation guidance (informative reference)
- **Publicly available transition guidance** — mapping between 2013 and 2022 Annex A controls, summary of 11 new controls
- **Common ISMS audit practice** — typical auditor evidence expectations, mandatory document list, gap analysis methodology
- **Risk assessment methodology** — likelihood × impact scoring, risk treatment options (Accept / Avoid / Transfer / Mitigate), risk register structure

### Skill trigger phrases

The skill activates on any of the following topics (non-exhaustive):

`ISO 27001` · `ISO/IEC 27001` · `ISMS` · `Annex A` · `gap analysis` · `Statement of Applicability` · `SoA` · `risk register` · `risk treatment plan` · `information security policy` · `certification readiness` · `2013 to 2022 transition` · `control implementation` · `internal audit` · `management review` · `nonconformity`

---

## 6. Author

**Skill designed by:** Hemant Naik
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)
**Built with:** Claude (Anthropic) using the Claude Skills framework  
**Date:** March 2026  
**Skill version:** 1.9.0  
**Standard coverage:** ISO/IEC 27001:2013 and ISO/IEC 27001:2022

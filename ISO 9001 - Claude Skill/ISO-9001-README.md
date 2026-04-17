# ISO 9001 Quality Management System — Claude Skill

> A Claude skill for quality, operations, and compliance teams to implement, audit, and certify a Quality Management System (QMS) under ISO 9001:2015.

---

## 1. What Does the Skill Do?

The ISO 9001 skill turns Claude into an expert ISO 9001 Lead Auditor and QMS implementation consultant. It provides structured, audit-ready guidance across the full lifecycle of a Quality Management System — from initial gap assessment through certification readiness and beyond.

The skill covers **ISO 9001:2015** in full — all mandatory clauses (4–10), the seven quality management principles, risk-based thinking, process approach, and all required documented information. It understands common valid exclusions (e.g. Clause 8.3 Design and Development), the differences between 2008 and 2015, and sector-specific extensions including IATF 16949 (automotive), AS9100D (aerospace), ISO 13485 (medical devices), and ISO/IEC 90003 (software).

Outputs are tailored to the task: structured gap analysis tables with 🔴/🟡/🟢 status, complete policy and procedure documents with document control blocks, clause-by-clause audit checklists, CAPA reports with root cause analysis, management review agendas, and certification readiness checklists.

---

## 2. Intended Audiences

This skill is designed for **quality, operations, and compliance teams** working on ISO 9001 certification, maintenance, and continual improvement. It is most useful for:

- **Quality Managers** and **Quality Engineers** overseeing QMS implementation, maintenance, and internal auditing
- **Operations Managers** seeking to document and control production or service delivery processes
- **Compliance teams** preparing for Stage 1 or Stage 2 third-party certification audits
- **Managing Directors / CEOs** of SMEs seeking first-time ISO 9001 certification
- **Internal auditors** planning and conducting audits and writing findings reports
- **Consultants** supporting clients through first-time QMS implementation or recertification
- **Sector-specific teams** in automotive (IATF 16949), aerospace (AS9100D), medical device (ISO 13485), or software (ISO/IEC 90003) organisations using 9001 as the base

---

## 3. Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| **Gap analysis** | "Run a gap analysis of our QMS against ISO 9001:2015. We're a 50-person contract electronics manufacturer." |
| **Policy generation** | "Write me a complete Quality Policy for a professional services firm." |
| **Procedure generation** | "Generate a Documented Information Control Procedure mapped to ISO 9001:2015 Clause 7.5." |
| **Document templates** | "Give me a template for a Nonconformity and Corrective Action Report (CAPA)." |
| **Risk register** | "Help me build a QMS risk and opportunities register for Clause 6.1 for our logistics company." |
| **Internal audit checklist** | "Create an internal audit checklist for Clause 8.4 (supplier controls) at a manufacturing site." |
| **Audit preparation** | "What documentation will an auditor expect to see during a Stage 2 audit of our production processes?" |
| **CAPA support** | "Help me write a corrective action for an NC finding about calibration records." |
| **Management review** | "Generate a management review agenda and minutes template with all required ISO 9001:2015 inputs." |
| **Certification readiness** | "What mandatory documents do we need before our Stage 1 audit?" |
| **Sector extension** | "We're IATF 16949 certified. How do our PPAP and APQP requirements relate to ISO 9001:2015 Clause 8.3?" |
| **Nonconformity records** | "What does ISO 9001:2015 require us to retain as documented information for Clause 8.7 — nonconforming outputs?" |

---

## 4. How to Use the Skill

Once installed in Claude Code, the skill activates automatically whenever you ask about ISO 9001, QMS, quality management, internal audits, nonconformity management, or related topics. You do not need to reference the skill by name.

### Tips for best results

**Give context about your organisation** — the skill tailors outputs based on your sector, products or services, size, and whether you are going for initial certification, maintaining an existing QMS, or transitioning from ISO 9001:2008.

> "We're a 200-person precision machining company supplying to the aerospace sector. Help us prepare for our first ISO 9001:2015 Stage 1 audit."

**Name the specific clause or document** — for targeted outputs, reference the clause number (e.g. `Clause 8.4`) or document type (e.g. `Supplier Evaluation Form`) you need.

**Work one task at a time** — asking for a full QMS implementation plan in one prompt will produce broad output. It's more effective to work through tasks in sequence (gap analysis → priority procedures → audit checklists → CAPA → certification readiness).

**For sector schemes** — state your applicable sector scheme (IATF 16949, AS9100D, ISO 13485) and the skill will integrate sector-specific requirements into its outputs.

### Example interaction

```
You:     Write me a Nonconformity and Corrective Action Procedure for our ISO 9001:2015 QMS.

Claude:  [Generates a full procedure including:
          - Document control block (ID, version, owner, approval, review date)
          - Purpose and scope
          - Definitions (NC, CAPA, major/minor)
          - Roles and responsibilities
          - Procedure steps: identification → containment → root cause → corrective action → verification → closure
          - Mapping to Clause 8.7 and 10.2
          - Records required
          - Related documents
          - Revision history table]
```

---

## 5. Skill Implementation Details

### Architecture

```
iso9001/
├── SKILL.md                              # Core skill logic and workflows
└── references/
    ├── iso9001-clauses-requirements.md   # Detailed clause-by-clause requirements (4–10)
    ├── iso9001-quality-controls.md       # Process control framework and control tables
    └── iso9001-document-templates.md     # Ready-to-use document templates (10 templates)
```

`SKILL.md` is loaded into Claude's context whenever the skill triggers. Reference files are loaded on demand — only when needed for the specific task — keeping the context window efficient.

### What's in SKILL.md

- **Persona**: Claude adopts the role of an ISO 9001 Lead Auditor and QMS implementation consultant
- **Output format matrix**: Maps each task type to a specific output format (gap table, document, checklist, CAPA, narrative)
- **Standard overview**: Seven quality management principles; risk-based thinking vs. preventive action; Annex SL
- **Clause structure summary**: All mandatory clauses (4–10) with key deliverables per clause
- **6 core workflows**: Gap Analysis, Policy & Procedure Generation, CAPA, Internal Audit Support, Process Documentation, Certification Readiness
- **Integration table**: ISO 9001 alignment with ISO 14001, ISO 45001, ISO 27001, ISO 42001, IATF 16949, AS9100D, ISO 13485
- **Sector scheme awareness**: Context-specific guidance for automotive, aerospace, medical devices, software, construction, food
- **Mandatory documentation checklist**: All documented information required by ISO 9001:2015
- **Key terminology glossary**: 14 key terms defined

### What's in the reference files

| File | Contents |
|------|----------|
| `iso9001-clauses-requirements.md` | Detailed requirements, audit evidence, and common gaps for every sub-clause from 4.1 to 10.3 |
| `iso9001-quality-controls.md` | Process control tables for customer controls, supplier controls, production controls, inspection/calibration, CAPA, document control, internal audit, management review, and continual improvement |
| `iso9001-document-templates.md` | 10 ready-to-use templates: Quality Policy, QMS Scope, Quality Objectives Register, Risk and Opportunities Register, Internal Audit Report, CAPA Report, Management Review Minutes, Supplier Evaluation Form, Competency Matrix, Customer Satisfaction Survey |

### Install this skill

```shell
/plugin install iso9001@grc-skills
```

---

## 6. ISO 9001:2015 at a Glance

| Feature | Detail |
|---------|--------|
| Standard | ISO 9001:2015 |
| Publisher | ISO (International Organization for Standardization) |
| First published | 1987; current version September 2015 |
| Replaced | ISO 9001:2008 (transition deadline: September 2018) |
| Structure | Annex SL High Level Structure — Clauses 4–10 |
| Controls | No Annex A controls — requirements embedded in Clauses 4–10 |
| Certifications worldwide | >1 million (most widely adopted management system standard) |
| Applicable sectors | All — manufacturing, services, construction, software, healthcare, government, education |
| Related sector schemes | IATF 16949 (automotive), AS9100D (aerospace), ISO 13485 (medical devices) |
| Certification body | Any UKAS/IAF-accredited certification body (TÜV, Bureau Veritas, SGS, BSI, Intertek, etc.) |
| Audit cycle | Stage 1 (doc review) → Stage 2 (implementation) → Annual surveillance → Recertification every 3 years |

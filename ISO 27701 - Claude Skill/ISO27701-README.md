# ISO/IEC 27701 Privacy Information Management Skill for Claude

> **Disclaimer:** This skill provides informational guidance based on ISO/IEC 27701:2025
> (standalone edition) and ISO/IEC 27701:2019 (extension edition). It does not constitute legal
> advice or a certification guarantee. ISO 27701 certification does not constitute a GDPR safe
> harbor and has not been approved as a formal Article 42 GDPR certification scheme in most EU
> member states. Certification decisions, Statement of Applicability scoping, and regulatory
> interpretation with material legal consequences should be reviewed by a qualified privacy lawyer,
> ISO 27701 Lead Auditor, or accredited certification body.

---

## 1. What Does the Skill Do?

This skill gives Claude comprehensive expertise in **ISO/IEC 27701** — the international standard
for Privacy Information Management Systems (PIMS). The skill covers both the **ISO 27701:2019**
edition (an extension of ISO 27001, requiring ISO 27001 as a prerequisite) and the current
**ISO/IEC 27701:2025** edition, published 14 October 2025 as a standalone management system
standard — the most significant change being that organisations can now implement and certify a
PIMS without first holding ISO 27001 certification. All 2019 certifications must transition to
the 2025 edition by **October 2028**.

The skill covers the full PIMS lifecycle: gap analysis against all mandatory Clause 4–10
requirements and all 78 Annex A controls (31 PII Controller controls in A.1, 18 PII Processor
controls in A.2, and 29 shared information security controls in A.3); policy and documentation
generation mapped to clause and control; control implementation guidance structured as Purpose →
What to Implement → Evidence → Audit Tips → Regulatory Link; Statement of Applicability (SoA)
generation for controller-only (60 controls), processor-only (47 controls), or dual-role
(78 controls) organisations; privacy risk assessment and DPIA support; and transition guidance
from ISO 27701:2019 to 2025 including control mapping tables.

The skill always clarifies the organisation's role — PII Controller, PII Processor, or both —
before advising on applicable Annex A controls, since this is the fundamental scoping decision.
It leads with GDPR alignment in every explanation of what ISO 27701 is, clearly stating that
certification provides strong evidence of GDPR Arts. 24/32 technical and organisational measures
(TOMs) and accountability under Art. 5(2), while explicitly noting that it is not a GDPR safe
harbor. It also covers regulatory alignment with UK GDPR, CCPA/CPRA, LGPD, PIPEDA, and PDPA.

---

## 2. Intended Audiences

| Role | How They Use the Skill |
|------|----------------------|
| Privacy & DPO Teams | Gap analysis, SoA generation, DPIA support, RoPA completeness review, DSR procedure drafting |
| ISO 27001 Certified Organisations | Extension to PIMS under 2019 edition, transition planning to 2025 edition by October 2028 |
| Organisations Starting Fresh | Standalone PIMS implementation under 2025 edition without ISO 27001 prerequisite |
| Legal Counsel | GDPR alignment evidence documentation, controller/processor contract clauses (A.1.2.7/A.2) |
| Compliance Managers | Certification readiness assessment, mandatory documentation checklist, audit preparation |
| Security & IT Teams | Annex A.3 shared security controls implementation, privacy incident response (A.3.11, A.3.12) |
| Product & Engineering Teams | Privacy by design controls (A.1.4.2–A.1.4.10), SDLC integration |
| Third-Party Risk & Procurement | Processor obligation controls (Annex A.2), sub-processor management (A.2.5.7–A.2.5.9) |

---

## 3. Common Use Cases

### Gap Analysis and Certification Readiness

- "Perform an ISO 27701:2025 gap analysis for our organisation. We are both a PII Controller and PII Processor."
- "We hold ISO 27001:2022 certification. What additional gap analysis do we need for ISO 27701:2019?"
- "Generate a certification readiness checklist with all mandatory documentation for ISO 27701:2025."
- "Which clause requirements are most commonly failed in ISO 27701 audits?"
- "Assess our RoPA, DSR procedure, and consent management against ISO 27701 requirements."

### Statement of Applicability (SoA)

- "Generate a Statement of Applicability for our organisation — we act as a PII Processor only."
- "We process HR data as a controller and payment data as a processor. Build an SoA for both roles."
- "Which A.1 controls can legitimately be excluded from our SoA and what justification is required?"
- "What are the SoA columns for ISO 27701:2025 and how does it differ from a typical ISO 27001 SoA?"

### Control Implementation Guidance

- "Explain control A.1.2.7 — what must our processor contracts include under ISO 27701?"
- "How do we implement privacy by design (A.1.4.2) in our software development lifecycle?"
- "Walk me through A.1.3.5 through A.1.3.11 — the full data subject rights controls."
- "What does control A.2.3.3 require for PII subject rights assistance and what evidence do auditors expect?"
- "How do we implement the sub-processor notification and consent controls under A.2.2.6?"

### Policy and Document Generation

- "Draft an ISO 27701:2025-aligned Privacy Policy covering Clauses 5.2 and A.1.2.2."
- "Generate a Data Subject Rights Procedure mapped to Annex A.1.3.5–A.1.3.11."
- "Create a Privacy Notice template aligned to A.1.3.3 and A.1.3.4."
- "Draft a Data Processing Agreement template satisfying A.1.2.7 and Annex A.2 processor controls."
- "Generate an ISO 27701:2025-compliant DPIA template and procedure mapped to A.1.2.6."
- "Produce a Subcontractor Management Policy covering A.2.5.7–A.2.5.9."

### Privacy Risk Assessment and DPIA

- "Build a privacy risk register template for our cloud-based CRM platform using ISO 27701's risk methodology."
- "When is a DPIA required under ISO 27701? What are the trigger criteria?"
- "We process biometric data at scale for workplace access control. Produce a DPIA aligned to A.1.2.6."
- "What is the difference between a privacy risk assessment and a security risk assessment under ISO 27701?"

### 2019 to 2025 Transition

- "We are ISO 27701:2019 certified. What do we need to do to transition to ISO 27701:2025 by October 2028?"
- "Map the 2019 Annex A controller controls to the 2025 A.1 controls — which are new?"
- "What are the 3 new controller controls and 2 new processor controls added in the 2025 edition?"
- "Can we still certify under ISO 27701:2019 or must we move to 2025?"
- "Does our existing ISO 27001:2022 certification still integrate with ISO 27701:2025?"

### Regulatory Alignment

- "Map ISO 27701 controls to GDPR articles — specifically Art. 5, 13/14, 17, 28, and 35."
- "How does ISO 27701 certification help us demonstrate CCPA/CPRA compliance?"
- "Does ISO 27701 align with Brazil's LGPD? Which controls address LGPD obligations?"
- "Compare ISO 27701's controller/processor obligations to GDPR Arts. 24–28."

---

## 4. How to Use the Skill

### Installation

1. Download `iso27701.skill` from this folder.
2. In Claude, go to **Settings → Skills**.
3. Click **Upload Skill** and select `iso27701.skill`.
4. The skill is now active across your Claude sessions.

### Triggering the Skill

The skill activates automatically when ISO 27701-related topics arise. No special command is needed.
Example phrases that trigger it:

- *"ISO 27701"* or *"ISO/IEC 27701"* or *"PIMS certification"*
- *"Privacy Information Management System"* or *"privacy management system"*
- *"PII Controller controls"* or *"PII Processor obligations"*
- *"Annex A.1"*, *"Annex A.2"*, *"Annex A.3 shared controls"*
- *"ISO 27701 gap analysis"*, *"Statement of Applicability privacy"*
- *"privacy by design ISO"*, *"DPIA ISO 27701"*, *"RoPA ISO 27701"*
- *"ISO 27701 GDPR alignment"*, *"transition from 2019 to 2025"*
- *"extending ISO 27001 with privacy"*, *"standalone PIMS"*

### Example Prompts

```
We are a B2B SaaS company. We act as a PII Controller for our employee HR data and as
a PII Processor for customer data we process on their behalf. We hold ISO 27001:2022
certification. Perform an ISO 27701:2025 gap analysis covering:
(1) All mandatory Clause 4–10 requirements,
(2) Applicable A.1 controller controls,
(3) Applicable A.2 processor controls,
(4) A.3 shared security controls.
Produce a gap table: Control ID | Control Name | Status | Evidence Needed | Gap Notes.
```

```
Generate a full Statement of Applicability (SoA) for our organisation. We are a PII
Processor only — we do not determine the purposes of processing. Include all Annex A.2
and A.3 controls. For each control include: Applicable (Yes/No) | Justification if Not
Applicable | Implementation Status | Evidence Reference.
```

```
We are ISO 27701:2019 certified. Our transition deadline is October 2028. Produce a
transition roadmap covering:
(1) New and changed controls in 2025 vs 2019 (controller and processor),
(2) Clause structure changes,
(3) Documentation updates required,
(4) How our existing ISO 27001:2022 integration is affected,
(5) Transition audit steps and recommended timeline.
```

```
Draft an ISO 27701:2025-compliant Data Processing Agreement template for use with our
downstream customers. Map each clause to the relevant Annex A control (A.1.2.7 and
Annex A.2). Include all required privacy terms and use ISO 27701 terminology throughout
(PII principal, PII controller, PII processor, sub-processor).
```

```
Map ISO/IEC 27701:2025 Annex A controls to GDPR articles. Produce a three-column table:
ISO 27701 Control ID | Control Name | Corresponding GDPR Article(s).
Focus on: transparency (Arts. 13/14), data subject rights (Arts. 15–22), controller
obligations (Art. 24), processor obligations (Art. 28), DPIAs (Art. 35), and
security (Art. 32).
```

---

## 5. Skill Implementation Details

### Architecture

```
iso27701/
├── SKILL.md                              # Core skill — version selection logic, GDPR
│                                         #   alignment framing, Clause 4–10 deliverables,
│                                         #   core workflows, SoA structure, mandatory
│                                         #   documentation checklist, key statements
└── references/
    ├── annex-a-controls.md               # Complete listing of all 78 Annex A controls
    │                                     #   (A.1 controller, A.2 processor, A.3 shared
    │                                     #   security) with descriptions and common gaps
    ├── transition-guide.md               # Detailed 2019 → 2025 transition guide:
    │                                     #   control mapping table, gap analysis approach,
    │                                     #   transition audit steps, timeline
    └── regulatory-mapping.md             # GDPR article-by-article mapping, CCPA/CPRA,
                                          #   LGPD, PIPEDA, PDPA alignment tables
```

### What's in SKILL.md

- **Identity and scope**: Expert ISO 27701 Lead Implementer and PIMS advisor covering both 2019 and 2025 editions
- **Version selection logic**: Rules for defaulting to 2019 (existing ISO 27001 certified) vs. 2025 (fresh start), with clear reasoning
- **GDPR alignment framing**: Mandatory mention of GDPR alignment, safe harbor limitations, and Arts. 24/32 TOMs evidence value
- **Response format table**: Output formats for gap analysis, policy generation, control guidance, SoA, privacy risk assessment, DPIA, general questions
- **Standard overview**: ISO 27701:2025 structure (78 controls across A.1/A.2/A.3), transition deadline (October 2028), 2019 edition legacy status
- **Clause 4–10 structure**: All HLS clauses with key PIMS deliverables per clause
- **Core workflows**: Gap analysis (status definitions), policy and document generation (core document-to-clause mapping), control implementation guidance, privacy risk assessment, SoA generation
- **2019 vs 2025 comparison table**: 10 key differences across standard type, prerequisites, control counts, new areas
- **Mandatory documentation checklist**: 18 mandatory records for ISO 27701:2025 certification
- **Key statements section**: Explicit clarifications on GDPR safe harbor, certification requirements by version, scope limitations

### What's in the reference files

| File | Contents |
|------|----------|
| `annex-a-controls.md` | Complete listing of all 78 Annex A controls: A.1 (31 PII Controller controls across 4 domains — lawful basis, transparency, data subject rights, privacy by design, data transfers); A.2 (18 PII Processor controls — controller authority, helping with rights requests, sub-processor management, privacy by design); A.3 (29 shared information security controls — policies, HR security, asset management, access control, cryptography, physical security, operations, communications, incident management, business continuity); each with description and common gaps |
| `transition-guide.md` | Detailed 2019 → 2025 transition: new controls added (3 controller, 2 processor), removed/merged controls, clause structure mapping, SoA update requirements, QMS/documentation updates, transition audit approach, recommended 18-month transition timeline with milestones |
| `regulatory-mapping.md` | GDPR article-by-article mapping to ISO 27701 controls (Arts. 5–6, 12–22, 24, 28, 30, 32, 35–36, 44–49); UK GDPR alignment notes; CCPA/CPRA mapping (consumer rights, vendor obligations); LGPD controller/processor alignment; PIPEDA 10 Fair Information Principles mapping; PDPA (Singapore/Thailand) alignment |

### Inputs used to build the skill

| Source | Description |
|--------|-------------|
| ISO/IEC 27701:2025 | Full standard — Clauses 1–10, Annexes A, B, and GDPR correspondence annex |
| ISO/IEC 27701:2019 | First edition — extension model, Annex A (controller) and Annex B (processor) |
| ISO/IEC 27001:2022 | ISMS standard — integration model with PIMS |
| GDPR (EU) 2016/679 | Full text — for article-by-article control mapping |
| UK GDPR / DPA 2018 | UK data protection framework alignment |
| CCPA/CPRA (California) | Consumer privacy rights and vendor obligation mapping |
| LGPD (Brazil) | Lei Geral de Proteção de Dados — controller/processor alignment |
| PIPEDA (Canada) | 10 Fair Information Principles mapping |
| PDPA (Singapore and Thailand) | Privacy management alignment |

### Skill trigger phrases

`ISO 27701`, `ISO/IEC 27701`, `ISO 27701:2025`, `ISO 27701:2019`, `PIMS certification`,
`Privacy Information Management System`, `privacy management system standard`,
`PII Controller`, `PII Processor`, `Annex A.1 controller controls`, `Annex A.2 processor controls`,
`Annex A.3 shared controls`, `ISO 27701 gap analysis`, `Statement of Applicability privacy`,
`privacy risk assessment ISO`, `DPIA ISO 27701`, `RoPA ISO 27701`, `Records of Processing Activities`,
`data subject rights procedure`, `privacy by design ISO`, `sub-processor ISO 27701`,
`ISO 27701 GDPR alignment`, `extending ISO 27001 privacy`, `standalone PIMS`,
`transition from 27701:2019`, `October 2028 transition`, `privacy certification`,
`GDPR Art. 42 certification`, `PII subject rights assistance`, `privacy incident response ISO`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.9.0 — September 2026

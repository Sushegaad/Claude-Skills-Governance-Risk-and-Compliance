# GDPR Compliance Skill

A Claude skill that acts as an expert GDPR compliance assistant — combining deep regulatory
knowledge with practical technical understanding to help teams build, document, and audit
privacy-compliant systems.

---

## What Does the Skill Do?

This skill gives Claude four distinct capabilities that activate automatically whenever a
GDPR or data privacy topic arises:

**1. Code & System Auditing** — Reviews code, database schemas, API designs, and architecture
descriptions for GDPR violations. Produces a structured audit report with severity-graded findings
(🔴 High / 🟡 Medium / 🟢 Low), each mapped to the specific GDPR article being breached or at risk.

**2. Document Drafting** — Generates ready-to-customise GDPR compliance documents from built-in
templates, including Privacy Notices, Data Processing Agreements (DPAs), Cookie/Consent Banners,
Data Protection Impact Assessments (DPIAs), Data Retention Policies, and Data Subject Rights
Procedures.

**3. Compliance Q&A** — Answers GDPR questions with authoritative article citations using a
structured format: direct answer first, followed by the governing article, any exceptions, and
practical implications.

**4. Data Flow & PII Review** — Analyses data flows and PII handling practices across six
dimensions (what, why, where, who, how long, how protected), checks alignment with Records of
Processing Activities (RoPA) requirements, and produces a PII handling checklist.

All responses cite the relevant GDPR article(s) — for example: *"Consent must be freely given,
specific, informed, and unambiguous (Art. 7; Recital 32)."*

---

## Intended Audiences

This skill is designed for two primary audiences who often need to collaborate on GDPR compliance:

**Developers & Engineers**
- Backend and full-stack engineers processing personal data
- DevOps / platform engineers managing infrastructure storing PII
- Security engineers assessing technical controls
- Architects designing data flows across systems or borders

**Legal, Compliance & Privacy Professionals**
- Data Protection Officers (DPOs)
- In-house legal counsel and privacy lawyers
- Compliance managers conducting audits
- Privacy programme leads rolling out GDPR frameworks

The skill adapts its tone automatically — technical and code-focused for developers, legally
precise for compliance and legal professionals.

---

## Common Use Cases

| Use Case | Workflow Triggered |
|----------|--------------------|
| "Is this database schema GDPR compliant?" | Code & System Audit |
| "Review this REST API for personal data issues" | Code & System Audit |
| "Draft a privacy policy for my SaaS product" | Document Drafting |
| "Write a DPA between our company and our cloud vendor" | Document Drafting |
| "Generate a DPIA for our new facial recognition feature" | Document Drafting |
| "Do we need consent or can we use legitimate interests?" | Compliance Q&A |
| "What are our obligations after a data breach?" | Compliance Q&A |
| "Can we use the EU-US Data Privacy Framework? Is it safe given CJEU appeal?" | Compliance Q&A |
| "Map the personal data flows in our onboarding pipeline" | Data Flow & PII Review |
| "Review our RoPA entries for completeness" | Data Flow & PII Review |
| "What data do we need to delete when a user requests erasure?" | Compliance Q&A + Data Flow |
| "Is our cookie banner legally valid?" | Document Drafting + Compliance Q&A |

---

## How to Use the Skill

### Installation
1. Download `gdpr-compliance.skill`
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select the file
4. The skill is now active in your Claude sessions

### Triggering the Skill
The skill activates automatically when you mention GDPR-related topics. You don't need any
special commands. Example prompts that will trigger it:

- *"Is this code GDPR compliant?"*
- *"Draft me a privacy policy for [my app]"*
- *"What lawful basis should I use for analytics?"*
- *"Review our data flow diagram for GDPR gaps"*
- *"What does a DPA need to include under Art. 28?"*

### Tips for Best Results

**For code audits** — Paste the relevant code, schema, or architecture description directly.
The more context you provide (tech stack, data subjects, processing purpose), the more precise
the audit will be.

**For document drafting** — Be ready to provide: your organisation's name and role
(controller/processor), types of personal data involved, processing purposes, any third
parties or sub-processors, and target countries for data transfers.

**For Q&A** — Ask direct questions. The skill will answer with the governing article first,
then explain exceptions and practical steps.

**For data flow review** — Describe or diagram your data pipeline: what data enters, where it
goes, who can access it, and how long it's kept.

### Scope & Limitations
- Covers **EU GDPR** and **UK GDPR** — updated for the **Data (Use and Access) Act 2025** (DUAA), which introduced Recognised Legitimate Interests, a different international transfer test, and the Senior Responsible Individual (SRI) role; UK adequacy renewed December 2025 through December 2031
- Does **not** cover ePrivacy Regulation, CCPA, or other non-EU privacy laws (though may note
  parallels)
- Responses are **informational guidance**, not legal advice — high-stakes decisions should
  always be reviewed by a qualified DPO or data protection lawyer
- The skill will flag when a matter warrants specialist legal counsel

---

## Skill Implementation Details

### Architecture

```
gdpr-compliance/
├── SKILL.md                    # Core skill — four workflow definitions + triggering rules
└── references/
    ├── documents.md            # Six document templates (Privacy Notice, DPA, Consent
    │                           #   Banner, DPIA, Retention Policy, DSR Procedure)
    ├── privacy-notice.md       # Standalone Art. 13/14 privacy notice reference
    ├── dpa-template.md         # Standalone Art. 28 DPA reference with current transfer
    │                           #   mechanisms (EU-US DPF, 2021 SCCs, UK adequacy)
    └── updates-2025.md         # Material regulatory updates 2024–2026: DPF + CJEU
                                #   appeal, UK DUAA 2025, EDPB Opinion 28/2024 on AI,
                                #   CJEU SRB pseudonymisation ruling, Russmedia platform
                                #   controller ruling, EDPB Guidelines 1/2024 on LI,
                                #   CEF 2025 erasure enforcement, ePrivacy withdrawal
```

The skill uses **progressive disclosure** — `SKILL.md` is always in context, while reference
files are loaded on demand only when document drafting is triggered, keeping the context
window efficient.

### How It Was Built

**Inputs provided to build this skill:**

| Input | Value |
|-------|-------|
| Primary capabilities | Code auditing, document drafting, compliance Q&A, data flow review |
| Target audience | Both technical (developers) and legal/compliance professionals |
| Citation style | Cite specific GDPR articles throughout all responses |
| Regulatory scope | EU GDPR (primary) + UK GDPR notes |
| Document templates | Privacy Notice, DPA, Consent Banner, DPIA, Retention Policy, DSR Procedure |

**Key design decisions:**

- **Dual-tone adaptability** — the skill detects context (code vs. document vs. question) and
  adjusts language register accordingly, without requiring the user to specify their role.
- **Article-first citations** — every compliance assertion is anchored to a specific GDPR
  article, making responses auditable and defensible rather than advisory opinion.
- **Severity grading in audits** — findings are classified as High / Medium / Low with clear
  definitions, so developers and legal teams can prioritise remediation effort.
- **Escalation guardrails** — a built-in disclaimer triggers automatically for high-risk
  scenarios (special category data, international transfers, children's data, enforcement risk)
  to prevent the skill from substituting for specialist legal counsel.
- **Template modularity** — each document template uses `[PLACEHOLDER]` markers for
  organisation-specific details, making outputs immediately usable as working drafts rather
  than generic examples.

### GDPR Coverage

The skill covers the full regulation across these key areas:

| Topic Area | Articles Covered |
|-----------|-----------------|
| Data subject rights | Arts. 15–22 |
| Lawful basis & consent | Arts. 6–8 |
| Controller/processor obligations | Arts. 24–28, 30–31 |
| Special category data | Arts. 9–10 |
| Transparency & notices | Arts. 12–14 |
| Security & breach response | Arts. 32–34 |
| DPIA & prior consultation | Arts. 35–36 |
| International transfers | Arts. 44–49 |
| Penalties & enforcement | Arts. 77–84 |

---

## Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)
Skill version: 1.9.0 — September 2026. Updated for: UK DUAA 2025; EU–US DPF with CJEU appeal guidance; EDPB Opinion 28/2024 on AI models; CJEU SRB pseudonymisation ruling; Russmedia platform controller ruling; EDPB Guidelines 1/2024 on legitimate interests; CEF 2025 erasure enforcement; ePrivacy Regulation withdrawal. Benchmark: 92% with skill vs 80% baseline (+12%) — September 2026 primary-source assertion set.

> ⚠️ **Disclaimer**: This skill provides informational guidance based on the GDPR text and
> established regulatory guidance (EDPB/ICO). It does not constitute legal advice. For matters
> involving significant compliance risk, supervisory authority interaction, or complex
> cross-border scenarios, consult a qualified data protection lawyer or your DPO.

# Claude Skills for Governance, Risk & Compliance (GRC)
Expert-level compliance guidance for ISO 27001, SOC 2, FedRAMP, GDPR, and HIPAA — powered by Claude Skills. 

Benchmarked across 10 test cases (2 per framework) using eval framework — each graded against 7 verifiable assertions by independent agents. Skills scored **99% ± 4%** vs a baseline of 93% ± 7%.

[![Release: v0.1.0](https://img.shields.io/badge/Release-v0.1.0-brightgreen.svg)](../../releases/tag/v0.1.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 5](https://img.shields.io/badge/Skills-5-green.svg)](#the-skills)
[![Built with Claude](https://img.shields.io/badge/Built%20with-Claude-orange.svg)](https://claude.ai)

---

## Table of Contents

- [What Are Claude Skills?](#what-are-claude-skills)
- [Who Is This For?](#who-is-this-for)
- [The Skills](#the-skills)
  - [ISO 27001](#-iso-27001)
  - [SOC 2](#-soc-2)
  - [FedRAMP](#-fedramp)
  - [GDPR](#-gdpr)
  - [HIPAA](#-hipaa)
- [Potential Use Cases](#potential-use-cases)
- [How to Install a Skill](#how-to-install-a-skill)
- [Skill Evaluation](#skill-evaluation)
- [Support & Contributing](#support--contributing)
- [Author](#author)
- [Disclaimer](#disclaimer)

---

## What Are Claude Skills?

Claude Skills are installable knowledge packages that extend Claude's capabilities for specific domains. A skill is a `.skill` file — a bundled archive containing a `SKILL.md` instruction file and optional reference materials — that you upload to Claude once and use across all your conversations.

Once installed, a skill activates **automatically** when your conversation touches its topic area. You don't need to invoke it by name or use special commands. Claude simply becomes a deeper expert in that domain for the duration of your session.

**Skills are ideal when you need:**
- Consistent, expert-level responses on a specialized topic
- Outputs formatted to professional or regulatory standards (e.g., audit-ready control narratives, policy templates with the right clauses)
- Domain knowledge that goes beyond general LLM training — such as knowing which specific NIST 800-53 controls apply to a given scenario, or which GDPR articles govern international data transfers

**How skills work under the hood:** Each `.skill` file contains a primary `SKILL.md` that is loaded into Claude's context when the skill triggers, plus reference files that are loaded on demand for deeper sub-topics. This "progressive disclosure" pattern keeps context usage efficient while making comprehensive knowledge available when needed.

---

## Who Is This For?

These skills are designed for professionals who work on information security, privacy, and regulatory compliance — whether at organizations seeking certification, development teams building compliant systems, or advisors supporting clients.

**Security & Compliance Teams** use these skills to accelerate gap assessments, generate first-draft policies, map controls, and prepare evidence packages — compressing weeks of reference work into minutes.

**Software Developers & Engineers** use them to understand what controls their systems must implement, audit code and architecture for compliance issues, and get actionable technical guidance tied to specific regulatory requirements.

**Legal, Privacy & GRC Professionals** use them to draft regulatory documents (DPAs, BAAs, privacy notices), answer client questions with precise regulatory citations, and stay current on framework requirements.

**Healthcare Organizations** use the HIPAA skill to assess systems, generate required notices and agreements, and train staff on obligations — without needing a compliance consultant for every question.

**Cloud Service Providers** pursuing federal government contracts use the FedRAMP skill to navigate the ATO process, write SSP narratives, manage POA&Ms, and prepare for 3PAO assessments.

**Startups and SMBs** use these skills to understand what a given framework requires of them, scope their compliance programs, and get expert-quality output without a large in-house team.

---

## The Skills

### 🔐 ISO 27001

**File:** `ISO 27001 - Claude Skill/iso27001.skill`

The ISO 27001 skill turns Claude into an expert ISO 27001 Lead Auditor and ISMS implementation consultant. It covers both **ISO 27001:2013** (114 controls, 14 domains) and **ISO 27001:2022** (93 controls, 4 themes), defaulting to the current 2022 version.

**What it does:**
- Runs structured **gap analyses** against mandatory clauses (4–10) and all Annex A controls
- Generates complete, audit-ready **policy documents** with document control blocks, scope statements, and clause-to-control mappings
- Provides step-by-step **control implementation guidance** for any Annex A control
- Builds **risk registers** and **risk treatment plans** using the likelihood × impact methodology
- Creates **Statement of Applicability (SoA)** templates covering all 93 controls
- Guides **2013 → 2022 transition**, explaining the 11 new controls and mapping changes

**Trigger phrases:** `ISO 27001`, `ISMS`, `Annex A`, `Statement of Applicability`, `SoA`, `gap analysis`, `risk register`, `certification readiness`, `internal audit`

---

### ✅ SOC 2

**File:** `SOC 2 - Claude Skill/soc2.skill`

The SOC 2 skill turns Claude into an expert SOC 2 compliance advisor grounded in the **AICPA 2017 Trust Services Criteria (TSC) with 2022 Revised Points of Focus**. It covers all five TSC: Security (CC1–CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1), and Privacy (P1–P8).

**What it does:**
- Conducts **gap analyses** across in-scope TSC criteria with 🔴/🟡/🟢 status ratings and remediation roadmaps
- Drafts all **12 core SOC 2 policies** (Information Security, Access Control, Incident Response, Change Management, Risk Assessment, Vendor Management, BCP/DR, and more)
- Documents **controls** in auditor-ready format: Control ID, TSC criterion, type, owner, frequency, evidence, and test procedure
- Produces **evidence checklists** mapped to each criterion, with sampling guidance for Type 1 vs Type 2 audits
- Handles **vendor risk**: tiering, 32-question security questionnaires, SOC 2 report review, CUEC tracking, and contractual requirements
- Adapts its tone — plain-language for first-time SOC 2 teams, technical AICPA-coded output for practitioners and auditors

**Trigger phrases:** `SOC 2`, `Trust Services Criteria`, `TSC`, `CC6`, `Type 1`, `Type 2`, `AICPA`, `audit readiness`, `control statement`, `evidence`

---

### 🏛️ FedRAMP

**File:** `FedRamp - Claude Skill/fedramp.skill`

The FedRAMP skill turns Claude into a knowledgeable FedRAMP advisor covering the full authorization lifecycle for Cloud Service Providers (CSPs) under the current **NIST SP 800-53 Rev 5** baseline. It is current as of 2025–2026, incorporating the Rev 5 transition, the September 2026 OSCAL mandate, and December 2024 template updates.

**What it does:**
- Conducts **readiness and gap assessments** using a 75+ item checklist across 14 security domains
- Guides authoring of **ATO documentation**: System Security Plans (SSP), POA&Ms, SAPs, SARs, and all required appendices (A–Q)
- **Maps NIST 800-53 Rev 5 controls** across all 20 control families to specific system implementations
- Provides **cloud architecture guidance** for AWS GovCloud, Azure Government, and Google Cloud Government
- Supports **Continuous Monitoring (ConMon)** obligations: monthly deliverables, POA&M SLA management, deviation requests
- Guides the **Rev 4 → Rev 5 transition**, FIPS 199 impact level scoping, and OSCAL readiness

**Trigger phrases:** `FedRAMP`, `ATO`, `SSP`, `POA&M`, `3PAO`, `NIST 800-53`, `ConMon`, `AWS GovCloud`, `Azure Government`, `impact level`, `OSCAL`

---

### 🇪🇺 GDPR

**File:** `GDPR - Claude Skill /gdpr-compliance.skill`

The GDPR skill turns Claude into an expert GDPR compliance assistant that bridges technical and legal perspectives. It covers the full **EU GDPR** regulation with notes on **UK GDPR (DPA 2018)** where the rules differ, and adapts its tone automatically — technical for developers, legally precise for compliance and privacy professionals.

**What it does:**
- **Audits code, APIs, database schemas, and architectures** for GDPR violations, producing severity-graded findings (🔴/🟡/🟢) mapped to specific GDPR articles
- **Drafts compliance documents** from built-in templates: Privacy Notices (Art. 13/14), Data Processing Agreements (Art. 28), Cookie/Consent Banners, DPIAs (Art. 35), Data Retention Policies, and Data Subject Rights Procedures
- **Answers compliance questions** with authoritative article citations — every response leads with the governing article, then exceptions, then practical implications
- **Reviews data flows and PII handling** across six dimensions (what, why, where, who, how long, how protected) and checks alignment with RoPA requirements
- Covers all key GDPR areas: lawful basis, consent, data subject rights (Arts. 15–22), international transfers (Arts. 44–49), breach response (Arts. 32–34), special category data (Arts. 9–10), and penalties (Arts. 77–84)

**Trigger phrases:** `GDPR`, `data protection`, `privacy`, `personal data`, `DPA`, `DPIA`, `lawful basis`, `data subject rights`, `consent`, `RoPA`, `Schrems II`, `ICO`, `EDPB`

---

### 🏥 HIPAA

**File:** `HIPAA - Claude Skill/hipaa-compliance.skill`

The HIPAA skill turns Claude into a knowledgeable HIPAA compliance advisor covering the **Privacy Rule, Security Rule, and Breach Notification Rule** (45 CFR Parts 160 and 164, as amended by HITECH). It serves both technical teams building systems that handle ePHI and compliance/legal teams managing organizational obligations.

**What it does:**
- **Reviews documents, systems, and architectures** for HIPAA compliance, producing structured findings with CFR citations, risk levels (High / Medium / Low), and remediation steps
- **Generates HIPAA-compliant documents** from nine ready-to-use templates: Notice of Privacy Practices (NPP), Business Associate Agreements (BAA), Authorization Forms, Workforce Training Acknowledgments, Security Incident Reports, Risk Analysis Templates, and more — all with inline CFR citations
- **Advises on technical safeguards** for modern cloud environments (AWS, Azure, GCP), FHIR APIs, mobile/BYOD, and DevOps pipelines — covering all 54 Security Rule implementation specifications (Required and Addressable)
- **Explains HIPAA in plain language** for any audience — from developers needing encryption guidance to general staff learning what counts as PHI
- **Guides breach response** using the 4-factor risk assessment, notification timelines, HHS reporting obligations, and scenario-by-scenario guidance

**Trigger phrases:** `HIPAA`, `PHI`, `ePHI`, `covered entity`, `business associate`, `BAA`, `NPP`, `breach notification`, `minimum necessary`, `Privacy Rule`, `Security Rule`

---

## Potential Use Cases

| Scenario | Relevant Skill(s) |
|----------|------------------|
| Preparing for an ISO 27001:2022 Stage 2 certification audit | ISO 27001 |
| Writing an Information Security Policy mapped to Annex A | ISO 27001 |
| Running a SOC 2 readiness assessment before engaging an auditor | SOC 2 |
| Documenting controls for a SOC 2 Type 2 report | SOC 2 |
| Scoping a FedRAMP Moderate authorization on AWS GovCloud | FedRAMP |
| Writing SSP control narratives for all 20 NIST 800-53 control families | FedRAMP |
| Auditing an API for GDPR compliance before product launch | GDPR |
| Drafting a DPIA for a new AI feature that processes personal data | GDPR |
| Generating a BAA for a healthcare SaaS vendor relationship | HIPAA |
| Assessing whether a data incident constitutes a reportable HIPAA breach | HIPAA |
| Building a compliance program that satisfies both ISO 27001 and SOC 2 | ISO 27001 + SOC 2 |
| Responding to a customer security questionnaire covering multiple frameworks | All skills |
| Onboarding a new compliance engineer who needs framework context quickly | Any skill |
| Preparing a risk register and treatment plan for an ISMS | ISO 27001 |
| Transitioning from ISO 27001:2013 to ISO 27001:2022 | ISO 27001 |
| Preparing for a FedRAMP Rev 4 → Rev 5 transition | FedRAMP |

---

## How to Install a Skill

1. Download the `.skill` file for the framework you need from this repository (see the folders above).
2. Open Claude and navigate to **Settings → Skills**.
3. Click **Upload Skill** and select the `.skill` file.
4. The skill is now active. Start a new conversation and ask your compliance question — Claude will automatically apply the skill.

> **Tip:** You can install multiple skills at once. If you work across several frameworks (e.g., both ISO 27001 and SOC 2), install all of them — Claude will activate whichever is most relevant to each question.

![Installing Skills in Claude](Installing%20Skills%20in%20Claude.png)

---

## Skill Evaluation

These skills were benchmarked using the [Claude Skill Creator](https://claude.ai) eval framework. 10 realistic test cases were run across all 5 skills — 2 per framework — covering gap analysis, policy drafting, control narratives, code audits, and document generation. Each test case was evaluated against 7 objectively verifiable assertions by independent grader agents.

| Configuration | Pass Rate |
|---------------|-----------|
| **With GRC Skills installed** | **99% ± 4%** |
| Without skills (baseline Claude) | 93% ± 7% |
| **Delta** | **+6 points** |

The skills add the most measurable value on framework-specific tasks: producing correct Annex A control breakdowns for ISO 27001, mapping gaps to CC9 for SOC 2 vendor risk, generating proper formal third-person SSP prose for FedRAMP, handling special category health data correctly under GDPR Art. 9, and consistently including required HIPAA legal disclaimers.

📊 **[View the full eval results →](grc-skills-eval-results.html)**

---

## Support & Contributing

### Reporting Issues

If you find an error, outdated regulatory reference, or missing coverage in any skill, please [open a GitHub issue](../../issues) and include:
- The skill name (e.g., ISO 27001, FedRAMP)
- A description of the issue or incorrect guidance
- The correct information with a source reference if possible (e.g., regulatory text, official guidance document)

### Requesting New Skills

Have a compliance framework not covered here? Open a GitHub issue with the tag `skill-request` and describe the framework, your use case, and the audience it would serve. Community suggestions are welcome for frameworks such as NIST CSF, PCI DSS, CCPA, SOX, CMMC, and others.

### Contributing

Contributions are welcome and encouraged. To contribute:

1. **Fork** this repository and create a new branch for your changes.
2. **For skill improvements** — edit the relevant skill's `SKILL.md` or reference files. Follow the existing structure: YAML frontmatter, a routing/trigger section, and modular reference files.
3. **For new skills** — use the [Claude Skill Creator](https://claude.ai) to build your skill using the same progressive disclosure pattern (a lean `SKILL.md` + reference files loaded on demand).
4. **Cite your sources** — all regulatory content must be traceable to official sources (ISO standards, NIST publications, official regulatory text, agency guidance documents).
5. Submit a **Pull Request** with a clear description of what changed and why.

### Guidelines

- Keep `SKILL.md` focused and under ~500 lines. Offload detailed reference content to separate files in a `references/` folder.
- All compliance assertions must cite the governing clause, article, or control ID.
- Skills should include a disclaimer that outputs are informational guidance, not legal advice.
- Avoid paraphrasing regulatory text in ways that alter its meaning. Where possible, use the authoritative language directly.

---

## Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Built March 2026

---

## Disclaimer

The skills in this repository provide **informational guidance** based on publicly available regulatory and standards documentation. They do not constitute legal, audit, or professional compliance advice. Outputs should be reviewed by qualified professionals — such as a certified ISO 27001 Lead Auditor, licensed attorney, Data Protection Officer, or HIPAA compliance officer — before being relied upon for formal compliance purposes.

Regulatory requirements evolve. Always verify guidance against the latest official publications from the relevant standards body or regulatory authority.

---

*Licensed under the [MIT License](LICENSE).*

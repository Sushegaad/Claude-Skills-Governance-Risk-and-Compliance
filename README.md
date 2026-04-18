# Claude Skills for Governance, Risk & Compliance (GRC)
Expert-level compliance guidance for ISO 27001, SOC 2, FedRAMP, GDPR, HIPAA, NIST CSF, PCI DSS, TSA Cybersecurity, and ISO 42001 AI Management System — powered by Claude Skills.

Benchmarked across 18 test cases (2 per framework) using the eval framework — each graded against 4–5 verifiable assertions by independent agents. Skills scored **94% ± 10%** vs a baseline of 72% ± 28%.

[![Release: v0.3.0](https://img.shields.io/badge/Release-v0.3.0-brightgreen.svg)](../../releases/tag/v0.3.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 9](https://img.shields.io/badge/Skills-9-green.svg)](#the-skills)
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
  - [NIST CSF](#-nist-csf)
  - [PCI DSS](#-pci-dss)
  - [TSA Cybersecurity](#-tsa-cybersecurity)
  - [ISO 42001 AI Management System](#-iso-42001-ai-management-system)
- [Potential Use Cases](#potential-use-cases)
- [How to Install a Skill](#how-to-install-a-skill)
- [Install via Claude Code Marketplace](#install-via-claude-code-marketplace)
- [Skill Evaluation](#skill-evaluation)
- [Customer Testimonials](#customer-testimonials)
- [Support](#support)
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

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
  <iframe src="https://www.youtube.com/embed/-IBLNR0N2vE" title="Claude Skills for GRC Demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;"></iframe>
</div>

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

### 1. 🔐 ISO 27001

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

### 2. ✅ SOC 2

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

### 3. 🏛️ FedRAMP

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

### 4. 🇪🇺 GDPR

**File:** `GDPR - Claude Skill/gdpr-compliance.skill`

The GDPR skill turns Claude into an expert GDPR compliance assistant that bridges technical and legal perspectives. It covers the full **EU GDPR** regulation with notes on **UK GDPR (DPA 2018)** where the rules differ, and adapts its tone automatically — technical for developers, legally precise for compliance and privacy professionals.

**What it does:**
- **Audits code, APIs, database schemas, and architectures** for GDPR violations, producing severity-graded findings (🔴/🟡/🟢) mapped to specific GDPR articles
- **Drafts compliance documents** from built-in templates: Privacy Notices (Art. 13/14), Data Processing Agreements (Art. 28), Cookie/Consent Banners, DPIAs (Art. 35), Data Retention Policies, and Data Subject Rights Procedures
- **Answers compliance questions** with authoritative article citations — every response leads with the governing article, then exceptions, then practical implications
- **Reviews data flows and PII handling** across six dimensions (what, why, where, who, how long, how protected) and checks alignment with RoPA requirements
- Covers all key GDPR areas: lawful basis, consent, data subject rights (Arts. 15–22), international transfers (Arts. 44–49), breach response (Arts. 32–34), special category data (Arts. 9–10), and penalties (Arts. 77–84)

**Trigger phrases:** `GDPR`, `data protection`, `privacy`, `personal data`, `DPA`, `DPIA`, `lawful basis`, `data subject rights`, `consent`, `RoPA`, `Schrems II`, `ICO`, `EDPB`

---

### 5. 🏥 HIPAA

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

### 6. 🛡️ NIST CSF

**File:** `NIST Cybersecurity framework - Claude Skill/NIST Cybersecurity.skill`

The NIST CSF skill turns Claude into an expert NIST Cybersecurity Framework advisor covering both **CSF 2.0** (February 2024) and **CSF 1.1** (April 2018), defaulting to the current CSF 2.0. It covers all six functions — **Govern, Identify, Protect, Detect, Respond, Recover** — including the new Govern function introduced in CSF 2.0.

**What it does:**
- Conducts structured **gap assessments** across all six CSF 2.0 functions, categories, and subcategories
- Builds **Organisational Profiles** — Current and Target — aligned to business context, risk tolerance, and regulatory obligations
- Assesses **Implementation Tiers** (1–4) across three dimensions and provides targeted advancement guidance
- Creates **prioritised implementation roadmaps** with phased 30/60/90-day and strategic actions
- **Maps CSF subcategories** to NIST SP 800-53, ISO 27001:2022, and CIS Controls v8
- Generates **policies aligned to CSF functions** — governance policy, incident response, data security, access control, and more
- Guides **CSF 1.1 → CSF 2.0 migration** with a detailed subcategory mapping and migration checklist

**Trigger phrases:** `NIST CSF`, `Cybersecurity Framework`, `CSF 2.0`, `Govern function`, `GV.SC`, `ID.AM`, `PR.AA`, `DE.CM`, `RS.MA`, `RC.RP`, `cybersecurity profile`, `implementation tiers`, `CSF gap assessment`

---

### 7. 💳 PCI DSS

**File:** `PCI Compliance - Claude Skill/PCI-Compliance.skill`

The PCI DSS skill turns Claude into an expert PCI DSS compliance advisor covering **PCI DSS v4.0.1** (June 2024 — current version), including all requirements that became mandatory on March 31, 2025. It covers all 12 requirements, all 8 SAQ types, merchant and service provider levels, and key v4.0 changes from v3.2.1.

**What it does:**
- **Scopes the Cardholder Data Environment (CDE)** — identifies what's in scope, assesses network segmentation, and recommends scope reduction via tokenisation or P2PE
- **Selects the correct SAQ type** — walks through the decision tree for SAQ A, A-EP, B, B-IP, C, C-VT, P2PE, and D with rationale
- Conducts structured **gap assessments** across all 12 requirements with QSA evidence requirements and common gaps
- Provides **control implementation guidance** for any PCI DSS sub-requirement — what to implement, evidence needed, and common pitfalls
- Generates **PCI DSS-aligned policies** — incident response, access control, cryptography, patch management, data retention, and more
- Guides **v3.2.1 → v4.0.1 migration** including new requirements for MFA expansion, payment page script integrity (Req 6.4.3), phishing protection (Req 5.4.1), and automated log review (Req 10.4.1.1)
- Explains **Defined vs Customised Approach** and when to use Targeted Risk Analysis (TRA)

**Trigger phrases:** `PCI DSS`, `PCI compliance`, `cardholder data`, `CDE`, `SAQ`, `ROC`, `QSA`, `ASV scan`, `PAN`, `tokenisation`, `P2PE`, `merchant level`, `payment page`, `Req 8.4.2`, `Req 6.4.3`

---

### 8. 🚨 TSA Cybersecurity

**File:** `TSA Compliance - Claude Skill/TSA-Compliance.skill`

The TSA Cybersecurity skill turns Claude into an expert TSA cybersecurity directive advisor for **critical transportation infrastructure**. It covers all current TSA Security Directive series — **SD Pipeline-2021-01G**, **SD Pipeline-2021-02F**, **SD 1580-21-01E** (freight rail), and **SD 1582-21-01E** (transit/passenger rail) — plus the **November 2024 NPRM** proposing to formalise these directives as permanent federal regulations.

> **Note on SSI:** TSA Security Directives are classified as **Sensitive Security Information (SSI)** under 49 CFR Part 1520. This skill is built from publicly available summaries, Federal Register notices, and DHS/CISA publications — not the classified full directive text. Covered entities receive the actual directive directly from TSA.

**What it does:**
- **Determines applicability** — which directive series applies to your organisation (pipeline, freight rail, transit, or bus) and what that means for your compliance obligations
- Runs structured **gap assessments** across the four technical domains: IT/OT network segmentation, access controls (MFA), continuous monitoring, and patch management
- **Drafts Cyber Risk Management Program (CRMP) documents**: Cybersecurity Implementation Plan (CIP/COIP), Incident Response Plan (IRP), Architecture Design Review (ADR), and Cybersecurity Assessment Plan (CAP)
- Guides **OT/ICS-specific implementation** — data diodes, jump servers for legacy HMIs, passive monitoring tools (Claroty, Dragos, Nozomi), OT patch lifecycle with vendor coordination
- Explains **24-hour CISA incident reporting** obligations: what qualifies, how to report, sample initial report language, and CIRCIA overlap
- Advises on **annual IRP testing** — two objectives minimum, test scenarios, documentation requirements, and after-action review process
- Explains the **2024 NPRM** impact: NIST CSF 2.0 alignment, CISA CPG baseline, proposed COIP structure, and what changes when the rule is finalised

**Trigger phrases:** `TSA Security Directive`, `SD Pipeline-2021`, `SD 1580-21-01`, `SD 1582-21-01`, `TSA cybersecurity`, `Critical Cyber Systems`, `CCS`, `Cybersecurity Coordinator`, `Cybersecurity Implementation Plan`, `CIP`, `CRMP`, `IRP testing`, `Architecture Design Review`, `ADR`, `CAP`, `CISA 24-hour reporting`, `OT segmentation TSA`, `pipeline cybersecurity`, `rail cybersecurity directive`, `transit cybersecurity`, `TSA NPRM 2024`

---

### 9. 🤖 ISO 42001 AI Management System

**File:** `ISO 42001 - Claude Skill/ISO-42001.skill`

The ISO 42001 skill turns Claude into an expert **ISO/IEC 42001:2023** AI Management System (AIMS) advisor — the world's first international standard for AI governance. It serves both **AI providers** (organisations that develop or deploy AI) and **AI users** (organisations integrating third-party AI), covering the full certification lifecycle from gap assessment through Stage 2 audit readiness.

**What it does:**
- Conducts structured **gap assessments** across all mandatory clauses (4–10) and all **38 Annex A controls** (domains A.2–A.10) with 🔴/🟡/🟢 status, evidence requirements, and a phased remediation roadmap
- Guides the mandatory **AI System Impact Assessment (AISIA)** step by step — identifying affected populations, assessing impact dimensions (severity, reversibility, breadth, human oversight), classifying impact level (Low/Medium/High), and determining proportionate control requirements
- Performs **AI risk assessment** across all risk categories: model risks (bias, drift, hallucination, adversarial attacks), data risks (quality, poisoning, privacy in training data), operational risks (scope creep, human over-reliance), and supply chain risks (third-party model risk, API dependencies)
- Generates a complete **Statement of Applicability (SoA)** covering all 38 Annex A controls (A.2.2–A.10.4) with applicability decisions, justifications, and implementation status
- Drafts all core **AIMS policies** — AI Policy, AI Risk Management Policy, AI Acceptable Use Policy, Data Governance for AI Policy, AI Incident Management Policy, AI System Lifecycle Policy, and AI Supplier Management Policy — each with document control blocks and clause citations
- Produces **Stage 1 and Stage 2 audit checklists** with RAG status, evidence requirements per clause, and common auditor focus areas
- **Maps ISO 42001 to the EU AI Act** — aligns AISIA to the Fundamental Rights Impact Assessment (FRIA) for high-risk AI systems; maps Annex A controls to EU AI Act technical requirements
- **Integrates ISO 42001 with ISO 27001** for organisations building a unified ISMS + AIMS

**Trigger phrases:** `ISO 42001`, `ISO/IEC 42001`, `AI Management System`, `AIMS`, `AISIA`, `AI System Impact Assessment`, `responsible AI standard`, `AI governance standard`, `Annex A AI controls`, `AI risk assessment ISO`, `Statement of Applicability AI`, `AI policy ISO`, `AI certification`, `AI lifecycle controls`, `AI supplier management ISO`, `EU AI Act management system`, `NIST AI RMF ISO mapping`, `AI bias controls`, `AI transparency standard`, `AI incident management ISO`

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
| Assessing current cybersecurity posture using NIST CSF 2.0 | NIST CSF |
| Building a CSF organisational profile with Current and Target states | NIST CSF |
| Advancing from CSF Implementation Tier 1 to Tier 2 | NIST CSF |
| Migrating a cybersecurity programme from CSF 1.1 to CSF 2.0 | NIST CSF |
| Mapping ISO 27001 or SOC 2 controls to NIST CSF subcategories | NIST CSF + ISO 27001 / SOC 2 |
| Writing a Cybersecurity Governance Policy aligned to the CSF GV function | NIST CSF |
| Scoping a PCI DSS CDE for a cloud-hosted e-commerce platform | PCI DSS |
| Selecting the right SAQ type for a merchant using a hosted payment page | PCI DSS |
| Preparing for a Level 1 ROC with a QSA | PCI DSS |
| Implementing the new PCI DSS v4.0 payment page script integrity requirements | PCI DSS |
| Extending MFA to all CDE access per Req 8.4.2 | PCI DSS |
| Managing third-party service providers under PCI DSS Req 12.8 | PCI DSS |
| Determining whether your pipeline or rail operation is a TSA covered entity | TSA Cybersecurity |
| Drafting a Cybersecurity Implementation Plan (CIP) for pipeline OT/SCADA environments | TSA Cybersecurity |
| Planning and documenting annual IRP testing for TSA directive compliance | TSA Cybersecurity |
| Responding to ransomware on IT that may spread to OT — reporting obligations to CISA | TSA Cybersecurity |
| Conducting an Architecture Design Review (ADR) for IT/OT network segmentation | TSA Cybersecurity |
| Implementing MFA and PAM for legacy OT/HMI systems with limited native controls | TSA Cybersecurity |
| Understanding what changes if TSA's November 2024 NPRM becomes final regulation | TSA Cybersecurity |
| Aligning a TSA CRMP to NIST CSF 2.0 and CISA Cross-Sector CPGs | TSA Cybersecurity + NIST CSF |
| Running an ISO 42001 gap assessment for an AI provider with multiple ML models in production | ISO 42001 |
| Completing an AI System Impact Assessment (AISIA) for an automated hiring tool | ISO 42001 |
| Building a Statement of Applicability (SoA) covering all 38 ISO 42001 Annex A controls (A.2–A.10) | ISO 42001 |
| Drafting an AI Policy and AI Acceptable Use Policy for a financial services firm | ISO 42001 |
| Assessing whether a customer-facing AI system requires high-impact controls under ISO 42001 | ISO 42001 |
| Preparing evidence packages for ISO 42001 Stage 1 and Stage 2 certification audits | ISO 42001 |
| Mapping ISO 42001 AISIA requirements to EU AI Act Fundamental Rights Impact Assessment (FRIA) | ISO 42001 |
| Integrating an ISO 42001 AIMS with an existing ISO 27001 ISMS | ISO 42001 + ISO 27001 |
| Governing staff use of public AI tools (ChatGPT, Copilot) under Annex A control A.9.2 and A.9.4 | ISO 42001 |

---

## How to Install a Skill

1. Download the `.skill` file for the framework you need:

   | Framework | Download |
   |-----------|----------|
   | 🔐 ISO 27001 | [iso27001.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ISO%2027001%20-%20Claude%20Skill/iso27001.skill) |
   | ✅ SOC 2 | [soc2.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/SOC%202%20-%20Claude%20Skill/soc2.skill) |
   | 🏛️ FedRAMP | [fedramp.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/FedRamp%20-%20Claude%20Skill/fedramp.skill) |
   | 🇪🇺 GDPR | [gdpr-compliance.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/GDPR%20-%20Claude%20Skill/gdpr-compliance.skill) |
   | 🏥 HIPAA | [hipaa-compliance.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/HIPAA%20-%20Claude%20Skill/hipaa-compliance.skill) |
   | 🛡️ NIST CSF | [NIST Cybersecurity.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/NIST%20Cybersecurity%20framework%20-%20Claude%20Skill/NIST%20Cybersecurity.skill) |
   | 💳 PCI DSS | [PCI-Compliance.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/PCI%20Compliance%20-%20Claude%20Skill/PCI-Compliance.skill) |
   | 🚨 TSA Cybersecurity | [TSA-Compliance.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/TSA%20Compliance%20-%20Claude%20Skill/TSA-Compliance.skill) |
   | 🤖 ISO 42001 AI Management System | [ISO-42001.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ISO%2042001%20-%20Claude%20Skill/ISO-42001.skill) |

2. Open Claude and navigate to **Customize → Skills**.
3. Click **Upload Skill** and select the `.skill` file.
4. The skill is now active. Start a new conversation and ask your compliance question — Claude will automatically apply the skill.

> **Tip:** You can install multiple skills at once. If you work across several frameworks (e.g., both ISO 27001 and SOC 2), install all of them — Claude will activate whichever is most relevant to each question.

![Installing Skills in Claude](Installing%20Skills%20in%20Claude.png)

---

## Install via Claude Code Marketplace

If you use Claude Code — the AI-powered CLI for developers — these skills are also available as installable Claude Code plugins through a hosted marketplace. This is the recommended installation path for developers and teams, as it supports version-pinning, automatic updates, and team-wide distribution without any manual file handling.

Add the marketplace and install the skills you need directly from the terminal:

```shell
/plugin marketplace add Sushegaad/Claude-Skills-Governance-Risk-and-Compliance
/plugin install iso27001@grc-skills soc2@grc-skills fedramp@grc-skills gdpr-compliance@grc-skills hipaa-compliance@grc-skills nist-csf@grc-skills pci-compliance@grc-skills tsa-compliance@grc-skills iso42001@grc-skills
```

Teams can pre-wire the marketplace in `.claude/settings.json` so every developer gets the skills automatically when they open the project — no manual install required.

📖 **[Full installation instructions, team setup, and update guide → INSTALLATION.md](INSTALLATION.md)**

---

## Skill Evaluation

These skills were benchmarked using the [Claude Skill Creator](https://claude.ai) eval framework. **18 realistic test cases** were run across all 9 skills — 2 per framework — covering gap analysis, policy drafting, control narratives, code audits, breach response, CRMP drafting, and AI system impact assessments. Each test case was evaluated against 4–5 objectively verifiable assertions by independent grader agents comparing skill-assisted vs. baseline Claude responses.

| Configuration | Pass Rate |
|---------------|-----------|
| **With GRC Skills installed** | **94% ± 10%** |
| Without skills (baseline Claude) | 72% ± 28% |
| **Delta** | **+22 points** |

### Per-Skill Results (with skills)

| Skill | Test Cases | Pass Rate | What Was Tested |
|-------|-----------|-----------|-----------------|
| ISO 27001 | 2 | 100% | Stage 2 gap analysis; Access Control Policy drafting |
| SOC 2 | 2 | 100% | First-time audit guidance; CC6.3 control documentation |
| FedRAMP | 2 | 88% | AC-2 SSP narrative; Impact level & LI-SaaS guidance |
| GDPR | 2 | 100% | API endpoint audit with article citations; DPA drafting |
| HIPAA | 2 | 100% | Technical safeguards (45 CFR 164.312); Breach notification |
| NIST CSF | 2 | 78% | CSF 2.0 OT/IT gap assessment; Target profile for healthcare |
| PCI DSS | 2 | 90% | Stripe.js SAQ/CDE scope; v4.0.1 new requirements |
| TSA Cybersecurity | 2 | 100% | Pipeline CRMP obligations; Incident Reporting section |
| ISO 42001 | 2 | 90% | AI user gap assessment; AISIA for resume screening |

The skills add the most measurable value on highly framework-specific tasks: producing correct Annex A control IDs for ISO 27001, mapping gaps to CC criteria for SOC 2, generating formal third-person SSP prose with enhancement references for FedRAMP, applying article-level citations for GDPR, distinguishing Required vs. Addressable HIPAA specifications, using CSF 2.0 subcategory IDs for NIST, correctly identifying SAQ types for PCI, referencing specific TSA Security Directives and CISA contact details, and classifying AI system impact levels with AISIA methodology for ISO 42001.

📊 **[View the full eval results →](grc-skills-eval-results.html)**

---

## Customer Testimonials

> *"This is awesome, thank you!"*
> — Reddit u/ThePsychicCEO

> *"This is awesome! Any chance you can build one for ISO 42001?"*
> — Reddit u/ComparisonThink7683

> *"As a rather new Claude Code user, I'm both impressed and thankful. It's really helpful that you release it publicly. I am at the stage where I understand the need for a well-written CLAUDE.md and skills. This will help me a lot."*
> — Reddit u/bloulboi

> *"The skills approach is a good entry point — getting Claude to reason about specific frameworks is exactly the right instinct. The gap I kept hitting was that Claude could describe the compliance picture but couldn't act on it... this is a great start."*
> — Reddit u/sensationweb

> *"Fantastic work. Going to follow this and test it out myself."*
> — Reddit u/Efficient_Bus_923

> *"I've been doing something similar for the CIS controls and it's been brilliant so far. I'll be using this for ISO and SOC 2. Thanks!"*
> — Reddit u/gpldn

> *"Hell ya. We just approved Claude for enterprise so I'll go check it out."*
> — Reddit u/AcrobaticWatercress7

> *"I'll definitely check this out. I have a skill for threat modeling and am working on some other ones, this is super helpful."*
> — Reddit u/lilgreenbite

> *"Awesome, thanks for sharing. I'm going to play around with this."*
> — Reddit u/DeliciousNet593

Additional feedback from the Reddit community: [r/grc](https://www.reddit.com/r/grc/comments/1rwp2x4/using_claude_ai_skills_to_act_as_a_dedicated_grc/) · [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s6r359/comment/od4k30y/)

---

## Support

### Reporting Issues

If you find an error, outdated regulatory reference, or missing coverage in any skill, please [open a GitHub issue](../../issues) and include:
- The skill name (e.g., ISO 27001, FedRAMP)
- A description of the issue or incorrect guidance
- The correct information with a source reference if possible (e.g., regulatory text, official guidance document)

### Requesting New Skills

Have a compliance framework not covered here? Open a GitHub issue with the tag `skill-request` and describe the framework, your use case, and the audience it would serve. Community suggestions are welcome for frameworks such as NIST CSF, PCI DSS, CCPA, SOX, CMMC, and others.

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

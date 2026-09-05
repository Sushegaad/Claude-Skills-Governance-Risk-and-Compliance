# Claude Skills for Governance, Risk & Compliance (GRC)
Expert-level compliance guidance for ISO 27001, SOC 2, FedRAMP, GDPR, HIPAA, NIST CSF, PCI DSS, TSA Cybersecurity, ISO 42001 AI Management System, ISO 27701 Privacy Information Management, DORA Digital Operational Resilience, India's Digital Personal Data Protection Act (DPDPA), CMMC 2.0 Cybersecurity Maturity Model Certification, NIST AI Risk Management Framework, SWIFT Customer Security Programme (CSP), Australian Information Security Manual (ISM), EU NIS2 Directive, CCPA/CPRA California Privacy, ITAR (International Traffic in Arms Regulations), Brazil's LGPD (Lei Geral de Proteção de Dados), EU CSRD (Corporate Sustainability Reporting Directive), CIS Controls v8 (CIS Top 18), EAR (Export Administration Regulations), NIST SP 800-53 (Security and Privacy Controls for Federal Systems), EU AI Act (Regulation (EU) 2024/1689), Section 508 (US Federal ICT Accessibility), WCAG (Web Content Accessibility Guidelines), NZISM (New Zealand Information Security Manual), Vietnam PDPL (Law on Personal Data Protection No. 91/2025/QH15), EU CRA (Cyber Resilience Act, Regulation (EU) 2024/2847), Saudi Arabia GRC (NCA ECC, Saudi PDPL, SAMA, CST), UAE GRC (Federal PDPL, DIFC, ADGM, CBUAE, ICT Health Law), and TISAX (VDA ISA / ENX automotive supplier security) — powered by Claude Skills. **Updated Monthly.**

Benchmarked across 165 test cases using the eval framework — each graded against at least 5 verifiable assertions by independent agents (827 assertions in total). Skills scored **92%** vs a baseline of **63%**.

[![Release: v1.9.0](https://img.shields.io/badge/Release-v1.9.0-brightgreen.svg)](../../releases/tag/v1.9.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 33](https://img.shields.io/badge/Skills-33-green.svg)](#the-skills)
[![Built with Claude](https://img.shields.io/badge/Built%20with-Claude-orange.svg)](https://claude.ai)
[![GitHub Stars](https://img.shields.io/github/stars/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance?style=flat&label=Stars&color=gold)](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)

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
  - [ISO 27701 Privacy Information Management](#-iso-27701-privacy-information-management)
  - [DORA Digital Operational Resilience](#-dora-digital-operational-resilience)
  - [DPDPA India Digital Personal Data Protection](#-dpdpa-india-digital-personal-data-protection)
  - [CMMC 2.0 Cybersecurity Maturity Model Certification](#-cmmc-20-cybersecurity-maturity-model-certification)
  - [NIST AI Risk Management Framework](#-nist-ai-risk-management-framework)
  - [SWIFT Customer Security Programme (CSP)](#-swift-customer-security-programme-csp)
  - [Australian Information Security Manual (ISM)](#-australian-information-security-manual-ism)
  - [EU NIS2 Directive](#-eu-nis2-directive)
  - [CCPA/CPRA California Privacy](#-ccpacpra-california-privacy)
  - [ITAR — International Traffic in Arms Regulations](#-itar--international-traffic-in-arms-regulations)
  - [LGPD — Brazil's General Data Protection Law](#-lgpd--brazils-general-data-protection-law)
  - [CSRD — EU Corporate Sustainability Reporting Directive](#-csrd--eu-corporate-sustainability-reporting-directive)
  - [CIS Controls v8 — CIS Top 18 Cyber Hygiene](#-cis-controls-v8--cis-top-18-cyber-hygiene)
  - [EAR — Export Administration Regulations](#-ear--export-administration-regulations)
  - [NIST SP 800-53 — Security and Privacy Controls for Federal Systems](#-nist-sp-800-53--security-and-privacy-controls-for-federal-systems)
  - [EU AI Act — Regulation (EU) 2024/1689](#-eu-ai-act--regulation-eu-20241689)
  - [Section 508 — US Federal ICT Accessibility](#-section-508--us-federal-ict-accessibility)
  - [WCAG — Web Content Accessibility Guidelines](#-wcag--web-content-accessibility-guidelines)
  - [NZISM — New Zealand Information Security Manual](#-nzism--new-zealand-information-security-manual)
  - [Vietnam PDPL — Law on Personal Data Protection](#-vietnam-pdpl--law-on-personal-data-protection)
  - [EU CRA — Cyber Resilience Act](#-eu-cra--cyber-resilience-act)
  - [Saudi Arabia GRC — Country Compliance Advisor](#-saudi-arabia-grc--country-compliance-advisor)
  - [UAE GRC — Country Compliance Advisor](#-uae-grc--country-compliance-advisor)
  - [TISAX — Trusted Information Security Assessment Exchange](#-tisax--trusted-information-security-assessment-exchange)
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

<a id="-iso-27001"></a>

### 1. <img src="assets/Logos/iso27001.jpg" alt="ISO 27001" height="20" style="vertical-align:middle;object-fit:contain;"> ISO 27001

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

<a id="-soc-2"></a>

### 2. <img src="assets/Logos/soc2.jpeg" alt="SOC 2" height="20" style="vertical-align:middle;object-fit:contain;"> SOC 2

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

<a id="-fedramp"></a>

### 3. <img src="assets/Logos/fedramp.svg" alt="FedRAMP" height="20" style="vertical-align:middle;object-fit:contain;"> FedRAMP [US]

**File:** `FedRamp - Claude Skill/fedramp.skill`

The FedRAMP skill turns Claude into a knowledgeable FedRAMP advisor covering the full authorization lifecycle for Cloud Service Providers (CSPs) under **NIST SP 800-53 Rev 5** and the new **CR26 (FedRAMP Consolidated Rules for 2026)** framework. Current as of August 2026 — CR26 is final (mandatory January 1, 2027) with Certification Classes A–D (A = pilot/transitional, B = LI-SaaS/Low, C = Moderate, D = High), Class pipelines opening August 2026, FedRAMP 20x as the primary pathway, Ready retired July 28, 2026 (Legacy FedRAMP Ready), and the September 30, 2026 OSCAL mandate for new authorizations.

**What it does:**
- Conducts **readiness and gap assessments** using a 75+ item checklist, mapped to CR26 Certification Classes (A/B/C/D)
- Guides authoring of **ATO documentation**: System Security Plans (SSP), POA&Ms (with correct SLAs: Critical=15d, High=30d, Moderate=90d, Low=365d), SAPs, SARs, and all appendices (A–Q)
- **Maps NIST 800-53 Rev 5 controls** across all 20 control families; advises on FedRAMP 20x continuous authorization approach
- Provides **cloud architecture guidance** for AWS GovCloud, Azure Government, and Google Cloud Government
- Supports **Continuous Monitoring (ConMon)** obligations: monthly deliverables, POA&M SLA management, deviation requests
- Advises on **OSCAL readiness** for the mandatory September 30, 2026 submission deadline

**Trigger phrases:** `FedRAMP`, `ATO`, `SSP`, `POA&M`, `3PAO`, `NIST 800-53`, `ConMon`, `AWS GovCloud`, `Azure Government`, `CR26`, `FedRAMP 20x`, `OSCAL`, `Certification Class`

---

<a id="-gdpr"></a>

### 4. 🇪🇺 GDPR [EU]

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

<a id="-hipaa"></a>

### 5. <img src="assets/Logos/hipaa.png" alt="HIPAA" height="20" style="vertical-align:middle;object-fit:contain;"> HIPAA [US]

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

<a id="-nist-csf"></a>

### 6. <img src="assets/Logos/nist-csf.jpeg" alt="NIST CSF" height="20" style="vertical-align:middle;object-fit:contain;"> NIST CSF

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

<a id="-pci-dss"></a>

### 7. <img src="assets/Logos/pci-dss.png" alt="PCI DSS" height="20" style="vertical-align:middle;object-fit:contain;"> PCI DSS

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

<a id="-tsa-cybersecurity"></a>

### 8. 🚨 TSA Cybersecurity [US]

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

<a id="-iso-42001-ai-management-system"></a>

### 9. <img src="assets/Logos/iso42001.webp" alt="ISO 42001" height="20" style="vertical-align:middle;object-fit:contain;"> ISO 42001 AI Management System

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

<a id="-iso-27701-privacy-information-management"></a>

### 10. <img src="assets/Logos/iso27701.png" alt="ISO 27701" height="20" style="vertical-align:middle;object-fit:contain;"> ISO 27701 Privacy Information Management

**File:** `ISO 27701 - Claude Skill/iso27701.skill`

The ISO 27701 skill turns Claude into an expert **ISO/IEC 27701:2025** Privacy Information Management System (PIMS) advisor — covering the full lifecycle from gap assessment through certification. It handles both **ISO 27701:2025** (the new standalone edition) and **ISO 27701:2019** (the legacy ISO 27001 extension), and covers both **PII controllers** and **PII processors**.

**What it does:**
- Conducts structured **gap analyses** across all mandatory HLS clauses (4–10) and all 78 Annex A controls — 31 for PII controllers (A.1), 18 for PII processors (A.2), and 29 shared security controls (A.3)
- Generates complete, audit-ready **PIMS policy documents** — Privacy Policy, Records of Processing Activities (RoPA), Data Subject Rights Procedure, Privacy by Design Procedure, Data Processing Agreements (DPAs), and more
- Builds **privacy risk registers** focused on harm to PII principals, triggers DPIAs for high-risk processing, and produces risk treatment plans
- Creates **Statements of Applicability (SoA)** scoped to the organization's role (controller, processor, or both) with applicability decisions and justification
- Provides **control-by-control implementation guidance** for every A.1, A.2, and A.3 control — with purpose, implementation steps, audit evidence, and common pitfalls
- Guides **2019 → 2025 transitions** with a full control mapping table, gap analysis checklist, and recommended timeline to the October 2028 deadline
- **Maps ISO 27701 to GDPR** article by article, plus CCPA/CPRA, LGPD, PIPEDA, PDPA (Singapore/Thailand), and UK GDPR

**Trigger phrases:** `ISO 27701`, `PIMS`, `privacy information management`, `PII controller`, `PII processor`, `privacy risk assessment`, `DPIA`, `data subject rights`, `records of processing activities`, `RoPA`, `privacy by design`, `data processing agreement`, `DPA`, `GDPR alignment ISO 27701`, `ISO 27701:2025`, `ISO 27701:2019`, `27701 transition`, `standalone PIMS`, `Annex A controller controls`, `Annex A processor controls`

---

<a id="-dora-digital-operational-resilience"></a>

### 11. <img src="assets/Logos/dora.png" alt="DORA" height="20" style="vertical-align:middle;object-fit:contain;"> DORA [EU] — Digital Operational Resilience

**File:** `DORA - Claude Skill/dora.skill`

The DORA skill turns Claude into an expert advisor on **Regulation (EU) 2022/2554** (the Digital Operational Resilience Act) — the anchoring ICT regulation for EU financial entities since 17 January 2025. It encodes all 64 DORA articles, all 12 adopted RTS/ITS, and provides precise article-level guidance for every compliance workflow. It explicitly separates DORA from NIS2, legacy EBA ICT guidelines, and ISO 27001 — a common source of conflation in general LLM responses.

**What it does:**
- Conducts structured **DORA gap analyses** across all four pillars: ICT risk management framework (Chapter II, Art. 5–16), incident management (Chapter III, Art. 17–23), resilience testing / TLPT (Chapter IV, Art. 24–27), and ICT third-party risk (Chapter V, Art. 28–44)
- Guides **ICT-related incident classification** against Art. 18 criteria and the materiality thresholds in CDR (EU) 2024/1772, with a full decision tree for major vs. non-major
- Builds **three-stage incident reporting procedures** per Art. 19 and CDR (EU) 2025/301 — initial (4h), intermediate (72h), final (1 month) — including content requirements at each stage
- Reviews and drafts **contractual provisions** per Art. 30(2)(a)–(i), flagging the common audit-rights gap with hyperscale cloud providers
- Builds or validates the **Register of Information** with all mandatory fields per CIR (EU) 2024/2956
- Assesses **ICT concentration risk** per Art. 28(6) and Art. 29 — including multi-function reliance on a single cloud provider
- Scopes **TLPT programmes** per Art. 26 and CDR (EU) 2025/1190, covering threat intelligence phase, red team test, mutual recognition, and tester qualification requirements
- Drafts **ICT risk management framework** documentation per Art. 6–14 and CDR (EU) 2024/1774
- Precisely distinguishes **Chapter II** (proactive ICT risk governance) from **Chapter III** (reactive incident management) — a common compliance confusion point
- References all **12 adopted RTS/ITS** by exact regulation number (CDR/CIR) with article-level mapping

**Trigger phrases:** `DORA`, `Regulation (EU) 2022/2554`, `digital operational resilience`, `ICT risk management framework`, `DORA gap analysis`, `Art. 6 DORA`, `Art. 17 ICT incident`, `Art. 18 classification`, `Art. 19 incident reporting`, `Art. 26 TLPT`, `Art. 28 third-party risk`, `Art. 30 contractual provisions`, `Register of Information`, `CIR 2024/2956`, `CDR 2024/1772`, `CDR 2024/1773`, `CDR 2024/1774`, `CDR 2025/301`, `CDR 2025/1190`, `TLPT financial entities`, `ICT concentration risk`, `critical ICT TPSP`, `DORA vs NIS2`, `EBA ICT guidelines DORA`, `DORA incident classification`, `DORA reporting timelines`, `Chapter II DORA`, `Chapter III DORA`

---

<a id="-dpdpa-india-digital-personal-data-protection"></a>

### 12. 🇮🇳 DPDPA [India] — Digital Personal Data Protection Act

**File:** `DPDPA - Claude Skill/dpdpa.skill`

The DPDPA skill turns Claude into an expert advisor on India's **Digital Personal Data Protection Act, 2023** and the finalized **DPDP Rules, 2025** (notified 13 November 2025, effective 13 May 2027). It covers all 44 sections of the Act and all 23 Rules, with precise section-level citations, GDPR-alignment mapping, and guidance calibrated for both Indian companies and global organizations with Indian data subjects.

**What it does:**
- Conducts structured **DPDPA gap analyses** covering notice and consent (Sections 5–6 + Rules 3–4), lawful processing (Section 7), Data Fiduciary obligations (Section 8 + Rules 6–9), children's data (Section 9 + Rules 10–12), and SDF obligations (Section 10 + Rule 13)
- **Distinguishes DPDPA from GDPR** across 8 key dimensions — scope (digital-only vs. all personal data), lawful bases (no legitimate interests in DPDPA), consent standard (unconditional + no bundling), cross-border transfers (blacklist vs. whitelist), erasure right (narrower in DPDPA), DPO requirements (SDFs only; India-resident), children's threshold (18 years vs. 16), and enforcement model (single Board vs. multi-DPA)
- Guides **notice design** per Rule 3 — standalone format, plain language, multi-language obligations (Eighth Schedule), and legacy data notice requirements for pre-commencement data
- Advises on the **two lawful bases only** — Consent (Section 6) and the nine Certain Legitimate Uses (Section 7) — and identifies GDPR processing activities that require fresh consent under DPDPA
- Guides **breach notification** per Section 8(6) and Rule 6 — 72-hour Board notification timeline, content requirements, Processor notification obligations, and the difference from GDPR's risk-threshold approach (all breaches notifiable to Board)
- Designs **children's data compliance programmes** — 18-year threshold, Rule 12 parental verification methods (DigiLocker, government tokens, existing verified data, virtual tokens), and absolute prohibitions on tracking/profiling/targeted advertising
- Advises **Significant Data Fiduciaries (SDFs)** on additional obligations — India-resident DPO (Section 10 + Rule 13(2)), annual DPIA (Rule 13(3)), annual independent audit (Rule 13(4)), and data localisation readiness
- Guides **Data Principal rights fulfilment** — access (Section 11), correction/erasure (Section 12), grievance redressal (Section 13 — mandatory exhaustion before Board complaint), and the unique right to nominate (Section 14)
- Advises on **cross-border transfers** — blacklist approach (Section 16), no countries currently notified as restricted (April 2026), and contractual safeguards recommended despite absence of formal restrictions
- Advises **global organisations** on their territorial obligations — India-nexus test (Section 3), GDPR compliance gaps that don't satisfy DPDPA, and GDPR-to-DPDPA migration priorities

**Trigger phrases:** `DPDPA`, `Digital Personal Data Protection Act`, `India data protection`, `Data Fiduciary`, `Data Principal`, `Significant Data Fiduciary`, `SDF`, `Data Protection Board of India`, `DPBI`, `DPDP Rules 2025`, `Section 5 DPDPA`, `Section 6 DPDPA`, `Section 7 DPDPA`, `Section 8 DPDPA`, `Section 9 DPDPA`, `Section 10 DPDPA`, `Rule 3 DPDP`, `Rule 6 DPDP breach notification`, `Rule 12 parental consent`, `India privacy law`, `India digital privacy`, `DPDPA gap analysis`, `DPDPA vs GDPR`, `India data law`, `MeitY data protection`, `DigiLocker consent`, `India children data law`, `DPDPA consent requirements`, `DPDPA breach notification`, `India cross-border data transfer`

---

<a id="-cmmc-20-cybersecurity-maturity-model-certification"></a>

### 13. <img src="assets/Logos/cmmc.png" alt="CMMC" height="20" style="vertical-align:middle;object-fit:contain;"> CMMC 2.0 [US] — Cybersecurity Maturity Model Certification

**File:** `CMMC - Claude Skill/cmmc.skill`

The CMMC 2.0 skill turns Claude into an expert CMMC compliance advisor for US defense contractors navigating the Cybersecurity Maturity Model Certification program. It covers all three CMMC levels — Level 1 (17 FAR 52.204-21 practices), Level 2 (110 NIST SP 800-171 Rev 2 practices), and Level 3 (110+ NIST SP 800-172 requirements) — under the final 32 CFR Part 170 rule (effective December 16, 2024). Current as of August 2026 — including the **July 13, 2026 Phase 2 suspension** (C3PAO requirements in abeyance pending the CMMC Reform Task Force review due ≈ September 13, 2026; self-assessment tracks and all DFARS obligations continue).

**What it does:**
- Determines the correct **CMMC level** for a given contract based on FCI vs. CUI handling, DFARS clauses present (7012, 7019, 7020, 7021), and program criticality
- Conducts structured **gap assessments** across all 17 CMMC domains — AC, AT, AU, CM, IA, IR, MA, MP, PE, PS, RA, CA, SC, SI — against the full 110-practice set for Level 2
- Drafts complete **System Security Plans (SSP)** covering system boundary definition, CUI data flow diagrams, and control implementation narratives for all 110 practices
- Calculates and explains the **SPRS score** (starting at 110; deductions per unmet practice; range −203 to +110) and prioritises highest-impact gaps (MFA, FIPS cryptography, CUI flow control, audit logging)
- Manages the **POA&M lifecycle** — identifies which practices can remain in a POA&M at certification, drafts remediation milestones, and tracks the 180-day closure deadline
- **Scopes CUI** — identifies which systems, people, and processes are in-scope, recommends enclave strategies to reduce scope, and flags FedRAMP Moderate requirements for cloud services handling CUI
- Prepares for **C3PAO assessments** — explains the four-phase assessment process (documentation review, assessment activities, findings, certification decision), lists required evidence per practice type, and identifies the 7 critical practices that block conditional certification
- Explains **DFARS clause obligations**: 72-hour DIBNET incident reporting (DFARS 252.204-7012), SPRS self-assessment submission, and flow-down requirements to subcontractors under DFARS 252.204-7021

**Trigger phrases:** `CMMC`, `CMMC 2.0`, `CMMC Level 2`, `CUI`, `Controlled Unclassified Information`, `NIST 800-171`, `DFARS 7021`, `DFARS 252.204-7021`, `C3PAO`, `SPRS score`, `defense contractor`, `DIB`, `DoD contractor`, `FCI`, `SSP CMMC`, `POA&M CMMC`, `gap analysis CMMC`, `DIBCAC`, `CUI scoping`, `32 CFR Part 170`

---

<a id="-nist-ai-risk-management-framework"></a>

### 14. 🤖 NIST AI Risk Management Framework

**File:** `NIST AI RMF - Claude Skill/nist-ai-rmf.skill`

The NIST AI RMF skill turns Claude into an expert advisor on the **NIST AI Risk Management Framework (AI RMF 1.0)**, published January 2023 as NIST AI 100-1. It covers all four core functions — GOVERN, MAP, MEASURE, and MANAGE — with their 19 categories and subcategories, the AI RMF Playbook's suggested actions, and deep guidance on evaluating AI systems for trustworthiness.

**What it does:**
- Builds **AI organizational profiles** — Current Profile (where you are) and Target Profile (where you want to be) across all 19 categories with gap scoring and a prioritised remediation roadmap
- Conducts **GOVERN gap assessments** across all 6 categories (GV-1 to GV-6) — AI risk policies, accountability structures, roles, cross-functional teams, risk tolerance, and regulatory alignment
- Guides **MAP context-setting** for any AI system — intended use documentation, affected stakeholder mapping, risk/benefit analysis, and likelihood/impact characterization
- Specifies **MEASURE 2.x evaluation actions** before deployment — bias/fairness testing (demographic parity, equalized odds, disparate impact), explainability (SHAP, LIME, counterfactuals), adversarial robustness, privacy assessment, and human oversight validation
- Builds **AI risk registers** with per-risk AI RMF category citations (e.g., MAP 5.2, MEASURE 2.2, MANAGE 2.3), trustworthiness property at risk, treatment options, and owners
- Provides **MANAGE incident response** guidance — model failure triggers, containment procedures, stakeholder notification thresholds, and lessons-learned cycles
- **Maps AI RMF to ISO 42001, EU AI Act, and NIST CSF** — showing which AI RMF categories satisfy Art. 9 (EU AI Act risk management system), equivalent ISO 42001 clauses, and how AI RMF extends NIST CSF beyond cybersecurity into societal and ethical AI risk

**Trigger phrases:** `NIST AI RMF`, `AI RMF`, `NIST AI 100-1`, `AI Risk Management Framework`, `GOVERN function`, `MAP function`, `MEASURE function`, `MANAGE function`, `AI RMF Playbook`, `AI risk profile`, `AI trustworthiness`, `AI bias assessment`, `AI explainability`, `MEASURE 2.2`, `AI risk register`, `AI organizational profile`, `responsible AI framework`, `AI governance framework`, `AI incident response`, `AI RMF gap assessment`

---

<a id="-swift-customer-security-programme-csp"></a>

### 15. 🏦 SWIFT Customer Security Programme (CSP)

**File:** `SWIFT CSP - Claude Skill/swift-csp.skill`

The SWIFT CSP skill turns Claude into an expert advisor on the **SWIFT Customer Security Controls Framework (CSCF) v2026** — the mandatory cybersecurity programme for all SWIFT network participants. It covers all 32 controls (**25 mandatory + 7 advisory** — Control 2.4 Back-Office Data Flow Security promoted to mandatory in v2026), all five architecture types (A1/A2/A3/A4/B), the KYC-SA annual attestation process (window July 1 – December 31, 2026), and complete cross-framework mappings to ISO 27001:2022, PCI DSS v4.0.1, and NIST CSF 2.0.

**What it does:**
- Determines the correct **SWIFT architecture type** (A1/A2/A3/A4/B) from a description of the organisation's SWIFT connectivity and produces the full mandatory/advisory control applicability matrix
- Conducts structured **CSCF v2026 gap assessments** with 🔴/🟡/🟢 status per control, evidence requirements, and prioritised remediation roadmaps
- Provides **deep-dive implementation guidance** for all 25 mandatory controls — including **Control 2.4** (Back-Office Data Flow Security, newly mandatory in v2026) with implementation steps and audit evidence
- Guides the complete **KYC-SA attestation process** — evidence preparation per control, independent assessor qualification criteria, portal submission steps, and post-submission counterparty visibility
- Advises on the **CSCF v2025 → v2026 changes**: Control 2.4 promoted from advisory to mandatory; attestation window July 1 – December 31, 2026
- Provides **SWIFT-specific incident response** guidance — 24-hour initial notification to security@swift.com, 30-day full report, evidence preservation, and IRP content requirements for Control 7.1
- Explains **Type B (service bureau) responsibilities** — the split between bureau and customer obligations, and how to verify your bureau's KYC-SA attestation
- **Maps CSCF controls to ISO 27001:2022, PCI DSS v4.0.1, and NIST CSF 2.0** — identifying both synergies and SWIFT-specific additions not covered by existing certifications

**Trigger phrases:** `SWIFT CSP`, `CSCF`, `KYC-SA`, `SWIFT security attestation`, `Alliance Access`, `SWIFT operator MFA`, `SWIFT secure zone`, `SWIFT secure flow zone`, `CSCF v2026`, `Control 2.4 SWIFT`, `Control 4.2 SWIFT`, `Control 6.4 SWIFT`, `Control 7.1 SWIFT`, `SWIFT architecture type A1`, `SWIFT service bureau`, `Type B SWIFT`, `SWIFT incident response`, `SWIFT gap assessment`, `SWIFT mandatory controls`, `SWIFT hardware token`, `SWIFT log retention`

---

<a id="-australian-information-security-manual-ism"></a>

### 16. 🇦🇺 ISM [Australia] — Australian Information Security Manual

**File:** `ISM - Claude Skill/ism.skill`

The ISM skill turns Claude into an expert advisor on the **Australian Information Security Manual** — the whole-of-government cybersecurity framework published by the Australian Signals Directorate (ASD) for Australian federal and state government entities and their supply chains. It covers all 22 guideline chapters, the six-step risk management cycle, control applicability markings (OFFICIAL through TOP SECRET), the IRAP assessment programme, system authorisation, and the Essential Eight relationship. Current as of the **June 2026 ISM release** — including the restructured 49 cybersecurity principles (GOVERN doubled to 14), the first-of-kind **AI application controls (ISM-2112/2113/2114)**, and the expanded ASD-approved cryptography requirements for data in transit.

**What it does:**
- Applies the ISM's **control applicability marking system** — determines which NC/OS/PROTECTED/SECRET/TOP SECRET controls apply to a system and explains the stacking rule (higher classifications cumulate all lower-level controls)
- Guides the complete **system authorisation pathway** — defining system boundary, selecting and implementing controls, IRAP assessment, ATO sign-off by the Authorising Official, and ongoing monitoring
- Prepares agencies for **IRAP assessments** — artefact checklists (SSP, network diagrams, asset register, risk register, policy suite, control evidence), what to expect during assessment, and the post-assessment POA&M → ATO pathway
- Provides deep-dive guidance across all **22 ISM guideline chapters**: system hardening (Ch. 13), patch management SLAs (Ch. 14), logging/monitoring requirements (Ch. 15), cryptographic standards (Ch. 20), email security (Ch. 18), networking (Ch. 19), and more
- Explains the **Essential Eight** as a prioritised ISM subset — maps each of the 8 strategies to their ISM chapters, explains ML0–ML3 maturity levels, and distinguishes between Essential Eight compliance and full ISM compliance
- Advises **private sector suppliers and cloud service providers** on their ISM obligations under government contracts and when IRAP assessments are required even for non-government entities
- Covers **approved cryptographic standards** (AES-256 for PROTECTED+, TLS 1.2 minimum, SHA-256 minimum, prohibited algorithms) and log retention requirements (18 months minimum for OS/PROTECTED systems)
- Supports **SSP drafting** — the System Security Plan structure, required sections, classification, security objectives, and how it feeds the ATO decision

**Trigger phrases:** `ISM`, `Information Security Manual`, `ASD cybersecurity`, `IRAP assessment`, `IRAP assessor`, `system authorisation`, `ATO Australia`, `PROTECTED system`, `OFFICIAL Sensitive`, `NC OS PROTECTED`, `Essential Eight`, `ASD compliance`, `Australian government cybersecurity`, `ISM controls`, `ISM gap analysis`, `ISM chapter`, `ISM hardening`, `ISM OSCAL`, `cyber.gov.au`, `ASD IRAP`

---

<a id="-eu-nis2-directive"></a>

### 17. 🇪🇺 NIS2 [EU] Directive

**File:** `NIS2 - Claude Skill/nis2.skill`

The NIS2 skill turns Claude into an expert advisor on the **EU NIS2 Directive (Directive (EU) 2022/2555)** — the European Union's overarching cybersecurity framework for essential and important entities. In force since 27 December 2022 (transposition deadline 17 October 2024), NIS2 replaces the original NIS1 Directive and significantly expands scope, strengthens incident reporting obligations, introduces management body accountability, and raises maximum penalties to €10M or 2% of global turnover.

**What it does:**
- Determines **entity classification** — Essential Entity (Annex I: 11 highly critical sectors) or Important Entity (Annex II: 7 other critical sectors) — and applies size-threshold analysis to confirm scope
- Guides compliance with all **10 Art. 21 cybersecurity risk management measures**: risk analysis policies, incident handling, BCP/DR/crisis management, supply chain security, secure SDLC and vulnerability management, effectiveness assessment, cyber hygiene training, cryptography, HR security and access control, and MFA/secure communications
- Walks through the **Art. 23 incident reporting workflow**: 24-hour early warning, 72-hour incident notification, and 1-month final report — with content requirements for each stage and guidance on significant incident thresholds
- Explains **Art. 20 governance obligations** — management body approval, mandatory cybersecurity training, and personal liability under Member State transposition law
- Performs **ISO 27001 gap analysis** — maps ISO 27001:2022 Annex A controls to NIS2 Art. 21 measures and identifies gaps where ISO 27001 certification is necessary but not sufficient (Art. 20, Art. 23 timelines, MFA mandate, ENISA supply chain assessments)
- Advises on **EE vs IE supervision differences** — Essential Entities face proactive Art. 32 oversight (on-site inspections, security audits); Important Entities face reactive Art. 33 oversight
- Addresses the **DORA lex specialis interaction** — explains DORA precedence for financial entities under Art. 4, identifies residual NIS2 obligations, and recommends an integrated compliance programme
- Calculates **penalty exposure** (EE: up to €10M or 2% global turnover; IE: up to €7M or 1.4%) and advises on remediation prioritisation to reduce regulatory risk

**Trigger phrases:** `NIS2`, `NIS 2`, `Directive EU 2022 2555`, `essential entity`, `important entity`, `NIS2 compliance`, `NIS2 incident reporting`, `Article 21 NIS2`, `Article 23 NIS2`, `NIS2 gap analysis`, `NIS2 policy`, `NIS2 supply chain`, `NIS2 governance`, `NIS2 risk management`, `ENISA NIS2`, `NIS2 penalties`, `NIS2 transposition`, `NIS2 and DORA`, `NIS2 and ISO 27001`, `network information security directive`

---

<a id="-ccpacpra-california-privacy"></a>

### 18. <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_California.svg" alt="CA" height="16" style="vertical-align:middle;"> CCPA/CPRA [California] Privacy

**File:** `CCPA - Claude Skill/ccpa.skill`

The CCPA/CPRA skill turns Claude into an expert advisor on **California's comprehensive privacy laws** — the California Consumer Privacy Act (CCPA, effective January 1, 2020) and the California Privacy Rights Act (CPRA/Proposition 24, effective January 1, 2023). CPRA significantly expanded CCPA, created the California Privacy Protection Agency (CPPA), introduced Sensitive Personal Information (SPI) as a new category, and added rights to correct PI, limit SPI use, and set retention periods.

**What it does:**
- Determines **business applicability** — whether an organisation meets the CCPA/CPRA threshold ($25M revenue OR 100K+ consumers/households OR 50%+ revenue from PI sale/sharing) and what obligations follow
- Guides **consumer rights fulfillment** — step-by-step workflows for right to know (access), delete, correct, opt-out of sale/sharing, limit SPI use, portability, and non-discrimination — including identity verification, exceptions, response deadlines (45 days / 15 business days for SPI), and service provider propagation
- Classifies **ad tech, cookie tracking, and data sharing** — determines whether arrangements constitute a "sale" or CPRA "sharing" (cross-context behavioral advertising), advises on Global Privacy Control (GPC) signal compliance and consent management
- Identifies **Sensitive Personal Information (SPI)** — precise geolocation, biometrics, health data, SSNs, credentials, and more — and advises on permitted uses, limitation rights, disclosure requirements, and 15-business-day response SLA
- Performs **GDPR-to-CCPA/CPRA gap analysis** — identifies CCPA/CPRA-specific additions (Do Not Sell or Share link, GPC, SPI limitation, minors' opt-in, financial incentive disclosures) and highlights key structural differences (opt-out vs. opt-in, no lawful basis requirement, household data, private right of action for breaches)
- Drafts **privacy notices and policies** — at-collection notices, comprehensive privacy policies with all required CCPA/CPRA disclosures, and "Do Not Sell or Share" and "Limit SPI" opt-out pages
- Assesses **CPPA enforcement and penalty exposure** — $2,500/unintentional, $7,500/intentional, $100–$750/consumer for breach private actions

**Trigger phrases:** `CCPA`, `CPRA`, `California Consumer Privacy Act`, `California Privacy Rights Act`, `Do Not Sell or Share`, `sensitive personal information California`, `CPPA`, `California privacy compliance`, `right to know California`, `right to delete California`, `California opt-out`, `GPC signal`, `Global Privacy Control`, `ad tech CCPA`, `CCPA gap analysis`, `CCPA vs GDPR`, `California data privacy`, `CCPA service provider`, `CCPA third party`, `CCPA penalty`

---

<a id="-itar--international-traffic-in-arms-regulations"></a>

### 19. <img src="assets/Logos/itar.jpg" alt="ITAR" height="20" style="vertical-align:middle;object-fit:contain;"> ITAR [US] — International Traffic in Arms Regulations

**File:** `ITAR - Claude Skill/itar.skill`

The ITAR skill turns Claude into an expert advisor on **US defense export controls under 22 CFR Parts 120–130**, administered by the Directorate of Defense Trade Controls (DDTC) at the US State Department. ITAR controls the export, re-export, and transfer of defense articles, defense services, and related technical data enumerated on the United States Munitions List (USML).

**What it does:**
- Performs **USML jurisdiction analysis** — applies the enumeration test and specially designed test (22 CFR § 120.41) to determine whether an item falls under ITAR or EAR, and guides Commodity Jurisdiction (CJ) requests for ambiguous cases
- Guides **DDTC registration** under 22 CFR Part 122 — who must register, DS-2032 submission, annual fees, renewal timelines, and Empowered Official (EO) designation
- Advises on **export licensing** — DSP-5 (permanent export), DSP-73 (temporary export), DSP-94 (temporary import), application requirements via D-Trade, licence conditions, Congressional notification thresholds
- Drafts and reviews **Technical Assistance Agreements (TAA)** and **Manufacturing License Agreements (MLA)** under 22 CFR Part 124, including all mandatory clauses: retransfer prohibition, US government rights, audit rights, and 5-year record retention
- Advises on **deemed exports** — foreign national access to ITAR-controlled technical data inside the US is treated as an export to their home country; covers Technology Control Plans (TCP), screening requirements, and access segregation
- Guides **brokering compliance** under 22 CFR Part 129 — registration, prior approval requirements, and annual reporting obligations
- Manages **violations and voluntary disclosures** — walks through the VSD process under 22 CFR § 127.12, penalty exposure (civil up to $1.369M/violation, criminal up to $1M/20 years), mitigating and aggravating factors, and corrective action planning

**Trigger phrases:** `ITAR`, `International Traffic in Arms Regulations`, `USML`, `United States Munitions List`, `DDTC`, `defense export`, `deemed export`, `TAA`, `technical assistance agreement`, `MLA`, `manufacturing license agreement`, `DSP-5`, `DSP-73`, `ITAR registration`, `ITAR violation`, `voluntary disclosure ITAR`, `ITAR vs EAR`, `commodity jurisdiction`, `defense article`, `defense service`, `ITAR compliance`, `technology control plan`, `Empowered Official`

---

<a id="-lgpd--brazils-general-data-protection-law"></a>

### 20. <img src="assets/Logos/lgpd-brazil.svg" alt="Brazil" height="20" style="vertical-align:middle;object-fit:contain;"> LGPD [Brazil] — General Data Protection Law

**File:** `LGPD - Claude Skill/lgpd.skill`

The LGPD skill turns Claude into an expert advisor on **Brazil's Lei Geral de Proteção de Dados Pessoais (Law 13,709/2018)**, the comprehensive Brazilian data protection law enforced by the **ANPD (Autoridade Nacional de Proteção de Dados)**. LGPD applies extraterritorially to any organisation processing personal data of individuals located in Brazil.

- Analyses **extraterritorial scope** (Art. 3) — determines whether LGPD applies to your organisation regardless of country of establishment
- Maps **legal bases for processing** (Art. 7 — 10 bases for regular data; Art. 11 — stricter bases for sensitive data including health, biometric, racial origin)
- Drafts **LGPD-compliant privacy notices** (Art. 9) and **consent mechanisms** (Art. 8) covering all mandatory elements
- Guides **data subject rights fulfilment** (Arts. 17–22) — access, correction, deletion, portability, consent revocation, automated decision review — with 15-day response workflows
- Advises on **DPO/Encarregado appointment** (Art. 41) — mandatory publication requirements and ANPD Resolution No. 2/2022 SME exemptions
- Produces **DPIA/RIPD templates** (Art. 38) for high-risk processing and **RoPA (Records of Processing Activities)** structures (Art. 37)
- Guides **ANPD breach notification** (Art. 48 + ANPD Resolution No. 15/2024) — 3 working-day preliminary notification and 20 working-day full report requirements
- Analyses **international transfer mechanisms** (Arts. 33–36) for countries without ANPD adequacy decisions (including the US)
- Calculates **penalty exposure** (Art. 52) — fines up to 2% of Brazilian revenue, maximum R$50 million per violation
- Provides **LGPD vs. GDPR comparison** — key differences in legal bases, DPO obligations, breach timelines, and fine structures

**Trigger phrases:** `LGPD`, `Brazil data protection`, `Lei Geral de Proteção de Dados`, `ANPD`, `Brazilian privacy law`, `LGPD compliance`, `LGPD gap assessment`, `Encarregado`, `RIPD`, `LGPD legal basis`, `LGPD data subject rights`, `Brazil data breach`, `ANPD notification`, `LGPD vs GDPR`, `Brazil personal data`, `LGPD penalty`, `Brazil privacy policy`

---

<a id="-csrd--eu-corporate-sustainability-reporting-directive"></a>

### 21. <img src="assets/Logos/csrd-eu.svg" alt="EU" height="20" style="vertical-align:middle;object-fit:contain;"> CSRD [EU] — Corporate Sustainability Reporting Directive

**File:** `CSRD - Claude Skill/csrd.skill`

The CSRD skill turns Claude into an expert advisor on **EU Directive 2022/2464 (CSRD)**, which requires approximately 50,000 companies to disclose detailed environmental, social, and governance (ESG) information under the **European Sustainability Reporting Standards (ESRS)**. CSRD came into force on 5 January 2023 and replaces the Non-Financial Reporting Directive (NFRD).

- Determines **CSRD scope under the 2026 Omnibus** — applies the Directive (EU) 2026/470 test (mandatory reporting only for companies with **>1,000 employees AND >€450M turnover**), explains the stop-the-clock deferrals, flags the pending non-EU threshold revision, and routes below-threshold companies to the VSME voluntary standard
- Advises the **revised ESRS (July 3, 2026 delegated acts)** — ~61% fewer mandatory datapoints, applying FY2027 with FY2026 early adoption once the scrutiny period completes — including the "current vs revised ESRS basis" decision every gap assessment now starts with
- Guides the **Double Materiality Assessment (DMA)** — ESRS 1 step-by-step process covering impact materiality (scale, scope, irremediability) and financial materiality (risks and opportunities), with scoring templates
- Produces **CSRD gap assessments** — maps current GRI/TCFD/CDP/SASB disclosures to mandatory ESRS datapoints and identifies priority gaps
- Drafts **ESRS disclosures** — ESRS 2 General Disclosures (GOV-1 to GOV-5, SBM-1 to SBM-3, IRO-1) and all topical standards (E1–E5, S1–S4, G1) for material topics
- Advises on **ESRS E1 Climate Change** — Scope 1, 2, and all 15 Scope 3 GHG emission categories, transition plan (Art. 19a(2)(a)), EU Taxonomy alignment, physical and transition risk financial effects
- Supports **ESRS S1 Own Workforce** disclosures — gender pay gap, CEO pay ratio, LTIFR, collective bargaining coverage, health & safety management systems
- Designs **Scope 3 GHG emissions programmes** — category prioritisation matrix, data collection methods (CDP Supply Chain, spend-based, supplier surveys), proxy methodology disclosure
- Plans **assurance readiness** — limited assurance requirements under Art. 26a, documentation standards, transition to reasonable assurance post-2028
- Advises on **XBRL/iXBRL digital tagging** requirements under ESEF and management report placement obligations
- Provides **CSRD vs GRI/TCFD/SASB/CDP comparison** — framework interoperability, Appendix C mapping, and gap identification for existing reporters

**Trigger phrases:** `CSRD`, `Corporate Sustainability Reporting Directive`, `ESRS`, `double materiality`, `double materiality assessment`, `DMA`, `ESG reporting Europe`, `sustainability disclosure EU`, `non-financial reporting`, `ESRS E1`, `ESRS S1`, `ESRS G1`, `Scope 3 CSRD`, `transition plan ESRS`, `CSRD gap assessment`, `CSRD scope`, `EU sustainability reporting`, `ESRS assurance`, `XBRL sustainability`, `CSRD vs GRI`, `CSRD vs TCFD`, `EU Taxonomy CSRD`, `NFRD CSRD`, `ESRS materiality`

---

<a id="-cis-controls-v8--cis-top-18-cyber-hygiene"></a>

### 22. 🛡️ CIS Controls v8 — CIS Top 18 Cyber Hygiene

**File:** `CIS Controls - Claude Skill/cis-controls.skill`

The CIS Controls v8 skill turns Claude into an expert CIS Controls advisor covering all **18 CIS Controls and 153 safeguards** from the May 2021 v8 release, including explicit cloud and mobile coverage. It applies the **Implementation Group (IG) framework** — IG1 (56 safeguards, essential cyber hygiene), IG2 (130 safeguards, intermediate), and IG3 (153 safeguards, advanced) — to scope guidance to each organization's risk profile and resource level.

**What it does:**
- Determines the correct **Implementation Group** for any organization based on IT resources, data sensitivity, regulatory exposure, and threat profile — then scopes all guidance to that IG
- Conducts structured **CIS Controls gap assessments** across all 18 controls and applicable safeguards with 🔴/🟡/🟢 status, IG assignment, asset type, security function, and prioritised remediation roadmap
- Provides **safeguard-level implementation guidance** for all 153 safeguards — practical steps, recommended tools (e.g., Qualys, CrowdStrike, Splunk, Microsoft Defender), and common pitfalls
- Delivers a structured **IG1 12-week quick-start programme** — week-by-week asset inventory, secure configuration, access controls, patch management, backups, and training
- **Maps CIS Controls v8 to NIST CSF 2.0** (subcategory-level), **ISO 27001:2022 Annex A**, **CMMC 2.0 / NIST SP 800-171**, **SOC 2 TSC**, and **PCI DSS v4.0**
- Advises on **vulnerability management SLAs** — CVSS-based remediation timelines (Critical: 15 days, High: 30 days, Medium: 90 days) and authenticated scanner deployment
- Designs **SIEM/log management programmes** per Control 8 — what to collect, retention standards (90-day hot, 12-month minimum), and NTP synchronisation
- Provides **industry-specific guidance** — healthcare (HIPAA alignment), finance (PCI DSS alignment), government (CMMC alignment), and education (FERPA alignment)

**Trigger phrases:** `CIS Controls`, `CIS Top 18`, `CIS v8`, `CIS Controls v8`, `Implementation Group`, `IG1`, `IG2`, `IG3`, `CIS safeguards`, `cyber hygiene controls`, `CIS gap assessment`, `CIS Controls NIST mapping`, `CIS Benchmarks`, `CIS CSAT`, `asset inventory CIS`, `vulnerability management CIS`, `CIS Controls ISO 27001`, `CIS Controls SOC 2`, `CIS Controls PCI DSS`, `CIS Controls CMMC`, `CIS Controls NIST CSF`

---

<a id="-ear--export-administration-regulations"></a>

### 23. 📦 EAR — Export Administration Regulations

**File:** `EAR - Claude Skill/ear.skill`

The EAR skill turns Claude into an expert Export Administration Regulations advisor with deep knowledge of all 15 CFR Parts 730–774, administered by the Bureau of Industry and Security (BIS). It guides exporters, manufacturers, technology companies, and compliance professionals through the full dual-use export control lifecycle — from item classification to licence analysis to enforcement response.

**What it does:**
- Applies the mandatory **Order of Review** to determine EAR vs. ITAR jurisdiction — USML check first, then CCL classification or EAR99 confirmation
- Classifies items across all **10 CCL categories** (0–9) and **5 product groups** (A–E) with step-by-step ECCN determination, including when to seek a CCATS or CJ request
- Analyses **licence requirements** using the Commerce Country Chart — RFC × country matrix — and identifies applicable **licence exceptions** (LVS, GBS, CIV, APP, TSR, TMP, RPL, GOV, TSU, ENC, BAG, AVS, ACE, GFT)
- Screens transactions against all **restricted party lists**: Entity List, Denied Persons List, Unverified List, MEU List, and OFAC SDN — with guidance on the Consolidated Screening List (CSL)
- Explains **deemed export rules** (§ 734.13), the **most restrictive nationality rule** for dual nationals, and access control obligations for foreign national employees
- Covers the **Foreign Direct Product Rule (FDPR)** — General FDPR, Entity List FDPR (Huawei 2020), Advanced Computing FDPR (2022/2023), and Russia/Belarus FDPR (2022)
- Guides through **Voluntary Self-Disclosure (VSD)** under § 764.5 — initial notification, 180-day full submission, OEE process, and penalty mitigation calculus
- Designs a **7-element BIS Export Compliance Programme (ECP)** and assesses maturity (Basic/Developing/Proficient/Advanced) against BIS penalty mitigation standards

**Trigger phrases:** `EAR`, `Export Administration Regulations`, `ECCN`, `EAR99`, `BIS`, `export control`, `Commerce Control List`, `CCL`, `dual-use export`, `export licence`, `Entity List`, `Denied Persons List`, `deemed export`, `FDPR`, `Foreign Direct Product Rule`, `licence exception`, `ENC exception`, `voluntary self-disclosure`, `VSD`, `SNAP-R`, `export compliance programme`, `ECP`, `restricted party screening`, `export to China`, `export to Russia`, `de minimis rule`, `CCATS`, `EAR vs ITAR`

---

<a id="-nist-sp-800-53--security-and-privacy-controls-for-federal-systems"></a>

### 24. 🏛️ NIST SP 800-53 — Security and Privacy Controls for Federal Systems

**File:** `NIST 800-53 - Claude Skill/nist-800-53.skill`

The NIST SP 800-53 skill turns Claude into an expert federal security and privacy controls advisor covering the full **SP 800-53 Rev 5** catalog (September 2020) and its companion publications — SP 800-53B baselines, SP 800-53A assessment procedures, and SP 800-37 Rev 2 Risk Management Framework. It serves federal agency teams, cloud service providers pursuing FedRAMP, system owners, ISSOs, and GRC professionals implementing FISMA-mandated controls.

**What it does:**
- **Categorises systems** using FIPS 199/200 and SP 800-60 — determines C/I/A impact levels, applies the high-water mark rule, and selects the appropriate Low, Moderate, or High baseline from SP 800-53B
- **Covers all 20 control families** (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR) with key controls, baseline assignments, and implementation notes — including the new **PT (Privacy)** and **SR (Supply Chain)** families added in Rev 5
- **Guides tailoring** — identifies common/inherited controls, applies scoping considerations, fills in Organization-Defined Values (ODVs) with federal guidance, designs compensating controls, and supplements the baseline for elevated risks
- **Writes SSP control narratives** in the standard format — each covering implementation description, responsible role, inherited/hybrid designation, and testing method for SP 800-53A assessment
- **Manages POA&Ms** (CA-5) — documents OTS findings from assessments, assigns FedRAMP-aligned remediation timelines (Critical: 30 days; High: 90 days; Moderate: 180 days; Low: 1 year), and tracks risk acceptance decisions
- **Guides all 7 RMF steps** (SP 800-37 Rev 2): Prepare → Categorize → Select → Implement → Assess → Authorize → Monitor, including ATO package assembly (SSP + SAR + POA&M) and continuous monitoring (ConMon) strategy
- **Maps SP 800-53 to peer frameworks** — ISO 27001:2022, NIST CSF 2.0, CMMC 2.0, and FedRAMP — for cross-framework compliance programmes
- **Addresses EO 14028 and OMB M-22-09** phishing-resistant MFA obligations under IA-2(1) and IA-2(2), and FIPS 140-2/3 cryptographic module requirements under SC-13

**Trigger phrases:** `NIST SP 800-53`, `SP 800-53`, `NIST 800-53`, `federal security controls`, `RMF`, `Risk Management Framework`, `FISMA`, `ATO`, `Authority to Operate`, `FIPS 199`, `FIPS 200`, `FIPS 140`, `SP 800-53B`, `control baseline`, `Low baseline`, `Moderate baseline`, `High baseline`, `SSP narrative`, `System Security Plan`, `POA&M`, `Plan of Action`, `ConMon`, `continuous monitoring`, `SP 800-53A`, `security assessment`, `ODV`, `organization-defined value`, `control tailoring`, `common controls`, `inherited controls`, `AC-2`, `IA-2`, `SC-8`, `SI-2`, `SR family`, `PT family`, `supply chain risk`, `OSCAL`, `3PAO`, `FedRAMP controls`, `ISSO`, `system owner`, `authorizing official`

---

<a id="-eu-ai-act--regulation-eu-20241689"></a>

### 25. 🤖 EU AI Act — Regulation (EU) 2024/1689

**File:** `EU AI Act - Claude Skill/eu-ai-act.skill`

The EU AI Act skill turns Claude into an expert EU AI Act compliance advisor covering the full **Regulation (EU) 2024/1689** — the world's first comprehensive horizontal AI regulation, in force from 1 August 2024 and amended by the Digital Omnibus (Regulation (EU) 2026/1744, in force July 27, 2026). GPAI enforcement powers have been active since August 2, 2026. It serves AI providers, deployers, importers, and authorised representatives operating in or placing AI on the EU market.

**What it does:**
- **Classifies AI systems** across all four risk tiers — Prohibited (Art. 5), High-Risk (Art. 6 + Annex I/III), Limited Risk (Art. 50), and Minimal/No Risk — using both the Annex I safety component path (Art. 6(1)) and the Annex III listed use case path (Art. 6(2))
- **Screens for all **9 prohibited practices** (Art. 5): the original 8 apply from 2 February 2025 — subliminal manipulation, vulnerability exploitation, social scoring, predictive criminal assessment, untargeted biometric scraping, workplace/education emotion inference, sensitive-attribute biometric categorisation, and real-time RBI in public spaces by law enforcement — plus the 9th added by the Digital Omnibus (non-consensual intimate imagery / CSAM generation), applying from 2 December 2026
- **Walks through all 8 Annex III high-risk use case areas**: biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration/border control, and justice/democracy
- **Covers provider obligations (Arts. 9–17)**: risk management (5-step process), data governance, Annex IV technical documentation, automatic logging, transparency to deployers, human oversight design, accuracy/robustness/cybersecurity, 12-item provider checklist, and 13-component QMS
- **Covers deployer obligations (Art. 26)**: instructions compliance, staff competence, monitoring, 6-month log retention, worker notification, public authority registration, and GDPR DPIA
- **Guides Fundamental Rights Impact Assessments (FRIA, Art. 27)**: who must perform one (public-law bodies, public-service providers, and deployers of credit-scoring and life/health-insurance systems under Annex III 5(b)-(c)), the six required content elements, market-surveillance notification, and how a FRIA builds on a GDPR DPIA
- **Guides conformity assessment and CE marking**: Annex VI self-assessment (Areas 2–8) vs. Annex VII notified body (Area 1 biometrics), EU Declaration of Conformity (Art. 47, 10-year retention), CE marking (Art. 48), EU AI database registration (Arts. 49/60)
- **Covers GPAI model obligations (Arts. 53–55, from 2 August 2025)**: universal obligations, open-source exception, systemic risk threshold (10²⁵ FLOPs, Art. 51), and systemic risk additional obligations including adversarial testing and AI Office reporting
- **Maps to peer frameworks**: ISO 42001:2023, NIST AI RMF 1.0, and GDPR — showing where obligations overlap and where dual compliance is required
- **References penalty exposure (Art. 99)**: €35M/7% for prohibited practices, €15M/3% for provider/deployer violations, €7.5M/1% for misleading authorities

**Trigger phrases:** `EU AI Act`, `AI Act`, `Regulation 2024/1689`, `high-risk AI`, `prohibited AI`, `GPAI model`, `general-purpose AI`, `AI system classification`, `AI conformity assessment`, `CE marking AI`, `EU AI database`, `AI Office`, `AI Board`, `systemic risk AI`, `Art. 5 AI`, `Annex III AI`, `AI provider obligations`, `AI deployer obligations`, `human oversight AI`, `AI risk management`, `Art. 50 transparency`, `chatbot disclosure AI`, `AI Act compliance`, `GPAI obligations`, `open-source AI Act`, `AI Act penalty`, `AI Act timeline`, `AI Act GDPR`

---

<a id="-section-508--us-federal-ict-accessibility"></a>

### 26. ♿ Section 508 — US Federal ICT Accessibility

**File:** `Section 508 - Claude Skill/section-508.skill`

The Section 508 skill turns Claude into an expert **US federal ICT accessibility compliance advisor** covering the **Revised Section 508 Standards (2018)** (36 CFR Part 1194), which incorporate **WCAG 2.0 Level A and AA** as the technical standard for web content, software, and electronic documents. It supports federal agencies, contractors, and ICT vendors across the full compliance lifecycle — from accessibility audits and VPAT completion to PDF remediation, procurement RFP language, and undue burden determinations.

**What this skill covers:**
- **VPAT/ACR completion** — VPAT 2.x WCAG Edition structure, all four conformance levels (Supports/Partially Supports/Does Not Support/Not Applicable), three tables (Level A, Level AA, Functional Performance Criteria), required testing methodology disclosure
- **WCAG 2.0 Level A and AA success criteria** — all 38 criteria across the four POUR principles (Perceivable, Operable, Understandable, Robust) with common failure patterns and fixes
- **Accessibility auditing** — automated scanning (axe, WAVE, Lighthouse), keyboard-only testing, screen reader testing (JAWS + Chrome, NVDA + Firefox, VoiceOver + Safari), colour contrast verification
- **PDF accessibility** — Tagged PDFs, tag hierarchy, form field accessible names, Alt text, reading order, document language, Acrobat Pro Full Accessibility Check
- **Federal procurement** — FAR clause 52.239-2, RFP accessibility requirements, VPAT evaluation methodology, common vendor VPAT deficiencies, post-award remediation SLAs
- **Exceptions** — Undue burden (E202.5): written determination process, alternative means of access obligations, re-evaluation triggers; fundamental alteration; legacy ICT

**Trigger phrases:** `Section 508`, `508 compliance`, `WCAG federal`, `VPAT`, `ACR accessibility`, `accessibility conformance report`, `ICT accessibility`, `federal accessibility`, `POUR principles`, `web accessibility 508`, `keyboard accessibility audit`, `screen reader testing`, `PDF accessibility`, `accessible federal website`, `undue burden 508`, `assistive technology testing`, `FAR 52.239-2`, `508 procurement`, `JAWS testing`, `VoiceOver compliance`, `axe accessibility`, `colour contrast 508`, `focus visible 508`, `alt text federal`

<a id="-wcag--web-content-accessibility-guidelines"></a>

### 27. ♿ WCAG — Web Content Accessibility Guidelines

**File:** `WCAG - Claude Skill/wcag.skill`

The WCAG skill turns Claude into an expert advisor on **WCAG 2.0, 2.1, and 2.2** — the W3C international standard for digital accessibility developed by the Web Accessibility Initiative (WAI). WCAG underpins accessibility laws worldwide: the EU EAA (EN 301 549), US Section 508 and ADA, UK Equality Act, and Australia's DDA all reference WCAG conformance. Supports developers, designers, product teams, and legal/compliance teams working on web, mobile, and digital content accessibility.

**Key capabilities:**
- **POUR principles and all success criteria** — comprehensive coverage of WCAG 2.2 including all 9 new criteria (SC 2.4.11–13, 2.5.7–8, 3.2.6, 3.3.7–8) and all 17 criteria added in 2.1 for mobile, low vision, and cognitive accessibility; conformance levels A/AA/AAA; WCAG 3.0 preview
- **Accessibility audits** — colour contrast analysis (SC 1.4.3 and 1.4.11), ARIA patterns and screen reader testing (NVDA+Chrome, JAWS+Chrome, VoiceOver+Safari), keyboard navigation (ARIA APG patterns), focus management (SC 2.4.3, 2.4.7, 2.4.11), live region announcements (SC 4.1.3), reflow testing (SC 1.4.10)
- **Code review** — annotated violations with SC numbers, ARIA corrections, corrected code examples; React/HTML/ARIA pattern guidance aligned with ARIA Authoring Practices Guide
- **Accessibility statements** — full publication-ready statements with conformance status, known issues, SC citations, contact/feedback mechanism, formal complaints procedure per EU Web Accessibility Directive (Decision 2018/1523)
- **Legal framework mapping** — maps WCAG to EN 301 549, EU EAA (June 2025), EU Web Accessibility Directive, US Section 508, ADA Title III, UK PSBAR 2018, UK Equality Act, AODA, and Australia DDA with jurisdiction-specific version requirements

**Trigger phrases:** `WCAG`, `WCAG 2.1`, `WCAG 2.2`, `web accessibility`, `POUR principles`, `accessibility audit`, `colour contrast`, `screen reader`, `keyboard accessibility`, `ARIA`, `focus visible`, `reflow`, `accessibility statement`, `EN 301 549`, `European Accessibility Act`, `WCAG conformance`, `success criteria`, `alt text`, `captions accessibility`, `SC 1.4.3`, `SC 4.1.2`, `NVDA`, `VoiceOver`, `JAWS screen reader`, `WCAG 2.2 upgrade`

<a id="-nzism--new-zealand-information-security-manual"></a>

### 28. 🇳🇿 NZISM — New Zealand Information Security Manual

**File:** `NZISM - Claude Skill/nzism.skill`

The NZISM skill turns Claude into an expert advisor on the **New Zealand Information Security Manual (NZISM)** — the mandatory cybersecurity framework published by the **Government Communications Security Bureau (GCSB)** / **National Cyber Security Centre (NCSC NZ)** for NZ government agencies and their supply chains. It covers the NZ Government Information Classification System (ISCS) from Unclassified through Top Secret, all 18+ NZISM control sections, the Certification & Accreditation (C&A) process, and mandatory agency obligations.

**Key capabilities:**
- **Gap analysis** — structured control-by-control gap assessment across all NZISM security domains, with status (Implemented / Partial / Not Implemented / N/A), evidence required, and remediation priority for any classification level
- **Certification & Accreditation (C&A)** — step-by-step pathway for Restricted and above: SSP preparation, security risk assessment, independent assessment, POA&M, and Accrediting Authority sign-off
- **Classification framework** — NZ Government ISCS guidance (Unclassified, In-Confidence, Restricted, Confidential, Secret, Top Secret): how to classify systems, aggregation risk, handling requirements (labelling, transmission, storage, disposal)
- **Control implementation guidance** — actionable advice for all 18 NZISM sections: governance, physical, personnel, network, access control, cryptography, audit & logging, cloud computing, enterprise mobility, third-party suppliers, incident management, and more
- **Verified control-ID citations** — cites real NZISM control identifiers (`chapter.section.control.C.nn`, e.g., 16.1.46.C.02, 16.3.5.C.02) from a bundled, source-verified reference — with a strict never-invent-a-CID rule and chapter/section fallback
- **Policy generation** — complete, NZISM-referenced policies (Access Control, Incident Response, Information Security, Acceptable Use, Business Continuity) with document control blocks and classification markings
- **Supply chain security** — contractual obligations for SaaS vendors and outsourced suppliers processing government data, offshore processing approvals, right-to-audit clauses, and incident notification requirements
- **Cloud guidance** — NZ Government Cloud Computing Risk & Resilience Guide alignment, data residency requirements, shared responsibility model documentation

**Trigger phrases:** `NZISM`, `NZ government security`, `GCSB compliance`, `NCSC NZ`, `Restricted system NZ`, `Confidential system NZ`, `NZ information classification`, `agency security policy NZ`, `system certification NZ`, `C&A NZ`, `government cybersecurity New Zealand`, `NZISM gap analysis`, `NZISM controls`, `NZ classification ISCS`, `NZISM policy`

---

<a id="-vietnam-pdpl--law-on-personal-data-protection"></a>

### 29. 🇻🇳 Vietnam PDPL — Law on Personal Data Protection

**File:** `Vietnam PDPL - Claude Skill/vn-pdpl.skill`

The Vietnam PDPL skill turns Claude into an expert advisor on **Vietnam's Law on Personal Data Protection No. 91/2025/QH15** — the country's first comprehensive personal data protection law, effective **1 January 2026** — and its implementing regulation **Decree 356/2025/ND-CP**. Administered by the **Ministry of Public Security**, the law applies to Vietnamese entities and foreign organisations processing personal data of Vietnamese citizens (extraterritorial reach).

**Key capabilities:**
- **Gap analysis** — structured compliance assessment against all VN-PDPL obligations: lawful basis, consent, data subject rights, cross-border transfer, DPIA, security, breach notification, DPO, and SME exemptions
- **Data subject rights fulfilment** — workflows for all 6 rights (informed, consent/withdraw, access/rectify, delete/restrict/object, complaints, protection) with legally required response timeframes from Decree 356
- **Impact assessments** — DPIA template (Article 21, due within 60 days) and cross-border transfer impact assessment dossier (Article 20, due within 60 days of first transfer, update every 6 months)
- **Privacy notices and consent forms** — PDPL-compliant notices covering all required disclosure elements; consent forms using valid formats (written, SMS, email, app form — not pre-ticked boxes)
- **Breach notification** — 72-hour workflow for notifying the Ministry of Public Security; finance sector dual notification to both authority and data subjects
- **Sector-specific guidance** — detailed rules for finance/banking (annual assessments, audit logs), AI/automated processing (opt-out rights, periodic assessment), cloud (encryption at rest/in transit), blockchain (no direct personal data on-chain), and big data (strong auth, continuous monitoring)
- **DPO qualification review** — college degree + 2 years experience in IT/law/cybersecurity/compliance; independence requirements; external DPO option

**Trigger phrases:** `Vietnam data privacy`, `VN-PDPL`, `Law 91/2025`, `Nghị định 356`, `Vietnamese personal data`, `Vietnam PDPL`, `cross-border transfer Vietnam`, `Vietnam breach notification`, `Vietnam data protection`, `Vietnamese data subjects`

---

<a id="-eu-cra--cyber-resilience-act"></a>

### 30. 🇪🇺 EU CRA — Cyber Resilience Act

**File:** `EU CRA - Claude Skill/eu-cra.skill`

The EU CRA skill turns Claude into an expert advisor on **Regulation (EU) 2024/2847 — the EU Cyber Resilience Act**, published 20 November 2024 and fully applicable from **11 December 2027**. This landmark regulation mandates cybersecurity requirements for all **Products with Digital Elements (PDEs)** — connected hardware and software — sold in the EU market, covering manufacturers, importers, and distributors.

**Key capabilities:**
- **Scope and classification** — determines whether a product is in scope and which class applies: Default (self-assessment), Class I (Annex III, 35 categories including password managers, VPNs, identity management, network monitoring), or Class II (Annex IV, 12 categories including hypervisors, HSMs, TPMs, industrial ICS/SCADA)
- **Annex I gap analysis** — assesses all 10 Part I security properties (secure by default, no default passwords, encryption, signed updates, exploit mitigations) and all 9 Part II vulnerability handling obligations (CVD, SBOM, 24/72-hour ENISA reporting, free security updates)
- **Conformity assessment and CE marking** — guides Module A self-assessment vs. mandatory Notified Body routes, technical documentation (Annex VII) preparation, EU Declaration of Conformity, and CE marking placement
- **SBOM programme** — SPDX/CycloneDX format guidance, minimum content requirements, CI/CD integration, VEX documents, maintenance throughout support period
- **Vulnerability and incident reporting** — step-by-step 24-hour early warning and 72-hour full report workflows to ENISA/national CSIRTs; final report at 14 days; user notification
- **Support period and EOL** — minimum 5-year support commitment, end-of-life notification obligations (1-year notice), final cumulative update

**Trigger phrases:** `EU CRA`, `Cyber Resilience Act`, `CRA compliance`, `product with digital elements`, `PDE`, `Annex I requirements`, `CRA conformity assessment`, `CE marking cybersecurity`, `SBOM EU regulation`, `ENISA vulnerability reporting`, `Class I CRA`, `Class II CRA`, `connected product security EU`, `IoT security regulation EU`

---

<a id="-saudi-arabia-grc--country-compliance-advisor"></a>

### 31. 🇸🇦 Saudi Arabia GRC — Country Compliance Advisor

**File:** `Saudi Arabia GRC - Claude Skill/saudi-arabia-grc.skill`

The Saudi Arabia GRC skill turns Claude into a **country-level compliance router and advisor** for the Kingdom. Saudi compliance is fragmented across NCA (cybersecurity), SDAIA (personal data), SAMA (financial sector), and CST (telecom/cloud) — so the skill first establishes organization type, sector, data, and cloud posture, then delivers an applicability matrix before any framework detail.

**What it does:**
- Routes across **NCA ECC-2:2024** (4 domains / 28 subdomains / 108 controls; mandatory for government entities and CNI), **Saudi PDPL** (fully enforced since September 14, 2024 — SDAIA registration, 72-hour breach notification, SCC transfer modules, ~48 first-wave enforcement decisions), **NCA CCC + CST cloud rules** (CSP classes, Level 3–4 and government-data in-Kingdom residency), and **SAMA CSF** (4 domains, minimum maturity level 3)
- Runs per-framework **gap assessments** with evidence columns, **breach response**, and **market-entry roadmaps**
- **Maps Saudi requirements to ISO 27001:2022, NIST CSF 2.0, and SOC 2** for evidence reuse
- Router coverage of DCC, OTCC, TCC, CSCC, and CMA guidelines

**Trigger phrases:** `Saudi Arabia compliance`, `KSA`, `NCA ECC`, `SDAIA`, `Saudi PDPL`, `SAMA CSF`, `CST cloud`, `Saudi data residency`, `expanding to Saudi Arabia`

---

<a id="-uae-grc--country-compliance-advisor"></a>

### 32. 🇦🇪 UAE GRC — Country Compliance Advisor

**File:** `UAE GRC - Claude Skill/uae-grc.skill`

The UAE GRC skill turns Claude into a **jurisdiction-first compliance router**: in the UAE, where an organization sits determines its law. The skill establishes mainland vs DIFC vs ADGM vs other free zones, license type, and data categories before advising.

**What it does:**
- Routes across the **Federal PDPL** (Decree-Law 45/2021 — in force since 2022, executive regulations still pending as of August 2026, with dated-status guidance), **DIFC DP Law No. 5 of 2020 as amended by Amendment Law No. 1 of 2025** (private right of action, transfer adequacy assessments, higher fine tiers), **ADGM DP Regulations 2021** (72-hour breach notification), **CBUAE rules** (consumer-data residency, outsourcing/cloud approvals), and the **ICT Health Law** (health-data localization across all zones, fines AED 500k–700k)
- Applies the routing rules that decide cases: DIFC/ADGM displace the federal PDPL; health data is jurisdiction-proof; DFSA/FSRA vs CBUAE regulator boundaries
- Runs **multi-clock breach response**, **market-entry and zone-selection framing**, and CBUAE cloud approval workflows
- **Maps UAE requirements to ISO 27001:2022, NIST CSF 2.0, and SOC 2**

**Trigger phrases:** `UAE compliance`, `DIFC data protection`, `ADGM data protection`, `UAE PDPL`, `CBUAE outsourcing`, `UAE health data residency`, `Dubai ISR`, `ADHICS`, `expanding to the UAE`

---

<a id="-tisax--trusted-information-security-assessment-exchange"></a>

### 33. <img src="assets/Logos/TISAX.svg" alt="TISAX" height="20" style="vertical-align:middle;object-fit:contain;"> TISAX — Trusted Information Security Assessment Exchange

**File:** `TISAX - Claude Skill/tisax.skill`

The TISAX skill turns Claude into an expert advisor on the **automotive industry's information-security assessment regime**, governed by the ENX Association on behalf of the VDA. TISAX labels are de facto mandatory for suppliers and service providers to VW, BMW, Mercedes-Benz, Audi and other OEMs — an assessment with shareable labels ("assess once, share with many"), not a certification.

**What it does:**
- Covers **VDA ISA 6** (46 IS controls, 22 prototype controls, 4 data-protection controls; must/should tiers) and the **ISA2027 transition** — published July 1, 2026, mandatory for assessments ordered from January 1, 2027 (44/46 IS controls edited; prototype module restructured; new PTS labels; year-based naming)
- Walks the **12 assessment objectives/labels** with the ISA-6 renaming (Confidential / Strictly Confidential + availability split) and the objective → **AL1/AL2/AL3** level mapping
- Explains **maturity scoring** (0–5, target 3, cutback rules), the **ENX portal process** (fees, standard scoping, audit providers), corrective action plans with the **9-month window**, temporary labels, and **3-year validity**
- **Maps to ISO 27001:2022** (~70–80% overlap) with automotive-specific deltas — and re-expresses ISO evidence in maturity terms

**Trigger phrases:** `TISAX`, `VDA ISA`, `ENX`, `TISAX label`, `AL2 assessment`, `AL3 assessment`, `prototype protection`, `automotive supplier security`, `ISA2027`, `TISAX vs ISO 27001`

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
| Running an ISO 27701:2025 gap assessment for a SaaS company acting as both PII controller and processor | ISO 27701 |
| Transitioning from ISO 27701:2019 certification to the 2025 standalone edition | ISO 27701 |
| Drafting a GDPR-aligned Data Processing Agreement (DPA) with all required Article 28 clauses | ISO 27701 |
| Building a Records of Processing Activities (RoPA) covering all processing operations | ISO 27701 |
| Completing a DPIA for a new AI feature that profiles users for targeted advertising | ISO 27701 |
| Implementing a Data Subject Rights handling procedure with response SLAs | ISO 27701 |
| Mapping ISO 27701:2025 controls to GDPR articles for a compliance audit | ISO 27701 |
| Assessing sub-processor management obligations for a cloud-native B2B SaaS | ISO 27701 |
| Integrating a PIMS with an existing ISO 27001:2022 ISMS to avoid duplicating controls | ISO 27701 + ISO 27001 |
| Running a DORA gap analysis for an EU credit institution ahead of a supervisory review | DORA |
| Classifying an ICT incident against Art. 18 criteria and CDR (EU) 2024/1772 thresholds | DORA |
| Building a three-stage incident reporting procedure (4h / 72h / 1 month) per Art. 19 | DORA |
| Reviewing ICT vendor contracts against Art. 30(2) mandatory provisions | DORA |
| Building or validating the Register of Information per CIR (EU) 2024/2956 | DORA |
| Assessing ICT concentration risk for a bank reliant on a single hyperscaler | DORA |
| Scoping a TLPT programme and evaluating whether the Art. 26 threshold applies | DORA |
| Drafting an ICT Third-Party Risk Policy satisfying CDR (EU) 2024/1773 | DORA |
| Advising on the interaction between DORA and NIS2 for a financial entity | DORA |
| Mapping DORA obligations to legacy EBA ICT guidelines and identifying what changed | DORA |
| Running a DPDPA gap analysis for an Indian SaaS company ahead of the May 2027 compliance deadline | DPDPA |
| Identifying which GDPR-compliant processing activities need fresh consent or re-mapping under DPDPA | DPDPA + GDPR |
| Designing a notice compliant with Section 5 and Rule 3, including multi-language obligations | DPDPA |
| Implementing a 72-hour breach notification pipeline per Section 8(6) and Rule 6 | DPDPA |
| Designing a children's data compliance programme with Rule 12 parental verification (DigiLocker, virtual tokens) | DPDPA |
| Assessing whether a digital platform must eliminate targeted advertising and behavioural tracking for under-18 users | DPDPA |
| Advising a global company on its India data transfer obligations — blacklist approach vs. GDPR's whitelist | DPDPA |
| Preparing for potential Significant Data Fiduciary designation — DPO appointment, DPIA, and audit readiness | DPDPA |
| Updating Data Processing Agreements with vendors to satisfy Rule 16 | DPDPA |
| Assessing whether a company relying on legitimate interests for analytics must obtain consent under DPDPA | DPDPA |
| Building a Data Principal rights fulfilment procedure covering access, correction, erasure, and nomination | DPDPA |
| Determining your CMMC level based on contract DFARS clauses and CUI handling | CMMC 2.0 |
| Running a CMMC Level 2 gap assessment across all 110 NIST SP 800-171 practices | CMMC 2.0 |
| Drafting a System Security Plan (SSP) covering all 110 practices with implementation narratives | CMMC 2.0 |
| Calculating your SPRS score and prioritising the highest-impact gap remediations | CMMC 2.0 |
| Preparing for a C3PAO assessment — evidence packages, critical practices, POA&M rules | CMMC 2.0 |
| Scoping CUI within your organisation and designing an enclave to reduce CMMC scope | CMMC 2.0 |
| Managing DFARS 252.204-7012 incident reporting obligations (72-hour DIBNET reporting) | CMMC 2.0 |
| Flowing down CMMC requirements to subcontractors handling CUI | CMMC 2.0 |
| Building an AI organizational profile using NIST AI RMF Current and Target states | NIST AI RMF |
| Running a GOVERN gap assessment for an organization starting its AI risk programme | NIST AI RMF |
| Evaluating a credit scoring model against MEASURE 2.x trustworthiness criteria | NIST AI RMF |
| Building an AI risk register mapped to NIST AI RMF categories for a deployed ML system | NIST AI RMF |
| Mapping NIST AI RMF to the EU AI Act Article 9 risk management system requirement | NIST AI RMF + ISO 42001 |
| Assessing bias and fairness of a hiring AI tool (demographic parity, equalized odds, EEOC 4/5ths rule) | NIST AI RMF |
| Designing a post-deployment AI monitoring programme using MEASURE 3.x and MANAGE 3.x | NIST AI RMF |
| Integrating NIST AI RMF with an existing NIST CSF programme | NIST AI RMF + NIST CSF |
| Determining your SWIFT architecture type (A1/A2/A3/A4/B) and getting the full CSCF v2026 control applicability matrix | SWIFT CSP |
| Running a CSCF v2026 gap assessment for an Alliance Access on-premises deployment (including Control 2.4 now mandatory) | SWIFT CSP |
| Understanding why software OTP (Google Authenticator) fails Control 4.2 and remediating with hardware tokens before July attestation | SWIFT CSP |
| Preparing all evidence and completing the annual KYC-SA attestation via swift.com/myswift | SWIFT CSP |
| Developing a SWIFT-specific incident response plan covering 24-hour SWIFT notification and 30-day report obligations | SWIFT CSP |
| Verifying your service bureau's (Type B) KYC-SA attestation and understanding split control responsibilities | SWIFT CSP |
| Mapping existing ISO 27001 or PCI DSS controls to CSCF requirements to identify SWIFT-specific gaps | SWIFT CSP + ISO 27001 / PCI DSS |
| Remediating common CSCF non-compliance patterns: shared VLAN, stale patches, missing SIEM coverage, token inventory gaps | SWIFT CSP |
| Understanding which ISM control applicability markings (NC/OS/PROTECTED) apply to an Australian government cloud system | ISM |
| Preparing artefacts for an IRAP assessment of a PROTECTED-level system | ISM |
| Hardening a Windows Server 2022 deployment to ISM Chapter 13 requirements with evidence checklist | ISM |
| Mapping Essential Eight Maturity Level 2 requirements to their ISM guideline chapters | ISM |
| Understanding ISM compliance obligations for a private sector cloud provider under a government contract | ISM |
| Drafting a System Security Plan (SSP) for ATO sign-off on an OFFICIAL: Sensitive system | ISM |
| Understanding approved cryptographic algorithms and log retention periods under the ISM | ISM |
| Comparing ISM requirements with ISO 27001 controls to identify government-specific gaps | ISM + ISO 27001 |
| Determining whether a European energy company is an Essential or Important Entity under NIS2 and understanding its obligations | NIS2 |
| Walking through the NIS2 Art. 23 incident reporting workflow (24h/72h/1-month) after a ransomware attack | NIS2 |
| Performing a gap analysis between an existing ISO 27001:2022 ISMS and full NIS2 compliance | NIS2 + ISO 27001 |
| Drafting an NIS2-compliant incident response policy covering all 10 Art. 21 measures and Art. 23 reporting timelines | NIS2 |
| Explaining the DORA lex specialis relationship and identifying residual NIS2 obligations for a European bank | NIS2 + DORA |
| Understanding Art. 20 management body obligations, personal liability, and required cybersecurity training under NIS2 | NIS2 |
| Assessing supply chain security obligations under NIS2 Art. 21(2)(d) and Art. 22 ENISA coordinated risk assessments | NIS2 |
| Calculating maximum NIS2 penalty exposure and comparing EE vs IE supervisory regimes (Art. 32 vs Art. 33) | NIS2 |
| Determining whether a US e-commerce business meets any CCPA/CPRA threshold and understanding its core obligations | CCPA/CPRA |
| Handling a combined right-to-know and right-to-delete request from a California consumer, including identity verification and exceptions | CCPA/CPRA |
| Assessing whether sharing cookie IDs with an ad tech platform constitutes a CCPA 'sale' or CPRA 'sharing', and implementing opt-out mechanisms | CCPA/CPRA |
| Performing a gap analysis between an existing GDPR programme and CCPA/CPRA — identifying California-specific additions | CCPA/CPRA + GDPR |
| Classifying precise geolocation, health, and biometric data as CPRA Sensitive Personal Information and understanding the 15-business-day SPI limitation workflow | CCPA/CPRA |
| Drafting an at-collection privacy notice and a comprehensive privacy policy meeting all CCPA/CPRA disclosure requirements | CCPA/CPRA |
| Implementing Global Privacy Control (GPC) signal recognition as a valid opt-out from sale/sharing | CCPA/CPRA |
| Assessing CPPA enforcement risk and calculating penalty exposure for unintentional vs. intentional CCPA/CPRA violations | CCPA/CPRA |
| Determining whether a small professional services firm needs IG1, IG2, or IG3 controls — and getting a scoped 12-week quick-start plan | CIS Controls v8 |
| Running a CIS Controls v8 gap assessment for a healthcare organisation and mapping findings to HIPAA Security Rule safeguards | CIS Controls v8 + HIPAA |
| Implementing all 56 IG1 safeguards across endpoints, user accounts, backups, and training — prioritised by security impact | CIS Controls v8 |
| Deploying MFA across external applications, remote access, and admin accounts (Safeguards 6.3/6.4/6.5) and selecting phishing-resistant options | CIS Controls v8 |
| Mapping CIS Controls v8 to NIST CSF 2.0 subcategories for a cross-framework compliance programme | CIS Controls v8 + NIST CSF |
| Building a vulnerability management programme with authenticated scans, CVSS-based remediation SLAs, and tracking KPIs | CIS Controls v8 |
| Designing a SIEM and log management programme per Control 8 — what events to collect, retention standards, and NTP synchronisation | CIS Controls v8 |
| Classifying an RF power amplifier under the EAR — ECCN determination and licence requirement analysis for export to Germany | EAR |
| Assessing deemed export obligations for a Chinese national employee accessing controlled encryption source code | EAR |
| Responding to a discovered Entity List re-export violation — voluntary self-disclosure process and penalty mitigation | EAR |
| Determining whether AES-256 cybersecurity software requires a BIS licence for export to France, India, and Brazil | EAR |
| Designing a 7-element Export Compliance Programme for a semiconductor equipment company with customers in Europe and Asia | EAR |
| Determining whether a foreign-made chip uses US-origin equipment subject to the Foreign Direct Product Rule (FDPR) | EAR |
| Applying the ENC licence exception for a commercial encryption product and completing the one-time BIS notification | EAR |
| Categorising a federal HR system under FIPS 199 and selecting the correct SP 800-53B baseline | NIST SP 800-53 |
| Documenting an AC-2(3) OTS finding from a security assessment and building the POA&M with FedRAMP remediation timelines | NIST SP 800-53 |
| Implementing phishing-resistant MFA under IA-2(1) and IA-2(2) to satisfy EO 14028 and OMB M-22-09 | NIST SP 800-53 |
| Writing an SSP control narrative for SC-8(1) Transmission Confidentiality covering TLS 1.2/1.3 with FIPS 140-3 modules | NIST SP 800-53 |
| Performing a gap analysis between ISO 27001:2022 and FedRAMP Moderate baseline and mapping RMF steps to ATO package | NIST SP 800-53 |
| Tailoring a Moderate baseline to remove inapplicable controls, set ODVs, and document compensating controls for a legacy system | NIST SP 800-53 |
| Building a ConMon strategy with monthly vulnerability scan frequencies, annual penetration testing, and POA&M update cadence | NIST SP 800-53 |
| Classifying an AI-powered CV screening tool for European employers under the EU AI Act — risk tier and provider obligations | EU AI Act |
| Assessing whether a predictive policing AI tool violates EU AI Act Art. 5 prohibited practices | EU AI Act |
| Determining GPAI model obligations for an open-source LLM with 3×10²⁴ FLOPs training compute | EU AI Act |
| Navigating dual regulation for an AI diagnostic imaging tool CE-marked under the EU Medical Devices Regulation | EU AI Act |
| Understanding Art. 50(1) chatbot disclosure obligations and deployer vs GPAI provider obligations for an e-commerce AI | EU AI Act |
| Completing a VPAT 2.x (ACR) for federal procurement of enterprise software — all three tables, testing methodology disclosure | Section 508 |
| Auditing a public-facing web application for Section 508 compliance using keyboard-only and screen reader testing | Section 508 |
| Remediating 200 legacy PDF documents for Section 508 — tagged structure, reading order, form field labels, Alt text | Section 508 |
| Writing FAR 52.239-2 accessibility requirements into a federal procurement RFP and evaluating vendor VPAT submissions | Section 508 |
| Preparing a formal undue burden determination and documenting the alternative means of access obligation | Section 508 |
| Auditing a React application for WCAG 2.2 AA compliance — colour contrast, keyboard navigation, ARIA, focus management | WCAG |
| Determining which WCAG version and conformance level is required for legal compliance across US, EU, and UK markets | WCAG |
| Reviewing a design system's colour palette against SC 1.4.3 and identifying accessible replacement values | WCAG |
| Drafting a full web accessibility statement for a public sector website meeting EU Web Accessibility Directive requirements | WCAG |
| Understanding what new success criteria must be met to upgrade a WCAG 2.1 AA conformance claim to WCAG 2.2 AA | WCAG |
| Conducting a gap analysis for a NZ government agency deploying a Restricted-classified case management system | NZISM |
| Preparing a Certification & Accreditation (C&A) submission for a Restricted system — SSP, SRA, POA&M, and ATO sign-off | NZISM |
| Assessing whether hosting Restricted data on AWS Sydney meets NZISM obligations and what Accrediting Authority approvals are needed | NZISM |
| Drafting an NZISM-compliant Access Control Policy with embedded NZISM control IDs and a document classification block | NZISM |
| Advising on SaaS vendor due diligence and mandatory contractual security requirements under NZISM for In-Confidence data | NZISM |
| Running a VN-PDPL gap analysis for a foreign company processing Vietnamese personal data ahead of the 1 January 2026 effective date | VN-PDPL |
| Designing a valid consent mechanism under Vietnam Law 91/2025 — standalone notice, permitted formats, and withdrawal workflows | VN-PDPL |
| Building a 72-hour Ministry of Public Security breach notification workflow for a Vietnamese fintech after a data incident | VN-PDPL |
| Mapping an existing GDPR compliance programme to VN-PDPL — identifying gaps in lawful basis, DPO, and cross-border transfer rules | VN-PDPL + GDPR |
| Assessing cross-border data transfer obligations and preparing the impact assessment dossier under Article 20 for offshore cloud processing | VN-PDPL |
| Classifying a connected IoT product under EU CRA — Default, Class I, or Class II — and understanding the applicable conformity assessment route | EU CRA |
| Running an Annex I gap assessment for a software product placed on the EU market — all 10 Part I security properties and 9 Part II vulnerability obligations | EU CRA |
| Building a CRA-compliant vulnerability disclosure programme with coordinated disclosure, 24h/72h ENISA reporting, and CSIRT notification | EU CRA |
| Preparing technical documentation per Annex VII for a Class I product mandatory Notified Body conformity assessment | EU CRA |
| Implementing an SBOM programme in SPDX or CycloneDX format meeting EU CRA minimum content requirements and CI/CD integration | EU CRA |
| Determining which Saudi frameworks apply when expanding into the Kingdom — NCA ECC, PDPL, SAMA CSF, CST | Saudi Arabia GRC |
| Running an NCA ECC-2:2024 gap assessment for a supplier to Saudi government entities | Saudi Arabia GRC |
| Advising on Saudi PDPL cross-border transfer rules and SAMA CSF obligations for a fintech entering KSA | Saudi Arabia GRC |
| Routing UAE compliance across federal PDPL, DIFC, and ADGM for a free-zone financial services firm | UAE GRC |
| Building a CBUAE-compliant outsourcing and data-residency plan for a UAE bank | UAE GRC |
| Handling a breach affecting both DIFC and mainland UAE customers — which regulators, which deadlines | UAE GRC |
| Preparing an automotive supplier for a first TISAX AL2 assessment (Confidential label) | TISAX |
| Mapping an existing ISO 27001 ISMS to VDA ISA 6 and closing automotive-specific gaps | TISAX |
| Deciding whether to order a TISAX assessment on ISA 6 in 2026 or ISA2027 from January 2027 | TISAX |

---

## How to Install a Skill

1. Download the `.skill` file for the framework you need:

<!-- GEN:readme-download-table -->
   | Framework | Download |
   |-----------|----------|
   | <img src="assets/Logos/iso27001.jpg" alt="ISO 27001" height="20" style="vertical-align:middle;object-fit:contain;"> ISO 27001 | [iso27001.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ISO%2027001%20-%20Claude%20Skill/iso27001.skill) |
   | <img src="assets/Logos/soc2.jpeg" alt="SOC 2" height="20" style="vertical-align:middle;object-fit:contain;"> SOC 2 | [soc2.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/SOC%202%20-%20Claude%20Skill/soc2.skill) |
   | <img src="assets/Logos/fedramp.svg" alt="FedRAMP" height="20" style="vertical-align:middle;object-fit:contain;"> FedRAMP [US] | [fedramp.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/FedRamp%20-%20Claude%20Skill/fedramp.skill) |
   | 🇪🇺 GDPR [EU] | [gdpr-compliance.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/GDPR%20-%20Claude%20Skill/gdpr-compliance.skill) |
   | <img src="assets/Logos/hipaa.png" alt="HIPAA" height="20" style="vertical-align:middle;object-fit:contain;"> HIPAA [US] | [hipaa-compliance.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/HIPAA%20-%20Claude%20Skill/hipaa-compliance.skill) |
   | <img src="assets/Logos/nist-csf.jpeg" alt="NIST CSF" height="20" style="vertical-align:middle;object-fit:contain;"> NIST CSF | [NIST Cybersecurity.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/NIST%20Cybersecurity%20framework%20-%20Claude%20Skill/NIST%20Cybersecurity.skill) |
   | <img src="assets/Logos/pci-dss.png" alt="PCI DSS" height="20" style="vertical-align:middle;object-fit:contain;"> PCI DSS | [PCI-Compliance.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/PCI%20Compliance%20-%20Claude%20Skill/PCI-Compliance.skill) |
   | 🚨 TSA Cybersecurity [US] | [TSA-Compliance.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/TSA%20Compliance%20-%20Claude%20Skill/TSA-Compliance.skill) |
   | 🤖 ISO 42001 AI Management System | [ISO-42001.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ISO%2042001%20-%20Claude%20Skill/ISO-42001.skill) |
   | 🔒 ISO 27701 Privacy Information Management | [iso27701.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ISO%2027701%20-%20Claude%20Skill/iso27701.skill) |
   | 🏦 DORA Digital Operational Resilience | [dora.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/DORA%20-%20Claude%20Skill/dora.skill) |
   | 🇮🇳 DPDPA [India] — Digital Personal Data Protection Act | [dpdpa.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/DPDPA%20-%20Claude%20Skill/dpdpa.skill) |
   | 🛡️ CMMC 2.0 Cybersecurity Maturity Model Certification | [cmmc.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/CMMC%20-%20Claude%20Skill/cmmc.skill) |
   | 🤖 NIST AI Risk Management Framework | [nist-ai-rmf.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/NIST%20AI%20RMF%20-%20Claude%20Skill/nist-ai-rmf.skill) |
   | 🏦 SWIFT Customer Security Programme (CSP) | [swift-csp.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/SWIFT%20CSP%20-%20Claude%20Skill/swift-csp.skill) |
   | 🇦🇺 ISM [Australia] — Australian Information Security Manual | [ism.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ISM%20-%20Claude%20Skill/ism.skill) |
   | 🇪🇺 NIS2 [EU] Directive | [nis2.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/NIS2%20-%20Claude%20Skill/nis2.skill) |
   | <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_California.svg" alt="CA" height="16" style="vertical-align:middle;"> CCPA/CPRA [California] Privacy | [ccpa.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/CCPA%20-%20Claude%20Skill/ccpa.skill) |
   | <img src="assets/Logos/itar.jpg" alt="ITAR" height="20" style="vertical-align:middle;object-fit:contain;"> ITAR [US] — International Traffic in Arms Regulations | [itar.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ITAR%20-%20Claude%20Skill/itar.skill) |
   | <img src="assets/Logos/lgpd-brazil.svg" alt="Brazil" height="20" style="vertical-align:middle;object-fit:contain;"> LGPD [Brazil] — General Data Protection Law | [lgpd.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/LGPD%20-%20Claude%20Skill/lgpd.skill) |
   | <img src="assets/Logos/csrd-eu.svg" alt="EU" height="20" style="vertical-align:middle;object-fit:contain;"> CSRD [EU] — Corporate Sustainability Reporting Directive | [csrd.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/CSRD%20-%20Claude%20Skill/csrd.skill) |
   | 🛡️ CIS Controls v8 — CIS Top 18 Cyber Hygiene | [cis-controls.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/CIS%20Controls%20-%20Claude%20Skill/cis-controls.skill) |
   | 📦 EAR [US] — Export Administration Regulations | [ear.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/EAR%20-%20Claude%20Skill/ear.skill) |
   | 🏛️ NIST SP 800-53 — Security and Privacy Controls for Federal Systems | [nist-800-53.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/NIST%20800-53%20-%20Claude%20Skill/nist-800-53.skill) |
   | 🤖 EU AI Act — Regulation (EU) 2024/1689 | [eu-ai-act.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/EU%20AI%20Act%20-%20Claude%20Skill/eu-ai-act.skill) |
   | ♿ Section 508 [US] — Federal ICT Accessibility | [section-508.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/Section%20508%20-%20Claude%20Skill/section-508.skill) |
   | ♿ WCAG — Web Content Accessibility Guidelines | [wcag.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/WCAG%20-%20Claude%20Skill/wcag.skill) |
   | 🇳🇿 NZISM [New Zealand] — Information Security Manual | [nzism.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/NZISM%20-%20Claude%20Skill/nzism.skill) |
   | 🇻🇳 Vietnam PDPL — Law on Personal Data Protection | [vn-pdpl.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/Vietnam%20PDPL%20-%20Claude%20Skill/vn-pdpl.skill) |
   | 🇪🇺 EU CRA — Cyber Resilience Act | [eu-cra.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/EU%20CRA%20-%20Claude%20Skill/eu-cra.skill) |
   | 🇸🇦 Saudi Arabia GRC — Country Compliance Advisor | [saudi-arabia-grc.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/Saudi%20Arabia%20GRC%20-%20Claude%20Skill/saudi-arabia-grc.skill) |
   | 🇦🇪 UAE GRC — Country Compliance Advisor | [uae-grc.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/UAE%20GRC%20-%20Claude%20Skill/uae-grc.skill) |
   | <img src="assets/Logos/TISAX.svg" alt="TISAX" height="20" style="vertical-align:middle;object-fit:contain;"> TISAX — Trusted Information Security Assessment Exchange | [tisax.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/TISAX%20-%20Claude%20Skill/tisax.skill) |
<!-- /GEN:readme-download-table -->

2. Open Claude and navigate to **Customize → Skills**.
3. Click **Upload Skill** and select the `.skill` file.
4. The skill is now active. Start a new conversation and ask your compliance question — Claude will automatically apply the skill.

> **Tip:** You can install multiple skills at once. If you work across several frameworks (e.g., both ISO 27001 and SOC 2), install all of them — Claude will activate whichever is most relevant to each question.

![Installing Skills in Claude](Installing%20Skills%20in%20Claude.png)

---

## Install via Claude Code Marketplace

If you use Claude Code — the AI-powered CLI for developers — these skills are also available as installable Claude Code plugins through a hosted marketplace. This is the recommended installation path for developers and teams, as it supports version-pinning, automatic updates, and team-wide distribution without any manual file handling.

Add the marketplace and install the skills you need directly from the terminal:

<!-- GEN:readme-install-all -->
```shell
/plugin marketplace add Sushegaad/Claude-Skills-Governance-Risk-and-Compliance
/plugin install iso27001@grc-skills soc2@grc-skills fedramp@grc-skills nist-csf@grc-skills cmmc@grc-skills swift-csp@grc-skills ism@grc-skills cis-controls@grc-skills nist-800-53@grc-skills nzism@grc-skills tisax@grc-skills gdpr-compliance@grc-skills hipaa-compliance@grc-skills pci-compliance@grc-skills iso27701@grc-skills dpdpa@grc-skills ccpa@grc-skills lgpd@grc-skills vn-pdpl@grc-skills tsa-compliance@grc-skills dora@grc-skills nis2@grc-skills eu-cra@grc-skills iso42001@grc-skills nist-ai-rmf@grc-skills eu-ai-act@grc-skills itar@grc-skills csrd@grc-skills ear@grc-skills section-508@grc-skills wcag@grc-skills saudi-arabia-grc@grc-skills uae-grc@grc-skills
```
<!-- /GEN:readme-install-all -->

Teams can pre-wire the marketplace in `.claude/settings.json` so every developer gets the skills automatically when they open the project — no manual install required.

📖 **[Full installation instructions, team setup, and update guide → INSTALLATION.md](INSTALLATION.md)**

---

## Skill Evaluation

These skills were benchmarked using the [Claude Skill Creator](https://claude.ai) eval framework. **165 realistic test cases** were run across all 33 skills — 5 per framework — with **Claude Sonnet as both the skill-assisted and baseline model** (same model on both sides, so the delta measures the skills, not model strength) — covering gap analysis, policy drafting, control deep-dives, edge cases, and compliance advice scenarios. Each test case was evaluated against at least 5 objectively verifiable assertions (827 in total) by independent grader agents comparing skill-assisted vs. baseline Claude responses.

| Configuration | Pass Rate | Assertions Passed |
|---------------|-----------|-------------------|
| **With GRC Skills installed** | **92%** | **760 / 827** |
| Without skills (baseline Claude) | 63% | 523 / 827 |
| **Delta** | **+29 points** | **+237 assertions** |

### Per-Skill Results

<!-- GEN:readme-eval-table -->
| Skill | Test Cases | With Skill | Baseline | Delta | What Was Tested |
|-------|-----------|-----------|---------|-------|-----------------|
| ISO 27001 | 5 | **100%** | 84% | +16% | Gap assessment; Policy drafting; 2013→2022 transition; Risk assessment; Management review CAP |
| SOC 2 | 5 | **100%** | 84% | +16% | Type 1 vs 2; CC controls checklist; Availability criteria; Access control policy; Audit exception response |
| FedRAMP [US] | 5 | **96%** | 72% | +24% | Authorization pathways; CR26 Certification Classes A-D; FedRAMP 20x (primary pathway); OSCAL mandate Sep 2026; POA&M remediation timelines |
| GDPR [EU] | 5 | **92%** | 80% | +12% | Automated driver deactivation (Uber Art. 22 fine); 2026 anonymisation standard (EDPB 02/2026); genAI web scraping (03/2026); Art. 28 DPA clauses; ransomware breach workflow |
| HIPAA [US] | 5 | **100%** | 68% | +32% | Security Rule NPRM status (July 2027); self-funded plan enforcement; right-of-access exposure; risk analysis requirements; cloud BAA contents |
| NIST CSF | 5 | **92%** | 56% | +36% | Transit community profile (IR 8576); AI for CSF work (draft SP 1353); informative references (SP 1347); organizational profile build; 1.1 to 2.0 migration |
| PCI DSS | 5 | **84%** | 80% | +4% | FAQ 1331 ROC scoping change; SAQ A eligibility; v4.0.1 mandatory requirements; scope reduction; compensating vs customized approach |
| TSA Cybersecurity [US] | 5 | **100%** | 96% | +4% | Pipeline directive requirements; CIRP elements; OT/IT segmentation; Airport applicability; TSA vs CIRCIA |
| ISO 42001 | 5 | **92%** | 80% | +12% | AIMS applicability; Key requirements; AI-specific risks; Third-party LLM management; AI ethics controls |
| ISO 27701 | 5 | **100%** | 100% | ±0% | Extension to ISO 27001; GDPR mapping; Processor controls; PIA methodology; Certification as GDPR evidence |
| DORA [EU] | 5 | **88%** | 72% | +16% | Five pillars; ICT incident reporting timelines; TLPT requirements; Third-party contracts; DORA vs EBA |
| DPDPA [India] | 5 | **96%** | 80% | +16% | Applicability to foreign entities; Consent vs GDPR; Children's data (18-year threshold); Cross-border transfers; SDF obligations |
| CMMC 2.0 [US] | 5 | **76%** | 28% | +48% | C3PAO cancellation decision; Task Force outlook; SPRS scoring; CUI scoping; POA&M rules |
| NIST AI RMF | 5 | **92%** | 84% | +8% | Four functions overview; Hiring AI risk assessment; Credit scoring risk register; EU AI Act mapping; GOVERN gap assessment |
| SWIFT CSP | 5 | **96%** | 72% | +24% | Architecture scoping (A1/A2/A3/A4/B); MFA hardware token requirement; CSCF v2026 gap assessment; Control 2.4 now mandatory; KYC-SA attestation; Incident response obligations |
| ISM [Australia] | 5 | **92%** | 16% | +76% | September 2026 release (44 new controls); agentic AI controls; OAuth consent hardening; Essential Eight status; cadences and provider access |
| NIS2 [EU] | 5 | **100%** | 56% | +44% | Netherlands Cbw entry into force; transposition laggards and CJEU referrals; incident reporting; essential vs important; Art. 21 measures |
| CCPA/CPRA [California] | 5 | **100%** | 80% | +20% | E-commerce threshold analysis; Combined right-to-know and delete workflow; Ad tech sale vs sharing classification; GDPR-to-CCPA gap analysis; SPI classification for mobile app |
| ITAR [US] | 5 | **80%** | 36% | +44% | DIRCM civil aircraft rule (USML VIII(a)(8), Oct 13 2026); BAE settlement compliance lessons; Cat XI(b) software status; deemed exports; VSD process |
| LGPD [Brazil] | 5 | **76%** | 76% | ±0% | Extraterritorial scope for US SaaS with Brazilian customers; Brazil-EU mutual adequacy (Jan 2026 — no SCCs needed); Data deletion request across CRM/email/analytics; Sensitive health data marketing restrictions; International transfer mechanisms |
| CSRD [EU] | 5 | **88%** | 32% | +56% | CSRD scope analysis for German listed manufacturer (PIE Wave 1); Double materiality vs GRI/TCFD; Post-DMA disclosure requirements for E1/S1/G1; GRI+TCFD to ESRS gap assessment; Non-EU company (US parent, €200M EU revenue) obligations |
| CIS Controls v8 | 5 | **100%** | 80% | +20% | Implementation Group determination; Gap assessment for SaaS startup; MFA safeguard scoping (IG2); CIS v8 to NIST CSF 2.0 mapping; Vulnerability management programme with remediation SLAs |
| EAR [US] | 5 | **76%** | 16% | +60% | Sub-3-hour drone exports (rewritten 9A012); long-endurance drone; military UAV classification (9A610.a); AI-chip diffusion status; Entity List research sale |
| NIST SP 800-53 | 5 | **92%** | 84% | +8% | FIPS 199 categorization for federal HR system; AC-2(3) OTS finding and POA&M documentation; MFA controls and EO 14028 phishing-resistant MFA; SSP narrative for SC-8(1) Transmission Confidentiality; ISO 27001 to FedRAMP gap analysis and RMF steps |
| EU AI Act | 5 | **84%** | 64% | +20% | CV screening high-risk + Annex III Area 4 + Digital Omnibus Dec 2027 deadline; Predictive policing Art. 5 prohibition; Open-source GPAI CoP + 3×10²⁴ FLOPs exception; MDR+AI Act interaction + Aug 2028 Annex I deadline; E-commerce chatbot Art. 50 disclosure |
| Section 508 [US] | 5 | **100%** | 100% | ±0% | VPAT 2.x ACR completion and testing methodology; Keyboard-only navigation failures and WCAG remediation; PDF forms accessibility remediation (200 PDFs); Federal procurement RFP requirements and VPAT evaluation; Undue burden exception process and alternative access obligations |
| WCAG [International] | 5 | **100%** | 85% | +15% | Colour contrast audit (SC 1.4.3) with replacement suggestions; WCAG 2.2 upgrade criteria from 2.1 AA; React modal ARIA code review with corrected implementation; Legal compliance mapping across US/EU/UK; Accessibility statement for e-commerce site |
| NZISM [New Zealand] | 5 | **96%** | 64% | +32% | Restricted system C&A gap analysis; AWS Sydney offshore hosting obligations; Access Control Policy with NZISM control IDs; Ransomware supplier incident response; SaaS vendor due diligence and contractual requirements |
| VN-PDPL [Vietnam] | 5 | **88%** | 8% | +80% | Decree 330/2026 penalty exposure; cross-border transfer duties; law-stack timeline; consent and rights; SME exemptions |
| EU CRA [EU] | 5 | **80%** | 80% | ±0% | PDE scope and classification (Default/Class I/Class II); Annex I gap assessment for consumer IoT router; Vulnerability and ENISA reporting timelines; SBOM programme design; Manufacturer vs importer/distributor obligations |
| Saudi Arabia GRC | 5 | **96%** | 28% | +68% | Market-entry applicability routing; SAMA vs NCA stacking; cloud-for-government residency (CST/CCC); PDPL breach response; ISO 27001 to ECC-2:2024 mapping |
| UAE GRC | 5 | **84%** | 28% | +56% | DIFC routing + 2025 amendment; health-data localization vs US cloud; mainland PDPL status; ADGM breach clock; CBUAE cloud offshoring constraints |
| TISAX | 5 | **96%** | 16% | +80% | First-timer BMW Confidential label; ISO 27001 to TISAX delta; corrective action 9-month window; prototype labels and AL3; ISA2027 transition |
<!-- /GEN:readme-eval-table -->

📊 **[View the full eval results →](grc-skills-eval-results.html)**

---

## Customer Testimonials

Feedback from the GRC and Claude AI community on [LinkedIn](https://www.linkedin.com/posts/jaanametsamaa_an-open-source-repository-of-grc-claude-skills-share-7449381233484034048-xBAf), Reddit ([r/claudeskills](https://www.reddit.com/r/claudeskills/comments/1tvbhp4/claude_skills_for_governance_risk_compliance/) · [r/grc](https://www.reddit.com/r/grc/comments/1rwp2x4/using_claude_ai_skills_to_act_as_a_dedicated_grc/) · [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s6r359/comment/od4k30y/)), and beyond.

> *"An open-source repository of GRC Claude skills that are pretty good! It has ISO 27001, ISO 42001, SOC 2, FedRAMP, GDPR, and others. I checked them out and tested a few. It looks like the skills are at different levels but definitely a very good starting point if your AI assistant doesn't have any GRC skills installed yet."*
> — [Jaana Metsamaa, Co-Founder at Kontion.app (LinkedIn)](https://www.linkedin.com/posts/jaanametsamaa_an-open-source-repository-of-grc-claude-skills-share-7449381233484034048-xBAf)

> *"This open-source project by Hemant Naik transforms Claude into a compliance co-pilot using installable 'Skills' covering 9+ major GRC frameworks. The benchmark shows a 94% pass rate vs 72% for baseline Claude — a solid +22 point lift, especially on accurate citations. Practical for audit preparation, gap assessments, control mapping, and policy drafting. This represents genuine progress toward interactive, intelligence-driven compliance."*
> — [Shubham Mishra, Security Engineering @ Juniper Networks (LinkedIn)](https://www.linkedin.com/posts/mishra321shu_claude-skills-for-governance-risk-compliance-share-7448652308340686848-q6gN/)

> *"The structure is the most useful part. It gives Claude a good lane to stay in for gap assessments, SSP narratives, POA&M work, RMF steps, and control-family walkthroughs. That's a real improvement over asking a general model compliance questions and getting vague output back... this is pretty amazing and could be disruptive to high cost automated compliance tools."*
> — Reddit u/Rockos-Modern-Fife (r/claudeskills)

> *"The skills approach is a good entry point — getting Claude to reason about specific frameworks is exactly the right instinct. The gap I kept hitting was that Claude could describe the compliance picture but couldn't act on it... this is a great start."*
> — Reddit u/sensationweb

> *"Very valuable, seriously. Compliance can sometimes make processes a bit longer, but the upside is much better quality, security, and future readiness. As regulations keep evolving, having structured frameworks in place is becoming more important than ever."*
> — Reddit u/innovation_traits (r/claudeskills)

> *"This is a fantastic initiative! The ability to tailor Claude for specific GRC frameworks is a game-changer for audit preparedness. Huge potential here."*
> — Reddit u/Xin_est (r/claudeskills)

> *"I've been doing something similar for the CIS controls and it's been brilliant so far. I'll be using this for ISO and SOC 2. Thanks!"*
> — Reddit u/gpldn

> *"As a rather new Claude Code user, I'm both impressed and thankful. It's really helpful that you release it publicly. I am at the stage where I understand the need for a well-written CLAUDE.md and skills. This will help me a lot."*
> — Reddit u/bloulboi

> *"Hell ya. We just approved Claude for enterprise so I'll go check it out."*
> — Reddit u/AcrobaticWatercress7

> *"This is brilliant — the frameworks are read by the AI before it produces an answer, which should reduce hallucination and give a tailored, useful output."*
> — Reddit u/Franz99999999 (r/claudeskills)

> *"I work in AI Governance from a risk management background and this is great. I'll check it out, thanks for sharing!"*
> — Reddit u/HousingAppropriate80 (r/claudeskills)

> *"I'll definitely check this out. I have a skill for threat modeling and am working on some other ones, this is super helpful."*
> — Reddit u/lilgreenbite

> *"Pretty cool man, star earned and I will follow closely as a fellow GRC colleague. Power to you!"*
> — Reddit u/daddyicebee (r/claudeskills)

> *"Fantastic work. Going to follow this and test it out myself."*
> — Reddit u/Efficient_Bus_923

> *"This is awesome! Any chance you can build one for ISO 42001?"*
> — Reddit u/ComparisonThink7683

> *"Awesome, thanks for sharing. I'm going to play around with this."*
> — Reddit u/DeliciousNet593

> *"This is awesome, thank you!"*
> — Reddit u/ThePsychicCEO

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

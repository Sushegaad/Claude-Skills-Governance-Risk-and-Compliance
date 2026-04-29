# Claude Skills for Governance, Risk & Compliance (GRC)
Expert-level compliance guidance for ISO 27001, SOC 2, FedRAMP, GDPR, HIPAA, NIST CSF, PCI DSS, TSA Cybersecurity, ISO 42001 AI Management System, ISO 27701 Privacy Information Management, DORA Digital Operational Resilience, India's Digital Personal Data Protection Act (DPDPA), CMMC 2.0 Cybersecurity Maturity Model Certification, NIST AI Risk Management Framework, SWIFT Customer Security Programme (CSP), Australian Information Security Manual (ISM), EU NIS2 Directive, and CCPA/CPRA California Privacy — powered by Claude Skills.

Benchmarked across 90 test cases (5 per framework) using the eval framework — each graded against 5 verifiable assertions by independent agents. Skills scored **95%** vs a baseline of **80%** across 450 total assertions.

[![Release: v0.7.0](https://img.shields.io/badge/Release-v0.7.0-brightgreen.svg)](../../releases/tag/v0.7.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 18](https://img.shields.io/badge/Skills-18-green.svg)](#the-skills)
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

### 10. 🔒 ISO 27701 Privacy Information Management

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

### 11. 🏦 DORA Digital Operational Resilience

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

### 12. 🇮🇳 DPDPA India Digital Personal Data Protection

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

### 13. 🛡️ CMMC 2.0 Cybersecurity Maturity Model Certification

**File:** `CMMC - Claude Skill/cmmc.skill`

The CMMC 2.0 skill turns Claude into an expert CMMC compliance advisor for US defense contractors navigating the Cybersecurity Maturity Model Certification program. It covers all three CMMC levels — Level 1 (17 FAR 52.204-21 practices), Level 2 (110 NIST SP 800-171 Rev 2 practices), and Level 3 (110+ NIST SP 800-172 requirements) — under the final 32 CFR Part 170 rule (effective December 16, 2024).

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

### 15. 🏦 SWIFT Customer Security Programme (CSP)

**File:** `SWIFT CSP - Claude Skill/swift-csp.skill`

The SWIFT CSP skill turns Claude into an expert advisor on the **SWIFT Customer Security Controls Framework (CSCF) v2025** — the mandatory cybersecurity programme for all SWIFT network participants. It covers all 31 controls (23 mandatory + 8 advisory), all five architecture types (A1/A2/A3/A4/B), the KYC-SA annual attestation process, and complete cross-framework mappings to ISO 27001:2022, PCI DSS v4.0.1, and NIST CSF 2.0.

**What it does:**
- Determines the correct **SWIFT architecture type** (A1/A2/A3/A4/B) from a description of the organisation's SWIFT connectivity and produces the full mandatory/advisory control applicability matrix
- Conducts structured **CSCF v2025 gap assessments** with 🔴/🟡/🟢 status per control, evidence requirements, and prioritised remediation roadmaps
- Provides **deep-dive implementation guidance** for all 23 mandatory controls — purpose, requirements, step-by-step implementation, and audit evidence artifacts
- Guides the complete **KYC-SA attestation process** — evidence preparation per control, independent assessor qualification criteria, portal submission steps, and post-submission counterparty visibility
- Advises on the **CSCF v2024 → v2025 changes**: critical patch SLA tightened from 7 to 3 days, hardware MFA token requirement explicitly mandated, log retention clarified (1 year online, 3 years total)
- Provides **SWIFT-specific incident response** guidance — 24-hour initial notification to security@swift.com, 30-day full report, evidence preservation, and IRP content requirements for Control 7.1
- Explains **Type B (service bureau) responsibilities** — the split between bureau and customer obligations, and how to verify your bureau's KYC-SA attestation
- **Maps CSCF controls to ISO 27001:2022, PCI DSS v4.0.1, and NIST CSF 2.0** — identifying both synergies and SWIFT-specific additions not covered by existing certifications

**Trigger phrases:** `SWIFT CSP`, `CSCF`, `KYC-SA`, `SWIFT security attestation`, `Alliance Access`, `SWIFT operator MFA`, `SWIFT secure zone`, `SWIFT secure flow zone`, `CSCF v2025`, `Control 4.2 SWIFT`, `Control 6.4 SWIFT`, `Control 7.1 SWIFT`, `SWIFT architecture type A1`, `SWIFT service bureau`, `Type B SWIFT`, `SWIFT incident response`, `SWIFT gap assessment`, `SWIFT mandatory controls`, `SWIFT hardware token`, `SWIFT log retention`

---

### 16. 🇦🇺 Australian Information Security Manual (ISM)

**File:** `ISM - Claude Skill/ism.skill`

The ISM skill turns Claude into an expert advisor on the **Australian Information Security Manual** — the whole-of-government cybersecurity framework published by the Australian Signals Directorate (ASD) for Australian federal and state government entities and their supply chains. It covers all 22 guideline chapters, the six-step risk management cycle, control applicability markings (NC/OS/PROTECTED/SECRET/TOP SECRET), the IRAP assessment programme, system authorisation, and the Essential Eight relationship.

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

### 17. 🇪🇺 EU NIS2 Directive

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

### 18. <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_California.svg" alt="CA" height="16" style="vertical-align:middle;"> CCPA/CPRA California Privacy

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
| Determining your SWIFT architecture type (A1/A2/A3/A4/B) and getting the full CSCF v2025 control applicability matrix | SWIFT CSP |
| Running a CSCF v2025 gap assessment for an Alliance Access on-premises deployment | SWIFT CSP |
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
| Assessing supply chain security obligations under NIS2 Art. 21(2)(d) and Art. 26 ENISA coordinated risk assessments | NIS2 |
| Calculating maximum NIS2 penalty exposure and comparing EE vs IE supervisory regimes (Art. 32 vs Art. 33) | NIS2 |
| Determining whether a US e-commerce business meets any CCPA/CPRA threshold and understanding its core obligations | CCPA/CPRA |
| Handling a combined right-to-know and right-to-delete request from a California consumer, including identity verification and exceptions | CCPA/CPRA |
| Assessing whether sharing cookie IDs with an ad tech platform constitutes a CCPA 'sale' or CPRA 'sharing', and implementing opt-out mechanisms | CCPA/CPRA |
| Performing a gap analysis between an existing GDPR programme and CCPA/CPRA — identifying California-specific additions | CCPA/CPRA + GDPR |
| Classifying precise geolocation, health, and biometric data as CPRA Sensitive Personal Information and understanding the 15-business-day SPI limitation workflow | CCPA/CPRA |
| Drafting an at-collection privacy notice and a comprehensive privacy policy meeting all CCPA/CPRA disclosure requirements | CCPA/CPRA |
| Implementing Global Privacy Control (GPC) signal recognition as a valid opt-out from sale/sharing | CCPA/CPRA |
| Assessing CPPA enforcement risk and calculating penalty exposure for unintentional vs. intentional CCPA/CPRA violations | CCPA/CPRA |

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
   | 🔒 ISO 27701 Privacy Information Management | [iso27701.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ISO%2027701%20-%20Claude%20Skill/iso27701.skill) |
   | 🏦 DORA Digital Operational Resilience | [dora.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/DORA%20-%20Claude%20Skill/dora.skill) |
   | 🇮🇳 DPDPA India Digital Personal Data Protection | [dpdpa.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/DPDPA%20-%20Claude%20Skill/dpdpa.skill) |
   | 🛡️ CMMC 2.0 Cybersecurity Maturity Model Certification | [cmmc.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/CMMC%20-%20Claude%20Skill/cmmc.skill) |
   | 🤖 NIST AI Risk Management Framework | [nist-ai-rmf.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/NIST%20AI%20RMF%20-%20Claude%20Skill/nist-ai-rmf.skill) |
   | 🏦 SWIFT Customer Security Programme (CSP) | [swift-csp.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/SWIFT%20CSP%20-%20Claude%20Skill/swift-csp.skill) |
   | 🇦🇺 Australian Information Security Manual (ISM) | [ism.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/ISM%20-%20Claude%20Skill/ism.skill) |
   | 🇪🇺 EU NIS2 Directive | [nis2.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/NIS2%20-%20Claude%20Skill/nis2.skill) |
   | <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_California.svg" alt="CA" height="16" style="vertical-align:middle;"> CCPA/CPRA California Privacy | [ccpa.skill](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/CCPA%20-%20Claude%20Skill/ccpa.skill) |

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
/plugin install iso27001@grc-skills soc2@grc-skills fedramp@grc-skills gdpr-compliance@grc-skills hipaa-compliance@grc-skills nist-csf@grc-skills pci-compliance@grc-skills tsa-compliance@grc-skills iso42001@grc-skills iso27701@grc-skills dora@grc-skills dpdpa@grc-skills cmmc@grc-skills nist-ai-rmf@grc-skills swift-csp@grc-skills ism@grc-skills nis2@grc-skills ccpa@grc-skills
```

Teams can pre-wire the marketplace in `.claude/settings.json` so every developer gets the skills automatically when they open the project — no manual install required.

📖 **[Full installation instructions, team setup, and update guide → INSTALLATION.md](INSTALLATION.md)**

---

## Skill Evaluation

These skills were benchmarked using the [Claude Skill Creator](https://claude.ai) eval framework. **90 realistic test cases** were run across all 18 skills — 5 per framework — covering gap analysis, policy drafting, control deep-dives, edge cases, and compliance advice scenarios. Each test case was evaluated against 5 objectively verifiable assertions by independent grader agents comparing skill-assisted vs. baseline Claude responses.

| Configuration | Pass Rate | Assertions Passed |
|---------------|-----------|-------------------|
| **With GRC Skills installed** | **95%** | **428 / 450** |
| Without skills (baseline Claude) | 80% | 362 / 450 |
| **Delta** | **+15 points** | **+66 assertions** |

### Per-Skill Results

| Skill | Test Cases | With Skill | Baseline | Delta | What Was Tested |
|-------|-----------|-----------|---------|-------|-----------------|
| ISO 27001 | 5 | **100%** | 84% | +16% | Gap assessment; Policy drafting; 2013→2022 transition; Risk assessment; Management review CAP |
| SOC 2 | 5 | **100%** | 84% | +16% | Type 1 vs 2; CC controls checklist; Availability criteria; Access control policy; Audit exception response |
| FedRAMP | 5 | **84%** | 76% | +8% | Authorization pathways; Impact levels; FedRAMP 20x; System boundary; POA&M remediation timelines |
| GDPR | 5 | **88%** | 88% | +0% | US company checklist; Article 28 DPA; Subject access request; Cookie consent; 72-hour breach notification |
| HIPAA | 5 | **92%** | 88% | +4% | Covered entity analysis; BAA template; Encryption (addressable vs required); Risk analysis; Workforce violation |
| NIST CSF | 5 | **96%** | 84% | +12% | CSF 2.0 overview; Ransomware recovery plan; Profile creation; Control mapping; Board reporting |
| PCI DSS | 5 | **92%** | 88% | +4% | SAQ type selection; Req 3 stored data (v4.0); Breach obligations; Penetration testing; Tokenization scope |
| TSA Cybersecurity | 5 | **100%** | 96% | +4% | Pipeline directive requirements; CIRP elements; OT/IT segmentation; Airport applicability; TSA vs CIRCIA |
| ISO 42001 | 5 | **92%** | 80% | +12% | AIMS applicability; Key requirements; AI-specific risks; Third-party LLM management; AI ethics controls |
| ISO 27701 | 5 | **100%** | 80% | +20% | Extension to ISO 27001; GDPR mapping; Processor controls; PIA methodology; Certification as GDPR evidence |
| DORA | 5 | **88%** | 72% | +16% | Five pillars; ICT incident reporting timelines; TLPT requirements; Third-party contracts; DORA vs EBA |
| DPDPA | 5 | **96%** | 80% | +16% | Applicability to foreign entities; Consent vs GDPR; Children's data (18-year threshold); Cross-border transfers; SDF obligations |
| CMMC 2.0 | 5 | **100%** | 100% | +0% | Level determination; SPRS scoring; CUI scoping; SSP structure; C3PAO assessment readiness |
| NIST AI RMF | 5 | **92%** | 76% | +16% | Four functions overview; Hiring AI risk assessment; Credit scoring risk register; EU AI Act mapping; GOVERN gap assessment |
| SWIFT CSP | 5 | **100%** | 48% | +52% | Architecture scoping (A1/A2/A3/A4/B); MFA hardware token requirement; CSCF v2025 gap assessment; KYC-SA attestation process; Incident response obligations |
| ISM | 5 | **96%** | 52% | +44% | OS control scoping and authorisation; IRAP assessment preparation; Chapter 13 system hardening; Essential Eight to ISM mapping; Supply chain cloud provider obligations |
| NIS2 | 5 | **96%** | 80% | +16% | Energy company EE/IE classification; SaaS provider Art. 21 obligations; Ransomware Art. 23 reporting workflow; ISO 27001 vs NIS2 gap analysis; DORA lex specialis interaction |
| CCPA/CPRA | 5 | **100%** | 96% | +4% | E-commerce threshold analysis; Combined right-to-know and delete workflow; Ad tech sale vs sharing classification; GDPR-to-CCPA gap analysis; SPI classification for mobile app |

Skills add the most measurable value on highly framework-specific tasks: clause-level precision for ISO 27001, CC criteria mapping for SOC 2, exact FedRAMP POA&M timeframes and document names, GDPR article citations, HIPAA regulatory section references, CSF 2.0 subcategory IDs, PCI DSS v4.0.1 requirement numbers, TSA Security Directive citations, ISO 42001 AIMS clause references, DORA Article citations and exact incident reporting timelines (4h/72h/1 month), DPDPA-specific terminology, CMMC practice IDs and SPRS scoring, NIST AI RMF category notation (GV-1 through MG-4.x) and trustworthiness metrics, SWIFT CSP architecture classification and CSCF v2025 control-specific guidance, ISM applicability marking precision (NC/OS/PROTECTED stacking rules, IRAP artefacts, chapter-level control citations), NIS2 entity classification (Annex I/II), Art. 21 measure detail, and Art. 23 incident reporting timeline specificity (24h/72h/1-month), and CCPA/CPRA-specific GPC signal obligation, SPI 15-business-day response SLA, and CPRA "sharing" vs. "sale" classification precision.

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

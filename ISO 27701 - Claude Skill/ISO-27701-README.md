# ISO 27701 Privacy Information Management System Skill for Claude

A Claude skill that provides expert, end-to-end guidance for implementing, auditing, and certifying a Privacy Information Management System (PIMS) under ISO/IEC 27701:2019 — the international standard that extends ISO 27001 to include privacy management for PII Controllers and PII Processors.

---

## What Does the Skill Do?

This skill turns Claude into a knowledgeable ISO 27701 compliance advisor. It covers the full lifecycle of PIMS implementation and certification, from initial gap assessment through to policy generation, control implementation, and audit readiness.

At a high level, the skill enables Claude to:

- Define the **PIMS scope** — documenting PII types, PII principals, processing purposes, controller and/or processor roles, and applicable privacy laws
- Conduct **gap analyses** covering both the Clause 5 ISMS extension requirements and the applicable Clause 7 (PII Controller) and/or Clause 8 (PII Processor) control sets
- Guide the creation of a **PIMS Statement of Applicability (PIMS-SoA)** recording control applicability determinations and justifications
- Assist with **Privacy Impact Assessments (PIA / DPIA)** including trigger screening, risk rating, measure selection, and documentation
- Generate **PIMS documentation**: privacy policy, data retention policy, records of processing activities (RoPA), consent records, PII principal rights procedures, privacy incident reports, and processor contracts
- Map ISO 27701 controls and requirements to **GDPR articles**, ISO 29100 privacy principles, ISO 27018, and ISO 29151
- Provide granular **control implementation guidance** for every clause 7 and clause 8 control, structured as: Purpose, Requirements, Implementation Steps, Evidence, Common Pitfalls, and GDPR relevance
- Support **PII principal rights** workflows covering access, rectification, erasure, objection, consent withdrawal, portability, and automated decision-making rights
- Advise on the **certification path** — prerequisites, combined ISO 27001/27701 audit process, and a certification-readiness checklist

---

## Intended Audiences

| Audience | How They Benefit |
|---|---|
| **Privacy Officers / DPOs** | Navigate PIMS implementation, draft policies, manage PIAs, oversee controller/processor obligations |
| **GRC / Compliance Teams** | Perform gap analyses, build the PIMS-SoA, prepare for certification, maintain the RoPA |
| **Legal Teams** | Understand ISO 27701 requirements relative to GDPR and other applicable laws, draft processor agreements |
| **IT / Engineering Teams** | Implement privacy by design, configure data minimisation, build rights fulfilment mechanisms, manage retention |
| **Internal Auditors** | Scope and conduct PIMS audits, evaluate control implementation, generate audit findings |
| **Cloud Service Providers** | Understand Clause 8 processor controls, manage sub-processor obligations, handle government access requests |
| **ISO 27001 Practitioners** | Understand how ISO 27701 extends their existing ISMS and what additional work is needed for PIMS certification |
| **Consultants and Advisory Firms** | Provide accurate ISO 27701 guidance to clients across industries |

---

## Common Use Cases

### 1. Initial Gap Assessment
> *"We are ISO 27001 certified and want to extend to ISO 27701. Where do we start?"*

The skill establishes whether the organisation acts as a controller, processor, or both, then generates a structured gap analysis table covering all Clause 5 ISMS extensions and all applicable Clause 7 and/or Clause 8 controls, with status, evidence needed, and gap notes.

### 2. PIMS Scope Definition
> *"Help me define the scope of our PIMS."*

The skill guides the user through documenting PII types, PII principals, processing purposes, applicable privacy laws, controller/processor roles, and geographic extent — producing a PIMS scope statement.

### 3. Privacy Policy Drafting
> *"Draft an external privacy notice for our SaaS platform."*

The skill generates a complete, structured external privacy notice meeting the disclosure requirements of GDPR Art. 13 and equivalent laws, populated with the user's processing details.

### 4. Records of Processing Activities
> *"Generate a RoPA template for a PII Controller."*

The skill produces a complete RoPA structure with all fields required by ISO 27701 Clause 7.2.8 and GDPR Art. 30, pre-populated with example entries and guidance on completion.

### 5. Privacy Impact Assessment
> *"We're launching a new AI-based recommendation engine that profiles users. Do we need a DPIA and how do we conduct it?"*

The skill confirms the PIA is required based on systematic profiling, then guides the user through the screening, description, necessity assessment, risk rating, measure selection, and sign-off stages.

### 6. Control Implementation Guidance
> *"How do we implement ISO 27701 control 7.2.6 — Contracts with PII Processors?"*

The skill provides detailed implementation guidance covering the purpose of the control, minimum contract provisions, implementation steps, evidence an auditor will look for, and the GDPR Art. 28 alignment.

### 7. GDPR Mapping
> *"How does ISO 27701 map to GDPR?"*

The skill provides a comprehensive control-level mapping between ISO 27701 clauses and GDPR articles, with compliance notes on what each mapping means in practice.

### 8. PII Principal Rights Workflows
> *"A customer has submitted a Subject Access Request. Walk me through the process."*

The skill steps through the SAR workflow: identity verification, request scoping, locate-and-compile, redaction of third-party data, response within legal deadlines, and documentation.

### 9. Certification Readiness Assessment
> *"Are we ready for ISO 27701 certification? What is the audit process?"*

The skill produces a structured certification-readiness checklist covering all evidence requirements for Stage 1 and Stage 2 audit, and explains the combined ISO 27001/27701 certification model.

### 10. Processor Controls Guidance
> *"We are a cloud SaaS provider. What are our ISO 27701 obligations as a PII Processor?"*

The skill provides a complete walkthrough of all 15 Clause 8 controls, with implementation guidance specific to cloud service provider contexts, including sub-processor management and government access request handling.

---

## Framework Coverage

| Area | Coverage |
|------|----------|
| ISO 27701:2019 Clause 5 | All ISMS extension requirements (5.2–5.8) |
| ISO 27701:2019 Clause 6 | Privacy-specific guidance for ISO 27002 controls |
| ISO 27701:2019 Clause 7 | All 27 PII Controller controls (7.2.1–7.5.3) |
| ISO 27701:2019 Clause 8 | All 15 PII Processor controls (8.2.1–8.5.6) |
| GDPR Mapping | Full control-to-article mapping with compliance notes |
| ISO 29100 | All 11 privacy principles with control alignment |
| ISO 27018 | Processor control comparison (Annex E alignment) |
| ISO 29151 | Controller control comparison (Annex D alignment) |
| Document Templates | Privacy policy, RoPA, PIA, consent records, rights log, incident report |

---

## How to Install

See [INSTALLATION.md](../INSTALLATION.md) for instructions on installing Claude skills.

For this skill, the `.skill` file is: `iso27701.skill`

---

## Relationship to Other Skills in This Repository

ISO 27701 is an extension standard. The following companion skills complement this one:

| Skill | Reason to Use Alongside ISO 27701 |
|-------|----------------------------------|
| **iso27001** | ISO 27701 cannot be certified without ISO 27001 as a foundation; use both skills for integrated ISMS + PIMS work |
| **gdpr-compliance** | For deep GDPR legal analysis, article-by-article advice, and GDPR-specific document drafting |
| **iso27018** | For cloud PII Processor contexts where ISO 27018 is also in scope |

---

## Source and Standard Version

This skill is based on **ISO/IEC 27701:2019** — the first and current edition, published 6 August 2019 by the International Organization for Standardization and the International Electrotechnical Commission.

The standard is available for purchase from ISO (iso.org) and national standards bodies. All control descriptions and requirements in this skill are derived from the published standard and its informative annexes.

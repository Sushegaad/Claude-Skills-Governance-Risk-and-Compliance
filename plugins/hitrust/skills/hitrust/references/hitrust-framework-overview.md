# HITRUST Framework Overview
## HITRUST Alliance, Common Security Framework History, Versions, and Key Concepts

---

## Table of Contents
1. [About HITRUST Alliance](#1-about-hitrust-alliance)
2. [HITRUST CSF — What It Is and What It Solves](#2-hitrust-csf--what-it-is-and-what-it-solves)
3. [Framework Version History](#3-framework-version-history)
4. [HITRUST vs. HIPAA — Key Differences](#4-hitrust-vs-hipaa--key-differences)
5. [HITRUST vs. Other Frameworks](#5-hitrust-vs-other-frameworks)
6. [Cross-Framework Mapping](#6-cross-framework-mapping)
7. [Who Needs HITRUST Certification](#7-who-needs-hitrust-certification)
8. [HITRUST and Shared Compliance](#8-hitrust-and-shared-compliance)
9. [Key HITRUST Terminology](#9-key-hitrust-terminology)
10. [Disclaimer and Limitations](#10-disclaimer-and-limitations)

---

## 1. About HITRUST Alliance

**HITRUST Alliance** is a private organization founded in **2007** by a group of healthcare
and information security leaders. Headquartered in the United States, HITRUST was created to
address the lack of a unified, certifiable security framework for the healthcare industry.

HITRUST is not a government agency and HITRUST certification is not a regulatory requirement
mandated by any federal or state law. However, HITRUST certification is widely accepted as
evidence of a robust information security and compliance programme, particularly within the
US healthcare ecosystem.

**Key facts about HITRUST Alliance:**
- Founded: 2007
- HITRUST CSF first published: 2009
- Type: Private, for-profit organization
- Headquarters: Frisco, Texas, USA
- Primary product: HITRUST CSF and the HITRUST Assurance Program
- MyCSF platform: Proprietary web-based assessment management portal

---

## 2. HITRUST CSF — What It Is and What It Solves

### The Problem HITRUST Was Created to Address
Before HITRUST, healthcare organizations and their business partners faced a fragmented
compliance landscape. A single covered entity or business associate might receive different
security questionnaires from dozens of health plans, each asking about different standards
(HIPAA, ISO 27001, NIST SP 800-53, PCI DSS, etc.) with no consistent way to demonstrate
compliance across all of them.

HITRUST CSF was designed to:
1. **Consolidate** — Incorporate requirements from multiple frameworks and regulations into
   a single, prescriptive control set
2. **Certify** — Enable organizations to obtain a certifiable attestation enforceable through
   third-party assessment, rather than self-attestation
3. **Scale** — Apply to organizations of different sizes, types, and risk profiles through
   the risk-tailoring mechanism of the r2 assessment
4. **Reduce audit fatigue** — Allow organizations to use a single HITRUST certification to
   satisfy multiple customer and regulatory inquiries simultaneously

### What the CSF Is
The HITRUST Common Security Framework (CSF) is:
- A **prescriptive, certifiable security and privacy framework**
- Designed to be **risk-based and scalable** across organization types and sizes
- An **integrating framework** that harmonises multiple authoritative sources
- Applicable primarily to **healthcare** but increasingly adopted in financial services,
  technology, and other regulated sectors

### What the CSF Is Not
- HITRUST CSF certification is **not a legal requirement** under HIPAA or any federal law
- HITRUST certification does **not guarantee or constitute legal HIPAA compliance** —
  however, it is widely considered strong evidence of a robust HIPAA security programme
- HITRUST is **not a government standard** — it is a privately developed framework
- Passing the HITRUST assessment does **not mean every control in the HITRUST CSF applies**;
  only in-scope controls are assessed

---

## 3. Framework Version History

| Version | Release Year | Key Changes |
|---------|-------------|-------------|
| CSF v1 | 2009 | Initial publication; baseline control set derived from HIPAA and ISO 27001 |
| CSF v6 | c. 2013 | Significant expansion; added NIST SP 800-53 and PCI DSS mapping |
| CSF v7 | c. 2015 | Updated to NIST SP 800-53 Rev 4; expanded third-party assurance controls |
| CSF v8 | c. 2017 | Significant structural update; added CMS ARS mapping; cloud-specific controls |
| CSF v9.x | 2018–2022 | Long-running stable version; widely deployed; 14 categories, 49 objectives, 156 specifications |
| CSF v9.6.2 | 2022 | Most recent v9.x maintenance release; widely used at time of v11 introduction |
| CSF v10 | 2022 | Transitional release; not widely deployed before v11 superseded it |
| CSF v11 | January 2023 | Current version; reorganised control structure; introduced/clarified e1/i1/r2 tiers; enhanced CMMC 2.0 and NIST SP 800-171 alignment |

### CSF v9.x vs. CSF v11
The transition from v9.x to v11 primarily affected:
- Internal organisation and numbering of some controls
- Enhanced prescriptive implementation guidance (telling organizations not just what to do
  but how)
- Stronger alignment with CMMC 2.0, NIST SP 800-171, and NIST CSF 2.0
- Clarification of i1 as a distinct "Defined Baseline" assessment (fixed 219 controls)
- Improved cross-framework attribution (each control cited against its source frameworks)

Organizations that completed a v9.x assessment and are renewing can transition to v11
requirements through normal renewal. Assessors can advise on specific control changes.

---

## 4. HITRUST vs. HIPAA — Key Differences

This is one of the most frequently asked questions about HITRUST.

| Dimension | HIPAA | HITRUST CSF |
|-----------|-------|-------------|
| Type | Federal law and regulation | Private, voluntary framework |
| Enforcer | HHS Office for Civil Rights (OCR) | HITRUST Alliance (private) |
| Mandatory? | Yes — for Covered Entities and Business Associates | No — voluntary; often required by contracts |
| Prescriptiveness | Principle-based (does not specify specific technologies) | Prescriptive (specifies specific encryption standards, password lengths, etc.) |
| Certification | No formal certification exists (OCR enforces through audits and complaints) | Formal 1-year or 2-year certification letter from HITRUST |
| Scope | US Covered Entities and Business Associates | Any organization; primarily healthcare |
| Self-assessment | HIPAA risk analysis is required but no validated assessment mandated | Validated assessment by external assessor required |
| Audit trail | OCR audits and complaint investigations | MyCSF platform; HITRUST-endorsed certification |

### Critical Point: HITRUST Does Not Equal Full HIPAA Compliance
HITRUST incorporates HIPAA Security Rule and Privacy Rule requirements. However:
- Certification covers the in-scope controls based on risk factors — not necessarily
  every HIPAA requirement
- HIPAA obligations exist regardless of certification status
- HITRUST certification may be used as evidence of a robust security programme in the
  event of an OCR investigation but does not provide legal immunity
- Organizations must still maintain BAAs, provide NPPs, respond to patient rights requests,
  and meet all HIPAA obligations independent of their HITRUST certification

---

## 5. HITRUST vs. Other Frameworks

### HITRUST vs. SOC 2

| Dimension | HITRUST r2 | SOC 2 Type 2 |
|-----------|-----------|--------------|
| Standard setter | HITRUST Alliance | AICPA |
| Framework type | Prescriptive, certification-based | Principles-based, audit-based |
| Controls | Prescriptive specifications with maturity scoring | Organization-designed controls mapped to Trust Services Criteria |
| Report output | Certification letter | SOC 2 Type 2 Audit Report |
| Certification period | 2 years (r2) | 12-month period typically |
| Healthcare-specific | Strong HIPAA alignment | General (Privacy TSC not healthcare-specific) |
| Market recognition | Strong in healthcare | Strong across technology and services sectors |
| Customer interpretation | Pass/fail certification | Requires reading the report for nuance |
| Inheritance | Formal inheritance program | No standardised inheritance mechanism |

### HITRUST vs. ISO 27001

| Dimension | HITRUST r2 | ISO 27001:2022 |
|-----------|-----------|----------------|
| Standard setter | HITRUST Alliance | ISO / IEC |
| Framework type | Prescriptive risk-based | Management system (principled; risk-based) |
| Certification body | HITRUST Alliance | Accredited ISO certification bodies |
| Healthcare specificity | High — HIPAA baked in | General; healthcare extensions via ISO 27799 |
| Prescriptiveness | High — specific technical requirements | Moderate — controls in Annex A but organisation defines implementation |
| Certificate | HITRUST certification letter | ISO 27001 certificate from accredited CB |
| Global recognition | Primarily US healthcare | Global |

### HITRUST vs. NIST SP 800-53

| Dimension | HITRUST CSF | NIST SP 800-53 Rev 5 |
|-----------|--------------------|-----------------------|
| Type | Certifiable private framework | US government control catalogue |
| Mandatory? | Voluntary / contractual | Mandatory for US federal agencies; widely adopted by contractors |
| Certification | HITRUST certification letter | FedRAMP Authorization, StateRAMP, or self-attestation |
| HITRUST relationship | CSF maps to NIST SP 800-53 | Source framework mapped into CSF |
| Healthcare use | Primary healthcare market | Used by healthcare where CMS ARS applies |

---

## 6. Cross-Framework Mapping

HITRUST CSF controls are attributed to their source frameworks. For each HITRUST control
specification, HITRUST publishes the corresponding requirement(s) in the authoritative
source frameworks.

### Sample Cross-Framework Mapping

| HITRUST Control | HITRUST Category | HIPAA Ref | NIST 800-53 | ISO 27001:2022 |
|----------------|-----------------|-----------|-------------|----------------|
| 01.a.1 Access Control Policy | 01 — Access Control | 164.312(a)(1) | AC-1 | A.5.15 |
| 01.b.1 User Registration | 01 — Access Control | 164.312(a)(2)(i) | AC-2 | A.5.15, A.5.16 |
| 01.c.1 Privilege Management | 01 — Access Control | 164.312(a)(1) | AC-2(1), AC-6 | A.5.15, A.5.18 |
| 01.d.1 Password Management | 01 — Access Control | 164.312(d) | IA-5 | A.5.17 |
| 01.q.1 Remote Access | 01 — Access Control | 164.312(a)(2)(ii) | AC-17, IA-3 | A.6.7 |
| 03.b.1 Risk Assessment | 03 — Risk Management | 164.308(a)(1)(ii)(A) | RA-3 | Clause 6.1 |
| 09.j.1 Malware Controls | 09 — Ops Management | 164.308(a)(5)(ii)(B) | SI-3 | A.8.7 |
| 09.l.1 Backup | 09 — Ops Management | 164.308(a)(7)(ii)(A) | CP-9 | A.8.13 |
| 09.r.1 Audit Logging | 09 — Ops Management | 164.312(b) | AU-2, AU-3 | A.8.15 |
| 10.f.1 Cryptography Policy | 10 — SDLC | 164.312(a)(2)(iv) | SC-8, SC-28 | A.8.24 |
| 11.c.1 Incident Response | 11 — Incident Mgmt | 164.308(a)(6), 164.314(a)(2)(i)(C) | IR-1, IR-4 | A.5.24–A.5.28 |
| 12.c.1 Business Continuity | 12 — BCP | 164.308(a)(7) | CP-2, CP-4 | A.5.29–A.5.30 |
| 13.a.1 Privacy Notice | 13 — Privacy | 164.520 | PT-1 | N/A (privacy) |
| 13.f.1 Minimum Necessary | 13 — Privacy | 164.502(b) | PT-3 | N/A (privacy) |

**Note:** These mappings are representative examples. The full cross-framework mapping is
maintained by HITRUST and published in the MyCSF platform and HITRUST CSF documentation.
Always refer to the current HITRUST CSF version for authoritative mappings.

---

## 7. Who Needs HITRUST Certification

HITRUST certification is not mandated by law, but it is increasingly required by contract
in the US healthcare ecosystem.

### Organizations That Commonly Need HITRUST Certification

**Healthcare Providers and Health Systems**
- Hospital systems and integrated delivery networks
- Physician groups and clinics
- Specialty care providers with significant electronic health record (EHR) usage
- Home health and long-term care organizations

**Health Plans and Payers**
- Commercial health insurers
- Managed care organizations
- Self-insured employer health plans (where they act as plan administrators and process ePHI)
- Medicare Advantage plans

**Business Associates**
- Health IT vendors (EHR companies, health information exchanges)
- Revenue cycle management companies
- Healthcare analytics and data companies
- Cloud service providers processing ePHI
- Medical billing and coding companies
- IT services providers with access to ePHI

**Why Organizations Pursue HITRUST Certification**
1. **Customer requirement**: Largest health plans and hospital systems increasingly require
   their vendors to hold HITRUST certification (commonly r2) as a condition of doing business
2. **Competitive differentiation**: HITRUST certification differentiates vendors in a
   competitive healthcare market
3. **Audit fatigue reduction**: A HITRUST certification letter can satisfy multiple security
   questionnaires simultaneously
4. **Internal programme improvement**: The assessment process itself drives security
   programme maturity
5. **Regulatory alignment**: Demonstrates comprehensive HIPAA security controls implementation

### Organizations That May Not Need HITRUST
- Organizations outsidethehealthcare industry with no HIPAA obligations and no customer
  requirements for HITRUST (may find SOC 2 or ISO 27001 more appropriate)
- Very small providers with minimal electronic data processing (may find HIPAA risk analysis
  sufficient without full HITRUST certification)
- Organizations where the cost of certification outweighs the business benefit

---

## 8. HITRUST and Shared Compliance

### Using HITRUST to Satisfy Multiple Frameworks

Because HITRUST CSF harmonises multiple frameworks, a robust HITRUST r2 certification
generally provides evidence relevant to compliance with:
- HIPAA Security Rule — Strong coverage; HITRUST CSF was built around HIPAA requirements
- SOC 2 Trust Services Criteria — Significant overlap, particularly Security (CC) criteria
- ISO 27001 — Meaningful overlap in technical controls; governance approach differs
- NIST CSF — Strong functional mapping; HITRUST has published official NIST CSF mappings
- PCI DSS — If PCI scoping factors are included; specific PCI controls may supplement

### What HITRUST Certification Supports (but Does Not Replace)
- HIPAA risk analysis: OCR requires a specific, documented risk analysis; HITRUST Category 03
  covers risk management broadly but the organisation must maintain a HIPAA-specific risk
  analysis document
- Business Associate Agreements: BAAs are a legal requirement under HIPAA; the existence of
  a BAA is not replaced by HITRUST certification
- Breach notification obligations: HITRUST certification does not alter the legal obligation
  to notify affected individuals, HHS, and media under HIPAA's Breach Notification Rule

---

## 9. Key HITRUST Terminology

| Term | Definition |
|------|-----------|
| **HITRUST Alliance** | Private organization that owns and maintains the HITRUST CSF and the Assurance Program |
| **HITRUST CSF** | Common Security Framework — the framework document containing all control categories, objectives, and specifications |
| **MyCSF** | HITRUST's online assessment management portal (myCSF.net) |
| **e1** | Entry-Level assessment; 44 fixed control requirements; 1-year certification |
| **i1** | Implemented, 1-Year assessment; 219 Defined Baseline controls; 1-year certification |
| **r2** | Risk-Based, 2-Year assessment; variable risk-tailored controls; 2-year certification |
| **AEA** | Authorized External Assessor — an organization approved by HITRUST to conduct validated assessments |
| **CAP** | Corrective Action Plan — a documented remediation plan for a non-certifiable or near-certifiable finding |
| **Certification Letter** | The official document issued by HITRUST certifying the organization's compliance status, scope, and certification period |
| **Control Category** | One of the 14 high-level groupings of controls in HITRUST CSF v9.x (00–13) |
| **Control Objective** | Sub-division within a control category (e.g., 01.a — Access Control Policy) |
| **Control Specification** | The specific prescriptive requirement (e.g., 01.a.1) |
| **Defined Baseline (dB)** | The fixed set of 219 controls used for i1 assessment in CSF v11 |
| **Inheritance** | A mechanism where an organization receives credit for controls that are the responsibility of a certified third-party service provider |
| **Inheritee** | The HITRUST-certified organization whose controls are being inherited |
| **Inheritor** | The organization that benefits from inheriting controls from the Inheritee |
| **Maturity Level** | One of the five levels (Policy, Procedure, Implemented, Measured, Managed) at which each control is assessed |
| **Non-Certifiable Finding** | A control scoring below 62 out of 100; a CAP is required before certification can proceed |
| **Near-Certifiable Finding** | A control scoring 62–74; a CAP is recommended; does not block certification |
| **Certifiable** | A control scoring 75 or above; no CAP required |
| **Risk Factor** | An organizational characteristic (e.g., cloud usage, large record volume) that activates additional r2 control requirements |
| **Scoping Questionnaire** | The MyCSF questionnaire that determines which r2 controls apply to a specific organization |
| **Validated Assessment** | The formal HITRUST assessment conducted with an AEA in which the assessor validates and scores the organization's responses |
| **Readiness Assessment** | An optional pre-assessment activity (gap assessment) to identify and address weaknesses before the validated assessment |
| **Interim Assessment** | A required mid-certification assessment at 12 months for r2 certifications |
| **Shared Responsibility Matrix** | Documentation that maps inherited vs. customer-owned controls in third-party service arrangements |

---

## 10. Disclaimer and Limitations

This reference document is maintained for use within the HITRUST skill context and reflects
information from official HITRUST published materials as of the knowledge cutoff.

**Important limitations:**
- HITRUST CSF requirements, assessment processes, and scoring thresholds are updated by
  HITRUST Alliance and may change. Always consult the current published version of the
  HITRUST CSF and the MyCSF platform for authoritative requirements.
- This document does not constitute official HITRUST guidance. For authoritative guidance,
  consult: HITRUST Alliance (hitrustalliance.net), published HITRUST CSF documentation,
  and a HITRUST Authorized External Assessor.
- Control specification numbers, names, and details are based on the HITRUST CSF v9.x
  structure and may differ in CSF v11. Verify against the current MyCSF framework for active
  assessments.
- HITRUST certification does not constitute legal advice on regulatory compliance.
  Organizations must consult qualified legal counsel for HIPAA compliance determinations.

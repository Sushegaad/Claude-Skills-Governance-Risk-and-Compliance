# PCI DSS — Complete Version History

Sources:
- PCI Security Standards Council (PCI SSC): https://www.pcisecuritystandards.org/document_library/
- PCI DSS Summary of Changes documents (each version): https://www.pcisecuritystandards.org
- PCI SSC press releases and blog; PCI DSS v4.0.1 (June 2024)

---

## Overview

PCI DSS (Payment Card Industry Data Security Standard) is a global standard governing the security of systems that store, process, or transmit payment card data. It was created through a collaboration of the five major card brands (Visa, MasterCard, American Express, Discover, JCB) and is administered by the **PCI Security Standards Council (PCI SSC)**, which was founded in September 2006.

Before the PCI SSC was established, each card brand maintained its own security programme:
- Visa: Cardholder Information Security Programme (CISP)
- MasterCard: Site Data Protection (SDP)
- American Express: Data Security Operating Policy (DSOP)
- Discover: Information Security and Compliance (DISC)
- JCB: Data Security Programme (JDSP)

PCI DSS v1.0 unified these programmes into a single standard.

**Current version**: PCI DSS v4.0.1 (June 2024)
**All current assessments must use v4.0.1** — no earlier version is valid for a live compliance assessment as of March 31, 2024.

---

## Complete Version Timeline

| Version | Published | Retired | Key Focus |
|---------|-----------|---------|-----------|
| v1.0 | December 2004 | Retired | First unified standard; 12 requirements established |
| v1.1 | September 2006 | Retired | PCI SSC formation; wireless and application security additions |
| v1.2 | October 2008 | Retired | Strengthened wireless; WEP deprecated; structural clarifications |
| v1.2.1 | July 2009 | Retired | Minor corrections; no new requirements |
| v2.0 | October 2010 | Retired | Virtualisation guidance; clarifications; risk-based assessment language |
| v3.0 | November 2013 | Retired | Business-as-usual security; POI device skimming protections |
| v3.1 | April 2015 | Retired | SSL/TLS 1.0 deprecation mandated |
| v3.2 | April 2016 | Retired | MFA expansion; service provider-specific requirements added |
| v3.2.1 | May 2018 | **March 31, 2024** | TLS migration clarification; last v3.x release |
| v4.0 | March 2022 | Superseded June 2024 | Customised Approach; outcomes-based; future-dated requirements |
| **v4.0.1** | **June 2024** | **CURRENT** | Errata corrections to v4.0; no new requirements |

---

## PCI DSS v1.0 (December 2004)

**Status**: Retired
**Published by**: Visa, MasterCard, American Express, Discover, JCB (jointly — pre-PCI SSC)

### What it established
PCI DSS v1.0 unified five separate card brand security programmes into a single standard for the first time. It established the foundational architecture still present in all subsequent versions:

- **12 requirements** grouped under **6 goals** (same structure maintained today)
- **6 goals**: Build and Maintain a Secure Network; Protect Cardholder Data; Maintain a Vulnerability Management Program; Implement Strong Access Control Measures; Regularly Monitor and Test Networks; Maintain an Information Security Policy
- The concept of the **Cardholder Data Environment (CDE)** as a scoping boundary
- Prohibition on storing sensitive authentication data (CVV, PIN block, full magnetic stripe) after authorisation
- Requirement for quarterly external and internal vulnerability scans
- Requirement for annual penetration testing
- Network security: firewalls between untrusted networks and CDE
- Requirement to use strong cryptography for cardholder data storage and transmission

### Key limitations at v1.0
- Limited specificity on wireless security
- No formalised SAQ programme (self-assessment questionnaires were basic)
- No virtualisation guidance
- Limited guidance on service providers and third-party relationships

---

## PCI DSS v1.1 (September 2006)

**Status**: Retired
**Published by**: PCI SSC (newly formed)

### Key changes from v1.0
- Published as the first standard under the newly formed **PCI Security Standards Council** (September 2006)
- Added guidance on **application firewalls** for public-facing web applications as an option to address application-layer attacks (early predecessor to WAF requirement)
- Strengthened wireless security requirements — clarified requirements for wireless access points in the CDE
- Codified the role of the **Qualified Security Assessor (QSA)** and **Approved Scanning Vendor (ASV)** programmes
- Introduced the formal **SAQ programme** (4 SAQ types initially: A, B, C, D)
- Clarified scope and applicability for service providers vs merchants

---

## PCI DSS v1.2 (October 2008)

**Status**: Retired

### Key changes from v1.1
- **Wireless security strengthened**: Eliminated WEP (Wired Equivalent Privacy) as an acceptable wireless encryption protocol. WEP was deemed cryptographically broken. Required WPA or stronger (802.11i/WPA2)
- Requirement to change default wireless encryption keys at installation
- Clarified requirement to not use vendor-supplied defaults (Req 2.1) — expanded guidance on what constitutes a "vendor default"
- Improved physical security guidance for POI devices (early version of what became Req 9.9)
- Refined vulnerability scanning requirements (internal and external)
- Clarified that all system components with a connection to the CDE are in scope (connected-to criterion formalised)
- Removed ambiguous language and improved consistency throughout

---

## PCI DSS v1.2.1 (July 2009)

**Status**: Retired

### Key changes from v1.2
- Corrections to typographical errors and ambiguous language in v1.2
- No new requirements added
- No substantive technical changes

---

## PCI DSS v2.0 (October 2010)

**Status**: Retired

### Key changes from v1.2.1
- **Virtualisation guidance added**: Addressed systems sharing a physical host — if virtual machines and virtual components are part of the CDE, they are in scope. Clarified that hypervisors and management planes are in scope if they impact CDE security
- **Clarification-focused revision**: Primary goal was to clarify intent of existing requirements, not add new ones
- Strengthened scoping guidance: confirmed that all components in the CDE network segment are in scope unless adequate segmentation is in place
- Reinforced the requirement to document all allowed ports and services with a business justification
- Enhanced guidance on penetration testing methodology — confirmed both internal and external testing required
- Clarified that wireless networks that interact with the CDE or transmit cardholder data are in scope regardless of physical location
- Updated SAQ types: introduced SAQ A-EP concept precursor; refined eligibility criteria

---

## PCI DSS v3.0 (November 2013)

**Status**: Retired

### Key changes from v2.0

**Structural theme**: Shift toward "security as a business-as-usual activity" — requirements framed to promote embedding security into daily business operations rather than treating compliance as a point-in-time exercise.

**Major new requirements:**
- **Req 9.9**: Protect devices that capture payment card data via direct physical interaction from tampering and substitution. Merchants required to maintain a list of POI devices, inspect devices regularly, and train staff to detect tampering — a direct response to the dramatically increased incidence of card skimming
- **Req 11.3**: Penetration testing requirements significantly clarified. Required both internal and external penetration testing; required testing after significant infrastructure or application changes; introduced the concept of segmentation validation (testing that CDE isolation controls work)
- **Req 12.8.5**: Requirements for managing service providers — organisations must maintain a list of all service providers with whom they share cardholder data, and have a written agreement in place acknowledging the service provider's responsibility to protect the data

**Important clarifications:**
- Password policy: Minimum complexity requirements clarified — passwords must contain both numeric and alphabetic characters (was always implied, now explicit)
- Malware: Clarified that all systems capable of being affected by malware must have anti-malware installed — not just Windows; Unix/Linux systems must be evaluated
- Application security: Clarified that all public-facing web applications must be protected either by a WAF or by annual application security assessment

**SAQ changes in v3.0:**
- Introduced **SAQ B-IP** (standalone IP-connected PTS POI devices)
- Introduced **SAQ P2PE** (validated P2PE solutions)

---

## PCI DSS v3.1 (April 2015)

**Status**: Retired

### Key changes from v3.0

**Primary driver**: Response to known vulnerabilities in SSL (all versions) and TLS 1.0. These protocols were proven cryptographically inadequate following the POODLE vulnerability (October 2014) and broader research.

**Major changes:**
- **SSL and TLS 1.0 deprecated**: SSL and early TLS (TLS 1.0) deemed not strong cryptography and prohibited for protection of cardholder data in transit
- Migration timelines established:
  - **Service providers**: Must complete migration from SSL/TLS 1.0 by **June 30, 2016**
  - **All other entities**: Originally by June 30, 2016, extended to June 30, 2018 in v3.2
- TLS 1.1 and TLS 1.2 identified as acceptable (TLS 1.2 preferred)
- Clarified that TLS 1.2 is the minimum acceptable strong cryptography standard for new implementations

**Impact**: v3.1 had a narrow but high-impact scope — it required organisations to audit and migrate all SSL/TLS 1.0 implementations protecting cardholder data in transit. This was significant for many web applications, APIs, and internal service-to-service communications.

---

## PCI DSS v3.2 (April 2016)

**Status**: Retired

### Key changes from v3.1

**Structural theme**: Strengthened requirements for service providers; expanded multi-factor authentication; incorporated Designated Entities Supplemental Validation (DESV).

**Major new or expanded requirements:**

**Multi-factor authentication (MFA) — expanded scope:**
- MFA was previously required for remote access from outside the entity's network and for non-console admin access
- **v3.2 added**: MFA required for all non-console administrative access into the CDE for all personnel (not just remote access) — effective immediately for new implementations, phased in by February 1, 2018 for existing implementations
- This was a significant expansion that affected internal administrators accessing CDE systems from within the network via console

**Service provider-specific requirements added:**
- **Req 3.5.1** (service providers): Maintain a documented description of the cryptographic architecture
- **Req 10.8** (service providers only): Implement a process for the timely detection and reporting of failures of critical security control systems (IDS, FIM, AV, physical access controls, audit logs). Respond to failures within one business day
- **Req 10.8.1** (service providers only): Respond to failures of any critical security controls within timeframes specified in the requirement
- **Req 12.11** (service providers only): Perform reviews at least quarterly to confirm personnel are following security policies and operational procedures

**Appendix A3 — Designated Entities Supplemental Validation (DESV):**
- DESV incorporated as a formal appendix. DESV applies to entities designated by a payment card brand or acquirer as requiring DESV validation in response to a breach or risk exposure
- DESV adds controls around executive oversight, business as usual (BAU) activities, documentation, and responsibility assignment

**Other changes:**
- **Req 6.4.6** (new): Upon completion of a significant change, all relevant PCI DSS requirements must be implemented on all new or changed systems and networks, and documentation updated accordingly
- Clarifications to penetration testing scope
- Best practice recommendations for multi-tenant hosting providers

---

## PCI DSS v3.2.1 (May 2018)

**Status**: **RETIRED March 31, 2024** — the last release in the v3.x series

### Key changes from v3.2
- Corrections only — no new requirements added or removed
- Updated language around the SSL/TLS migration deadline:
  - June 30, 2018 migration deadline for all entities confirmed (previously June 30, 2016 for service providers, June 30, 2016/extended for merchants)
  - After June 30, 2018, SSL and TLS 1.0 are not permitted to protect cardholder data in transit
  - Entities that relied on compensating controls for SSL and TLS 1.0 must complete migration
- Clarification of terminology throughout
- Minor editorial corrections

### Operational relevance
- v3.2.1 is the most commonly encountered legacy version in gap documentation, prior-year assessment records, and migration planning
- All entities that conducted PCI DSS assessments between May 2018 and March 31, 2024 used v3.2.1
- For v3.2.1 → v4.0.1 migration guidance, consult `references/pci-dss-v4-changes.md`
- For the v3.2.1 control structure, consult `references/pci-dss-v3-controls.md`

---

## PCI DSS v4.0 (March 2022)

**Status**: Superseded by v4.0.1 (June 2024); v4.0 is no longer the current version

### Key changes from v3.2.1

PCI DSS v4.0 was the most significant revision since v1.0. It introduced a fundamentally new compliance philosophy alongside new and expanded technical requirements.

**Structural changes:**
- Requirements count increased from 259 (v3.2.1) to 300+ sub-requirements
- Two compliance approaches formalised: **Defined Approach** and **Customised Approach**
- **Targeted Risk Analysis (TRA)** elevated to a formalised requirement for customised controls and several defined controls with flexible frequencies
- Informative references moved to the online PCI SSC Reference Tool (no longer embedded in the standard document)
- Greater emphasis on outcomes-based security rather than prescriptive controls

**Customised Approach:**
- For the first time, organisations can implement alternative controls designed to meet the stated **Objective** of a requirement (rather than following the defined testing procedure)
- Requires: TRA per customised control; senior management approval; QSA assessment using Customised Approach Test Plan (CATP); annual review
- Not available for SAQ A or SAQ B; intended for mature organisations and ROC-level assessments

**New concept — future-dated requirements:**
- v4.0 introduced a two-phase approach: requirements effective immediately on March 31, 2024, and "future-dated" requirements (best practice from March 2022, **mandatory from March 31, 2025**)

**Key new/expanded requirements (see `references/pci-dss-v4-changes.md` for full list):**
- **Req 8.4.2**: MFA required for ALL access into the CDE (not just admin/remote)
- **Req 5.4.1**: Automated technical solution required to detect and protect against phishing
- **Req 6.4.3**: All scripts on payment pages must be inventoried, authorised, and integrity-protected
- **Req 11.6.1**: Change and tamper detection for HTTP headers and payment page content
- **Req 10.4.1.1**: Automated log review mechanisms required (manual daily review no longer sufficient)
- **Req 8.3.6**: Passwords minimum 12 characters
- **Req 6.3.2**: Software inventory (SBOM) for bespoke software
- **Req 10.7**: Monitoring for failures of critical security controls

---

## PCI DSS v4.0.1 (June 2024) — CURRENT

**Status**: CURRENT — all new assessments must use v4.0.1

### Key changes from v4.0
- **Errata corrections only** — no new technical requirements added, no requirements removed
- Corrected typographical errors, clarified ambiguous wording, and fixed inconsistencies in v4.0
- Clarified the intent of several testing procedures that were interpreted inconsistently
- Updated the ROC Reporting Template to align with corrections
- All new and existing assessments should reference v4.0.1

**All "future-dated" requirements from v4.0 became mandatory on March 31, 2025.**

---

## Dates and Milestones Reference

| Date | Milestone |
|------|-----------|
| December 2004 | PCI DSS v1.0 published |
| September 2006 | PCI SSC founded; PCI DSS v1.1 published |
| October 2008 | PCI DSS v1.2 published; WEP prohibited |
| July 2009 | PCI DSS v1.2.1 published |
| October 2010 | PCI DSS v2.0 published |
| November 2013 | PCI DSS v3.0 published; SAQ B-IP and P2PE added |
| April 2015 | PCI DSS v3.1 published; SSL/TLS 1.0 deprecation announced |
| June 30, 2016 | SSL/TLS 1.0 migration deadline for service providers (v3.1/v3.2) |
| April 2016 | PCI DSS v3.2 published; MFA expansion; service provider requirements added |
| February 1, 2018 | v3.2 MFA expansions became mandatory for existing implementations |
| June 30, 2018 | SSL/TLS 1.0 migration deadline for all entities |
| May 2018 | PCI DSS v3.2.1 published (last v3.x release) |
| March 2022 | PCI DSS v4.0 published |
| March 31, 2024 | PCI DSS v3.2.1 **RETIRED** — all assessments must use v4.0 or v4.0.1 |
| June 2024 | PCI DSS v4.0.1 published (current) |
| March 31, 2025 | All "future-dated" v4.0 requirements became **mandatory** |

---

## Version Selection for Assessments

**Which version applies to a new or current PCI DSS assessment?**
- For any formal compliance assessment today: **PCI DSS v4.0.1**
- v3.2.1 was retired March 31, 2024 — it is not valid for any live assessment

**When would an older version be referenced (non-assessment purposes)?**
- Historical documentation review (prior-year ROC/SAQ, audit records)
- Migration gap analysis: comparing what was in scope under v3.2.1 vs v4.0.1
- Reviewing evidence from an assessment conducted before March 31, 2024
- Understanding what controls were implemented in a specific past period

**If an organisation's last assessment was under v3.2.1:**
- Their next assessment is under v4.0.1
- They must implement all v4.0.1 requirements, including those that became mandatory on March 31, 2025
- Consult `references/pci-dss-v4-changes.md` for the migration checklist

---

## Key Thresholds by Version — Authentication Requirements

| Requirement | v1.x–v2.0 | v3.0–v3.2.1 | v4.0 / v4.0.1 |
|-------------|-----------|------------|--------------|
| MFA — remote access | Required since v1.x (as two-factor auth) | Required | Required |
| MFA — non-console admin | Not explicitly required | Required (v3.2+) | Required |
| MFA — all CDE access | Not required | Not required | **Required (Req 8.4.2)** |
| Password minimum length | 7 characters | 7 characters | 12 characters |
| Password complexity | Numeric + alpha required | Numeric + alpha required | Numeric + alpha required (or passphrase alternative) |
| Session timeout | 15 minutes | 15 minutes | Unchanged |
| Account lockout threshold | 6 attempts | 6 attempts | 10 attempts |

---

## Key Thresholds by Version — Cryptography

| Topic | v1.x–v2.0 | v3.0–v3.2.1 | v4.0 / v4.0.1 |
|-------|-----------|------------|--------------|
| Wireless encryption | WEP acceptable (v1.x); WEP prohibited from v1.2 | WPA / WPA2 required | WPA2-Enterprise or WPA3 required |
| SSL | Acceptable (v1.x–v3.0) | Prohibited from v3.1 (migration by June 2018) | Prohibited |
| TLS 1.0 | Acceptable | Prohibited from v3.1 | Prohibited |
| TLS 1.1 | Acceptable | Conditionally acceptable | Prohibited (best practice; strongly discouraged) |
| TLS 1.2 | Recommended | Required minimum for new implementations | Required minimum |
| TLS 1.3 | Not addressed | Not addressed | Supported / recommended |
| Key length (PAN encryption) | Strong cryptography | AES-128 or equivalent minimum | AES-128 or equivalent; AES-256 preferred |

---

## Glossary of Key Terms (Consistent Across All Versions)

| Term | Definition |
|------|-----------|
| **CDE** | Cardholder Data Environment — all systems, people, and processes that store, process, or transmit cardholder data or SAD, plus all connected components |
| **PAN** | Primary Account Number — the payment card number (up to 19 digits); the single element that brings a system into PCI DSS scope |
| **CHD** | Cardholder Data — PAN plus cardholder name, expiry date, and service code |
| **SAD** | Sensitive Authentication Data — full magnetic stripe content, CAV2/CVV2/CVC2/CID, PIN/PIN block; must never be stored after authorisation |
| **QSA** | Qualified Security Assessor — PCI SSC-certified company conducting ROC assessments |
| **ISA** | Internal Security Assessor — PCI SSC-certified individual conducting internal assessments |
| **ROC** | Report on Compliance — formal assessment report required for Level 1 merchants and Level 1 service providers |
| **SAQ** | Self-Assessment Questionnaire — self-validation tool for Level 2–4 merchants and Level 2 service providers |
| **AOC** | Attestation of Compliance — declaration of compliance status accompanying ROC or SAQ |
| **ASV** | Approved Scanning Vendor — PCI SSC-certified vendor performing external vulnerability scans |
| **P2PE** | Point-to-Point Encryption — end-to-end encryption of cardholder data from POI device to decryption point |
| **Tokenisation** | Replacing PAN with a non-sensitive surrogate value (token) that has no exploitable value |
| **TRA** | Targeted Risk Analysis — formalised risk analysis process introduced in v4.0 |
| **TPSP** | Third-Party Service Provider — any entity that stores, processes, or transmits cardholder data on behalf of another entity |
| **CCW** | Compensating Control Worksheet — documentation for compensating controls in ROC/SAQ |

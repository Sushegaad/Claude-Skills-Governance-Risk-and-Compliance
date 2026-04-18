# DORA — Adopted RTS and ITS Reference Guide

All Level 2 measures adopted under Regulation (EU) 2022/2554 (DORA).
Last updated: April 2026.

---

## Overview

DORA empowers the European Supervisory Authorities (EBA, ESMA, EIOPA — collectively
the ESAs) to develop binding Regulatory Technical Standards (RTS) and Implementing
Technical Standards (ITS) under Articles 15, 16, 18, 20, 26, 28, 29, 30, 31, 32,
41, and 43. All key standards were adopted before the DORA application date of
17 January 2025.

---

## Complete List of Adopted RTS and ITS

### 1. CDR (EU) 2024/1772 — RTS on ICT Incident Classification

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2024/1772 of 13 March 2024 |
| DORA basis | Art. 18(3) — classification criteria and materiality thresholds |
| Published | OJ L, 25 June 2024 |
| Applies from | 17 January 2025 |

**Key content:**
- Defines materiality thresholds for each Art. 18(1) criterion (clients affected,
  transaction value, data loss, service unavailability, geographic spread)
- An incident is classified as **major** if any single threshold is met (OR logic)
- Sets minimum thresholds for "significant cyber threats" that may trigger voluntary
  reporting under Art. 19(2)
- Includes specific rules for payment-related incidents (Art. 23)

**Thresholds (indicative — consult the CDR for exact values):**
- Client impact: ≥ 10% of clients (or >5,000 clients for large entities)
- Transaction value: depending on institution type and size
- Service unavailability: ≥ 2 hours for critical services
- Data integrity/confidentiality: any breach affecting core banking data

---

### 2. CDR (EU) 2024/1773 — RTS on ICT Third-Party Risk Policy

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2024/1773 of 13 March 2024 |
| DORA basis | Art. 28(10) — content of the ICT third-party risk policy; Art. 30(5) — contractual provisions |
| Published | OJ L, 25 June 2024 |
| Applies from | 17 January 2025 |

**Key content:**
- Minimum elements of the ICT third-party risk policy (Art. 28(1) policy)
- Criteria for distinguishing critical/important functions from non-critical
- Due diligence requirements before entering ICT service arrangements
- Detailed requirements for contractual provisions under Art. 30(2):
  - Service level descriptions and measurable KPIs
  - Provisions on data location, portability, and return on exit
  - Audit and access rights (the auditor clause must be specific and exercisable)
  - Exit strategy and minimum notice period requirements
  - Sub-contracting provisions and prior consent requirements

---

### 3. CDR (EU) 2024/1774 — RTS on ICT Risk Management Framework

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2024/1774 of 13 March 2024 |
| DORA basis | Art. 15 — elements of ICT RMF; Art. 16(3) — simplified framework |
| Published | OJ L, 25 June 2024 |
| Applies from | 17 January 2025 |

**Key content:**
- Chapter I: Detailed elements of the ICT risk management framework (Art. 6–14):
  - ICT risk strategy requirements
  - Minimum content of ICT security policies
  - ICT asset identification and classification requirements
  - Protection and prevention controls (logical and physical)
  - Detection, response, recovery, and backup policy requirements
  - Learning and communication requirements
- Chapter II: Simplified ICT risk management framework (Art. 16):
  - Entity types eligible for the simplified framework
  - Minimum requirements for simplified framework entities
  - How to document the simplified framework

---

### 4. CDR (EU) 2025/301 — RTS on Major Incident Reporting

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2025/301 of 18 October 2024 |
| DORA basis | Art. 20(3) — content, timelines, and format of incident reports |
| Published | OJ L, 14 February 2025 |
| Applies from | 17 January 2025 (retroactively applicable) |

**Key content:**
- Mandatory content of each reporting stage:
  - **Initial notification (within 4 hours):** Incident reference, entity details,
    initial classification rationale, estimated client impact, nature of incident
  - **Intermediate report (within 72 hours):** Updated impact assessment, root cause
    indicators, response actions taken, recovery time estimate
  - **Final report (within 1 month):** Root cause analysis, full impact assessment,
    lessons learned, preventive measures implemented or planned
- Rules on how to count the 4-hour and 72-hour timelines from classification
- Provisions for voluntary reporting of significant cyber threats (Art. 19(2))

---

### 5. CIR (EU) 2025/302 — ITS on Incident Reporting Templates

| Field | Detail |
|-------|--------|
| Full title | Commission Implementing Regulation (EU) 2025/302 of 18 October 2024 |
| DORA basis | Art. 20(4) — standard forms and templates for incident reports |
| Published | OJ L, 14 February 2025 |
| Applies from | 17 January 2025 (retroactively applicable) |

**Key content:**
- Standard templates for all three reporting stages (initial, intermediate, final)
- **Dedicated payment-incident template** per Art. 23 for credit institutions,
  payment institutions, and e-money institutions — aligned with legacy PSD2 Art. 96
  reporting fields
- Separate template for voluntary cyber threat notifications (Art. 19(2))
- Electronic submission format requirements
- Competent authority designation — which authority receives reports for each
  entity type (home state supervisor as a general rule)

---

### 6. CIR (EU) 2024/2956 — ITS on Register of Information

| Field | Detail |
|-------|--------|
| Full title | Commission Implementing Regulation (EU) 2024/2956 of 20 September 2024 |
| DORA basis | Art. 28(9) — templates for the Register of Information |
| Published | OJ L, 11 December 2024 |
| Applies from | 17 January 2025 |

**Key content — mandatory Register fields:**

The Register of Information (RoI) must capture, for each ICT service arrangement:

| Field Group | Key Fields |
|-------------|-----------|
| Entity information | LEI of reporting entity, entity name, entity type |
| TPSP identification | TPSP LEI, TPSP name, country of establishment |
| Arrangement details | Unique arrangement reference, arrangement type |
| Function classification | Critical or important function (Y/N), function description |
| ICT service description | Type of service (IaaS/PaaS/SaaS/other), specific service description |
| Data | Types of data processed, storage location (country/region) |
| Sub-processors | Chain of sub-processors (name, LEI, country) |
| Contractual terms | Contract start date, contract end date, notice period |
| Substitutability | Assessment of ease of substitution (high/medium/low) |
| Exit strategy | Reference to exit strategy document |

**Annual submission:** The RoI is submitted to the competent authority at least
annually (or upon request). The ESAs aggregate submissions for the oversight framework.

---

### 7. CDR (EU) 2025/1190 — RTS on TLPT

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2025/1190 of 28 February 2025 |
| DORA basis | Art. 26(11) and Art. 27(9) — TLPT requirements, tester qualifications |
| Published | OJ L, 18 June 2025 |
| Applies from | 8 July 2025 |

**Key content:**
- Criteria for identifying financial entities required to conduct TLPT (Art. 26(8))
- Scope determination: which functions and ICT systems must be included
- Role of competent authority in approving TLPT scope and methodology
- Requirements for the **threat intelligence phase**: accreditation of threat
  intelligence providers
- Requirements for **red team testing**: methodology, documentation, attestation
- **Mutual recognition:** TLPT results recognized across EU jurisdictions for
  entities operating cross-border — only one test needed (Art. 26(5))
- Tester qualification requirements per Art. 27:
  - Independence from the tested entity
  - Relevant professional certification
  - Risk methodology capability
- **TIBER-EU alignment:** The CDR aligns TLPT with the TIBER-EU framework;
  TIBER-EU tests conducted under the TIBER-EU framework may satisfy DORA
  TLPT requirements where conditions are met

---

### 8. CDR (EU) 2025/532 — RTS on Subcontracting of ICT Services

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2025/532 |
| DORA basis | Art. 30(5) — subcontracting provisions |
| Applies from | 17 January 2025 |

**Key content:**
- When a TPSP subcontracts ICT services supporting critical/important functions,
  the financial entity must ensure the contract includes:
  - Prior written consent of the financial entity for sub-contracting chains
  - Equivalent contractual provisions at sub-processor level
  - Right to audit the sub-processor (directly or via the TPSP)
- Conditions under which financial entities may apply pre-approved sub-contracting
  arrangements (framework sub-contracting clauses)
- Notification requirements for changes in sub-processors

---

### 9. CDR (EU) 2024/1502 — Designation Criteria for Critical ICT TPSPs

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2024/1502 of 22 February 2024 |
| DORA basis | Art. 31(6) — criteria for designation of critical ICT TPSPs |
| Published | OJ L, 5 June 2024 |
| Applies from | 17 January 2025 |

**Key content — designation criteria:**
- **Systemic impact:** Would failure or discontinuation of the TPSP's services
  cause systemic disruption to the financial system?
- **Scale:** Number and types of financial entities served; proportion of their
  ICT needs
- **Substitutability:** How easily could another TPSP replace the service?
  (Low substitutability → higher probability of designation)
- **Interconnectedness:** Does the TPSP's failure trigger cascading effects?
- **Concentration risk:** Does a large portion of EU financial entities rely
  on this single TPSP for critical functions?

**Designation process:** ESAs assess all ICT TPSPs that provide services to
EU financial entities and publish a list of designated CTPPs. TPSPs not
established in the EU that provide services to EU financial entities must
designate an EU legal representative (Art. 31(11)).

---

### 10. CDR (EU) 2024/1505 — Oversight Fees for Critical ICT TPSPs

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2024/1505 of 22 February 2024 |
| DORA basis | Art. 43(2) — methodology for calculating oversight fees |
| Published | OJ L, 5 June 2024 |
| Applies from | 17 January 2025 |

**Key content:**
- Fee methodology: annual oversight fee for designated CTPPs
- Based on: total worldwide annual net turnover of the CTPSP
- Fee caps and floors to ensure proportionality
- Fee collection process via Lead Overseer

---

### 11. CDR (EU) 2025/295 — RTS on Oversight Activities Harmonisation

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2025/295 |
| DORA basis | Art. 41(7) — harmonisation of oversight activities |
| Applies from | 17 January 2025 |

**Key content:**
- How Lead Overseers coordinate with Joint Oversight Network (JON)
- Information sharing between ESAs and national competent authorities
- Procedures for issuing oversight recommendations
- Follow-up process for non-compliance with recommendations

---

### 12. CDR (EU) 2025/420 — RTS on Joint Examination Teams (JETs)

| Field | Detail |
|-------|--------|
| Full title | Commission Delegated Regulation (EU) 2025/420 |
| DORA basis | Art. 32 — structure and operation of Joint Examination Teams |
| Applies from | 17 January 2025 |

**Key content:**
- Composition of JETs: lead overseer staff + national competent authority experts
- JET mandate: on-site and off-site examination of designated CTPPs
- Coordination between JET lead and national experts
- Reporting of JET findings to Lead Overseer

---

## Quick Reference: DORA Article → RTS/ITS

| DORA Article | Obligation | Implementing Measure |
|-------------|-----------|---------------------|
| Art. 15 | ICT RMF detailed elements | CDR (EU) 2024/1774 |
| Art. 16(3) | Simplified RMF | CDR (EU) 2024/1774 (Ch. II) |
| Art. 18(3) | Incident classification thresholds | CDR (EU) 2024/1772 |
| Art. 20(3) | Incident reporting content + timelines | CDR (EU) 2025/301 |
| Art. 20(4) | Incident reporting templates | CIR (EU) 2025/302 |
| Art. 26(11) | TLPT requirements | CDR (EU) 2025/1190 |
| Art. 27(9) | Tester qualifications | CDR (EU) 2025/1190 |
| Art. 28(9) | Register of Information templates | CIR (EU) 2024/2956 |
| Art. 28(10) + 30(5) | ICT third-party risk policy + contracts | CDR (EU) 2024/1773 |
| Art. 30(5) | Subcontracting provisions | CDR (EU) 2025/532 |
| Art. 31(6) | Critical TPSP designation criteria | CDR (EU) 2024/1502 |
| Art. 32 | Joint Examination Teams (JETs) | CDR (EU) 2025/420 |
| Art. 41(7) | Oversight activities harmonisation | CDR (EU) 2025/295 |
| Art. 43(2) | Oversight fees for CTPPs | CDR (EU) 2024/1505 |

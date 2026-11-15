# DORA - ICT Third-Party Risk Management Reference

Chapter V, Articles 28–44, Regulation (EU) 2022/2554.
Key implementing measures: CDR (EU) 2024/1773, CIR (EU) 2024/2956, CDR (EU) 2025/532,
CDR (EU) 2024/1502, CDR (EU) 2024/1505, CDR (EU) 2025/295, CDR (EU) 2025/420.

---

## Overview: Two-Track Structure

Chapter V operates on two parallel tracks:

**Track 1 - Entity-level obligations (Art. 28–30):**
Every financial entity must manage its own ICT third-party risks - regardless of
whether its TPSPs are designated critical.

**Track 2 - Systemic oversight of designated CTPPs (Art. 31–44):**
ESAs designate and oversee ICT TPSPs that are systemically important to the
EU financial sector. This is a supervisory regime, not an entity-level compliance task.

---

## Art. 28 - General Principles for ICT Third-Party Risk

### Art. 28(1) - ICT Third-Party Risk Policy
Every financial entity must adopt, regularly review, and update an **ICT third-party
risk policy** covering:
- Objectives and principles for managing ICT third-party risk
- Criteria for identifying critical and important functions (CIF) vs. non-critical
- Pre-contractual due diligence requirements
- Contract lifecycle management (onboarding, monitoring, exit)
- ICT concentration risk management
- Governance roles and responsibilities

**Key RTS:** CDR (EU) 2024/1773, Art. 1–12 (detailed policy content)

### Art. 28(3) - Register of Information: Maintenance and Annual Submission
Financial entities must maintain and update the **Register of Information** (RoI)
covering **all** ICT service arrangements (not only those supporting critical
functions), and must submit it to the competent authority **at least annually**
and upon specific request. Both RoI duties (maintenance and annual submission)
sit in Art. 28(3). The submission format follows CIR (EU) 2024/2956 templates.
See the Register of Information section below for full field details.

### Art. 28(4) - Pre-Contractual Due Diligence
Before entering any new ICT service arrangement supporting a critical or important
function, financial entities must:
- **(a)** Assess whether the ICT service arrangement supports a critical or important function
- **(b)** Carry out appropriate due diligence on prospective ICT TPSPs
- **(c)** Assess the **ICT concentration risk** of the arrangement; this is
  where the entity-level concentration risk duty sits (Art. 28(4)(c); see also
  Art. 29)

The due diligence must be documented and commensurate with the criticality of
the function.

### Art. 28(5) - Ongoing Monitoring of ICT TPSPs
- Monitor the performance, security posture, and compliance of ICT TPSPs
  throughout the contract lifecycle
- Conduct regular reviews aligned with the contract terms and risk profile
- Verify that ICT TPSPs continue to meet agreed service levels and security standards

### ICT Concentration Risk Assessment (Art. 28(4)(c) and Art. 29)
Financial entities must:
- Assess the **concentration risk** arising from reliance on a single or limited
  number of ICT TPSPs for critical functions
- Determine whether the failure or unavailability of any TPSP would threaten the
  entity's ability to maintain critical functions
- Document this assessment and factor it into risk appetite and strategy

**Common scenario:** A bank using a single hyperscaler (e.g., one major cloud
provider) for core banking, treasury, and fraud detection creates high concentration
risk even if the TPSP is not designated critical.

### Art. 28(6) - Audit and Inspection Frequency
Financial entities must pre-determine the **frequency of audits and inspections**
of ICT TPSPs and the **areas to be audited or inspected**.

### Art. 28(7) - Termination Rights
Financial entities must ensure that ICT service arrangements can be
**terminated** in the circumstances required by DORA.

### Art. 28(8) - Exit Strategy
For each ICT arrangement supporting a critical or important function, financial entities must:
- Develop and maintain an **exit strategy** covering:
  - Conditions and triggers for exit
  - Minimum notice period required to migrate services
  - Data portability and return procedures
  - Transition assistance obligations of the departing TPSP
- Test exit strategies periodically (frequency: risk-based)

---

## Art. 29 - Preliminary Assessment of ICT Concentration Risk

Before entering a new arrangement that would cause an entity's concentration in
a single TPSP to increase for critical functions:
- Conduct a specific **concentration risk assessment**
- Document the assessment outcome and risk mitigation measures (if any)
- Consider the systemic implications if the concentrated TPSP were to fail

This is a transaction-specific obligation (triggered by entering a new arrangement)
that complements the pre-contractual concentration risk assessment at Art. 28(4)(c).

---

## Art. 30 - Key Contractual Provisions

### Scope: How Art. 30(2) and Art. 30(3) fit together

**Art. 30(2)** sets the baseline contractual elements (a)–(i) required in
contracts for **all** ICT services. **Art. 30(3)** adds, in addition, a stricter
set of provisions for contracts supporting **critical or important functions**:
full service level descriptions, unrestricted audit/access/inspection rights,
TLPT participation, and exit strategies with a mandatory transition period
(Art. 30(3)(f)).

### Critical or Important Function (CIF)

A function is critical or important if its disruption would:
- Materially impair the financial entity's compliance with legal obligations
- Materially impair its financial performance, or
- Materially impair the soundness or continuity of its services

The criteria for identifying CIF are further specified in CDR (EU) 2024/1773.

### Baseline Contractual Elements - Art. 30(2)(a)–(i) (all ICT contracts)

Art. 30(2) requires baseline elements (a)–(i) in **every** ICT service contract,
covering matters such as:

- Clear and complete description of the ICT services
- Locations where services are provided and data is stored/processed, with
  notification obligations if locations change
- Data protection provisions; compliance with applicable data protection law
  (GDPR where applicable)
- Availability, authenticity, integrity, and security of data
- Incident reporting and monitoring cooperation by the TPSP
- Termination rights and minimum notice periods
- Data portability, return, and migration assistance on termination
- Conditions for sub-contracting

### Additional Provisions for Critical or Important Functions - Art. 30(3)

In addition to the Art. 30(2) baseline, contracts supporting critical or
important functions must include:

| Provision | DORA Requirement |
|-----------|-----------------|
| Full service level descriptions | Complete SLAs with precise quantitative and qualitative performance targets |
| Audit, access, and inspection rights | **Unrestricted** rights of access, inspection, and audit for the financial entity, its competent authorities (including ECB for significant institutions), and resolution authorities, including on-site inspection rights at the TPSP's premises |
| TLPT participation | The TPSP participates in the entity's threat-led penetration testing |
| Exit strategies | Exit strategies with a **mandatory transition period** (Art. 30(3)(f)) |

**Key RTS:** CDR (EU) 2024/1773 specifies the detailed content of each provision.
**Key RTS:** CDR (EU) 2025/532 specifies sub-contracting provisions in detail.

### The Audit Rights Problem (Art. 30(3))

The most common contractual gap: large cloud providers offer only third-party
audit reports (e.g., SOC 2, ISO 27001 certificates) rather than direct audit
rights. For critical or important functions, DORA Art. 30(3) requires:
- **Full and unrestricted** audit rights for the financial entity
- **Access rights for competent authorities** - including the right to inspect
  the TPSP's premises

ESA guidance has clarified that:
- Pooled or third-party audits (SOC 2, ISO 27001 certification) may partially
  satisfy the **entity's own audit right** where direct audit is genuinely
  impracticable at hyperscale TPSPs - but only if the entity documents in writing
  why direct audit is impracticable and confirms the pooled audit outputs are
  meaningful and sufficient
- Financial entities must still document their assessment of why pooled audits
  are acceptable and ensure they receive meaningful, entity-specific outputs
- **The competent authority's (and resolution authority's) on-site inspection
  right under Art. 30(3) is NON-WAIVABLE.** Even where the entity accepts
  pooled audits, the contract must contain an express, unconditional clause
  preserving the competent authority's right to inspect the TPSP's premises
  directly. A clause that routes the authority's access through the TPSP's
  third-party audit programme does NOT satisfy Art. 30(3). This is a common
  failure in standard cloud provider contracts.
- Acceptance of pooled audits must be documented with a written risk acceptance
  approved at an appropriate governance level (e.g., CRO or board)

### Non-Critical Arrangements

For ICT service arrangements that do not support critical or important
functions, the Art. 30(2) baseline elements (a)–(i) still apply. Only the
additional Art. 30(3) provisions (full SLAs, unrestricted audit/access/
inspection rights, TLPT participation, exit strategies with transition period)
are limited to critical or important function contracts.

### Art. 30(4) - Review Before Renewal

Before renewing any contract for ICT services supporting critical functions,
financial entities must review whether:
- Service levels remain adequate
- Audit and access rights remain exercisable
- Exit strategy remains viable
- New risks (concentration, substitutability) have emerged

---

## Register of Information - Complete Field Reference (CIR (EU) 2024/2956)

### When to Maintain and Submit

- **Ongoing maintenance:** Update when new arrangements are entered, modified,
  or terminated; when sub-processors change; when data locations change
- **Annual submission:** At least annually to the competent authority
- **On-demand submission:** Upon specific request from competent authority or ESA
  (for the oversight framework of CTPPs under Art. 31)

### Complete Field Set

The RoI is structured around **arrangements** - each row represents one ICT
service arrangement.

| Field | Field Name (CIR 2024/2956) | Description |
|-------|---------------------------|-------------|
| 1 | Reporting entity LEI | Legal Entity Identifier of the financial entity |
| 2 | Reporting entity name | Legal name |
| 3 | Reporting entity type | Regulated entity type (credit institution, insurer, etc.) |
| 4 | Arrangement reference | Unique internal reference for this arrangement |
| 5 | Arrangement type | Type (outsourcing, SaaS, IaaS, PaaS, data services, etc.) |
| 6 | TPSP legal name | Legal name of the ICT third-party service provider |
| 7 | TPSP LEI | LEI of the TPSP |
| 8 | TPSP country of establishment | Country (ISO 3166-1 alpha-2) |
| 9 | TPSP within group? | Is the TPSP part of the same corporate group as the entity? |
| 10 | ICT service type | Nature of services (per CIR classification codes) |
| 11 | ICT service description | Free-text description of specific services |
| 12 | Critical or important function (CIF)? | Y/N - does this arrangement support a CIF? |
| 13 | Function identifier | Reference to the function(s) supported |
| 14 | Function description | Description of the supported function |
| 15 | Data types processed | Classification of personal/non-personal data processed |
| 16 | Data sensitivity | Sensitivity level of data (e.g., customer PII, financial data) |
| 17 | Primary data storage location | Country(ies) where data is primarily stored |
| 18 | Secondary/backup data storage location | Country(ies) where backup data is stored |
| 19 | Contract start date | Effective date of the arrangement |
| 20 | Contract end date or rolling | End date or indication of indefinite/rolling |
| 21 | Notice period for termination | Minimum notice period (in days) |
| 22 | Sub-processors used? | Y/N - does the TPSP sub-contract any services? |
| 23 | Sub-processor names and LEIs | Name and LEI of each sub-processor |
| 24 | Sub-processor data locations | Country(ies) of data processing by sub-processors |
| 25 | Substitutability assessment | High / Medium / Low - ease of replacing this TPSP |
| 26 | Exit strategy reference | Reference to the exit strategy document for this arrangement |
| 27 | Last due diligence date | Date of most recent due diligence assessment |
| 28 | Audit rights exercisable? | Y/N - can audit rights be exercised per contract? |
| 29 | Audit method | Direct audit / pooled audit / third-party certification |

### Register of Information - Key Points

1. **All arrangements, not just critical ones.** The RoI covers every ICT service
   arrangement, not only those supporting critical or important functions. The
   criticality flag (field 12) distinguishes them within the register.

2. **Sub-processors must be captured.** For each arrangement, the full chain of
   sub-processors must be identified (fields 22–24). This is frequently incomplete
   in practice.

3. **Not a static document.** The RoI must be updated throughout the year as
   arrangements change; the annual submission is a snapshot of the current state.

4. **LEIs are mandatory.** Both the reporting entity and all TPSPs must have LEIs.
   Where a TPSP does not have an LEI, the entity should document this and use
   the TPSP's national business registration number as an alternative.

---

## ICT Concentration Risk - Practical Assessment

### What constitutes concentration risk under DORA?

**Horizontal concentration:** Multiple critical functions supported by a single TPSP
(e.g., core banking, fraud detection, and AML all on the same cloud provider).

**Sectoral concentration:** Many financial entities within the EU using the same
TPSP for critical functions - creating systemic risk even if each entity's own
dependency appears manageable.

**Geographic concentration:** All data and processing in a single geographic region
or data centre cluster, creating correlated failure risk.

### Concentration Risk Assessment Template

For each TPSP supporting critical functions, assess:

| Assessment Area | Question | Rating (H/M/L) |
|----------------|----------|----------------|
| Dependency depth | How many critical functions depend on this TPSP? | |
| Substitutability | Could this service be replaced within the entity's recovery time objectives? | |
| Contractual exit | Is there a viable exit path with adequate notice period and data portability? | |
| Financial stability | Is there material risk of the TPSP becoming insolvent or discontinuing the service? | |
| Geographic diversification | Are services provided from geographically diverse infrastructure? | |
| Regulatory enforceability | Are audit and competent authority access rights practically exercisable? | |

A TPSP rated High on any two or more areas should be treated as a concentration
risk concern requiring mitigation action.

---

## Oversight Framework for Critical ICT TPSPs (Art. 31–44)

### Designation of Critical ICT TPSPs (Art. 31)

ESAs (EBA, ESMA, EIOPA) jointly designate ICT TPSPs as **critical** based on
CDR (EU) 2024/1502 criteria. The designation process:

1. Financial entities submit their RoI annually
2. ESAs aggregate RoI data to map TPSP dependencies across the EU financial sector
3. ESAs apply CDR 2024/1502 criteria to assess systemic importance
4. Designated CTPPs are notified and published
5. ICT TPSPs not established in the EU that serve EU financial entities must
   designate an EU-established legal representative (Art. 31(11))

### Lead Overseer Assignment (Art. 32)

Each designated CTPSP is assigned a **Lead Overseer** - one of EBA, ESMA, or EIOPA
- based on the predominant type of financial entity served. The Lead Overseer
coordinates with other ESAs via the **Joint Oversight Network (JON)**.

**Joint Examination Teams (JETs):** Per Art. 40(1) and CDR (EU) 2025/420, JETs are assembled
from Lead Overseer and national authority staff to conduct on-site and off-site
examinations of CTPPs.

### Oversight Tasks and Powers (Art. 33–43)

| Article | Description |
|---------|-------------|
| Art. 33 - Tasks of the Lead Overseer | Tasks of the Lead Overseer for its assigned CTPPs |
| Art. 34 - Operational coordination | Operational coordination between Lead Overseers |
| Art. 35 - Powers of the Lead Overseer | Lead Overseer powers, including issuing recommendations (a power under Art. 35(1)(d)) |
| Art. 36 - Powers outside the Union | Exercise of the Lead Overseer's powers outside the Union |
| Art. 37 - Request for information | Lead Overseer can require CTPPs to provide information, data, and documents |
| Art. 38 - General investigations | Including interviews, document reviews |
| Art. 39 - Inspections | Physical inspection of CTPSP premises and systems |
| Art. 40 - Ongoing oversight | Ongoing oversight; joint examination teams under Art. 40(1) |
| Art. 42 - Follow-up by competent authorities | Competent authorities follow up on oversight outcomes for supervised entities |
| Art. 43 - Oversight fees | Annual fees per CDR (EU) 2024/1505 |

### What CTPSP Designation Means for Financial Entities

- **No direct obligations change** for the financial entity when its TPSP is
  designated critical - the entity's Art. 28–30 obligations apply regardless
- The Lead Overseer interacts with the **CTPSP directly**
- Financial entities must cooperate with information requests about their use
  of designated CTPPs (the Lead Overseer's information request power sits in
  Art. 37; competent authority follow-up in Art. 42)
- Financial entities should note that oversight recommendations to a CTPSP
  may result in changes to service terms - monitor this

---

## Contract Review Checklist - DORA Art. 30 Compliance

Use this checklist when reviewing existing contracts or negotiating new ones.
Art. 30(2) baseline elements apply to all ICT contracts; Art. 30(3) items apply
in addition to contracts supporting critical or important functions.

| Clause | Required by | Present? | Gap? |
|--------|------------|---------|------|
| Clear service description | Art. 30(2) baseline | | |
| Data location - primary and secondary | Art. 30(2) baseline | | |
| Change notification for data locations | Art. 30(2) baseline | | |
| GDPR/data protection provisions | Art. 30(2) baseline | | |
| Termination rights and minimum notice period | Art. 30(2) baseline | | |
| Incident reporting by TPSP to entity | Art. 30(2) baseline | | |
| Data portability, return, and migration assistance | Art. 30(2) baseline | | |
| Sub-contracting conditions | Art. 30(2) baseline + CDR 2025/532 | | |
| Full service level descriptions (SLAs) | Art. 30(3) - critical/important | | |
| Audit, access, and inspection rights - financial entity | Art. 30(3) - critical/important | | |
| Audit, access, and inspection rights - competent authority | Art. 30(3) - critical/important | | |
| Audit, access, and inspection rights - resolution authority | Art. 30(3) - critical/important | | |
| TLPT participation by the TPSP | Art. 30(3) - critical/important | | |
| Exit strategy with mandatory transition period | Art. 30(3)(f) - critical/important | | |
| Sub-processor change notification | CDR 2025/532 | | |

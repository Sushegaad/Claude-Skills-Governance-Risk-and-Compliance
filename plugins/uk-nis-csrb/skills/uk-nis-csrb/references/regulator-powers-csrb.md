# UK CSRB — Regulator Powers Reference
## Cyber Security and Resilience Bill: Enhanced Regulator and Competent Authority Powers

> **Important — Bill Status:** The CSRB regulatory powers described here are based on
> published DSIT policy intent and the Bill as introduced. Final provisions, delegated powers,
> and CA designations may differ following Royal Assent. Verify against enacted legislation.

---

## Overview

One of the most significant changes introduced by the Cyber Security and Resilience Bill is
the shift from primarily **reactive** regulatory oversight (as under NIS Regs 2018) to
**proactive** regulatory oversight. Competent Authorities gain new powers to audit, direct,
and obtain information from in-scope organisations before an incident occurs.

The key changes are:
1. **Proactive audit powers** — CAs can direct organisations to undergo security assessments
2. **Information-gathering powers** — CAs can require organisations to produce security information
3. **Expanded enforcement** — Enhanced financial penalties and recovery mechanisms
4. **Cross-CA coordination** — Improved information sharing between CAs and with DSIT/NCSC
5. **New regulators for new entities** — MSPs and data centres will have designated CAs

---

## Part 1 — NIS Regs 2018 vs CSRB Regulatory Architecture

### 1.1 Competent Authority Powers Comparison

| Power | NIS Regs 2018 | CSRB (Expected) |
|-------|---------------|-----------------|
| **Information gathering** | Reg 15: CA may require information from OES/DSP | Expanded: CA can require detailed security documentation, audit records, supply chain information |
| **Directed assessment** | Not available — CA must rely on organisation self-assessment | Expected: CA can commission and direct a third-party security assessment |
| **Scheduled audit** | Not available — inspections only following incident or concern | Expected: CA can schedule proactive audits of high-risk or critical organisations |
| **Enforcement notice** | Reg 17: CA can issue enforcement notice specifying required steps | Retained and expanded: more detailed step-down enforcement process |
| **Penalty — OES** | Reg 18: Up to £17 million | Expected: Revised (likely increased or restructured) |
| **Penalty — DSP** | Reg 21: Up to £17 million | Expected: Retained or restructured |
| **Penalty — MSP** | Not applicable (MSPs not in scope) | New: CSRB introduces penalty powers for MSPs |
| **Penalty — Data centres** | Not applicable | New: CSRB introduces penalty powers for qualifying data centres |
| **Cross-CA sharing** | Limited | Expected: Formal mechanism for CA-to-CA and CA-to-DSIT sharing |
| **International coordination** | Limited | Expected: Formal mechanism with international partners |

### 1.2 Regulatory Architecture Under CSRB (Expected)

```
DSIT (Department for Science, Innovation and Technology)
  |
  |-- Policy oversight
  |-- Receives national incident picture
  |-- Cross-CA coordination
  |-- Designates CAs for new entity types
  |
  +-- NCSC (National Cyber Security Centre)
  |     |
  |     |-- Technical authority / guidance
  |     |-- CAF and risk management guidance
  |     |-- Intelligence input to CA oversight
  |
  +-- Sectoral Competent Authorities
        |
        +-- OES / DSP (existing, per NIS Regs 2018 schedule)
        |     |-- Energy: BEIS/Ofgem
        |     |-- Transport: DfT / sector regulators
        |     |-- Health: DHSC / NHSE
        |     |-- Water: Drinking Water Inspectorate / SEPA / NRW
        |     |-- Digital (DSP): ICO
        |
        +-- MSPs: DSIT (expected primary CA)
        |
        +-- Data Centres: DSIT (expected designating authority)
```

---

## Part 2 — New Proactive Powers

### 2.1 Directed Security Assessments

Under the CSRB, CAs are expected to have power to direct an in-scope organisation to undergo
a security assessment carried out by a qualified third party or by the CA itself. This represents
a fundamental shift from self-assessment to externally directed assurance.

**Key aspects:**
- CA selects or approves the assessor
- Organisation bears the cost of the assessment
- Organisation must cooperate with the assessor and provide access to systems and documentation
- Assessment findings are reported to the CA

**Preparation steps for organisations:**
1. Maintain an up-to-date asset register (systems and data flows)
2. Keep security policies and procedures current and review-ready
3. Maintain audit trails for patching, access reviews, and security decisions
4. Conduct periodic internal assessments against CAF (NCSC guidance) in preparation

### 2.2 Information-Gathering Powers

CAs will be able to require organisations to provide:
- Security policies and procedures
- Network architecture diagrams
- Patch management records
- Access and privilege management records
- Supply chain security assessments
- Previous incident records and remediation evidence
- Board-level cyber risk reporting documentation

**Implication:** Organisations should maintain audit-ready documentation at all times, not only
in response to incidents or formal investigations.

### 2.3 Proactive Audit Schedule (Expected)

The CSRB is expected to allow CAs to schedule audits of organisations classified as highest-risk
or most critical. The criteria for selection are not yet prescribed but are likely to include:

- Scale of essential service provided
- Previous incident history
- Known vulnerability exposure
- Sector-wide risk indicators (threat intelligence)
- Known deficiencies in previous self-assessments

---

## Part 3 — Enforcement Powers and Penalties

### 3.1 Enforcement Process

Under the NIS Regs 2018 the enforcement process proceeds:
**Information notice → Enforcement notice → Penalty notice**

The CSRB is expected to retain this stepped approach but with enhanced provisions:

| Stage | NIS Regs (current) | CSRB (expected) |
|-------|--------------------|-----------------|
| Information notice | CA requires specific information | Expanded: broader categories of information; MSP/data centre entities added |
| Enforcement notice | CA requires specific steps; time-limited | Retained; step-down process more prescriptive |
| Penalty notice | Max £17M (OES/DSP) | Revised structure; MSP and data centre entities added |
| Appeals | Upper Tribunal | Retained |
| Criminal offences | Obstruction etc. | Retained |

### 3.2 Financial Penalties — Current (NIS Regs 2018)

| Entity | Maximum Penalty |
|--------|----------------|
| OES | £17,000,000 |
| DSP | £17,000,000 |

> Source: Regulation 18 and Regulation 21, NIS Regulations 2018

### 3.3 Financial Penalties — CSRB (Expected)

The exact penalty figures are subject to the enacted legislation. Three possible models based on
comparable UK legislation:

| Model | OES/DSP | MSP | Data Centre |
|-------|---------|-----|-------------|
| Retained NIS | £17M | £17M | £17M |
| GDPR-aligned (% of global turnover) | Higher of £17M or 4% global turnover | Higher of £8.7M or 2% global turnover | TBD |
| Sector-differentiated | TBD per sector | TBD | TBD |

> Note: The GDPR-aligned model is used in the EU NIS2 Directive (higher of €10M or 2% for
> essential entities; €7M or 1.4% for important entities). The UK CSRB may adopt a comparable
> structure. Verify against enacted legislation.

---

## Part 4 — Cross-CA Information Sharing

### 4.1 Current Limitations (NIS Regs 2018)

Under the NIS Regulations 2018, information sharing between Competent Authorities is limited:
- Each CA operates primarily within its own sector
- No statutory obligation to share incident information across sectors
- NCSC receives information informally but this is not a statutory duty

### 4.2 CSRB Cross-CA Sharing Framework (Expected)

The CSRB is expected to establish:
- **Statutory gateway** for CAs to share incident information between each other
- **DSIT coordination function** — receiving sector incident information to maintain national
  security posture assessment
- **NCSC integration** — formal channel for CAs to receive NCSC threat intelligence and for
  NCSC to receive CA incident data
- **International sharing** — formal gateway for sharing with equivalent EU NIS2 competent
  authorities and trusted international partners

### 4.3 Implications for Organisations

Cross-CA sharing means:
1. An incident reported to one CA may be shared with other CAs relevant to your sector
2. Multi-sector organisations (or MSPs serving multiple sectors) should assume reports will
   reach all relevant regulatory bodies
3. Confidentiality claims over reported information are likely limited — plan reporting
   accordingly

---

## Part 5 — Powers Specific to MSPs and Data Centres

### 5.1 Managed Service Provider Oversight

DSIT is expected to be the Competent Authority for MSPs. Powers specific to MSPs are expected to
include:

**Information requirements:**
- List of in-scope clients (organisations that are OES/DSP)
- Architecture of shared infrastructure serving multiple clients
- Client security access controls and privilege management records
- Incident history across client estate

**Assessment triggers:**
- Incident affecting multiple clients
- Threat intelligence indicating MSP targeting
- Scheduled proactive audit

**Notification obligations:**
- MSP must notify CA within 24 hours of detecting incident affecting client(s)
- MSP must notify affected clients within 24 hours
- CA may coordinate with sectoral CAs of affected clients

### 5.2 Data Centre Oversight

Large data centres above the qualifying threshold are expected to have DSIT as their CA. Powers
are expected to include:

**Physical and environmental security:**
- Audit of physical security controls
- Access control systems inspection
- Power and cooling resilience verification

**Logical (cyber) security:**
- Assessment of management plane security
- Customer-facing access controls
- Interconnect and peering security

---

## Part 6 — Compliance Programme Implications

### 6.1 From Audit-Responsive to Continuous Compliance

Under NIS Regs 2018, many organisations treated compliance as event-driven:
- Respond to CA information requests
- Conduct self-assessments when asked
- Produce documentation when inspected

Under the CSRB, the proactive audit model requires continuous compliance readiness:

| Activity | Recommended Frequency |
|----------|-----------------------|
| Asset register review | Quarterly |
| Security policy review | Annual (minimum) |
| CAF self-assessment | Annual |
| Third-party penetration test | Annual (minimum) |
| Supply chain security review | Annual |
| Board cyber risk report | Quarterly |
| Access and privilege review | Quarterly |
| Patch management evidence review | Monthly |

### 6.2 Board-Level Accountability

The CSRB is expected to reinforce board accountability for cyber security. CAs are likely to
require evidence of:
- Board-level oversight of cyber risk
- Named senior responsible owner (SRO) for CSRB compliance
- Board minutes recording cyber risk discussions
- Board-approved cyber security strategy and investment

### 6.3 Documentation Checklist for CA Assessment Readiness

```
CA ASSESSMENT READINESS CHECKLIST

POLICIES AND PROCEDURES
[ ] Cyber Security Policy (board-approved, dated)
[ ] Incident Response Plan (tested, dated)
[ ] Business Continuity Plan (tested, dated)
[ ] Supplier / Supply Chain Security Policy
[ ] Access Control Policy
[ ] Patch Management Policy and records

TECHNICAL EVIDENCE
[ ] Asset register (systems, data flows)
[ ] Network architecture diagram (current)
[ ] Patching status records (last 12 months)
[ ] Vulnerability management records
[ ] Penetration test report (dated within 12 months)
[ ] Access review records (privileged accounts)
[ ] Multi-factor authentication coverage evidence

CAF ASSESSMENT
[ ] CAF self-assessment (current, NCSC CAF v3.2 or later)
[ ] Objective A (Managing security risk) — documented
[ ] Objective B (Protecting against cyber attack) — documented
[ ] Objective C (Detecting cyber security events) — documented
[ ] Objective D (Minimising the impact of incidents) — documented

INCIDENT RECORDS
[ ] Previous incident log (past 3 years)
[ ] Evidence of CA notifications where applicable
[ ] Post-incident review records

SUPPLY CHAIN
[ ] Supplier register with security risk assessment
[ ] Key supplier questionnaire responses
[ ] Contractual security obligations — evidence of enforcement

GOVERNANCE
[ ] Board cyber risk report (most recent)
[ ] CSRB SRO appointment documented
[ ] Staff cyber security training records
```

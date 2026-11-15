# CMMC 2.0 - Level Comparison, Assessment Types & Flow-Down Rules

## Level Comparison Table

| Attribute | Level 1 - Foundational | Level 2 - Advanced | Level 3 - Expert |
|-----------|----------------------|-------------------|-----------------|
| **Practices** | 15 requirements (FAR 52.204-21(b)(1)(i)–(xv); map to 17 NIST SP 800-171 requirements) | 110 (NIST SP 800-171 Rev 2) | 110+ (SP 800-171 + SP 800-172 subset) |
| **Focus** | Federal Contract Information (FCI) | Controlled Unclassified Information (CUI) | CUI on highest-priority DoD programs; APT resilience |
| **Assessment type** | Annual self-assessment | Triennial C3PAO assessment (critical) OR self-assessment (non-critical) | DIBCAC-led government assessment (triennial) |
| **SPRS submission** | Yes | Yes | Yes |
| **Certification body** | Self | C3PAO (CMMC Third-Party Assessment Organization) | DIBCAC (Defense Industrial Base Cybersecurity Assessment Center) |
| **Conditional certification** | No (all requirements must be MET; no POA&M) | Yes (limited POA&M allowed) | Yes (Conditional Level 3 per 32 CFR 170.21(a)(3), with excluded requirements) |
| **Who needs it** | All DoD contractors receiving/generating FCI | Contractors handling CUI on DoD contracts | Contractors on highest-priority programs (e.g., nuclear C3, certain weapons systems) |

---

## DFARS Clause Mapping

| DFARS Clause | Requirement | Level Implied |
|-------------|-------------|---------------|
| FAR 52.204-21 | Basic Safeguarding of FCI - 15 requirements | Level 1 baseline |
| DFARS 252.204-7012 | Safeguarding CUI; 72-hr DIBNET incident reporting; cloud = FedRAMP Moderate | Level 2 prerequisite |
| DFARS 252.204-7019 | NIST SP 800-171 self-assessment; SPRS submission required | Level 2 self-assessment |
| DFARS 252.204-7020 | DoD access to contractor assessment results in SPRS | Level 2 |
| DFARS 252.204-7021 | CMMC certification requirement; flow-down to subcontractors | Level 2 or 3 |

**Rule**: If your contract contains DFARS 252.204-7021, your CMMC level is specified in the contract. Check Section L or the Performance Work Statement.

---

## Assessment Process by Level

### Level 1 - Self-Assessment
1. Assess all 15 security requirements of FAR 52.204-21(b)(1)(i)–(xv)
2. Confirm every requirement is MET: Level 1 has **no POA&M and no numeric score**; the result is simply compliant or not
3. Enter the self-assessment result in SPRS at https://www.sprs.csd.disa.mil/
4. Senior official affirms accuracy
5. Repeat annually

### Level 2 - C3PAO Assessment (Critical Programs)
1. **Pre-assessment preparation** (6–12 months): SSP, POA&M, gap remediation
2. **Select a C3PAO**: Must be authorized by The Cyber AB; find at cyberAB.us
3. **Contract with C3PAO**: Negotiate scope, timeline, NDA
4. **Assessment**: C3PAO reviews evidence, interviews, observes (typically 2–4 weeks on-site/remote)
5. **Findings**: Assessment results are entered in CMMC eMASS and reflected in SPRS; conditional certification possible with limited POA&M
6. **Certification**: Valid for 3 years
7. **Annual affirmation**: Affirm continued compliance each year

### Level 2 - Self-Assessment (Non-Critical Programs)
- Same 110 practices as C3PAO path
- Self-assessed by contractor; senior official affirms in SPRS
- DoD reserves right to audit; false statements = False Claims Act liability
- Must still submit SPRS score

### Level 3 - DIBCAC Assessment
1. Contractor must hold a current Level 2 C3PAO certification first
2. DIBCAC (government team) conducts assessment - not contractor-selected
3. Assesses SP 800-171 practices PLUS select SP 800-172 enhanced requirements
4. Conditional Level 3 is permitted (32 CFR 170.21(a)(3)), but IR.L3-3.6.1e, IR.L3-3.6.2e, RA.L3-3.11.1e, RA.L3-3.11.4e, RA.L3-3.11.6e, RA.L3-3.11.7e, and SI.L3-3.14.3e may never be on a POA&M and must be MET
5. Government schedules the assessment; no commercial negotiation

---

## Flow-Down Requirements

DFARS 252.204-7021(c) requires prime contractors to:
- Include CMMC requirements in **all subcontracts** where the subcontractor processes, stores, or transmits CUI
- Specify the required CMMC level in the subcontract
- Verify subcontractor certification before award (Level 2/3 results appear in SPRS via CMMC eMASS)
- Flow-down applies to **all tiers** - sub-subcontractors are not exempt

**Practical implication**: If you're a prime, map your CUI to each subcontractor and determine which level applies to each. Document this in your supply chain security program.

---

## Timeline and Key Dates

| Milestone | Date |
|-----------|------|
| CMMC 2.0 Final Rule (32 CFR Part 170) effective | December 16, 2024 |
| DFARS rule (48 CFR Parts 204, 212, 252) effective | December 16, 2024 |
| CMMC requirements in new contracts | Phased: began Q1 2025, full rollout through 2026 |
| Level 1 self-assessments required | All contracts with FAR 52.204-21, immediately |
| Level 2 C3PAO assessments | Required when DFARS 7021 included in solicitation |

---

## CUI Categories Most Common in Defense Contracts

| CUI Category | Examples | Typical Contract Types |
|-------------|----------|----------------------|
| Export Controlled (CTI) | Technical data, software, drawings | Engineering, manufacturing |
| Naval Nuclear Propulsion (NOFORN) | Propulsion design data | Shipbuilding, nuclear |
| Controlled Technical Information (CTI) | ITAR/EAR-controlled technical data | Weapons systems, aerospace |
| Privacy (PII) | Personnel records | HR, health, benefits |
| Law Enforcement Sensitive | Investigation data | Base security contractors |
| Procurement/Acquisition | Pre-award contract info | Proposal/BD teams |

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **FCI** | Federal Contract Information - information provided by or generated for the Government under contract, not intended for public release |
| **CUI** | Controlled Unclassified Information - information the Government creates or possesses that requires safeguarding per law/regulation/policy |
| **SPRS** | Supplier Performance Risk System - DoD portal where self-assessment scores are submitted |
| **C3PAO** | CMMC Third-Party Assessment Organization - authorized to conduct Level 2 assessments |
| **DIBCAC** | Defense Industrial Base Cybersecurity Assessment Center - DCSA organization conducting Level 3 government assessments |
| **The Cyber AB** | Accreditation body that authorizes C3PAOs, assessors, and consultants |
| **OSC** | Organization Seeking Certification - the defense contractor being assessed |
| **POA&M** | Plan of Action & Milestones - documented remediation plan for unmet practices |
| **SSP** | System Security Plan - describes the system boundary, CUI flows, and control implementations |

# CMMC 2.0 Skill for Claude

> **Disclaimer:** This skill provides informational guidance on CMMC 2.0 requirements based on 32 CFR Part 170, NIST SP 800-171 Rev 2, and associated DFARS clauses. It does not constitute legal advice and does not substitute for engagement with a Registered Practitioner Organization (RPO) or Certified Third-Party Assessment Organization (C3PAO). CMMC certification decisions, SPRS score submissions, and DIBCAC assessment responses involve significant legal and contractual obligations — consult a qualified CMMC professional for high-stakes compliance matters.

---

## 1. What Does the Skill Do?

This skill turns Claude into an expert **CMMC 2.0 Registered Practitioner and NIST SP 800-171 implementation advisor**, providing deep, structured guidance to defense contractors, subcontractors, and their IT and compliance teams across the full CMMC 2.0 compliance lifecycle. It covers the final CMMC 2.0 rule (**32 CFR Part 170**, effective December 2024) and all supporting regulatory instruments: **NIST SP 800-171 Rev 2**, **NIST SP 800-172**, and **DFARS clauses 252.204-7012/7019/7020/7021**.

The skill handles CMMC's three-level framework with precision, distinguishing between the 17 practices required for **Level 1** (FCI protection, FAR 52.204-21 self-assessment), the 110 practices required for **Level 2** (CUI protection, NIST SP 800-171, triennial C3PAO assessment or self-assessment for non-critical programs), and the enhanced requirements of **Level 3** (APT resistance, NIST SP 800-172 practices, DIBCAC government assessment). Advice is always scoped to the applicable level and the specific DFARS clause in the contract.

A central capability is the **SPRS score calculation** — the skill walks through the Supplier Performance Risk System scoring methodology, starting from 110 and applying per-practice deductions for each NOT MET practice, to produce an estimated score with remediation priorities. It also supports **System Security Plan (SSP) drafting**, generating fully structured SSP sections with practice ID, requirement statement, implementation description, responsible roles, associated systems, and evidence artifacts — exactly the format expected by C3PAOs and DIBCAC assessors.

The skill is also attentive to the most common compliance pitfalls in the Defense Industrial Base: scope creep that inflates assessment burden, missing CUI flow-down to subcontractors, non-FIPS-validated encryption, MFA gaps (the most commonly failed practice — IA.L2-3.5.3), DIBNET incident reporting timelines, and the use of non-FedRAMP cloud services for CUI. It surfaces these issues proactively in every assessment.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|----------------------|
| **Defense contractors (prime)** | Level determination, gap assessments, SSP drafting, SPRS score calculation, flow-down obligation management |
| **Defense subcontractors** | Understanding DFARS 7021 flow-down requirements, Level 1/2 readiness, scoping CUI handling |
| **IT and security teams (DIB)** | Practice-level implementation guidance for all 110 NIST SP 800-171 requirements |
| **Compliance managers** | POA&M development, remediation roadmaps, audit preparation, C3PAO engagement readiness |
| **Contracts and legal teams** | DFARS clause identification, subcontractor flow-down language, FCI vs. CUI scope analysis |
| **RPOs and CMMC consultants** | Gap assessment frameworks, SSP templates, client assessment tooling |
| **CISOs and risk officers** | SPRS score management, risk prioritization, DoD contract cybersecurity strategy |
| **Cloud and infrastructure teams** | FedRAMP authorization requirements for CUI, FIPS 140-2/3 validation, enclave design |

---

## 3. Common Use Cases

### Level Determination and Contract Scoping
- *"We just received a new DoD RFP. Which CMMC level does DFARS 252.204-7021 require us to meet?"*
- *"What's the difference between a self-assessment under DFARS 7019 vs. a C3PAO assessment under DFARS 7021?"*
- *"We handle both FCI and CUI. Do we need Level 1, Level 2, or Level 3?"*
- *"Our prime contractor is flowing CMMC Level 2 down to us. What does that require?"*

### Gap Assessment
- *"Run a CMMC 2.0 Level 2 gap assessment. We have Active Directory, MFA on email only, no formal SSP, and we store CUI on shared drives."*
- *"Assess our Access Control (AC) domain practices against Level 2 requirements."*
- *"Which of the 110 practices are we most likely to fail if we're assessed today?"*
- *"What practices do IG1-covered organizations most commonly miss when they start preparing for CMMC?"*

### SSP Drafting
- *"Draft the SSP entry for AC.L2-3.1.3 — Control CUI flow to external systems."*
- *"Write the system boundary description section of our SSP for our AWS-hosted CUI environment."*
- *"Generate SSP entries for all Identification and Authentication (IA) domain practices."*
- *"Review our SSP entry for IA.L2-3.5.3 (MFA) — does it meet the documentation standard?"*

### SPRS Score Calculation
- *"Calculate our estimated SPRS score. We have 15 practices NOT MET and 8 PARTIAL."*
- *"Which NOT MET practices carry the highest point deductions? Where should we focus remediation first?"*
- *"Our current SPRS score is -47. What's a realistic remediation path to reach +80 in 6 months?"*

### POA&M Management
- *"Create a POA&M for our 12 NOT MET Level 2 practices, with milestones and owners."*
- *"Which POA&M items require accelerated timelines under CMMC 2.0 rules?"*
- *"Can we get conditional certification with open POA&M items? Which practices are eligible?"*

### CUI Scoping and Third-Party Cloud
- *"How do we define the CUI Asset Boundary? What's in scope vs. out of scope?"*
- *"We use Microsoft 365 Government (GCC High) for CUI. Does that satisfy DFARS 7012?"*
- *"Our cloud storage provider is FedRAMP Moderate authorized. Does that cover our CUI handling?"*
- *"We use Slack and Google Workspace. Can CUI flow through those systems?"*

---

## 4. How to Use the Skill

### Installation
1. Download the `cmmc.skill` file from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `cmmc.skill`
4. The skill is immediately active in your Claude sessions

### Triggering the Skill
The skill activates automatically when your message relates to CMMC 2.0 or the regulatory instruments that underpin it. Example phrases that trigger it:

- *"CMMC gap assessment"*
- *"CMMC Level 2 readiness"*
- *"NIST SP 800-171 practices"*
- *"CUI protection requirements"*
- *"SPRS score calculation"*
- *"System Security Plan for CMMC"*
- *"DFARS 252.204-7021 compliance"*
- *"C3PAO assessment preparation"*
- *"FCI protection requirements"*
- *"DIBCAC audit readiness"*

### Example Prompts

```
"We're a 75-person defense subcontractor. We handle CUI under a DoD 
contract that includes DFARS 252.204-7021. We have never done a CMMC 
assessment. Walk me through the steps to determine our Level 2 readiness 
and produce a gap assessment table for all 17 CMMC domains."
```

```
"Calculate our estimated SPRS score. The following 110 practices have 
these statuses: [MET/PARTIAL/NOT MET list]. Identify the 10 highest-value 
remediation actions to maximize our SPRS score increase."
```

```
"Draft a complete SSP section for the following practices: AC.L2-3.1.1, 
AC.L2-3.1.2, AC.L2-3.1.3. Our environment is an on-premises Windows 
Server AD domain with 40 CUI-handling workstations."
```

```
"We use AWS GovCloud for CUI storage. Is this sufficient for DFARS 7012 
compliance? What specific AWS services and configurations are required?"
```

```
"Our prime contractor has told us they are flowing CMMC Level 2 down to 
us as a subcontractor handling CUI design documents. What does this mean 
for our timeline, assessment type, and contractual obligations? Draft the 
flow-down clauses we should expect in our subcontract."
```

---

## 5. Skill Implementation Details

### Architecture

```
cmmc/
├── SKILL.md                      # Core skill — 3 CMMC levels, 17 domains, 5 core
│                                 #   workflows, key regulatory references, common pitfalls
└── references/
    ├── cmmc-practices.md         # All 110 NIST SP 800-171 practices mapped to CMMC
    │                             #   domains and levels with practice text
    ├── cmmc-levels.md            # Level 1/2/3 comparison, assessment types, timelines,
    │                             #   flow-down rules, self-assessment vs. C3PAO vs. DIBCAC
    └── cmmc-assessment.md        # SPRS scoring methodology, C3PAO assessment process,
                                  #   POA&M rules, conditional certification, DIBCAC guidance
```

**Total:** ~625 lines across 4 files (SKILL.md + 3 reference files)

### What's in SKILL.md

- **Three-level framework** — Level 1 (17 FCI practices), Level 2 (110 CUI practices), Level 3 (110+ APT practices) with assessment types
- **17 CMMC domains** — all domain abbreviations and full names
- **Five core workflows** — gap assessment, SSP drafting, SPRS score calculation, POA&M management, and CUI scoping
- **Key regulatory references table** — 9 documents from 32 CFR Part 170 through FAR 52.204-21 with relevance descriptions
- **Common pitfalls** — scope creep, missing flow-down, FIPS validation, MFA gaps, incident reporting, cloud CUI
- **Output format routing** — 6 task types with specific output format specifications

### What's in the reference files

| File | Contents |
|------|----------|
| `cmmc-practices.md` | All 110 NIST SP 800-171 Rev 2 practices with practice ID, domain, practice statement, and CMMC level assignment; Level 1 practices (FAR 52.204-21) separately listed |
| `cmmc-levels.md` | Level 1/2/3 deep comparison: required practices, assessment type (self/C3PAO/DIBCAC), assessment timelines, SPRS submission requirements, flow-down obligations to subcontractors, key DFARS clause mapping |
| `cmmc-assessment.md` | SPRS scoring methodology with per-practice weight table; C3PAO assessment process stages; POA&M requirements and eligible practices for conditional certification; DIBCAC assessment process for Level 3 |

### Inputs used to build the skill

| Input | Description |
|-------|-------------|
| **32 CFR Part 170** | CMMC 2.0 final rule (effective December 2024) — the authoritative regulatory text |
| **NIST SP 800-171 Rev 2** | All 110 CUI protection requirements forming the Level 2 practice set |
| **NIST SP 800-172** | Enhanced security requirements for Level 3 APT resistance |
| **DFARS 252.204-7012/7019/7020/7021** | DFARS clauses governing CUI safeguarding, self-assessment, SPRS submission, and CMMC flow-down |
| **FAR 52.204-21** | Basic safeguarding requirements for FCI (Level 1 foundation) |
| **DoD CMMC Assessment Guides** | DoD-published assessment methodology for Level 1, 2, and 3 |
| **SPRS methodology guidance** | DoD scoring tables and per-practice deduction weights |
| **DoD CUI Registry** | Authoritative list of CUI categories referenced in scoping workflows |

### Skill trigger phrases

`CMMC`, `CMMC 2.0`, `Cybersecurity Maturity Model Certification`, `CMMC Level 1`, `CMMC Level 2`, `CMMC Level 3`, `NIST SP 800-171`, `NIST 800-171`, `CUI`, `Controlled Unclassified Information`, `FCI`, `Federal Contract Information`, `SPRS score`, `System Security Plan`, `SSP`, `POA&M`, `C3PAO`, `DIBCAC`, `DFARS 7012`, `DFARS 7021`, `defense contractor cybersecurity`, `DIB`, `Defense Industrial Base`, `CMMC gap assessment`, `CMMC readiness`, `CUI scoping`, `FedRAMP CUI`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.8.0 — August 2026

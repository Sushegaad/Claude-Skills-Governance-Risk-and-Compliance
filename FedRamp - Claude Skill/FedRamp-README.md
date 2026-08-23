# FedRAMP Certification Skill for Claude

A Claude skill that provides expert, end-to-end guidance for FedRAMP authorization —
from initial readiness assessment through ATO documentation, control mapping, cloud
architecture review, and ongoing continuous monitoring.

---

## What Does the Skill Do?

This skill turns Claude into a knowledgeable FedRAMP advisor. It covers the full
authorization lifecycle for Cloud Service Providers (CSPs) pursuing or maintaining
FedRAMP certification under the current **NIST SP 800-53 Rev 5** baseline and the
**CR26 (FedRAMP Consolidated Rules for 2026)** framework.

At a high level, the skill enables Claude to:

- Conduct **readiness and gap assessments** against a 75+ item checklist across 14 security domains
- Guide the authoring of core **ATO documentation**: SSP, POA&M, SAP, SAR, and all required appendices (A–Q)
- **Map controls** from all 20 NIST 800-53 Rev 5 control families to specific system implementations
- Advise on **CR26 Certification Classes A–D**, which replace the old Low/Moderate/High/LI-SaaS impact levels
- Provide **architecture guidance** for AWS GovCloud, Azure Government, and Google Cloud — including common findings, inheritance patterns, and design recommendations
- Support **continuous monitoring (ConMon)** obligations: monthly deliverables, annual assessments, POA&M management, and deviation request handling
- Guide **FedRAMP 20x** adoption — now the primary authorization pathway with continuous authorization and automated evidence collection
- Prepare CSPs for the **OSCAL mandate** (September 30, 2026) — machine-readable authorization package submissions

The skill is current as of July 2026, incorporating CR26 Certification Classes A–D, FedRAMP 20x as the primary pathway, the FedRAMP Ready retirement (July 28, 2026), the September 2026 OSCAL mandate, the January 2026 Security Inbox requirement, and the December 2024 template updates.

---

## Intended Audiences

| Audience | How They Benefit |
|---|---|
| **Cloud Service Providers (CSPs)** | Navigate the authorization process, write SSP narratives, manage POA&M, prepare for 3PAO assessments |
| **ISSOs / Security Engineers** | Map controls to implementations, identify gaps, review SAR findings, manage ConMon activities |
| **Compliance Managers / GRC Teams** | Understand FedRAMP requirements, track remediation SLAs, coordinate documentation across teams |
| **Cloud Architects** | Design systems that satisfy FedRAMP requirements from the ground up; understand boundary scoping |
| **Federal Agency Personnel** | Understand what to expect from a CSP's authorization package; evaluate SSP and SAR quality |
| **3PAO Assessors** | Reference control family requirements, test case scope, and document structure expectations |
| **Consultants / Advisory Firms** | Quickly provide accurate FedRAMP guidance to clients across certification classes and authorization phases |

---

## Common Use Cases

### 1. Readiness Assessment
> *"We're a SaaS company on AWS GovCloud targeting FedRAMP Class B (Moderate equivalent). Are we ready?"*

The skill walks through a structured gap analysis — asking about your boundary, encryption posture, logging, IAM, policies, and incident response — and produces a prioritized gap table with recommendations. It also advises whether to pursue FedRAMP 20x (now the primary pathway) or a legacy Agency Authorization package.

### 2. Writing SSP Control Narratives
> *"Help me write the control implementation statement for AC-2 (Account Management)."*

The skill generates detailed, reviewer-ready prose that addresses every verb in the control requirement, distinguishes CSP vs. customer responsibilities, and references specific tools and policies.

### 3. POA&M Entry Creation
> *"The 3PAO found that we don't have MFA on one of our admin interfaces. Help me write the POA&M entry."*

The skill produces a complete POA&M row with all required fields: risk rating, remediation plan, milestone dates, owner, and deviation request guidance if applicable.

### 4. CR26 Certification Class Scoping
> *"Our system processes law enforcement data. What certification class do we need and how many controls apply?"*

The skill maps the system's data sensitivity to the appropriate CR26 Certification Class (A, B, C, or D) and explains the corresponding control baseline. It also notes legacy Low/Moderate/High equivalents for CSPs familiar with the old framework.

### 5. NIST 800-53 Control Mapping
> *"Which controls cover encryption in transit, and how should we implement them on Azure Government?"*

The skill maps the question to specific control families (SC, IA), describes FedRAMP parameter requirements, and provides Azure-specific implementation guidance.

### 6. Architecture Review
> *"Review our architecture for FedRAMP compliance gaps."*

Given a description of the system, the skill identifies common findings — undocumented external connections, FIPS non-compliance, IAM over-permissioning, logging gaps, missing OSCAL tooling — and recommends remediations.

### 7. FedRAMP 20x Pathway Guidance
> *"What is FedRAMP 20x and how do we pursue it?"*

The skill explains FedRAMP 20x as the primary authorization pathway under CR26 — covering continuous authorization, modular API-driven submissions, automated evidence collection, and how it differs from legacy Agency Authorization packages.

### 8. Continuous Monitoring Support
> *"What do we need to submit to our agency AO every month?"*

The skill outlines monthly and annual ConMon obligations, POA&M SLA requirements, and how to handle vendor dependencies and deviation requests.

### 9. 3PAO Engagement Guidance
> *"How do we select and work with a 3PAO?"*

The skill explains FedRAMP Marketplace requirements, the A2LA R311 advisory/assessment separation rule, and CSP responsibilities for reviewing and approving SAP and SAR documents.

### 10. OSCAL Readiness
> *"What is OSCAL and what do we need to do before September 30, 2026?"*

The skill explains the OSCAL mandate (RFC-0024), what machine-readable authorization packages require, and how to begin structuring SSP data for OSCAL export ahead of the September 30, 2026 deadline.

---

## Key CR26 Changes (July 2026)

| Change | Details |
|---|---|
| **Certification Classes A–D** | Replace FIPS 199 baseline labels (per NTC-0004): Class A = new pilot/transitional baseline (external-framework entry, e.g. SOC 2 Type II), Class B = LI-SaaS + Low, Class C = Moderate, Class D = High |
| **FedRAMP Ready retires** | July 28, 2026 — no new designations; existing Ready CSPs must transition to FedRAMP 20x or full authorization |
| **FedRAMP 20x is primary pathway** | Continuous authorization, modular submissions, automated evidence — not just a pilot |
| **JAB P-ATO retired** | FedRAMP PMO is now the sole authorization body |
| **OSCAL mandate** | All CSPs must submit machine-readable OSCAL packages by September 30, 2026 |

---

## How to Use the Skill

### Installation
1. Download `fedramp.skill` from this repository
2. In Claude, navigate to **Settings → Skills**
3. Upload the `.skill` file
4. The skill is now active — Claude will automatically use it for FedRAMP-related questions

### Triggering the Skill
The skill activates automatically when you mention topics like:
- FedRAMP, ATO, Authority to Operate, CR26
- SSP, SAP, SAR, POA&M
- NIST 800-53, control families, control mapping
- FedRAMP Certification Classes (A, B, C, D) or old impact levels (Low, Moderate, High, LI-SaaS)
- FedRAMP 20x, OSCAL, continuous authorization
- 3PAO, continuous monitoring, ConMon
- Cloud security for federal government, AWS GovCloud, Azure Government

### Example Prompts
```
"Assess our FedRAMP readiness. We're a SaaS company running on AWS GovCloud targeting Class B (Moderate equivalent)."

"Write an SSP control narrative for SC-8 (Transmission Confidentiality and Integrity)."

"Create a POA&M entry for a High finding: missing MFA on the admin portal."

"Map the AU control family to our AWS CloudTrail and Security Hub setup."

"What architecture changes do we need to meet FedRAMP Class C (High equivalent) requirements?"

"Explain the CR26 Certification Classes and how they map to the old impact levels."

"What do we need to do to prepare for the September 30, 2026 OSCAL mandate?"
```

---

## Skill Implementation Details

### File Structure

```
fedramp/
├── SKILL.md                          # Main skill — routing logic, all five domains
└── references/
    ├── readiness-checklist.md        # 75+ item readiness checklist (14 categories)
    ├── ssp-guide.md                  # SSP section-by-section writing guide + appendices A–Q
    ├── poam-guide.md                 # POA&M fields, deviation types, SLA table
    └── sap-sar-guide.md              # SAP/SAR structure, 3PAO guidance, CSP review tips
```

### How It Was Built

The skill was authored using the **Claude Skill Creator** framework, which structures knowledge into a layered, progressively-disclosed format:

- **SKILL.md** (primary file): Contains a routing table to direct Claude to the right domain based on user intent, a current-state summary of FedRAMP as of July 2026 (CR26), and five domain sections (Readiness, ATO Docs, Control Mapping, Architecture, ConMon)
- **Reference files**: Loaded on demand when deeper guidance is needed — keeping the main skill lean and focused

**Inputs used to construct the skill:**
- FedRAMP CR26 (Consolidated Rules for 2026) documentation, incl. notice NTC-0004, and PMO announcements (fedramp.gov)
- FedRAMP Rev 5 baseline documentation and transition guides
- NIST SP 800-53 Rev 5 control families and parameter requirements
- FedRAMP CSP Authorization Playbook (v4.2, November 2025)
- FedRAMP Annual Assessment Guidance (v3.0, February 2024)
- FedRAMP Rev 5 template release notes (December 2024)
- RFC-0024 OSCAL mandate documentation
- FedRAMP SSP, POA&M, SAP, SAR template structures
- A2LA R311 3PAO advisory/assessment separation requirements
- FedRAMP Jan 2026 Security Inbox directive

**Design decisions:**
- The skill uses a **quick-reference routing table** at the top so Claude can immediately navigate to the right section rather than reading the full document for every query
- **CR26 Certification Classes A–D** are the primary framework; legacy Low/Moderate/High mappings are preserved to help CSPs in transition
- **Output format is matched to request type** (tables for gap assessments, prose for control narratives, structured rows for POA&M) — ensuring outputs are immediately usable
- Reference files are **modular and loaded on demand**, keeping the main skill under 500 lines per the Skill Creator guidelines
- All guidance is pinned to **current FedRAMP state** (CR26, Rev 5, July 2026 requirements) with explicit callouts for CR26 changes to avoid outdated advice

### Dependencies
- No external tools or APIs required
- Works entirely within Claude's context window
- Official FedRAMP templates referenced by URL (https://www.fedramp.gov/documents-templates/) — not embedded, as these are periodically updated by the FedRAMP PMO

---

## Version History

| Version | Date | Changes |
|---|---|---|
| **1.5.0** | July 2026 | Corrected CR26 Certification Class mapping to official NTC-0004 (A = pilot/transitional, B = LI-SaaS + Low, C = Moderate, D = High); CR26 renamed to "Consolidated Rules for 2026"; POA&M remediation SLAs corrected to ConMon Performance Management Guide values (High 30d / Moderate 90d / Low 180d); benchmark re-run with primary-source assertions: 96% with skill vs 72% baseline |
| **1.4.0** | July 2026 | CR26 update: Certification Classes A–D, FedRAMP 20x as primary pathway, FedRAMP Ready retirement (July 28, 2026), OSCAL mandate (September 30, 2026), JAB P-ATO retirement |
| **1.0.0** | March 2026 | Initial release with Rev 5 baseline, ConMon guidance, OSCAL awareness |

---

## Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)
July 2026

---

*Skill version: 1.8.0 — August 2026*

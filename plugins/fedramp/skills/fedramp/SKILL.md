---
name: fedramp
description: >
  Expert guidance for FedRAMP certification and compliance under CR26 (FedRAMP
  Consolidated Rules for 2026). Use this skill whenever a user asks about FedRAMP
  authorization, ATO (Authority to Operate), cloud security for federal government,
  NIST SP 800-53 controls, CSP compliance, or any of the core FedRAMP document types:
  SSP, SAP, SAR, POA&M, CIS/CRM workbooks. Also trigger for questions about FedRAMP
  Certification Classes (A, B, C, D — new baseline labels: A = pilot/transitional,
  B = LI-SaaS/Low, C = Moderate, D = High, per NTC-0004), FedRAMP 20x
  (now the primary authorization pathway), OSCAL mandate (September 2026), 3PAO
  assessments, continuous monitoring (ConMon), gap assessments, system boundary
  definition, or architecture reviews for federal cloud. FedRAMP Ready retired
  July 28, 2026 (Legacy FedRAMP Ready). When in doubt, use this skill — it covers the full FedRAMP lifecycle
  from readiness through continuous monitoring.
---

# FedRAMP Certification Skill

> **Last verified:** 2026-08-15

A comprehensive guide for helping users navigate FedRAMP authorization — from initial
readiness through ATO and ongoing continuous monitoring.

## Quick Reference: What Does the User Need?

Identify the user's goal and jump to the appropriate section:

| User Goal | Go To |
|---|---|
| "Are we ready for FedRAMP?" / gap assessment | → [Readiness & Gap Assessment](#1-readiness--gap-assessment) |
| Writing SSP, POA&M, SAR, SAP, or other docs | → [ATO Documentation](#2-ato-documentation) |
| "Which controls apply to us?" / control mapping | → [NIST 800-53 Control Mapping](#3-nist-800-53-control-mapping) |
| Cloud architecture / AWS/Azure/GCP config | → [Architecture Guidance](#4-architecture-guidance) |
| Already authorized, ongoing compliance | → [Continuous Monitoring](#5-continuous-monitoring) |

---

## Current FedRAMP State (as of August 2026 — CR26)

> ⚠️ **CR26 (FedRAMP Consolidated Rules for 2026)**: FedRAMP has restructured its authorization framework. FIPS 199-based baseline labels (Low/Moderate/High/LI-SaaS) are replaced with **Certification Classes A–D** (per notice NTC-0004; CR26 rules valid through December 31, 2028). Class labels change the *names* of the baselines, not their requirements. CSPs already authorized under the old labels retain their authorization through a transition period in which old and new labels are linked.

- **Baseline**: NIST SP 800-53 **Rev 5** (fully in effect)
- **Control counts** (Rev 5): Low ≈ 156, Moderate = 323, High = 421 (legacy references; CR26 class-based counts being published by PMO)
- **CR26 Certification Classes** (official mapping, NTC-0004): **A** = new pilot/transitional baseline (entry via external frameworks such as SOC 2 Type II through Program Certification; holders have a 2-year window to obtain B/C/D), **B** = current **LI-SaaS + Low** baselines, **C** = current **Moderate** baseline (majority of federal deployments, incl. CUI), **D** = current **High** baseline.
- **FedRAMP 20x**: Now the **primary authorization pathway** — continuous authorization built on **Key Security Indicators (KSIs)**, machine-readable evidence, modular API-driven submissions, and automated validation. Traditional SSP/SAP/SAR templates remain for legacy paths.
- **CR26 status**: finalized **June 25, 2026**; optional early adoption since **July 4, 2026**; **mandatory January 1, 2027**.
- **Legacy FedRAMP Ready**: the Ready designation was retired/relabeled **Legacy FedRAMP Ready on July 28, 2026** — no new submissions. Rev5 Ready holders must convert by the later of their annual-assessment expiration or **November 17, 2026**; the status disappears entirely **December 31, 2027**.
- **Certification Class pipelines**: **Class A open since August 3, 2026**; Classes **B/C open August 31, 2026**; Class D pilot expected late 2026 with a formal option in early 2027.
- **Rev5 wind-down**: new Rev5 applications are not accepted after **June 11, 2027**; Rev5 sunsets **December 31, 2028**.
- **JAB P-ATO**: Fully suspended; FedRAMP PMO is the sole authorization body.
- **OSCAL mandate (RFC-0024)**: machine-readable packages required for **new authorizations from September 30, 2026**, and for **all packages by September 30, 2027**.
- **Security Inbox**: All authorized CSPs must maintain a dedicated Security Inbox (no CAPTCHAs or barriers) for urgent vulnerability directives — effective January 5, 2026.
- **Key templates updated**: SSP, SAR, SAP, POA&M, CIS/CRM, IIW, ISCP — all updated to align with Rev 5 (Dec 2024 releases).

---

## 1. Readiness & Gap Assessment

### Approach
1. **Clarify scope** — Ask the user: What is the CSO (Cloud Service Offering)? IaaS/PaaS/SaaS? Target Certification Class under CR26?
2. **Identify authorization path** — FedRAMP 20x (primary, preferred) vs. legacy Agency Authorization package (still available for complex systems during CR26 transition)
3. **Run through the readiness checklist** — See `references/readiness-checklist.md`
4. **Surface gaps** — Map current state to required controls; flag missing documentation, unimplemented controls, and architectural deficiencies
5. **Prioritize** — Group gaps by: (a) blockers for readiness review, (b) items addressable before 3PAO assessment, (c) POA&M candidates

> **FedRAMP Ready retired July 28, 2026** (now "Legacy FedRAMP Ready"). Advise CSPs by pipeline instead: Class A (open since August 3, 2026) for external-framework entry, Classes B/C from August 31, 2026 for full certification; legacy Rev5 Ready holders must convert by the later of annual-assessment expiration or November 17, 2026.

### Key Readiness Questions to Ask the User
- Are you targeting FedRAMP 20x (preferred) or a legacy authorization package?
- What cloud platform (AWS GovCloud, Azure Government, GCP, on-prem hybrid)?
- Are you leveraging any existing FedRAMP-authorized IaaS/PaaS (e.g., AWS GovCloud FedRAMP High)?
- Do you have FIPS 140-2/3 validated encryption in place?
- Is your authorization boundary defined and documented?
- Do you have a vulnerability scanning program (OS, DB, web app, container)?
- Are security policies and procedures documented?
- Do you have an Incident Response Plan (IRP) and Contingency Plan (CP) that have been tested?
- Are your authorization package artifacts in OSCAL format (mandatory by September 30, 2026)?

### Output Format
- Produce a **gap table**: Control Family | Current State | Gap | Priority | Owner
- Summarize top 5–10 high-priority gaps as prose
- Note the target Certification Class and whether FedRAMP 20x is feasible

---

## 2. ATO Documentation

The core FedRAMP authorization package consists of:

```
Authorization Package
├── System Security Plan (SSP) + Appendices A–Q
├── Security Assessment Plan (SAP) + Appendices A–D  [3PAO-prepared]
├── Security Assessment Report (SAR) + Appendices A–F  [3PAO-prepared]
└── Plan of Action & Milestones (POA&M)  [SSP Appendix O]
```

> **Important**: CSPs must use official FedRAMP PMO templates. OSCAL-format submissions are mandatory by September 30, 2026.
> Templates: https://www.fedramp.gov/documents-templates/

### Document Guidance

For detailed guidance on each document type, read the appropriate reference file:

- **SSP** → `references/ssp-guide.md`
- **POA&M** → `references/poam-guide.md`
- **SAP / SAR** → `references/sap-sar-guide.md`
- **Supporting appendices** → `references/appendices-guide.md`

### General Writing Principles for All ATO Docs
1. **Describe only what is implemented** — Do not document planned or aspirational controls; these trigger findings and must go in POA&M instead
2. **Be specific** — Reference exact tools, filenames, section numbers, policy names; vague language causes findings
3. **Mind the verbs** — Each control requirement uses specific verbs (track, document, enforce, test). Address each verb explicitly
4. **Shared responsibility** — For any customer-configurable or shared control, create a clear "Customer Responsibility" section
5. **Keep it consistent** — Architecture diagrams, data flows, inventory, and control statements must all be internally consistent

---

## 3. NIST 800-53 Control Mapping

### Control Families (Rev 5)

| ID | Family | Notes |
|---|---|---|
| AC | Access Control | IAM, RBAC, least privilege, remote access |
| AT | Awareness & Training | Security + **privacy** training (new in Rev 5) |
| AU | Audit & Accountability | Log retention, SIEM, audit review |
| CA | Assessment, Authorization & Monitoring | ConMon, 3PAO, ATO |
| CM | Configuration Management | Baselines, change control, CMDB |
| CP | Contingency Planning | BCP/DR, tested annually |
| IA | Identification & Authentication | MFA, PIV, FIPS 140-2/3 crypto |
| IR | Incident Response | IRP, tested annually, reporting SLAs |
| MA | Maintenance | Remote maintenance controls |
| MP | Media Protection | Data at rest, media sanitization |
| PE | Physical & Environmental | Datacenters; often inherited from IaaS |
| PL | Planning | SSP, rules of behavior |
| PM | Program Management | Enterprise-level security program |
| PS | Personnel Security | Screening, termination procedures |
| PT | PII Processing & Transparency | **New family in Rev 5** — privacy controls |
| RA | Risk Assessment | Vulnerability scanning, MITRE ATT&CK scoring |
| SA | System & Services Acquisition | SDLC, supply chain |
| SC | System & Communications Protection | Encryption in transit, network segmentation |
| SI | System & Information Integrity | Patching, malware, integrity monitoring |
| SR | Supply Chain Risk Management | **New family in Rev 5** — SCRM |

### CR26 Certification Class Mapping

Under CR26, the FedRAMP PMO is aligning control baselines to Certification Classes. When users describe their system, map to a class:

- **Class A** (Pilot/Transitional): New baseline introduced under 20x — entry into the federal market via external frameworks (initially SOC 2 Type II) through Program Certification; Class A holders have a **2-year window** to obtain a Class B, C, or D certification through full assessment
- **Class B** (replaces LI-SaaS + Low): Systems handling non-sensitive federal information where a breach would cause limited harm
- **Class C** (replaces Moderate): Most common — the majority of federal cloud deployments, including systems handling CUI
- **Class D** (replaces High): Federal information where compromise has severe or catastrophic effect (e.g., law enforcement, financial, health data)

> **Legacy references**: Many existing FedRAMP documents still reference Low/Moderate/High/LI-SaaS. These map to **LI-SaaS/Low → Class B, Moderate → Class C, High → Class D** (Class A is new — it has no legacy equivalent). During the CR26 transition, old and new labels are linked. Advise CSPs to check fedramp.gov for the latest.

### Mapping Workflow
1. Ask: What types of federal data will the system process/store/transmit?
2. Determine target Certification Class (A, B, C, or D) under CR26
3. Select NIST 800-53 Rev 5 baseline using the class mapping (B ↔ Low, C ↔ Moderate, D ↔ High)
4. Cross-reference with FedRAMP parameter requirements (FedRAMP often sets stricter parameters than base NIST)
5. For inherited controls, identify which are fully/partially inherited from leveraged FedRAMP IaaS/PaaS and document in CIS/CRM workbook

### Rev 4 → Rev 5 Key Changes to Highlight
- **New control families**: PT (Privacy), SR (Supply Chain)
- **Password controls revised**: No more forced rotation schedules; requires compromised-password lists and password strength meters (NIST 800-63b alignment)
- **Privacy integrated**: AT-3 now mandates privacy training; many families have privacy-specific enhancements
- **Threat-based methodology**: MITRE ATT&CK framework informs control prioritization

---

## 4. Architecture Guidance

### Authorization Boundary
The boundary defines what is IN scope for FedRAMP. This is one of the most common sources of findings and delays.

Key principles:
- **Everything that processes, stores, or transmits federal data** must be inside the boundary
- External services connected to in-scope systems must be FedRAMP-authorized OR documented with compensating controls
- Boundary must be depicted in a clear **network/data flow diagram** (required in SSP)

### Cloud Platform Considerations

**AWS GovCloud (US)**
- AWS GovCloud is FedRAMP High authorized — most PE and some SC controls are fully inherited
- Use AWS Config, CloudTrail, GuardDuty, Security Hub to satisfy AU, RA, SI controls
- Ensure use of GovCloud region endpoints (not standard commercial) to stay in boundary
- FIPS endpoints available for IA controls

**Azure Government**
- Azure Government is FedRAMP High authorized
- Azure Policy + Defender for Cloud maps well to CM, RA, SI
- Use Azure Blueprints / Policy Initiatives aligned to FedRAMP Moderate/High

**Google Cloud (FedRAMP-authorized regions)**
- Assured Workloads for FedRAMP compliance
- Chronicle SIEM for AU controls

### Architecture Patterns That Support FedRAMP
- **Zero Trust** — aligns directly with AC, IA, SC control families
- **Immutable infrastructure** — simplifies CM (configuration drift is a common finding)
- **Centralized logging** — SIEM/log aggregation addresses AU family comprehensively
- **Automated vulnerability scanning** — Required; must cover OS, DB, web app, and containers (if used)
- **OSCAL-native tooling** — Invest now; OSCAL submission is mandatory September 30, 2026

### Common Architecture Findings
- Undocumented external connections leaving the boundary
- FIPS-non-compliant encryption algorithms in transit or at rest
- Overly broad IAM roles / lack of least privilege
- Missing MFA on privileged accounts
- Vulnerability scans not covering all boundary components
- Logging gaps (not all components sending logs to centralized SIEM)
- Authorization packages not in OSCAL format ahead of September 2026 mandate

---

## 5. Continuous Monitoring

Once authorized, CSPs must maintain compliance through ConMon activities:

### Monthly Requirements
- Vulnerability scan results submitted to agency AOs
- POA&M updates (open findings, remediation progress)
- Inventory updates (new/removed assets)
- ConMon Monthly Executive Summary (template updated Nov 2024)

### Annual Requirements
- Full security assessment by 3PAO using Annual Assessment Controls Selection Worksheet
- Updated SSP and appendices
- Tested IRP and CP
- SAR and updated POA&M

### POA&M Management
- All open findings must have: risk level, owner, milestone dates, remediation plan
- Vendor Dependencies (VDs): when a finding depends on a third-party fix — document and track
- Deviation Requests (DRs): false positives and risk adjustments require AO approval
- SLA for remediation (FedRAMP ConMon Performance Management Guide): **High = 30 days**, **Moderate = 90 days**, **Low = 180 days** from identification. Where Critical is distinguished from High (e.g., scanner ratings), treat it as High-or-stricter (≤30 days, prioritized immediately)

---

## Output Formatting Guide

Match output format to request type:

| Request Type | Preferred Format |
|---|---|
| Gap assessment | Table + prose summary |
| SSP control narrative | Prose paragraphs (one per control/enhancement) |
| POA&M entry | Structured table row with all required fields |
| Architecture review | Bullet findings + recommended remediations |
| Control mapping question | Table: Control ID \| Requirement \| How to Implement |
| Readiness overview | Executive summary prose + priority action list |

When generating document content, always note: *"Use official FedRAMP templates from fedramp.gov — this content should be inserted into the appropriate template section."*

---

## Reference Files

Load these when more depth is needed:

- `references/readiness-checklist.md` — Full readiness checklist (75+ items)
- `references/ssp-guide.md` — SSP section-by-section writing guide
- `references/poam-guide.md` — POA&M structure, field definitions, SLA table
- `references/sap-sar-guide.md` — SAP/SAR overview and review tips for CSPs
- `references/appendices-guide.md` — Guide to all SSP appendices (A–Q)
- `references/control-families.md` — Deep-dive on each of the 20 control families

---

> *This skill provides general compliance information, not legal advice. Verify current requirements against official sources; consult qualified counsel or an accredited assessor for decisions.*

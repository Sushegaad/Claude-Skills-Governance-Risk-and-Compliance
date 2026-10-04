---
name: nist-800-53
description: >
  NIST SP 800-53 Rev 5 compliance advisor — all 20 control families (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR), Low/Moderate/High baseline selection, FIPS 199/200 system categorization, control tailoring and overlays, privacy controls (PT family), supply chain risk management (SR family), assessment procedures (SP 800-53A), OSCAL, RMF integration (SP 800-37), and mapping to FedRAMP, FISMA, CMMC 2.0, and ISO 27001. Use for any federal system security controls, FISMA compliance, RMF step guidance, control narrative writing, or baseline tailoring question.
---

# NIST SP 800-53 Rev 5 Compliance Skill

> **Last verified:** 2026-10-03

You are an expert NIST SP 800-53 compliance advisor with comprehensive knowledge of Special Publication 800-53 Revision 5 — *Security and Privacy Controls for Information Systems and Organizations* — published by NIST in September 2020 and updated December 2020. You guide federal agencies, contractors, cloud service providers, and system owners through control selection, implementation, assessment, and authorization.

---

## How to Respond

Match output format to task type:

| Task | Output Format |
|------|--------------|
| Control family deep-dive | Family overview → control-by-control with baseline assignment → implementation guidance |
| Baseline selection | FIPS 199 categorization → Low/Moderate/High baseline → tailoring rationale |
| Gap assessment | Table: Control ID \| Requirement \| Status \| Finding \| Remediation |
| Control narrative | Structured SSP narrative: Implementation Statement + Evidence + Responsible Roles |
| RMF step guidance | Step-by-step with required tasks, outputs, and responsible roles |
| General question | Precise prose with SP/section citations (e.g., SP 800-53 Rev 5, AC-2, SI-3(10)) |

Always cite controls precisely: Family prefix + control number + enhancement in parentheses (e.g., **AC-2(3)**, **SI-3(10)**). Distinguish between base controls and control enhancements. State which baseline (L/M/H) each control/enhancement applies to.

---

## SP 800-53 Rev 5 Framework Overview

**Authority:** Federal Information Security Modernization Act (FISMA) 2014 (44 U.S.C. § 3551 et seq.)  
**Published by:** National Institute of Standards and Technology (NIST), Information Technology Laboratory  
**Current version:** Rev 5 (September 2020; updated December 2020)  
**Scope:** Federal information systems and organizations; widely adopted by contractors, cloud providers, and private sector

### Key Changes in Rev 5 (from Rev 4)

| Change | Impact |
|--------|--------|
| Outcome-based control statements | Controls describe *what* to achieve, not *how* |
| Privacy controls integrated | PT family added; privacy merged with security throughout |
| Supply Chain Risk Management | SR family added (12 controls) |
| Program Management separated | PM controls separated from baselines (organization-wide) |
| Control baselines moved | Baselines moved to SP 800-53B (separate publication) |
| Proactive and systemic approach | Emphasis on cyber resiliency, trustworthiness |

---

## Step 1 — System Categorization (FIPS 199 / FIPS 200)

### FIPS 199 Impact Levels

Categorize the system by assessing the potential impact of a security breach on three objectives:

| Objective | Low | Moderate | High |
|-----------|-----|----------|------|
| **Confidentiality** | Limited adverse effect | Serious adverse effect | Severe or catastrophic effect |
| **Integrity** | Limited adverse effect | Serious adverse effect | Severe or catastrophic effect |
| **Availability** | Limited adverse effect | Serious adverse effect | Severe or catastrophic effect |

**Overall system categorization** = highest impact level across all three objectives (high-water mark).

### Common Information Types (NIST SP 800-60)

Use SP 800-60 Volume II to determine impact levels for specific information types:
- **PII / Privacy data** → typically Moderate Confidentiality
- **National security information** → High across all objectives
- **Financial systems** → Moderate/High Integrity
- **Life-safety systems** → High Availability
- **Public-facing information** → Low Confidentiality

---

## Step 2 — Baseline Selection (SP 800-53B)

The three control baselines are defined in **NIST SP 800-53B** (October 2020):

| Baseline | System Category | Controls (approx.) |
|----------|-----------------|-------------------|
| **Low** | Low impact (FIPS 199 Low) | ~156 controls/enhancements |
| **Moderate** | Moderate impact | ~323 controls/enhancements |
| **High** | High impact | ~422 controls/enhancements |
| **Privacy** | Systems processing PII | Overlaps all baselines; PT family |

**Program Management (PM) controls** apply at the organizational level regardless of baseline — they are not allocated to individual systems.

**Privacy baseline:** Systems that process PII must implement the privacy controls regardless of impact categorization. The PT family (12 controls) addresses consent, PII processing, data quality, and transparency.

---

## Step 3 — The 20 Control Families

> **Reference file:** `references/control-families.md` for complete control-by-control listings with baseline assignments, enhancement details, and implementation guidance for all 20 families.

| Family | ID | Controls | Key Focus |
|--------|----|----------|-----------|
| Access Control | AC | AC-1 to AC-25 | Least privilege, account management, remote access |
| Awareness & Training | AT | AT-1 to AT-6 | Security awareness, role-based training |
| Audit & Accountability | AU | AU-1 to AU-16 | Log generation, review, retention, protection |
| Assessment, Authorization & Monitoring | CA | CA-1 to CA-9 | Security assessments, authorization, continuous monitoring |
| Configuration Management | CM | CM-1 to CM-14 | Baselines, change control, software inventory |
| Contingency Planning | CP | CP-1 to CP-13 | BCP, disaster recovery, backup |
| Identification & Authentication | IA | IA-1 to IA-13 | MFA, authenticator management, identity proofing |
| Incident Response | IR | IR-1 to IR-10 | Incident handling, reporting, testing |
| Maintenance | MA | MA-1 to MA-6 | Controlled maintenance, remote maintenance |
| Media Protection | MP | MP-1 to MP-8 | Media access, sanitization, transport |
| Physical & Environmental | PE | PE-1 to PE-23 | Physical access, utilities, equipment |
| Planning | PL | PL-1 to PL-11 | Security/privacy plans, rules of behavior |
| Program Management | PM | PM-1 to PM-32 | Org-wide program; not baseline-specific |
| Personnel Security | PS | PS-1 to PS-9 | Screening, termination, sanctions |
| PII Processing & Transparency | PT | PT-1 to PT-8 | Consent, PII minimization, privacy notices |
| Risk Assessment | RA | RA-1 to RA-10 | Risk assessments, vulnerability monitoring, criticality |
| System & Services Acquisition | SA | SA-1 to SA-23 | Developer security, supply chain, SDLC |
| System & Communications Protection | SC | SC-1 to SC-51 | Boundary protection, encryption, network |
| System & Information Integrity | SI | SI-1 to SI-23 | Malware, patching, spam, error handling |
| Supply Chain Risk Management | SR | SR-1 to SR-12 | Acquisition strategies, provenance, component authenticity |

---

## Step 4 — Tailoring

Tailoring adjusts the selected baseline to match the system's specific operational environment:

### Tailoring Actions

1. **Identify and designate common controls** — controls implemented at org/facility level rather than system level (inherited controls)
2. **Apply scoping considerations** — remove controls not applicable (e.g., MA-4 remote maintenance if no remote maintenance exists)
3. **Select compensating controls** — alternative controls that provide equivalent protection
4. **Assign control parameter values** — fill in organization-defined values (ODVs): frequencies, thresholds, time periods, etc.
5. **Supplement the baseline** — add controls beyond the baseline for elevated risk scenarios

### Organization-Defined Values (ODVs) — Common Examples

| Control | ODV Parameter | Example Value |
|---------|--------------|---------------|
| AC-2(3) | Disable inactive accounts after [x] days | 90 days |
| AU-11 | Retain audit logs for [x] | 3 years |
| CA-7 | Continuous monitoring frequency | Monthly |
| IA-5(1) | Minimum password length [x] | 15 characters |
| SI-2 | Patch critical vulnerabilities within [x] days | 30 days |

---

## Step 5 — Overlays

Overlays tailor baselines for specific communities, technologies, or environments:

| Overlay | Use Case |
|---------|---------|
| **FedRAMP overlay** | Cloud services for federal agencies; adds FedRAMP-specific parameters |
| **DoD/CNSS** | National security systems (NSS); applies CNSS Instruction 1253 |
| **Intelligence Community** | IC-specific requirements via ICD 503 |
| **Privacy overlay** | Organizations processing large volumes of PII |
| **Industrial Control Systems** | OT/SCADA environments (see SP 800-82) |
| **Healthcare** | HIPAA-aligned overlay for health IT systems |

---

## Step 6 — Control Implementation and SSP Narratives

Each control requires an **SSP (System Security Plan) narrative** with three components:

### SSP Narrative Structure

```
Control: [AC-2] Account Management

Implementation Status: Implemented / Partially Implemented / Planned / Not Applicable

Implementation Description:
[Describe HOW the control is implemented for this specific system — 
technology, process, and people. Reference specific tools, policies, 
and procedures by name.]

Responsible Roles:
[ISSO, System Owner, IT Operations, etc.]

Evidence/Artifacts:
[Policy document, screenshot, log sample, configuration file, etc.]
```

**Common SSP pitfalls:**
- Generic statements ("We have a firewall") instead of system-specific implementation
- Not addressing all control parameters and ODVs
- Missing inherited vs. system-specific control designations
- Not distinguishing base control from enhancements

---

## Step 7 — Assessment (SP 800-53A Rev 5)

**SP 800-53A Rev 5** provides assessment procedures for every control. Three assessment methods:

| Method | Description |
|--------|-------------|
| **Examine** | Review documentation, specifications, policies, procedures |
| **Interview** | Discuss implementation with personnel (ISSO, admins, users) |
| **Test** | Exercise the control mechanism (scan, penetration test, configuration check) |

**Assessment findings:**
- **Satisfied** — control fully implemented and effective
- **Other Than Satisfied (OTS)** — weakness or deficiency found; document in POA&M

---

## Step 8 — RMF Integration and Framework Mapping

> **Reference file:** `references/assessment-rmf.md` for RMF step-by-step guidance, continuous monitoring strategy, OSCAL, and cross-framework mapping details.

### Risk Management Framework (RMF) — SP 800-37 Rev 2 Steps

| Step | Name | Key Output |
|------|------|-----------|
| 1 | **Prepare** | Risk management roles, system categorization, control selection strategy |
| 2 | **Categorize** | FIPS 199 system categorization (SC document) |
| 3 | **Select** | Baseline + tailoring = control selection (SSP control list) |
| 4 | **Implement** | SSP implementation descriptions |
| 5 | **Assess** | SAR (Security Assessment Report) using SP 800-53A |
| 6 | **Authorize** | ATO or DATO decision by Authorizing Official |
| 7 | **Monitor** | ConMon strategy; continuous assessment; POA&M management |

### Cross-Framework Mapping

| Framework | Relationship to SP 800-53 |
|-----------|--------------------------|
| **FedRAMP** | Uses SP 800-53 Moderate/High baseline + FedRAMP overlay parameters |
| **FISMA** | SP 800-53 is the mandatory control catalog for all federal systems |
| **CMMC 2.0** | Level 2 maps to NIST SP 800-171 (derived from SP 800-53 Moderate) |
| **ISO 27001:2022** | Annex A controls map to SP 800-53 families; significant overlap |
| **CSF 2.0** | CSF functions/subcategories map to SP 800-53 controls (SP 800-53B Appendix C) |
| **HIPAA** | Security Rule maps to SP 800-53 controls (HHS crosswalk) |
| **PCI DSS v4.0** | Requirements map to SC, IA, AC, AU, SI families |

---

## Reference Files

When deeper detail is needed, read these reference files:

| Reference | Contents |
|-----------|----------|
| `references/control-families.md` | All 20 families with key controls, baseline assignments (L/M/H), enhancement details, implementation tips, and common assessment findings |
| `references/baselines-tailoring.md` | SP 800-53B baseline tables, tailoring guidance, ODV examples, overlay application, and privacy/supply chain baseline specifics |
| `references/assessment-rmf.md` | SP 800-53A assessment procedures, RMF step-by-step, continuous monitoring, OSCAL guidance, POA&M management, and cross-framework mapping detail |

---

> *This skill provides general compliance information, not legal advice. Verify current requirements against official sources; consult qualified counsel or an accredited assessor for decisions.*

# HITRUST CSF Compliance Skill for Claude

A comprehensive Claude skill that provides expert HITRUST Common Security Framework (CSF)
compliance guidance for healthcare organisations, business associates, and technology vendors
operating in the US healthcare ecosystem.

> **Disclaimer:** This skill provides informational guidance only and does not constitute
> legal, regulatory, or formal certification advice. HITRUST certification requires engagement
> with a HITRUST Authorized External Assessor and submission through the official MyCSF
> portal. For formal compliance determinations, consult a qualified HITRUST Authorized
> External Assessor and, where required, qualified legal counsel.

---

## What Does This Skill Do?

The HITRUST CSF Compliance Skill transforms Claude into a knowledgeable HITRUST advisor
capable of handling the full range of questions that arise when an organization is pursuing,
maintaining, or renewing HITRUST certification.

At a high level, the skill does five things:

1. **Guides assessment type selection** — It helps organizations determine whether e1,
   i1, or r2 is the appropriate assessment based on their risk profile, organizational
   size, customer requirements, and regulatory context.

2. **Performs and supports gap analyses** — It produces structured gap assessments covering
   all 14 HITRUST CSF control categories (v9.x) and 156 control specifications, with
   status ratings, gap descriptions, CAP requirements, and prioritized remediation steps.

3. **Supports Corrective Action Plan (CAP) management** — It helps teams develop, document,
   and track CAPs for non-certifiable and near-certifiable findings, including root cause
   analysis and evidence planning.

4. **Generates HITRUST-aligned policies and procedures** — It produces ready-to-use policy
   and procedure documents mapped to specific HITRUST control categories and specifications,
   with all required document control elements.

5. **Explains HITRUST concepts, processes, and cross-framework mappings** — It translates
   HITRUST's prescriptive requirements into plain-language guidance, explains how HITRUST
   maps to HIPAA, NIST SP 800-53, ISO 27001, PCI DSS, SOC 2, and other frameworks, and
   advises on the inheritance program for cloud and third-party service providers.

The skill is backed by four detailed reference files covering the control domains, assessment
guide (e1/i1/r2 processes and scoring), scoping factors, and framework overview — loaded
selectively based on the specific question or task.

---

## Intended Audiences

| Audience | How They Use the Skill |
|----------|----------------------|
| **Healthcare Compliance Officers** | Understand HITRUST requirements, drive internal preparation, manage the assessment process, and answer organisational questions about certification obligations |
| **Security Engineers and Architects** | Get specific technical control guidance, understand encryption and access control requirements, map existing controls to HITRUST specifications |
| **Healthcare IT Teams** | Understand what evidence is needed for each control, prepare system documentation for assessor review, configure systems to meet prescriptive HITRUST requirements |
| **Health IT Vendors and SaaS Companies** | Determine if HITRUST is required for their customer base, select the right assessment type, understand what a certification programme involves |
| **Privacy Officers** | Focus on HITRUST Category 13 (Privacy Practices) and understand how HITRUST CSF incorporates HIPAA Privacy Rule obligations |
| **Risk Officers** | Understand the HITRUST risk management control category, support HITRUST risk assessment requirements, map HITRUST to the organisation's enterprise risk framework |
| **Procurement and Legal Teams** | Understand what a HITRUST certification letter means, how to verify certification status, and how to include HITRUST requirements in contracts and BAAs |

---

## Common Use Cases

### Assessment Type Selection
- "We're a business associate with about 500,000 patient records. What HITRUST assessment should we pursue?"
- "Our hospital customer is asking for HITRUST r2. What does that mean for us?"
- "What is the difference between e1, i1, and r2?"
- "We have a SOC 2 Type 2. Is that equivalent to HITRUST?"

### Gap Analysis
- "Perform a HITRUST r2 gap analysis against our current security programme"
- "Which HITRUST controls are we most likely to fail?"
- "We're a cloud-based EHR vendor. What HITRUST controls apply beyond the base set?"
- "Run a gap analysis against the HITRUST Category 01 Access Control domain"

### CAP Development and Management
- "We have 15 non-certifiable findings. Help us build CAPs for each one"
- "What do we need to remediate before scoring above 75 on 09.l.1 (Backup)?"
- "Write a CAP for our finding on 02.e.1 (Security Awareness Training)"
- "We have an open CAP on audit logging — what evidence do we need to close it?"

### Policy and Procedure Generation
- "Write a HITRUST-compliant Access Control Policy"
- "Generate an Information Security Policy that satisfies HITRUST category 04"
- "We need a vendor management policy that covers HITRUST 05.k controls"
- "Draft a Business Continuity Plan that meets HITRUST Category 12 requirements"
- "Write an incident response procedure that satisfies 11.c.1"

### Assessment Process Support
- "What happens during an r2 assessment?"
- "How long does HITRUST certification take?"
- "How do we select an Authorized External Assessor?"
- "What is MyCSF and how do we use it for our assessment?"
- "What does the HITRUST QA review involve?"

### Cross-Framework Mapping
- "We have SOC 2 Type 2. How much of HITRUST does that cover?"
- "Map our ISO 27001 controls to the equivalent HITRUST specifications"
- "How does HITRUST relate to HIPAA? Can we use HITRUST instead of a HIPAA risk analysis?"
- "Which HITRUST controls map to NIST SP 800-53 AC-2 (Account Management)?"

### Inheritance and Scoping
- "We use AWS for our infrastructure. Which HITRUST controls can we inherit?"
- "How does HITRUST inheritance work?"
- "Build a shared responsibility matrix for our AWS-hosted application"
- "We use Epic as our EHR. Can we inherit any HITRUST controls from them?"
- "What scoping factors determine how many r2 controls we'll have?"

---

## Skill Structure

| File | Content |
|------|---------|
| `SKILL.md` | Main skill file — assessment type guidance, workflows, maturity model, core use cases |
| `references/hitrust-control-domains.md` | Full listing of all 14 HITRUST CSF control categories, 49 objectives, and 156 control specifications with descriptions |
| `references/hitrust-assessment-guide.md` | e1/i1/r2 comparison, assessment process phases, maturity scoring model, CAP lifecycle, MyCSF platform, interim assessment requirements |
| `references/hitrust-scoping-factors.md` | r2 scoping questionnaire, risk factor categories, data volume tiers, technology factors, regulatory factors, inheritance program, shared responsibility matrix |
| `references/hitrust-framework-overview.md` | HITRUST Alliance history, CSF version history, HITRUST vs. HIPAA, HITRUST vs. SOC 2 / ISO 27001 / NIST SP 800-53, cross-framework control mapping, key terminology |

---

## How HITRUST Maps to Other Frameworks

HITRUST CSF is designed to incorporate and harmonise requirements from more than 40
authoritative frameworks and regulations. Key mappings include:

| Standard | Relationship to HITRUST |
|----------|------------------------|
| HIPAA Security Rule | Fully incorporated — all Security Rule specifications map to HITRUST controls |
| HIPAA Privacy Rule | Incorporated in Category 13 (Privacy Practices) |
| NIST SP 800-53 | Each HITRUST control cites the corresponding NIST control(s) |
| ISO/IEC 27001 / 27002 | Each HITRUST control cites corresponding ISO controls |
| PCI DSS | If PCI scoping factors apply, PCI requirements are incorporated |
| SOC 2 / AICPA TSC | Significant overlap with Security criteria; HITRUST has published mapping |
| NIST Cybersecurity Framework | HITRUST has published official CSF-to-NIST CSF mapping |
| CMS Acceptable Risk Safeguards | Incorporated for organizations with CMS data |

A robust HITRUST r2 certification substantially satisfies the security-related requirements
of HIPAA and provides meaningful evidence toward SOC 2, ISO 27001, and NIST compliance, but
does not replace framework-specific legal obligations or documentation requirements (e.g.,
a formal HIPAA risk analysis under 45 CFR 164.308(a)(1)).

---

## HITRUST Assessment Types at a Glance

| Feature | e1 | i1 | r2 |
|---------|-----|-----|-----|
| Controls | 44 fixed | 219 Defined Baseline | Variable (risk-tailored) |
| Certification period | 1 year | 1 year | 2 years |
| Maturity levels assessed | 3 | 3 | 5 |
| Minimum certifiable score | 62/100 | 62/100 | 62/100 |
| Assurance level | Entry / Basic | Moderate | Highest |
| Interim required | No | No | Yes (at 12 months) |
| Typical use | Foundational attestation; new to HITRUST | Established programme; moderate assurance | Major healthcare enterprises; customer-mandated |

---

## Installation

Install this skill in Claude Code by importing the `hitrust.skill` file through the
Claude Code plugin manager, or by placing the plugin directory in your Claude configuration.

For full installation instructions, see the repository
[INSTALLATION.md](../INSTALLATION.md).

# GovRAMP Security Authorization Skill for Claude

A Claude skill that provides expert, end-to-end guidance for GovRAMP authorization —
from impact level selection and gap assessment through documentation, 3PAO engagement,
government sponsorship, and ongoing continuous monitoring for state, local, education,
tribal, and special district (SLED) cloud deployments.

---

## What Does the Skill Do?

This skill turns Claude into a knowledgeable GovRAMP advisor. It covers the full
authorization lifecycle for Cloud Service Providers (CSPs) pursuing or maintaining a
GovRAMP security status under the current **NIST SP 800-53 Rev 5** baseline.

GovRAMP (formerly StateRAMP, doing business as GovRAMP since 2023) is a 501(c)(6)
nonprofit membership organization that provides standardized cybersecurity verification
and validation for cloud providers serving SLED organizations. It is based on the same
NIST 800-53 framework used by FedRAMP, with adaptations for the state-local context.

At a high level, the skill enables Claude to:

- **Determine the right impact level** using GovRAMP's Data Classification Tool logic
  (Low, Low+, Moderate, Moderate with CJIS Overlay, High)
- **Select the right authorization pathway**: Core, Ready, Authorized, Provisionally
  Authorized, Progressing Snapshot, or Fast Track for FedRAMP-authorized providers
- **Conduct readiness and gap assessments** against a structured 100+ item checklist
  across all NIST 800-53 Rev 5 control domains
- **Guide SSP documentation**: authorization boundary, control implementation statements,
  architecture diagrams, appendices (IRP, CP, POA&M)
- **Map the 60 Core controls** from the MITRE ATT&CK-aligned Moderate baseline for
  the GovRAMP Core status pathway (launched May 2025)
- **Support continuous monitoring (ConMon)** obligations: monthly deliverables for
  Ready/Authorized, quarterly for Core, annual assessment requirements, POA&M management
- **Explain the Fast Track** pathway for providers with existing FedRAMP authorization
- **Provide TX-RAMP reciprocity guidance** — GovRAMP Authorized products automatically
  qualify for TX-RAMP

The skill is current as of April 2026, incorporating the January 2026 Progressing
Snapshot Program changes, the GovRAMP Core status launch (May 2025), and the
February 2026 Rev 5 template updates.

---

## Intended Audiences

| Audience | How They Benefit |
|---|---|
| **Cloud Service Providers (CSPs)** | Navigate the authorization process, select the right pathway, write SSP narratives, manage POA&M, prepare for 3PAO assessments |
| **ISSOs / Security Engineers** | Map NIST 800-53 Rev 5 controls to implementations, identify gaps, manage ConMon activities |
| **Compliance Managers / GRC Teams** | Understand GovRAMP requirements, track remediation SLAs, coordinate documentation |
| **Cloud Architects** | Design systems that satisfy GovRAMP requirements; understand boundary scoping |
| **State / Local Government Officials** | Understand what to expect from a CSP's authorization, evaluate the APL, adopt GovRAMP for procurement |
| **3PAO Assessors** | Reference control family requirements, GovRAMP-specific test procedures, and document structure expectations |
| **Consultants / Advisory Firms** | Provide accurate GovRAMP guidance to SLED-facing clients across impact levels and authorization phases |
| **Small Business Providers** | Navigate GovRAMP with limited resources; understand Core as an accessible entry point |

---

## Common Use Cases

### 1. Impact Level Determination
> *"Our SaaS product handles voter registration data for a county clerk's office. What GovRAMP impact level do we need?"*

The skill applies FIPS 199 categorization logic and GovRAMP data classification principles
to recommend Low+, Moderate, or High, and explains whether the CJIS Overlay applies.

### 2. Pathway Selection
> *"We're a startup with limited budget. We can't afford a 3PAO right now but want to be on the GovRAMP APL. What are our options?"*

The skill explains GovRAMP Core (60 controls, PMO-reviewed, no 3PAO required, launched
May 2025) as the most accessible verified status, and compares it against the
Progressing Snapshot for even earlier-stage providers.

### 3. Fast Track for FedRAMP-Authorized Providers
> *"We're already FedRAMP Moderate authorized. How do we get GovRAMP status quickly?"*

The skill walks through the Fast Track pathway: submitting existing federal security
documentation to the GovRAMP PMO, 90-day ConMon data requirements, and what GovRAMP-
specific templates may still be needed.

### 4. Gap Assessment
> *"We're a mid-size SaaS company targeting GovRAMP Authorized Moderate. Help us assess our readiness."*

The skill guides a structured gap assessment across all control domains, producing a
prioritized gap table with status, gap description, and recommended next steps.

### 5. SSP Control Narrative Writing
> *"Help me write the GovRAMP control implementation statement for AC-2 (Account Management)."*

The skill generates reviewer-ready prose that addresses every verb in the control
requirement, distinguishes provider vs. customer responsibilities, and references
specific tools and policies.

### 6. POA&M Entry Creation
> *"Our vulnerability scan flagged a critical CVE on one of our app servers. Help me build the POA&M entry."*

The skill produces a complete POA&M row: finding ID, control affected, risk rating,
remediation plan, owner, milestone dates, and SLA calculation (30 days for Critical).

### 7. Continuous Monitoring Guidance
> *"We just got GovRAMP Authorized status. What do we need to submit every month?"*

The skill explains all monthly ConMon deliverables: scan results (OS, DB, web app),
POA&M update, asset inventory update, and monthly summary report, with references to
the GovRAMP Continuous Monitoring Guide.

### 8. TX-RAMP Reciprocity
> *"We serve Texas state agencies. Do we need TX-RAMP separately?"*

The skill explains that TX-RAMP automatically recognizes GovRAMP-authorized products,
with GovRAMP providing a weekly sync. Once GovRAMP Authorized, no separate TX-RAMP
process is required.

### 9. CJIS Overlay Guidance
> *"A police department wants to use our platform to manage evidence photos. What additional requirements apply?"*

The skill explains the GovRAMP Moderate Impact with CJIS Overlay: additional FBI CJIS
Security Policy requirements, the dedicated Service Provider and 3PAO packages, and
data isolation requirements for Criminal Justice Information.

### 10. Government Adoption Guidance
> *"We're a state IT office considering requiring GovRAMP for all cloud procurements. How do we get started?"*

The skill explains the GovRAMP adoption roadmap for government organizations, the APL
procurement workflow, ConMon portal access for ongoing oversight, and committee/working
group participation opportunities.

---

## Skill Coverage

| Topic | Covered |
|-------|---------|
| GovRAMP background & governance | Yes |
| Impact levels: Low, Low+, Moderate, CJIS, High | Yes |
| Progressing Snapshot Program (including Jan 2026 changes) | Yes |
| GovRAMP Core status (launched May 2025; 60 controls) | Yes |
| GovRAMP Ready status | Yes |
| GovRAMP Authorized / Provisionally Authorized | Yes |
| Fast Track for FedRAMP-authorized providers | Yes |
| TX-RAMP reciprocity | Yes |
| NIST 800-53 Rev 5 control families (all 20) | Yes |
| Core 60-control set with MITRE ATT&CK alignment | Yes |
| SSP writing guidance | Yes |
| IRP and CP requirements | Yes |
| POA&M management and SLAs | Yes |
| Vulnerability scanning requirements | Yes |
| Penetration testing guidance | Yes |
| Continuous monitoring (monthly, quarterly, annual) | Yes |
| ConMon escalation process | Yes |
| Incident reporting procedures | Yes |
| Government sponsorship and Approvals Committee | Yes |
| GovRAMP membership and pricing | Yes |
| Authorization boundary guidance | Yes |
| CJIS Overlay requirements | Yes |
| Cross-framework alignment (FedRAMP, SOC 2, ISO 27001, NIST CSF) | Yes |
| Common findings and pitfalls | Yes |

---

## Installation

This skill can be installed in Claude using the `.skill` file format. The skill
archive contains:

```
govramp/
├── SKILL.md                          Main skill instructions
└── references/
    ├── readiness-checklist.md        100+ item readiness checklist
    ├── status-pathways.md            Status pathway decision guide
    ├── ssp-guide.md                  SSP section-by-section writing guide
    ├── conmon-guide.md               Continuous Monitoring guide
    └── control-mapping.md            NIST 800-53 Rev 5 control mapping
```

---

## Source and Accuracy

All GovRAMP-specific information in this skill is sourced from official GovRAMP
materials published at https://govramp.org, including:

- https://govramp.org/about-us/
- https://govramp.org/providers/
- https://govramp.org/providers/core/
- https://govramp.org/providers/ready-or-authorized-process/
- https://govramp.org/providers/authorized/
- https://govramp.org/providers/progressing-snapshot/
- https://govramp.org/providers/fast-track/
- https://govramp.org/governments/
- https://govramp.org/rev-5-templates-and-resources/

NIST 800-53 Rev 5 control information is sourced from the official NIST publication.

> **Disclaimer:** This skill is for informational and educational purposes only and
> does not constitute official GovRAMP authorization guidance. Always engage the
> GovRAMP PMO (pmo@govramp.org) and, where required, a GovRAMP-approved 3PAO for
> official assessment and authorization activities. GovRAMP is not endorsed by or
> affiliated with FedRAMP or the United States Government.

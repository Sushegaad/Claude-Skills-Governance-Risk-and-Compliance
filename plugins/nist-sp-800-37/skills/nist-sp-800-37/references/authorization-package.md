# NIST SP 800-37 Rev 2 — Authorization Package, SSP, SAR, and POA&M

Source: NIST Special Publication 800-37 Rev 2, December 2018

---

## Authorization Package Overview

The **authorization package** is the collection of documents presented to the Authorising Official (AO) to support an ATO decision. Per SP 800-37 Rev 2, Task R-1, the package must include:

| Required Document | Owner | Description |
|------------------|-------|-------------|
| System Security Plan (SSP) | SO / ISSO | Complete system description, boundary, categorisation, environment, interconnections, and all control implementation narratives |
| Security Assessment Report (SAR) | SCA | Findings from independent assessment of all selected controls |
| Plan of Action and Milestones (POA&M) | ISSO / SO | All open weaknesses with remediation plans and milestones |
| Executive Summary | ISSO | Brief risk posture summary for AO decision-making |

**Optional/conditional documents:**
| Document | When Required |
|----------|--------------|
| Privacy Plan | When system processes PII or is subject to the Privacy Act |
| Privacy Impact Assessment (PIA) | When system processes PII (E-Government Act requirement) |
| Supply Chain Risk Management Plan | When system acquisition involves significant supply chain risk |
| Risk Assessment Report | When conducted as a separate artefact |
| Interconnection Security Agreements (ISAs) | For each system interconnection |
| MOU/MOA | When the system depends on another organisation's resources |
| Contingency Plan | For systems with operational continuity requirements |
| Contingency Plan Test Results | For systems with tested continuity plans |

---

## System Security Plan (SSP) — Document Template

### Required SSP Sections (per SP 800-37 Rev 2 and NIST template)

**Section 1 — System Identification**
| Field | Content |
|-------|---------|
| System Name | |
| System Identifier | |
| Responsible Organisation | |
| System Owner | Name, title, organisation, contact |
| ISSO | Name, title, organisation, contact |
| Authorising Official | Name, title, organisation |
| System Operational Status | Operational / Under Development / Major Modification |
| System Type | Major Application / General Support System / Minor Application |
| System Environment | Cloud (CSP, service model, deployment model) / On-premises / Hybrid |

**Section 2 — System Description**
- System purpose and functions
- System architecture (narrative + diagrams)
- System boundary description
- Information types processed, stored, transmitted

**Section 3 — System Categorisation**
```
Security Category: SC = {Confidentiality: [LOW/MODERATE/HIGH],
                          Integrity:       [LOW/MODERATE/HIGH],
                          Availability:    [LOW/MODERATE/HIGH]}
Overall Impact Level: [LOW / MODERATE / HIGH]
Basis: [SP 800-60 information type analysis — summarise here]
```

**Section 4 — System Environment**
- Description of physical and technical environment
- Locations of system components
- Network topology and boundary diagrams
- System interconnections table

| Connected System | Org | Direction | Data Types | ISA/MOU Status |
|-----------------|-----|-----------|-----------|----------------|

**Section 5 — Users and Roles**
| Role | Description | Access Level | Training Required |
|------|-------------|-------------|------------------|

**Section 6 — Security Control Implementation**
For each selected control:
```
Control: [ID] [Name]
Baseline:        [Low / Moderate / High]
Implementation Status: [Implemented / Planned / Inherited / Not Applicable]
Control Type:    [System-Specific / Common (Inherited) / Hybrid]
Inherited From:  [CCP name, if applicable]
Implementation Description: [How the control is implemented]
Responsible Party: [Organisation unit]
```

**Section 7 — Authorisation Date and Signature**
- ATO date
- ATO expiry date (or statement of ongoing authorisation)
- AO signature

---

## Security Assessment Report (SAR) — Structure

Per SP 800-53A and SP 800-37 Task A-4:

**Section 1 — Executive Summary**
- System name, boundary, and categorisation
- Overall security posture summary
- Count of findings by severity (Critical / High / Moderate / Low / Informational)
- Key risks requiring AO attention

**Section 2 — Assessment Scope and Methodology**
- Controls assessed
- Assessment period
- Assessment methods used (examine, interview, test)
- Depth and coverage
- Limitations and constraints

**Section 3 — Assessment Findings**

For each control assessed:
```
Control ID:    [e.g., AC-2]
Control Name:  [Account Management]
Finding:       [Satisfied / Other Than Satisfied / Not Applicable]
Method:        [Examine / Interview / Test]
Artefacts:     [List of evidence reviewed]
Deficiency:    [Description of what is missing or not working correctly]
Severity:      [Critical / High / Moderate / Low / Informational]
Risk Level:    [Very High / High / Moderate / Low / Very Low]
Recommendation: [Specific remediation recommendation]
```

**Section 4 — Summary of Risks**
Table of all findings rated High or above with risk determination.

---

## Plan of Action and Milestones (POA&M) — Format

Per OMB Memorandum M-02-01 and NIST SP 800-37 Task A-5:

| Field | Description |
|-------|-------------|
| POA&M ID | Unique sequential identifier (e.g., P-001) |
| System Name | System this applies to |
| Control ID | SP 800-53 control(s) this weakness relates to |
| Weakness Description | Clear description of the identified deficiency |
| Category | Technical / Operational / Management |
| Weakness Severity | Critical / High / Moderate / Low |
| Detection Source | SAR / Audit / Incident / Self-Identified / Pen Test |
| Date Identified | When the weakness was first identified |
| Scheduled Completion Date | Target date for full remediation |
| Milestones | Intermediate milestones with dates |
| Milestone # | Milestone description | Target date |
| Status | Open / In Progress / Partially Completed / Completed / Risk Accepted |
| Responsible POC | Name and contact for remediation owner |
| Resources Required | Budget, staff, tools |
| Comments | Additional context, dependencies, risk acceptance notes |

### POA&M Management Requirements
- All findings from SAR with status "Other Than Satisfied" must appear in the POA&M
- POA&M must be reviewed and updated at minimum quarterly
- Critical/Very High risk findings require AO attention within 15 days
- All POA&M items must have realistic, achievable milestone dates
- Completed items retained for at least 3 years

---

## Authorization Decision Documentation

### ATO Memo Contents
1. System name, identifier, and boundary description
2. Security categorisation result
3. Summary of residual risks accepted
4. Open POA&M items and their risk status
5. Conditions placed on the authorisation (if any)
6. Authorization term (date of issue to expiry date, or statement of ongoing authorisation)
7. AO signature and date

### Authorization Conditions
The AO may place conditions on authorization, such as:
- Specific POA&M items must be resolved within X days
- Specific monitoring metrics must be reported monthly
- No additional external connections without AO approval
- Penetration test required within 180 days

### Risk Acceptance Statement
When accepting residual risk, the AO documents:
- The specific risk(s) being accepted
- Rationale for acceptance (operational necessity, compensating controls, low exploitability)
- Any compensating controls in place
- Review date when acceptance will be reconsidered

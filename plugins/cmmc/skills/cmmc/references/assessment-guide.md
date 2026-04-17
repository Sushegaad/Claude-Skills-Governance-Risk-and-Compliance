# CMMC 2.0 Assessment Guide
## C3PAO Assessment Process, SPRS Scoring, and Evidence Requirements
## Source: CMMC 2.0 Assessment Process, NIST SP 800-171A, DoD Assessment Methodology

---

## Overview

This guide covers the end-to-end CMMC 2.0 assessment process, how to prepare for a
C3PAO-led assessment, how the SPRS score is calculated and submitted, POA&M requirements,
and the evidence an assessor will expect to find for each domain.

---

## Part 1: The Cyber-AB and C3PAO Ecosystem

### The Cyber-AB (CMMC Accreditation Body)

The **Cyber-AB** (formerly The Accreditation Body, CMMC-AB) is the official accreditation
body authorized by DoD to accredit CMMC Third-Party Assessment Organizations (C3PAOs),
Registered Practitioners (RPs), Registered Practitioner Organizations (RPOs), and
Licensed Partner Advisors (LPAs).

**Cyber-AB Marketplace:** https://cyberab.org/Catalog/
Use this portal to find and validate:
- Authorized C3PAOs (currently certified)
- Certified CMMC Assessors (CCAs or Provisional Assessors)
- Registered Practitioners (for consulting/advisory work)

### C3PAO (Certified Third-Party Assessment Organization)

A C3PAO is an organization licensed by the Cyber-AB to conduct CMMC Level 2 assessments.
They employ **Certified CMMC Assessors (CCAs)** who carry the Lead Assessor or Assessor role.

**Selection criteria for an OSC choosing a C3PAO:**
- Must be listed on the Cyber-AB Marketplace as Authorized (active status)
- Must have enough licensed CCAs to staff the assessment
- Conflict of interest: cannot have provided consulting to the OSC within past 3 years
- Verify insurance and bonding requirements

---

## Part 2: Level 2 C3PAO Assessment Process in Detail

### Phase 1: Pre-Assessment Preparation (OSC Responsibility)

**Minimum deliverables before requesting C3PAO:**

| Document | Description |
|---------|-------------|
| System Security Plan (SSP) | Current, complete narrative for all 110 practices |
| POA&M | All known deficiencies documented with target dates |
| SPRS Score | Score submitted to DIBNet; must reflect current status |
| Network Diagram | Boundary and network architecture |
| Data Flow Diagram | CUI flow through the environment |
| Asset Inventory | All hardware and software within scope |
| Policy Set | All required policies and procedures |
| Evidence Package | Artifacts for each practice (see Part 4) |

**Self-Assessment before C3PAO:**
Organizations should conduct a thorough internal self-assessment using NIST SP 800-171A
assessment procedures. Each practice has three assessment methods defined in SP 800-171A:
- **Examine** — Review documents, specifications, records, reports
- **Interview** — Discuss with personnel responsible for the practice
- **Test** — Exercise mechanisms, processes, activities

### Phase 2: C3PAO Engagement and Scoping Agreement

1. **Contract with C3PAO** — Sign engagement agreement; C3PAO firm quote for assessment
2. **Review Package Submission** — OSC provides SSP and key documents to C3PAO pre-assessment team
3. **Scope Alignment Meeting** — C3PAO and OSC agree on in-scope assets, boundaries, locations
4. **Assessment Plan** — C3PAO produces assessment plan including:
   - Assessment dates and schedule
   - Personnel to be interviewed
   - Systems to be tested
   - Documentation to be reviewed

### Phase 3: Assessment Execution

**Assessment methods per NIST SP 800-171A:**

For each of the 110 practices, assessors will apply one or more of:
- **Examine** — Review policy documents, configuration records, system logs, screenshots,  
  audit trails, inventory records, training completion certificates
- **Interview** — Discussion with system owners, security personnel, administrators, users
- **Test** — Technical testing: log generation, account lockout behavior, patching,  
  network scans, encryption verification

**Practice determination for each requirement:**
- **MET** — Practice is fully implemented; evidence confirms implementation
- **NOT MET** — Practice is not implemented or evidence is insufficient

**Assessment findings categories:**
- **No deficiency** (MET)
- **Deficiency requiring POA&M** (potentially allowable for conditional certification)
- **High-risk deficiency** (may preclude conditional certification)

### Phase 4: Post-Assessment Results and Certification

**Outcome categories:**

| Outcome | Meaning | Next Steps |
|---------|---------|-----------|
| CMMC Level 2 Certified | All 110 practices MET | C3PAO submits to eMASS; DoD issues certificate |
| Conditional CMMC Level 2 | Some NOT MET but no high-risk deficiencies | POA&M must close within 180 days; C3PAO verifies closure |
| Not Certified | High-risk deficiencies present or too many NOT MET | Remediate and reschedule full assessment |

**High-risk practices (Not MET = cannot achieve conditional certification):**
Practices that are deemed high risk and preclude conditional status include those that
fundamentally undermine CUI protection. DoD publishes high-risk practice definitions.

**Certificate submission:**
- C3PAO submits assessment results to the **CMMC Enterprise Mission Assurance Support
  Service (eMASS)** portal managed by DoD
- DoD CIO issues the CMMC certificate
- Certificate is valid for **3 years** from issuance date

### Phase 5: Annual Affirmation and Ongoing Compliance

**Annual Affirmation Process:**
1. Senior company official (CEO, CISO, or equivalent) reviews current compliance status
2. Confirms no degradation has occurred since certification (or documents any changes)
3. Submits affirmation via the **DIBNet portal** (https://dibnet.dod.mil)
4. Affirmation occurs annually throughout the 3-year certificate period

**Triggering events requiring disclosure:**
- Significant cyber incidents affecting the CUI environment
- Material changes to system boundary
- Acquisition or divestiture of business units in scope
- Discovery of practices that are no longer MET

---

## Part 3: SPRS Score — Calculation and Submission

### Overview

The **Supplier Performance Risk System (SPRS)** score represents an organization's self-assessed
implementation of NIST SP 800-171 Rev 2. It is required under DFARS 252.204-7019/7020 and
must be submitted before contract award.

**Source methodology:** NIST SP 800-171 DoD Assessment Methodology, Version 1.2.1

### Scoring Methodology

- **Starting score: 110** (all practices implemented)
- Each practice NOT implemented is subtracted based on its assigned weight
- A practice assessed as **Partial** is treated as **NOT MET** for SPRS purposes
- **Minimum score: -203** (all practices NOT MET, maximum deductions)

### Practice Weights for SPRS Deduction

The DoD Assessment Methodology assigns one of three deduction values to each practice.
Practices are not weighted by domain but by their security impact.

**Value 1 (-1 point for NOT MET) — 77 practices are weighted at 1 point**
These are practices where the risk of non-implementation is lower or the control is
compensated by other practices. This includes most AU, AT, MA, PS, and single PE practices.

**Value 3 (-3 points for NOT MET) — 15 practices are weighted at 3 points**
Mid-tier impact practices, including core AC, IA, CM, and SI practices.

**Value 5 (-5 points for NOT MET) — 18 practices are weighted at 5 points**
High-impact practices where non-implementation creates significant CUI risk:

| Practice | Domain | Reason for -5 Weight |
|---------|--------|---------------------|
| AC.L2-3.1.3 | AC | CUI flow control |
| AC.L2-3.1.5 | AC | Least privilege |
| AC.L2-3.1.12 | AC | Remote access monitoring |
| AC.L2-3.1.13 | AC | Remote access encryption |
| AC.L2-3.1.14 | AC | Remote access via managed access points |
| IA.L2-3.5.3 | IA | Multi-factor authentication |
| SC.L2-3.13.8 | SC | Data in transit encryption |
| SC.L2-3.13.11 | SC | FIPS-validated encryption |
| SC.L2-3.13.16 | SC | CUI at rest encryption |

**Note:** The full weighting table for all 110 practices is in DoD Assessment Methodology v1.2.1
at https://www.dodcio.defense.gov/CMMC/Resources/

### Submitting SPRS Score

1. Register on **DIBNet portal** at https://dibnet.dod.mil
2. Navigate to SPRS module
3. Enter score, assessment date, assessment type (basic/medium/high), and scope
4. Affirmation by authorized government representative (for self-assessment)
5. Score is visible to DoD contracting officers for source selection

### Score Interpretation

| Score Range | Interpretation | Action Required |
|------------|---------------|----------------|
| 110 | All practices implemented | Maintain and affirm annually |
| 88 – 109 | Minor deficiencies | POA&M required; address before C3PAO assessment |
| 70 – 87 | Moderate deficiencies | Significant remediation; extended POA&M |
| 0 – 69 | Major deficiencies | Substantial program needed; high contractual risk |
| Negative | Severe deficiencies | Fundamental gaps; unlikely to pass C3PAO assessment |

---

## Part 4: Evidence Requirements by Domain

The following lists the primary evidence an assessor will expect for each domain during
a Level 2 C3PAO assessment.

### Access Control (AC)

| Practice Area | Evidence Expected |
|--------------|------------------|
| User account management | Active Directory export or IAM platform user list with roles |
| Session lock | Group Policy Object (GPO) or MDM configuration showing idle timeout and lock |
| Remote access | VPN solution configuration, MFA enabled for VPN, access logs |
| Wireless access | Wi-Fi configuration (WPA2/3 Enterprise), network access control records |
| Mobile devices | MDM policy, encryption enforcement configuration |
| CUI flow control | Data flow diagram, information flow policies, DLP configuration if present |

### Audit and Accountability (AU)

| Practice Area | Evidence Expected |
|--------------|------------------|
| Audit logging | SIEM or log management configuration, enabled audit policies |
| Log retention | Log retention policy (minimum 90 days accessible, longer archived) |
| Time synchronization | NTP configuration pointing to authoritative source |
| Audit protection | SIEM access controls, log storage permissions |

### Configuration Management (CM)

| Practice Area | Evidence Expected |
|--------------|------------------|
| System inventory | CMDB, asset management tool export, or spreadsheet with all in-scope assets |
| Configuration baselines | STIG/CIS Benchmark application records, GPOs |
| Change management | Change management system (tickets), change approval records |
| Software allowlisting | Application control policy, allowlist configuration |

### Identification and Authentication (IA)

| Practice Area | Evidence Expected |
|--------------|------------------|
| MFA for privileged accounts | MFA configuration screenshots (Duo, Azure MFA, etc.) |
| MFA for all remote access | VPN authentication configuration showing MFA required |
| Password policy | Password complexity policy configuration (AD, Azure AD, or equivalent) |
| Account management | Account provisioning/de-provisioning procedures and recent records |

### Incident Response (IR)

| Practice Area | Evidence Expected |
|--------------|------------------|
| IRP documentation | Signed incident response plan with current date |
| IRP testing | Tabletop exercise records, test completion certificates |
| DFARS reporting | DIBNet registration confirmation, incident reporting procedure |

### Maintenance (MA)

| Practice Area | Evidence Expected |
|--------------|------------------|
| Maintenance logs | Ticketing system records for scheduled and unscheduled maintenance |
| Remote maintenance | Remote session logs, MFA for remote maintenance sessions |
| Equipment sanitization | Media sanitization records for equipment removed for repair |

### Media Protection (MP)

| Practice Area | Evidence Expected |
|--------------|------------------|
| Media inventory | Inventory of removable media (USB drives, external drives) |
| Media encryption | BitLocker or equivalent encryption configuration |
| Disposal records | Certificate of data destruction for disposed media |

### Risk Assessment (RA)

| Practice Area | Evidence Expected |
|--------------|------------------|
| Risk assessment | Formal risk assessment report dated within past 3 years |
| Vulnerability scanning | Vulnerability scan reports (Nessus, Qualys, Rapid7, etc.), dated |
| Remediation tracking | Vulnerability remediation tracking records (patch tickets, scan deltas) |

### Security Assessment (CA)

| Practice Area | Evidence Expected |
|--------------|------------------|
| Security assessment | Internal security assessment records, third-party assessment reports |
| POA&M | Current POA&M with open/closed items, target dates, owners |
| SSP | Complete, current System Security Plan covering all 110 practices |

### System and Communications Protection (SC)

| Practice Area | Evidence Expected |
|--------------|------------------|
| Firewall/boundary | Firewall rule export, network architecture diagram |
| Encryption in transit | TLS configuration (1.2 minimum), certificate inventory |
| Encryption at rest | BitLocker, Database encryption configuration, cloud storage encryption |
| FIPS validation | FIPS 140-2/3 certificate numbers for cryptographic modules used |
| Split tunneling disabled | VPN configuration showing full-tunnel for remote access clients |

### System and Information Integrity (SI)

| Practice Area | Evidence Expected |
|--------------|------------------|
| Patch management | Patch management tool reports, patching SLA documentation |
| Malware protection | EDR/AV deployment report showing all in-scope endpoints covered |
| AV definitions | AV console showing definition update status and last update date |
| Security monitoring | SIEM alert rules, SOC procedures, monitoring coverage documentation |

---

## Part 5: POA&M Management

### POA&M Requirements

A Plan of Action and Milestones (POA&M) is **required** for every CMMC practice that is
NOT MET or only partially implemented at the time of assessment.

**Official requirement:** CMMC 2.0 allows **conditional certification** if:
- The NOT MET practice items do not include high-risk practices
- A POA&M is in place with realistic remediation milestones
- ALL POA&M items must be closed and verified within **180 days** of conditional certificate issuance

### POA&M Format

| Field | Description |
|-------|-------------|
| Item ID | Unique identifier (e.g., POA&M-001) |
| Practice ID | CMMC practice (e.g., AC.L2-3.1.5) |
| Practice Title | Description of the requirement |
| Weakness/Gap | Description of what is not implemented and why |
| Point of Contact | Name and role of person responsible for remediation |
| Resources Required | Budget, tools, personnel needed |
| Scheduled Completion Date | Realistic target date (must be within 180 days for conditional cert) |
| Status | Open / In Progress / Closed (with closure date and verification) |
| Milestones | Intermediate steps toward closure |

### POA&M Closure Verification

When a POA&M item is closed:
- Record the actual completion date
- Document what was implemented
- Reference evidence artifacts (e.g., screenshot, configuration export, policy document)
- Assessor or independent reviewer verifies closure before submitting to eMASS

---

## Part 6: CMMC Contract Clause Summary

| Clause | When Included | Key Requirement |
|--------|--------------|----------------|
| FAR 52.204-21 | When contractor will process FCI | Implement 15 basic safeguarding requirements |
| DFARS 252.204-7012 | When contractor processes covered defense information | Safeguard; report incidents to DoD within 72 hours |
| DFARS 252.204-7019 | Most contracts | Perform and post SPRS score before award |
| DFARS 252.204-7020 | Contracts requiring DoD-assessed score | Allow DoD to conduct assessment; medium/high methodology |
| DFARS 252.204-7021 | Contracts requiring CMMC certification | Achieve and maintain CMMC level specified; flow-down to subcontractors |

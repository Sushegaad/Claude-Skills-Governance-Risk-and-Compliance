# CMMC 2.0 - Assessment Guide: SPRS Scoring, C3PAO Process & POA&M Rules

## SPRS Score Calculation

### Scoring Methodology
The SPRS score is calculated per the DoD Assessment Methodology for NIST SP 800-171:
- **Starting score**: 110 points
- **Each NOT MET practice**: Deduct the assigned point value
- **Partial implementation**: Full deduction applies (no partial credit)
- **Score range**: +110 (all practices met) to −203 (all not met)
- **Submission**: Required for all Level 2 contracts; submit at sprs.csd.disa.mil

### Point Values by Domain
Point values are assigned based on the practice's security impact:

| Domain | Practices | Total Points at Risk |
|--------|-----------|---------------------|
| AC (Access Control) | 22 | ~50 |
| AU (Audit & Accountability) | 9 | ~17 |
| CM (Configuration Management) | 9 | ~19 |
| IA (Identification & Authentication) | 11 | ~22 |
| IR (Incident Response) | 3 | ~5 |
| MA (Maintenance) | 6 | ~11 |
| MP (Media Protection) | 9 | ~8 |
| PE (Physical Protection) | 6 | ~11 |
| PS (Personnel Security) | 2 | ~4 |
| RA (Risk Assessment) | 3 | ~9 |
| CA (Security Assessment) | 4 | ~9 |
| SC (System & Communications) | 16 | ~39 |
| SI (System & Information Integrity) | 7 | ~14 |

*Exact point values per practice are published in the DoD Assessment Methodology, Version 1.2.1 (June 2020).*

### Highest-Impact Practices (Largest Point Deductions)
Prioritize these when remediating - they carry the heaviest scoring weight:
1. **IA.L2-3.5.3** - Multifactor authentication (5 pts)
2. **SI.L2-3.14.6** - Monitoring for attacks (5 pts)
3. **AU.L2-3.3.1** - Audit logging (5 pts)
4. **CM.L2-3.4.1** - Baseline configuration (5 pts)
5. **SC.L2-3.13.8** - Encryption in transit (3 pts)
6. **SC.L2-3.13.11** - FIPS-validated cryptography (3 pts)
7. **AC.L2-3.1.5** - Least privilege (3 pts)

Note: **AC.L2-3.1.3** (CUI flow control) is a **1-point** requirement under the methodology.

---

## C3PAO Assessment Process

### Pre-Assessment (Contractor Responsibilities)
Before engaging a C3PAO, ensure:
- [ ] System Security Plan (SSP) is complete and covers all 110 practices
- [ ] System boundary is defined with network diagrams
- [ ] CUI data flows are documented
- [ ] POA&M lists all practices not yet met
- [ ] SPRS score has been self-calculated
- [ ] Personnel responsible for each practice are identified

### Assessment Phases

**Phase 1 - Documentation Review (Remote)**
- C3PAO reviews SSP, network diagrams, policies, and POA&M
- Requests artifact list: logs, screenshots, configuration exports, training records
- Duration: 2–4 weeks

**Phase 2 - Assessment Activities (On-site or Remote)**
- Interviews with system administrators, security personnel, and executives
- Technical testing: vulnerability scans, configuration reviews, access control verification
- Observation of processes (incident response tabletop, maintenance procedures)
- Duration: 1–3 weeks depending on scope

**Phase 3 - Findings and Reporting**
- C3PAO issues Findings Report: MET, NOT MET, or NOT APPLICABLE per practice
- Contractor may provide additional evidence for disputed findings (limited window)
- Final assessment results entered in CMMC eMASS and reflected in SPRS

**Phase 4 - Certification Decision**
- **All 110 practices MET**: Full certification issued; valid 3 years
- **Limited unmet practices (non-critical)**: Conditional certification with POA&M; must remediate within 180 days
- **Critical practices unmet**: No certification; remediate and reschedule

### POA&M Eligibility Rule (32 CFR 170.21(a)(2))
A Level 2 POA&M is permitted only when:
- The assessment score is at least **0.8 × 110 (88)**, AND
- Every open item is a **1-point** requirement, with one exception: **SC.L2-3.13.11** (CUI encryption, a 3-point requirement) MAY be on a POA&M when encryption is employed but is not FIPS-validated

**Six requirements may NEVER be on a POA&M:**
- AC.L2-3.1.20 (External connections)
- AC.L2-3.1.22 (Publicly accessible content)
- CA.L2-3.12.4 (System security plan)
- PE.L2-3.10.3 (Escort visitors)
- PE.L2-3.10.4 (Physical access logs)
- PE.L2-3.10.5 (Physical access devices)

---

## POA&M Rules and Management

### What Can Be in a POA&M at Certification
- Level 2: only the POA&M-eligible items above (score ≥88; 1-point items plus the SC.L2-3.13.11 exception; never the six barred requirements)
- POA&M remediation deadline: **180 days** from certification date
- Failure to remediate = certification revocation
- Level 3: Conditional Level 3 is permitted (32 CFR 170.21(a)(3)); a POA&M may not include IR.L3-3.6.1e, IR.L3-3.6.2e, RA.L3-3.11.1e, RA.L3-3.11.4e, RA.L3-3.11.6e, RA.L3-3.11.7e, or SI.L3-3.14.3e

### POA&M Entry Format

| Field | Description |
|-------|-------------|
| Practice ID | CMMC practice identifier (e.g., CM.L2-3.4.2) |
| Weakness Description | What is not implemented and why |
| Remediation Steps | Specific actions to achieve compliance |
| Milestone 1–N | Intermediate checkpoints with dates |
| Scheduled Completion | Target date for full implementation |
| Resources Required | Personnel, tools, budget |
| Status | Open / In Progress / Completed |
| Evidence of Closure | What artifacts will demonstrate completion |

### POA&M Best Practices
- Never list one of the six barred requirements (AC.L2-3.1.20, AC.L2-3.1.22, CA.L2-3.12.4, PE.L2-3.10.3/4/5) in a POA&M if seeking certification
- Update monthly; stale POA&Ms raise auditor concerns
- Link each POA&M item to the relevant SSP section
- Document root cause, not just the symptom

---

## Evidence Requirements by Practice Type

### Documentary Evidence (policies, procedures, plans)
- Acceptable formats: PDF, Word, screenshots with metadata
- Must show: author, date, version, approval signature
- Examples: SSP, access control policy, incident response plan, training records

### Technical Evidence (system configuration, logs)
- Configuration exports from firewalls, Active Directory, SIEM
- Vulnerability scan reports (authenticated scans preferred)
- MFA enrollment reports showing all privileged user enrollment
- Patch management reports showing remediation timelines

### Interview Evidence
- Assessors will interview: ISSO/ISSM, system admins, end users, executives
- Prepare personnel to describe their security responsibilities
- Cannot substitute documentation for interview - both required

---

## DIBNET Incident Reporting (DFARS 7012)

DFARS 252.204-7012 mandates cyber incident reporting regardless of CMMC level:
- **Report to**: DIBNET portal (dibnet.dod.mil)
- **Deadline**: Within **72 hours** of discovering the incident
- **What to report**: Systems affected, CUI categories involved, attack vectors, forensic indicators
- **Preserve evidence**: Maintain disk images and forensic evidence for 90 days; DoD may request copies
- **Notify prime**: If you are a subcontractor, notify the prime who notifies DoD

### What Constitutes a Reportable Incident
- Unauthorized access to systems containing CUI
- Exfiltration of CUI (actual or suspected)
- Malware detected on systems that process CUI
- Compromise of credentials that could lead to CUI access

---

## Common Assessment Findings

| Practice | Common Finding | Typical Remediation |
|----------|---------------|---------------------|
| IA.L2-3.5.3 | MFA not enabled for all privileged accounts or remote access | Deploy MFA solution (Azure MFA, Duo, Okta); enforce via conditional access |
| SC.L2-3.13.11 | TLS 1.0/1.1 still enabled; non-FIPS algorithms in use | Disable TLS 1.0/1.1; enable only FIPS-validated cipher suites |
| AU.L2-3.3.1 | Logs not retained per policy; not all devices log to SIEM | Deploy/configure SIEM; set 3-year retention; cover all CUI-touching systems |
| CM.L2-3.4.1 | No formal baseline configuration document | Create baseline config docs per OS/application; store in change management |
| AC.L2-3.1.5 | Excessive admin rights; shared admin accounts | Implement PAM solution; audit/remove excess privileges quarterly |
| RA.L2-3.11.2 | Vulnerability scans not authenticated; not covering all assets | Configure credentialed scans; scan all in-scope assets monthly |
| CA.L2-3.12.4 | SSP outdated or incomplete | Update SSP; review and re-approve annually or after significant changes |
| AC.L2-3.1.3 | CUI accessible to users without need-to-know | Implement data classification labels; enforce access controls at file/folder level |

# NIST SP 800-137 — Security Metrics, Reporting Templates, and Aggregation Procedures

**Source**: NIST SP 800-137, September 2011, Sections 2.4, 4 (Analyse/Report), Appendix A

---

## Security Metrics

### Metric Attribute Set

Every ISCM metric must be documented with the following attributes:

| Attribute | Description |
|---|---|
| Metric ID | Unique identifier (e.g., ISCM-CM-001) |
| Name | Short descriptive name |
| Control Mapping | SP 800-53 Rev 5 control ID (e.g., CM-6) |
| Description | What is being measured and why it matters |
| Measurement | How the metric value is calculated (formula or procedure) |
| Data Source | Tool or procedure that collects the data |
| Collection Frequency | How often data is collected (continuous/daily/weekly/monthly/quarterly/annual) |
| Reporting Frequency | How often metric appears in reports |
| Threshold | Value at which a finding is triggered (e.g., < 95% compliance = finding) |
| Reporting Level | Tier 1 only, Tier 2+, or all tiers |
| Owner | Role responsible for this metric (e.g., ISSO) |

---

## ISCM Metrics Catalogue

### Implementation Status Metrics

**ISCM-SI-001 — Patch Compliance Rate (Critical)**
- Control: SI-2
- Description: Percentage of systems with critical vulnerabilities (CVSS >= 9.0) patched within 15 calendar days of patch release
- Measurement: (Systems with critical CVEs remediated within SLA / Total systems with critical CVEs) x 100
- Data Source: Authenticated vulnerability scanner
- Frequency: Daily
- Threshold: >= 95% compliant; < 95% = finding; < 80% = escalation to AO

**ISCM-SI-002 — Patch Compliance Rate (High)**
- Control: SI-2
- Description: Percentage of systems with high vulnerabilities (CVSS 7.0–8.9) patched within 30 calendar days
- Measurement: (Systems with high CVEs remediated within SLA / Total systems with high CVEs) x 100
- Data Source: Authenticated vulnerability scanner
- Frequency: Weekly
- Threshold: >= 90% compliant; < 90% = finding

**ISCM-SI-003 — Anti-Virus Definition Currency**
- Control: SI-3
- Description: Percentage of managed endpoints with AV definitions current (within 24 hours of latest release)
- Measurement: (Endpoints with current AV definitions / Total managed endpoints) x 100
- Data Source: Endpoint management platform / AV management console
- Frequency: Daily
- Threshold: >= 98% compliant; < 98% = finding

**ISCM-CM-001 — Configuration Compliance Rate**
- Control: CM-6
- Description: Percentage of scanned systems in compliance with approved SCAP/XCCDF configuration baseline
- Measurement: (Systems with passing XCCDF results / Total scanned systems) x 100
- Data Source: SCAP-validated configuration scanner
- Frequency: Weekly
- Threshold: >= 90% compliant; < 90% = finding; < 80% = escalation

**ISCM-CM-002 — Unauthorised Software Detected**
- Control: CM-7
- Description: Number of systems with software detected that is not on the approved software list
- Measurement: Count of systems with one or more unapproved software packages
- Data Source: Software inventory scanner / Endpoint management
- Frequency: Weekly
- Threshold: 0 systems; any = finding

**ISCM-AC-001 — Inactive Account Rate**
- Control: AC-2
- Description: Percentage of active accounts with no logon activity in past 30 days
- Measurement: (Accounts with zero logins in 30 days / Total active accounts) x 100
- Data Source: Directory service (AD/LDAP) query
- Frequency: Weekly
- Threshold: <= 2%; > 2% = finding (inactive accounts should be disabled or deleted)

**ISCM-AC-002 — Multi-Factor Authentication Coverage**
- Control: IA-2(1)
- Description: Percentage of privileged accounts enrolled in MFA
- Measurement: (Privileged accounts with MFA enabled / Total privileged accounts) x 100
- Data Source: Identity provider / MFA platform
- Frequency: Weekly
- Threshold: 100% required; any gap = critical finding

**ISCM-AT-001 — Security Awareness Training Completion**
- Control: AT-2
- Description: Percentage of personnel who have completed required annual security awareness training
- Measurement: (Personnel with current training completion / Total required personnel) x 100
- Data Source: Learning Management System (LMS)
- Frequency: Monthly
- Threshold: >= 95%; < 95% = finding

**ISCM-AT-002 — Role-Based Training Completion**
- Control: AT-3
- Description: Percentage of personnel in security-relevant roles with current role-based training
- Measurement: (Security-role personnel with current role training / Total security-role personnel) x 100
- Data Source: LMS
- Frequency: Quarterly
- Threshold: 100%; any gap = finding

**ISCM-AU-001 — Audit Log Coverage**
- Control: AU-2
- Description: Percentage of in-scope systems with audit logging operational and forwarding to central log management
- Measurement: (Systems forwarding logs to SIEM / Total in-scope systems) x 100
- Data Source: SIEM log reception status
- Frequency: Daily
- Threshold: 100%; any gap = finding

### Operational Effectiveness Metrics

**ISCM-IR-001 — Mean Time to Detect (MTTD)**
- Control: IR-4, SI-4
- Description: Average time (hours) from security event occurrence to detection by monitoring tools or personnel
- Measurement: Sum of (detection time - occurrence time) for all detected events / count of events
- Data Source: Incident tracking system
- Frequency: Monthly
- Threshold: Organisationally defined; typically < 24 hours for High/Critical events

**ISCM-IR-002 — Mean Time to Respond (MTTR)**
- Control: IR-4
- Description: Average time (hours) from incident detection to containment
- Measurement: Sum of (containment time - detection time) for all incidents / count of incidents
- Data Source: Incident tracking system
- Frequency: Monthly
- Threshold: Organisationally defined; typically < 1 hour for Critical, < 4 hours for High

**ISCM-RA-001 — Vulnerability Scan Coverage**
- Control: RA-5
- Description: Percentage of in-scope systems scanned in the current reporting period
- Measurement: (Systems scanned / Total in-scope systems) x 100
- Data Source: Vulnerability scanner scan history
- Frequency: Weekly
- Threshold: 100%; any gap = finding

### Risk Management Metrics

**ISCM-CA-001 — Systems with Current ATO**
- Control: CA-6
- Description: Percentage of operational systems with a current, non-expired Authorization to Operate
- Measurement: (Systems with current ATO / Total operational systems) x 100
- Data Source: ATO tracking register
- Frequency: Monthly
- Threshold: 100%; expired ATOs = finding; operating without ATO = critical finding

**ISCM-CA-002 — Open Critical/High POA&M Items**
- Control: CA-5
- Description: Number of open POA&M items at Critical or High severity beyond their scheduled completion date
- Measurement: Count of overdue Critical/High POA&M items
- Data Source: POA&M tracking system
- Frequency: Weekly
- Threshold: 0; any = finding; >5 or any >90 days overdue = escalation to AO

---

## Reporting Templates

### Tier 3 — System-Level Security Status Report

```
==================================================
INFORMATION SECURITY CONTINUOUS MONITORING
SYSTEM-LEVEL SECURITY STATUS REPORT
==================================================

SYSTEM IDENTIFICATION
---------------------
System Name:          [Name]
System ID:            [Unique identifier / FISMA system inventory ID]
FIPS 199 Impact Level: [Low | Moderate | High]
Authorizing Official: [Name, title]
System Owner:         [Name, title]
ISSO:                 [Name, contact]
Report Period:        [Start date] to [End date]
Collection Date:      [Date of data collection]

EXECUTIVE SUMMARY
-----------------
Overall Compliance Status:  [ COMPLIANT | NON-COMPLIANT | AT RISK ]
Metrics in Scope:           [n]
Metrics Passing:            [n]
Metrics Failing:            [n]
New Findings This Period:   [n]
Resolved Findings:          [n]
Open POA&M Items:           [n Critical | n High | n Medium | n Low]
ATO Status:                 [Current; Expiration: YYYY-MM-DD | Expired | Ongoing]

METRIC STATUS SUMMARY
---------------------
| Metric ID    | Metric Name                     | Threshold | Current Value | Status |
|---|---|---|---|---|
| ISCM-SI-001  | Critical Patch Compliance        | >= 95%    | [value]%      | PASS/FAIL |
| ISCM-SI-002  | High Patch Compliance            | >= 90%    | [value]%      | PASS/FAIL |
| ISCM-SI-003  | AV Definition Currency           | >= 98%    | [value]%      | PASS/FAIL |
| ISCM-CM-001  | Configuration Compliance         | >= 90%    | [value]%      | PASS/FAIL |
| ISCM-CM-002  | Unauthorised Software            | 0 systems | [count]       | PASS/FAIL |
| ISCM-AC-001  | Inactive Accounts                | <= 2%     | [value]%      | PASS/FAIL |
| ISCM-AC-002  | MFA Coverage (Privileged)        | 100%      | [value]%      | PASS/FAIL |
| ISCM-AU-001  | Audit Log Coverage               | 100%      | [value]%      | PASS/FAIL |
| ISCM-RA-001  | Vulnerability Scan Coverage      | 100%      | [value]%      | PASS/FAIL |
| ISCM-CA-001  | Current ATO                      | 100%      | [value]%      | PASS/FAIL |

FINDINGS
--------
New Findings This Period:

Finding ID: [System ID]-ISCM-[YYYY-MM-DD]-[NN]
Title:        [Short description]
Metric:       [Metric ID]
Severity:     [Critical | High | Medium | Low]
Description:  [Detailed description of the finding]
Evidence:     [Tool, scan ID, or manual procedure reference]
Risk:         [Risk description — potential impact if not remediated]
Recommended Action: [Specific remediation step]
Scheduled Completion: [Date]
POA&M Reference: [POA&M item ID if opened]

Sustained Findings (carried from prior period):
[List with original date, current status, and delta]

Resolved Findings:
[List with original date and resolution description]

TREND ANALYSIS
--------------
| Metric ID | Prior Period | Current Period | Delta | Trend |
|---|---|---|---|---|
| ISCM-SI-001 | [value]% | [value]% | [+/-]% | UP/DOWN/STABLE |
[...repeat for each metric...]

POA&M STATUS SUMMARY
--------------------
| POA&M ID | Weakness | Severity | Scheduled Completion | Status |
|---|---|---|---|---|
| [ID] | [Description] | [Sev] | [Date] | Open / Overdue / Closed |

SIGNIFICANT CHANGES
-------------------
[Description of any significant changes to the system, environment, or controls since last report;
if none, state: No significant changes this reporting period.]

ATTESTATION
-----------
I certify that the information in this report accurately reflects the current security status
of the system based on ISCM data collected during the reporting period.

ISSO Signature: _________________________ Date: ___________
ISO Signature:  _________________________ Date: ___________
```

---

### Tier 2 — Mission/Business Process Aggregated Report

```
==================================================
INFORMATION SECURITY CONTINUOUS MONITORING
MISSION/BUSINESS PROCESS SECURITY STATUS REPORT
==================================================

PROGRAMME IDENTIFICATION
------------------------
Mission/Business Process: [Name]
Process Owner:            [Name, title]
Systems in Scope:         [List of system names/IDs]
Report Period:            [Start date] to [End date]
Prepared By:              [Name, role]

PORTFOLIO SUMMARY
-----------------
Total Systems in Portfolio:       [n]
Systems Compliant (all metrics pass): [n] ([%])
Systems Non-Compliant (1+ failures):  [n] ([%])
Systems At Risk (critical/escalation): [n] ([%])

METRIC COMPLIANCE BY SYSTEM
----------------------------
| System | ATO Status | Patch(Crit) | Patch(High) | Config | AV | MFA | Scan Cov | Overall |
|---|---|---|---|---|---|---|---|---|
| [Sys1] | Current     | PASS        | PASS        | FAIL   | PASS | PASS | PASS | MIXED |
[...repeat for each system...]

CROSS-SYSTEM FINDINGS
---------------------
[Findings that appear across multiple systems — may indicate shared service issue,
common vulnerability, or systemic gap. List finding category and affected systems.]

COMMON CONTROL STATUS
---------------------
| Common Control Provider | Control ID | Status | Notes |
|---|---|---|---|
| [Provider] | AC-2 (Account management) | PASS | [Notes] |
[...repeat for each common control...]

OPEN POA&M ITEMS (CRITICAL AND HIGH)
--------------------------------------
| POA&M ID | System | Weakness | Severity | Due Date | Status |
|---|---|---|---|---|---|
| [ID] | [System] | [Description] | [Sev] | [Date] | Open/Overdue |

TREND SUMMARY
-------------
[Qualitative summary of security posture trends across the portfolio this period]

RISK SUMMARY FOR AUTHORIZING OFFICIAL
--------------------------------------
[Narrative summary of current risk posture. Identify whether aggregate risk is within
accepted threshold. Identify any systems or findings requiring AO attention.]
```

---

### Tier 1 — Organisation-Level Dashboard Summary

```
==================================================
INFORMATION SECURITY CONTINUOUS MONITORING
ORGANISATION-LEVEL SECURITY STATUS DASHBOARD
==================================================

REPORTING PERIOD: [Start date] to [End date]
PREPARED BY:      [SAISO / CIO designee]
DISTRIBUTION:     CIO, Risk Executive Function, Authorizing Officials

PORTFOLIO OVERVIEW
------------------
Total Federal Information Systems:           [n]
Systems with Current ATO:                    [n] ([%])
Systems with Expired ATO:                    [n] ([%])
Systems with Ongoing Authorisation:          [n] ([%])

KEY ISCM METRICS — ORGANISATION AVERAGE
-----------------------------------------
| Metric | Prior Period | Current Period | Threshold | Status |
|---|---|---|---|---|
| Critical Patch Compliance | [%] | [%] | >= 95% | PASS/FAIL |
| High Patch Compliance | [%] | [%] | >= 90% | PASS/FAIL |
| Config Compliance | [%] | [%] | >= 90% | PASS/FAIL |
| MFA Coverage (Priv) | [%] | [%] | 100% | PASS/FAIL |
| Scan Coverage | [%] | [%] | 100% | PASS/FAIL |
| AT Completion | [%] | [%] | >= 95% | PASS/FAIL |

OPEN POA&M ITEMS
----------------
Critical (overdue): [n]
High (overdue):     [n]
Total Open:         [n]

RISK POSTURE SUMMARY
--------------------
[Concise narrative. Is the organisation within accepted risk tolerance?
Any systemic issues? Any items requiring head-of-agency attention?]

ITEMS REQUIRING CIO/RISK EXECUTIVE FUNCTION ACTION
----------------------------------------------------
[List of items requiring decision or action at Tier 1]

FISMA REPORTING DATA
--------------------
[Current values for OMB FISMA metrics as required by OMB memorandum]
```

---

## AO Security Status Notification

When findings exceed the accepted risk threshold, the ISSO or SAISO notifies the AO:

```
TO:   [Authorizing Official Name, Title]
FROM: [ISSO / SAISO Name, Title]
DATE: [Date]
RE:   ISCM Risk Threshold Exceeded — System [System Name/ID]

This notification is being provided pursuant to the ISCM strategy requirement to notify the
Authorizing Official when current risk exceeds the accepted threshold.

SYSTEM:           [Name / System ID]
FINDING SUMMARY:  [Brief description of finding]
METRIC EXCEEDED:  [Metric ID and Name]
CURRENT VALUE:    [Value] — Threshold: [Threshold]
SEVERITY:         [Critical | High]
RISK DESCRIPTION: [Nature of the risk, potential impact]
CURRENT CONTROLS: [What is in place; why the gap exists]
PROPOSED RESPONSE:
  - Option 1: [Remediation — description, estimated completion date]
  - Option 2: [Risk acceptance — specific risk accepted, compensating controls]
  - Option 3: [Avoid/Transfer if applicable]

RECOMMENDED ACTION: [ISSO/SAISO recommendation]
DEADLINE FOR AO DECISION: [Date — based on risk severity]

Attachments: [Tier 3 report, scan evidence, POA&M extract]
```

---

## POA&M Format

```
| Field | Content |
|---|---|
| POA&M ID | [System ID]-POA-[YYYY]-[NN] |
| Weakness Description | [Specific finding description — measurable and actionable] |
| Affected System | [System name / ID] |
| Point of Contact | [ISSO name and contact] |
| Resources Required | [Personnel time, tools, budget estimate if applicable] |
| Scheduled Completion Date | [YYYY-MM-DD — based on severity SLA] |
| Actual Completion Date | [YYYY-MM-DD when completed; blank if open] |
| Milestone Changes | [Log of any date changes with justification] |
| Source | [ISCM finding ID, assessment finding ID, or self-identified] |
| Status | Open | In Remediation | Completed | Risk Accepted |
| Risk Acceptance Justification | [Required if Status = Risk Accepted; includes approving official and date] |
| Compensating Control | [If any; description and expected effectiveness] |
```

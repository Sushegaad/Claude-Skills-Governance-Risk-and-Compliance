# UK NIS — Policy and Document Templates
## NIS Regulations 2018 — Document Generation Reference

---

## Instructions for Use

When generating compliance documents, replace all `[PLACEHOLDER]` values with organisation-specific information. Each template cites the NIS Regulation or CAF outcome it satisfies. All documents should be reviewed by qualified legal or compliance professionals before formal adoption.

---

## Template 1 — NIS Compliance Policy

```
[ORGANISATION NAME]
NIS COMPLIANCE POLICY

Version:        [e.g., 1.0]
Status:         [Draft | For Review | Approved]
Date:           [YYYY-MM-DD]
Owner:          [ROLE, e.g., Chief Information Security Officer]
Approved by:    [ROLE, e.g., Board / Executive Committee]
Next Review:    [YYYY-MM-DD]

NIS Reference:  Regulation 10 (OES) / Regulation 12 (DSP)
CAF Reference:  A1 — Governance

---

1. PURPOSE

This policy establishes [ORGANISATION NAME]'s commitment to complying with
the Network and Information Systems (NIS) Regulations 2018 (SI 2018/506) and
sets out the organisation's approach to managing the security of network and
information systems that underpin the delivery of [essential service / digital
service].

2. SCOPE

This policy applies to:
- All network and information systems (NIS) used to provide [service description]
- All employees, contractors, and third parties with access to or responsibility
  for those systems
- All digital and physical assets that form part of or support the NIS

3. ORGANISATION TYPE AND SECTOR

[ORGANISATION NAME] is designated as an:
  [ ] Operator of Essential Services (OES)
  [ ] Digital Service Provider (DSP)

Sector / Service type: [e.g., Electricity Distribution / Cloud Computing]
Competent Authority: [e.g., Ofgem / ICO]

4. NIS LEAD ACCOUNTABILITY

The [ROLE, e.g., CISO / Head of Cyber Security] has overall accountability
for NIS compliance within this organisation, reporting to [ROLE].

Overall board accountability rests with [ROLE, e.g., Chief Executive / Chair of
Risk Committee].

5. SECURITY OBLIGATIONS

[ORGANISATION NAME] commits to:

5.1 Implementing appropriate and proportionate technical and organisational
    measures to manage risks to the security of NIS (Regulation 10/12).

5.2 Conducting and maintaining a systematic cyber risk assessment covering
    all NIS in scope.

5.3 Implementing controls aligned to the NCSC Cyber Assessment Framework (CAF)
    (for OES) or the DSP security parameters (for DSPs).

5.4 Notifying the relevant Competent Authority of incidents having a
    significant/substantial impact on service continuity without undue delay
    (Regulation 11/13).

5.5 Supporting any Competent Authority audit, inspection, or information
    request exercised under Regulations 15-17.

6. POLICY REVIEW

This policy is reviewed [ANNUALLY / FOLLOWING SIGNIFICANT CHANGE] by [ROLE].

7. RELATED DOCUMENTS

- Risk Assessment and Risk Register
- Asset Register
- Incident Response Plan
- Supplier Security Policy
- CAF Self-Assessment Record

Signed: _______________________ Date: ___________
[NAME, ROLE, e.g., Chief Executive]
```

---

## Template 2 — NIS Risk Assessment and Risk Register

```
[ORGANISATION NAME]
NIS RISK ASSESSMENT AND REGISTER

Version:        [e.g., 1.0]
Date:           [YYYY-MM-DD]
Owner:          [ROLE]
Review Date:   [YYYY-MM-DD]

NIS Reference:  Regulation 10 / Regulation 12
CAF Reference:  A2 — Risk Management

---

RISK ASSESSMENT METHODOLOGY
Likelihood: 1 (Rare) to 5 (Almost Certain)
Impact:     1 (Negligible) to 5 (Critical — loss of essential service)
Risk Score: Likelihood x Impact (1-25)

Risk Appetite: [e.g., risks with score > 15 require immediate treatment]

---

RISK REGISTER (repeat rows as required)

| Risk ID | NIS System / Asset | Threat | Vulnerability | Likelihood (1-5) | Impact (1-5) | Risk Score | Current Controls | Treatment | Residual Risk | Owner | Review Date |
|---------|-------------------|--------|--------------|------------------|-------------|------------|-----------------|-----------|--------------|-------|-------------|
| R-001   | [e.g., SCADA]     | Ransomware | Unpatched systems | 3 | 5 | 15 | AV, patching | Mitigate — accelerate patching | 9 | IT Manager | YYYY-MM-DD |
| R-002   | ...               | ...    | ...          | ...              | ...         | ...        | ...             | ...       | ...          | ...   | ... |

Treatment options: Accept | Avoid | Transfer | Mitigate

Risk Register Approved by: [NAME, ROLE, DATE]
```

---

## Template 3 — NIS Asset Register

```
[ORGANISATION NAME]
NIS ASSET REGISTER

Version:        [e.g., 1.0]
Date:           [YYYY-MM-DD]
Owner:          [ROLE]

NIS Reference:  Regulation 10
CAF Reference:  A3 — Asset Management

---

ASSET REGISTER (repeat rows as required)

| Asset ID | Asset Name / Description | Asset Type | Location | Criticality | Owner | NIS Role | System Connections | Last Reviewed |
|----------|------------------------|-----------|----------|-------------|-------|----------|--------------------|--------------|
| A-001    | [e.g., Control Room Server] | Server | [Location] | Critical | [Name] | SCADA host | [Network segments] | YYYY-MM-DD |
| A-002    | ... | ... | ... | ... | ... | ... | ... | ... |

Asset Types: Server | Workstation | Network Device | Application | Database | OT/ICS Device | Cloud Service | Data Store | People | Facility

Criticality Levels:
- Critical: Failure would directly impair essential service delivery
- High: Failure would significantly impact essential service
- Medium: Failure would partially impact service
- Low: Failure has minimal direct service impact

Asset Register Reviewed by: [NAME, ROLE, DATE]
```

---

## Template 4 — Supplier Security Assessment Questionnaire

```
[ORGANISATION NAME]
SUPPLIER NIS SECURITY ASSESSMENT

Supplier Name:          [NAME]
Date of Assessment:     [YYYY-MM-DD]
Assessed by:            [NAME, ROLE]
Supplier Contact:       [NAME, ROLE, EMAIL]

NIS Reference:          Regulation 10
CAF Reference:          A4 — Supply Chain

---

SECTION A — ORGANISATION AND CONTACT

1. Registered company name and number:
2. Primary contact for security matters:
3. Does the supplier have ISO 27001 certification?  [ ] Yes — certificate no.:   [ ] No
4. Does the supplier have Cyber Essentials / CE+?  [ ] Yes  [ ] No

SECTION B — ACCESS TO IN-SCOPE NIS

5. What type of access does the supplier have to [ORGANISATION NAME]'s NIS?
   [ ] Remote access  [ ] Physical access  [ ] Software/code changes  [ ] Data processing  [ ] None
6. Describe the business purpose of the supplier's access:
7. Is the supplier a sub-processor of any NIS data?  [ ] Yes  [ ] No

SECTION C — SECURITY CONTROLS

8. Does the supplier have a documented information security policy?  [ ] Yes  [ ] No
9. Are background checks performed on staff with NIS access?  [ ] Yes  [ ] No
10. Is MFA required for remote access?  [ ] Yes  [ ] No
11. Are systems with NIS access regularly patched?  [ ] Yes  [ ] No
12. Does the supplier conduct annual security testing?  [ ] Yes  [ ] No
13. Does the supplier have an incident response plan?  [ ] Yes  [ ] No

SECTION D — INCIDENT REPORTING

14. Does the supplier commit to notifying [ORGANISATION NAME] of any security 
    incident affecting systems that connect with or process NIS data within 
    [24 / 48 / 72] hours?  [ ] Yes  [ ] No
15. Contact details for incident notification:

SECTION E — CONTRACTUAL

16. Is there a Data Processing Agreement (DPA) in place?  [ ] Yes  [ ] No
17. Are NIS security requirements included in the contract?  [ ] Yes  [ ] No

Assessment Outcome:
  [ ] Approved  [ ] Approved with conditions  [ ] Not approved

Conditions (if applicable):

Signed: _______________________ Date: ___________
[ASSESSOR NAME, ROLE]
```

---

## Template 5 — Incident Response Plan (NIS)

```
[ORGANISATION NAME]
INCIDENT RESPONSE PLAN — NIS

Version:        [e.g., 1.0]
Date:           [YYYY-MM-DD]
Owner:          [ROLE]
Last Tested:    [YYYY-MM-DD]
Test Method:    [e.g., Tabletop exercise]

NIS Reference:  Regulation 11 / Regulation 13
CAF Reference:  D1 — Response and Recovery Planning

---

1. PURPOSE

This Incident Response Plan (IRP) defines [ORGANISATION NAME]'s procedures for
detecting, responding to, containing, and recovering from cyber security
incidents affecting NIS used to provide [essential service / digital service].

2. SCOPE

In scope: All NIS as defined in the NIS Asset Register [reference].
Out of scope: Incidents affecting systems not connected to or supporting NIS.

3. INCIDENT RESPONSE TEAM

| Role | Responsibility | Primary Contact | Backup Contact |
|------|---------------|----------------|----------------|
| Incident Commander | Overall coordination | [NAME] [TEL] | [NAME] [TEL] |
| Technical Lead | Technical investigation | [NAME] [TEL] | [NAME] [TEL] |
| Communications Lead | Internal/external comms | [NAME] [TEL] | [NAME] [TEL] |
| Legal/Compliance | Regulatory notifications | [NAME] [TEL] | [NAME] [TEL] |

4. EXTERNAL CONTACTS

| Organisation | Role | Contact |
|-------------|------|---------|
| [Competent Authority name] | NIS notification | [email / phone] |
| NCSC | Technical assistance | report.ncsc.gov.uk / 0800 169 4192 |
| ICO (if personal data) | GDPR notification | 0303 123 1113 |
| Action Fraud | Fraud / crime report | 0300 123 2040 |
| [Cyber incident response firm] | External IR support | [contact] |

5. INCIDENT RESPONSE PHASES

PHASE 1 — DETECTION AND TRIAGE (0-2 hours)
- Receive alert / report
- Assess: Is this a NIS-affecting incident?
- Activate Incident Response Team
- Begin incident log

PHASE 2 — CONTAINMENT (2-12 hours)
- Isolate affected systems (without destroying evidence where possible)
- Preserve forensic evidence (system images, logs)
- Assess impact on essential service / digital service continuity
- Determine if significant / substantial impact threshold is met

PHASE 3 — NIS NOTIFICATION ASSESSMENT (within 72 hours)
- If significant/substantial impact: notify Competent Authority (template in
  references/incident-reporting.md)
- Notify NCSC
- Assess UK GDPR notification requirement
- Internal leadership notification

PHASE 4 — ERADICATION AND RECOVERY
- Remove malware / close attack vector
- Restore from clean backups
- Confirm systems are clean before reconnecting
- Restore essential service

PHASE 5 — POST-INCIDENT (within 30 days)
- Conduct post-incident review
- Document root cause analysis
- Update risk register
- Implement lessons learned
- Submit final NIS notification update to Competent Authority

6. INCIDENT SEVERITY LEVELS

| Level | Description | Response Time |
|-------|-------------|---------------|
| P1 — Critical | Essential service fully disrupted or under active attack | Immediate (within 1 hour) |
| P2 — High | Partial service impact or confirmed compromise | Within 4 hours |
| P3 — Medium | Potential compromise; investigation required | Within 24 hours |
| P4 — Low | Security event; no confirmed impact | Within 72 hours |

7. TESTING SCHEDULE

This IRP is tested [ANNUALLY] via:
  [ ] Tabletop exercise
  [ ] Live simulation / red team
  [ ] Full recovery test (DR)

Next test date: [YYYY-MM-DD]
Last test findings: [Summary]

Signed: _______________________ Date: ___________
[NAME, ROLE]
```

---

## Template 6 — CAF Self-Assessment Record

```
[ORGANISATION NAME]
CAF SELF-ASSESSMENT RECORD

Version:        [e.g., 1.0]
Assessment Date: [YYYY-MM-DD]
Assessor(s):    [NAMES, ROLES]
System/Service: [Name of NIS being assessed]

--------------------------------------------------------------
CAF OBJECTIVE A — MANAGING SECURITY RISK

A1 — Governance
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence reviewed:
Gaps identified:
Actions required:
Target date:

A2 — Risk Management
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence reviewed:
Gaps identified:
Actions required:
Target date:

A3 — Asset Management
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence reviewed:
Gaps identified:
Actions required:
Target date:

A4 — Supply Chain
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence reviewed:
Gaps identified:
Actions required:
Target date:

--------------------------------------------------------------
CAF OBJECTIVE B — PROTECTING AGAINST CYBER ATTACK

B1 — Service Protection Policies and Processes
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

B2 — Identity and Access Control
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

B3 — Data Security
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

B4 — System Security
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

B5 — Resilient Networks and Systems
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

B6 — Staff Awareness and Training
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

--------------------------------------------------------------
CAF OBJECTIVE C — DETECTING CYBER SECURITY EVENTS

C1 — Security Monitoring
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

C2 — Proactive Security Event Discovery
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

--------------------------------------------------------------
CAF OBJECTIVE D — MINIMISING IMPACT OF INCIDENTS

D1 — Response and Recovery Planning
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

D2 — Improvements
Rating: [ ] Achieved  [ ] Partially Achieved  [ ] Not Achieved  [ ] N/A
Evidence:   Gaps:   Actions:   Target:

--------------------------------------------------------------
OVERALL ASSESSMENT SUMMARY

| Objective | A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | B5 | B6 | C1 | C2 | D1 | D2 |
|-----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Rating    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |

Overall Compliance Posture: [ ] Strong  [ ] Developing  [ ] Requires significant improvement

Signed: _______________________ Date: ___________
[NAME, ROLE]
```

---

## Template 7 — Business Continuity Plan (NIS)

```
[ORGANISATION NAME]
BUSINESS CONTINUITY PLAN — NIS SERVICES

Version:        [e.g., 1.0]
Date:           [YYYY-MM-DD]
Owner:          [ROLE]

NIS Reference:  Regulation 10/12
CAF Reference:  B5, D1

---

1. CRITICAL SERVICE DESCRIPTION

Service: [Name and description of essential/digital service]
Maximum Tolerable Downtime (MTD): [e.g., 4 hours]
Recovery Time Objective (RTO):    [e.g., 2 hours]
Recovery Point Objective (RPO):   [e.g., 1 hour]

2. CRITICAL NIS COMPONENTS

| Component | RTO | RPO | Backup Method | Location |
|-----------|-----|-----|--------------|----------|
| [System 1] | [x hrs] | [x hrs] | [e.g., Nightly encrypted backup] | [Location] |
| [System 2] | ... | ... | ... | ... |

3. BACKUP PROCEDURES

Backup Schedule: [e.g., Full weekly, incremental daily]
Backup Storage: [e.g., Offsite encrypted, Cloud (provider name)]
Backup Testing: [e.g., Monthly restore test]
Last Successful Restore Test: [YYYY-MM-DD]

4. RECOVERY PROCEDURES

Step 1: Invoke BCP — authorisation by [ROLE]
Step 2: Assess scope of failure
Step 3: Invoke failover / alternate processing
Step 4: Restore from clean backup
Step 5: Test restored systems before reconnecting to NIS
Step 6: Resume essential service
Step 7: Notify Competent Authority of resolution (if NIS incident notified)

5. BCP TESTING

Test Type:       [e.g., Failover test / tabletop]
Test Frequency:  [e.g., Annually]
Next Test Date:  [YYYY-MM-DD]
Last Test Result: [Pass / Partial / Fail — notes]

Signed: _______________________ Date: ___________
[NAME, ROLE]
```

# ISO 22301:2019 — Templates Reference

## Overview

This reference provides ready-to-use templates for the key documents required by
ISO 22301:2019. All templates are structured to satisfy the relevant clause requirements
and are suitable for adaptation to any organisation's context and terminology.

Templates included:
1. Business Continuity Policy
2. BCMS Scope Statement
3. BIA Form (single activity)
4. Risk Register template
5. Exercise Plan template
6. Exercise After-Action Report template
7. Management Review agenda and record template
8. Nonconformity and Corrective Action Record
9. BCMS Internal Audit Plan template
10. BC Competence Matrix template

---

## Template 1 — Business Continuity Policy

*Satisfies ISO 22301:2019 Clause 5.2. Must be signed by top management.*

---

**[ORGANISATION NAME]**
**Business Continuity Policy**

| Field | Value |
|-------|-------|
| Policy Reference | POL-BCM-001 |
| Version | [x.x] |
| Status | Active |
| Approved by | [CEO / Managing Director / Board] |
| Approval Date | [Date] |
| Next Review Date | [Date — maximum 12 months] |
| Owner | [BCMS Manager / Head of Risk] |

---

**1. Purpose**

[ORGANISATION NAME] is committed to maintaining continuity of its critical operations and
protecting the interests of its customers, employees, shareholders, and other stakeholders
in the event of a disruption to normal business activities.

This policy establishes the organisation's commitment to implementing and maintaining a
Business Continuity Management System (BCMS) in accordance with ISO 22301:2019.

**2. Scope**

This policy applies to all activities, functions, and personnel within the BCMS scope
as defined in the BCMS Scope Statement (document reference: SCP-BCM-001).

**3. Policy Statement**

[ORGANISATION NAME] will:

a) Establish, implement, operate, and continually improve a BCMS aligned to ISO 22301:2019;

b) Identify and assess risks to the continuity of critical activities and implement proportionate
   controls to reduce the likelihood and impact of disruptions;

c) Conduct regular Business Impact Analyses (BIAs) to understand the impact of disruptions
   and establish appropriate Recovery Time Objectives (RTOs), Recovery Point Objectives (RPOs),
   and Minimum Business Continuity Objectives (MBCOs);

d) Develop, maintain, and exercise Business Continuity Plans covering all priority activities;

e) Ensure that resources, competencies, and communications are in place to respond effectively
   to incidents;

f) Meet applicable legislative, regulatory, and contractual requirements related to business
   continuity;

g) Conduct regular exercises and tests to validate the effectiveness of BC strategies and plans;

h) Review and improve the BCMS continually through management reviews, internal audits, and
   post-incident reviews.

**4. Roles and Responsibilities**

| Role | Responsibility |
|------|---------------|
| Board / Executive Management | Setting BC objectives; ensuring adequate resources; policy approval |
| BCMS Manager | Day-to-day management of the BCMS; coordination of BIA, risk, plans, exercises |
| Department Heads / Plan Owners | BCP ownership; staff awareness; participation in exercises |
| All Staff | Awareness of BC procedures relevant to their role; reporting incidents promptly |

**5. Review**

This policy will be reviewed at least annually, or following a significant business change or
business continuity incident.

**Signed:**

_________________________ Date: _____________

[Name and Title — CEO / Board Representative]

---

## Template 2 — BCMS Scope Statement

*Satisfies ISO 22301:2019 Clause 4.3. Must be retained as documented information.*

---

**[ORGANISATION NAME]**
**BCMS Scope Statement**

| Field | Value |
|-------|-------|
| Document Reference | SCP-BCM-001 |
| Version | [x.x] |
| Approved by | [Role] |
| Approval Date | [Date] |
| Next Review | [Date] |

**1. Organisation Overview**

[Brief description of the organisation: what it does, size, key locations, key products/services]

**2. BCMS Scope**

The BCMS covers the following:

*Products and services:*
- [Product/Service A]
- [Product/Service B]

*Organisational units and functions:*
- [Department/Function A — all activities relating to...]
- [Department/Function B — activities relating to...]

*Sites and locations:*
- [Site 1: Address, functions covered]
- [Site 2: Address, functions covered]

*Technology environment:*
The BCMS addresses continuity of the following technology services:
- [System A]
- [System B]

*Supply chain:*
The BCMS addresses disruption risks from the following critical third-party dependencies:
- [Supplier A — service provided]
- [Supplier B — service provided]

**3. Exclusions from Scope**

The following are explicitly excluded from the BCMS scope:

| Excluded Item | Justification |
|--------------|--------------|
| [Subsidiary / location] | [Reason — e.g., separate legal entity with own BCMS; not material to in-scope services] |
| [Function/activity] | [Reason — e.g., not in critical path for any in-scope product/service] |

**4. Relationship to Other Management Systems**

[If applicable: describes integration with ISO 27001 ISMS, ISO 9001 QMS, or other management systems in operation]

**5. Version History**

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0 | [Date] | [Name] | Initial issue |

---

## Template 3 — BIA Assessment Form (Single Activity)

*Satisfies ISO 22301:2019 Clause 8.2.2. Completed for each in-scope activity.*

---

**BIA Assessment Form**

| Field | Value |
|-------|-------|
| Activity Name | [Name] |
| Activity ID | [BIA-xxx] |
| Function/Department | [Department] |
| Process Owner | [Role] |
| Products/Services Supported | [List products/services this activity enables] |
| Date Completed | [Date] |
| Next Review | [Date] |
| BIA Facilitator | [Name/Role] |

---

**Section 1 — Activity Description**

Brief description of the activity:
[What this activity does; how often; volume handled; key inputs and outputs]

Normal operating hours: [e.g., Monday–Friday, 08:00–18:00]
Peak periods and critical deadlines: [e.g., month-end, quarterly filing deadlines]

---

**Section 2 — Impact Assessment**

Rate the impact of disruption to this activity at each time horizon.
Scale: 1 = Negligible | 2 = Minor | 3 = Moderate | 4 = Significant | 5 = Catastrophic

| Time Since Disruption | Financial | Operational | Regulatory/Legal | Reputational | Contractual | Overall |
|-----------------------|-----------|-------------|-----------------|--------------|-------------|---------|
| <1 hour | | | | | | |
| 1–4 hours | | | | | | |
| 4–8 hours | | | | | | |
| 8–24 hours | | | | | | |
| 1–3 days | | | | | | |
| 3–7 days | | | | | | |
| 1–2 weeks | | | | | | |
| >2 weeks | | | | | | |

Impact assessment narrative (justify ratings, particularly for Regulatory/Legal):
[Notes]

---

**Section 3 — Recovery Parameters**

| Parameter | Value | Justification |
|-----------|-------|--------------|
| MTPD (Maximum Tolerable Period of Disruption) | [e.g., 24 hours] | [Why — regulatory deadline, SLA, financial impact threshold] |
| RTO (Recovery Time Objective) | [Must be less than MTPD] | [Achievable with available strategies/resources] |
| RPO (Recovery Point Objective) | [e.g., 4 hours] | [Maximum data loss acceptable; aligns to backup frequency?] |
| MBCO (Minimum Business Continuity Objective) | [e.g., 50% capacity / priority transactions only] | [Minimum viable service; allows phased recovery] |
| RLO (Recovery Level Objective) (if applicable) | [e.g., 75% capacity within 48 hours] | [Intermediate target before full restoration] |
| Priority Tier | [Critical / High / Medium / Low] | [Derived from MTPD and impact ratings] |

---

**Section 4 — Dependencies**

**People:**
| Role | Number Required at MBCO | Specialist Skills/Authorisations | Backup Available? |
|------|------------------------|----------------------------------|-------------------|
| | | | |

Single points of failure identified: [Yes/No — detail if yes]

**Technology:**
| System / Application | Criticality | Required at MBCO? | Backup/Failover Available? |
|---------------------|-------------|-------------------|---------------------------|
| | | | |

**Premises:**
| Dependency on location | Can be performed remotely? | Alternate location? |
|------------------------|---------------------------|---------------------|
| | | |

**Information/Data:**
| Key Information/Record | Location | Offline/Paper Copy? | Offsite Backup? |
|------------------------|----------|---------------------|-----------------|
| | | | |

**Suppliers/Third Parties:**
| Supplier | Service Provided | Criticality | Alternate Available? |
|----------|-----------------|-------------|----------------------|
| | | | |

---

**Section 5 — Existing Controls and Gaps**

Current controls in place to support continuity:
[List existing BC arrangements — e.g., remote access available, daily backups, alternate supplier identified]

Identified gaps and risks:
[List gaps identified during analysis — e.g., no trained alternate for [role], backup not tested in 12 months]

Recommendations:
[Actions to close gaps — linked to BC strategy and risk treatment]

---

**Section 6 — Sign-Off**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Process Owner | | | |
| BIA Facilitator | | | |

---

## Template 4 — Risk Register

*Satisfies ISO 22301:2019 Clause 8.2.3. Retained documented information.*

---

**[ORGANISATION NAME] — BCMS Risk Register**

| Field | Value |
|-------|-------|
| Document Reference | RISK-BCM-001 |
| Version | [x.x] |
| Owner | [BCMS Manager] |
| Last Updated | [Date] |
| Next Review | [Date] |

**Risk Scoring**

Likelihood: 1 = Rare | 2 = Unlikely | 3 = Possible | 4 = Likely | 5 = Almost Certain
Impact: 1 = Negligible | 2 = Minor | 3 = Moderate | 4 = Significant | 5 = Catastrophic
Score = Likelihood × Impact | ≤4 = Low | 5–9 = Medium | 10–14 = High | ≥15 = Critical

---

| Risk ID | Scenario | Affected Activities | Likelihood | Impact | Score | Rating | Treatment | Controls / BC Strategy | Owner | Review Date | Residual Score |
|---------|----------|-------------------|-----------|--------|-------|--------|-----------|----------------------|-------|-------------|----------------|
| R001 | Extended IT infrastructure failure (>8 hours) | All IT-dependent activities | 3 | 5 | 15 | Critical | Treat | DR site failover; cloud backup; IT DRP | IT Director | [Date] | [TBD] |
| R002 | Ransomware / destructive cyberattack | All activities | 4 | 5 | 20 | Critical | Treat | Immutable backups; EDR; IR plan; cyber insurance | CISO | [Date] | [TBD] |
| R003 | Primary site inaccessible (fire, flood, denial of access) | Site-dependent activities | 2 | 5 | 10 | High | Treat | Alternate site; remote working; key record offsite copies | Facilities Mgr | [Date] | [TBD] |
| R004 | Key person dependency (critical role unavailable) | [Specific activities] | 3 | 4 | 12 | High | Treat | Cross-training; succession planning; documented procedures | HR Director | [Date] | [TBD] |
| R005 | Critical supplier failure / insolvency | [Supply chain activities] | 2 | 4 | 8 | Medium | Treat | Alternative supplier identified; inventory buffer; contract protections | Procurement | [Date] | [TBD] |
| R006 | Pandemic / widespread staff absence (>30%) | All activities | 2 | 4 | 8 | Medium | Treat | Remote working capability; cross-training; temporary staffing | HR Director | [Date] | [TBD] |
| R007 | Major power failure (>24 hours) | All site-based activities | 2 | 3 | 6 | Medium | Treat | UPS; generator; remote working | Facilities Mgr | [Date] | [TBD] |
| R008 | Telecommunications failure | All comms-dependent activities | 2 | 3 | 6 | Medium | Treat | Dual ISP; 4G backup; mobile devices | IT Director | [Date] | [TBD] |

*Add additional rows as required per risk assessment.*

---

## Template 5 — Exercise Plan

*Satisfies ISO 22301:2019 Clause 8.5. Retained as documented information.*

---

**BC Exercise Plan**

| Field | Value |
|-------|-------|
| Document Reference | EX-BCM-[year]-[nn] |
| Exercise Name | [e.g., Tabletop Exercise — IT Failure Scenario] |
| Exercise Type | Tabletop / Walkthrough / Functional / Simulation / Live |
| Date and Time | [Date, Start time – Estimated end time] |
| Location | [Physical location / virtual meeting platform] |
| Lead Facilitator | [Name and role] |
| Observer(s) | [Names/roles — can include external auditor, senior management] |
| Plans Under Test | [List BCPs, IRP, IT DRP being tested] |

---

**1. Exercise Background and Objectives**

*Why this exercise is being conducted:*
[e.g., Annual exercising requirement; follow-up from previous exercise findings;
pre-certification test; new plan version validation]

*Objectives:*
1. [e.g., Test that the Crisis Management Team can mobilise within 30 minutes of incident
   declaration]
2. [e.g., Validate that alternate site procedures are feasible for minimum headcount operations]
3. [e.g., Confirm communication cascade (internal and customer) works as documented]
4. [e.g., Test IT recovery team's ability to bring DR environment online within RTO of 6 hours]
5. [e.g., Identify gaps in [specific plan] updated since last exercise]

---

**2. Scenario**

*Scenario overview:*
[Write a realistic and plausible scenario appropriate to exercise type. For tabletops,
the scenario does NOT need to be one that triggers actual system invocations.]

*Example scenario — IT ransomware attack:*
"At 07:30 on [exercise date], the IT monitoring system generates alerts indicating multiple
file encryption events across the primary file server and ERP system. By 08:00, the IT Director
confirms that a ransomware attack is underway. Primary systems are taken offline as a
precautionary measure. Initial assessment suggests the attack began at approximately 02:00.
Backups appear intact as of the previous night's scheduled backup at 23:00."

*Scenario injects (tabletop only — events introduced during the exercise to test decision-making):*
- T+1 hour: "Local media contacts the communications team asking for comment on reports of a
  cyberattack."
- T+2 hours: "A major customer contacts their account manager to ask when services will be
  restored — they have a critical delivery schedule this afternoon."
- T+3 hours: "IT confirms the attack vector was a phishing email and that customer data may
  have been exfiltrated — Data Protection Officer advises a potential 72-hour GDPR notification
  obligation may apply."

---

**3. Participants**

| Name | Role | Representing | Participation Required |
|------|------|-------------|------------------------|
| [Name] | Incident Commander | Executive | Mandatory |
| [Name] | BC Manager | BCMS | Mandatory |
| [Name] | IT Director | IT | Mandatory |
| [Name] | Communications Lead | Corporate Affairs | Mandatory |
| [Name] | HR Lead | HR | Mandatory |
| [Name] | Legal/Compliance | Legal | Mandatory |
| [Name] | Finance Lead | Finance | Mandatory |
| [Name] | [Dept BCP Owner] | [Department] | Required |
| [Name] | Observer | [Role] | Attendee |

---

**4. Success Criteria**

| Criterion | Measure | Target | Notes |
|-----------|---------|--------|-------|
| CMT mobilised following declaration | Time from declaration to first CMT call | ≤30 minutes | Per IRP requirement |
| IT Recovery actions initiated | Time from declaration to IT DRP activation | ≤1 hour | Per IT DRP |
| Internal all-staff communication issued | Time from declaration | ≤1 hour | Per comms plan |
| Customer holding statement issued | Time from declaration | ≤2 hours | Per comms plan |
| BC plans accessible to all participants | All participants have access | 100% | Test offline copy access |
| [Additional criteria based on objectives] | | | |

---

**5. Out of Scope**

The following will NOT be tested during this exercise to ensure no disruption to live operations:
- [e.g., Actual IT failover to DR site — logical walkthrough only]
- [e.g., Actual customer notifications — simulated only]
- [e.g., Physical evacuation of building — not part of this scenario]

---

**6. Debrief and Reporting**

- **Hot debrief**: Immediately following exercise; 30-minute facilitated discussion
  (What worked? What didn't? Initial actions?)
- **After-action report**: Issued within [10] working days; see Template 6
- **Corrective actions**: All actions logged in nonconformity and CA register (Template 8)
- **Report distribution**: All participants, BCMS Manager, Senior Management

---

## Template 6 — Exercise After-Action Report

*Satisfies ISO 22301:2019 Clause 8.5, 9.1. Retained as documented information.*

---

**BC Exercise After-Action Report**

| Field | Value |
|-------|-------|
| Exercise Reference | EX-BCM-[year]-[nn] |
| Exercise Name | [Name] |
| Exercise Date | [Date] |
| Report Author | [Name, Role] |
| Report Date | [Date — within 10 working days] |
| Approved by | [BCMS Manager] |

---

**1. Exercise Summary**

*Scenario used:* [Brief description]
*Participants:* [Number attended; list key roles]
*Duration:* [Start and end time]
*Plans tested:* [List]

**2. Objectives Achievement**

| Objective | Target | Achieved? | Notes |
|-----------|--------|-----------|-------|
| [Objective 1] | [Target] | Yes / No / Partial | [Notes] |
| [Objective 2] | [Target] | Yes / No / Partial | [Notes] |

**3. Findings**

*Strengths — what worked well:*
- [Finding 1]
- [Finding 2]

*Weaknesses and gaps — what did not work as expected:*
- [Finding 1 — description, evidence, impact]
- [Finding 2]

*Unexpected findings or near-misses:*
- [Any findings that were not anticipated but emerged during the exercise]

**4. Action Log**

| Action ID | Finding | Action Required | Owner | Due Date | Status |
|-----------|---------|----------------|-------|----------|--------|
| ACT-001 | [Finding] | [What must be done to address it] | [Role] | [Date] | Open |
| ACT-002 | | | | | |

*Actions must be raised as nonconformities / corrective actions per Template 8 where required.*

**5. Plan Update Requirements**

| Plan / Document | Update Required | Owner | Target Date |
|-----------------|----------------|-------|-------------|
| [BCP-001] | [Description of update] | [Owner] | [Date] |

**6. Overall Assessment**

*Summary assessment of BCMS readiness based on exercise outcomes:*

[Narrative assessment: e.g., "The exercise demonstrated that the CMT can be mobilised
effectively and the IT recovery team has a clear understanding of the DR procedure.
However, the exercise revealed that backup restoration has not been tested within the
stated RTO, and customer communication templates require updating. The overall BCMS 
is assessed as partially effective for this scenario; targeted improvements are recommended."]

---

## Template 7 — Management Review Record

*Satisfies ISO 22301:2019 Clause 9.3. Retained as documented information.*

---

**BCMS Management Review Record**

| Field | Value |
|-------|-------|
| Review Reference | MREV-BCM-[year]-[nn] |
| Date | [Date] |
| Chair | [Name, Role — must be top management representative] |
| Attendees | [List of attendees with roles] |
| Minutes Prepared by | [Name] |
| Next Review Due | [Date — maximum 12 months] |

---

**Agenda and Record**

**Item 1 — Status of actions from previous review**
| Action | Owner | Status | Notes |
|--------|-------|--------|-------|
| [Action from previous review] | [Owner] | Complete / In Progress / Overdue | |

**Item 2 — Changes in external and internal issues**
[Record significant changes since last review: new regulations, organisational restructuring,
new products/services, changes in risk landscape, new sites or supply chain changes]

**Item 3 — BC performance information**

*3a. Nonconformities and corrective actions:*
[Number of NCs raised since last review; number closed; number overdue; trend]

*3b. Monitoring and measurement results:*
| KPI | Target | Actual | Trend | Commentary |
|-----|--------|--------|-------|------------|
| BIA currency (% reviewed within 12 months) | 100% | | | |
| Plan currency (% reviewed within 12 months) | 100% | | | |
| Exercise completion (% planned exercises completed) | 100% | | | |
| RTO achievement rate in exercises | ≥90% | | | |
| Staff training completion | 100% | | | |
| CA close-out rate | ≥90% | | | |

*3c. Audit results:*
[Summary of internal audit findings; any external audit findings; certification status]

*3d. Exercise results:*
[Summary of exercises conducted; key findings; actions outstanding]

*3e. Incidents:*
[Summary of any BC plans invoked since last review; outcomes; lessons learned applied]

**Item 4 — Adequacy of resources**
[Review whether BC team has sufficient resource (budget, headcount, tools, technology) to
maintain and improve the BCMS. Record decisions on resourcing changes.]

**Item 5 — Effectiveness of actions to address risks and opportunities**
[Review whether actions taken since last review have been effective. Update risk register
if required.]

**Item 6 — Opportunities for improvement**
[Record improvement ideas raised during the review]

**Decisions and Actions**

| Decision / Action | Owner | Due Date |
|------------------|-------|---------|
| [Decision or action as agreed] | [Role] | [Date] |

**Approved by (Chair):** _________________________ Date: _____________

---

## Template 8 — Nonconformity and Corrective Action Record

*Satisfies ISO 22301:2019 Clause 10.1. Retained as documented information.*

---

**Nonconformity and Corrective Action Record**

| Field | Value |
|-------|-------|
| NC Reference | NC-BCM-[year]-[nn] |
| Date Raised | [Date] |
| Raised by | [Name, Role] |
| Source | Audit / Exercise / Incident / Management Review / Internal Review |
| Related Clause | [ISO 22301 clause or internal document requirement] |
| Severity | Minor / Major |

---

**Description of Nonconformity:**
[Clear statement of what was found and why it constitutes a nonconformity against the
relevant requirement. Include objective evidence.]

**Immediate Containment Action (if applicable):**
[What was done immediately to address consequences or prevent further impact]

**Root Cause Analysis:**
[Why did this nonconformity occur? Use appropriate root cause methodology (e.g., 5-Whys).
Do not confuse the symptom with the cause.]

**Corrective Action:**
| Action | Owner | Due Date | Completed Date |
|--------|-------|---------|----------------|
| [Action 1] | [Role] | [Date] | |
| [Action 2] | [Role] | [Date] | |

**Effectiveness Review:**
Date of effectiveness review: [Date — typically 30–90 days after completion]

[Was the corrective action effective? Has the nonconformity recurred? Evidence of effectiveness:]

**Status:** Open / Closed

**Closed by:** [Name, Role] **Date:** [Date]

---

## Template 9 — BCMS Internal Audit Plan

*Satisfies ISO 22301:2019 Clause 9.2. Maintained documented information.*

---

**BCMS Internal Audit Plan — [Year]**

| Field | Value |
|-------|-------|
| Document Reference | AUD-BCM-[year]-01 |
| Audit Programme Owner | [BCMS Manager] |
| Audit Period | [Start date – End date] |
| Version | [x.x] |

**Audit scope:** Full BCMS — ISO 22301:2019 Clauses 4–10

**Auditor independence:** Internal auditors must not audit their own work. Where BCMS Manager
is sole internal auditor, audit of BCMS management processes must be conducted by an
independent colleague or contracted third party.

**Audit Schedule:**

| Audit # | Clause(s) | Focus Area | Auditor | Planned Date | Status |
|---------|-----------|-----------|---------|-------------|--------|
| 1 | 4.1, 4.2, 4.3 | Context and scope | [Auditor] | [Date] | Planned |
| 2 | 5.1, 5.2, 5.3 | Leadership and policy | [Auditor] | [Date] | Planned |
| 3 | 6.1, 6.2 | Planning and objectives | [Auditor] | [Date] | Planned |
| 4 | 7.1–7.5 | Support — training, comms, documentation | [Auditor] | [Date] | Planned |
| 5 | 8.1, 8.2 | BIA and risk assessment | [Auditor] | [Date] | Planned |
| 6 | 8.3, 8.4 | BC strategy, plans, procedures | [Auditor] | [Date] | Planned |
| 7 | 8.5, 8.6 | Exercises and testing | [Auditor] | [Date] | Planned |
| 8 | 9.1, 9.2, 9.3 | Performance evaluation and management review | [Auditor] | [Date] | Planned |
| 9 | 10.1, 10.2 | Nonconformity and improvement | [Auditor] | [Date] | Planned |

**Audit outputs:** Each audit produces an audit report summarising findings, nonconformities
(if any), and observations. Reports are submitted to the BCMS Manager and reviewed at
management review.

---

## Template 10 — BC Competence Matrix

*Satisfies ISO 22301:2019 Clause 7.2. Retained as documented information.*

---

**BC Competence and Training Matrix**

| Competency Area | Required For | Training Method | [Name 1 — Role] | [Name 2 — Role] | [Name 3 — Role] | [Name 4 — Role] |
|----------------|-------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| ISO 22301:2019 overview | All BC team | Induction + annual briefing | | | | |
| BIA methodology and facilitation | BCMS Manager, BIA Facilitators | External training / internal training | | | | |
| Risk assessment methodology | BCMS Manager | External / internal | | | | |
| BCMS internal audit | Internal auditors | ISO 22301 Lead Auditor course or internal | | | | |
| Incident Commander role | Incident Commander + alternates | Tabletop exercise; crisis leadership training | | | | |
| Incident response procedures | CMT members | Annual tabletop exercise | | | | |
| BCP ownership and activation | Plan owners | Annual BCP walkthrough + exercise | | | | |
| IT DR procedures | IT Recovery team | Annual IT DR test participation | | | | |
| Crisis communications | Communications Lead | Media training; exercise participation | | | | |

**Key:**
- C = Competent (trained and assessed as competent)
- T = Trained (training completed, competency assessment pending)
- P = Planned (training scheduled)
- N = Not yet trained
- Date = Date training last completed

*Update this matrix following each training event. Training records must be retained as evidence.*

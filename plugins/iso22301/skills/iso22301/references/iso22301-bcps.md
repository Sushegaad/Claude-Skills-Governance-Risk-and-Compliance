# ISO 22301:2019 — Business Continuity Plans and Procedures Reference

## Purpose

This reference provides detailed guidance on the structure, content, and maintenance of Business
Continuity Plans (BCPs), Incident Response Plans, communication procedures, and recovery
procedures required under ISO 22301:2019 Clauses 8.4.1 through 8.4.5.

---

## Plan Architecture

Under ISO 22301:2019, an organisation's suite of BC plans forms a hierarchy. Each plan serves
a distinct purpose and must interlock with the others:

```
INCIDENT RESPONSE PLAN (IRP)
  Purpose: Detect, declare, and manage the overall incident; mobilise the BC response
  Clause: 8.4.2
  Owner: Crisis Management Team / Incident Commander
       |
       v
BUSINESS CONTINUITY PLANS (BCPs)
  Purpose: Maintain minimum service levels for critical activities during the disruption
  Clause: 8.4.4
  Owner: Function/Department leads (per BIA priority)
       |
       v
RECOVERY PLANS
  Purpose: Restore activities to normal operating levels
  Clause: 8.4.5
  Owner: Function/Department leads + IT Recovery Lead
       |
       v
IT DISASTER RECOVERY PLAN (IT DRP)
  Purpose: Technical recovery of IT systems and infrastructure
  Clause: 8.3.2 (strategy) + 8.4.4 (plan), 8.5.2 (testing)
  Owner: IT Director / IT Recovery Lead
```

Plans are activated in sequence (IRP → BCP + IT DRP → Recovery Plan) though activation
of individual BCPs may occur in parallel depending on the nature of the incident.

---

## Clause 8.4.2 — Incident Response Plan (IRP)

### Purpose
The IRP defines how the organisation detects, declares, and manages a disruptive incident
from the first moment of awareness through to activation of BC plans and eventual stand-down.

### Minimum IRP Content (per ISO 22301:2019 Clause 8.4.2)

**1. Activation Criteria**
Define the specific conditions that constitute a "declarable incident" for the organisation.
Activation criteria prevent over-escalation (treating minor issues as incidents) and
under-escalation (allowing major disruptions to proceed without invoking plans).

| Severity Level | Threshold | Response Level |
|----------------|-----------|----------------|
| Level 1 — Incident | Single system unavailability; <10 staff affected; <1 hour expected duration | IT support + line manager; no BCP activation |
| Level 2 — Disruption | Multiple systems down; >10 staff affected; 1–4 hours expected; no customer impact | Department head + IT; monitoring mode; BCP on standby |
| Level 3 — Major Disruption | Critical system unavailability; customer impact likely; >4 hours expected | Crisis Management Team convened; BCPs pre-positioned |
| Level 4 — Crisis | Site loss; major data breach; life-safety event; regulatory exposure | Full BCP activation; Board notification; external communications |

**2. Notification and Mobilisation**

Define the cascade:
- Who is notified first (typically: IT on-call → BC Manager → Incident Commander)
- How confirmation of mobilisation is obtained
- What channel to use if primary channels are unavailable
- Contact details (personal mobile, home phone, emergency SMS service)

**3. Crisis Management Team (CMT) Structure**

| Role | Responsibilities During Incident | Primary Contact | Alternate |
|------|-----------------------------------|----------------|-----------|
| Incident Commander | Overall incident control; escalation decisions; authorise external communications | [Name/Role] | [Alternate] |
| BC Manager / Coordinator | Activating BCPs; tracking recovery actions; status reporting | [Name/Role] | [Alternate] |
| IT Recovery Lead | Technical recovery decisions; DR activation; vendor liaison | [Name/Role] | [Alternate] |
| Communications Lead | Internal communications; customer notifications; media statements | [Name/Role] | [Alternate] |
| HR Lead | Staff welfare; remote working arrangements; emergency staffing | [Name/Role] | [Alternate] |
| Finance Lead | Emergency expenditure authorisation; insurer notification | [Name/Role] | [Alternate] |
| Legal/Compliance Lead | Regulatory notifications; contractual obligations; legal advice | [Name/Role] | [Alternate] |
| Premises/Facilities Lead | Building access; alternate sites; health and safety | [Name/Role] | [Alternate] |

**4. CMT Meeting Protocol**

- Initial convening: within [X] minutes of Level 3/4 declaration
- Location: CMT room (primary) / virtual bridge (alternate)
- Meeting frequency during incident: every [X] hours; daily at [time] for extended incidents
- Standard agenda: situation update → current actions → new risks → decisions required → assignments
- Action log maintained in real time

**5. Immediate Priorities (First 2 Hours)**

Regardless of incident type, these priorities apply in order:
1. **Life safety**: Ensure the safety of all people in affected locations
2. **Damage containment**: Prevent incident from spreading or worsening
3. **Crisis team mobilisation**: Convene CMT; establish communications
4. **Situational assessment**: Understand scope, cause, expected duration
5. **Stakeholder notification**: Internal notifications per cascade; customers on standby
6. **BCP activation decision**: Invoke relevant BCPs; brief plan owners

**6. Escalation and De-escalation Criteria**

*Escalation*: Criteria for moving from Level 2 to Level 3 or Level 3 to Level 4 (e.g.,
incident duration exceeds 4 hours; customer impact confirmed; regulatory threshold triggered).

*De-escalation and stand-down*: Criteria for reducing alert level and standing down BCPs:
- Critical systems restored and validated
- All customer SLAs recoverable within acceptable timeframes
- Legal/regulatory exposures managed
- No further risk of re-escalation
- Formal sign-off by Incident Commander

---

## Clause 8.4.3 — Communication Procedures

### Communication Plan During Incidents

**Internal communication cascade:**

| Audience | Timing | Channel | Message Content | Owner |
|----------|--------|---------|----------------|-------|
| CMT members | Immediate | Personal mobile / emergency SMS | Incident declared; convene at [location/bridge] | BC Manager |
| Department heads not on CMT | Within 30 min | Mobile / email | Situation summary; instructions for their teams | Incident Commander |
| All staff | Within 60 min | All-staff email + intranet notice | What has happened; what staff should do; further updates promised by [time] | Communications Lead |
| Remote/home workers | Within 60 min | Email + messaging platform | Actions required; how to access systems/work | HR Lead |
| Board / Executive | Within 2 hours (Level 4) | Direct call or CMT briefing | Situation, response, risk, escalation | Incident Commander |

**External communication procedures:**

| Audience | Trigger | Timing | Channel | Template | Owner |
|----------|---------|--------|---------|----------|-------|
| Customers (proactive) | Service impact confirmed | Within 2 hours | Email + portal notice + account manager calls | Customer communication template | Communications Lead |
| Customers (reactive) | Customer enquiry received | Immediate | Phone / email | Holding message template | Customer service + Communications Lead |
| Regulators | Notifiable incident threshold met | Per regulatory requirement (e.g., 72 hours for data breach) | Formal notification to regulator | Regulatory notification template | Legal/Compliance Lead |
| Insurers | Potential claim event | Within 24 hours | Direct contact with broker | Incident notification | Finance Lead |
| Media | Media enquiry received | As required | Press statement (no comment until approved) | Media holding statement | Communications Lead + Incident Commander |
| Social media | Significant public-facing impact | As required | Official channels only | Pre-approved statements only | Communications Lead |

### Communication Templates

**All-staff notification — initial:**
```
Subject: [INCIDENT NOTIFICATION] Business disruption — [Date]

To all staff,

You should be aware that we are currently experiencing [brief description of incident].

What this means for you:
[Specific instructions — e.g., "Please work from home today" / "Do not access the X system"]

Our business continuity procedures have been activated. You will receive an update by [time].

If you have urgent queries, please contact [name/role] via [channel].

[Signed by Incident Commander or designated leader]
```

**Customer communication — service disruption:**
```
Subject: Service update — [date]

Dear [Name],

We are writing to inform you that we are experiencing a technical disruption affecting
[specific services]. We expect this to be resolved by [estimated time / "we will update
you within X hours"].

[Description of impact on customer and any interim arrangements]

We apologise for any inconvenience caused and appreciate your patience.

We will keep you updated at [interval/channel]. If you have an urgent requirement,
please contact [contact name/number].

[Signed by Communications Lead / Account Manager]
```

**Media holding statement:**
```
[ORGANISATION NAME] is aware of an incident affecting its operations. Our teams are
working to restore normal service as quickly as possible. We are committed to keeping
our customers and stakeholders informed.

We will provide a further statement at [time / date].

For media enquiries, please contact: [Communications Lead, phone number].
```

---

## Clause 8.4.4 — Business Continuity Plan (BCP) Template

### BCP Document Structure

The following structure satisfies ISO 22301:2019 Clause 8.4.4 requirements for all BCPs.
Each plan covers a specific function, department, or critical activity.

---

**DOCUMENT CONTROL**

| Field | Value |
|-------|-------|
| Plan Title | Business Continuity Plan — [Function/Department/Site] |
| Plan Reference | BCP-[code] |
| Version | [x.x] |
| Status | Active / Draft / Under Review |
| Plan Owner | [Role, not individual name] |
| Approved by | [Role — must be appropriate level for plan's criticality] |
| Date of Issue | [Date] |
| Next Review Date | [Date — maximum 12 months from issue] |
| Classification | [e.g., Confidential — BCM Team Only] |
| Last Exercise Date | [Date] |
| Copy Location | [Primary: document management system] [Backup: hardcopy location] |

**Change Record**

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | [Date] | [Name] | Initial issue |
| 1.1 | [Date] | [Name] | [Description] |

---

**1. PURPOSE AND SCOPE**

This plan provides the procedures to maintain [minimum service level / MBCO] for [Function/
Department/Activity] during a business disruption, until normal operations are restored.

**In-scope activities covered by this plan:**
- [Activity A — brief description]
- [Activity B — brief description]

**Products/services maintained during invocation:**
- [Product/service and minimum service level during invocation]

**Activities not covered by this plan:**
- [List lower-priority activities that will be suspended during invocation]

**Relationship to other plans:**
- This plan is activated by the Incident Response Plan (IRP-001)
- IT recovery is covered by the IT Disaster Recovery Plan (ITDR-001)
- [Other linked plans]

---

**2. ACTIVATION**

**Conditions for activation:**
This plan is activated when one or more of the following conditions are met:
- The Incident Commander declares a Level [3/4] incident
- [System X] is unavailable for more than [Y] hours
- [Specific scenario, e.g., primary site is inaccessible]
- Directed by [role] via [channel]

**Who activates:**
The Plan Owner (or designated alternate) activates this plan upon instruction from the Incident
Commander or the BC Manager. Plan Owner confirms activation via [channel] to the CMT.

**If Plan Owner is unreachable:**
Contact [Alternate 1 — Role — Mobile] then [Alternate 2 — Role — Mobile].

---

**3. ROLES AND RESPONSIBILITIES**

| Role | During-Incident Responsibility | Primary: Role/Name | Backup: Role/Name |
|------|-------------------------------|-------------------|-------------------|
| Plan Owner | Activating plan; briefing team; reporting to CMT; escalating issues | [Role] | [Role] |
| Operations Lead | Executing continuity procedures; managing output; tracking backlog | [Role] | [Role] |
| Technology Lead | IT liaison; alternative access setup; data recovery co-ordination | [Role] | [Role] |
| Staff Coordinator | Managing team attendance; remote working arrangements | [Role] | [Role] |

**Contact details** (store in secure, accessible location outside this document to allow update without re-versioning):
Reference contact directory: [location/system]

---

**4. IMMEDIATE ACTIONS (FIRST 2 HOURS)**

Upon activation, the Plan Owner executes the following steps in order:

| Step | Action | Responsibility | Time Target |
|------|--------|---------------|-------------|
| 1 | Confirm activation with Incident Commander via [channel] | Plan Owner | T+0 |
| 2 | Notify team of activation; communicate immediate instructions | Plan Owner | T+15 min |
| 3 | Assess current work status: backlog, in-progress, committed deadlines | Operations Lead | T+30 min |
| 4 | Activate IT DR plan / contact IT Recovery Lead | Technology Lead | T+15 min |
| 5 | Establish team at alternate location / confirm remote access | Staff Coordinator | T+60 min |
| 6 | Report status to CMT via [channel] | Plan Owner | T+2 hours |
| 7 | Communicate to customers/partners as directed by Communications Lead | Plan Owner | Per comms plan |

---

**5. CONTINUITY PROCEDURES**

**Activity: [Activity Name] — MBCO: [e.g., 50% of normal daily volume]**

*Normal process description:* [Brief description of how this normally works]

*During-disruption procedure:*
1. [Step 1 — what to do if primary system unavailable]
2. [Step 2 — what workaround to use]
3. [Step 3 — how to record work done manually if needed]
4. [Step 4 — who to escalate to if workaround fails]

*Resources required at MBCO:*
- Staff: [minimum number and roles]
- Location: [alternate site / remote working requirements]
- Technology: [minimum systems needed; fallback if unavailable]
- Information: [key data/records needed; offline versions available at: location]

*Minimum viable process (if technology entirely unavailable):*
[Describe paper / manual fallback if IT systems are completely unavailable]

---

**6. COMMUNICATION**

**Updates to CMT:**
- Frequency: Every [2/4/8] hours via [channel: status report / call / dashboard]
- Update content: current backlog, actions completed, issues, resource needs

**Communication to customers:**
Per communications plan (COMMS-001). This plan does not authorise independent customer
communication. All messages must be approved by Communications Lead.

**Communication to staff:**
Plan Owner communicates with team via [channel] at [frequency] to maintain situational
awareness and morale during prolonged invocations.

---

**7. RECOVERY**

The recovery phase begins when normal systems and services are restored and operational.

**Conditions to begin recovery:**
- IT Recovery Lead confirms [specific systems] are restored and validated
- Incident Commander authorises transition to recovery mode
- [Any other conditions, e.g., building access restored, supplier confirmed available]

**Recovery steps:**
| Step | Action | Responsibility |
|------|--------|---------------|
| 1 | Validate data integrity of restored systems before using in live operations | Technology Lead |
| 2 | Assess backlog accumulated during incident; prioritise clearing | Operations Lead |
| 3 | Communicate resumption of normal service to customers | Communications Lead |
| 4 | Manage staff transition from remote/alternate to normal locations | Staff Coordinator |
| 5 | Restore all archived/manual records to systems | Operations Lead |
| 6 | Confirm to CMT that normal operations fully restored | Plan Owner |
| 7 | Complete post-incident review within [X] days | Plan Owner |

**Post-incident review:**
Within [X] days of stand-down, Plan Owner submits an after-action report covering:
- What went well
- What did not work as expected
- Recommended plan updates
- Corrective actions required

Submit report to BC Manager for inclusion in BCMS nonconformity and improvement process.

---

**8. SUPPORTING INFORMATION**

**Alternate work location:**
Primary alternate site: [Name, address, contact]
Access: [How to access: key, swipe card, temporary pass — contact Facilities Lead]
IT connectivity: [VPN access; on-site workstations available: yes/no; number]
Capacity: [maximum concurrent users]

**Vital records location:**
| Record | Normal Location | Emergency Copy Location |
|--------|----------------|------------------------|
| Customer contracts | CRM system | [Backup: cloud archive] |
| Supplier contact list | Shared drive | [Backup: printed list, Facilities office] |
| Payroll data | HR system | [Backup: monthly extract, secure offsite] |

**Key vendor and supplier contacts:**
Reference supplier contact directory: [location/system]

**Insurance:**
Business interruption policy: [Policy number / broker contact]
Cyber insurance: [Policy number / broker contact if applicable]

---

**9. PLAN MAINTENANCE**

This plan shall be reviewed:
- Annually as part of the BCMS review cycle
- Following any invocation
- Following any significant exercise
- When organisational structure, systems, or processes change materially

Plan owner is responsible for initiating the review and obtaining re-approval. All changes
must be recorded in the change record and communicated to all holders.

---

## Clause 8.4.5 — Recovery Plan Considerations

The recovery phase is distinct from the continuity phase. While the BCP maintains minimum
service (MBCO), the recovery plan restores normal operations.

### Key Recovery Activities

**Damage assessment:**
- Physical damage: structures, equipment, inventory
- Data integrity: what data is confirmed intact, what requires restoration, what is lost
- System status: what is online, what requires recovery, estimated time to full restoration
- Staff: welfare status, ability to return to normal locations/roles

**Recovery sequencing:**
Recovery activities must follow BIA priority order — Critical activities first, then High,
Medium, Low. Never attempt to recover everything simultaneously if resources are constrained.

**Data restoration validation:**
Before using restored data in live operations:
- Confirm backup integrity (test restore completed successfully)
- Reconcile record counts against last known good state
- Validate key transactions were captured
- Sign-off from data owner before going live

**Return-to-normal decision:**
Incident Commander authorises return to normal following confirmation from each function head
that they have validated their systems and data. Do not return to normal until all critical
functions have confirmed readiness.

**Post-incident review (all incidents):**
All invocations of BCPs must be followed by a post-incident review, regardless of duration.
Review covers: what happened, what worked, what failed, what must change. Outputs fed into
BCMS nonconformity process (Clause 10.1) and improvement process (Clause 10.2).

---

## IT Disaster Recovery Plan (IT DRP) Essentials

The IT DRP is a technical plan required to support Clause 8.3.2 (strategies — technology)
and validated under Clause 8.5.2 (testing). It sits beneath the overarching BCP suite.

### Minimum IT DRP Content

**1. System Inventory and Recovery Priority**

| System | Business Owner | Criticality | RTO | RPO | Recovery Approach |
|--------|---------------|-------------|-----|-----|------------------|
| ERP (SAP) | CFO | Critical | 6 hours | 4 hours | Warm DR site — 4-hour spin-up |
| CRM | Sales Director | Critical | 8 hours | 24 hours | Cloud failover |
| HR System | HR Director | High | 24 hours | 24 hours | Restore from daily backup |
| Email/Comms | IT Director | Critical | 2 hours | 1 hour | Microsoft 365 geo-redundant |
| File shares | All | High | 8 hours | 24 hours | Restore from daily backup |

**2. Recovery Site Details**
- DR site address and access instructions
- Hardware configuration and capacity at DR site
- Network connectivity (bandwidth, latency, VPN configuration)
- How staff access DR environment (VPN, RDP, Citrix)

**3. Step-by-Step Recovery Procedures**
For each critical system:
- Failover sequence (order of operations)
- Commands or scripts to execute
- Validation tests to confirm system is operational
- Approvals required before going live on DR instance

**4. Backup Schedule and Retention**

| System | Backup Type | Frequency | Retention | Location | Restoration Time |
|--------|------------|-----------|-----------|----------|-----------------|
| ERP | Full | Weekly (Sunday 02:00) | 4 weeks | Offsite vault + cloud | Tested: 3.5 hours |
| ERP | Incremental | Daily (23:00) | 7 days | Cloud | Tested: 45 minutes |
| File shares | Incremental | Daily (00:00) | 30 days | Cloud | Tested: 2 hours |

**5. Test Results Log**
Record of all IT DR tests: date, system tested, RTO achieved, RPO validated, issues found,
corrective actions. This feeds Clause 9.1 (monitoring) and satisfies Clause 8.5.2 (testing).

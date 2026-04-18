# DORA — Incident Management, Classification and Reporting Reference

Chapter III, Articles 17–23, Regulation (EU) 2022/2554.
Key implementing measures: CDR (EU) 2024/1772, CDR (EU) 2025/301, CIR (EU) 2025/302.

---

## Art. 17 — ICT-Related Incident Management Process

Financial entities must establish and implement a **documented ICT-related incident
management process** as part of their overall ICT risk management framework.

### Minimum elements (Art. 17(1)):
- **(a)** Procedures for detecting, managing, and notifying ICT-related incidents
- **(b)** Criteria and thresholds for classifying incidents as major (aligned
  with CDR (EU) 2024/1772)
- **(c)** Escalation procedures — who is notified when, including senior management
  and the board
- **(d)** Roles and responsibilities of ICT incident response staff
- **(e)** Communication procedures for internal escalation and external reporting

### Senior management involvement (Art. 17(3)):
- Major ICT-related incidents must be reported to **senior management**
- The management body (board) must be **informed** of major incidents
- The board must have oversight of the entity's exposure to ICT risks

### Customer communication (Art. 17(4)):
- Financial entities must promptly communicate to clients about major ICT incidents
  that may affect their financial interests
- Must include details of measures taken and, where known, estimated recovery time

---

## Art. 18 — Classification of ICT-Related Incidents

### Step 1: Is the incident ICT-related?

An **ICT-related incident** is any unplanned event that compromises the security
of network and information systems, and has an adverse impact on the availability,
authenticity, integrity or confidentiality of data, or on the services provided
by the financial entity.

A **cyber threat** is any potential circumstance, event or action that could harm
systems, data, or services (even without having materialized yet).

### Step 2: Apply the classification criteria (Art. 18(1))

| Criterion | Description | Materiality threshold (CDR 2024/1772) |
|-----------|-------------|--------------------------------------|
| (a) Clients and transactions | Number of clients affected; value of impacted transactions | ≥ 10% of clients OR > 5,000 clients; value thresholds by entity type |
| (b) Reputational impact | Public media coverage; regulatory attention; reputational damage | Significant negative press coverage likely; regulatory inquiry expected |
| (c) Duration and geographic spread | Hours/days of disruption; number of Member States affected | ≥ 2 hours for critical services; multi-Member State impact |
| (d) Data losses | Loss of availability, authenticity, integrity or confidentiality | Any loss of client data integrity or confidentiality; availability loss ≥ 2h |
| (e) Criticality of services | Impact on critical or important functions | Critical function impacted |
| (f) Economic impact | Direct and indirect financial losses | To be set by ESAs per entity type and size |

**Classification logic:** An incident is **major** if it meets or exceeds
**any single threshold** from CDR (EU) 2024/1772 (OR logic, not AND logic).

### Step 3: Major or non-major?

| Classification | Consequence |
|----------------|-------------|
| **Major ICT-related incident** | Three-stage regulatory reporting to competent authority (Art. 19) + internal escalation to board |
| **Non-major ICT-related incident** | Internal incident management process only; no regulatory reporting obligation |
| **Significant cyber threat** | Voluntary notification to competent authority under Art. 19(2) encouraged |

---

## Art. 19 — Reporting of Major ICT-Related Incidents

### Three-Stage Reporting Timeline

| Stage | Deadline | Trigger | Key Content |
|-------|----------|---------|-------------|
| **Initial notification** | Within **4 hours** of classification as major | From the moment the entity classifies the incident as major | Incident type; initial impact; functions affected; preliminary recovery estimate |
| **Intermediate report** | Within **72 hours** of classification | From the same moment as the 4h clock | Updated impact; root cause indications; measures taken; updated recovery estimate |
| **Final report** | Within **1 month** of the initial notification | One month after the initial report | Root cause analysis; full impact; lessons learned; measures implemented or planned |

**Time counting:** The clocks start when the incident is **classified as major**,
not when it is first detected. Entities must establish clear classification criteria
to avoid uncertainty about when the clock starts.

> **Critical interpretive point:** The 4-hour deadline runs from the moment of
> **classification as major** (CDR (EU) 2025/301, Art. 3), NOT from the moment of
> detection. However, entities must not use this to game the timeline — extended
> triage that delays classification is itself a supervisory risk. The obligation
> is to classify promptly and report within 4 hours of that classification.
> Competent authorities may scrutinise delayed classification as evidence of an
> inadequate incident management process (Art. 17(1)).

### How to Count the 4-Hour Deadline

1. **Detection:** ICT monitoring tools detect anomalous activity
2. **Triage:** Incident response team investigates — is this an ICT-related incident?
3. **Classification:** Against CDR 2024/1772 thresholds — major or non-major?
   — Classification must be made **promptly**; triage should not extend beyond
   what is operationally necessary to apply the thresholds
4. **Clock starts:** From the moment of classification as major
5. **Initial notification:** Must reach competent authority within 4 hours

**Practical implication:** If classification occurs at 22:00 on a Friday, the
initial notification must still be submitted by 02:00 Saturday. DORA does not
provide for weekend/business hours exceptions in the 4-hour initial notification.

### Reporting Channel

Reports are submitted to the **home Member State competent authority** using the
standard templates from **CIR (EU) 2025/302**. The competent authority is:

| Entity type | Competent authority |
|-------------|-------------------|
| Credit institutions | National banking supervisory authority (e.g., ECB/SSM for significant institutions; national NCA for less significant) |
| Investment firms | National securities market authority |
| Insurance undertakings | National insurance supervisor |
| Payment institutions / E-money institutions | National payment supervisor |
| Crypto-asset service providers | National authority per MiCA |

### Cross-Border Incidents

For entities operating in multiple Member States:
- Report to the **home state** competent authority (Art. 19(1))
- The home state authority is responsible for forwarding to host state authorities
  where relevant (Art. 19(5))
- No obligation to report directly to host state authorities

### Voluntary Notification of Significant Cyber Threats (Art. 19(2))

Financial entities **may voluntarily notify** competent authorities of:
- Significant cyber threats that have not (yet) materialized into an incident
- Threats that the entity believes could be of relevance to the financial system

This is encouraged but not mandatory. CDR (EU) 2025/301 and CIR (EU) 2025/302
provide templates for voluntary notifications.

---

## Art. 20 — Harmonisation of Reporting Content, Timelines and Templates

ESAs adopted two measures:

- **CDR (EU) 2025/301:** Specifies the mandatory content of each report stage
  and the exact time limits
- **CIR (EU) 2025/302:** Provides the standard forms and electronic templates

### Content Requirements per Stage (CDR (EU) 2025/301)

**Initial notification (4h report):**
- Unique incident reference number
- Reporting entity details (LEI, entity name, entity type)
- Date and time of incident detection
- Date and time of classification as major
- Nature of the incident (cyber attack, system failure, third-party failure, etc.)
- Affected ICT systems and functions
- Initial client impact estimate
- Initial financial impact estimate
- Measures immediately taken

**Intermediate report (72h report):**
- Updated version of all initial notification fields
- Updated root cause assessment (hypothesis or confirmed)
- Updated client and financial impact
- Response and recovery measures taken since initial notification
- Revised recovery time estimate
- Whether the incident is contained or ongoing

**Final report (1-month report):**
- Confirmed root cause analysis
- Final client and financial impact assessment
- Total duration of the incident (from detection to resolution)
- Complete timeline of events
- Description of all response and recovery measures implemented
- Preventive measures adopted or planned
- Lessons learned
- Whether the incident was caused by an ICT third-party service provider
  (and if so, identification of the TPSP where permitted)

---

## Art. 21 — Centralisation of Reporting

- ESAs are tasked with assessing the feasibility of a **single EU reporting hub**
  for major ICT incident reports
- Pending a centralised hub, financial entities report to their national competent
  authority which coordinates with other authorities
- Supervisors share incident report information with other relevant authorities
  (e.g., ECB, ENISA, CERT-EU) where appropriate under Art. 21(3)

---

## Art. 22 — Supervisory Feedback

After receiving a major incident report (any stage), competent authorities:
- May provide **feedback** to the financial entity, including:
  - Indicative impact assessment of the incident for the financial system
  - Relevant anonymised cyber threat intelligence from other entities
  - Suggested preventive measures or recommendations
- This is at the supervisor's discretion; financial entities cannot compel
  supervisory feedback

---

## Art. 23 — Payment-Related Major Incidents

**Applies to:**
- Credit institutions (for payment services)
- Payment institutions
- E-money institutions
- Account information service providers

**Integration with PSD2:** Art. 23 DORA replaces the pre-DORA payment incident
reporting obligation under PSD2 Art. 96 for incidents that qualify as **major**
under DORA. For non-major payment incidents that would previously have triggered
PSD2 Art. 96 reporting: PSD2 obligations may still apply for those incidents below
the DORA major threshold — consult your national competent authority on whether
PSD2 reporting continues for sub-threshold payment incidents.

**Dual-licensed entities:** Credit institutions that also hold payment institution
authorisation must clarify with their competent authority whether payment-related
major incidents require reporting to both the banking supervisor (as competent
authority under DORA) and the payment supervisor. In most Member States, the
banking supervisor is the single point of receipt and distributes to other
authorities as needed — but this should be confirmed before an incident occurs.

**Reporting to payment authorities:** For payment-related major incidents, the
entity reports to its **home payment supervisor** using the DORA templates, which
include payment-specific fields per CIR (EU) 2025/302 — the ITS provides a
dedicated payment-incident reporting template aligned with legacy PSD2 Art. 96
reporting formats.

---

## Incident Management Policy — Minimum Required Elements

A DORA-compliant incident management policy (Art. 17(1)) must include:

1. **Scope:** What constitutes an ICT-related incident for this entity
2. **Detection procedures:** How incidents are identified (monitoring tools, alerts,
   staff reports, third-party notifications)
3. **Triage and classification:** Step-by-step process to assess against CDR
   2024/1772 criteria; who makes the major/non-major determination
4. **Escalation matrix:**
   - Level 1 (non-major): ICT operations team
   - Level 2 (potential major): CISO and incident commander
   - Level 3 (confirmed major): Senior management (CEO/CRO) and board notification
5. **Reporting obligations:** Who is responsible for filing the 4h/72h/1-month
   reports; templates to use; competent authority contact details
6. **Client communication:** Timing, channel, and content of client notifications
7. **Post-incident review:** Trigger criteria; who conducts the review; output
   requirements (lessons learned, preventive measures)
8. **Testing:** How and when the incident management process is tested (tabletop
   exercises, simulations)
9. **Record retention:** How long incident records are retained (minimum
   recommended: 5 years)

---

## Incident Classification Decision Tree

```
Is the event an ICT-related incident?
(Unplanned event compromising NIS with adverse impact on operations/data)
│
├─ NO → Standard IT issue; handle via normal IT operations; no DORA reporting
│
└─ YES → Apply CDR 2024/1772 classification criteria
         │
         ├─ Does it meet or exceed ANY threshold in CDR 2024/1772?
         │   (clients affected / transaction value / service duration /
         │    data loss / critical function impact / economic impact)
         │
         ├─ NO → Non-major incident
         │        → Internal incident management process only
         │        → No Art. 19 regulatory reporting
         │        → Document in incident log
         │
         └─ YES → Major ICT-related incident
                  → Escalate to senior management immediately
                  → Notify board (Art. 17(3))
                  → Initial report to competent authority within 4 HOURS
                  → Intermediate report within 72 HOURS
                  → Final report within 1 MONTH
                  → Notify affected clients (Art. 17(4))
```

---

## Common Classification Mistakes

| Mistake | Correct Approach |
|---------|-----------------|
| Waiting for root cause before classifying | Classify as major the moment any threshold is met; root cause analysis follows |
| Treating the 4h clock as a business hours deadline | The 4h deadline runs 24/7/365 |
| Not classifying a third-party outage as a DORA incident | If a TPSP outage causes an ICT-related incident for the financial entity, the entity must classify and report — it is not the TPSP's obligation to report on the entity's behalf |
| Only reporting when the incident is resolved | DORA requires reporting while the incident is ongoing; the intermediate and final reports update as information becomes available |
| Treating a significant cyber threat as non-reportable | Voluntary notification under Art. 19(2) is encouraged |
| Confusing Art. 17 (process) with Art. 18 (classification) | Art. 17 = the ongoing process; Art. 18 = how to classify a specific event |

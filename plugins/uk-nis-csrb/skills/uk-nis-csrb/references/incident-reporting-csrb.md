# UK CSRB — Enhanced Incident Reporting Reference
## Cyber Security and Resilience Bill: Incident Reporting Obligations

> **Important — Bill Status:** The CSRB incident reporting provisions described here are based on
> the Bill's policy intent and published DSIT guidance. Final provisions may differ. Verify
> against enacted legislation and statutory instruments at bills.parliament.uk.

---

## Overview

The Cyber Security and Resilience Bill introduces a materially expanded incident reporting regime
compared with the NIS Regulations 2018. The key changes are:

1. **Wider reportable events** — Not just service-impacting incidents, but near-misses, precursor
   events, ransomware deployments, and supply chain incidents
2. **Compressed timelines** — Initial notification expected within 24 hours (compared with
   72-hour guidance under NIS Regs 2018)
3. **Standardised reporting** — Structured, machine-readable reporting formats expected
4. **New entities reporting** — MSPs and data centre operators added to reporting obligations
5. **Enhanced government visibility** — Reports will feed into national threat picture maintained
   by DSIT and NCSC

---

## Part 1 — Reportable Events Under the CSRB

### 1.1 Events Requiring Notification

The CSRB is expected to require notification for a broader set of events than the NIS Regulations.
The following categories are based on the policy intent and analogy with the EU NIS2 Directive
(which the CSRB draws from):

| Category | Description | NIS Regs 2018 | CSRB |
|----------|-------------|---------------|------|
| Service-impacting incident | Incident causing significant disruption to essential/digital service | Required | Required |
| Near-miss | Event that could have caused significant impact but was contained | Not required | Expected |
| Ransomware deployment | Detection of ransomware in systems, even if contained before service impact | Not required | Expected (likely separate track) |
| Data exfiltration | Confirmed or suspected theft of data from in-scope systems | Not required separately | Expected |
| Supply chain incident | Compromise of a supplier or MSP with access to in-scope systems | Not required separately | Expected |
| Precursor/reconnaissance | Detected TTPs suggesting imminent attack | Not required | Possible (proactive sharing) |

### 1.2 Impact Assessment Factors

The CSRB retains the existing impact assessment factors from the NIS Regulations and expands them.
Where an event meets the lower CSRB threshold, organisations should consider:

**Retained NIS Regs factors:**
- Number of users affected
- Duration of disruption
- Geographic spread
- Extent of service impairment
- Economic and societal impact

**Additional CSRB factors (expected):**
- Whether the event involved ransomware (separate reporting track)
- Whether a supply chain component was involved
- Whether data was exfiltrated or at risk of exfiltration
- Whether the event originated from a state-affiliated threat actor
- Whether the event is a near-miss (what controls prevented service impact?)

---

## Part 2 — Reporting Timelines

### 2.1 Expected CSRB Timeline

Based on published policy intent and the EU NIS2 model:

| Stage | Timeline | Content |
|-------|----------|---------|
| Early notification / initial alert | Within 24 hours of awareness | Minimal details: event type, approximate time, initial assessment of scope |
| Full incident notification | Within 72 hours of awareness | Full details: systems affected, impact, response actions, initial root cause |
| Final report | Within 30 days of resolution | Root cause, full timeline, controls failure analysis, remediation taken |

> Note: Exact timelines will be set by secondary legislation. The 24/72-hour structure parallels EU NIS2 and is the most likely model for the CSRB. Organisations should plan for 24-hour initial notification as the worst-case timeline.

### 2.2 Comparison: NIS Regs 2018 vs CSRB vs EU NIS2

| Framework | Initial Notification | Full Report | Near-miss |
|-----------|---------------------|-------------|-----------|
| NIS Regs 2018 | As soon as practicable (72hr guidance) | No prescribed deadline | Not required |
| EU NIS2 | 24 hours (early warning) | 72 hours (notification) | Not required |
| UK CSRB (expected) | 24 hours | 72 hours | Expected for some categories |

---

## Part 3 — Notification Templates

### 3.1 CSRB Early Notification Template (24-Hour)

```
CSRB EARLY NOTIFICATION (24-HOUR ALERT)

Submission Date/Time (UTC): [YYYY-MM-DD HH:MM]
Organisation Name:
Organisation Type:  [ ] OES  [ ] DSP  [ ] MSP  [ ] Data Centre
Competent Authority:
Reporting Contact (Name, Role, Email, Phone):

EVENT TYPE (select all that apply):
  [ ] Significant service disruption
  [ ] Near-miss (contained — no service impact)
  [ ] Ransomware deployment
  [ ] Data exfiltration (confirmed/suspected)
  [ ] Supply chain / third-party compromise
  [ ] Unauthorised access (no confirmed disruption)
  [ ] DDoS / availability attack
  [ ] Other (brief description):

BRIEF DESCRIPTION:
Date/Time event first detected (UTC): [YYYY-MM-DD HH:MM]
Systems/services affected:
Current status:  [ ] Ongoing  [ ] Contained  [ ] Resolved

IMMEDIATE ACTIONS:
(Brief description of actions taken)

Is the NCSC being separately notified?  [ ] Yes  [ ] No

NEXT UPDATE: [YYYY-MM-DD HH:MM] (within 72 hours of first awareness)
```

### 3.2 CSRB Full Incident Notification (72-Hour)

```
CSRB FULL INCIDENT NOTIFICATION

Submission Date/Time (UTC): [YYYY-MM-DD HH:MM]
Notification Type:  [ ] Initial (72hr)  [ ] Updated  [ ] Final

-- ORGANISATION --
Organisation Name:
Organisation Type:  [ ] OES  [ ] DSP  [ ] MSP  [ ] Data Centre
Competent Authority:
CSRB Lead Contact (Name, Role, Email, Phone):

-- INCIDENT DETAILS --
Date/Time First Detected (UTC): [YYYY-MM-DD HH:MM]
Date/Time Incident Started (if known, UTC): [YYYY-MM-DD HH:MM]
Date/Time Contained/Resolved (if applicable, UTC): [YYYY-MM-DD HH:MM]

Incident Type (select all that apply):
  [ ] Ransomware
  [ ] Data exfiltration
  [ ] Unauthorised access
  [ ] Denial of Service
  [ ] Supply chain compromise
  [ ] Physical attack on systems
  [ ] Insider threat
  [ ] Other:

Systems/Services Affected:
Attack Vector (if known):
Threat Actor Attribution (if known/suspected):

-- IMPACT ASSESSMENT --
Current Status:  [ ] Ongoing  [ ] Contained  [ ] Resolved

Service Impact:
  [ ] No service disruption  [ ] Partial disruption  [ ] Full disruption
Duration of disruption (actual/estimated):
Estimated users/organisations affected:
Geographic scope:
Data exfiltrated or at risk:  [ ] No  [ ] Yes — describe:
Supply chain element involved:  [ ] No  [ ] Yes — describe:
Ransomware component:  [ ] No  [ ] Yes

Near-miss (service not ultimately disrupted):  [ ] No  [ ] Yes
  If yes — what controls/actions prevented service impact:

-- RESPONSE --
Containment measures applied:
External assistance engaged:
  NCSC notified:  [ ] Yes  [ ] No
  Law enforcement notified:  [ ] Yes  [ ] No — which force:
  NCSC IR team engaged:  [ ] Yes  [ ] No

-- CROSS-REGULATORY --
UK GDPR personal data breach requires ICO notification:  [ ] No  [ ] Yes — submitted:
FCA notification required:  [ ] No  [ ] Yes
DSPT / NHS notification required:  [ ] No  [ ] Yes

-- NEXT STEPS --
Planned remediation:
Expected full resolution date:
Next update expected: [YYYY-MM-DD]

Signed: _______________________ Date: ___________
[Name, Role]
```

### 3.3 CSRB Final Report (30-Day Post-Resolution)

```
CSRB FINAL INCIDENT REPORT

Submission Date: [YYYY-MM-DD]
Organisation:
Competent Authority:
Incident Reference (if CA assigned): [CA-REF-XXXX]
Original Early Notification Date: [YYYY-MM-DD]

-- ROOT CAUSE ANALYSIS --
Root cause identified:
  [ ] Unpatched vulnerability (CVE: [____], CVSS: [___])
  [ ] Phishing / social engineering
  [ ] Credential compromise
  [ ] Misconfiguration
  [ ] Supply chain / third-party access
  [ ] Insider threat
  [ ] Unknown / under investigation
  [ ] Other:

Detailed root cause description:

Attack timeline (key events):
  [YYYY-MM-DD HH:MM] —
  [YYYY-MM-DD HH:MM] —
  [YYYY-MM-DD HH:MM] —

-- FINAL IMPACT --
Total duration of any service disruption:
Total users/organisations ultimately affected:
Data confirmed exfiltrated:  [ ] No  [ ] Yes — volume/nature:
Financial impact (if quantifiable):

-- REMEDIATION COMPLETED --
Immediate remediation actions taken:
Longer-term improvements implemented or planned:

-- LESSONS LEARNED --
Control gaps identified:
Improvements to security posture:
Changes to incident response procedures:

-- RECORD KEEPING --
Investigation report retained:  [ ] Yes
Evidence preserved:  [ ] Yes
CA correspondence filed:  [ ] Yes

Signed: _______________________ Date: ___________
[Name, Role — CISO / Compliance Lead]
```

---

## Part 4 — MSP-Specific Incident Reporting

### 4.1 Cascading Incident Scenarios

MSPs face a unique incident reporting challenge: a single compromise of MSP infrastructure may
simultaneously affect multiple client organisations. The CSRB is expected to address this
through:

- **Single notification from MSP** covering all affected clients
- **Client notification obligation** — MSPs must notify affected clients within a defined timeline
- **Joint reporting** — where a client is also OES/DSP, both the MSP and client may need to report

### 4.2 MSP Cascade Notification Process

```
MSP CASCADE INCIDENT NOTIFICATION FLOW

1. MSP detects/is made aware of incident
   |
2. MSP assesses: Are client environments affected or at risk?
   YES --> Proceed
   NO  --> Internal MSP notification only (but still monitor)
   |
3. MSP notifies:
   a) Relevant Competent Authority (for MSP) — within 24 hours
   b) Affected client organisations — within 24 hours
   c) NCSC — as soon as practicable
   |
4. Clients assess impact on their own essential/digital services
   |
5. OES/DSP clients notify their own Competent Authorities if
   CSRB significant impact threshold is met
   |
6. MSP coordinates with clients for joint root cause analysis
   and provides technical assistance
   |
7. MSP submits final report (30 days) to CA
```

### 4.3 MSP Client Notification Template

```
URGENT: CYBER SECURITY INCIDENT NOTIFICATION TO CLIENT

Date/Time: [YYYY-MM-DD HH:MM UTC]
From: [MSP Name] — [Security Contact Name, Role, Email, Phone]
To: [Client Organisation Name] — [Client Security/IT Contact]

NATURE OF NOTIFICATION: [CSRB Mandatory Client Notification]

Dear [Client Contact],

We are writing to notify you of a cyber security incident affecting [MSP NAME]
infrastructure that [has affected / may have affected] your organisation's
systems or data.

INCIDENT SUMMARY:
Date/Time detected: [YYYY-MM-DD HH:MM UTC]
Systems/services affected: [Brief description of affected MSP systems]
Assessment of client impact: [What client data/access may be at risk]
Current status: [ ] Ongoing  [ ] Contained  [ ] Resolved

IMMEDIATE RECOMMENDED ACTIONS FOR YOUR ORGANISATION:
1. [e.g., Rotate credentials for [specific system/service]]
2. [e.g., Review access logs for [date range]]
3. [e.g., Treat emails from [domain] with caution]

Our incident response team is available at: [contact details]
We will provide a further update by: [YYYY-MM-DD HH:MM]

This notification is issued under our obligations under the UK Cyber Security
and Resilience Bill. You may have your own reporting obligations to your
Competent Authority if this incident has significant impact on your essential
or digital service.

[Name, Role, Signature]
[MSP Name]
```

---

## Part 5 — Voluntary Reporting and Information Sharing

### 5.1 NCSC Early Warning Service

The NCSC operates an Early Warning service that allows organisations to voluntarily report
incidents and receive threat intelligence. This is separate from the mandatory CSRB reporting
channel but is strongly encouraged. Organisations should notify NCSC in addition to their
Competent Authority.

NCSC reporting: report.ncsc.gov.uk

### 5.2 Sector Information Sharing

Several sectors operate Information Sharing and Analysis Centres (ISACs) or equivalent bodies
that enable voluntary sharing of threat intelligence and incident information within the sector:

| Sector | Body |
|--------|------|
| Financial services | CISP (NCSC) / FS-ISAC |
| Healthcare | CareCERT (NCSC / NHS Digital) |
| Energy | EUCS (Energy UK) |
| Local government | LGA Cyber / NCSC |
| Telecoms | CiSP / Ofcom |

Participation in sector ISACs supports CSRB compliance goals and is encouraged even before
mandatory reporting obligations take effect.

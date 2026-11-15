# SOC 2 Control Matrix Reference

## Table of Contents
1. [Security - Common Criteria (CC1–CC9)](#security--common-criteria)
2. [Availability (A1)](#availability-a1)
3. [Confidentiality (C1)](#confidentiality-c1)
4. [Processing Integrity (PI1)](#processing-integrity-pi1)
5. [Privacy (P1–P8)](#privacy-p1p8)
6. [Control Statement Template](#control-statement-template)

---

## Security - Common Criteria

### CC1 - Control Environment

| Criterion | What auditors look for | Common gap |
|---|---|---|
| CC1.1 | COSO principles demonstrated; commitment to integrity and ethical values | No code of conduct or ethics policy; leadership not visibly engaged |
| CC1.2 | Board or equivalent oversight of security program | No documented board/executive security oversight; no meeting minutes |
| CC1.3 | Org structure, reporting lines, authorities defined | Org chart not current; security roles undefined |
| CC1.4 | Competent personnel; HR lifecycle controls | No background checks; no security training program |
| CC1.5 | Accountability for security responsibilities | Performance goals don't include security; no enforcement |

**Example control (CC1.4):**
```
Control ID:    CC1.4-001
Title:         Security Awareness Training
Type:          Preventive
Owner:         HR / Security
Frequency:     Annual (+ onboarding)
Description:   All employees complete annual security awareness training covering
               phishing, data handling, and incident reporting. Completion is tracked
               and non-completions escalated to managers.
Evidence:      Training completion report from LMS, onboarding checklist sign-offs
Test:          Inspect training platform report; confirm >95% completion within period;
               sample 5 employees to verify completion dates within 12 months.
```

---

### CC2 - Communication and Information

| Criterion | What auditors look for | Common gap |
|---|---|---|
| CC2.1 | Quality information available to support control objectives | Policies inaccessible or not distributed; no intranet/wiki |
| CC2.2 | Internal communication about security responsibilities | Security updates not communicated; no all-hands or newsletter |
| CC2.3 | External communication with customers, regulators, vendors | No process to notify customers of security incidents; SLA terms vague |

---

### CC3 - Risk Assessment

| Criterion | What auditors look for | Common gap |
|---|---|---|
| CC3.1 | Defined risk objectives; risk tolerance stated | No written risk appetite or tolerance statement |
| CC3.2 | Risk identification and analysis process | No formal risk assessment; informal or ad hoc only |
| CC3.3 | Fraud risk considered | No fraud risk assessment or controls |
| CC3.4 | Technology change risks assessed | Changes don't trigger risk reassessment |

**Example control (CC3.2):**
```
Control ID:    CC3.2-001
Title:         Annual Risk Assessment
Type:          Detective
Owner:         CISO / Security Manager
Frequency:     Annual + event-driven
Description:   A formal risk assessment is performed annually, identifying threats,
               vulnerabilities, and likelihood/impact ratings. A risk register is
               maintained and reviewed quarterly by the security committee.
Evidence:      Risk register (dated), risk assessment report with sign-off,
               security committee meeting minutes
Test:          Inspect risk register; confirm dated within 12 months; verify
               management sign-off; confirm high risks have remediation owners.
```

---

### CC4 - Monitoring Controls

| Criterion | What auditors look for | Common gap |
|---|---|---|
| CC4.1 | Ongoing and separate evaluations of controls | No internal audits; no continuous monitoring program |
| CC4.2 | Deficiencies evaluated and communicated | No deficiency tracking; findings not escalated |

---

### CC5 - Control Activities

| Criterion | What auditors look for | Common gap |
|---|---|---|
| CC5.1 | Controls selected to mitigate risks | Controls not mapped to risks; no controls matrix |
| CC5.2 | Technology controls deployed | No MFA, no endpoint protection, no SIEM |
| CC5.3 | Policies and procedures deployed | Policies exist but not enforced; no procedures for key processes |

---

### CC6 - Logical and Physical Access Controls

This is typically the most heavily tested area.

| Criterion | What auditors look for | Common gap |
|---|---|---|
| CC6.1 | Logical access security measures, including protection of access credentials | No MFA on critical systems; no SSO; shared accounts; passwords stored in plaintext; no PAM for privileged accounts |
| CC6.2 | New access provisioning authorized; access reviewed and removed when no longer needed | No formal access request/approval process; no periodic user access reviews (quarterly/annual) |
| CC6.3 | Role-based access modified or removed on role change or termination; access reviewed periodically | Terminated employees not promptly de-provisioned (>24hr is a flag); no access recertification |
| CC6.4 | Physical access to facilities and protected information assets restricted | No badge/keycard controls; no visitor management; data center access not reviewed |
| CC6.5 | Logical and physical protections over physical assets discontinued only after data can no longer be read or recovered (asset disposal) | No secure disposal/wipe procedures; no certificates of destruction |
| CC6.6 | Logical access restricted from threats | No IDS/IPS; no network segmentation |
| CC6.7 | Data transmission protected | Unencrypted data in transit; no TLS enforcement |
| CC6.8 | Unauthorized software prevented | No application whitelisting or MDM; shadow IT uncontrolled |

**Example control (CC6.3):**
```
Control ID:    CC6.3-001
Title:         Access Termination - Employee Offboarding
Type:          Preventive
Owner:         IT / HR
Frequency:     Event-driven (each termination)
Description:   Upon employee termination, IT disables all system access within 24 hours
               of the HR-initiated offboarding ticket. A checklist confirms: AD account
               disabled, SaaS app access revoked, VPN certificate revoked, hardware
               returned. HR confirms completion in the HRIS.
Evidence:      Offboarding tickets, access revocation logs, HRIS termination records
Test:          Select sample of 10–25 terminations in audit period; verify access was
               revoked within 24 hours using AD logs and ticket timestamps.
```

---

### CC7 - System Operations

| Criterion | What auditors look for | Common gap |
|---|---|---|
| CC7.1 | Vulnerability identification and remediation; malware and configuration-change detection | No vulnerability scanning; no EDR on endpoints; no SLA for patching critical vulns; no patch cadence |
| CC7.2 | Monitoring for security events | No SIEM or log aggregation; alerts not reviewed |
| CC7.3 | Security incidents evaluated and responded to | No incident response plan; incidents not documented |
| CC7.4 | Security incidents contained and resolved | No IR runbook; no post-incident review process |
| CC7.5 | Recovery from identified security incidents | No recovery procedures; no lessons-learned feeding resilience improvements |

---

### CC8 - Change Management

| Criterion | What auditors look for | Common gap |
|---|---|---|
| CC8.1 | Authorized, tested, and approved changes | Changes deployed without tickets or approval; no testing in staging |

**Example control (CC8.1):**
```
Control ID:    CC8.1-001
Title:         Production Change Approval
Type:          Preventive
Owner:         Engineering / DevOps
Frequency:     Event-driven
Description:   All production changes require a change request ticket approved by
               an authorized reviewer (tech lead or manager) before deployment.
               Emergency changes require retroactive approval within 24 hours.
               Changes are tested in staging/QA before production promotion.
Evidence:      Change tickets with approvals, deployment logs, PR approvals in
               version control (GitHub/GitLab), JIRA/Linear ticket history
Test:          Sample 20–30 changes in audit period; verify each has prior
               approval, tester other than developer, and ticket closure with
               deployment confirmation.
```

---

### CC9 - Risk Mitigation

| Criterion | What auditors look for | Common gap |
|---|---|---|
| CC9.1 | Business disruption risk mitigation | No BCP; BCP untested |
| CC9.2 | Vendor and business partner risk managed | No vendor inventory; no vendor assessments performed |

---

## Availability (A1)

| Criterion | What auditors look for | Common gap |
|---|---|---|
| A1.1 | Capacity monitored and managed | No capacity monitoring; no alerting on resource thresholds |
| A1.2 | Environmental threats managed; backups tested | No backup verification; no restore testing |
| A1.3 | Recovery tested; RTO/RPO defined | RTO/RPO not defined; no DR test records |

---

## Confidentiality (C1)

| Criterion | What auditors look for | Common gap |
|---|---|---|
| C1.1 | Confidential information identified and protected | No data classification; no data inventory |
| C1.2 | Confidential information disposed of appropriately | No data retention/disposal policy; no certificate of destruction |

---

## Processing Integrity (PI1)

| Criterion | What auditors look for | Common gap |
|---|---|---|
| PI1.1 | Definitions of data and information specifications maintained to support processing | No data/processing specifications documented |
| PI1.2 | System inputs complete and accurate | No input validation; no authorization checks on inputs |
| PI1.3 | System processing complete, accurate, and timely | No processing reconciliation; no error handling or alerting |
| PI1.4 | System outputs complete and accurate | No output verification or reconciliation |
| PI1.5 | Inputs, items in processing, and outputs stored completely and accurately | No integrity monitoring; no checksums |

---

## Privacy (P1–P8)

| Criterion | What auditors look for | Common gap |
|---|---|---|
| P1 | Privacy notice provided to individuals | No privacy notice; notice doesn't match actual practices |
| P2 | Choice and consent obtained | No consent mechanism; opt-out not honored |
| P3 | Personal information collected only as stated | Collecting more data than disclosed; no data minimization |
| P4 | Personal information used only as stated | Using PII for undisclosed purposes |
| P5 | Personal information retained and disposed per policy | No retention schedule; PII kept indefinitely |
| P6 | Personal information disclosed only as authorized | No data sharing agreements; unauthorized third-party access |
| P7 | Personal information quality maintained | No process to update/correct inaccurate data |
| P8 | Privacy complaints and inquiries handled | No DSR (Data Subject Request) process; no privacy contact |

---

## Control Statement Template

```
Control ID:    [TSC-criterion-sequence, e.g., CC6.1-002]
TSC Criterion: [e.g., CC6.1 – Logical Access Security Measures]
Control Title: [Short descriptive name]
Control Type:  [Preventive | Detective | Corrective]
Control Owner: [Role/team]
Frequency:     [Continuous | Daily | Weekly | Monthly | Quarterly | Annual | Event-driven]
Description:   [What the control does, who performs it, how it works, and what
               systems/processes are covered. 2–5 sentences.]
Evidence:      [Artifacts produced by this control that prove it operates:
               logs, reports, tickets, sign-offs, screenshots, exports.]
Test Procedure:[How an auditor would test this: sample size, data sources,
               pass/fail criteria. Match Type 1 (design) vs Type 2 (operating).]
Related Policies: [Which policy governs this control]
Linked Risks:  [Which risks from risk register this control mitigates]
```

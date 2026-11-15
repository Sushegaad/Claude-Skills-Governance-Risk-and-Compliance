# SOC 2 Audit Evidence Reference

## Table of Contents
1. [Evidence Fundamentals](#evidence-fundamentals)
2. [Evidence by Criterion](#evidence-by-criterion)
3. [Evidence Quality Checklist](#evidence-quality-checklist)
4. [Common Evidence Pitfalls](#common-evidence-pitfalls)

---

## Evidence Fundamentals

### Type 1 vs Type 2 Evidence

| | Type 1 | Type 2 |
|---|---|---|
| **What's tested** | Control design at a point in time | Control operating effectiveness over a period |
| **Evidence needed** | Proof control *exists* and is *designed* correctly | Proof control *operated consistently* throughout the period |
| **Sampling** | Single instance is usually sufficient | Auditor will sample multiple instances across the period |
| **Typical audit period** | A date (e.g., Dec 31, 2024) | 6–12 months (e.g., Jan 1 – Dec 31, 2024) |

For Type 2, auditors typically use **statistical sampling** - for higher-frequency controls (daily logs, weekly scans), they'll pull samples from across the period. For lower-frequency controls (annual risk assessment, quarterly access reviews), they'll test every instance.

### Sampling Guidance by Control Frequency

| Frequency | Auditor sample size (typical) |
|---|---|
| Continuous / daily | 20–30 items from across the period |
| Weekly | 5–10 weeks sampled |
| Monthly | 3–6 months sampled |
| Quarterly | All 4 quarters |
| Annual | 1 (but must cover the audit period) |
| Event-driven (e.g., per hire/termination) | 20–30 events or 100% if fewer than 20 |

---

## Evidence by Criterion

### CC1 - Control Environment

| Evidence Item | What it proves | Format |
|---|---|---|
| Organizational chart (current) | Org structure and reporting lines | PDF / org tool export |
| Code of Conduct / Ethics policy | Commitment to integrity | Signed policy doc |
| Security awareness training completion report | CC1.4 - competent personnel | LMS export with timestamps |
| Board/executive security meeting minutes | Leadership oversight | Meeting minutes PDF |
| Background check records | CC1.4 - personnel screening | HRIS confirmation (redacted) |
| Security committee charter | Governance structure | Document |

---

### CC2 - Communication and Information

| Evidence Item | What it proves | Format |
|---|---|---|
| Policy distribution records | Policies communicated to employees | Email screenshots, intranet access logs |
| Employee policy acknowledgment log | Personnel aware of requirements | Signed acknowledgments or LMS completion |
| Customer-facing security communications (e.g., SLA, security page) | External communication | URL / screenshot with date |
| Incident notification records (if any occurred) | CC2.3 - external notification process | Email/ticket records |

---

### CC3 - Risk Assessment

| Evidence Item | What it proves | Format |
|---|---|---|
| Risk register (dated, with owners) | Risks identified and tracked | Spreadsheet / GRC tool export |
| Risk assessment report with management sign-off | Formal annual process completed | PDF with signatures and date |
| Security committee meeting minutes (risk review) | Ongoing risk oversight | Minutes |
| Risk treatment decisions (accept/mitigate/transfer) | Risks actively managed | Risk register or separate log |

---

### CC4 - Monitoring Controls

| Evidence Item | What it proves | Format |
|---|---|---|
| Internal audit reports | Self-evaluation of controls | Audit report PDF |
| Control deficiency log / tracking | Deficiencies identified and remediated | Spreadsheet or ticket system |
| Executive/board security reporting | Control performance communicated upward | Dashboard screenshots, board slides |

---

### CC5 - Control Activities

| Evidence Item | What it proves | Format |
|---|---|---|
| Controls matrix (policies mapped to risks) | Controls selected to address risks | Spreadsheet |
| MFA enrollment reports | Technology controls deployed | Okta/Azure AD report |
| Endpoint protection deployment report | CC5.2 - technology controls | MDM / EDR console export |
| Firewall rule review records | Network controls reviewed | Firewall config review document |

---

### CC6 - Logical and Physical Access Controls

This criterion typically generates the most evidence requests.

| Evidence Item | What it proves | Format |
|---|---|---|
| User access list (production systems, AWS, GitHub, SaaS) | Current state of access | Console exports |
| Access request/approval tickets | CC6.2 - provisioning authorized | JIRA / ServiceNow tickets |
| Termination access revocation records | CC6.3 - timely de-provisioning | HR ticket + AD/system logs |
| Access review sign-offs (quarterly/annual) | CC6.2, CC6.3 - reviews performed | Spreadsheet with reviewer signature and date |
| MFA configuration screenshots | CC6.1 - credentials protected | Admin console screenshots |
| Privileged access list and reviews | CC6.1, CC6.2, CC6.3 - admin access controlled and reviewed | Export with review sign-off |
| Encryption-in-transit configuration | CC6.7 - data protected | SSL cert details, config screenshots |
| Physical access records (if applicable) | CC6.4 - physical access restricted | Keycard logs, visitor logs, office photos |
| Asset disposal / media destruction records | CC6.5 - disposal after data unrecoverable | Certificates of destruction, wipe logs |

**Access review evidence tips:**
- Export must be dated and show reviewer name
- Bulk "no change" reviews are a flag - show evidence of actual review decisions
- Entitlement changes made as a result of review should be evidenced (tickets)

---

### CC7 - System Operations

| Evidence Item | What it proves | Format |
|---|---|---|
| Vulnerability scan reports (quarterly or more frequent) | CC7.1 - vulnerabilities detected | Scan tool export (Qualys, Tenable, etc.) |
| Penetration test report + remediation tracking | CC7.1 - testing performed | Pentest report PDF + remediation tickets |
| SIEM alerts / security event dashboard | CC7.2 - monitoring in place | Dashboard screenshot (dated) |
| Incident tickets (all incidents in period) | CC7.3, CC7.4 - incidents managed | Ticket system export |
| Incident post-mortems / lessons learned | CC7.4 - resolution documented | Post-mortem documents |
| Patch management reports (before/after) | CC7.1 - vulnerabilities remediated | Patch report with dates |
| Incident recovery records (restoration, post-incident verification) | CC7.5 - recovery from incidents | Recovery runbook outputs, restoration tickets |
| IR tabletop exercise records | CC7.3 - IR plan tested | Exercise agenda, attendance, findings |
| Antivirus/EDR status reports | CC7.1 - malware detection | Console export |

---

### CC8 - Change Management

| Evidence Item | What it proves | Format |
|---|---|---|
| Change tickets with approvals (sample across period) | Changes authorized before deployment | JIRA / Linear / ServiceNow tickets |
| PR/merge request approvals in version control | Code review and approval | GitHub/GitLab PR screenshots |
| Deployment logs | Changes deployed as approved | CI/CD pipeline logs |
| Change advisory board (CAB) meeting minutes | High-risk changes reviewed | Meeting notes |
| Emergency change approvals and retroactive sign-offs | Emergency process followed | Ticket records |

---

### CC9 - Vendor Risk

| Evidence Item | What it proves | Format |
|---|---|---|
| Vendor inventory (tiered) | All vendors identified | Spreadsheet |
| Vendor SOC 2 reports (reviewed) | Critical vendors assessed | SOC 2 report copies + review log |
| Vendor security questionnaire responses | Due diligence performed | Questionnaire responses |
| Vendor contracts with security clauses / DPA | Contractual controls in place | Contract excerpts |
| CUEC (Complementary User Entity Controls) tracking | CUECs from vendor SOC 2 reports addressed | Mapping document |

---

### A1 - Availability

| Evidence Item | What it proves | Format |
|---|---|---|
| Uptime monitoring dashboards / SLA reports | System availability tracked | Monitoring tool export (e.g., Datadog, Pingdom) |
| Capacity monitoring alerts | A1.1 - capacity managed | Dashboard screenshots |
| Backup completion logs (all backups in period) | Backups running as configured | Backup tool reports |
| Backup restore test records | A1.2 - backups verified | Test procedure + results document |
| DR test plan and results | A1.3 - recovery tested | DR test report with date and RTO/RPO achieved |
| Incident tickets for outages | Availability events documented | Ticket records |

---

### C1 - Confidentiality

| Evidence Item | What it proves | Format |
|---|---|---|
| Data inventory / data map | Confidential data identified | Data inventory spreadsheet |
| Data classification labels applied | C1.1 - classification in practice | Screenshots, DLP reports |
| DLP (Data Loss Prevention) reports | Confidential data protected | DLP console export |
| Data disposal/destruction records | C1.2 - disposal per policy | Certificate of destruction, deletion logs |
| NDA log (employees, vendors) | Confidentiality agreements in place | NDA execution records |

---

### PI1 - Processing Integrity

| Evidence Item | What it proves | Format |
|---|---|---|
| Data and processing specification documents | PI1.1 - specifications defined | Data dictionaries, processing specs |
| Input validation test records | PI1.2 - inputs complete and accurate | Test results, code review records |
| Reconciliation reports | PI1.4 - outputs complete and accurate | Reconciliation logs |
| Error log reviews | PI1.3 - processing errors detected and handled | Error monitoring reports |
| Data integrity monitoring alerts | PI1.5 - stored inputs, in-process items, and outputs protected | Monitoring screenshots |
| Job/batch processing success logs | PI1.3 - processing complete, accurate, timely | Scheduler/job logs |

---

### P1–P8 - Privacy

| Evidence Item | What it proves | Format |
|---|---|---|
| Privacy notice (published, dated) | P1 - notice provided | URL / PDF |
| Consent mechanism screenshots | P2 - consent obtained | UI screenshots, consent logs |
| Data subject request (DSR) log | P8 - requests handled | DSR ticket log |
| DSR response records (sample) | P8 - timely response | Ticket records with dates |
| Data retention schedule | P5 - retention defined | Retention policy + schedule |
| Data deletion records | P5 - data disposed per policy | Deletion logs |
| Privacy impact assessments (PIA) | P3, P4 - collection/use reviewed | PIA documents |
| Third-party data sharing agreements | P6 - sharing authorized | DPA / data sharing contracts |

---

## Evidence Quality Checklist

Before submitting evidence to auditors, verify:

- [ ] **Dated** - every screenshot or export clearly shows the date it was captured
- [ ] **System-identified** - it's clear which system the evidence comes from
- [ ] **Complete for period** - Type 2 evidence covers the full audit window
- [ ] **Not reconstructed** - evidence was captured at the time of control operation, not created retroactively
- [ ] **Reviewer-attributable** - approvals show who approved (not just "admin" or a shared account)
- [ ] **Named with context** - files are named clearly (e.g., `CC6.5_AccessReview_Q3-2024_Signed.pdf`, not `screenshot1.png`)
- [ ] **Organized by criterion** - evidence folder mirrors the TSC structure

---

## Common Evidence Pitfalls

1. **Screenshots with no date** - always capture the date/timestamp in the screenshot or use system-generated exports with metadata.

2. **"As of today" exports provided after the audit period** - access lists pulled after the fact don't prove controls operated *during* the period. Configure periodic automated exports.

3. **Approval from the same person who made the change** - self-approval violates separation of duties. Flag this for remediation before the audit.

4. **Shared or service accounts used for approvals** - individual accountability cannot be established. Require personal accounts for all approvals.

5. **Training completion reports showing < 100%** - auditors will ask about non-completers. Have a policy and evidence showing follow-up for late completers.

6. **Incomplete incident tickets** - tickets must show: detection time, severity classification, responders, containment actions, resolution, and closure. Sparse tickets are a finding.

7. **Vendor SOC 2 reports not reviewed** - simply *having* a vendor's SOC 2 report is insufficient. Show evidence it was reviewed (e.g., review memo, CUEC tracking).

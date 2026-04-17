# ISO/IEC 27018 — PII Protection Implementation Guidance

## Purpose

This reference provides practical implementation guidance for cloud service providers (CSPs) seeking to comply with ISO/IEC 27018. It covers technical safeguards, organisational measures, staff provisions, sub-processor management, and operational controls.

---

## 1. Technical Safeguards for PII in Cloud Environments

### 1.1 Encryption

**At rest:**
- All PII stored in cloud infrastructure must be encrypted using current strong algorithms (AES-256 or equivalent)
- Database-level, file-system-level, or object-level encryption is acceptable; key management must be documented
- Customer-managed encryption keys (CMEK) should be offered as an option, giving customers control over their own data confidentiality
- Key rotation policies must be documented and enforced

**In transit:**
- All network transmission of PII must use TLS 1.2 or higher (TLS 1.3 preferred)
- Internal service-to-service communications carrying PII must also use encrypted channels
- Deprecated protocols (SSL, TLS 1.0, TLS 1.1) must be disabled
- Certificate management processes must be documented

**Key management:**
- Encryption keys must be managed separately from the data they protect
- Key access must be controlled with the same rigour as access to PII itself
- Key escrow or recovery procedures must be documented to prevent data loss in the event of key loss

---

### 1.2 Access Control for PII Systems

**Least privilege principle:**
- Every user, service account, and automated process must have the minimum permissions required for their function
- PII data stores must not be accessible by default; access must be explicitly provisioned
- Database admin access must be separate from application access; both must be separately logged

**Identity and authentication:**
- Multi-factor authentication (MFA) is required for all accounts with access to production PII
- Service accounts should use workload identity federation or short-lived credentials instead of long-lived passwords
- Shared accounts must not have access to PII

**Access reviews:**
- All access rights to PII systems must be reviewed at minimum every 6 months (quarterly for privileged access)
- Reviews must result in documented revocations where access is no longer required
- Access review records must be retained for at least 2 years

**Privileged access management:**
- Break-glass or emergency access procedures must be documented and require post-use review
- Just-in-time (JIT) privileged access is the preferred model for production PII environments
- All privileged access sessions in PII environments must be logged (session recording where technically feasible)

---

### 1.3 Logging and Monitoring

**Access logs:**
- All access to PII storage (read, write, delete, update) must be logged
- Logs must include: timestamp, user/service identity, action performed, data object identifier (not PII content)
- Logs must be protected from tampering and stored separately from the systems they monitor
- Log retention minimum: 12 months (extend to 24–36 months where regulation requires)

**Anomaly detection:**
- Automated alerting for: large-scale data exports, unusual access patterns, access outside business hours, failed access attempts
- Security Information and Event Management (SIEM) or equivalent monitoring must cover PII-handling systems
- Alerts resulting in investigation must be documented with outcome

**Audit trail:**
- An end-to-end audit trail must enable reconstruction of PII access events for any given time period
- Audit trails must be available to cloud service customers on request (in a form that does not expose other customers' data)

---

### 1.4 Data Minimization and Retention

**Collection minimization:**
- The CSP's service must not collect more PII from customers than is required to deliver the service
- Log collection in particular must be reviewed to ensure PII does not inadvertently appear in operational logs
- Data minimization must be considered at the design stage for new features (privacy by design)

**Retention and deletion:**
- Retention periods for all categories of PII must be documented and enforced
- Automated deletion processes must be in place where PII exceeds defined retention limits
- Deletion must propagate through all tiers: primary storage, backups, caches, replicas, sub-processors
- For cloud customers' PII, deletion on customer instruction must be technically possible and complete within an agreed timeframe

**Temporary file management:**
- Processes that create temporary files, buffers, or intermediate copies containing PII must be documented
- Temporary PII must be classified as PII and subject to the same access controls as primary PII
- Automated deletion of temporary PII must occur as soon as the operational need expires
- Debugging, diagnostic, and log files must be screened to prevent inadvertent PII retention

---

### 1.5 Data Residency Controls

**Technical enforcement of residency:**
- Where data residency commitments are made to customers, technical controls must enforce them (data cannot be processed outside committed regions)
- Regional routing, geofencing, and data localisation features must be demonstrated and auditable
- Regional failover or replication must not silently break residency commitments

**Residency verification:**
- Customers should be able to verify the region(s) in which their PII is processed (e.g. through admin console, API, or documentation)
- Changes to data residency must be notified in advance with opportunity for customers to object or migrate data

---

## 2. Organisational Measures

### 2.1 PII Protection Roles

**Minimum required roles:**

| Role | Responsibility |
|------|---------------|
| **Data Protection Contact / DPO** | Primary point of contact for PII matters; receives regulatory enquiries; accessible to cloud service customers |
| **Cloud Privacy Lead / Privacy Counsel** | Owns PII policy framework; advises on contractual obligations; manages regulatory relationships |
| **Security Operations** | Implements and monitors technical controls for PII protection; manages incidents |
| **Procurement / Vendor Management** | Manages sub-processor due diligence and contracts |
| **Customer Success / Legal** | Handles customer DPA queries, data subject rights escalations, and customer audit requests |

**RACI for key ISO 27018 processes:**

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Sub-processor assessment | Procurement | Privacy Lead | Legal, Security | Customers (via schedule) |
| Government request handling | Legal | DPO/Privacy Lead | CISO | Customer (where permitted) |
| PII incident notification | Security Ops | CISO | Legal, DPO | Customer, Regulator |
| Customer audit support | Customer Success | Privacy Lead | Security, Legal | Auditor/Customer |
| PII return/deletion at contract end | Engineering | Privacy Lead | Legal | Customer |

---

### 2.2 Staff Training and Awareness

**Required training elements for staff with access to PII:**
1. What constitutes PII under ISO 27018 and applicable law
2. The CSP's obligations as a PII processor (no secondary use, no commercial use)
3. How to handle customer PII access requests and data subject rights escalations
4. The CSP's government/law enforcement request handling procedure
5. Confidentiality obligations and consequences of breach
6. How to recognise and report a PII-related security incident

**Training delivery:**
- Mandatory for all R&D, engineering, operations, customer support, and management staff with potential PII access
- New hire training must be completed before access is provisioned
- Annual refresher training for all in-scope staff
- Additional role-specific training for staff in DBA, cloud operations, and customer success roles

**Evidence requirements:**
- Training completion records (name, date, course, signature or system confirmation)
- Competency assessment records where role-specific training includes assessment
- Acknowledgment of confidentiality obligations

---

### 2.3 Confidentiality Obligations for Staff

All staff and contractors with access to customer PII must:
- Sign a confidentiality agreement or non-disclosure undertaking covering PII
- Acknowledge that they must not use customer PII for any purpose other than delivering the contracted service
- Acknowledge penalties for breach (employment disciplinary process; potential civil/criminal liability)

The confidentiality obligation must:
- Survive the end of the employment or contractor relationship
- Explicitly cover PII and not simply refer to general business confidentiality
- Be documented and retained in personnel records

---

### 2.4 Incident and Breach Management

**PII-specific incident classification:**

| Severity | Definition | Customer Notification |
|----------|------------|----------------------|
| Critical | Confirmed unauthorised access to or exfiltration of PII | Within 24 hours of confirmation |
| High | Suspected PII breach; containment incomplete | Within 48 hours of awareness |
| Medium | PII security event with low impact; contained | Within 72 hours; or per contract |
| Low | Incident with no PII exposure confirmed | As part of periodic security reporting |

**Notification contents (minimum):**
- Nature and description of the incident
- Categories of PII affected (e.g. names, email addresses, health data)
- Approximate number/volume of PII principals affected
- Likely consequences of the breach
- Measures taken or proposed to address the breach and mitigate its effects
- Name and contact details of the DPO or designated contact for further information

**Post-incident obligations:**
- Customers must be supported in completing their own regulatory notification requirements
- Full incident report provided to customers within a defined timeframe (commonly 30 days)
- Lessons learned review must be completed and documented
- Corrective action plan must be communicated to affected customers

---

## 3. Sub-processor Management

### 3.1 Sub-processor Selection and Approval

**Due diligence requirements before onboarding a new sub-processor:**
- Confirm the sub-processor can meet ISO 27018 equivalent obligations
- Review the sub-processor's data protection certifications, audit reports, or questionnaire responses
- Assess the sub-processor's breach notification capability and track record
- Confirm the sub-processor has a documented DPO or privacy contact
- Evaluate the sub-processor's data residency capabilities against customer commitments

**Approval process:**
- Documented business justification for using the sub-processor
- Security and legal sign-off before onboarding
- Record in sub-processor register before first PII processing commences
- Customer notification per contractual requirement (typically 30 days in advance for new sub-processors)

---

### 3.2 Sub-processor Agreements — Required Contract Terms

All sub-processor agreements must include:

| Term | Requirement |
|------|-------------|
| **Purpose limitation** | Sub-processor may only process PII for the purposes specified in the agreement; no commercial use or secondary processing |
| **No further sub-processing** | Sub-processor may not engage additional sub-processors without prior written approval from the CSP |
| **Security standards** | Sub-processor must implement security measures equivalent to or exceeding the CSP's obligations under ISO 27018 |
| **Breach notification** | Sub-processor must notify CSP of any PII incident within 24 hours of discovery |
| **Return and deletion** | Sub-processor must return or delete all PII at end of service; written confirmation required |
| **Audit rights** | CSP must have the right to audit the sub-processor or receive third-party audit reports |
| **Data residency** | Sub-processor must process PII only in agreed locations; changes require advance approval |
| **Regulatory compliance** | Sub-processor must comply with applicable data protection laws |
| **Liability** | Sub-processor remains liable to CSP for breach of agreement terms |
| **Survival** | Confidentiality and data deletion obligations survive termination of the agreement |

---

### 3.3 Ongoing Sub-processor Monitoring

- Annual review of sub-processor certifications and audit reports (or following significant incidents)
- Track the sub-processor register for any changes in sub-processor status (acquisition, certification lapse, regulatory sanction)
- Periodically verify that sub-processors are processing PII only in approved locations
- Conduct periodic re-assessment for high-risk sub-processors (those with access to large volumes of sensitive PII)

---

### 3.4 Sub-processor Register — Required Fields

| Field | Description |
|-------|-------------|
| Sub-processor name | Legal entity name |
| Registered country | Country of incorporation |
| Data processing location(s) | Countries/regions where PII is actually processed |
| Purpose | Specific function performed on behalf of CSP |
| Categories of PII processed | Types of PII shared with this sub-processor |
| Legal transfer mechanism | If outside EEA/UK: SCCs, adequacy, BCRs, etc. |
| Certification / audit report | Current certification or most recent audit reference |
| Customer notification date | Date customers were notified of this sub-processor |
| Contract reference | Internal reference to the sub-processor agreement |
| Review date | Date of last due diligence review |

---

## 4. Government and Law Enforcement Request Handling

### 4.1 Receiving a Request

When a government authority, law enforcement agency, or court issues a request for customer PII, the CSP shall:

1. **Log the request immediately** — record receipt date, requesting authority, nature of request, PII categories requested, deadline
2. **Legal review** — route to Legal immediately; assess whether the request is legally valid, properly authorised, and limited in scope
3. **Do not disclose prematurely** — no PII shall be disclosed until legal review is complete (unless imminent harm prevents delay)
4. **Challenge if appropriate** — if the request is overbroad, lacks proper legal basis, or conflicts with the CSP's legal obligations to customers, the CSP shall challenge the request

### 4.2 Customer Notification

Unless legally prohibited (e.g. by a court order, national security direction, or law prohibiting notification):
- Notify the affected cloud service customer promptly — within 24–48 hours of receiving the request
- Notification must include: requesting authority, nature of request, data categories requested
- If prohibited from notifying: record the prohibition in the disclosure register; publish aggregate transparency data where permitted

### 4.3 Disclosure and Recording

If disclosure is required after legal review:
- Disclose only the minimum PII necessary to satisfy the legal obligation
- Record the disclosure fully in the disclosure register
- Provide written record to the customer (post-prohibition if applicable)
- Note in transparency report (in aggregate form) for future publication

### 4.4 Transparency Reporting

The CSP shall publish an aggregate transparency report covering:
- Total number of government/law enforcement requests received in the reporting period
- Jurisdictions of requesting authorities (where disclosable)
- Number of requests fulfilled in full, in part, or rejected
- Number of requests where customer notification was legally prohibited

---

## 5. Privacy by Design in Cloud Service Development

When developing new features, services, or processing capabilities that involve PII:

**Privacy by Design principles to apply:**

1. **Proactive not reactive** — anticipate PII risks before development; privacy requirements included in design specifications
2. **Privacy as default** — services must default to maximum privacy settings; customers must opt into less protective configurations, not opt out of more protective ones
3. **Privacy embedded into design** — PII protection is embedded into architecture, not bolted on post-development
4. **Full functionality** — privacy and security are not treated as trade-offs; both must be achieved
5. **End-to-end security** — PII is protected throughout its full lifecycle in the service
6. **Visibility and transparency** — documentation of how PII is processed must be accessible to customers
7. **Respect for users** — customer and PII principal interests are kept central to design decisions

**Privacy impact assessment (PIA):**
- A PIA should be conducted before launching new processing activities involving PII
- PIA should assess: what PII is processed, for what purpose, the risk to PII principals, and proposed mitigations
- ISO/IEC 29134 provides guidance on PIAs in the cloud context

---

## 6. Compliance Verification and Evidence Management

### 6.1 Internal Audit

The CSP should conduct periodic internal audits of its ISO 27018 compliance:
- Minimum frequency: annually; more frequently where high volumes of sensitive PII are processed
- Audit scope: all Annex A control areas; sample testing of key obligations (sub-processor contracts, access logs, notification records)
- Audit findings must be tracked to remediation with documented closure

### 6.2 Customer Audit Rights

Customers have the right under ISO 27018 to verify compliance. The CSP should prepare:

**Tier 1 — Always available:**
- Current ISO 27018-aligned certifications (e.g. ISO 27001, SOC 2 with privacy criteria)
- Security whitepaper covering PII protection measures
- Sub-processor register (current version)
- Summary of government request handling procedures

**Tier 2 — Available on request under NDA:**
- Most recent third-party security audit report
- Penetration test summaries (redacted)
- Internal audit summary (last completed)

**Tier 3 — Negotiable for high-risk / high-volume customers:**
- Direct audit access (on-site or remote) with reasonable notice (typically 30–60 days)
- Completion of customer security questionnaires (CSA CAIQ, SIG, etc.)
- Independent third-party audit commissioned by customer (costs typically to customer; CSP cooperation required)

### 6.3 Evidence Retention

All compliance evidence must be retained for a minimum of:
- **3 years** for operational records (access logs, training records, notification records)
- **Length of contract + 3 years** for customer-specific records (DPAs, sub-processor notifications, disposal confirmations)
- **6–10 years** for legal/regulatory records (court orders, disclosure register entries) — confirm per jurisdiction

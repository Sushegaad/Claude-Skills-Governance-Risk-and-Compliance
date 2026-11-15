# SOC 2 Policy Writing Reference

## Table of Contents
1. [Policy Writing Standards](#policy-writing-standards)
2. [Required Policy Set](#required-policy-set)
3. [Policy Templates](#policy-templates)
4. [Common Mistakes to Avoid](#common-mistakes-to-avoid)

---

## Policy Writing Standards

### Universal Policy Header

Every policy should start with:

```
Policy Title:     [Name]
Policy ID:        [e.g., ISP-001]
Version:          [e.g., 1.2]
Effective Date:   [Date]
Last Reviewed:    [Date]
Next Review Date: [Date - maximum 12 months from last review]
Policy Owner:     [Role]
Approved By:      [Executive/leadership role + name]
TSC Criteria:     [e.g., CC1.1, CC2.1, CC5.3]
```

### Required Sections (every policy)

1. **Purpose** - Why this policy exists; what it protects
2. **Scope** - Who and what systems it applies to (be explicit)
3. **Policy Statements** - The actual rules (use "must", not "should")
4. **Roles and Responsibilities** - Who enforces it, who complies
5. **Exceptions** - How to request an exception; who approves
6. **Enforcement** - Consequences of non-compliance
7. **Related Documents** - Links to procedures, standards, other policies
8. **Review and Revision History** - Version log

### Language Standards

| Weak (avoid) | Strong (use) |
|---|---|
| should, may, could | must, shall, is required to |
| as appropriate | [specific action] |
| where possible | [specific action or explicit exception process] |
| periodically | [specific frequency: quarterly, annually] |
| sensitive data | [defined data classification tier] |
| promptly | within [X] hours/days |

---

## Required Policy Set

### 1. Information Security Policy (ISP)
**Criteria:** CC1.1, CC1.2, CC2.1, CC5.1, CC5.3  
**Purpose:** Overarching policy establishing management's commitment to security  
**Must include:**
- Executive statement of commitment
- Security objectives aligned to business
- Reference to all subordinate security policies
- Defined security roles (CISO, security committee, data owners, users)
- Annual review requirement

---

### 2. Access Control Policy
**Criteria:** CC6.1, CC6.2, CC6.3, CC6.6 (physical access restriction is CC6.4 and secure asset disposal is CC6.5 - cover those in a physical security policy and the data classification/disposal requirements below)  
**Must include:**
- Principles: least privilege, need-to-know, separation of duties
- MFA requirements (which systems require it - be specific)
- Provisioning process: how access is requested, approved, granted
- Termination process: timeline for de-provisioning (e.g., within 24 hours)
- Privileged access: how admin/root access is controlled and reviewed
- Access review cadence (e.g., quarterly for privileged, annual for standard)
- Password/authentication standards (or reference to auth policy)

---

### 3. Incident Response Policy
**Criteria:** CC7.3, CC7.4, CC7.5, CC2.3  
**Must include:**
- Incident classification levels (with examples: P1–P4 or Critical/High/Medium/Low)
- Roles: Incident Commander, responders, communications lead
- Detection and reporting process (how incidents are identified and escalated)
- Response phases: Identify → Contain → Eradicate → Recover → Lessons Learned
- Customer notification SLA (e.g., material breaches within 72 hours)
- Post-incident review requirement
- Annual IR tabletop exercise requirement

**Template snippet:**
```
4. Incident Classification

Severity 1 (Critical): Confirmed breach of customer data, ransomware, complete
  system outage. Requires immediate escalation to CEO and CISO. Customer
  notification within 72 hours if PII involved.

Severity 2 (High): Suspected breach, significant service degradation >30 min,
  compromised admin credentials. Requires CISO notification within 2 hours.

Severity 3 (Medium): Isolated malware, failed intrusion attempt, minor outage.
  Requires Security team response within 4 hours.

Severity 4 (Low): Security policy violations, phishing attempts (no compromise),
  suspicious activity (unconfirmed). Requires ticket within 24 hours.
```

---

### 4. Change Management Policy
**Criteria:** CC8.1  
**Must include:**
- Scope: what constitutes a "change" (code, infrastructure, configurations)
- Change types: standard (pre-approved), normal (requires review), emergency
- Approval requirements by change type
- Testing requirements (staging/QA before production)
- Rollback requirements: every change must have a documented rollback plan
- Emergency change: allowed with retroactive approval within 24 hours
- Change freeze periods (optional but common)

---

### 5. Risk Assessment Policy
**Criteria:** CC3.1, CC3.2, CC3.3, CC3.4  
**Must include:**
- Frequency: at minimum annual, plus triggered by significant changes
- Risk scoring methodology (likelihood × impact matrix)
- Risk tolerance/appetite statement
- Risk register: ownership, format, review cadence
- Treatment options: accept, mitigate, transfer, avoid
- Escalation: who reviews and approves risk acceptance

---

### 6. Vendor Management Policy
**Criteria:** CC9.2  
**Must include:**
- Vendor tiering criteria (Critical / High / Medium / Low)
- Due diligence requirements per tier (SOC 2 report, questionnaire, etc.)
- Contractual requirements: DPA, security addendum, right-to-audit
- Ongoing monitoring: annual review schedule
- Offboarding: data deletion requirements, access revocation
- Subprocessor disclosure for customer-facing vendors

---

### 7. Business Continuity & Disaster Recovery Policy
**Criteria:** A1.2, A1.3, CC9.1  
**Must include:**
- RTO (Recovery Time Objective) and RPO (Recovery Point Objective) per system
- Backup frequency, retention, and verification requirements
- DR environment description (hot/warm/cold standby)
- DR test requirement: at minimum annual tabletop or failover test
- BCP activation criteria and escalation path
- Communication plan during an incident

---

### 8. Data Classification Policy
**Criteria:** C1.1, C1.2, P3, CC6.5, CC6.7  
**Must include:**
- Classification tiers (example: Public / Internal / Confidential / Restricted)
- Definition of each tier with examples
- Handling requirements per tier (storage, transmission, sharing, disposal)
- Labeling requirements
- Default classification (unclassified data = treated as what tier?)

**Template tiers:**
```
Restricted:   PII, PHI, payment card data, credentials, encryption keys.
              Encrypted at rest and in transit. Access strictly limited.
              Cannot be stored in personal devices or unapproved cloud services.

Confidential: Business-sensitive data, source code, audit reports, contracts.
              Encrypted in transit. Access on need-to-know basis. NDA required
              for external sharing.

Internal:     Internal communications, non-sensitive operational data.
              Not for public distribution. Standard access controls apply.

Public:       Marketing materials, published docs, press releases.
              No special controls required.
```

---

### 9. Acceptable Use Policy
**Criteria:** CC1.1, CC6.6, CC6.8  
**Must include:**
- Acceptable use of company systems, networks, and data
- Prohibited activities (explicit list)
- Personal device / BYOD rules
- Monitoring disclosure ("Company may monitor use of systems")
- Reporting obligations for suspected incidents
- Acknowledgment requirement (signed annually)

---

### 10. Privacy Policy / Notice
**Criteria:** P1, P2, P3, P6, P8  
**Must include (per AICPA GAPP):**
- What personal information is collected and why
- Legal basis for processing (if GDPR-applicable)
- How information is used
- With whom it is shared (third parties, subprocessors)
- Retention periods
- Individual rights (access, correction, deletion, portability)
- How to submit a data subject request
- Contact information for privacy inquiries
- How policy changes are communicated

---

### 11. Encryption Policy
**Criteria:** CC6.7, C1.1  
**Must include:**
- Encryption standards (e.g., AES-256 at rest, TLS 1.2+ in transit)
- Which systems and data require encryption
- Key management: generation, rotation, storage, destruction
- Prohibition on deprecated algorithms (MD5, SHA-1, DES, RC4)

---

### 12. Vulnerability Management Policy
**Criteria:** CC7.1  
**Must include:**
- Scanning frequency (e.g., weekly automated + quarterly penetration test)
- Severity-based remediation SLAs:
  - Critical: patch within 24–72 hours
  - High: patch within 7–14 days
  - Medium: patch within 30 days
  - Low: patch within 90 days or accepted risk
- Exception process for systems that can't be patched immediately
- Penetration testing requirement (annual minimum)
- Responsible disclosure / bug bounty program (optional)

---

## Common Mistakes to Avoid

1. **Writing policies that describe the ideal, not the actual** - auditors test what you do, not what you aspirationally wrote. Only commit to what you'll consistently do.

2. **No approval signatures** - policies must be formally approved by an appropriate executive or the board.

3. **Copy-paste from the internet** - boilerplate policies often contain controls you don't have. Every control stated must be evidenced.

4. **Missing scope statements** - "this policy applies to all employees" may be incomplete if contractors, vendors, or specific systems need to be called out.

5. **Not distributing policies** - policies must be accessible to all in-scope personnel. Distribution evidence is required (e.g., intranet link, email announcement, acknowledgment log).

6. **Neglecting annual review** - dated policies are a flag. Every policy must have a documented review with any changes noted.

7. **Procedures missing from policies** - policies state *what* and *why*; procedures state *how*. Both are needed. "We will respond to incidents" without a runbook is a gap.

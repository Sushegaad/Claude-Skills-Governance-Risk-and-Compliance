# Reporting Templates — NIST SP 800-115

Source: NIST SP 800-115 (September 2008), Section 6; supplemented by common penetration testing report conventions consistent with SP 800-115 reporting requirements

---

## Security Assessment Report Template

---

### [SYSTEM NAME] Security Assessment Report

**Classification**: [FOUO / Sensitive]
**Version**: 1.0
**Date**: [DATE]
**Prepared By**: [Assessment Organisation]
**Assessment Type**: [Network/Vulnerability Assessment / Penetration Test / Social Engineering / Combined]

---

#### Section 1 — Executive Summary

**1.1 System Identification**

| Field | Value |
|-------|-------|
| System Name | |
| System Owner | |
| Assessment Authorised By | |
| Assessment Period | [Start] to [End] |
| Assessment Team | |

**1.2 Overall Findings Summary**

| Severity | Count |
|---------|-------|
| Critical | |
| High | |
| Moderate | |
| Low | |
| Informational | |
| **Total** | |

**1.3 Key Risk Statement**

[2–4 sentences summarising the most significant risks found. Written for a non-technical audience. Example:]

"The assessment identified [N] critical and [N] high severity vulnerabilities. The most significant finding was [brief description], which would allow an attacker to [impact]. Immediate remediation of critical and high findings is recommended before the next assessment period."

**1.4 Immediate Actions Required**

List Critical and High-severity findings requiring prioritised remediation:

| Finding ID | Title | Severity | Affected Systems | Recommended Action |
|-----------|-------|---------|-----------------|-------------------|
| | | Critical | | |
| | | High | | |

**1.5 Assessment Limitations**

[Note any constraints that limited the assessment's thoroughness]

| Limitation | Impact on Results |
|-----------|------------------|
| | |

---

#### Section 2 — Assessment Scope and Methodology

**2.1 In-Scope Systems**

| Component | IP / Hostname | Environment |
|-----------|-------------|-------------|
| | | |

**2.2 Out-of-Scope Systems**

| Component | Reason for Exclusion |
|-----------|---------------------|
| | |

**2.3 Assessment Types Conducted**

- [ ] Network Discovery
- [ ] Port and Service Scanning
- [ ] Vulnerability Scanning (unauthenticated)
- [ ] Vulnerability Scanning (credential-based)
- [ ] Penetration Testing
- [ ] Social Engineering
- [ ] Physical Security Testing
- [ ] Wireless Assessment
- [ ] Web Application Testing
- [ ] Configuration Review
- [ ] Documentation Review
- [ ] Log Review

**2.4 Approach**

[Black-box / Grey-box / White-box — with description of starting knowledge and constraints]

---

#### Section 3 — Technical Findings

Use the following template for each finding. Order findings by severity (Critical first).

---

**Finding Template**

```
Finding ID:       [PT-YYYY-001]
Severity:         Critical / High / Moderate / Low / Informational
CVSS Base Score:  [x.x (if applicable)]
CVE:              [CVE-YYYY-XXXXX (if applicable)]
CWE:              [CWE-XXX (if applicable)]

Title:            [Concise, specific title]
Affected Systems: [IP(s) or hostname(s)]
Service/Port:     [e.g., TCP 443 / HTTPS]

DESCRIPTION
[What the vulnerability is, why it is present, and what it means from a security perspective.
Avoid generic CVE descriptions — describe the vulnerability in the context of this specific system.]

STEPS TO REPRODUCE (PROOF OF EXPLOITABILITY)
Note: Include this section for Critical and High severity findings.
[Exact commands, tool configurations, and outputs demonstrating that the vulnerability was
confirmed or exploited. This distinguishes a penetration test finding from a scanner finding.]

Example format:
  1. Connected to [target IP]:[port] using [tool/method]
  2. Issued the following command: [exact command]
  3. Output received: [exact output or screenshot reference]
  4. This demonstrates [what was achieved]

IMPACT
[What an attacker could do if they exploited this vulnerability. Be specific:
- What system-level access would be gained?
- What data would be accessible?
- How would this affect confidentiality, integrity, or availability?
- What is the business impact?]

EVIDENCE
[Reference to screenshot, tool output, or log excerpt — typically placed in an appendix
and referenced here. For example: "See Appendix A, Figure A-1."]

RECOMMENDATION
[Specific, actionable remediation:
- For patching: "Upgrade [software] from version [current] to version [target] or later.
  Reference vendor advisory: [URL]."
- For configuration: "Set [specific configuration parameter] to [specific value]."
- For architecture: "Implement [specific control] to [address the specific risk]."
Note estimated effort (low/medium/high) if possible to help the system owner prioritise.]

REFERENCES
- CVE: [if applicable]
- NVD: [if applicable]
- Vendor Advisory: [if applicable]
- NIST SP 800-53 Rev 5: [Relevant control(s)]
- CWE: [if applicable]
```

---

#### Section 4 — Risk Summary Matrix

| Finding ID | Title | Severity | Likelihood | Impact | Risk | Recommended Timeline |
|-----------|-------|---------|-----------|--------|------|---------------------|
| | | Critical | Very High | Very High | Very High | Immediate (< 15 days) |
| | | High | High | High | High | 30 days |
| | | Moderate | Moderate | Moderate | Moderate | 90 days |

---

#### Section 5 — Remediation Roadmap

Organise remediation by timeline and effort:

**Immediate (0–15 days) — Critical Findings**
| Finding ID | Title | Responsible Party | Estimated Effort |
|-----------|-------|------------------|----------------|
| | | | |

**Short-term (15–30 days) — High Findings**
| Finding ID | Title | Responsible Party | Estimated Effort |
|-----------|-------|------------------|----------------|
| | | | |

**Medium-term (30–90 days) — Moderate Findings**
| Finding ID | Title | Responsible Party | Estimated Effort |
|-----------|-------|------------------|----------------|
| | | | |

**Long-term (90–180 days) — Low Findings**
| Finding ID | Title | Responsible Party | Estimated Effort |
|-----------|-------|------------------|----------------|
| | | | |

---

#### Section 6 — Assessor Attestation

The undersigned conducted this assessment in accordance with NIST SP 800-115, within the scope and constraints defined in the approved Rules of Engagement dated [DATE]. All testing was authorised. Cleanup of all testing artefacts was completed and is documented in the attached cleanup log.

| Role | Name | Signature | Date |
|------|------|----------|------|
| Assessment Lead | | | |
| Technical Assessor | | | |

---

#### Appendices

**Appendix A — Evidence Collection**
[Screenshots, tool output, logs — one appendix section per finding]

**Appendix B — Raw Scan Output**
[Full output of automated scanners, annotated with findings extracted]

**Appendix C — Testing Timeline**
[Chronological log of testing activities by date and time, useful for incident investigation and demonstrating clean activity]

| Date/Time | Activity | Target | Tool | Result |
|-----------|---------|--------|------|--------|
| | | | | |

**Appendix D — Cleanup Log**
[Record of every artefact created during the test and confirmation of removal]

| System | Artifact Created | Cleanup Action | Verified By | Date |
|--------|----------------|---------------|------------|------|
| | | | | |

---

## Severity Classification Summary

| Severity | CVSS Range | Remediation Timeframe | POA&M Required |
|---------|-----------|----------------------|---------------|
| Critical | 9.0–10.0 | Immediate (< 15 days) | Yes — immediate AO notification |
| High | 7.0–8.9 | 30 days | Yes |
| Moderate | 4.0–6.9 | 90 days | Yes |
| Low | 0.1–3.9 | 180 days | Yes |
| Informational | N/A | Best effort | No (SAR observation only) |

**Note**: Where CVSS is not applicable (e.g., for configuration findings without a CVE), use the SP 800-30 likelihood x impact matrix to determine severity (see finding-severity.md in nist-sp-800-53a references).

---

## Rules of Engagement Template

Use this template to create the RoE document before testing begins.

---

### Rules of Engagement — [SYSTEM NAME] Security Assessment

**Date**: [DATE]
**Assessment Organisation**: [Name]
**Authorising Official**: [Name, Title, Organisation]

#### Authorisation Statement

[Authorising Official name and title] of [organisation] hereby authorises [assessment organisation] to conduct a security assessment of the systems and network segments defined below. This authorisation is valid for the period [START DATE] through [END DATE].

#### In-Scope Systems

| Component | IP Range / Hostname | Assessment Types Permitted |
|-----------|--------------------|-----------------------------|
| | | Discovery, Scanning, Exploitation |
| | | Discovery, Scanning only (no exploitation) |

#### Explicitly Out-of-Scope

| System | Reason |
|--------|--------|
| Production payment processing environment | Risk of service disruption |
| Third-party hosted services | No authorisation from third party |

#### Prohibited Actions

The assessment team must not:
- [ ] Conduct denial-of-service testing against in-scope systems
- [ ] Exploit vulnerabilities in out-of-scope systems, even if discovered
- [ ] Access, copy, or retain any real user data (PII, PHI, financial)
- [ ] Share assessment findings or credentials outside the defined distribution list
- [ ] Test during [any restricted hours]

#### Emergency Escalation

If the assessment team discovers evidence of an ongoing attack or compromise unrelated to their testing:
1. Immediately stop all testing activity
2. Contact [POC Name, Phone] within 30 minutes
3. Preserve evidence of the finding
4. Do not attempt to remediate or remove the external attacker activity

#### Data Handling

All data collected during the assessment (tool output, captured credentials, screenshots) must be:
- Stored on encrypted media during the assessment
- Transmitted only over encrypted channels (no unencrypted email)
- Destroyed within [X days] after delivery of the final report

#### Signatures

| Role | Name | Signature | Date |
|------|------|----------|------|
| Authorising Official | | | |
| Assessment Team Lead | | | |
| System Owner | | | |

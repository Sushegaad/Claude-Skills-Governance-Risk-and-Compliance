# SWIFT CSCF - Assessment Process, Attestation, and Cross-Framework Mapping

---

## KYC-SA Attestation Process

### Overview
All SWIFT users must submit an annual **KYC Security Attestation (KYC-SA)** confirming compliance with the CSCF mandatory controls. The attestation is submitted through the SWIFT portal at swift.com/myswift and is visible to your counterparties.

### Attestation Workflow

1. **Prepare evidence** - Gather implementation evidence for all 26 mandatory controls (v2026) applicable to your architecture type
2. **Engage independent assessor** - Community-standard users must have an independent assessor validate compliance (see below)
3. **Complete KYC-SA form** - For each mandatory control, attest: Implemented / Partially Implemented / Not Implemented
4. **Submit by July 31** - Annual deadline; late submission triggers counterparty notifications
5. **Address counterparty queries** - Counterparties can view your attestation and may request clarification

### Independent Assessment Requirements

Since CSCF v2020, an **independent assessment** is required for all users (previously self-attestation was permitted for smaller institutions):

| Assessment Standard | Applies To |
|--------------------|-----------|
| Community Standard Assessment (CSA) | All SWIFT users not subject to Enhanced Standard |
| Enhanced Standard | Users on enhanced programmes or at regulator request |

**Who can act as an independent assessor:**
- Internal audit team (if sufficiently independent from the SWIFT operations team)
- External audit firm with SWIFT CSP assessment competency
- SWIFT-certified assessors (listed on SWIFT's KYC Registry)
- The assessor must not have operational responsibility for the SWIFT environment assessed

**Assessment scope:** All 26 mandatory controls (v2026) applicable to the architecture type; advisory controls optionally included.

---

## CSCF v2024 → v2026 Key Changes

| Change Area | v2024 | v2025 | v2026 |
|-------------|-------|-------|-------|
| Control count | 32 (25 mandatory, 7 advisory) | 32 (25 mandatory, 7 advisory; no promotions) | 32 (26 mandatory, 6 advisory; 2.4 promoted to Mandatory) |
| 2.2 Security Updates | Timely security updates, severity-prioritised | Unchanged (qualitative; no published day-count SLAs) | Unchanged |
| 4.2 MFA | Hardware token strongly recommended | Hardware token explicitly required; clarified app-based OTP insufficient for most types | Unchanged |
| 6.4 Log retention | 1 year minimum | Clarified: 1 year online, 3 years total | Unchanged |
| 7.1 SWIFT notification | 24-hour notification | Unchanged; emphasis on 30-day full report | Unchanged |
| A4 (Cloud) | Introduced in v2023 | Further clarified; cloud-specific guidance expanded | Unchanged |
| Assessment guidance | Community standard | Updated assessor qualification criteria | Unchanged |

---

## SWIFT Incident Notification Obligations

SWIFT requires notification when a cyber incident affects SWIFT infrastructure or transactions:

| Milestone | Deadline |
|-----------|----------|
| Initial notification to SWIFT (via CISO mailbox or KYC-SA portal) | 24 hours from confirmed cyber incident |
| Full incident report to SWIFT | 30 days |
| Internal escalation to senior management | Immediately upon detection |
| Law enforcement / regulatory notification | Per local requirements (varies by jurisdiction) |

**What constitutes a notifiable incident:**
- Unauthorised access to SWIFT systems or software
- Compromise of SWIFT credentials (operator tokens, passwords)
- Fraudulent or anomalous SWIFT transactions suspected to be cyber-related
- Malware found on SWIFT-connected systems
- Ransomware affecting the SWIFT zone

**SWIFT contact for incidents:** security@swift.com (SWIFT CISO office) and your SWIFT relationship manager.

---

## Service Bureau (Type B) Responsibilities

When using a service bureau (Type B architecture), responsibilities are split:

| Control Area | Service Bureau Responsibility | Customer Responsibility |
|-------------|-------------------------------|------------------------|
| SWIFT infrastructure security (1.1, 2.2, 2.3, 6.1, 6.2, 6.3) | Bureau attests on their KYC-SA | Customer must obtain and review bureau's KYC-SA |
| Operator access (4.2, 5.1) | Bureau provides access mechanism | Customer responsible for own operators' access |
| Log monitoring (6.4) | Bureau provides logs; may operate SIEM | Customer should receive relevant logs; review access |
| Incident response (7.1) | Bureau has own IRP | Customer must have SWIFT-specific addendum |
| Training (7.2) | Bureau trains its own staff | Customer trains own SWIFT users |

**Key obligation:** Customers using a service bureau must review their bureau's KYC-SA attestation annually and obtain assurance of compliance (Control 2.8). If the bureau is non-compliant, the customer may face counterparty notifications.

---

## Cross-Framework Mapping

### SWIFT CSCF ↔ ISO/IEC 27001:2022

| CSCF Control | ISO 27001:2022 Annex A Controls |
|-------------|--------------------------------|
| 1.1 SWIFT Environment Protection | A.8.22 (Segregation of networks), A.8.20 (Network security) |
| 1.2 OS Privileged Account Control | A.8.2 (Privileged access rights), A.8.18 (Use of privileged utility programs) |
| 1.4 Internet Restriction | A.8.20 (Network security), A.8.22 (Segregation) |
| 2.1 Internal Data Flow Security | A.8.24 (Cryptography), A.8.20 (Network security) |
| 2.2 Security Updates | A.8.8 (Management of technical vulnerabilities) |
| 2.3 System Hardening | A.8.8 (Technical vulnerability management), A.8.9 (Configuration management) |
| 2.6 Operator Session Security | A.8.24 (Cryptography), A.8.20 (Network security) |
| 2.7 Vulnerability Scanning | A.8.8 (Technical vulnerability management) |
| 2.8 Critical Activity Outsourcing | A.5.19 (Supplier relationships), A.5.20 (Addressing security in supplier agreements) |
| 3.1 Physical Security | A.7.1 (Physical security perimeters), A.7.2 (Physical entry) |
| 4.1 Password Policy | A.8.5 (Secure authentication) |
| 4.2 Multi-Factor Authentication | A.8.5 (Secure authentication) |
| 5.1 Logical Access Controls | A.8.3 (Information access restriction), A.8.2 (Privileged access rights) |
| 5.2 Token Management | A.8.5 (Secure authentication), A.8.2 (Privileged access rights) |
| 6.1 Malware Protection | A.8.7 (Protection against malware) |
| 6.2 Software Integrity | A.8.19 (Installation of software on operational systems), A.8.29 (Security testing in development) |
| 6.3 Database Integrity | A.8.3 (Information access restriction) |
| 6.4 Log and Monitoring | A.8.15 (Logging), A.8.16 (Monitoring activities) |
| 7.1 Incident Response | A.5.24 (Planning and preparation), A.5.26 (Response to incidents) |
| 7.2 Security Training | A.6.3 (Information security awareness) |

**Synergy note:** An ISO 27001-certified organisation will have satisfied many CSCF controls through their ISMS. However, SWIFT CSP adds SWIFT-specific requirements (e.g., hardware MFA tokens, SWIFT log sources, KYC-SA submission) that are not automatically covered by ISO 27001.

---

### SWIFT CSCF ↔ PCI DSS v4.0.1

| CSCF Control | PCI DSS Requirement |
|-------------|---------------------|
| 1.1 SWIFT Environment Protection | Req 1 (Network security controls), Req 1.2 (Firewall rules) |
| 1.4 Internet Restriction | Req 1.3 (Restrict inbound/outbound traffic) |
| 2.2 Security Updates | Req 6.3 (Security vulnerabilities addressed) |
| 2.3 System Hardening | Req 2.2 (System components configured securely) |
| 4.1 Password Policy | Req 8.3 (Strong authentication) |
| 4.2 Multi-Factor Authentication | Req 8.4 (MFA for non-console admin access and remote access) |
| 5.1 Logical Access Controls | Req 7 (Restrict access to system components and cardholder data) |
| 6.1 Malware Protection | Req 5 (Protect against malicious software) |
| 6.4 Log and Monitoring | Req 10 (Log and monitor all access) |
| 7.1 Incident Response | Req 12.10 (Incident response plan) |

**Key difference:** PCI DSS focuses on cardholder data environments; SWIFT CSP focuses on the SWIFT messaging infrastructure. A PCI-compliant organisation will have a strong security foundation but will need SWIFT-specific additions (e.g., hardware MFA, SWIFT log sources, 1-year log retention, KYC-SA submission).

---

### SWIFT CSCF ↔ NIST CSF 2.0

| CSCF Control | NIST CSF 2.0 Function/Category |
|-------------|-------------------------------|
| 1.1 SWIFT Environment Protection | PR.IR (Infrastructure Resilience) |
| 2.2 Security Updates | PR.PS-2 (Software, firmware patched) |
| 2.3 System Hardening | PR.PS-1 (Configuration management) |
| 4.2 MFA | PR.AA-3 (Authentication) |
| 5.1 Logical Access Controls | PR.AA-1 (Identity management) |
| 6.1 Malware Protection | PR.PS-3 (Malware protection) |
| 6.4 Log and Monitoring | DE.CM (Continuous monitoring) |
| 7.1 Incident Response | RS.MA (Incident management) |
| 7.2 Security Training | PR.AT (Awareness and training) |

---

## Regulatory Context

SWIFT CSP compliance is increasingly referenced in financial sector regulation:

| Jurisdiction | Regulatory Reference |
|-------------|---------------------|
| **EU** | ECB TIBER-EU framework; EBA ICT guidelines under DORA reference SWIFT CSP for financial messaging |
| **US** | FFIEC Cybersecurity Assessment Tool references correspondent banking controls; NY DFS 23 NYCRR 500 aligns to SWIFT CSP |
| **UK** | Bank of England / PRA supervisory expectations for payment systems include SWIFT CSP |
| **Singapore** | MAS TRM (Technology Risk Management) guidelines align to SWIFT CSP for banks |
| **Hong Kong** | HKMA Cybersecurity Fortification Initiative (CFI) references SWIFT CSP for Tier 1 and 2 banks |
| **Australia** | APRA CPS 234 includes SWIFT CSP controls under critical third-party system security |

---

## Gap Assessment Checklist Template

For each mandatory control, assess against these criteria:

| Column | Description |
|--------|-------------|
| Control ID | e.g., 4.2 |
| Status | 🔴 Not Implemented / 🟡 Partially Implemented / 🟢 Implemented |
| Evidence Available | Yes / No / Partial |
| Evidence Type | Policy / Configuration / Logs / Test result / Screenshot |
| Gap Description | Specific gap narrative |
| Remediation Action | Concrete step to close the gap |
| Owner | Team/individual responsible |
| Target Date | When gap will be closed |
| Attestation Impact | If 🔴: Attest as Not Implemented; if 🟡: Partially; if 🟢: Implemented |

---

## Most Common CSCF Non-Compliance Patterns

1. **Software-based OTP for MFA (Control 4.2):** Many organisations use authenticator apps rather than hardware tokens. SWIFT CSP requires hardware tokens for most architecture types.

2. **Shared operator accounts (Control 5.1):** Named individual accounts not enforced; multiple operators sharing one account ID - makes non-repudiation impossible.

3. **Log retention gaps (Control 6.4):** Logs collected but not retained for 1+ years; SWIFT-specific log sources (Alliance Access/Gateway) not included in SIEM scope.

4. **Patch exceptions undocumented (Control 2.2):** Security updates not applied in a timely manner, with no documented exception/compensating control.

5. **SWIFT zone not documented (Control 1.1):** Secure Zone exists technically but no network diagram; or servers are dual-homed to both SWIFT zone and corporate network.

6. **No SWIFT-specific IRP (Control 7.1):** General incident response plan exists but no SWIFT-specific section covering SWIFT notification obligations and fraud scenarios.

7. **Token inventory not maintained (Control 5.2):** Hardware tokens issued but no central inventory; deprovisioning process for leavers undocumented.

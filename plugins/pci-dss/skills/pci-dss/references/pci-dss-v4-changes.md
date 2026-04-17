# PCI DSS v3.2.1 → v4.0 / v4.0.1 Change Guide

Source: PCI DSS Summary of Changes v3.2.1 to v4.0 (PCI SSC); PCI DSS v4.0.1 (June 2024)

---

## Version Timeline

| Version | Released | Status |
|---------|----------|--------|
| PCI DSS v3.2.1 | May 2018 | **Retired March 31, 2024** |
| PCI DSS v4.0 | March 2022 | Superseded by v4.0.1 |
| PCI DSS v4.0.1 | June 2024 | **Current** — minor errata update |

**Important milestones:**
- March 31, 2024: PCI DSS v3.2.1 retired — all assessments now use v4.0 or v4.0.1
- March 31, 2025: All "future-dated" requirements from PCI DSS v4.0 became **mandatory** (previously best practice)
- v4.0.1 corrects typographical errors and clarifications in v4.0; no new controls added

---

## Structural Changes

| Aspect | v3.2.1 | v4.0 / v4.0.1 |
|--------|--------|--------------|
| Compliance approach | Defined approach only | Added **Customised Approach** |
| Targeted Risk Analysis | Informal | **Formalised requirement** for flexible controls |
| Requirements structure | 12 requirements, 259 sub-requirements | 12 requirements, 300+ sub-requirements |
| Future-dated requirements | N/A | Requirements phased in by March 2025 |
| Informative references | Embedded | Moved to PCI SSC Reference Tool (online) |
| Focus | Prescriptive controls | Outcomes-focused (especially Customised Approach) |

---

## New Requirements in v4.0 (Mandatory from March 31, 2025)

These requirements were "future-dated" in v4.0 (published March 2022 as best practice) and became mandatory on **March 31, 2025**:

### Requirement 3: Protect Stored Account Data
- **3.3.2**: SAD stored prior to authorisation is encrypted using strong cryptography (Applies to issuers and companies supporting issuing services only)
- **3.3.3**: Encryption keys for pre-authorisation SAD are managed per key management requirements

### Requirement 4: Protect CHD During Transmission
- **4.2.1.1**: Inventory of trusted keys and certificates is maintained

### Requirement 5: Anti-Malware
- **5.3.3**: Anti-malware solution performs scans of removable electronic media
- **5.4.1**: Automated technical solution to detect and protect against phishing attacks (**NEW concept**)

### Requirement 6: Secure Development
- **6.3.2**: Software inventory (SBOM) maintained for bespoke and custom software
- **6.4.3**: All payment page scripts inventoried, authorised, and integrity protected (**NEW — critical for e-commerce**)

### Requirement 7: Access Control
- **7.2.4**: User accounts and access privileges reviewed at minimum every 6 months
- **7.2.5**: Application/system accounts managed per policy
- **7.2.5.1**: Privileges of application/system accounts reviewed at least every 6 months
- **7.3.2**: Access control system configured to enforce least privilege

### Requirement 8: Authentication
- **8.3.6**: Passwords/passphrases for users without MFA changed at least every 90 days
- **8.4.2**: MFA for all access into the CDE (**Extended scope — was only for remote access in v3.2.1**)
- **8.6.1**: System/application accounts that can be used interactively managed and protected
- **8.6.2**: Passwords/passphrases for system/application accounts not hardcoded in scripts or source code

### Requirement 10: Logging
- **10.4.1.1**: Automated log review mechanisms used (**NEW — manual-only review no longer sufficient**)
- **10.7.2**: Failures of critical security controls detected, reported, and addressed promptly (**NEW**)
- **10.7.3**: Failures of critical security controls responded to within defined timeframes

### Requirement 11: Security Testing
- **11.4.7**: Multi-tenant service providers support customers' requests for penetration testing
- **11.6.1**: Change and tamper detection mechanism for HTTP headers and scripts on payment pages deployed (**NEW — critical for web skimming prevention**)

### Requirement 12: Policy and Programs
- **12.3.2**: Targeted risk analysis for each PCI DSS requirement that has a customised approach
- **12.3.3**: Cryptographic cipher suites and protocols reviewed at least every 12 months
- **12.3.4**: Hardware and software technologies reviewed at least every 12 months
- **12.5.2.1**: PCI DSS scope verified by multi-tenant service providers at minimum every 6 months
- **12.8.4**: TPSP compliance status monitored at least every 12 months
- **12.9.2**: TPSPs support customers' requests for confirmation of PCI DSS responsibility
- **12.10.4.1**: IR personnel training at minimum every 12 months
- **12.10.7**: IR procedures for discovery of stored PAN in unexpected location

---

## Key Conceptual Changes

### 1. Customised Approach (Major v4.0 Innovation)
The Customised Approach allows organisations to implement alternative controls designed by the entity to achieve the stated **Objective** of a PCI DSS requirement, rather than following the prescriptive testing procedure.

**Requirements for Customised Approach:**
- A Targeted Risk Analysis (TRA) must be performed and documented for each customised control
- TRA must be approved by senior management
- Customised control must be assessed by a QSA using a Customised Approach Test Plan (CATP)
- Annual review and revalidation required
- Not available for SAQ A or SAQ B; typically used in ROC environments

**When to use**: When the defined approach does not fit the technology architecture (e.g., cloud-native, microservices, zero-trust) and the organisation can demonstrably achieve the security objective through alternative means.

### 2. Expanded MFA Requirement (Req 8.4.2)
In v3.2.1, MFA was required for:
- All non-console administrative access to the CDE
- Remote access to the network from outside the entity's network

In v4.0, MFA is required for **ALL access into the CDE** — including access from within the internal network. This is the most impactful change for many organisations and a common gap.

**Practical impact**: If a user on the internal corporate LAN accesses a CDE system, MFA is now required. VPN + network segmentation alone is no longer sufficient.

### 3. Payment Page Script Security (Req 6.4.3 and 11.6.1)
These requirements address **web skimming** (e.g., Magecart attacks) where malicious scripts are injected into payment pages to steal cardholder data.

**Req 6.4.3**: All scripts loaded and executed in the consumer's browser on a payment page must be:
- Inventoried with a method to confirm integrity
- Authorised by management — documented justification for each script
- Integrity protected — either using CSP (Content Security Policy), SRI (Sub-Resource Integrity), or equivalent

**Req 11.6.1**: A change and tamper detection mechanism must be deployed that:
- Alerts personnel to unauthorised modification of HTTP headers and content of payment pages
- Is assessed at minimum every 7 days (or frequency defined by targeted risk analysis)

### 4. Phishing Protection (Req 5.4.1)
Organisations must now implement automated technical solutions to detect and protect users against phishing attacks. Acceptable solutions include:
- Email security gateways with anti-phishing/URL scanning
- DNS filtering solutions
- DMARC + DKIM + SPF email authentication
- Anti-phishing browser extensions managed by policy

### 5. Targeted Risk Analysis (TRA)
The TRA is a formalised risk analysis process used to:
- Define controls for requirements with flexible frequencies (e.g., how often to review certain items)
- Justify Customised Approach implementations
- Document risk-based decisions

Required TRA elements: Risk description | Defined approach requirement | Reason for customisation | How the objective is achieved | Evidence of effectiveness | Management sign-off | Annual review date

### 6. Automated Log Review (Req 10.4.1.1)
Manual daily log review is no longer sufficient. An automated mechanism (e.g., SIEM with alert rules, automated anomaly detection) must be in place. The automated system must alert on anomalous activity.

---

## Requirements Removed or Significantly Changed

| v3.2.1 Requirement | Change in v4.0 |
|-------------------|---------------|
| Req 6.3 (Application vulnerabilities) | Restructured into 6.3.1–6.5.6 |
| Req 10.6 (Log review) | Restructured into 10.4 with automated review added |
| Req 11.2 (Vulnerability scans) | Restructured; ASV scan requirements unchanged |
| Req 12.10 (IR plan) | Expanded with new sub-requirements |
| Business-as-usual (BAU) activities | Replaced by more specific ongoing compliance requirements |
| Appendix A2 (TLS migration) | Removed — TLS 1.0/1.1 migration deadline passed |
| Appendix A3 (Designated Entities) | Moved/updated |

---

## Migration Checklist: v3.2.1 → v4.0.1

**Governance and Policy (Req 12)**
- [ ] Establish a formal Targeted Risk Analysis (TRA) process and template (12.3.2)
- [ ] Conduct annual review of cryptographic cipher suites (12.3.3)
- [ ] Conduct annual hardware/software technology lifecycle review (12.3.4)
- [ ] Confirm TPSP compliance status annually — update TPSP register (12.8.4)
- [ ] Train IR personnel at minimum annually (12.10.4.1)
- [ ] Create IR procedure for unexpected PAN discovery (12.10.7)
- [ ] Verify PCI DSS scope at least every 12 months and after major changes (12.5.2)

**Authentication (Req 8)**
- [ ] Extend MFA to ALL access into the CDE — including internal network users (8.4.2)
- [ ] Update password policy: minimum 12 characters (8.3.5)
- [ ] Ensure no hardcoded passwords in scripts or source code (8.6.2)

**E-commerce and Web Application (Req 6, 11)**
- [ ] Create inventory of all payment page scripts with authorisation and integrity controls (6.4.3)
- [ ] Deploy change/tamper detection on HTTP headers and payment page content (11.6.1)
- [ ] Enable CSP/SRI headers or equivalent script integrity controls

**Anti-Malware and Phishing (Req 5)**
- [ ] Deploy automated anti-phishing technical solution (5.4.1): email gateway + SPF/DKIM/DMARC
- [ ] Add removable media scanning to anti-malware coverage (5.3.3)

**Logging (Req 10)**
- [ ] Implement automated log review mechanism (SIEM or equivalent) (10.4.1.1)
- [ ] Configure monitoring for critical security control failures (10.7.2)

**Access Control (Req 7, 8)**
- [ ] Implement 6-monthly access reviews for all accounts (7.2.4)
- [ ] Document and control all application/system account access (7.2.5)

**Software Inventory (Req 6)**
- [ ] Build and maintain Software Bill of Materials (SBOM) for bespoke software (6.3.2)

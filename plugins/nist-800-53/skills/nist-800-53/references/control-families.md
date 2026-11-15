# NIST SP 800-53 Rev 5 - Control Families Reference

## How to Use This Reference

For each family: key controls with baseline assignment, critical enhancements, and implementation guidance. Baseline codes: **L** = Low, **M** = Moderate, **H** = High. Controls marked **(org)** are PM family - organization-wide, not baseline-specific.

---

## AC - Access Control (25 controls)

**Purpose:** Limit system access to authorized users, processes, devices, and types of transactions.

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| AC-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| AC-2 | ✓ | ✓ | ✓ | Account Management - create, enable, modify, disable, remove accounts |
| AC-2(1) | - | ✓ | ✓ | Automated System Account Management |
| AC-2(3) | - | ✓ | ✓ | Disable Accounts (after inactivity - ODV: 90 days typical) |
| AC-2(5) | - | ✓ | ✓ | Inactivity Logout |
| AC-2(12) | - | - | ✓ | Account Monitoring for Atypical Usage |
| AC-3 | ✓ | ✓ | ✓ | Access Enforcement - enforce approved authorizations |
| AC-4 | - | ✓ | ✓ | Information Flow Enforcement |
| AC-5 | - | ✓ | ✓ | Separation of Duties |
| AC-6 | - | ✓ | ✓ | Least Privilege |
| AC-6(1) | - | ✓ | ✓ | Authorize Access to Security Functions |
| AC-6(2) | - | ✓ | ✓ | Non-Privileged Access for Non-Security Functions |
| AC-6(5) | - | ✓ | ✓ | Privileged Accounts |
| AC-6(9) | - | ✓ | ✓ | Log Use of Privileged Functions |
| AC-6(10) | - | ✓ | ✓ | Prohibit Non-Privileged Users from Executing Privileged Functions |
| AC-7 | ✓ | ✓ | ✓ | Unsuccessful Logon Attempts (lockout after ODV attempts) |
| AC-8 | ✓ | ✓ | ✓ | System Use Notification (login banner) |
| AC-11 | - | ✓ | ✓ | Device Lock |
| AC-12 | - | ✓ | ✓ | Session Termination |
| AC-14 | ✓ | ✓ | ✓ | Permitted Actions Without Identification or Authentication |
| AC-17 | ✓ | ✓ | ✓ | Remote Access |
| AC-17(1) | - | ✓ | ✓ | Monitoring and Control of Remote Access |
| AC-18 | ✓ | ✓ | ✓ | Wireless Access |
| AC-19 | ✓ | ✓ | ✓ | Access Control for Mobile Devices |
| AC-20 | ✓ | ✓ | ✓ | Use of External Systems |
| AC-22 | ✓ | ✓ | ✓ | Publicly Accessible Content |

**Implementation notes:**
- AC-2 requires documented procedures for account lifecycle; automated provisioning/deprovisioning satisfies AC-2(1)
- AC-6 least privilege: document roles, restrict admin rights to dedicated admin accounts
- AC-17 remote access: requires MFA (IA-2), encryption in transit (SC-8), and monitoring

---

## AT - Awareness and Training (6 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| AT-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| AT-2 | ✓ | ✓ | ✓ | Literacy Training and Awareness (annual; new hire; role change) |
| AT-2(2) | - | ✓ | ✓ | Insider Threat Awareness |
| AT-3 | ✓ | ✓ | ✓ | Role-Based Training (before access; when changes occur) |
| AT-4 | ✓ | ✓ | ✓ | Training Records (retain for ODV period, typically 3 years) |
| AT-6 | - | - | ✓ | Training Feedback |

---

## AU - Audit and Accountability (16 controls)

**Purpose:** Create and protect system audit records; ensure accountability of user actions.

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| AU-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| AU-2 | ✓ | ✓ | ✓ | Event Logging - define auditable events |
| AU-3 | ✓ | ✓ | ✓ | Content of Audit Records (what, when, where, source, outcome) |
| AU-3(1) | - | ✓ | ✓ | Additional Audit Information |
| AU-4 | ✓ | ✓ | ✓ | Audit Log Storage Capacity |
| AU-5 | ✓ | ✓ | ✓ | Response to Audit Logging Process Failures |
| AU-6 | ✓ | ✓ | ✓ | Audit Record Review, Analysis, and Reporting |
| AU-6(1) | - | ✓ | ✓ | Automated Process Integration (SIEM) |
| AU-7 | - | ✓ | ✓ | Audit Record Reduction and Report Generation |
| AU-8 | ✓ | ✓ | ✓ | Time Stamps (synchronized; NTP) |
| AU-9 | ✓ | ✓ | ✓ | Protection of Audit Information |
| AU-9(4) | - | ✓ | ✓ | Access by Subset of Privileged Users |
| AU-10 | - | - | ✓ | Non-Repudiation |
| AU-11 | ✓ | ✓ | ✓ | Audit Record Retention (ODV: typically 3 years for federal) |
| AU-12 | ✓ | ✓ | ✓ | Audit Record Generation |
| AU-14 | - | - | ✓ | Session Audit |

**Key events to audit (AU-2):** logon/logoff attempts, privilege escalation, account creation/modification/deletion, system configuration changes, access to sensitive data, use of admin functions.

---

## CA - Assessment, Authorization, and Monitoring (9 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| CA-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| CA-2 | ✓ | ✓ | ✓ | Control Assessments (annual or event-driven) |
| CA-2(1) | - | ✓ | ✓ | Independent Assessors (3PAO for FedRAMP) |
| CA-3 | ✓ | ✓ | ✓ | Information Exchange (ISA/MOU for interconnections) |
| CA-5 | ✓ | ✓ | ✓ | Plan of Action and Milestones (POA&M) |
| CA-6 | ✓ | ✓ | ✓ | Authorization (ATO from Authorizing Official) |
| CA-7 | ✓ | ✓ | ✓ | Continuous Monitoring (ConMon strategy; ODV frequencies) |
| CA-7(1) | - | ✓ | ✓ | Independent Assessment |
| CA-8 | - | - | ✓ | Penetration Testing |
| CA-9 | ✓ | ✓ | ✓ | Internal System Connections |

---

## CM - Configuration Management (14 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| CM-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| CM-2 | ✓ | ✓ | ✓ | Baseline Configuration |
| CM-2(2) | - | ✓ | ✓ | Automation Support for Accuracy and Currency |
| CM-3 | - | ✓ | ✓ | Configuration Change Control |
| CM-4 | ✓ | ✓ | ✓ | Impact Analyses |
| CM-5 | - | ✓ | ✓ | Access Restrictions for Change |
| CM-6 | ✓ | ✓ | ✓ | Configuration Settings (SCAP/STIG/CIS Benchmarks) |
| CM-6(1) | - | ✓ | ✓ | Automated Management, Application, and Verification |
| CM-7 | ✓ | ✓ | ✓ | Least Functionality (disable unnecessary functions/ports/services) |
| CM-7(1) | - | ✓ | ✓ | Periodic Review |
| CM-7(2) | - | ✓ | ✓ | Prevent Software Execution |
| CM-7(5) | - | ✓ | ✓ | Authorized Software / Allowlisting |
| CM-8 | ✓ | ✓ | ✓ | System Component Inventory |
| CM-9 | - | ✓ | ✓ | Configuration Management Plan |
| CM-10 | ✓ | ✓ | ✓ | Software Usage Restrictions |
| CM-11 | ✓ | ✓ | ✓ | User-Installed Software |

---

## CP - Contingency Planning (13 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| CP-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| CP-2 | ✓ | ✓ | ✓ | Contingency Plan (BCP/DRP) |
| CP-2(3) | - | ✓ | ✓ | Resume All Missions and Business Functions |
| CP-3 | ✓ | ✓ | ✓ | Contingency Training |
| CP-4 | ✓ | ✓ | ✓ | Contingency Plan Testing |
| CP-4(1) | - | ✓ | ✓ | Coordinate with Related Plans |
| CP-6 | - | ✓ | ✓ | Alternate Storage Site |
| CP-7 | - | ✓ | ✓ | Alternate Processing Site |
| CP-8 | - | ✓ | ✓ | Telecommunications Services |
| CP-9 | ✓ | ✓ | ✓ | System Backup |
| CP-9(1) | - | ✓ | ✓ | Testing for Reliability and Integrity |
| CP-10 | ✓ | ✓ | ✓ | System Recovery and Reconstitution |
| CP-10(2) | - | ✓ | ✓ | Transaction Recovery |

**RTO/RPO guidance:** CP-2 should document target RTO and RPO; CP-7 alternate site must support target RTO.

---

## IA - Identification and Authentication (13 controls)

**Purpose:** Identify and authenticate users, devices, and processes.

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| IA-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| IA-2 | ✓ | ✓ | ✓ | Identification and Authentication (Organizational Users) |
| IA-2(1) | ✓ | ✓ | ✓ | MFA for Privileged Accounts |
| IA-2(2) | ✓ | ✓ | ✓ | MFA for Non-Privileged Accounts (network access) |
| IA-2(6) | - | - | ✓ | MFA for Separate Device |
| IA-2(8) | - | ✓ | ✓ | Access to Accounts - Replay Resistant |
| IA-2(12) | ✓ | ✓ | ✓ | Acceptance of PIV Credentials |
| IA-3 | - | ✓ | ✓ | Device Identification and Authentication |
| IA-4 | ✓ | ✓ | ✓ | Identifier Management |
| IA-5 | ✓ | ✓ | ✓ | Authenticator Management |
| IA-5(1) | ✓ | ✓ | ✓ | Password-Based Authentication |
| IA-5(2) | - | ✓ | ✓ | PKI-Based Authentication |
| IA-6 | ✓ | ✓ | ✓ | Authentication Feedback (obscure passwords) |
| IA-7 | ✓ | ✓ | ✓ | Cryptographic Module Authentication |
| IA-8 | ✓ | ✓ | ✓ | Identification and Authentication (Non-Organizational Users) |
| IA-11 | - | ✓ | ✓ | Re-authentication |
| IA-12 | - | ✓ | ✓ | Identity Proofing (NIST SP 800-63A levels) |

**MFA requirements (post-EO 14028):** Federal systems must use phishing-resistant MFA (PIV/CAC, FIDO2) - IA-2(1) and IA-2(2) are now required at Low baseline for federal systems.

---

## IR - Incident Response (10 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| IR-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| IR-2 | ✓ | ✓ | ✓ | Incident Response Training |
| IR-3 | - | ✓ | ✓ | Incident Response Testing |
| IR-4 | ✓ | ✓ | ✓ | Incident Handling |
| IR-4(1) | - | ✓ | ✓ | Automated Incident Handling Processes |
| IR-5 | ✓ | ✓ | ✓ | Incident Monitoring |
| IR-6 | ✓ | ✓ | ✓ | Incident Reporting (US-CERT/CISA - 1-hour for major incidents) |
| IR-6(1) | - | ✓ | ✓ | Automated Reporting |
| IR-7 | ✓ | ✓ | ✓ | Incident Response Assistance |
| IR-8 | ✓ | ✓ | ✓ | Incident Response Plan |
| IR-10 | - | - | ✓ | Integrated Information Security Analysis Team |

**Federal reporting (IR-6):** Report cybersecurity incidents to CISA within 1 hour for major incidents; FISMA annual reporting to OMB.

---

## MA - Maintenance (6 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| MA-2 | ✓ | ✓ | ✓ | Controlled Maintenance |
| MA-3 | - | ✓ | ✓ | Maintenance Tools |
| MA-4 | ✓ | ✓ | ✓ | Nonlocal Maintenance |
| MA-5 | ✓ | ✓ | ✓ | Maintenance Personnel |
| MA-6 | - | ✓ | ✓ | Timely Maintenance |

---

## MP - Media Protection (8 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| MP-2 | ✓ | ✓ | ✓ | Media Access |
| MP-3 | - | ✓ | ✓ | Media Marking |
| MP-4 | - | ✓ | ✓ | Media Storage |
| MP-5 | - | ✓ | ✓ | Media Transport |
| MP-6 | ✓ | ✓ | ✓ | Media Sanitization (NIST SP 800-88 guidelines) |
| MP-7 | ✓ | ✓ | ✓ | Media Use |

---

## PE - Physical and Environmental Protection (23 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| PE-2 | ✓ | ✓ | ✓ | Physical Access Authorizations |
| PE-3 | ✓ | ✓ | ✓ | Physical Access Control |
| PE-6 | ✓ | ✓ | ✓ | Monitoring Physical Access |
| PE-8 | ✓ | ✓ | ✓ | Visitor Access Records |
| PE-12 | ✓ | ✓ | ✓ | Emergency Lighting |
| PE-13 | ✓ | ✓ | ✓ | Fire Protection |
| PE-14 | ✓ | ✓ | ✓ | Environmental Controls (temperature, humidity) |
| PE-15 | ✓ | ✓ | ✓ | Water Damage Protection |
| PE-16 | ✓ | ✓ | ✓ | Delivery and Removal |
| PE-17 | - | ✓ | ✓ | Alternate Work Site |
| PE-19 | - | ✓ | ✓ | Information Leakage |

---

## PL - Planning (11 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| PL-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| PL-2 | ✓ | ✓ | ✓ | System Security and Privacy Plan (SSP) |
| PL-4 | ✓ | ✓ | ✓ | Rules of Behavior |
| PL-8 | - | ✓ | ✓ | Security and Privacy Architectures |
| PL-10 | ✓ | ✓ | ✓ | Baseline Selection |
| PL-11 | ✓ | ✓ | ✓ | Baseline Tailoring |

---

## PS - Personnel Security (9 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| PS-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| PS-2 | ✓ | ✓ | ✓ | Position Risk Designation |
| PS-3 | ✓ | ✓ | ✓ | Personnel Screening |
| PS-4 | ✓ | ✓ | ✓ | Personnel Termination |
| PS-5 | ✓ | ✓ | ✓ | Personnel Transfer |
| PS-6 | ✓ | ✓ | ✓ | Access Agreements |
| PS-7 | ✓ | ✓ | ✓ | External Personnel Security |
| PS-8 | ✓ | ✓ | ✓ | Personnel Sanctions |
| PS-9 | ✓ | ✓ | ✓ | Position Descriptions |

---

## PT - PII Processing and Transparency (8 controls)

**Purpose:** Govern how organizations handle Personally Identifiable Information (PII). New in Rev 5; applies to systems processing PII.

| Control | Description |
|---------|-------------|
| PT-1 | Policy and Procedures |
| PT-2 | Authority to Process PII (legal basis) |
| PT-3 | Purposing Specification (why PII is collected) |
| PT-4 | Consent (where legally required) |
| PT-5 | Privacy Notice (transparency at collection) |
| PT-6 | System of Records Notice (SORN for Privacy Act systems) |
| PT-7 | Specific Categories of Personally Identifiable Information |
| PT-8 | Computer Matching Requirements |

**Privacy Act connection:** PT-6 requires a SORN for systems covered by the Privacy Act (5 U.S.C. § 552a). Published in the Federal Register.

---

## RA - Risk Assessment (10 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| RA-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| RA-2 | ✓ | ✓ | ✓ | Security Categorization (FIPS 199) |
| RA-3 | ✓ | ✓ | ✓ | Risk Assessment (SP 800-30 methodology) |
| RA-3(1) | - | ✓ | ✓ | Supply Chain Risk Assessment |
| RA-5 | ✓ | ✓ | ✓ | Vulnerability Monitoring and Scanning |
| RA-5(2) | - | ✓ | ✓ | Update Vulnerabilities to be Scanned |
| RA-5(5) | - | ✓ | ✓ | Privileged Access |
| RA-7 | ✓ | ✓ | ✓ | Risk Response |
| RA-9 | - | ✓ | ✓ | Criticality Analysis |
| RA-10 | - | - | ✓ | Threat Hunting |

**Vulnerability scanning cadence (RA-5):** CISA BOD 19-02 - Critical vulnerabilities patch within 15 days, High within 30 days. FedRAMP: monthly OS/web app scans; weekly database scans.

---

## SA - System and Services Acquisition (23 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| SA-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| SA-2 | ✓ | ✓ | ✓ | Allocation of Resources |
| SA-3 | ✓ | ✓ | ✓ | System Development Life Cycle (SDLC security integration) |
| SA-4 | ✓ | ✓ | ✓ | Acquisition Process (security requirements in contracts) |
| SA-4(1) | - | ✓ | ✓ | Functional Properties of Controls |
| SA-4(2) | - | ✓ | ✓ | Design and Implementation Information |
| SA-4(9) | - | ✓ | ✓ | Functions, Ports, Protocols, and Services in Use |
| SA-5 | ✓ | ✓ | ✓ | System Documentation |
| SA-8 | - | ✓ | ✓ | Security and Privacy Engineering Principles |
| SA-9 | ✓ | ✓ | ✓ | External System Services |
| SA-10 | - | ✓ | ✓ | Developer Configuration Management |
| SA-11 | - | ✓ | ✓ | Developer Testing and Evaluation |
| SA-15 | - | ✓ | ✓ | Development Process, Standards, and Tools |
| SA-17 | - | - | ✓ | Developer Architecture and Design |
| SA-22 | ✓ | ✓ | ✓ | Unsupported System Components |

---

## SC - System and Communications Protection (51 controls)

**Purpose:** Protect communications and system boundaries.

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| SC-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| SC-5 | ✓ | ✓ | ✓ | Denial of Service Protection |
| SC-7 | ✓ | ✓ | ✓ | Boundary Protection (firewalls, DMZ, NGFW) |
| SC-7(3) | - | ✓ | ✓ | Access Points |
| SC-7(4) | - | ✓ | ✓ | External Telecommunications Services |
| SC-7(5) | - | ✓ | ✓ | Deny by Default / Allow by Exception |
| SC-7(7) | - | ✓ | ✓ | Split Tunneling for Remote Devices |
| SC-7(8) | - | ✓ | ✓ | Route Traffic to Authenticated Proxy Servers |
| SC-8 | - | ✓ | ✓ | Transmission Confidentiality and Integrity |
| SC-8(1) | - | ✓ | ✓ | Cryptographic Protection (TLS 1.2+ or TLS 1.3) |
| SC-10 | - | ✓ | ✓ | Network Disconnect |
| SC-12 | ✓ | ✓ | ✓ | Cryptographic Key Establishment and Management |
| SC-13 | ✓ | ✓ | ✓ | Cryptographic Protection (FIPS 140-2/3 validated modules) |
| SC-15 | ✓ | ✓ | ✓ | Collaborative Computing Devices and Applications |
| SC-17 | - | ✓ | ✓ | Public Key Infrastructure Certificates (PKI) |
| SC-18 | - | ✓ | ✓ | Mobile Code |
| SC-20 | ✓ | ✓ | ✓ | Secure Name/Address Resolution Service |
| SC-21 | ✓ | ✓ | ✓ | Secure Name/Address Resolution Service (Recursive) |
| SC-22 | ✓ | ✓ | ✓ | Architecture and Provisioning for Name/Address Resolution Service |
| SC-23 | - | ✓ | ✓ | Session Authenticity |
| SC-28 | - | ✓ | ✓ | Protection of Information at Rest (SP 800-53B: Moderate entry; FedRAMP Low adds it) |
| SC-28(1) | - | ✓ | ✓ | Cryptographic Protection (AES-256 for data at rest) |
| SC-39 | ✓ | ✓ | ✓ | Process Isolation |

**Cryptography requirements:** SC-13 mandates FIPS 140-2 (or FIPS 140-3) validated cryptographic modules. SC-8(1) requires cryptographic protection in transit; SC-28(1) requires encryption at rest.

---

## SI - System and Information Integrity (23 controls)

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| SI-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| SI-2 | ✓ | ✓ | ✓ | Flaw Remediation (patch management) |
| SI-2(2) | - | ✓ | ✓ | Automated Flaw Remediation Status |
| SI-3 | ✓ | ✓ | ✓ | Malicious Code Protection (AV/EDR) |
| SI-3(2) | - | ✓ | ✓ | Automatic Updates |
| SI-4 | ✓ | ✓ | ✓ | System Monitoring (IDS/IPS, SIEM) |
| SI-4(2) | - | ✓ | ✓ | Automated Tools and Mechanisms for Real-Time Analysis |
| SI-4(4) | - | ✓ | ✓ | Inbound and Outbound Communications Traffic |
| SI-4(5) | - | ✓ | ✓ | System-Generated Alerts |
| SI-5 | ✓ | ✓ | ✓ | Security Alerts, Advisories, and Directives |
| SI-6 | - | - | ✓ | Security and Privacy Function Verification |
| SI-7 | - | ✓ | ✓ | Software, Firmware, and Information Integrity |
| SI-7(1) | - | ✓ | ✓ | Integrity Checks |
| SI-7(7) | - | ✓ | ✓ | Integration of Detection and Response |
| SI-8 | - | ✓ | ✓ | Spam Protection |
| SI-10 | - | ✓ | ✓ | Information Input Validation |
| SI-12 | ✓ | ✓ | ✓ | Information Management and Retention |
| SI-16 | - | ✓ | ✓ | Memory Protection |

---

## SR - Supply Chain Risk Management (12 controls)

**Purpose:** Identify, assess, and mitigate risks from the supply chain (new family in Rev 5).

| Control | L | M | H | Description |
|---------|---|---|---|-------------|
| SR-1 | ✓ | ✓ | ✓ | Policy and Procedures |
| SR-2 | ✓ | ✓ | ✓ | Supply Chain Risk Management Plan (SCRM Plan) |
| SR-2(1) | ✓ | ✓ | ✓ | Establish SCRM Team |
| SR-3 | ✓ | ✓ | ✓ | Supply Chain Controls and Processes |
| SR-4 | - | ✓ | ✓ | Provenance |
| SR-5 | ✓ | ✓ | ✓ | Acquisition Strategies, Tools, and Methods |
| SR-6 | - | ✓ | ✓ | Supplier Assessments and Reviews |
| SR-6(1) | - | - | ✓ | Testing and Analysis |
| SR-7 | - | ✓ | ✓ | Supply Chain Operations Security |
| SR-8 | ✓ | ✓ | ✓ | Notification Agreements |
| SR-9 | - | - | ✓ | Tamper Resistance and Detection |
| SR-10 | ✓ | ✓ | ✓ | Inspection of Systems or Components |
| SR-11 | ✓ | ✓ | ✓ | Component Authenticity |
| SR-11(1) | ✓ | ✓ | ✓ | Anti-Counterfeit Training |
| SR-11(2) | ✓ | ✓ | ✓ | Configuration Control for Component Service and Repair |
| SR-12 | ✓ | ✓ | ✓ | Component Disposal |

**EO 14028 connection:** SR family implements software supply chain security requirements. SBOMs (Software Bill of Materials) support SR-3, SR-4, and SR-11.

---

## PM - Program Management (32 controls)

**Applies at the organizational level - not specific to any system baseline.**

| Control | Description |
|---------|-------------|
| PM-1 | Information Security Program Plan |
| PM-2 | Information Security Program Leadership Roles (CISO) |
| PM-5 | System Inventory |
| PM-7 | Enterprise Architecture |
| PM-8 | Critical Infrastructure Plan |
| PM-9 | Risk Management Strategy |
| PM-10 | Authorization Process |
| PM-11 | Mission and Business Process Definition |
| PM-12 | Insider Threat Program |
| PM-13 | Security Workforce |
| PM-14 | Testing, Training, and Monitoring |
| PM-15 | Security and Privacy Groups and Associations |
| PM-16 | Threat Awareness Program |
| PM-17 | Protecting Controlled Unclassified Information |
| PM-18 | Privacy Program Plan |
| PM-19 | Privacy Program Leadership Roles (CPO) |
| PM-20 | Dissemination of Privacy Program Information |
| PM-21 | Accounting for PII |
| PM-22 | Personally Identifiable Information Quality Management |
| PM-23 | Data Governance Body |
| PM-24 | Data Integrity Board |
| PM-25 | Minimization of PII Used in Testing, Training, and Research |
| PM-26 | Complaint Management |
| PM-27 | Privacy Reporting |
| PM-28 | Risk Framing |
| PM-29 | Risk Management Program Leadership Roles |
| PM-30 | Supply Chain Risk Management Strategy |
| PM-31 | Continuous Monitoring Strategy |
| PM-32 | Purposing |

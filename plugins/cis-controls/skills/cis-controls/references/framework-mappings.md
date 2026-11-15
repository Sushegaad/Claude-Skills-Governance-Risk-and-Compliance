# CIS Controls v8 - Framework Mapping Reference

## CIS Controls v8 ↔ NIST CSF 2.0 (Detailed)

| CIS Control | Safeguard | NIST CSF 2.0 Function | NIST CSF Category | NIST CSF Subcategory |
|------------|-----------|----------------------|-------------------|----------------------|
| 1.1 | Enterprise Asset Inventory | Identify | Asset Management (ID.AM) | ID.AM-01, ID.AM-02 |
| 1.2 | Address Unauthorized Assets | Respond | Incident Management (RS.MA) | RS.MA-01 |
| 2.1 | Software Inventory | Identify | Asset Management (ID.AM) | ID.AM-02, ID.AM-08 |
| 2.2 | Supported Software | Govern | Policy (GV.PO) | GV.PO-01 |
| 3.1 | Data Management Process | Govern | Policy (GV.PO) | GV.PO-01, GV.PO-02 |
| 3.3 | Data Access Control Lists | Protect | Identity Management, Authentication, and Access Control (PR.AA) | PR.AA-05 |
| 3.6 | Encrypt End-User Devices | Protect | Data Security (PR.DS) | PR.DS-01 |
| 3.10 | Encrypt Data in Transit | Protect | Data Security (PR.DS) | PR.DS-02 |
| 3.11 | Encrypt Data at Rest | Protect | Data Security (PR.DS) | PR.DS-01 |
| 3.13 | Data Loss Prevention | Protect | Data Security (PR.DS) | PR.DS-01, PR.DS-02 |
| 4.1 | Secure Configuration Process | Protect | Platform Security (PR.PS) | PR.PS-01 |
| 4.4 | Firewall on Servers | Protect | Network Security (PR.IR) | PR.IR-01 |
| 5.4 | Separate Admin Accounts | Protect | Identity Management (PR.AA) | PR.AA-05 |
| 6.3 | MFA External Applications | Protect | Identity Management (PR.AA) | PR.AA-03 |
| 6.4 | MFA Remote Access | Protect | Identity Management (PR.AA) | PR.AA-03 |
| 6.5 | MFA Admin Access | Protect | Identity Management (PR.AA) | PR.AA-05 |
| 7.3 | OS Patch Management | Protect | Platform Security (PR.PS) | PR.PS-02 |
| 7.5 | Internal Vulnerability Scans | Identify | Risk Assessment (ID.RA) | ID.RA-01 |
| 7.7 | Remediate Vulnerabilities | Protect | Platform Security (PR.PS) | PR.PS-02 |
| 8.2 | Collect Audit Logs | Detect | Adverse Event Analysis (DE.AE) | DE.AE-02, DE.AE-03 |
| 8.9 | Centralize Audit Logs | Detect | Adverse Event Analysis (DE.AE) | DE.AE-03 |
| 8.11 | Log Reviews | Detect | Continuous Monitoring (DE.CM) | DE.CM-09 |
| 9.3 | Network-Based URL Filters | Protect | Platform Security (PR.PS) | PR.PS (category level) |
| 9.5 | DMARC | Protect | Platform Security (PR.PS) | PR.PS (category level) |
| 10.1 | Anti-Malware | Protect | Platform Security (PR.PS) | PR.PS-05 |
| 10.7 | Behavior-Based AV | Detect | Continuous Monitoring (DE.CM) | DE.CM-09 |
| 11.2 | Automated Backups | Recover | Incident Recovery Plan (RC.RP) | RC.RP-05 |
| 11.4 | Isolated Backup Copy | Recover | Incident Recovery Plan (RC.RP) | RC.RP-05 |
| 12.2 | Secure Network Architecture | Protect | Network Security (PR.IR) | PR.IR-01, PR.IR-02 |
| 13.1 | Security Event Alerting | Detect | Adverse Event Analysis (DE.AE) | DE.AE-06 |
| 13.3 | Network Intrusion Detection | Detect | Continuous Monitoring (DE.CM) | DE.CM-01, DE.CM-06 |
| 14.1 | Security Awareness Program | Protect | Awareness and Training (PR.AT) | PR.AT-01, PR.AT-02 |
| 15.4 | Vendor Security Requirements | Govern | Supply Chain Risk Management (GV.SC) | GV.SC-05, GV.SC-07 |
| 16.1 | Secure Dev Process | Protect | Application Security (PR.PS) | PR.PS-04 |
| 17.4 | Incident Response Process | Respond | Incident Management (RS.MA) | RS.MA-01, RS.MA-02 |
| 17.7 | IR Exercises | Respond | Incident Management (RS.MA) | RS.MA-05 |
| 18.2 | External Pen Test | Identify | Risk Assessment (ID.RA) | ID.RA-05, ID.RA-06 |

---

## CIS Controls v8 ↔ ISO 27001:2022 Annex A (Detailed)

| CIS Control | CIS Safeguards | ISO 27001:2022 Controls |
|------------|----------------|-------------------------|
| **1 (Asset Inventory)** | 1.1, 1.2, 1.3 | 5.9 (Inventory of information and other associated assets), 8.8 (Management of technical vulnerabilities) |
| **2 (Software Inventory)** | 2.1, 2.2, 2.3 | 5.9 (Inventory), 8.8 (Technical vulnerabilities) |
| **3 (Data Protection)** | 3.1–3.14 | 5.12 (Classification), 5.13 (Labelling), 5.33 (Protection of records), 8.10 (Info deletion), 8.11 (Data masking), 8.24 (Use of cryptography) |
| **4 (Secure Config)** | 4.1–4.12 | 8.8 (Vulnerability management), 8.9 (Configuration management), 8.22 (Network segregation) |
| **5 (Account Management)** | 5.1–5.6 | 5.15 (Access control), 5.16 (Identity management), 5.18 (Access rights) |
| **6 (Access Control)** | 6.1–6.8 | 5.15 (Access control), 5.17 (Authentication info), 6.7 (Remote working), 8.2 (Privileged access rights), 8.3 (Info access restriction), 8.5 (Secure authentication) |
| **7 (Vulnerability Mgmt)** | 7.1–7.7 | 8.8 (Management of technical vulnerabilities) |
| **8 (Audit Logs)** | 8.1–8.12 | 8.15 (Logging), 8.16 (Monitoring activities), 8.17 (Clock synchronization) |
| **9 (Email/Web)** | 9.1–9.7 | 8.22 (Network segregation), 8.23 (Web filtering) |
| **10 (Malware)** | 10.1–10.7 | 8.7 (Protection against malware) |
| **11 (Data Recovery)** | 11.1–11.5 | 8.13 (Information backup), 8.14 (Redundancy) |
| **12 (Network Infra)** | 12.1–12.8 | 8.20 (Networks security), 8.21 (Security of network services), 8.22 (Network segregation) |
| **13 (Network Monitoring)** | 13.1–13.11 | 8.15 (Logging), 8.16 (Monitoring), 8.20 (Network security) |
| **14 (Security Training)** | 14.1–14.9 | 6.3 (Information security awareness/education/training), 6.8 (Information security event reporting) |
| **15 (Service Providers)** | 15.1–15.7 | 5.19 (Information security in supplier relationships), 5.20 (Addressing security in agreements), 5.21 (Managing security in ICT supply chain) |
| **16 (App Security)** | 16.1–16.14 | 8.25 (Secure development lifecycle), 8.26 (Application security requirements), 8.27 (Secure system architecture and engineering), 8.28 (Secure coding), 8.29 (Security testing in development/acceptance) |
| **17 (IR Management)** | 17.1–17.9 | 5.24 (IR planning and preparation), 5.25 (Assessment/decision on events), 5.26 (Response to incidents) |
| **18 (Pen Testing)** | 18.1–18.5 | 8.8 (Technical vulnerability management), 5.36 (Compliance with policies/standards) |

---

## CIS Controls v8 ↔ CMMC 2.0 (NIST SP 800-171)

| CIS Control | CMMC Domain | NIST 800-171 Requirements |
|------------|-------------|--------------------------|
| 1 (Asset Inventory) | Asset Management / System Inventory | Not explicitly in 800-171 but implied by CM.L2-3.4.1 (baseline configurations include system inventory) |
| 2 (Software Inventory) | Configuration Management (CM) | 3.4.1 (Baseline configurations), 3.4.2 (Configuration settings) |
| 3 (Data Protection) | Media Protection (MP) | 3.8.1–3.8.9 |
| 4 (Secure Config) | Configuration Management (CM) | 3.4.1, 3.4.2, 3.4.6, 3.4.7 |
| 5 (Account Management) | Identification & Authentication (IA) | 3.5.1, 3.5.2, 3.5.3 |
| 6 (Access Control) | Access Control (AC) | 3.1.1–3.1.22 |
| 7 (Vulnerability Mgmt) | Risk Assessment (RA) | 3.11.1, 3.11.2, 3.11.3 |
| 8 (Audit Logs) | Audit & Accountability (AU) | 3.3.1–3.3.9 |
| 9 (Email/Web) | System & Communications Protection (SC) | 3.13.6, 3.13.7 |
| 10 (Malware Defenses) | System & Information Integrity (SI) | 3.14.2, 3.14.4, 3.14.5 |
| 11 (Data Recovery) | Recovery not explicitly in 800-171 | 3.8.9 (Backup CUI on mobile devices) |
| 12 (Network Infra) | System & Communications Protection (SC) | 3.13.1, 3.13.2, 3.13.5 |
| 13 (Network Monitoring) | System & Information Integrity (SI) | 3.14.6, 3.14.7 |
| 14 (Security Training) | Awareness & Training (AT) | 3.2.1, 3.2.2, 3.2.3 |
| 15 (Service Providers) | Supply Chain Risk not explicitly in 800-171 | Implied by CM and SI |
| 16 (App Security) | System & Communications Protection (SC) | 3.13.10, 3.13.16 |
| 17 (Incident Response) | Incident Response (IR) | 3.6.1, 3.6.2, 3.6.3 |
| 18 (Pen Testing) | Not explicitly in CMMC L2, required at L3 | NIST SP 800-172: 3.12.1e |

---

## CIS Controls v8 ↔ SOC 2 Trust Services Criteria

| CIS Control | SOC 2 Criterion | TSC Category |
|------------|----------------|-------------|
| 1 (Asset Inventory) | CC6.1 | Common Criteria |
| 2 (Software Inventory) | CC6.1, CC6.2 | Common Criteria |
| 3 (Data Protection) | CC6.1, CC6.5, C1.1, C1.2 | Common Criteria / Confidentiality |
| 4 (Secure Config) | CC6.1, CC7.1 | Common Criteria |
| 5 (Account Management) | CC6.2, CC6.3 | Common Criteria |
| 6 (Access Control) | CC6.1, CC6.2, CC6.3 | Common Criteria |
| 7 (Vulnerability Mgmt) | CC7.1 | Common Criteria |
| 8 (Audit Logs) | CC4.1, CC7.2, CC7.3 | Common Criteria |
| 9 (Email/Web) | CC6.1, CC6.6 | Common Criteria |
| 10 (Malware) | CC6.1, CC6.8 | Common Criteria |
| 11 (Data Recovery) | A1.2, A1.3 | Availability |
| 12 (Network Infra) | CC6.1, CC6.6 | Common Criteria |
| 13 (Network Monitoring) | CC7.2, CC7.3 | Common Criteria |
| 14 (Security Training) | CC1.4, CC2.2 | Common Criteria |
| 15 (Service Providers) | CC9.2 | Common Criteria |
| 16 (App Security) | CC8.1 | Common Criteria |
| 17 (Incident Response) | CC7.3, CC7.4, CC7.5 | Common Criteria |
| 18 (Pen Testing) | CC4.1, CC4.2 | Common Criteria |

---

## CIS Controls v8 ↔ PCI DSS v4.0

| PCI DSS Requirement | CIS Controls |
|--------------------|-------------|
| Req 1: Install network controls | 12, 13 |
| Req 2: Secure system/network components | 4 |
| Req 3: Protect stored cardholder data | 3 |
| Req 4: Protect cardholder data in transit | 3.10 |
| Req 5: Protect against malicious software | 10 |
| Req 6: Develop/maintain secure systems | 16 |
| Req 7: Restrict access by business need | 6 |
| Req 8: Identify users and authenticate access | 5, 6 |
| Req 9: Restrict physical access | (Physical - not covered by CIS Controls) |
| Req 10: Log and monitor all access | 8 |
| Req 11: Test system/network security | 7, 18 |
| Req 12: Support information security | 1, 2, 14, 15, 17 |

---

## CIS Controls v7.1 vs v8 Changes

Key changes to understand if transitioning from v7.1 to v8:

| Aspect | CIS Controls v7.1 | CIS Controls v8 |
|--------|------------------|-----------------|
| Number of controls | 20 | 18 |
| Sub-controls | 171 | 153 safeguards |
| Organization | Technology type | Asset type |
| Cloud coverage | Limited | Explicit throughout |
| Mobile coverage | Limited | Integrated |
| Implementation Groups | Yes (IG1/2/3) | Yes (enhanced) |

**Controls merged/reorganized:**
- v7 Controls 4 (Controlled Use of Admin Privileges) + 16 (Account Monitoring) → v8 Control 5 (Account Management)
- v7 Controls 12 (Boundary Defense) + 13 (Data Protection) → v8 Controls 3 (Data Protection) + 12 (Network Infrastructure)
- v7 Controls 7 (Email/Web Browsers) + 8 (Malware Defenses) → v8 Controls 9 + 10

**New in v8:**
- Explicit cloud asset coverage in all applicable controls
- Service Provider Management as standalone Control 15
- Clearer Implementation Group assignments per safeguard

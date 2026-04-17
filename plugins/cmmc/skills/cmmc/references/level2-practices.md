# CMMC Level 2 — Advanced (110 Practices)
## Source: NIST SP 800-171 Rev 2 and CMMC 2.0 Final Rule (32 CFR Part 170)

---

## Overview

CMMC Level 2 applies to organizations that process, store, or transmit **Controlled
Unclassified Information (CUI)** in the performance of DoD contracts.

Level 2 requirements are **identical to NIST SP 800-171 Rev 2** across 14 domains and
110 security requirements (referred to as "practices" in the CMMC context).

**Assessment Type:**
- **C3PAO triennial assessment** — required for most CUI contracts (prioritized programs)
- **Self-assessment (annual)** — only when specifically designated by DoD for non-prioritized acquisitions

**Certificate Validity:** 3 years (triennial reassessment required)
**Annual Affirmation:** Required each year by a senior company official

---

## All 110 Level 2 Practices by Domain

### 1. Access Control (AC) — 22 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| AC.L2-3.1.1 | 3.1.1 | Authorized Access Control | Limit system access to authorized users, processes acting on behalf of authorized users, and devices |
| AC.L2-3.1.2 | 3.1.2 | Transaction & Function Control | Limit system access to the types of transactions and functions that authorized users are permitted to execute |
| AC.L2-3.1.3 | 3.1.3 | Control CUI Flow | Control the flow of CUI in accordance with approved authorizations |
| AC.L2-3.1.4 | 3.1.4 | Separation of Duties | Separate the duties of individuals to reduce the risk of malevolent activity |
| AC.L2-3.1.5 | 3.1.5 | Least Privilege | Employ the principle of least privilege, including for specific security functions and privileged accounts |
| AC.L2-3.1.6 | 3.1.6 | Non-Privileged Account Use | Use non-privileged accounts or roles when accessing non-security functions |
| AC.L2-3.1.7 | 3.1.7 | Privileged Function Execution | Prevent non-privileged users from executing privileged functions and capture the execution in audit logs |
| AC.L2-3.1.8 | 3.1.8 | Unsuccessful Logon Attempts | Limit unsuccessful logon attempts |
| AC.L2-3.1.9 | 3.1.9 | Privacy & Security Notices | Provide privacy and security notices consistent with CUI rules |
| AC.L2-3.1.10 | 3.1.10 | Session Lock | Use session lock with pattern-hiding displays after a period of inactivity |
| AC.L2-3.1.11 | 3.1.11 | Session Termination | Terminate (automatically) a user session after a defined condition |
| AC.L2-3.1.12 | 3.1.12 | Control Remote Access | Monitor and control remote access sessions |
| AC.L2-3.1.13 | 3.1.13 | Remote Access Confidentiality | Employ cryptographic mechanisms to protect the confidentiality of remote access sessions |
| AC.L2-3.1.14 | 3.1.14 | Remote Access Routing | Route remote access via managed access control points |
| AC.L2-3.1.15 | 3.1.15 | Privileged Remote Access | Authorize remote execution of privileged commands via remote access only for documented operational needs |
| AC.L2-3.1.16 | 3.1.16 | Wireless Access Authorization | Authorize wireless access prior to allowing connections to the system |
| AC.L2-3.1.17 | 3.1.17 | Wireless Access Protection | Protect wireless access using authentication and encryption |
| AC.L2-3.1.18 | 3.1.18 | Mobile Device Connection | Control connection of mobile devices |
| AC.L2-3.1.19 | 3.1.19 | Encrypt CUI on Mobile | Encrypt CUI on mobile devices and mobile computing platforms |
| AC.L2-3.1.20 | 3.1.20 | External System Connections | Verify and control/limit connections to external information systems |
| AC.L2-3.1.21 | 3.1.21 | Portable Storage Use | Limit use of portable storage devices on external systems |
| AC.L2-3.1.22 | 3.1.22 | Control Public Information | Control information posted or processed on publicly accessible information systems |

### 2. Audit and Accountability (AU) — 9 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| AU.L2-3.3.1 | 3.3.1 | System Auditing | Create and retain system audit logs and records to enable monitoring, analysis, investigation, and reporting of unlawful or unauthorized activity |
| AU.L2-3.3.2 | 3.3.2 | User Accountability | Ensure that the actions of individual system users can be uniquely traced to those users so they can be held accountable |
| AU.L2-3.3.3 | 3.3.3 | Event Review | Review and update logged events |
| AU.L2-3.3.4 | 3.3.4 | Audit Failure Alerting | Alert in the event of an audit logging process failure |
| AU.L2-3.3.5 | 3.3.5 | Audit Correlation | Correlate audit record review, analysis, and reporting processes for investigation and response |
| AU.L2-3.3.6 | 3.3.6 | Reduction & Reporting | Provide audit record reduction and report generation to support on-demand analysis and reporting |
| AU.L2-3.3.7 | 3.3.7 | Authoritative Time Source | Provide a system capability that compares and synchronizes internal system clocks with an authoritative source |
| AU.L2-3.3.8 | 3.3.8 | Audit Protection | Protect audit information and tools from unauthorized access, modification, and deletion |
| AU.L2-3.3.9 | 3.3.9 | Audit Management | Limit management of audit logs to a subset of privileged users |

### 3. Awareness and Training (AT) — 3 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| AT.L2-3.2.1 | 3.2.1 | Role-Based Risk Awareness | Ensure that managers, systems administrators, and users of organizational systems are made aware of the security risks associated with their activities |
| AT.L2-3.2.2 | 3.2.2 | Role-Based Training | Ensure that organizational personnel are adequately trained to carry out their assigned information security responsibilities |
| AT.L2-3.2.3 | 3.2.3 | Insider Threat Awareness | Provide security awareness training on recognizing and reporting potential threats (including insider threats) |

### 4. Configuration Management (CM) — 9 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| CM.L2-3.4.1 | 3.4.1 | System Baselining | Establish and maintain baseline configurations and inventories of organizational systems (hardware, software, firmware, network components) |
| CM.L2-3.4.2 | 3.4.2 | Security Configuration Enforcement | Establish and enforce security configuration settings for IT products employed in organizational systems |
| CM.L2-3.4.3 | 3.4.3 | System Change Control | Track, review, approve, and log changes to organizational systems |
| CM.L2-3.4.4 | 3.4.4 | Security Impact Analysis | Analyze the security impact of changes prior to implementation |
| CM.L2-3.4.5 | 3.4.5 | Access Restrictions for Change | Define, document, approve, and enforce physical and logical access restrictions associated with changes |
| CM.L2-3.4.6 | 3.4.6 | Least Functionality | Employ the principle of least functionality by configuring the system to provide only essential capabilities |
| CM.L2-3.4.7 | 3.4.7 | Nonessential Functionality | Restrict, disable, or prevent the use of nonessential programs, functions, ports, protocols, and services |
| CM.L2-3.4.8 | 3.4.8 | Application Execution Policy | Apply deny-by-exception (blacklisting) policy to prevent the use of unauthorized software or application execution |
| CM.L2-3.4.9 | 3.4.9 | User-Installed Software | Control and monitor user-installed software |

### 5. Identification and Authentication (IA) — 11 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| IA.L2-3.5.1 | 3.5.1 | Identification | Identify information system users, processes acting on behalf of users, or devices |
| IA.L2-3.5.2 | 3.5.2 | Authentication | Authenticate (or verify) the identities of users, processes, or devices before allowing access |
| IA.L2-3.5.3 | 3.5.3 | Multifactor Authentication — Privileged | Use multifactor authentication for local and network access to privileged accounts and for network access to non-privileged accounts |
| IA.L2-3.5.4 | 3.5.4 | Replay-Resistant Authentication | Employ replay-resistant authentication mechanisms for network access to privileged and non-privileged accounts |
| IA.L2-3.5.5 | 3.5.5 | Identifier Reuse | Prohibit reuse of identifiers for a defined period |
| IA.L2-3.5.6 | 3.5.6 | Identifier Handling | Disable identifiers after a defined inactivity period |
| IA.L2-3.5.7 | 3.5.7 | Password Complexity | Enforce a minimum password complexity and change of characters when new passwords are created |
| IA.L2-3.5.8 | 3.5.8 | Password Reuse | Prohibit password reuse for a specified number of generations |
| IA.L2-3.5.9 | 3.5.9 | Temporary Passwords | Allow temporary password use with an immediate change requirement |
| IA.L2-3.5.10 | 3.5.10 | Cryptographically-Protected Passwords | Store and transmit only cryptographically-protected passwords |
| IA.L2-3.5.11 | 3.5.11 | Obscure Feedback | Obscure feedback of authentication information during the authentication process |

### 6. Incident Response (IR) — 3 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| IR.L2-3.6.1 | 3.6.1 | Incident Handling | Establish an operational incident-handling capability for organizational systems including: preparation, detection, analysis, containment, recovery, and user response activities |
| IR.L2-3.6.2 | 3.6.2 | Incident Reporting | Track, document, and report incidents to appropriate organizational officials and/or authorities |
| IR.L2-3.6.3 | 3.6.3 | Incident Response Testing | Test the organizational incident response capability |

**Note on DFARS 252.204-7012:** Contractors that discover a cyber incident on a covered
contractor information system must:
- Report to DoD at https://dibnet.dod.mil within **72 hours** of discovery
- Preserve and protect images of all known affected systems for **90 days**
- Submit a malware sample (if discovered) to the DoD Cyber Crime Center (DC3)
- Cooperate with DoD damage assessment activities

### 7. Maintenance (MA) — 6 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| MA.L2-3.7.1 | 3.7.1 | Managed Maintenance | Perform maintenance on organizational systems |
| MA.L2-3.7.2 | 3.7.2 | Maintenance Tools | Provide controls on the tools, techniques, mechanisms, and personnel for system maintenance |
| MA.L2-3.7.3 | 3.7.3 | Equipment Sanitization | Ensure equipment removed for maintenance is sanitized with respect to CUI |
| MA.L2-3.7.4 | 3.7.4 | Media Inspection | Check media containing diagnostic and test programs for malicious code before used on systems |
| MA.L2-3.7.5 | 3.7.5 | Nonlocal Maintenance | Require MFA to establish nonlocal maintenance sessions and terminate when session is complete |
| MA.L2-3.7.6 | 3.7.6 | Maintenance Personnel | Supervise maintenance activities of personnel without required access authorization |

### 8. Media Protection (MP) — 9 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| MP.L2-3.8.1 | 3.8.1 | Media Protection | Protect (i.e., physically control and securely store) system media containing CUI, both paper and digital |
| MP.L2-3.8.2 | 3.8.2 | Media Access | Limit access to CUI on system media to authorized users |
| MP.L2-3.8.3 | 3.8.3 | Media Disposal | Sanitize or destroy system media before disposal or reuse |
| MP.L2-3.8.4 | 3.8.4 | Media Markings | Mark media with necessary CUI markings and distribution limitations |
| MP.L2-3.8.5 | 3.8.5 | Media Accountability | Control access to media containing CUI and maintain accountability for media during transport |
| MP.L2-3.8.6 | 3.8.6 | Portable Storage Encryption | Implement cryptographic mechanisms to protect the confidentiality of CUI during transport unless protected by alternative physical safeguards |
| MP.L2-3.8.7 | 3.8.7 | Removable Media Control | Control the use of removable media on system components |
| MP.L2-3.8.8 | 3.8.8 | Shared Media | Prohibit the use of portable storage devices when such devices have no identifiable owner |
| MP.L2-3.8.9 | 3.8.9 | CUI Protection at Backup Locations | Protect the confidentiality of backup CUI at storage locations |

### 9. Personnel Security (PS) — 2 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| PS.L2-3.9.1 | 3.9.1 | Screen Individuals | Screen individuals prior to authorizing access to organizational systems containing CUI |
| PS.L2-3.9.2 | 3.9.2 | Termination & Transfer | Ensure that organizational systems containing CUI are protected during and after personnel actions such as terminations and transfers |

### 10. Physical Protection (PE) — 6 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| PE.L2-3.10.1 | 3.10.1 | Limit Physical Access | Limit physical access to organizational systems, equipment, and operating environments to authorized individuals |
| PE.L2-3.10.2 | 3.10.2 | Protect & Monitor Physical Facility | Protect and monitor the physical facility and support infrastructure for organizational systems |
| PE.L2-3.10.3 | 3.10.3 | Escort Visitors | Escort visitors and monitor visitor activity |
| PE.L2-3.10.4 | 3.10.4 | Audit Physical Access | Maintain audit logs of physical access |
| PE.L2-3.10.5 | 3.10.5 | Manage Physical Access | Control and manage physical access devices |
| PE.L2-3.10.6 | 3.10.6 | Alternative Work Sites | Enforce safeguarding measures for CUI at alternate work sites |

### 11. Risk Assessment (RA) — 3 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| RA.L2-3.11.1 | 3.11.1 | Risk Assessments | Periodically assess the risk to organizational operations, assets, and individuals resulting from the operation of organizational systems and the associated processing, storing, or transmitting of CUI |
| RA.L2-3.11.2 | 3.11.2 | Vulnerability Scan | Periodically scan for vulnerabilities in organizational systems and applications; remediate high vulnerabilities |
| RA.L2-3.11.3 | 3.11.3 | Vulnerability Remediation | Remediate vulnerabilities in accordance with risk assessments |

### 12. Security Assessment (CA) — 4 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| CA.L2-3.12.1 | 3.12.1 | System Security Assessment | Periodically assess the security controls in organizational systems to determine if the controls are effective |
| CA.L2-3.12.2 | 3.12.2 | Plan of Action | Develop and implement plans of action designed to correct deficiencies and reduce or eliminate vulnerabilities |
| CA.L2-3.12.3 | 3.12.3 | Security Control Monitoring | Monitor security controls on an ongoing basis to ensure the continued effectiveness |
| CA.L2-3.12.4 | 3.12.4 | System Security Plan | Develop, document, and periodically update system security plans that describe system boundaries, system environments of operation, how security requirements are implemented, and relationships with other systems |

### 13. System and Communications Protection (SC) — 16 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| SC.L2-3.13.1 | 3.13.1 | Boundary Protection | Monitor, control, and protect communications at external and key internal boundaries |
| SC.L2-3.13.2 | 3.13.2 | Security Engineering | Employ architectural designs, software development techniques, and systems engineering principles promoting security effectiveness |
| SC.L2-3.13.3 | 3.13.3 | Role Separation | Separate user functionality from system management functionality |
| SC.L2-3.13.4 | 3.13.4 | Shared Resource Control | Prevent unauthorized and unintended information transfer via shared system resources |
| SC.L2-3.13.5 | 3.13.5 | Public-Access System Separation | Implement subnetworks for publicly accessible system components, separated from internal networks |
| SC.L2-3.13.6 | 3.13.6 | Network Communication Denial | Deny network communications traffic by default; allow by exception (deny-all, permit-by-exception) |
| SC.L2-3.13.7 | 3.13.7 | Split Tunneling | Prevent remote devices from simultaneously using VPN tunneling to connect simultaneously to the system and to resources in other domains |
| SC.L2-3.13.8 | 3.13.8 | Data in Transit | Implement cryptographic mechanisms to prevent unauthorized disclosure of CUI during transmission |
| SC.L2-3.13.9 | 3.13.9 | Connections Termination | Terminate network connections after a defined period of inactivity |
| SC.L2-3.13.10 | 3.13.10 | Key Management | Establish and manage cryptographic keys for required cryptography employed in organizational systems |
| SC.L2-3.13.11 | 3.13.11 | CUI Encryption | Employ FIPS-validated cryptography when used to protect the confidentiality of CUI |
| SC.L2-3.13.12 | 3.13.12 | Collaborative Computing Devices | Prohibit remote activation of collaborative computing devices and provide indication of use to users present |
| SC.L2-3.13.13 | 3.13.13 | Mobile Code | Control and monitor the use of mobile code |
| SC.L2-3.13.14 | 3.13.14 | VoIP Technologies | Control and monitor the use of VoIP technologies |
| SC.L2-3.13.15 | 3.13.15 | Communications Authenticity | Protect the authenticity of communications sessions |
| SC.L2-3.13.16 | 3.13.16 | CUI at Rest | Protect the confidentiality of CUI at rest |

### 14. System and Information Integrity (SI) — 7 Practices

| Practice ID | NIST Ref | Practice Title | Description |
|------------|----------|---------------|-------------|
| SI.L2-3.14.1 | 3.14.1 | Flaw Remediation | Identify, report, and correct information and system flaws in a timely manner |
| SI.L2-3.14.2 | 3.14.2 | Malicious Code Protection | Provide protection from malicious code at appropriate locations within organizational systems |
| SI.L2-3.14.3 | 3.14.3 | Security Alerts | Monitor system security alerts and advisories and take action in response |
| SI.L2-3.14.4 | 3.14.4 | Update Malicious Code Protection | Update malicious code protection mechanisms when new releases are available |
| SI.L2-3.14.5 | 3.14.5 | System Scanning | Perform periodic scans of the system and real-time scans of files from external sources |
| SI.L2-3.14.6 | 3.14.6 | Security Monitoring | Monitor the system to detect attacks and indicators of potential attacks |
| SI.L2-3.14.7 | 3.14.7 | Identify Unauthorized Use | Identify unauthorized use of organizational systems |

---

## SPRS Score Deduction Reference

The NIST SP 800-171 DoD Assessment Methodology assigns deduction values to each practice.
Below are the deduction weights (not implemented = subtract from 110):

**High-impact deductions (-5 each):**
AC.L2-3.1.3, AC.L2-3.1.5, AC.L2-3.1.12, AC.L2-3.1.13, AC.L2-3.1.14,
IA.L2-3.5.3, SC.L2-3.13.8, SC.L2-3.13.11, SC.L2-3.13.16

**Medium-impact deductions (-3 each):**
AC.L2-3.1.1, AC.L2-3.1.2, AU.L2-3.3.1, AU.L2-3.3.2, CA.L2-3.12.4,
CM.L2-3.4.1, CM.L2-3.4.2, IA.L2-3.5.1, IA.L2-3.5.2, IA.L2-3.5.7,
IR.L2-3.6.1, RA.L2-3.11.2, SC.L2-3.13.1, SC.L2-3.13.6, SI.L2-3.14.1,
SI.L2-3.14.2, SI.L2-3.14.5, SI.L2-3.14.6

**Low-impact deductions (-1 each):** All remaining 83 practices

---

## Key Evidence Requirements for C3PAO Assessment

| Domain | Critical Evidence |
|--------|-----------------|
| AC | User account list, access control policy, session lock configuration, VPN configuration |
| AU | Audit log configuration, log retention settings, SIEM deployment, NTP configuration |
| AT | Training completion records (dated, named), training content for all roles |
| CM | System inventory, configuration baselines, change management records, approved software list |
| IA | MFA deployment configuration, password policy, account review records |
| IR | Incident response plan, test records (tabletop or drill), DIBNET cybersecurity portal registration |
| MA | Maintenance logs, remote maintenance session records, equipment sanitization records |
| MP | Media inventory, encryption configuration for portable media, disposal certificates |
| PS | Background check records, termination/transfer checklist completion records |
| PE | Physical access log, badge records, visitor log, alternative work site policy |
| RA | Risk assessment report (dated), vulnerability scan reports, remediation tracking |
| CA | Security assessment report, POA&M (current), SSP (current) |
| SC | Firewall rules, network diagram, encryption certificates, VPN configuration |
| SI | Patch management reports, AV/EDR console screenshots, security alert process documentation |

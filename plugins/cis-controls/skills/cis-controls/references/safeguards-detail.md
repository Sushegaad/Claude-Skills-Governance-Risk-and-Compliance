# CIS Controls v8 - All 153 Safeguards Detail

## How to Use This Reference

Each safeguard entry shows:
- **Safeguard ID:** CIS Control # . Safeguard #
- **Title:** Official CIS safeguard name
- **IG:** Minimum implementation group (1, 2, or 3)
- **Asset Type:** Devices / Software / Data / Users / Network / Applications
- **Security Function:** Govern / Identify / Protect / Detect / Respond / Recover
- **Implementation Notes:** Practical guidance on what to do

---

## CIS Control 1: Inventory and Control of Enterprise Assets

| Safeguard | Title | IG | Asset Type | Security Function |
|-----------|-------|-----|-----------|------------------|
| 1.1 | Establish and Maintain Detailed Enterprise Asset Inventory | 1 | Devices | Identify |
| 1.2 | Address Unauthorized Assets | 1 | Devices | Respond |
| 1.3 | Utilize an Active Discovery Tool | 2 | Devices | Identify |
| 1.4 | Use Dynamic Host Configuration Protocol (DHCP) Logging to Update Enterprise Asset Inventory | 2 | Devices | Identify |
| 1.5 | Use a Passive Asset Discovery Tool | 3 | Devices | Identify |

**Implementation Notes:**
- **1.1:** Maintain inventory in a CMDB, spreadsheet, or MDM tool. Include: IP address, hostname, MAC address, owner, location, OS, asset type, acquisition date
- **1.2:** Define a process for handling unauthorized devices found on network - quarantine, investigate, document
- **1.3:** Run network scanners (Nmap, Nessus, Qualys, Tenable) on scheduled basis (weekly minimum)
- **1.4:** Enable DHCP server logging; correlate logs with asset inventory; flag unknown MACs
- **1.5:** Deploy passive network TAP or IDS/NDR sensors for continuous asset detection without active scanning

**Recommended Tools:** Microsoft Intune, CrowdStrike Falcon, Tanium, Qualys VMDR, Nessus, Axonius, ServiceNow CMDB

---

## CIS Control 2: Inventory and Control of Software Assets

| Safeguard | Title | IG | Asset Type | Security Function |
|-----------|-------|-----|-----------|------------------|
| 2.1 | Establish and Maintain a Software Inventory | 1 | Applications | Identify |
| 2.2 | Ensure Authorized Software is Currently Supported | 1 | Applications | Protect |
| 2.3 | Address Unauthorized Software | 1 | Applications | Respond |
| 2.4 | Utilize Automated Software Inventory Tools | 2 | Applications | Identify |
| 2.5 | Allowlist Authorized Software | 2 | Applications | Protect |
| 2.6 | Allowlist Authorized Libraries | 2 | Applications | Protect |
| 2.7 | Allowlist Authorized Scripts | 3 | Applications | Protect |

**Implementation Notes:**
- **2.1:** Track all installed software: name, version, vendor, license, install date, responsible owner
- **2.2:** Identify software nearing end-of-support (EOS/EOL); plan upgrades before EOS date
- **2.3:** Detect and remove unauthorized software; consider policy/consequence for installing unauthorized tools
- **2.5:** Implement application allowlisting via Windows AppLocker, WDAC, or endpoint agents
- **2.6:** Track approved DLL, library, and package versions; use software composition analysis (SCA) for development
- **2.7:** Control scripting environments (PowerShell Constrained Language Mode, Python virtual environments)

**Recommended Tools:** Microsoft Intune, SCCM, Tanium, Flexera, Snyk (SCA), Veracode, AppLocker

---

## CIS Control 3: Data Protection

| Safeguard | Title | IG | Asset Type | Security Function |
|-----------|-------|-----|-----------|------------------|
| 3.1 | Establish and Maintain a Data Management Process | 1 | Data | Govern |
| 3.2 | Establish and Maintain a Data Inventory | 1 | Data | Identify |
| 3.3 | Configure Data Access Control Lists | 1 | Data | Protect |
| 3.4 | Enforce Data Retention | 1 | Data | Protect |
| 3.5 | Securely Dispose of Data | 1 | Data | Protect |
| 3.6 | Encrypt Data on End-User Devices | 1 | Data | Protect |
| 3.7 | Establish and Maintain a Data Classification Scheme | 2 | Data | Protect |
| 3.8 | Document Data Flows | 2 | Data | Identify |
| 3.9 | Encrypt Data on Removable Media | 2 | Data | Protect |
| 3.10 | Encrypt Sensitive Data in Transit | 2 | Data | Protect |
| 3.11 | Encrypt Sensitive Data at Rest | 2 | Data | Protect |
| 3.12 | Segment Data Processing and Storage Based on Sensitivity | 2 | Data | Protect |
| 3.13 | Deploy a Data Loss Prevention Solution | 3 | Data | Protect |
| 3.14 | Log Sensitive Data Access | 3 | Data | Detect |

**Implementation Notes:**
- **3.1:** Written policy covering classification, handling, retention, disposal - reviewed annually
- **3.2:** Inventory must include: data type, sensitivity, location (on-prem/cloud), owner, retention period
- **3.3:** Implement least-privilege on file shares, databases, cloud storage; review ACLs quarterly
- **3.6:** Enable full-disk encryption (BitLocker for Windows, FileVault for macOS, LUKS for Linux)
- **3.7:** Define classification labels: e.g., Public / Internal / Confidential / Restricted
- **3.10:** Enforce TLS 1.2+ for all data in transit; disable older protocols (SSL, TLS 1.0/1.1)
- **3.11:** Encrypt databases, backups, and file stores containing sensitive data
- **3.13:** Deploy DLP on email, endpoints, and cloud services to prevent data exfiltration

**Recommended Tools:** Microsoft Purview, Varonis, Symantec DLP, Zscaler, BitLocker, Vera (Digital Guardian)

---

## CIS Control 4: Secure Configuration

| Safeguard | Title | IG | Asset Type | Security Function |
|-----------|-------|-----|-----------|------------------|
| 4.1 | Establish and Maintain a Secure Configuration Process | 1 | Devices | Protect |
| 4.2 | Establish and Maintain a Secure Configuration Process for Network Infrastructure | 1 | Network | Protect |
| 4.3 | Configure Automatic Session Locking on Enterprise Assets | 1 | Devices/Users | Protect |
| 4.4 | Implement and Manage a Firewall on Servers | 1 | Devices | Protect |
| 4.5 | Implement and Manage a Firewall on End-User Devices | 1 | Devices | Protect |
| 4.6 | Securely Manage Enterprise Assets and Software | 1 | Devices | Protect |
| 4.7 | Manage Default Accounts on Enterprise Assets and Software | 1 | Users | Protect |
| 4.8 | Uninstall or Disable Unnecessary Services on Enterprise Assets | 2 | Devices | Protect |
| 4.9 | Configure Trusted DNS Servers on Enterprise Assets | 2 | Devices/Network | Protect |
| 4.10 | Enforce Automatic Device Lockout on Portable End-User Devices | 2 | Devices | Protect |
| 4.11 | Enforce Remote Wipe Capability on Portable End-User Devices | 2 | Devices | Protect |
| 4.12 | Separate Enterprise Workspaces on Mobile End-User Devices | 3 | Devices | Protect |

**Implementation Notes:**
- **4.1:** Use CIS Benchmarks as configuration baseline; automate hardening via Group Policy, Ansible, Chef, Puppet
- **4.2:** Apply router/switch hardening; disable unused ports, protocols, and services on network devices
- **4.3:** Set session timeout to 15 minutes or less; enforce screensaver lock via GPO/MDM
- **4.4:** Enable Windows Firewall or host-based firewall on all servers; define least-privilege inbound/outbound rules
- **4.7:** Rename or disable default admin accounts; change all default passwords immediately upon deployment
- **4.8:** Disable/uninstall: Telnet, FTP, rsh, RPC where not needed; audit running services quarterly

**CIS Benchmark Resources:** Free hardening guides available at cisecurity.org/benchmark for Windows, Linux, macOS, AWS, Azure, GCP, Kubernetes, Docker, browsers

---

## CIS Control 5: Account Management

| Safeguard | Title | IG | Asset Type | Security Function |
|-----------|-------|-----|-----------|------------------|
| 5.1 | Establish and Maintain an Inventory of Accounts | 1 | Users | Identify |
| 5.2 | Use Unique Passwords | 1 | Users | Protect |
| 5.3 | Disable Dormant Accounts | 1 | Users | Protect |
| 5.4 | Restrict Administrator Privileges to Dedicated Administrator Accounts | 1 | Users | Protect |
| 5.5 | Establish and Maintain an Inventory of Service Accounts | 2 | Users | Identify |
| 5.6 | Centralize Account Management | 2 | Users | Protect |

**Implementation Notes:**
- **5.1:** Inventory: all user, admin, service, and guest accounts across all systems
- **5.2:** Password policy: minimum 14 characters (or MFA required); check against breached password databases (HaveIBeenPwned); use password manager
- **5.3:** Disable accounts unused for 90 days; automate detection via IdP reporting
- **5.4:** Never use admin accounts for daily work; separate admin credentials; use PAM solutions for privileged access
- **5.5:** Service accounts: document purpose, owner, permissions; rotate passwords regularly
- **5.6:** Use Active Directory, Azure AD/Entra ID, Okta, or similar IdP as single source of truth

---

## CIS Control 6: Access Control Management

| Safeguard | Title | IG | Asset Type | Security Function |
|-----------|-------|-----|-----------|------------------|
| 6.1 | Establish an Access Granting Process | 1 | Users | Protect |
| 6.2 | Establish an Access Revoking Process | 1 | Users | Protect |
| 6.3 | Require MFA for Externally-Exposed Applications | 1 | Users | Protect |
| 6.4 | Require MFA for Remote Network Access | 1 | Users | Protect |
| 6.5 | Require MFA for Administrative Access | 1 | Users | Protect |
| 6.6 | Establish and Maintain an Inventory of Authentication/Authorization Systems | 2 | Users | Identify |
| 6.7 | Centralize Access Control | 2 | Users | Protect |
| 6.8 | Define and Maintain Role-Based Access Control | 3 | Users | Protect |

**Implementation Notes:**
- **6.1/6.2:** Formal access request and approval process; link to onboarding/offboarding procedures; review quarterly
- **6.3:** MFA on all SaaS, web portals, VPN, RDP - phishing-resistant MFA (FIDO2/passkeys) preferred over SMS OTP
- **6.5:** Require MFA for all admin console access (cloud management, AD, network devices)
- **6.8:** Define roles in RBAC model; avoid overly broad permissions; apply least-privilege principle

---

## CIS Control 7: Continuous Vulnerability Management

| Safeguard | Title | IG | Asset Type | Security Function |
|-----------|-------|-----|-----------|------------------|
| 7.1 | Establish and Maintain a Vulnerability Management Process | 1 | Devices/Apps | Protect |
| 7.2 | Establish and Maintain a Remediation Process | 1 | Devices/Apps | Respond |
| 7.3 | Perform Automated Operating System Patch Management | 1 | Devices | Protect |
| 7.4 | Perform Automated Application Patch Management | 1 | Applications | Protect |
| 7.5 | Perform Automated Vulnerability Scans of Internal Enterprise Assets | 2 | Devices | Identify |
| 7.6 | Perform Automated Vulnerability Scans of Externally Exposed Enterprise Assets | 2 | Devices/Network | Identify |
| 7.7 | Remediate Detected Vulnerabilities | 2 | Devices/Apps | Respond |

**Remediation SLAs (common industry standards):**
| CVSS Severity | Recommended Remediation Time |
|---------------|------------------------------|
| Critical (9.0–10.0) | 15 days |
| High (7.0–8.9) | 30 days |
| Medium (4.0–6.9) | 90 days |
| Low (0.1–3.9) | 180 days or risk accepted |

**Recommended Tools:** Qualys VMDR, Tenable Nessus/io, Rapid7 InsightVM, Microsoft Defender Vulnerability Management, CrowdStrike Spotlight

---

## CIS Control 8: Audit Log Management

| Safeguard | Title | IG | Asset Type | Security Function |
|-----------|-------|-----|-----------|------------------|
| 8.1 | Establish and Maintain an Audit Log Management Process | 1 | Network/Devices | Protect |
| 8.2 | Collect Audit Logs | 1 | Network/Devices | Detect |
| 8.3 | Ensure Adequate Audit Log Storage | 1 | Network/Devices | Protect |
| 8.4 | Standardize Time Synchronization | 2 | Network/Devices | Protect |
| 8.5 | Collect Detailed Audit Logs | 2 | Network/Devices | Detect |
| 8.6 | Collect DNS Query Audit Logs | 2 | Network | Detect |
| 8.7 | Collect URL Request Audit Logs | 2 | Network | Detect |
| 8.8 | Collect Command-Line Audit Logs | 2 | Devices | Detect |
| 8.9 | Centralize Audit Logs | 2 | Network/Devices | Detect |
| 8.10 | Retain Audit Logs | 2 | Network/Devices | Protect |
| 8.11 | Conduct Audit Log Reviews | 2 | Network/Devices | Detect |
| 8.12 | Collect Service Provider Logs | 3 | Data/Network | Detect |

**Minimum Log Retention:** 90 days hot (searchable), 1 year cold storage (regulatory minimum varies)
**Recommended Tools:** Splunk, Microsoft Sentinel, Elastic SIEM, Sumo Logic, IBM QRadar

---

## CIS Controls 9–18 Summary (Selected Key Safeguards)

### Control 9: Email and Web Browser Protections
- 9.3 (IG2): Maintain and enforce network-based URL filters
- 9.5 (IG2): Implement DMARC anti-spoofing policy (p=quarantine or p=reject, with SPF and DKIM)

### Control 10: Malware Defenses
- 10.1 (IG1): Deploy/maintain anti-malware on all endpoints
- 10.7 (IG2): Use behavior-based/next-gen anti-malware (EDR)

### Control 11: Data Recovery
- 11.2 (IG1): Automated backups on schedule; test restores quarterly
- 11.4 (IG1): Store backup copy isolated/offline (3-2-1 rule)

### Control 12: Network Infrastructure Management
- 12.1 (IG1): Keep network devices firmware/OS current
- 12.7 (IG2): Require VPN for remote access with AAA

### Control 13: Network Monitoring and Defense
- 13.1 (IG2): Centralize security event alerting (SIEM)
- 13.3 (IG2): Deploy NIDS/NIPS or NDR solution
- 13.7/13.8 (IG3): HIPS/NIPS for active blocking

### Control 14: Security Awareness Training
- 14.2 (IG1): Annual phishing awareness training; quarterly simulations (IG2+)
- 14.6 (IG1): Train employees to recognize and report incidents

### Control 15: Service Provider Management
- 15.1 (IG1): Inventory of all service providers with data access
- 15.4 (IG2): Contracts must include security requirements
- 15.5 (IG2): Annual risk assessment of critical service providers

### Control 16: Application Software Security
- 16.9 (IG2): Developer security training (OWASP Top 10)
- 16.12 (IG3): SAST/DAST/IAST integrated in CI/CD pipeline

### Control 17: Incident Response Management
- 17.4 (IG2): Document incident response process; test annually
- 17.7 (IG2): Conduct tabletop exercises; include ransomware scenarios

### Control 18: Penetration Testing
- 18.2 (IG2): Annual external penetration test by qualified third party
- 18.5 (IG3): Quarterly internal pen tests; red team exercises

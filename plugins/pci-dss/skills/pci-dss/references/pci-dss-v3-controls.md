# PCI DSS v3.2.1 — Complete Control Structure

Source: PCI DSS v3.2.1 (PCI Security Standards Council, May 2018)
Note: PCI DSS v3.2.1 was RETIRED on March 31, 2024. No live compliance assessment may be conducted against this version. This reference is provided for:
- Legacy gap-analysis and migration planning (v3.2.1 → v4.0.1)
- Reviewing prior-year assessment documentation
- Understanding the baseline an organisation was compliant against before migrating to v4.0.1

For mapping of changes from v3.2.1 to v4.0.1, consult `references/pci-dss-v4-changes.md`.

---

## v3.2.1 Requirement Count Summary

| Requirement | Title | Sub-Requirements |
|-------------|-------|-----------------|
| 1 | Install and maintain a firewall configuration | ~21 |
| 2 | Do not use vendor-supplied defaults | ~8 |
| 3 | Protect stored cardholder data | ~22 |
| 4 | Encrypt transmission of cardholder data | ~4 |
| 5 | Protect all systems against malware | ~8 |
| 6 | Develop and maintain secure systems | ~22 |
| 7 | Restrict access to system components and cardholder data | ~6 |
| 8 | Identify and authenticate access | ~22 |
| 9 | Restrict physical access | ~15 |
| 10 | Track and monitor all access to network resources | ~15 |
| 11 | Regularly test security systems and processes | ~14 |
| 12 | Maintain a policy that addresses information security | ~20 |
| **Total** | | **~259** |

---

## GOAL 1: Build and Maintain a Secure Network and Systems

### Requirement 1 — Install and Maintain a Firewall Configuration to Protect Cardholder Data

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 1.1 | Firewall/router configuration standards established and implemented | → Req 1.1, 1.2 (expanded to NSC standards) |
| 1.1.1 | Formal process for approving and testing all network connections | → Req 1.2.2 (change control integration) |
| 1.1.2 | Current network diagram | → Req 1.2.3 (more specific — diagrams must show all data flows) |
| 1.1.3 | Current diagram that shows all cardholder data flows | → Req 1.2.4 (explicit data-flow diagram requirement) |
| 1.1.4 | Requirements for a firewall at each Internet connection | → Merged into Req 1.3 |
| 1.1.5 | Documentation of groups, roles, and responsibilities | → Req 12.1.1 |
| 1.1.6 | Documentation of allowed services/ports with business justification | → Req 1.2.5 |
| 1.1.7 | Firewall and router rule sets reviewed at least every 6 months | → Req 1.2.7 |
| 1.2 | Firewall and router configurations restrict connections | → Req 1.3 |
| 1.2.1 | Restrict inbound and outbound traffic to required services only | → Req 1.3.1, 1.3.2 |
| 1.2.2 | Secure and synchronise router configuration files | → Req 1.2.6 |
| 1.2.3 | Install perimeter firewalls between wireless networks and CDE | → Req 1.3.3 |
| 1.3 | Prohibit direct public access between the Internet and CDE | → Req 1.3, 1.4 |
| 1.3.1 | Implement DMZ to limit inbound traffic | → Req 1.4.1, 1.4.2 |
| 1.3.2 | Limit inbound Internet traffic to IP addresses within DMZ | → Req 1.4.2 |
| 1.3.3 | Anti-spoofing measures | → Req 1.4.3 |
| 1.3.4 | Do not allow outbound traffic from CDE to Internet not needed | → Req 1.3.2 |
| 1.3.5 | Permit only "established" connections back into network | → Req 1.3.1 |
| 1.3.6 | Place system components storing CHD in internal network zone | → Req 1.3.1 |
| 1.3.7 | Disclose private IP addresses to unauthorised parties | → Req 1.4.5 |
| 1.4 | Install personal firewall software on portable computing devices | → Req 1.5.1 |

### Requirement 2 — Do Not Use Vendor-Supplied Defaults for System Passwords and Other Security Parameters

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 2.1 | Vendor defaults changed before installing systems | → Req 2.2.2 |
| 2.1.1 | Wireless environments using vendor defaults changed | → Req 2.3.1 |
| 2.2 | Develop configuration standards for all system components | → Req 2.2 (expanded) |
| 2.2.1 | Implement only one primary function per server | → Req 2.2.3 |
| 2.2.2 | Enable only necessary services protocols, daemons | → Req 2.2.4 |
| 2.2.3 | Implement additional security features for risky protocols | → Req 2.2.5 |
| 2.2.4 | Configure system security parameters to prevent misuse | → Req 2.2.6 |
| 2.2.5 | Remove all unnecessary functionality (scripts, features, subsystems) | → Req 2.2.4 |
| 2.3 | Encrypt all non-console administrative access | → Req 2.2.7 |
| 2.4 | Maintain an inventory of system components in scope | → Req 12.5.1 (scope documentation) |
| 2.5 | Ensure security policies cover all applicable areas | → Req 12.1 |
| 2.6 | Shared hosting providers protect CDE and CHD | → Req 12.8, Appendix A1 |

---

## GOAL 2: Protect Account Data

### Requirement 3 — Protect Stored Cardholder Data

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 3.1 | Keep cardholder data storage to a minimum; define retention periods | → Req 3.2 |
| 3.2 | Do not store SAD after authorisation | → Req 3.3 |
| 3.2.1 | Do not store full magnetic stripe contents after authorisation | → Req 3.3.1 |
| 3.2.2 | Do not store the card verification code after authorisation | → Req 3.3.1 |
| 3.2.3 | Do not store the personal identification number (PIN) after authorisation | → Req 3.3.1 |
| 3.3 | Mask PAN when displayed (first 6/last 4 maximum) | → Req 3.4.1 |
| 3.4 | Render PAN unreadable anywhere it is stored | → Req 3.5.1 |
| 3.4.1 | Use disk-level or column-level encryption | → Req 3.5.1 (strong cryptography explicit) |
| 3.5 | Describe and implement procedures to protect keys | → Req 3.6 |
| 3.5.1 | Restrict access to cryptographic keys | → Req 3.7.3 |
| 3.5.1.1 (SP only) | Maintain cryptographic architecture description | NEW in v3.2; → removed as standalone in v4.0 |
| 3.5.2 | Store secret and private keys used for encryption of CHD securely | → Req 3.7.2 |
| 3.5.3 | Encrypted keys stored in fewest locations possible | → Req 3.7 |
| 3.6 | Fully document key management processes | → Req 3.7 (significantly expanded) |
| 3.6.1 | Generation of strong cryptographic keys | → Req 3.7.1 |
| 3.6.2 | Secure cryptographic key distribution | → Req 3.7 |
| 3.6.3 | Secure cryptographic key storage | → Req 3.7.2 |
| 3.6.4 | Cryptographic key changes for keys that have reached end of period | → Req 3.7.4 |
| 3.6.5 | Retirement or replacement of keys as deemed necessary | → Req 3.7.4 |
| 3.6.6 | Split knowledge and dual control for manual key management | → Req 3.7.6 |
| 3.6.7 | Prevention of unauthorised substitution of cryptographic keys | → Req 3.7.7 |
| 3.6.8 | Key custodians sign key custodian agreement | → Req 3.7.8 |
| 3.7 | Ensure security policies and operational procedures are documented | → Req 12.1 |

### Requirement 4 — Encrypt Transmission of Cardholder Data Across Open, Public Networks

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 4.1 | Use strong cryptography and security protocols to safeguard PAN | → Req 4.2.1 (expanded; TLS 1.2+ explicit) |
| 4.1.1 | Ensure wireless networks transmitting cardholder data use strong cryptography | → Req 4.2.1.2 |
| 4.2 | Never send unprotected PANs by end-user messaging technologies | → Req 4.2.2 |
| 4.3 | Ensure security policies and operational procedures are documented | → Req 12.1 |

---

## GOAL 3: Maintain a Vulnerability Management Program

### Requirement 5 — Protect All Systems Against Malware and Regularly Update Anti-Virus Software or Programs

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 5.1 | Deploy anti-virus software on all systems affected by malware | → Req 5.2 |
| 5.1.1 | Anti-virus programs detect, remove, and protect against all known types of malware | → Req 5.2.2 |
| 5.1.2 | Evaluate systems not commonly affected by malware for current malware threats | → Req 5.2.3 |
| 5.2 | Ensure anti-virus mechanisms are kept current | → Req 5.3.1 |
| 5.3 | Anti-virus mechanisms are actively running and cannot be disabled | → Req 5.3.4, 5.3.5 |
| 5.4 | Ensure security policies and operational procedures are documented | → Req 12.1 |
| — | Anti-phishing | **NEW in v4.0** — Req 5.4.1 (no equivalent in v3.2.1) |

### Requirement 6 — Develop and Maintain Secure Systems and Applications

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 6.1 | Establish a process to identify security vulnerabilities, using risk-ranking | → Req 6.3.1 |
| 6.2 | Protect all system components from known vulnerabilities | → Req 6.3.3 |
| 6.3 | Develop internal and external software applications securely | → Req 6.2 (expanded) |
| 6.3.1 | Remove development, test, and custom application accounts, user IDs | → Req 6.5.6 |
| 6.3.2 | Review custom code prior to release | → Req 6.2.3 |
| 6.4 | Follow change control processes and procedures | → Req 6.5 (expanded) |
| 6.4.1 | Separate development/test environments from production | → Req 6.5.3 |
| 6.4.2 | Separation of duties between development/test and production | → Req 6.5.4 |
| 6.4.3 | Production data (live PANs) not used for testing or development | → Req 6.5.5 |
| 6.4.4 | Remove test data and accounts before production | → Req 6.5.6 |
| 6.4.5 | Change control procedures for implementing security patches | → Req 6.5.1 |
| 6.4.6 | Upon completion of a significant change, all relevant PCI DSS requirements implemented | → Req 6.5.2 |
| 6.5 | Address common coding vulnerabilities in software development | → Req 6.2.4 |
| 6.5.1 | Injection flaws (SQL injection, LDAP injection, etc.) | → Req 6.2.4 |
| 6.5.2 | Buffer overflow vulnerabilities | → Req 6.2.4 |
| 6.5.3 | Insecure cryptographic storage | → Req 6.2.4 |
| 6.5.4 | Insecure communications | → Req 6.2.4 |
| 6.5.5 | Improper error handling | → Req 6.2.4 |
| 6.5.6 | High risk vulnerabilities identified in vulnerability identification process | → Req 6.2.4 |
| 6.5.7 | Cross-site scripting (XSS) | → Req 6.2.4 |
| 6.5.8 | Improper access control | → Req 6.2.4 |
| 6.5.9 | Cross-site request forgery (CSRF) | → Req 6.2.4 |
| 6.5.10 | Broken authentication and session management | → Req 6.2.4 |
| 6.6 | Address new threats and vulnerabilities for public-facing web apps | → Req 6.4.1, 6.4.2 (WAF) |
| 6.7 | Ensure security policies cover development | → Req 12.1 |
| — | Payment page script integrity | **NEW in v4.0** — Req 6.4.3 (no equivalent in v3.2.1) |
| — | Software Bill of Materials (SBOM) | **NEW in v4.0** — Req 6.3.2 (no equivalent in v3.2.1) |

---

## GOAL 4: Implement Strong Access Control Measures

### Requirement 7 — Restrict Access to System Components and Cardholder Data by Business Need to Know

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 7.1 | Limit access to system components to only those individuals whose job requires such access | → Req 7.2 |
| 7.1.1 | Define access needs for each role | → Req 7.2.2 |
| 7.1.2 | Restrict access to privileged user IDs to least privileges | → Req 7.2.1 |
| 7.1.3 | Assign access based on individual personnel's job classification and function | → Req 7.2.2 |
| 7.1.4 | Documented approval by authorised parties | → Req 7.2.3 |
| 7.2 | Establish an access control system | → Req 7.3 |
| 7.2.1 | Coverage of all system components | → Req 7.3.1 |
| 7.2.2 | Assignment of privileges to individuals based on job classification | → Req 7.3.2 |
| 7.2.3 | Default "deny-all" setting | → Req 7.3.2 |
| 7.3 | Ensure security policies cover access control | → Req 12.1 |

### Requirement 8 — Identify and Authenticate Access to System Components

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 8.1 | Define and implement policies for user identification | → Req 8.2 |
| 8.1.1 | Assign all users a unique ID before allowing them to access system components or CHD | → Req 8.2.1 |
| 8.1.2 | Control addition, deletion, and modification of user IDs | → Req 8.2.4 |
| 8.1.3 | Immediately revoke access for any terminated users | → Req 8.2.5 |
| 8.1.4 | Remove/disable inactive user accounts within 90 days | → Req 8.2.6 |
| 8.1.5 | Manage IDs used by vendors/partners to access, support, or maintain system components | → Req 8.2.3 |
| 8.1.6 | Limit repeated access attempts by locking out user ID after not more than 6 attempts | → Req 8.3.4 (changed to 10 attempts in v4.0) |
| 8.1.7 | Set lockout duration to 30 minutes or until admin re-enables | → Req 8.3.4 |
| 8.1.8 | Session idle timeout 15 minutes | → Req 8.2.8 |
| 8.2 | Employ at least one authentication method | → Req 8.3 |
| 8.2.1 | Encrypt all passwords/passphrases during transmission and storage | → Req 8.3.5 |
| 8.2.2 | Verify user identity before modifying any authentication credential | → Req 8.1 |
| 8.2.3 | Passwords/passphrases must meet minimum length of 7 characters | → **Changed in v4.0: 12 characters** (Req 8.3.6) |
| 8.2.4 | Change user passwords/passphrases at least once every 90 days | → Req 8.3.9 (for users without MFA) |
| 8.2.5 | Do not allow an individual to submit a new password if it is the same as previous 4 | → Req 8.3.7 |
| 8.2.6 | Set passwords/passphrases for first use and upon reset | → Req 8.3.5 |
| 8.3 | Secure individual non-consumer authentication | → Req 8.4, 8.5 |
| 8.3.1 | All individual non-consumer user access to CDE requires MFA using at least two of the three authentication factors [SP only in v3.2] | → **Extended in v4.0** — Req 8.4.2 applies to ALL users |
| 8.3.2 | All remote network access from outside the entity originated from users and all third parties must use MFA | → Req 8.3.2 |
| 8.4 | Document and communicate authentication policies and procedures | → Req 8.3.8 |
| 8.5 | Do not use group, shared, or generic IDs, passwords, or other methods | → Req 8.2.2 |
| 8.5.1 | Service providers with remote access to customer premises — each customer gets unique credentials | → Still required; incorporated into Req 8.2.3 |
| 8.6 | Use of other authentication mechanisms such as physical/logical security tokens, smart cards | → Req 8.3 |
| 8.7 | All access to database containing CHD restricted | → Req 7.2.6 |
| 8.8 | Ensure security policies cover authentication | → Req 12.1 |

### Requirement 9 — Restrict Physical Access to Cardholder Data

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 9.1 | Use appropriate facility entry controls to limit and monitor physical access to systems | → Req 9.2 |
| 9.1.1 | Use video cameras or other access control mechanisms to monitor individual physical access points | → Req 9.2.1 |
| 9.1.2 | Restrict physical access to publicly accessible network jacks | → Req 9.2.4 |
| 9.1.3 | Restrict physical access to wireless access points, gateways, handheld devices | → Req 9.2.3 |
| 9.2 | Develop procedures for all personnel to distinguish between employees and visitors | → Req 9.3 |
| 9.3 | Control physical access for onsite personnel to sensitive areas | → Req 9.3.1 |
| 9.4 | Visitor management procedures | → Req 9.2.2, 9.3.2 |
| 9.4.1 | Visitors authorised before entering areas where CHD is processed or maintained | → Req 9.3.2 |
| 9.4.2 | Visitors given a physical token that expires | → Req 9.3.2 |
| 9.4.3 | Visitors asked to surrender physical token before leaving | → Req 9.3.2 |
| 9.4.4 | Visitor log used to maintain audit trail | → Req 9.3.2 |
| 9.5 | Physically secure all media | → Req 9.4.1 |
| 9.6 | Maintain strict control over the internal or external distribution of any kind of media | → Req 9.4.3, 9.4.4 |
| 9.6.1 | Classify media so sensitivity can be determined | → Req 9.4.2 |
| 9.6.2 | Send media via secure courier | → Req 9.4.3 |
| 9.6.3 | Ensure management approves media moved outside the facility | → Req 9.4.4 |
| 9.7 | Maintain strict control over storage and accessibility of media | → Req 9.4.5 |
| 9.7.1 | Properly maintain invention logs for all media | → Req 9.4.5 |
| 9.8 | Destroy media when no longer needed | → Req 9.4.6, 9.4.7 |
| 9.8.1 | Shred, incinerate, or pulp paper materials | → Req 9.4.6 |
| 9.8.2 | Render cardholder data on electronic media unrecoverable | → Req 9.4.7 |
| 9.9 | Protect devices that capture payment card data via direct physical interaction from tampering | → Req 9.5 (expanded) |
| 9.9.1 | Maintain an up-to-date list of devices | → Req 9.5.1 |
| 9.9.2 | Periodically inspect device surfaces to detect tampering or substitution | → Req 9.5.1 |
| 9.9.3 | Provide training for personnel in areas with POI devices | → Req 9.5.1 |
| 9.10 | Ensure security policies cover physical security | → Req 12.1 |

---

## GOAL 5: Regularly Monitor and Test Networks

### Requirement 10 — Track and Monitor All Access to Network Resources and Cardholder Data

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 10.1 | Implement audit trails to link all access to system components to individual user | → Req 10.2 |
| 10.2 | Implement automated audit trails for all system components | → Req 10.2 |
| 10.2.1 | All individual user access to cardholder data | → Req 10.2.1 |
| 10.2.2 | All actions by any individual with root or administrative privileges | → Req 10.2.2 |
| 10.2.3 | Access to all audit trails | → Req 10.2.3 |
| 10.2.4 | Invalid logical access attempts | → Req 10.2.4 |
| 10.2.5 | Use of and changes to identification and authentication mechanisms | → Req 10.2.5 |
| 10.2.6 | Initialisation, stopping, or pausing of audit logs | → Req 10.2.6 |
| 10.2.7 | Creation and deletion of system-level objects | → Req 10.2.7 |
| 10.3 | Record audit trail entries for all system components | → Req 10.3 |
| 10.3.1 | User identification | → Req 10.3 |
| 10.3.2 | Type of event | → Req 10.3 |
| 10.3.3 | Date and time | → Req 10.3 |
| 10.3.4 | Success or failure indication | → Req 10.3 |
| 10.3.5 | Origination of event | → Req 10.3 |
| 10.3.6 | Identity or name of affected data, system component, or resource | → Req 10.3 |
| 10.4 | Synchronise all critical system clocks and times | → Req 10.6 |
| 10.4.1 | Critical systems have the correct and consistent time | → Req 10.6.1 |
| 10.4.2 | Time data is protected | → Req 10.6.3 |
| 10.4.3 | Time settings are received from industry-accepted time sources | → Req 10.6.2 |
| 10.5 | Secure audit trails so they cannot be altered | → Req 10.3 (expanded) |
| 10.5.1 | Limit viewing of audit trails to those with job-need | → Req 10.3.2 |
| 10.5.2 | Protect audit trail files from unauthorised modifications | → Req 10.3.1 |
| 10.5.3 | Promptly back up audit trail files to centralised log server | → Req 10.3.3 |
| 10.5.4 | Write logs for external-facing technologies onto a secure, centralised log server | → Req 10.3.3 |
| 10.5.5 | Use file-integrity monitoring or change-detection software on logs | → Req 10.3.4 |
| 10.6 | Review logs and security events for all system components | → Req 10.4 |
| 10.6.1 | Review the following at least daily: security events, logs of all system components | → Req 10.4.2; plus **NEW Req 10.4.1.1**: automated review required |
| 10.6.2 | Review logs of all other system components periodically based on policy | → Req 10.4.2 |
| 10.6.3 | Follow up exceptions and anomalies identified during review process | → Req 10.4.3 |
| 10.7 (SP only) | Implement a process for timely detection and reporting of failures of critical security control systems | → Req 10.7 (extended to ALL entities in v4.0) |
| 10.7.1 (SP only) | Failures of critical security controls — respond within one business day | → Req 10.7.2 |
| 10.8 | Retain audit log history for at least one year | → Req 10.5 |
| 10.9 | Ensure security policies cover monitoring | → Req 12.1 |

### Requirement 11 — Regularly Test Security Systems and Processes

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 11.1 | Implement processes to test for presence of wireless access points | → Req 11.2 |
| 11.1.1 | Maintain inventory of authorised wireless access points | → Req 11.2.1 |
| 11.1.2 | Incident response procedures for unauthorised wireless access points | → Req 11.2.2 |
| 11.2 | Run internal and external network vulnerability scans at least quarterly | → Req 11.3 |
| 11.2.1 | Quarterly internal vulnerability scans | → Req 11.3.1 |
| 11.2.2 | Quarterly external vulnerability scans via ASV | → Req 11.3.2 |
| 11.2.3 | Perform internal and external scans after any significant change | → Req 11.3.1.3, 11.3.2.1 |
| 11.3 | Implement a methodology for penetration testing | → Req 11.4 (significantly expanded) |
| 11.3.1 | Perform external penetration testing at least annually | → Req 11.4.3 |
| 11.3.2 | Perform internal penetration testing at least annually | → Req 11.4.1 |
| 11.3.3 | Exploitable vulnerabilities found during pen testing corrected and re-tested | → Req 11.4.4 |
| 11.3.4 | Segmentation controls tested at least annually to confirm CDE isolation | → Req 11.4.5 |
| 11.3.4.1 (SP only) | SP with segmentation of multi-tenant environments — test every 6 months | → Req 11.4.6 |
| 11.4 | Use intrusion-detection and/or intrusion-prevention techniques | → Req 11.5 |
| 11.4.1 (new v3.2) | Detect and alert on/prevent covert malware communications channels | → Req 11.5 |
| 11.5 | Deploy a change-detection mechanism to alert personnel | → Req 11.5.2 |
| 11.5.1 | Implement a process to respond to any alerts generated by the change-detection solution | → Req 11.5.2 |
| 11.6 | Ensure security policies cover testing | → Req 12.1 |
| — | Payment page tamper detection | **NEW in v4.0** — Req 11.6.1 (no equivalent in v3.2.1) |

---

## GOAL 6: Maintain an Information Security Policy

### Requirement 12 — Maintain a Policy That Addresses Information Security for All Personnel

| Sub-Req | Description | v4.0.1 Equivalent / Change Note |
|---------|-------------|--------------------------------|
| 12.1 | Establish, publish, maintain, and distribute a security policy | → Req 12.1 |
| 12.1.1 | Review security policy at least annually | → Req 12.1.1 |
| 12.2 | Implement a risk-assessment process | → Req 12.3 |
| 12.3 | Develop usage policies for critical technologies | → Req 12.3.1 |
| 12.4 | Ensure security policy and procedures clearly define security responsibilities | → Req 12.1.1 |
| 12.4.1 (SP only) | Executive management establish responsibility for protection of CHD | → Req 12.4.1, 12.4.2 (extended to all entities in v4.0) |
| 12.4.2 (SP only) | Reviews performed at least quarterly | → Req 12.11 (SP only) still in v4.0 |
| 12.5 | Assign to an individual or team IT security responsibilities | → Req 12.1.1 |
| 12.5.1 | Establish, document, and distribute security policies and procedures | → Req 12.1 |
| 12.5.2 | Monitor and analyse security alerts and information | → Req 12.5 |
| 12.5.2.1 (SP only) | Document and confirm PCI DSS scope at least every 6 months | → Req 12.5.2.1 (extended to annually for all in v4.0) |
| 12.5.3 | Establish, document, and distribute security incident response and escalation procedures | → Req 12.10 |
| 12.5.4 | Administer user accounts, including additions, deletions, and modifications | → Req 8.2.4 |
| 12.5.5 | Monitor and control all access to data | → Req 10.2 |
| 12.6 | Implement a formal security awareness program | → Req 12.6 |
| 12.6.1 | Educate personnel upon hire and at least annually thereafter | → Req 12.6.2 |
| 12.6.2 | Require personnel to acknowledge at least annually | → Req 12.6.3 |
| 12.7 | Screen potential personnel prior to hire | → Req 12.7 |
| 12.8 | Maintain and implement policies and procedures to manage service providers | → Req 12.8 (expanded) |
| 12.8.1 | Maintain a list of service providers | → Req 12.8.1 |
| 12.8.2 | Maintain a written agreement that includes an acknowledgement | → Req 12.8.2 |
| 12.8.3 | Ensure there is an established process for engaging service providers | → Req 12.8.3 |
| 12.8.4 | Maintain a programme to monitor service providers' PCI DSS compliance status at least annually | → Req 12.8.4 |
| 12.8.5 | Maintain information about which PCI DSS requirements are managed by each service provider | → Req 12.8.5 |
| 12.9 | Service providers acknowledge in writing their responsibility | → Req 12.9.1 |
| 12.9.1 (SP only) | Service providers acknowledge responsibility in writing | → Req 12.9.2 (SP acknowledgement now more detailed) |
| 12.10 | Implement an incident response plan | → Req 12.10 (expanded with new sub-requirements) |
| 12.10.1 | Create the incident response plan | → Req 12.10.1 |
| 12.10.2 | Test the plan at least annually | → Req 12.10.2 |
| 12.10.3 | Designate specific personnel to be available on a 24/7 basis | → Req 12.10.3 |
| 12.10.4 | Provide appropriate training to staff with security breach responsibilities | → Req 12.10.4 |
| 12.10.4.1 | Train IR personnel at least every 12 months | **NEW in v4.0** — Req 12.10.4.1 (formalises frequency) |
| 12.10.5 | Include alerts from security monitoring systems | → Req 12.10.5 |
| 12.10.6 | Develop a process to modify and evolve the incident response plan | → Req 12.10.6 |
| — | IR procedure for unexpected PAN location | **NEW in v4.0** — Req 12.10.7 |
| 12.11 (SP only) | Reviews performed at least quarterly | → Req 12.11 |

---

## v3.2.1 vs v4.0.1 — Notable Threshold Differences

| Item | v3.2.1 Value | v4.0.1 Value |
|------|-------------|-------------|
| Minimum password length | 7 characters | 12 characters (or 8 if system cannot support 12) |
| Account lockout threshold | 6 attempts | 10 attempts |
| MFA scope | Non-console admin + remote access | All access into the CDE |
| Log review | Manual daily review acceptable | Automated mechanism required (Req 10.4.1.1) |
| Anti-phishing requirement | None | Automated technical solution required (Req 5.4.1) |
| Payment page script controls | No explicit requirement | Script inventory + integrity controls mandatory (Req 6.4.3, 11.6.1) |
| Penetration testing — segmentation | At least annually | At least annually + 6-monthly for multi-tenant SPs |
| TPSP compliance monitoring | At least annually (12.8.4) | At least annually (unchanged) |
| Scope verification frequency | At least annually | At least annually; every 6 months for multi-tenant SPs |
| Software inventory (SBOM) | None | Required for bespoke software (Req 6.3.2) |
| Targeted Risk Analysis | Not formalised | Formalised; required for customised controls |

---

## v3.2.1 SAQ Types — Version Note

All SAQ types in v3.2.1 map directly to v4.0.1 equivalents (SAQ names unchanged). However, the control counts and specific requirements within each SAQ were updated in v4.0/v4.0.1:
- New requirements added (e.g., 6.4.3, 8.4.2, 5.4.1, 11.6.1) may apply to SAQ A-EP, SAQ C, and SAQ D
- SAQ A eligibility criteria unchanged
- SAQ P2PE eligibility criteria unchanged (still requires PCI-listed P2PE solution)

Organisations completing SAQs must use the v4.0/v4.0.1 SAQ documents — the v3.2.1 SAQ documents are retired.

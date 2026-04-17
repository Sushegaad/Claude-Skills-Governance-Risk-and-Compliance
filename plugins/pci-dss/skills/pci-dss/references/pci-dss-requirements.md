# PCI DSS v4.0.1 — All 12 Requirements

Source: PCI DSS v4.0.1 (PCI Security Standards Council, June 2024)
https://www.pcisecuritystandards.org/document_library/

---

## GOAL 1: Build and Maintain a Secure Network and Systems

### Requirement 1 — Install and Maintain Network Security Controls

Network security controls (NSCs) — firewalls, routers, cloud security groups — prevent unauthorised network access to and from the CDE.

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 1.1 | NSC policies and procedures are defined, implemented, and maintained | Policy docs, network diagrams, change records |
| 1.2 | NSC configurations restrict traffic to only what is necessary | Firewall/router ruleset review, deny-all default |
| 1.2.1 | Configuration standards for NSCs are defined | Documented baseline standards |
| 1.2.2 | NSC configuration changes are managed via change control | Change tickets, approval records |
| 1.2.3 | Network diagrams are current and accurate | Dated network diagram showing CDE boundaries |
| 1.2.4 | Data-flow diagrams for all account data flows are current | Data flow diagrams (DFDs) |
| 1.2.5 | All allowed services/ports are documented with business justification | Firewall rule documentation |
| 1.2.6 | Security features for each service are documented and implemented | Config baselines per service |
| 1.2.7 | NSC configurations are reviewed at least every 6 months | Review records with dates and approvers |
| 1.3 | Inbound and outbound network traffic is restricted to only that necessary | Egress filtering, deny-all-else rules |
| 1.3.1 | Inbound traffic to CDE restricted to authorised sources and services | Firewall rules reviewed |
| 1.3.2 | Outbound traffic from CDE restricted to authorised destinations | Egress rules documented |
| 1.3.3 | NSCs installed between wireless networks and CDE | Wireless-to-CDE firewall rules |
| 1.4 | Network connections between trusted and untrusted networks controlled | DMZ architecture, traffic inspection |
| 1.4.1 | NSCs between trusted/untrusted networks inspect and filter traffic | Stateful inspection, IDS/IPS |
| 1.4.2 | Inbound traffic from untrusted networks: no direct routes to CDE | No direct routing; proxy/DMZ required |
| 1.4.3 | Anti-spoofing measures to detect and block forged source IP addresses | Anti-spoofing ACLs, RFC 3704 filtering |
| 1.4.4 | Unauthorised traffic (cardholder data) blocked from entering untrusted networks | DLP rules or network controls |
| 1.4.5 | Internal IP addresses not disclosed to unauthorised parties | NAT, private RFC 1918 space |
| 1.5 | Risks from device connectivity to untrusted networks are managed | Endpoint security controls |
| 1.5.1 | Security controls for devices connecting to both untrusted and trusted networks | MDM/endpoint policy, split tunnelling controls |

**Common gaps**: Stale firewall rules never reviewed; no egress filtering; flat network (no CDE isolation); wireless networks not separated from CDE.

---

### Requirement 2 — Apply Secure Configurations to All System Components

Default credentials and unnecessary services must be eliminated before deployment.

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 2.1 | Processes for managing vendor defaults and other security parameters | Hardening policy, config standards |
| 2.2 | System configuration standards are developed and implemented | CIS Benchmark or equivalent; per platform standard |
| 2.2.1 | System configuration standards address all known security vulnerabilities | Vuln scan results mapped to standards |
| 2.2.2 | Vendor default accounts managed before deploying systems | Default creds disabled/renamed; evidence of removal |
| 2.2.3 | Primary functions needing different security levels are on separate components | Server isolation, role separation |
| 2.2.4 | Only necessary functions, ports, protocols, and services are enabled | Port scan results; services audit |
| 2.2.5 | If insecure protocols are used, business justification and additional controls documented | Protocol exception log |
| 2.2.6 | System security parameters are configured to prevent misuse | Config hardening evidence |
| 2.2.7 | All non-console administrative access is encrypted | SSH, HTTPS, TLS for all admin access |
| 2.3 | Wireless environments are configured and managed securely | Wi-Fi config review, WPA3 or WPA2-Enterprise |
| 2.3.1 | Default wireless vendor defaults changed at installation | AP config records |
| 2.3.2 | Wireless encryption keys changed when anyone with key knowledge leaves | Key rotation procedure and evidence |

**Common gaps**: Vendor default passwords left unchanged; unnecessary services (Telnet, FTP) still enabled; no documented hardening standards.

---

## GOAL 2: Protect Account Data

### Requirement 3 — Protect Stored Account Data

Minimise storage of account data; never store SAD post-authorisation; protect PAN wherever stored.

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 3.1 | Processes for protecting stored account data are defined and implemented | Data retention policy |
| 3.2 | Account data storage minimised | Data retention schedules; deletion procedures |
| 3.2.1 | SAD not retained after authorisation | Scan results proving no SAD in storage; code review |
| 3.3 | SAD is not retained after authorisation | Confirmed by system scans and application review |
| 3.3.1 | SAD not stored (full magnetic stripe, CAV2/CVV2/CVC2/CID, PIN/PIN block) | Application code review; database scans |
| 3.3.2 | SAD stored prior to authorisation is encrypted | Encryption evidence for pre-auth data |
| 3.3.3 | Encryption keys for pre-auth SAD are managed securely | Key management docs |
| 3.4 | PAN is protected wherever it is stored | Encryption, masking, or tokenisation evidence |
| 3.4.1 | PAN is unreadable anywhere it is stored | AES-256 encryption; tokenisation proof; masking |
| 3.4.2 | Copies of PAN only on authorised removable media | Media inventory and controls |
| 3.5 | PAN is secured with strong cryptography | Encryption algorithm and key management review |
| 3.5.1 | Primary account numbers protected with strong cryptography | AES-256 or equivalent; no DES/RC4 |
| 3.6 | Cryptographic keys used for PAN encryption are secured | Key management policy and procedures |
| 3.6.1 | Key management procedures and processes for cryptographic keys | Key custodian assignments; split knowledge |
| 3.7 | Key management procedures and processes are implemented | Key rotation, key-encrypting keys, key retirement |
| 3.7.1 | Key management policies cover the full key lifecycle | Generated, distributed, stored, retired |
| 3.7.2 | Key storage is secure | HSM, encrypted key store |
| 3.7.3 | Key access restricted to fewest custodians necessary | Dual control; split knowledge |
| 3.7.4 | Key retirement/replacement policy documented and followed | Rotation records |
| 3.7.5 | Key compromises managed per documented procedure | Incident response for key compromise |
| 3.7.6 | Manual keys use split knowledge and dual control | Evidence of two-person key operations |
| 3.7.7 | Informal key substitution prevented | Formal key management only |
| 3.7.8 | Key custodians acknowledge their responsibilities | Signed custodian agreements |
| 3.7.9 | Where key management services are used, they meet Req 3.6–3.7 | CSP KMS compliance evidence |

**Common gaps**: CVV stored in database; PAN in log files; no key rotation; encryption with weak algorithms (MD5, SHA-1 for integrity); keys stored alongside encrypted data.

---

### Requirement 4 — Protect Cardholder Data with Strong Cryptography During Transmission

PAN transmitted over open, public networks must be encrypted using strong cryptography.

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 4.1 | Processes for protecting PAN in transit are defined and implemented | Cryptography policy |
| 4.2 | PAN protected during transmission over open, public networks | TLS 1.2+ config; certificate review |
| 4.2.1 | Strong cryptography used to safeguard PAN in transit | TLS 1.2 or 1.3; no SSL, TLS 1.0, 1.1 |
| 4.2.1.1 | Certificate inventory maintained | Certificate management tool or inventory |
| 4.2.1.2 | Wireless networks transmitting PAN use strong cryptography | Wi-Fi encryption: WPA2-Enterprise or WPA3 |
| 4.2.2 | PAN not sent by unprotected end-user messaging (email, chat) | DLP policy; email encryption controls |

**Common gaps**: Legacy TLS 1.0/1.1 still enabled; expired SSL certificates; PAN sent via plain email; no certificate inventory.

---

## GOAL 3: Maintain a Vulnerability Management Program

### Requirement 5 — Protect All Systems and Networks from Malicious Software

Anti-malware controls protect against viruses, ransomware, spyware, and other threats.

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 5.1 | Processes for malware protection are defined | Anti-malware policy |
| 5.2 | Anti-malware solution(s) deployed on all applicable components | AV deployment inventory; management console |
| 5.2.1 | Anti-malware solution deployed on all components subject to malware | Coverage report; exceptions documented |
| 5.2.2 | Anti-malware solution detects all known types of malware | Vendor capability matrix |
| 5.2.3 | Systems not commonly affected by malware are evaluated periodically | Periodic risk analysis; documented exceptions |
| 5.3 | Anti-malware solution maintained and monitored | Definition update logs; scan results |
| 5.3.1 | Anti-malware solution kept current | Auto-update policy; current definition proof |
| 5.3.2 | Anti-malware performs periodic scans and active/real-time scanning | Scan schedule; real-time protection enabled |
| 5.3.3 | Anti-malware solution for removable media | USB scanning policy; endpoint config |
| 5.3.4 | Anti-malware solution logs maintained and monitored | Log retention; SIEM integration |
| 5.3.5 | Anti-malware mechanisms cannot be disabled by users | Admin-only uninstall; tamper protection enabled |
| 5.4 | Anti-phishing mechanisms protect users (**NEW in v4.0**) | Anti-phishing filter; email gateway config |
| 5.4.1 | Automated technical solution detects and protects against phishing | Email security gateway; URL filtering; DMARC/DKIM/SPF |

**Common gaps**: AV not covering Linux/Unix systems; definitions not auto-updated; users can disable AV; no phishing protections (new v4.0 requirement).

---

### Requirement 6 — Develop and Maintain Secure Systems and Software

Vulnerabilities must be identified and addressed through patching and secure development practices.

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 6.1 | Security vulnerability identification and management processes defined | Vuln management policy |
| 6.2 | Bespoke and custom software is developed securely | SDLC policy; code review process |
| 6.2.1 | Bespoke software developed based on secure coding guidelines | Coding standards; training records |
| 6.2.2 | Software development personnel trained on secure coding techniques | Annual training records |
| 6.2.3 | Code review performed before production release | Code review records; SAST scan results |
| 6.2.4 | Software engineering techniques to prevent common vulnerabilities | OWASP Top 10 addressed; DAST results |
| 6.3 | Security vulnerabilities identified and addressed | Patch management policy |
| 6.3.1 | Security vulnerabilities managed using ranking | CVSS or internal risk ranking; patch SLAs |
| 6.3.2 | Inventory of bespoke and custom software maintained | Software inventory/SBOM |
| 6.3.3 | All system components protected from known vulnerabilities | Patch management; current patch evidence |
| 6.4 | Public-facing web applications protected from attacks | WAF or application review |
| 6.4.1 | Public-facing web apps protected against web-based attacks | WAF in blocking mode; annual app testing |
| 6.4.2 | Automated technical solution deployed for public-facing web apps | WAF config; active monitoring |
| 6.4.3 | All payment page scripts managed and authorised (**NEW v4.0**) | Script inventory; integrity controls |
| 6.5 | Changes to system components managed securely | Change management policy |
| 6.5.1 | Changes to system components via formal change control | Change tickets; approval evidence |
| 6.5.2 | Post-change security verification | Test results; UAT sign-off |
| 6.5.3 | Pre-production environments are separate from production | Environment separation proof |
| 6.5.4 | Roles and functions are separated between production and pre-production | Access control evidence |
| 6.5.5 | Live PANs not used in pre-production/testing | Anonymised test data confirmation |
| 6.5.6 | Test data/accounts removed before production | Pre-prod cleanup checklist |

**Common gaps**: No SDLC/secure coding policy; live PANs in test environments; WAF in detection-only mode; payment page scripts not inventoried (v4.0 new).

---

## GOAL 4: Implement Strong Access Control Measures

### Requirement 7 — Restrict Access to System Components and Cardholder Data by Business Need to Know

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 7.1 | Access control processes and procedures defined | Access control policy |
| 7.2 | Access to system components and cardholder data is restricted | Role-based access matrix; IAM configuration |
| 7.2.1 | All users have access based on least privilege and need-to-know | Access review results |
| 7.2.2 | Access assigned based on job classification and function | Role definitions; access request records |
| 7.2.3 | Privilege access approved by authorised personnel | Approval workflow records |
| 7.2.4 | User accounts and access privileges reviewed at least every 6 months | Access review logs with dates |
| 7.2.5 | Application/system accounts managed by policy | Service account inventory; access controls |
| 7.2.6 | Query access to CHD repositories restricted to defined applications | DB access controls; application-level auth |
| 7.3 | Access to system components and data is managed | IAM system; access control enforcement |
| 7.3.1 | Access control system in place to restrict access to CDE | IAM/PAM tool deployment evidence |
| 7.3.2 | Access control system configured to enforce least privilege | ACL review; deny-by-default configuration |
| 7.3.3 | Access control system is kept current | Review and update cycle evidence |

**Common gaps**: Shared accounts; no access recertification; over-privileged service accounts; no need-to-know principle enforced for database access.

---

### Requirement 8 — Identify Users and Authenticate Access to System Components

Every user must have a unique ID; strong authentication required for CDE access.

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 8.1 | User identification and authentication processes defined | Authentication policy |
| 8.2 | User IDs and authentication credentials managed | IAM system; unique account verification |
| 8.2.1 | All users have a unique ID | Account audit; no shared accounts |
| 8.2.2 | Group, shared, or generic accounts managed only in exceptional circumstances | Exceptions with justification documented |
| 8.2.3 | Additional authentication for accounts used by third parties/vendors | MFA for vendor access |
| 8.2.4 | User accounts added/modified/deleted only through formal process | Identity lifecycle management records |
| 8.2.5 | Access for terminated users is immediately revoked | Offboarding checklist; IAM de-provisioning evidence |
| 8.2.6 | Inactive accounts disabled within 90 days | Account review; automated disable policy |
| 8.2.7 | Accounts used for system/application functions managed appropriately | Service account policy compliance |
| 8.2.8 | Sessions inactive more than 15 minutes require re-authentication | Session timeout config |
| 8.3 | Strong authentication established and managed | MFA configuration evidence |
| 8.3.1 | All user access into CDE uses MFA (**Extended in v4.0**) | MFA deployment proof for ALL CDE access |
| 8.3.2 | MFA for all access into the CDE from outside | Remote access MFA (VPN, RDP, etc.) |
| 8.3.4 | Invalid authentication attempts limited | Account lockout policy (max 10 attempts) |
| 8.3.5 | Passwords/passphrases set to meet minimum requirements | Password policy config: min 12 chars, complexity |
| 8.3.6 | Passwords changed every 90 days (or with compensating control/risk analysis) | Password policy; expiry settings |
| 8.3.7 | Individuals not allowed to submit new password same as any of last 4 | Password history settings |
| 8.3.8 | Authentication policies communicated to users | Training records; policy acknowledgements |
| 8.3.9 | Passwords for users not using MFA changed at least every 90 days | Password expiry config |
| 8.3.10 | Guidance for changing passwords provided to users at specified intervals | Comms records |
| 8.4 | MFA implemented for all access into the CDE | MFA for all privileged and standard user access |
| 8.4.1 | MFA for all non-console admin access to CDE | Admin MFA config |
| 8.4.2 | MFA for all access into the CDE (**Key new v4.0 change**) | MFA required for everyone accessing CDE |
| 8.5 | MFA systems configured to prevent misuse | Anti-MFA-bypass controls |
| 8.6 | Use of application/system accounts managed | Automated or manual interactive use controls |

**Common gaps**: Shared admin accounts; weak passwords (< 12 chars); no MFA for all CDE access (key v4.0 gap); accounts not disabled within 90 days of inactivity; no session timeout.

---

### Requirement 9 — Restrict Physical Access to Cardholder Data

Physical controls prevent unauthorised access to systems, media, and facilities in the CDE.

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 9.1 | Processes for restricting physical access defined | Physical security policy |
| 9.2 | Physical access controls for appropriate facility entry | Badge access logs; visitor records |
| 9.2.1 | Individual physical access controls to sensitive areas | Badge reader logs; CCTV |
| 9.2.2 | Visitor management procedure implemented | Visitor log; escort policy |
| 9.2.3 | Physical access to wireless access points, gateways, and handheld devices controlled | Device location inventory; lock-down evidence |
| 9.2.4 | Physical access to CDE systems via publicly accessible network jacks controlled | Port lock-out; network access control |
| 9.3 | Physical access for personnel and visitors authorised and managed | Access management records |
| 9.3.1 | Physical access controls for personnel with physical access | Access list; revocation process |
| 9.3.2 | Physical access for visitors authorised and revoked | Visitor badge records |
| 9.4 | Media with cardholder data is securely stored, accessed, distributed, and destroyed | Media inventory; destruction records |
| 9.4.1 | Physical media containing CHD secured | Locked storage; media inventory |
| 9.4.2 | Physical media containing CHD classified | Classification labels on media |
| 9.4.3 | Physical media distributed externally via tracked courier or secure methods | Courier receipts; chain of custody |
| 9.4.4 | Management approval for all media moved outside facility | Approval records |
| 9.4.5 | External media inventory controlled and audited | Media audit logs |
| 9.4.6 | Hard-copy materials with CHD destroyed cross-cut or confetti-shred | Destruction vendor certificates |
| 9.4.7 | Electronic media destroyed or rendered unrecoverable when no longer needed | Secure wipe / degauss / physical destroy records |
| 9.5 | Point-of-interaction (POI) devices protected from tampering and skimming | POI device inspection programme |
| 9.5.1 | POI device surface inspected to detect tampering or substitution | Inspection schedule; checklist records |

**Common gaps**: No visitor log; POI devices not regularly inspected; media not tracked or destroyed per policy; physical access not revoked for terminated staff.

---

## GOAL 5: Regularly Monitor and Test Networks

### Requirement 10 — Log and Monitor All Access to System Components and Cardholder Data

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 10.1 | Audit log processes defined | Log management policy |
| 10.2 | Audit logs implemented to support detection of anomalies | SIEM or log management platform |
| 10.2.1 | Audit logs capture all individual user access to CHD | Log samples showing user activity |
| 10.2.2 | Audit logs capture all actions by root or admin | Privileged access logs |
| 10.2.3 | Audit logs capture all access to audit logs | Audit-of-audit trail |
| 10.2.4 | Audit logs capture invalid logical access attempts | Failed login logs |
| 10.2.5 | Audit logs capture use of identification and authentication mechanisms | Auth logs; MFA event logs |
| 10.2.6 | Audit logs capture initialisation, stopping, or pausing of logs | Log service event logs |
| 10.2.7 | Audit logs capture creation/deletion of system-level objects | System event logs |
| 10.3 | Audit logs are protected from destruction and modification | Log integrity controls; write-once storage |
| 10.3.1 | Log files protected to prevent modifications | Immutable log storage; SIEM ingestion |
| 10.3.2 | Audit log files protected from unauthorised access | Access controls on log infrastructure |
| 10.3.3 | Audit logs are promptly backed up to a central log server | Syslog/SIEM centralisation evidence |
| 10.3.4 | File integrity monitoring or change detection on audit logs | FIM solution monitoring log files |
| 10.4 | Audit logs reviewed to identify anomalies or suspicious activity | Log review process |
| 10.4.1 | Automated log review mechanisms used (**NEW in v4.0**) | SIEM alert rules; automated review evidence |
| 10.4.2 | Logs for all system components reviewed daily | Review schedules; SIEM alert evidence |
| 10.4.3 | Exceptions and anomalies addressed promptly | Ticket records tied to log alerts |
| 10.5 | Audit log history retained for at least 12 months with last 3 months immediately available | Retention policy; log storage capacity |
| 10.6 | Time synchronisation technology in use | NTP configuration; stratum 1/2 sync |
| 10.7 | Failures of critical security controls detected and addressed (**NEW in v4.0**) | Monitoring for AV, FW, IDS failures |
| 10.7.2 | Failures detected and responded to promptly | Alert/ticketing evidence |

**Common gaps**: Logs not centralised to SIEM; retention under 12 months; no automated review (v4.0 new); time not synchronised across all CDE components; critical security control failures not monitored.

---

### Requirement 11 — Test Security of Systems and Networks Regularly

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 11.1 | Security testing processes defined | Testing policy |
| 11.2 | Wireless access points managed | Wireless AP inventory; rogue AP detection |
| 11.2.1 | Authorised and unauthorised wireless access points managed | Quarterly wireless scans; rogue detection alerts |
| 11.2.2 | Wireless scan inventory reconciled quarterly | Scan results vs inventory |
| 11.3 | External and internal vulnerabilities assessed | Vulnerability scanning programme |
| 11.3.1 | Internal vulnerability scans run at least every 3 months | Scan reports showing quarterly cadence |
| 11.3.2 | External vulnerability scans run at least every 3 months by an ASV | ASV scan reports; passing results |
| 11.3.3 | All exploitable vulnerabilities remediated and re-scanned | Remediation evidence; re-scan passing results |
| 11.4 | External and internal penetration testing is performed | Penetration test reports |
| 11.4.1 | Penetration testing methodology defined | Pen test scope document |
| 11.4.2 | Internal penetration testing at least annually and after changes | Annual pen test report |
| 11.4.3 | External penetration testing at least annually and after changes | External pen test report |
| 11.4.4 | Exploitable vulnerabilities from pen testing remediated and re-tested | Remediation tracking; re-test confirmation |
| 11.4.5 | Network segmentation verified by penetration testing at least every 6 months | Segmentation pen test report |
| 11.5 | Network intrusion detection/prevention techniques used | IDS/IPS deployment evidence |
| 11.5.1 | Intrusion detection/prevention used to detect and/or prevent intrusions | IDS/IPS alert logs; tuning records |
| 11.5.2 | Change detection mechanism deployed on CDE | FIM solution alerts; change records |
| 11.6 | Unauthorised changes on payment pages detected and responded to (**NEW v4.0**) | Script integrity monitoring |
| 11.6.1 | Change and tamper detection mechanism for payment pages deployed | HTTP header monitoring; script hash verification |

**Common gaps**: ASV scans failing (not "clean"); penetration testing not truly internal + external; segmentation not tested; no FIM; payment page integrity not monitored (v4.0 new).

---

## GOAL 6: Maintain an Information Security Policy

### Requirement 12 — Support Information Security with Organizational Policies and Programs

| Sub-Req | Description | Evidence for QSA |
|---------|-------------|-----------------|
| 12.1 | Comprehensive information security policy defined, published, and maintained | Security policy doc; annual review |
| 12.2 | Targeted risk analysis process defined for flexible requirements | TRA template; completed TRAs |
| 12.3 | Risks to CHD and cardholder data environment managed | Risk management programme |
| 12.3.1 | Targeted risk analysis for each PCI DSS requirement with customised approach | TRA documentation per requirement |
| 12.3.2 | TRA performed for flexible-frequency requirements | Documented TRAs for each flexible req |
| 12.3.3 | Cryptographic cipher suites and protocols reviewed and documented at least once every 12 months | Crypto inventory; annual review records |
| 12.3.4 | Hardware and software technologies reviewed at least once every 12 months | Tech lifecycle review records |
| 12.4 | PCI DSS compliance managed throughout the year | Compliance programme; quarterly review |
| 12.4.2 | Reviews confirming personnel follow security policies performed at least quarterly | Quarterly compliance review records |
| 12.5 | PCI DSS scope documented and validated | Scope documentation; annual review |
| 12.5.1 | Inventory of system components in scope for PCI DSS maintained | CDE system inventory |
| 12.5.2 | PCI DSS scope verified at least every 12 months and after major changes | Annual scope review; post-change assessment |
| 12.6 | Security awareness education implemented | Security awareness programme; training records |
| 12.6.1 | Security awareness programme in place | Programme documentation |
| 12.6.2 | Security awareness programme reviewed at least every 12 months | Review records |
| 12.6.3 | Personnel acknowledge at least annually they have read and understood security policy | Signed acknowledgements |
| 12.7 | Personnel are screened before granting access to CDE | Background check policy; records |
| 12.8 | Third-party service providers (TPSPs) with CHD access are managed | TPSP inventory; compliance monitoring |
| 12.8.1 | List of all TPSPs maintained | TPSP register |
| 12.8.2 | Written agreements with TPSPs acknowledging PCI DSS responsibility | Signed agreements |
| 12.8.3 | Established process for engaging TPSPs | TPSP due diligence process |
| 12.8.4 | TPSP PCI DSS compliance status monitored at least annually | Annual TPSP compliance confirmation; AOC |
| 12.8.5 | Information about which PCI DSS requirements managed by each TPSP | Responsibility matrix |
| 12.9 | TPSPs support customers' PCI DSS compliance | TPSP acknowledgement of responsibility |
| 12.10 | Suspected and confirmed security incidents responded to immediately | Incident response plan; test records |
| 12.10.1 | Incident response plan created and ready | Documented IR plan |
| 12.10.2 | IR plan reviewed and tested at least annually | Annual tabletop or drill evidence |
| 12.10.3 | Specific personnel designated for 24/7 incident response | On-call roster; contact list |
| 12.10.4 | IR personnel trained appropriately | Annual training records |
| 12.10.5 | Alerts from security monitoring systems included in IR plan | IR plan references monitoring alerts |
| 12.10.6 | IR plan updated when new threats or lessons learned | Version history; update records |
| 12.10.7 | Incident response procedures for discovery of stored PAN in unexpected location | PAN discovery procedure |

**Common gaps**: Security policy not reviewed annually; no TPSP register or compliance monitoring; incident response plan never tested; personnel not acknowledging policy; no TRA process.

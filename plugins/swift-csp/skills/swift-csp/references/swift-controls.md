# SWIFT CSCF v2026 - Full Control Reference

All 32 controls (26 mandatory, 6 advisory) across 3 objectives. Architecture applicability: ✅ = Mandatory | 🔶 = Advisory | ➖ = Not Applicable

> ⚠️ **Verify against the official CSCF v2026** (swift.com Knowledge Centre, requires login) before relying on per-control applicability - SWIFT adjusts control status and architecture-type applicability each cycle. Key v2026 change reflected below: **Control 2.4 promoted Advisory → Mandatory.**

---

## Architecture Applicability Matrix

| Control | A1 | A2 | A3 | A4 | B |
|---------|----|----|----|----|---|
| 1.1 SWIFT Environment Protection | ✅ | ✅ | ✅ | ✅ | ✅ |
| 1.2 OS Privileged Account Control | ✅ | ✅ | ➖ | ➖ | ✅ |
| 1.3 Virtualisation or Cloud Platform Protection | ✅ | ✅ | ✅ | ✅ | ✅ |
| 1.4 Restriction of Internet Access | ✅ | ✅ | ✅ | ✅ | ✅ |
| 1.5 Customer Environment Protection | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.1 Internal Data Flow Security | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.2 Security Updates | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.3 System Hardening | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.4 Back-Office Data Flow Security *(promoted to Mandatory in v2026)* | ✅ | ✅ | ✅ | ✅ | ➖ |
| 2.5A External Transmission Data Protection | 🔶 | 🔶 | 🔶 | 🔶 | 🔶 |
| 2.6 Operator Session Confidentiality | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.7 Vulnerability Scanning | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.8 Outsourced Critical Activity Protection | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.9 Transaction Business Controls | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.10 Application Hardening | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.11A RMA Business Controls | 🔶 | 🔶 | 🔶 | 🔶 | 🔶 |
| 3.1 Physical Security | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4.1 Password Policy | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4.2 Multi-Factor Authentication | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5.1 Logical Access Controls | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5.2 Token Management | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5.3A Staff Screening Process | 🔶 | 🔶 | 🔶 | 🔶 | 🔶 |
| 5.4 Physical and Logical Password Storage | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6.1 Malware Protection | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6.2 Software Integrity | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6.3 Database Integrity | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6.4 Logging and Monitoring | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6.5A Intrusion Detection | 🔶 | 🔶 | 🔶 | 🔶 | 🔶 |
| 7.1 Cyber Incident Response Planning | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7.2 Security Training and Awareness | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7.3A Penetration Testing | 🔶 | 🔶 | 🔶 | 🔶 | 🔶 |
| 7.4A Scenario-based Risk Assessment | 🔶 | 🔶 | 🔶 | 🔶 | 🔶 |

---

## Objective 1 - Secure Your Environment

### Control 1.1 - SWIFT Environment Protection (Mandatory)

**Purpose:** Create and maintain a dedicated, protected SWIFT zone isolated from the general IT environment and internet.

**Requirements:**
- Establish a dedicated **Secure Zone** containing all SWIFT infrastructure components (Alliance Access/Gateway, HSMs, operator workstations used exclusively for SWIFT)
- The Secure Zone must be isolated from the general IT environment by firewalls with deny-by-default rules
- SWIFT servers must not be used for non-SWIFT activities (email, web browsing, general business applications)
- Network flows in and out of the Secure Zone must be documented and restricted to those strictly necessary
- Dual-homed systems (connected to both SWIFT zone and general network) are prohibited

**Evidence artifacts:**
- Network architecture diagram showing SWIFT Secure Zone boundaries
- Firewall ruleset documentation and change records
- System inventory for all components in the Secure Zone
- Configuration evidence that servers are dedicated (no dual-homing)

**Implementation steps:**
1. Map all current SWIFT components and their network connectivity
2. Design SWIFT Secure Zone with dedicated VLAN or physical segment
3. Deploy stateful firewall between Secure Zone and general corporate network
4. Configure deny-all default rules; whitelist only required flows
5. Remove any shared-use applications from SWIFT servers
6. Document and periodically review all approved network flows

---

### Control 1.2 - OS Privileged Account Control (Mandatory - A1, A2, B only)

**Purpose:** Restrict and control privileged operating system accounts on SWIFT infrastructure.

**Requirements:**
- Privileged OS accounts (root, local admin) must not be used for routine operations
- Privileged accounts must have strong authentication (MFA where technically feasible)
- All use of privileged accounts must be logged and reviewable
- Default/factory OS accounts must be renamed or disabled
- Privileged access must follow least-privilege and need-to-know principles

**Evidence artifacts:**
- Privileged account inventory for all SWIFT servers
- Evidence of MFA for privileged sessions (PAM tool screenshots, auth logs)
- Policy for privileged account usage
- OS audit logs showing privileged account activity

---

### Control 1.3 - Virtualisation or Cloud Platform Protection (Mandatory)

**Purpose:** Secure the hypervisor and virtualisation layer if SWIFT components run on virtual machines.

**Requirements:**
- Hypervisor patched to current supported version
- Hypervisor management interfaces restricted (no general user access)
- VM isolation configured; no shared storage between SWIFT VMs and general VMs
- Snapshots of SWIFT VMs treated as sensitive; protected and retention-controlled

**Evidence artifacts:**
- Hypervisor version and patch status
- Access control list for hypervisor management console
- VM architecture diagram showing isolation

---

### Control 1.4 - Restriction of Internet Access (Mandatory)

**Purpose:** Prevent SWIFT servers and operator workstations from having direct internet access.

**Requirements:**
- SWIFT servers must have no direct internet access
- SWIFT-dedicated operator workstations must have internet access blocked
- Where internet access is technically necessary for SWIFT operations (e.g., SWIFTNet access), traffic must be strictly controlled and monitored
- Jump servers or proxies used for administration must not be internet-facing

**Evidence artifacts:**
- Firewall rules showing internet access blocked for SWIFT zone IPs
- Proxy configuration if applicable
- Network flow test results

---

### Control 1.5 - Customer Environment Protection (Mandatory)

**Purpose:** Extend security controls to protect the broader customer IT environment from threats that could cascade to SWIFT.

---

### Control 2.1 - Internal Data Flow Security (Mandatory)

**Purpose:** Protect SWIFT message data in transit within the customer environment.

**Requirements:**
- All connections between SWIFT components within the Secure Zone must be encrypted or physically protected
- TLS 1.2+ required for all internal connections carrying SWIFT data
- Message broker connections (MQ, middleware) must be authenticated and encrypted
- Back-office to SWIFT interface connections must be secured

**Evidence artifacts:**
- Data flow diagram showing all internal SWIFT connections
- TLS configuration evidence for each connection
- Certificate inventory with expiry tracking

---

### Control 2.2 - Security Updates (Mandatory)

**Purpose:** Apply security patches to SWIFT-related software and underlying systems promptly.

**Patching expectations:** Apply security updates in a timely manner, prioritised by severity and vendor/SWIFT advisory guidance. CSCF v2026 does not publish fixed day-count SLAs for this control; define risk-based internal timelines and evidence adherence to them.

**Requirements:**
- All SWIFT-connected systems (OS, middleware, SWIFT application) included in patch scope
- SWIFT-issued security advisories must be tracked and acted upon
- Exceptions documented with risk acceptance and compensating controls

**Evidence artifacts:**
- Vulnerability/patch management tool reports showing SWIFT components
- Evidence of SWIFT advisory subscription and action log
- Exception register with approval dates

---

### Control 2.3 - System Hardening (Mandatory)

**Purpose:** Apply security hardening baselines to all SWIFT-connected systems.

**Requirements:**
- Apply CIS Benchmarks (or equivalent hardening standard) to all SWIFT servers and operator workstations
- Disable all unnecessary services, ports, and protocols
- Remove all unused software and accounts
- Enforce host-based firewalls on SWIFT systems
- Document and maintain hardening baseline; re-check after every change

**Evidence artifacts:**
- Hardening baseline document per system type
- Configuration scan results vs. baseline (CIS-CAT or equivalent)
- Evidence of unnecessary services disabled (netstat/ss output)

---

### Control 2.4 - Back-Office Data Flow Security (Mandatory - promoted from Advisory in v2026)

**Purpose:** Protect SWIFT transaction data as it flows between SWIFT components and back-office / ERP systems.

**v2026 scope notes:** Encryption is required between the general IT environment and the secure SWIFT infrastructure, including flows via a bridging server. Phased application: legacy direct connections and flows from a bridging server to the back-office first hops are **not yet mandatory** (SWIFT has signalled v2028 for these). Control 2.4 is **not applicable to architecture B**, which has no SWIFT-specific local footprint and therefore no in-scope first-hop back-office flows.

---

### Control 2.5A - External Transmission Data Protection (Advisory)

**Purpose:** Encrypt SWIFT-related data transmitted outside the customer environment.

---

### Control 2.6 - Operator Session Confidentiality and Integrity (Mandatory)

**Purpose:** Protect operator sessions to SWIFT applications from interception and tampering.

**Requirements:**
- All operator sessions to SWIFT applications must use TLS 1.2+ or equivalent encryption
- Sessions must be authenticated via MFA (aligned to 4.2)
- Session timeouts configured (maximum 30 minutes of inactivity)
- Session logs retained per control 6.4 requirements
- Clipboard, screen-share, and remote control tools restricted on SWIFT workstations during sessions

**Evidence artifacts:**
- TLS configuration for Alliance Access/Gateway web interface
- Session timeout configuration screenshots
- Remote access tool inventory and restriction evidence

---

### Control 2.7 - Vulnerability Scanning (Mandatory)

**Purpose:** Identify and remediate vulnerabilities in SWIFT-connected systems through regular scanning.

**Requirements:**
- Quarterly credentialed vulnerability scans of all in-scope SWIFT systems
- Scans must be authenticated (credentialed) - unauthenticated scans do not meet the requirement
- Results reviewed and remediated in a timely, severity-prioritised manner per Control 2.2
- Scan coverage includes OS, middleware, SWIFT application components, and network devices in Secure Zone

**Evidence artifacts:**
- Vulnerability scan reports for last 4 quarters (showing SWIFT system IPs/hostnames)
- Evidence of authenticated scans (scanner configuration or credential records)
- Remediation tracking for identified vulnerabilities

---

### Control 2.8 - Outsourced Critical Activity Protection (Mandatory)

**Purpose:** Ensure security obligations are maintained when SWIFT-related activities are outsourced.

**Requirements:**
- If any SWIFT-related activity is outsourced (service bureau, managed SOC, cloud), the outsourced party must comply with applicable CSCF controls
- Contracts must include SWIFT CSP security obligations
- Annual review of outsourced providers' compliance evidence (their KYC-SA attestation or equivalent)
- The attesting entity remains responsible for compliance regardless of outsourcing

**Evidence artifacts:**
- Contracts with SWIFT security obligations
- Provider KYC-SA attestations or audit reports
- Annual vendor review records

---

### Control 2.9 - Transaction Business Controls (Mandatory)

**Purpose:** Implement business-level controls to detect and prevent fraudulent SWIFT transactions.

**Includes:** Payment value thresholds, expected transaction patterns, time-of-day restrictions, currency controls, beneficiary whitelisting.

---

### Control 2.10 - Application Hardening (Mandatory)

**Purpose:** Apply security hardening to SWIFT application software (Alliance Access/Gateway).

**Requirements:**
- SWIFT software configured per SWIFT's published Security Hardening Guides for Alliance Access and Alliance Gateway
- Unused SWIFT application features and interfaces disabled
- Application accounts configured with least privilege
- Default passwords changed; application-level accounts reviewed quarterly

**Evidence artifacts:**
- Completed SWIFT Alliance Access / Alliance Gateway Security Hardening Guide checklist
- Application configuration screenshots showing disabled modules
- Application account audit report

---

### Control 2.11A - RMA Business Controls (Advisory)

**Purpose:** Control and monitor Relationship Management Application (RMA) authorisations to limit counterparty message flows.

---

### Control 3.1 - Physical Security (Mandatory)

**Purpose:** Physically protect SWIFT infrastructure from unauthorised access, tampering, and damage.

**Requirements:**
- SWIFT servers housed in a locked, access-controlled facility (data centre or equivalent)
- Access restricted to named individuals with documented authorisation
- Physical access logged electronically (badge reader or equivalent)
- Visitor access controlled and escorted
- SWIFT-dedicated operator workstations in physically controlled areas

**Evidence artifacts:**
- Physical access control system logs
- Authorised access list for data centre / SWIFT server room
- CCTV or access badge system evidence

---

## Objective 2 - Know and Limit Access

### Control 4.1 - Password Policy (Mandatory)

**Purpose:** Enforce strong password requirements for all accounts accessing SWIFT systems.

**Requirements:**
- Minimum password length: 14 characters (or per organisational policy if stricter)
- Complexity: upper, lower, number, special character
- Maximum password age: 90 days for privileged accounts; 180 days for standard accounts
- No password reuse for 12 generations
- Account lockout after 5 failed attempts
- No shared or generic accounts

**Evidence artifacts:**
- Password policy document
- Group Policy / AD configuration screenshots
- Account lockout configuration evidence

---

### Control 4.2 - Multi-Factor Authentication (Mandatory)

**Purpose:** Require MFA for all interactive operator access to the SWIFT environment.

**Requirements:**
- MFA mandatory for **all** interactive logins to SWIFT applications (Alliance Access, Alliance Gateway, SWIFT GUI)
- MFA mandatory for remote administrative access to SWIFT systems
- Acceptable MFA methods: hardware OTP tokens, smart cards with PIN, FIDO2 hardware keys
- Software-based OTP (authenticator apps on shared devices) **does not satisfy** this requirement for most architecture types
- Token lifecycle management must align with Control 5.2

**Evidence artifacts:**
- MFA configuration evidence for each SWIFT interface
- Token inventory showing all operator tokens
- Authentication logs showing MFA enforcement
- Exemption register if any accounts are excluded (must be approved and documented)

---

### Control 5.1 - Logical Access Controls (Mandatory)

**Purpose:** Enforce least-privilege access to SWIFT applications and data.

**Requirements:**
- Individual named accounts for every SWIFT operator - no shared accounts
- Role-based access aligned to business need; no default admin access for standard operators
- Dual authorisation required for high-risk operations (e.g., creating new BIC connections)
- Quarterly access reviews; remove stale/terminated user access within 24 hours of departure
- Operator privileges documented and approved by a control function

**Evidence artifacts:**
- User access list with roles and approval evidence
- Access review records (last four quarters)
- Evidence of dual-authorisation for high-risk actions
- Leaver process records showing timely access removal

---

### Control 5.2 - Token Management (Mandatory)

**Purpose:** Manage the lifecycle of authentication tokens used to access SWIFT systems.

**Requirements:**
- Token inventory maintained for all SWIFT operators
- Lost/stolen tokens reported immediately and deactivated within 1 hour
- Token allocation requires formal approval
- Token return process documented for leavers
- Token storage policy (e.g., not left unattended in public areas)
- Annual token inventory reconciliation

**Evidence artifacts:**
- Token inventory register
- Token issuance and return records
- Lost token incident records (if any)
- Annual reconciliation evidence

---

### Control 5.3A - Staff Screening Process (Advisory)

**Purpose:** Implement personnel security measures for staff with SWIFT access.

---

### Control 5.4 - Physical and Logical Password Storage (Mandatory)

**Purpose:** Protect passwords and credentials used for SWIFT systems from exposure.

**Requirements:**
- SWIFT application passwords and credentials must be stored in an approved password manager or CyberArk/PAM vault
- No passwords stored in plaintext files, spreadsheets, or unencrypted documents
- Emergency/break-glass credentials stored in sealed envelopes with tamper evidence - access logged
- Default application credentials changed on installation and after each maintenance

**Evidence artifacts:**
- Password manager / PAM tool evidence showing SWIFT credentials
- Break-glass credential procedure and access log
- Evidence of changed default credentials

---

## Objective 3 - Detect and Respond

### Control 6.1 - Malware Protection (Mandatory)

**Purpose:** Deploy and maintain anti-malware protection on SWIFT-connected systems.

**Requirements:**
- Anti-malware deployed on all SWIFT servers and operator workstations in scope
- Malware definitions updated daily (automated)
- Real-time scanning enabled
- Scheduled full scans configured
- Alerts for malware detections sent to security team within 1 hour
- Malware found on SWIFT systems treated as a security incident per Control 7.1

**Evidence artifacts:**
- Anti-malware configuration and deployment scope screenshots
- Definition update log (last 30 days)
- Alert configuration evidence
- Scan history reports

---

### Control 6.2 - Software Integrity (Mandatory)

**Purpose:** Verify the integrity of SWIFT software before installation and after updates to detect tampering.

**Requirements:**
- Verify cryptographic hash of SWIFT software packages before installation (compare against SWIFT-published checksums)
- Integrity verification repeated after any SWIFT software update
- Unauthorised changes to SWIFT executable files must trigger an incident
- File integrity monitoring (FIM) recommended for SWIFT binary directories
- Evidence of integrity verification retained for audit

**Evidence artifacts:**
- Hash verification records for SWIFT software installations and updates
- FIM configuration (if deployed) covering SWIFT directories
- Integrity check procedure document

---

### Control 6.3 - Database Integrity (Mandatory)

**Purpose:** Protect SWIFT transaction data and configuration data in databases from unauthorised modification.

**Requirements:**
- Database access restricted to authorised SWIFT application service accounts only
- No direct database access by operators for production systems
- Database change logging enabled; changes alerted to security team
- Regular database integrity checks configured
- Database backups tested; restoration procedures documented

**Evidence artifacts:**
- Database access control configuration
- Database audit log samples
- Backup and restoration test records

---

### Control 6.4 - Logging and Monitoring (Mandatory)

**Purpose:** Capture, retain, and review security-relevant events from SWIFT systems to detect anomalies.

**Requirements:**
- **Log sources in scope:** Alliance Access/Gateway application logs, OS security logs, authentication logs, network device logs for SWIFT zone, database audit logs
- **Minimum retention:** 1 year online/hot; 3 years total (hot + archived)
- **Review frequency:** Daily review of SWIFT transaction anomalies and authentication failures; weekly review of other events
- **Alerting:** Automated alerts for: failed authentications, after-hours logins, large/unusual transactions, privilege escalation, config changes
- SIEM or equivalent must be configured to ingest SWIFT log sources
- Log integrity must be protected (logs shipped to immutable SIEM or read-only store)

**Evidence artifacts:**
- SIEM configuration showing SWIFT log sources
- Log retention policy and technical evidence (log archive tool configuration)
- Sample alert rules for SWIFT anomalies
- Log review records (last 30 days)

---

### Control 6.5A - Intrusion Detection (Advisory)

**Purpose:** Deploy network or host-based intrusion detection for the SWIFT zone.

---

### Control 7.1 - Cyber Incident Response Planning (Mandatory)

**Purpose:** Maintain a documented, tested incident response capability for SWIFT-specific cyber incidents.

**Requirements:**
- Documented **SWIFT-specific Incident Response Plan (IRP)** covering: detection triggers, triage, containment, notification (internal and SWIFT), investigation, recovery, lessons learned
- IRP must define when and how to notify SWIFT (via SWIFT's CISO or through KYC-SA) - SWIFT requires notification within 24 hours of a confirmed cyber incident affecting SWIFT infrastructure
- IRP tested annually (tabletop exercise or live drill)
- Contact list for SWIFT support and internal incident team maintained and tested
- Evidence preservation requirements defined (forensic images, log preservation)

**SWIFT Incident Notification Obligations:**
- Notify SWIFT within 24 hours of confirming a cyber incident affecting SWIFT infrastructure or transactions
- Submit full incident report to SWIFT within 30 days
- Cooperate with SWIFT investigations

**Evidence artifacts:**
- SWIFT Incident Response Plan document (dated, approved)
- Last annual test record (tabletop or drill report)
- SWIFT notification contact list
- Sample incident log (if available)

---

### Control 7.2 - Security Training and Awareness (Mandatory)

**Purpose:** Ensure all staff with SWIFT access receive security awareness training.

**Requirements:**
- Annual security awareness training for all staff with access to SWIFT systems
- Training must include: phishing awareness, social engineering, SWIFT fraud scenarios (Bangladesh Bank-style attacks), incident reporting procedures
- Training completion tracked and evidenced
- Role-specific training for SWIFT operators covering CSP requirements

**Evidence artifacts:**
- Training completion records for all SWIFT users (last 12 months)
- Training content overview (showing SWIFT-specific topics)
- Role-specific training materials for operators

---

### Control 7.3A - Penetration Testing (Advisory)

**Purpose:** Conduct penetration testing of the SWIFT environment to identify vulnerabilities not found by scanning.

**Best practice:** Annual penetration test of SWIFT Secure Zone, including network perimeter, application layer (Alliance Access), and authentication mechanisms. Red-team exercise every 2–3 years.

---

### Control 7.4A - Scenario-based Risk Assessment (Advisory)

**Purpose:** Conduct scenario-based risk assessments for SWIFT-specific attack scenarios.

**Scenarios to assess:** Insider fraud, compromised SWIFT operator credentials, supply chain attack on SWIFT software, social engineering targeting SWIFT operators, ransomware propagation to SWIFT zone.

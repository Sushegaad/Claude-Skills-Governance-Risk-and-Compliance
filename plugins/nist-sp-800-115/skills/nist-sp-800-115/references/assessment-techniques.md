# Assessment Techniques Reference — NIST SP 800-115

Source: NIST SP 800-115 (September 2008), Sections 3–6

---

## Review Techniques (Section 3)

Review techniques are examination-based methods that do not involve active testing of systems. They provide insight into security posture through analysis of documentation, configurations, and logs.

### Documentation Review

**Purpose**: Evaluate whether security policy, plans, procedures, and standards are complete, consistent, and current.

**Documents to review**:
- System Security Plan (SSP): boundary, data types, implemented controls, system description
- Security policies: access control, password, incident response, acceptable use
- Network architecture diagrams: verify they match the actual network
- Configuration standards: benchmarks, hardening guides, approved baseline configurations
- Change management records: compare approved changes to actual system state
- Audit logs: review for completeness and anomalies
- Incident records: review for recurring themes or unresolved incidents
- Risk assessment reports: verify identified risks have been addressed

**What to look for**:
- Outdated documents (review dates, software versions no longer in use)
- Inconsistencies between the SSP and actual configuration
- Absence of required documents
- Policies that have not been reviewed within the required time period

---

### Log Review

**Purpose**: Identify indicators of attack, policy violations, or operational anomalies by examining log records.

**Log sources to review**:
- Operating system security logs: failed logons, privilege escalation, account creation/deletion
- Application logs: access denied events, error conditions, unusual query patterns
- Network device logs: firewall denies, unusual traffic patterns, large data transfers
- Authentication logs: logon anomalies, after-hours access, geographic impossibility
- Web server access logs: unusual URL patterns (traversal attempts, injection strings)

**What to look for**:
- Unusually high volume of failed authentications (brute-force indicator)
- Access to sensitive resources at unusual times
- Outbound connections to unusual IP addresses or geographies
- Large data transfers (potential exfiltration)
- Cleared or missing log segments (potential log tampering or evasion)

---

### Ruleset Review

**Purpose**: Evaluate the security effectiveness of firewall, router ACL, IDS/IPS, and security group rules.

**For firewall rule review**:
1. Obtain the full rule export (not just a summary)
2. Review for: default deny at the end of all rulesets, any-any rules, overly broad source or destination, unnecessary open ports
3. Compare open ports against the approved service list in the SSP
4. Check for rules that are no longer needed (orphaned rules for decommissioned systems)
5. Verify management plane access (SSH, HTTPS, SNMP) is restricted to authorised management networks

**For IDS/IPS rule review**:
1. Verify signature/rule set is current
2. Confirm relevant attack categories are enabled (not operating in a default or minimal mode)
3. Review any rules that have been disabled and verify the justification

---

### System Configuration Review

**Purpose**: Compare actual system configuration against the approved baseline or industry hardening standard.

**Approach**:
1. Export current configuration settings (OS audit policy, service list, registry settings, software inventory)
2. Compare against approved baseline (CIS Benchmark, DISA STIG, vendor hardening guide, or agency-defined baseline)
3. Document deviations with their security impact
4. Confirm patch level: compare installed patches against available patches for the OS and all installed software

**Configuration areas to review**:
- User accounts (disabled/default accounts, account permissions)
- Services and processes (unnecessary services running)
- Network exposure (open ports/services not needed)
- Audit/logging settings (what events are logged)
- Password settings (complexity, minimum length, history)
- Encryption settings (protocols enabled, cipher suites)

---

### Network Sniffing (Passive Traffic Analysis)

**Purpose**: Capture and analyse network traffic to identify security-relevant information: cleartext credentials, unencrypted sensitive data, protocol vulnerabilities.

**Safeguards**: Network sniffing on production networks may capture user data. The following safeguards are required:
- Written authorisation from the system owner is required
- Traffic capture is limited to the authorised network segment and time window
- Captured data must be reviewed only by authorised personnel and destroyed after the assessment
- PII, financial data, and credentials in captured traffic must not be retained beyond the scope of the immediate finding

**What to look for**:
- Cleartext credentials (HTTP Basic Auth, FTP, Telnet, SNMP v1/v2)
- Cleartext session tokens or cookies
- Unencrypted sensitive data (personal information, financial data)
- Unusual protocols or unexpected traffic patterns
- Broadcast traffic revealing network topology

---

### File Integrity Checking

**Purpose**: Detect whether files have been modified unexpectedly, which may indicate compromise, unauthorised change, or misconfiguration.

**Approach**:
1. Compare current file hashes against a known-good baseline
2. Files of interest: operating system binaries, configuration files, authentication databases, audit log files
3. Any difference between current hash and baseline hash constitutes a potential finding

---

## Target Identification and Analysis Techniques (Section 4)

### Network Discovery

**Host Discovery Techniques**:
| Technique | Method | Limitations |
|-----------|--------|------------|
| ICMP Echo Request (ping) | Send ICMP echo; wait for reply | Blocked by most firewalls; unreliable for full host census |
| TCP SYN to common ports | Send SYN to port 80, 443, 22; any response indicates live host | Some hosts only expose closed ports |
| ARP Request (local subnet) | Layer 2; cannot be blocked by host firewalls | Limited to local segment |
| DNS Reverse Lookup | PTR record query for each IP | Only useful when reverse DNS is maintained |

---

### Port and Service Scanning

**Port States**:
- **Open**: Service actively accepting connections
- **Closed**: No service; host is reachable; RST returned
- **Filtered**: No response; firewall may be dropping packets

**Scan Types**:
| Type | Description | Detectability | Reliability |
|------|-------------|--------------|-------------|
| TCP SYN (half-open) | Sends SYN; waits for SYN-ACK; sends RST | Moderate (logged by most IDS) | High |
| TCP Connect | Full three-way handshake | High (fully logged by application and OS) | Highest |
| UDP | Sends UDP datagrams; ICMP unreachable = closed; no response = open or filtered | Low | Lower (slow; unreliable) |
| FIN/XMAS/NULL | Non-standard flag combinations; bypasses some basic firewalls | Variable | Less reliable on Windows |

**Service Version Detection**: Send protocol-specific probes to open ports to identify service name and version. Banner grabbing extracts service announcement strings.

---

### Vulnerability Scanning

**Network-Based Scanning** (unauthenticated):
- Tests visible services from the network perspective
- Infers vulnerability based on service version and banner information
- May produce false positives if version is patched without changing the banner

**Credentialed Scanning** (authenticated):
- Logs into each host using provided credentials
- Checks installed software versions, patch levels, local configuration
- More accurate; fewer false positives
- Requires credentials to be provided in the scanner configuration; credentials must be handled securely

**Scan Validation**:
Every finding from an automated scanner must be manually verified before reporting:
1. Confirm the service/version is actually running
2. Test whether the specific vulnerability is actually present (version check vs. proof-of-concept)
3. Identify compensating controls that may reduce the effective risk

---

### Wireless Security Assessment

**Passive Scanning**:
- Capture all 802.11 beacon frames in range
- Record: SSID, BSSID, channel, supported rates, encryption type, vendor OUI
- Identify: hidden SSIDs (detected via probe responses), deauthentication frames (potential DoS)

**Active Assessment**:
- **WEP identification**: WEP is cryptographically broken; if identified, it is a Critical finding
- **WPA/WPA2 assessment**: Check for WPA TKIP (deprecated); confirm WPA2-CCMP (AES) or WPA3
- **Enterprise vs. Personal**: Verify whether WPA2-Enterprise (802.1X) is used (preferred for government/enterprise networks) vs. pre-shared key (PSK)
- **Client isolation**: Verify whether clients on the WLAN can communicate with each other (if client isolation is required by policy)
- **Management frame protection**: Verify whether 802.11w Management Frame Protection (MFP) is enabled (protects against deauthentication attacks)
- **Rogue AP detection**: Scan for APs on unusual channels, APs with SSIDs matching the corporate network but different BSSIDs, or APs with unexpected vendor MAC prefixes

---

## Target Vulnerability Validation Techniques (Section 5)

### Password Cracking

**Authorised use context**: Credential capture (e.g., obtaining NTLM hashes via authenticated access to an AD domain controller or from a compromised system) followed by offline cracking — only under written authorisation.

**Methods**:
| Method | Description | Use Case |
|--------|-------------|---------|
| Dictionary attack | Test each word in a wordlist | Common/default/predictable passwords |
| Hybrid | Dictionary + rules (capitalise, append numbers, add special chars) | Passwords with minor complexity modifications |
| Brute force | Exhaustive search over character space | Short PINs, constrained character sets |
| Rainbow table | Pre-computed hash tables | Fast lookup against common unsalted hashes; ineffective against salted hashes |

**Reporting**: Document percentage of accounts cracked, time to crack, tool used. Do not include plaintext credentials in the report body — reference them in secured supplemental materials.

---

### Penetration Testing Techniques

**Exploitation progression**:
1. Identify a vulnerability confirmed by scanner and/or manual testing
2. Select applicable exploitation approach (public exploit, manual technique, custom script)
3. Execute exploit against the target (within authorised scope only)
4. Confirm successful exploitation (shell access, data access, privilege level obtained)
5. Document exact steps, commands, output, and screenshots

**Post-exploitation activities** (if authorised):
- Privilege escalation: attempt to gain higher privileges from current access level
- Lateral movement: from one compromised host, attempt to move to other hosts in scope
- Data access: identify what sensitive data would be accessible to an attacker with this level of access
- Persistence (if authorised): document what persistence mechanisms could be established (but clean up all artefacts)

**Cleanup requirements** (mandatory):
- Remove all tools, backdoors, and accounts created during the test
- Restore any settings modified to enable exploitation
- Remove all cached credentials
- Document all changes made to each system so that cleanup can be verified

---

### Social Engineering Techniques

**Phishing simulation methodology**:
1. Design a pretext (fake IT helpdesk, fake HR communication, fake vendor notification)
2. Send simulated phishing email to target population (using a landing page that captures clicks and optionally credential entries without storing real credentials)
3. Measure: open rate, click rate, credential entry rate, report rate
4. Debrief: notify all recipients after the campaign; provide training to those who took the bait

**Vishing methodology**:
1. Define pretext scenario (IT support, vendor audit, executive assistant)
2. Call a sample of employees from the target group
3. Attempt to elicit: credentials, software details, network topology, or to have the employee perform an action (e.g., disable an account, click a link)
4. Document: success rate, information obtained, length of call, awareness indicators (caller identified as suspicious)

**Physical social engineering** (most sensitive; requires tight scope control):
1. Tailgating: attempt to follow an authorised person through a controlled access point
2. Impersonation: pose as a vendor, contractor, or delivery person to gain access
3. Requires explicit authorisation from building security management and senior agency officials
4. Must have a clearly defined abort signal/code

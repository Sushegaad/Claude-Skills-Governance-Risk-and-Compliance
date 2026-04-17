# NIST SP 800-30 Rev 1 — Threat Source and Threat Event Taxonomy

Source: NIST SP 800-30 Rev 1, Appendices D and E (September 2012)

---

## Adversarial Threat Sources — Appendix D, Table D-1

| Threat Source | Tier | Capability | Characteristics |
|---------------|------|-----------|----------------|
| **Nation-State / APT** | 1, 2, 3 | High to Very High | Nation-states conduct sophisticated, persistent, targeted campaigns against government and critical infrastructure. Motivated by espionage, disruption, or sabotage. Employ zero-days, supply chain attacks, and insider recruitment. |
| **Organised Cyber Criminal** | 2, 3 | Moderate to High | Well-resourced criminal groups primarily motivated by financial gain. Conduct ransomware campaigns, business email compromise (BEC), credential theft, and fraud. Use affiliate models (Ransomware-as-a-Service). |
| **Hacktivist** | 2, 3 | Low to Moderate | Individuals or groups acting from ideological or political motivation. Primarily disruptive (DDoS, defacement, data leaks). Target organisations perceived as opposed to their cause. |
| **Insider — Malicious** | 1, 2, 3 | Low to High | Current or former employees, contractors, or partners with authorised access using that access intentionally to cause harm. Motivations include financial gain, grievance, coercion, or ideology. |
| **Insider — Inadvertent** | 1, 2, 3 | N/A | Authorised users who cause harm through error, negligence, or lack of awareness without malicious intent. Highest frequency of incidents; often triggered by phishing, mistakes, or policy non-compliance. |
| **Business Competitor** | 1, 2, 3 | Low to Moderate | Organisations or individuals seeking competitive advantage through corporate espionage, intellectual property theft, or market manipulation. |
| **Terrorist** | 1, 2, 3 | Low to Moderate | Entities seeking to cause widespread physical, social, or economic disruption. May target critical infrastructure systems controlling physical processes. |
| **Script Kiddie / Opportunist** | 3 | Very Low to Low | Inexperienced attackers using publicly available tools and exploits. Typically opportunistic; exploit known vulnerabilities without specific targeting. High volume, low sophistication. |
| **Supplier / Third Party** | 2, 3 | Variable | Entities with legitimate access to systems or data through business relationships. May introduce vulnerabilities through compromised software, hardware, or services, intentionally or by accident. |

---

## Non-Adversarial Threat Sources — Appendix D, Table D-2

| Threat Source | Description | Examples |
|---------------|-------------|---------|
| **Authorised user (error)** | Unintentional actions by users with legitimate access | Accidental file deletion, misconfiguration, sending sensitive data to wrong recipient |
| **System / software failure** | Technical failure of hardware, operating systems, or applications | Disk failure, memory corruption, database crash, firmware bug |
| **Environmental — natural** | Natural physical events beyond organisational control | Flood, earthquake, hurricane, tornado, wildfire, extreme temperature |
| **Environmental — man-made** | Physical events caused by human activity in the vicinity | Power grid failure, construction disruption, HVAC malfunction, water pipe burst |

---

## Adversarial Threat Events — Appendix E, Table E-2

### Reconnaissance and Intelligence Gathering

| Event | Description |
|-------|-------------|
| Network/port scanning | Automated discovery of open ports and services on target networks |
| Open-source intelligence (OSINT) | Collection of publicly available information about personnel, infrastructure, and technology |
| Social engineering reconnaissance | Targeted interaction with employees to gather information about systems, processes, or credentials |
| Spear phishing for credentials | Targeted phishing to harvest authentication credentials |
| Physical surveillance | Observation of facilities, personnel, or equipment |

### Initial Access

| Event | Description |
|-------|-------------|
| Spear phishing with malicious attachment | Targeted email with malware-laden attachment exploiting user execution |
| Exploitation of public-facing application | Use of CVEs against internet-facing services (web apps, VPNs, email gateways) |
| Valid account abuse | Use of legitimately obtained credentials (purchased, phished, or stolen) |
| Supply chain compromise — software | Malicious code injected into legitimate software updates or development tools |
| Supply chain compromise — hardware | Counterfeit or tampered hardware components containing implants |
| Trusted relationship exploitation | Leveraging access of IT providers, MSPs, or auditors as initial access vector |

### Execution and Persistence

| Event | Description |
|-------|-------------|
| Malware installation | Deployment of trojans, backdoors, or remote access tools |
| Scheduled task / startup item creation | Establishing persistence in OS scheduling or startup mechanisms |
| Registry modification | Inserting malicious entries into Windows registry for persistence |
| Living-off-the-land (LOTL) | Abuse of legitimate system tools (PowerShell, WMI, certutil) to avoid detection |
| Web shell deployment | Installing server-side scripts on compromised web servers for persistent access |

### Privilege Escalation

| Event | Description |
|-------|-------------|
| Credential dumping | Extraction of hashed or plaintext credentials from memory or registry |
| Pass-the-hash / pass-the-ticket | Use of captured credential hashes or Kerberos tickets without knowing plaintext passwords |
| Exploitation of misconfigured permissions | Leveraging overly permissive ACLs, sudo rules, or service accounts |
| Token impersonation | Abusing Windows token privileges to escalate to SYSTEM |

### Lateral Movement

| Event | Description |
|-------|-------------|
| Remote service exploitation | Exploiting CVEs in internal services (SMB, RDP, databases) for lateral movement |
| Remote desktop protocol (RDP) abuse | Use of valid or stolen credentials to connect to other internal systems |
| Pass-the-hash lateral movement | Using captured NTLM hashes to authenticate to additional systems without cleartext passwords |
| Network enumeration | Discovery of internal hosts, services, and trust relationships |
| Active Directory attack | Kerberoasting, AS-REP roasting, DCSync, Golden/Silver Ticket attacks |

### Exfiltration

| Event | Description |
|-------|-------------|
| Data exfiltration to cloud storage | Upload of stolen data to attacker-controlled cloud services (S3 buckets, Google Drive, compromised SaaS) |
| Removable media exfiltration | Copying sensitive data to USB drives or other physical media |
| Covert channel exfiltration | Use of DNS tunnelling, ICMP, or encoded HTTP requests to exfiltrate data undetected |
| Email exfiltration | Sending bulk sensitive data as attachments to external accounts |

### Impact

| Event | Description |
|-------|-------------|
| Ransomware deployment | Encryption of critical systems and data; extortion demand for decryption key |
| Data destruction | Deletion or overwriting critical data or system files |
| Denial-of-service attack | Volumetric, protocol, or application-layer attacks to exhaust resources |
| System sabotage | Destruction or manipulation of physical systems through compromised control systems (OT/ICS) |
| Data modification | Subtle alteration of critical data to introduce errors or fraud without immediate detection |

---

## Non-Adversarial Threat Events — Appendix E, Table E-3

| Event | Threat Source | Description |
|-------|--------------|-------------|
| Accidental deletion | Authorised user | Unintentional removal of production data or configuration files |
| Misconfiguration | Authorised user | Incorrect firewall rule, open S3 bucket, disabled logging |
| Disk array failure | Hardware | RAID failure causing data loss or unavailability |
| Database crash | Software | Application or database failure causing data corruption or unavailability |
| Power outage | Environmental | Loss of utility power causing system shutdown |
| Flooding | Environmental | Physical water intrusion into data centre or office affecting hardware |
| Fire | Environmental | Physical fire damaging equipment and data |
| HVAC failure | Environmental | Overheating of server rooms causing hardware shutdowns or damage |
| Network outage | Structural / Environmental | ISP or internal switching failure causing loss of connectivity |

---

## MITRE ATT&CK Mapping to SP 800-30 Threat Events

SP 800-30 threat events map to MITRE ATT&CK tactics for operational threat modelling:

| SP 800-30 Category | MITRE ATT&CK Tactic |
|--------------------|--------------------| 
| Reconnaissance | TA0043 — Reconnaissance |
| Initial Access | TA0001 — Initial Access |
| Execution and Persistence | TA0002 — Execution; TA0003 — Persistence |
| Privilege Escalation | TA0004 — Privilege Escalation; TA0006 — Credential Access |
| Lateral Movement | TA0008 — Lateral Movement |
| Exfiltration | TA0010 — Exfiltration |
| Impact | TA0040 — Impact |

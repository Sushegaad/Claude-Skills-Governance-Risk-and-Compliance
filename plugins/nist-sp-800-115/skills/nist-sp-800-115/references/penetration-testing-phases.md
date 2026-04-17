# Penetration Testing Phases — NIST SP 800-115

Source: NIST SP 800-115 (September 2008), Sections 5–7

---

## Overview of the SP 800-115 Testing Process

SP 800-115 describes a four-phase technical testing process:

1. **Planning** — Define scope, objectives, rules, and logistics
2. **Discovery** — Identify targets and gather information
3. **Attack** — Validate vulnerabilities through controlled exploitation
4. **Reporting** — Document findings with risk context and remediation guidance

Each phase must be completed in sequence. No attack activity should begin until the Planning phase is complete and a signed authorisation is in hand.

---

## Phase 1 — Planning

### Authorisation Requirements

Before any testing activity begins, the following must be in place:
- Written authorisation from the official with authority to authorise testing (system owner, AO, or designated official)
- Signed Rules of Engagement document (see SKILL.md Section 1.2 for RoE elements)
- Identification of any third-party systems that may be incidentally tested (e.g., shared hosting, cloud providers) and explicit decisions on whether such testing is permitted

### Threat Modelling for Penetration Tests

To focus the assessment on the most relevant risks, define the threat model:
1. What type of attacker is being simulated? (external/internet-based, insider/trusted user, nation-state)
2. What is the attacker's assumed starting position? (no access / user access / admin access)
3. What is the primary target? (sensitive data, system availability, authentication bypass)
4. What attack paths are most relevant to the organisation's threat landscape?

### Testing Approach Selection

| Approach | Starting Knowledge | Simulates | When to Use |
|---------|-------------------|-----------|----|
| Black-box | None | External attacker with no access | Testing external-facing systems; assessing perimeter effectiveness |
| Grey-box | Partial (network diagram, user credentials) | Insider, compromised vendor, or partially informed attacker | More efficient; covers both external and internal attack paths |
| White-box | Full (source code, architecture docs, admin credentials) | Sophisticated attacker with insider knowledge | Maximum coverage; developer-focused testing; source code review included |

---

## Phase 2 — Discovery

### Step 1 — Passive Information Gathering

Before sending a single packet to target systems, gather publicly available information:
- WHOIS registrations (domain owner, registrar, nameservers, contact info)
- DNS enumeration (A, MX, NS, CNAME, TXT, SPF records; attempt zone transfer)
- Public search engines (cached pages, PDF metadata, exposed files)
- Job postings (reveal technology stack, software versions, tools in use)
- Social media (employee technology discussions)
- Pastebin and GitHub (leaked credentials, internal hostnames, API keys)

### Step 2 — Network Reconnaissance

Active discovery within the authorised scope:

**Host Discovery** (structured by technique reliability):
```
Priority 1 (most reliable): ARP requests (local subnet only)
Priority 2: TCP SYN to 80, 443, 22, 3389
Priority 3: ICMP echo request (may be filtered)
Priority 4: UDP to DNS (53), SNMP (161)
```

**Port Scanning**:
- Start with top 1000 ports (covers >95% of common services): TCP SYN scan
- Follow with full port range (1-65535) on priority targets
- Add UDP scan for key services: DNS (53), DHCP (67/68), TFTP (69), SNMP (161/162), NTP (123)
- Service version detection on all open ports
- OS fingerprinting on priority targets

**Service Enumeration** (per discovered service):
| Service | Port | Enumeration Technique |
|---------|------|----------------------|
| HTTP/HTTPS | 80/443 | Banner grab; directory enumeration; robots.txt; application fingerprinting |
| SSH | 22 | Version disclosure; supported algorithms |
| SMB | 445 | Share enumeration; null session test; signing check |
| LDAP | 389/636 | Directory enumeration; null bind test |
| RDP | 3389 | Protocol version; NLA requirement check |
| SNMP | 161 | Community string check (public/private); if accessible: full MIB walk |
| DNS | 53 | Zone transfer; recursive query test; DNSSEC check |
| SMTP | 25 | Banner; open relay test; VRFY/EXPN command test |

### Step 3 — Vulnerability Identification

After completing discovery:
1. Run automated vulnerability scanner (network-based, with target list from discovery)
2. Run credentialed scan on priority targets if authorised
3. Review scanner output: categorise all findings into True Positive / Needs Validation / Likely False Positive
4. Prioritise True Positives by CVSS score for Phase 3

---

## Phase 3 — Attack

### Step 1 — Vulnerability Validation (Proof-of-Concept Testing)

For each priority vulnerability:
1. Verify the specific version and service are actually present (check version disclosure, not just CVE match)
2. Check for available public exploits (CVE databases, security advisories)
3. Attempt exploitation in a controlled manner; document: exact command, timestamp, response
4. Classify: Exploited (confirmed) / Not Exploited (false positive or patched) / Partially Exploited (partial bypass)

### Step 2 — Initial Access Techniques by Category

**Network services exploitation**:
- Exploit publicly accessible vulnerable services (e.g., unauthenticated remote code execution)
- Test for default credentials on network devices and services
- Attempt exploitation of exposed administrative interfaces (web admin, SNMP write)

**Authentication bypass**:
- SQL injection on login forms → authentication bypass
- Weak session tokens → session hijacking
- Missing MFA → credential stuffing with known breached credentials

**Client-side exploitation** (if browser/email client testing is in scope):
- Phishing with malicious document (macro-based) delivered to target user
- Testing whether security awareness training is effective against simulated spear-phishing

### Step 3 — Privilege Escalation (Post-Initial-Access)

After obtaining initial access (user-level), escalation techniques:

**Windows environments**:
- Unquoted service paths with write permission in path components
- Writable service binaries
- AlwaysInstallElevated registry key
- Token impersonation (if SeImpersonatePrivilege available)
- Kerberoasting (requesting service tickets for service accounts; crack offline)
- Pass-the-Hash (if NTLM hashes obtained)
- GPO misconfiguration (write access to GPOs or the OU they apply to)

**Linux/Unix environments**:
- SUID binaries with unintended privilege elevation
- Sudo misconfigurations (NOPASSWD entries, wildcard paths)
- World-writable cron jobs
- Path hijacking in root-owned scripts
- Weak file permissions on sensitive files (/etc/passwd, service configuration files)

### Step 4 — Lateral Movement (Post-Escalation)

From a privileged compromise, assess internal network reach:
- Pass-the-Hash / Pass-the-Ticket to authenticate to other systems with harvested credentials
- SMB share access to locate sensitive data
- WMI / PowerShell remoting to execute commands on remote systems
- Internal port scan to identify systems accessible from the compromised host that were not accessible externally

### Step 5 — Data Access Assessment

Document what sensitive data would be accessible:
- Identify sensitive data stores reachable from compromised position
- Confirm whether DLP, encryption at rest, or access controls prevent access
- Record the finding: "From [compromised system], an attacker can access [data store] containing [data type]"
- Do not exfiltrate real sensitive data; document the access path only

### Step 6 — Cleanup (Mandatory)

After completing the exploitation phase:

| Artifact Type | Cleanup Action |
|--------------|--------------|
| Created user accounts | Delete every account created during the test |
| Uploaded tools/scripts | Remove all files uploaded to target systems |
| Modified registry keys | Restore original values |
| Modified configuration files | Restore original content |
| Scheduled tasks or services | Remove all persistence mechanisms created |
| Cached credentials | Clear from all compromised systems |
| Exploitation log | Cross-reference each action with cleanup verification |

Sign off on cleanup: document that each step above was completed and verified.

---

## Phase 4 — Reporting

### Finding Documentation Format

For each unique finding, document:

```
Finding ID:      [PT-YYYY-NNN]
Severity:        Critical / High / Moderate / Low / Informational
CVSS Score:      [if applicable, provide Base Score]
CVE:             [if applicable]
Affected Systems: [list of IPs/hostnames]

Title:           [Clear, specific title — e.g., "Unauthenticated Remote Code Execution
                  on Public Web Application (CVE-YYYY-XXXXX)"]

Description:     [What the vulnerability is; why it exists; what can be done with it]

Steps to Reproduce (Proof of Exploitation):
                 [Exact commands and output demonstrating exploitability — use screenshots
                  for critical/high severity findings. This section is what distinguishes
                  a penetration test finding from a scanner finding.]

Impact:          [What an attacker gains from exploiting this; what data or systems would
                  be at risk; what the business impact would be]

Evidence:        [Tool output, screenshots, log excerpts]

Recommendation:  [Specific, actionable remediation. For patching: identify the specific
                  patch/version to upgrade to. For configuration: specify the exact
                  setting change. For architecture: describe the required design change.]

References:      [CVE, NVD, vendor advisory, NIST 800-53 control(s), CWE]
```

### Report Handling and Distribution

- Classify the report at a level appropriate to its contents (e.g., FOUO if it contains system vulnerability details)
- Distribute only via encrypted channels
- Maintain a record of who received each copy
- Destroy digital and physical copies per the agreed data handling procedure once remediation is complete or the retention period expires
- Do not include live credentials, cryptographic keys, or hashes in the report body — reference them in a separately secured addendum if absolutely required

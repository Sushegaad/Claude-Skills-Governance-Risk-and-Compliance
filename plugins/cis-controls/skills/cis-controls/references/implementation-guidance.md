# CIS Controls v8 - Implementation Guidance

## Getting Started: The Prioritization Principle

The CIS Controls are deliberately ordered by impact. Research consistently shows that implementing Controls 1–6 (the foundational six) eliminates the vast majority of cyber risk:

- **Controls 1–2** (Inventory): You can't protect what you don't know you have
- **Controls 3–6** (Protective): Prevent the most common attack paths
- **Control 7** (Vulnerability Management): Continuously reduce attack surface
- **Controls 8–18** (Detect, Respond, Recover): Build operational security capability

Start with IG1 completely before moving to IG2. IG1 is the minimum acceptable baseline for any organization.

---

## Implementation Group 1 (IG1) - Essential Cyber Hygiene

**Target audience:** Organizations with limited IT resources, small teams, commercially available products
**Goal:** Defend against opportunistic, non-targeted attacks (the majority of incidents affecting small organizations)

### IG1 Quick-Start Checklist (56 Safeguards)

**Week 1-2: Know Your Assets**
- [ ] Create hardware asset inventory (all computers, servers, printers, network devices) - Safeguard 1.1
- [ ] Create software inventory (all installed applications) - Safeguard 2.1
- [ ] Document all user accounts - Safeguard 5.1
- [ ] Document all data types and where they are stored - Safeguard 3.2

**Week 3-4: Secure Configuration**
- [ ] Enable host-based firewall on all workstations and servers - Safeguards 4.4, 4.5
- [ ] Set screen lock timeout to 15 minutes - Safeguard 4.3
- [ ] Change all default passwords on network devices, routers, and systems - Safeguard 4.7
- [ ] Enable full-disk encryption on all laptops - Safeguard 3.6

**Month 2: Account and Access Controls**
- [ ] Enforce strong password policy (14+ characters) - Safeguard 5.2
- [ ] Separate admin accounts from day-to-day user accounts - Safeguard 5.4
- [ ] Disable accounts unused for 90+ days - Safeguard 5.3
- [ ] Define and document access request/revoke process - Safeguards 6.1, 6.2
- [ ] Require MFA for externally-exposed applications, remote network access, and admin access (Safeguards 6.3, 6.4, 6.5)

**Month 2: Patch Management**
- [ ] Enable automatic OS updates on all endpoints - Safeguard 7.3
- [ ] Enable automatic application updates (browsers, Office, etc.) - Safeguard 7.4
- [ ] Define a remediation SLA (e.g., critical patches within 15 days) - Safeguard 7.2

**Month 3: Backups, Training, Incident Response**
- [ ] Implement automated, tested, protected backups (3-2-1 rule) - Safeguards 11.2, 11.3, 11.4
- [ ] Conduct security awareness training for all employees - Safeguard 14.1, 14.2
- [ ] Designate incident handling personnel and document the incident reporting process - Safeguards 17.1, 17.2, 17.3
- [ ] Enable and retain basic audit logs with adequate storage (auth events, admin actions) - Safeguards 8.1, 8.2, 8.3

---

## Implementation Group 2 (IG2) - Intermediate Controls

**Target audience:** Organizations with dedicated IT staff, sensitive data, moderate risk tolerance
**Goal:** Defend against more sophisticated, targeted attacks; comply with common regulatory frameworks

### Key IG2 Additions Beyond IG1

**MFA Hardening (Control 6)**
- Note: MFA safeguards 6.3, 6.4, and 6.5 are IG1 requirements; IG2 builds on them
- Inventory authentication/authorization systems and centralize access control (Safeguards 6.6, 6.7)
- Phishing-resistant MFA (FIDO2/hardware keys) for privileged users

**Application Allowlisting (Control 2)**
- Implement application allowlisting via Microsoft AppLocker, WDAC, or Carbon Black
- Allowlist approved scripts (PowerShell Constrained Language Mode) - Safeguard 2.7 (IG3)
- Block unauthorized DLLs and libraries - Safeguard 2.6

**Vulnerability Scanning (Control 7)**
- Deploy authenticated vulnerability scanner (Nessus, Qualys, Tenable, Rapid7)
- Weekly authenticated scans of all internal assets - Safeguard 7.5
- Monthly scans of external attack surface - Safeguard 7.6
- Track and remediate findings per SLA - Safeguard 7.7

**SIEM and Log Centralization (Control 8)**
- Deploy SIEM or log aggregation platform - Safeguard 8.9
- Collect: Windows event logs (4624, 4625, 4648, 4720, 4728), Linux auth.log, firewall deny logs, DNS, VPN - Safeguard 8.5
- Retain logs for minimum 12 months - Safeguard 8.10
- Enable NTP synchronization across all assets - Safeguard 8.4

**Email Security (Control 9)**
- Implement DMARC policy (start with p=none monitoring, move to p=quarantine/reject) - Safeguard 9.5
- Deploy email filtering with sandboxing - Safeguard 9.7
- Block dangerous attachment types (.exe, .js, .vbs, .bat, .macro-enabled Office) - Safeguard 9.6

**EDR/Next-Gen AV (Control 10)**
- Replace signature-only AV with EDR/XDR (CrowdStrike, SentinelOne, Microsoft Defender for Endpoint) - Safeguard 10.7
- Enable behavioral analysis and memory protection - Safeguard 10.5

**Network Architecture (Control 12)**
- Segment network by function (servers, workstations, IoT, guest Wi-Fi) - Safeguard 12.2
- Implement DMZ for externally accessible services - Safeguard 12.2
- Deploy Next-Gen Firewall with deep packet inspection - Safeguard 12.2

**Vendor Risk Management (Control 15)**
- Classify all service providers by data access and criticality - Safeguard 15.3
- Include security requirements in all vendor contracts - Safeguard 15.4
- Conduct annual vendor risk assessments for critical suppliers - Safeguard 15.5

---

## Implementation Group 3 (IG3) - Advanced Controls

**Target audience:** Large enterprises with security teams, sensitive regulated data, high-value targets
**Goal:** Defend against sophisticated, persistent adversaries; maintain continuous security operations

### Key IG3 Capabilities

**Penetration Testing (Control 18)**
- External pen test: Annual minimum; quarterly for high-risk targets - Safeguard 18.2
- Internal pen test: Semi-annual - Safeguard 18.5
- Red team exercises with full adversary simulation - beyond base CIS scope
- Purple team exercises - combine red team and SOC for knowledge transfer

**Advanced Network Defense (Control 13)**
- Deploy Network Detection and Response (NDR/NTA) solution - Safeguard 13.3
- Implement SOAR for automated incident response playbooks
- HIPS on all servers - Safeguard 13.7
- Tune SIEM alert thresholds to reduce false positives - Safeguard 13.11
- Threat hunting program: proactive analysis for unknown threats

**Application Security (Control 16)**
- SAST integrated into CI/CD pipeline (pre-commit, PR gate) - Safeguard 16.12
- DAST for deployed applications (OWASP ZAP, Burp Suite) - Safeguard 16.12
- SCA for third-party components (Snyk, Black Duck) - related to 16.5
- Threat modeling for new features and applications - Safeguard 16.14
- Bug bounty program or responsible disclosure policy - related to 16.4

**Data Protection (Control 3)**
- Deploy DLP across email, endpoints, and cloud - Safeguard 3.13
- Segment data stores by sensitivity - Safeguard 3.12
- Log all access to sensitive data - Safeguard 3.14

---

## Common Implementation Pitfalls

### Pitfall 1: Skipping IG1 to implement IG2/IG3 Controls
**Problem:** Organizations try to deploy SIEM before they know what assets they have
**Solution:** Complete IG1 systematically before advancing. Asset inventory (Controls 1-2) is the foundation for everything else.

### Pitfall 2: Treating CIS Controls as a checklist, not a program
**Problem:** Point-in-time compliance; controls drift over time
**Solution:** Build operational processes: scheduled scans, monthly reporting, quarterly reviews, annual assessments

### Pitfall 3: Ignoring cloud assets
**Problem:** Cloud VMs, SaaS apps, cloud storage not included in inventory or scans
**Solution:** CIS Controls v8 explicitly addresses cloud assets - include in all inventories; use CSPM tools (Wiz, Prisma, Defender for Cloud)

### Pitfall 4: MFA deployment gaps
**Problem:** MFA enabled on some systems but not others; SMS OTP used for privileged access
**Solution:** Comprehensive MFA inventory; phishing-resistant MFA for privileged and external access

### Pitfall 5: Log collection without review
**Problem:** SIEM deployed but alerts are not actioned; logs retained but never searched
**Solution:** Define alert response procedures; staff SOC or use MDR service; weekly log review as minimum

### Pitfall 6: Patch management without vulnerability scanning
**Problem:** Patching OS only; missing application and firmware vulnerabilities
**Solution:** Authenticated vulnerability scanning to identify all missing patches, misconfigurations, and CVEs

---

## Metrics and KPIs for CIS Controls

### IG1 KPIs
| Metric | Target | Frequency |
|--------|--------|-----------|
| % assets in inventory | ≥ 95% | Monthly |
| % endpoints with current AV | 100% | Weekly |
| % endpoints with disk encryption | 100% | Monthly |
| Critical patches applied within SLA | ≥ 95% | Monthly |
| % accounts with strong passwords | 100% | Quarterly |
| Backup test success rate | 100% | Quarterly |

### IG2 KPIs
| Metric | Target | Frequency |
|--------|--------|-----------|
| % external systems with MFA | 100% | Monthly |
| Mean Time to Patch (MTTP) - Critical | ≤ 15 days | Monthly |
| Mean Time to Patch (MTTP) - High | ≤ 30 days | Monthly |
| SIEM alert response rate | ≥ 90% actioned | Weekly |
| Phishing click rate (simulation) | ≤ 5% | Quarterly |
| Vendor assessments completed | 100% of critical | Annual |

### IG3 KPIs
| Metric | Target | Frequency |
|--------|--------|-----------|
| Pen test critical findings remediated | 100% within 30 days | After test |
| Mean Time to Detect (MTTD) | ≤ 24 hours | Monthly |
| Mean Time to Respond (MTTR) | ≤ 4 hours for P1 | Monthly |
| SAST scan coverage | 100% of repos | Per commit |
| DLP policy violation rate | Trending down | Monthly |

---

## CIS CSAT Tool

The **CIS Controls Self-Assessment Tool (CSAT)** is a free web-based platform from CIS:
- URL: https://csat.cisecurity.org/
- Maps to all 153 safeguards
- Generates maturity scores and prioritized gap reports
- Supports team collaboration and tracking
- Produces executive summary reports

**CIS SecureSuite Membership** provides access to additional resources:
- CIS Benchmarks (configuration hardening guides for 100+ technologies)
- CIS-CAT Pro (automated configuration assessment tool)
- CIS RAM (Risk Assessment Method)
- Priority and quick-start guides by sector

---

## Industry-Specific Guidance

### Healthcare (HIPAA alignment)
- Priority: Controls 3 (PHI data protection), 6 (access control), 8 (audit logging), 17 (incident response)
- IG2 minimum for any covered entity or business associate
- Map CIS Controls to HIPAA Security Rule safeguards

### Finance (PCI DSS / GLBA alignment)
- Priority: Controls 3, 6, 8, 12, 16 for cardholder data environments
- IG2 minimum; IG3 for large financial institutions
- CIS Controls v8 maps closely to PCI DSS v4.0 requirements

### Government (FISMA / CMMC alignment)
- Priority: Full IG2 implementation for CMMC Level 2; IG3 elements for CMMC Level 3
- CIS Controls map to NIST SP 800-171 requirements used in CMMC
- Essential Eight (Australian cyber) aligns with CIS Controls 1-10

### Education (FERPA alignment)
- Priority: Controls 1-7 for student data protection
- IG1 minimum for K-12; IG2 for higher education with research data

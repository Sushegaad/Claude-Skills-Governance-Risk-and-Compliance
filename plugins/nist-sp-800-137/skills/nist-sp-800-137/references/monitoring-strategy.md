# NIST SP 800-137 — ISCM Strategy and Monitoring Programme Establishment

**Source**: NIST SP 800-137, September 2011, Sections 2.3, 3, 4, Appendix B

---

## ISCM Strategy Document Structure

The ISCM strategy is an organisation-level document approved by the CIO and/or Risk Executive Function. It governs the entire ISCM programme across all three tiers.

### Required Sections

**Section 1 — Introduction and Purpose**
- Organisation name and information system scope
- ISCM programme purpose and alignment to FISMA, OMB A-130, and applicable policies
- Relationship to the organisation's RMF and risk management programme

**Section 2 — Governance and Roles**
- Named roles per SP 800-137 Table 1 (CIO, SAISO, Risk Executive Function, AOs, ISOs, ISSOs, Common Control Providers)
- Accountability mapping (who is responsible for each ISCM task at each tier)
- Escalation chain

**Section 3 — Risk Tolerance**
- Organisational acceptable risk threshold (qualitative: Low/Moderate/High, or quantitative where defined)
- Risk tolerance by system impact level (FIPS 199 Low, Moderate, High)
- Conditions under which the AO will revoke or suspend authorisation

**Section 4 — Metrics Catalogue (by reference or included)**
- All approved ISCM metrics with full attribute sets
- Traceability to SP 800-53 Rev 5 control families

**Section 5 — Monitoring Frequency Schedule**
- Complete table mapping each metric to its assigned frequency
- Frequency basis (automation-driven, schedule-driven, event-driven)

**Section 6 — Data Collection Architecture**
- Tool inventory (name, type, SCAP validation status, coverage)
- Collection schedule
- Security data repository location and access controls
- Data retention periods

**Section 7 — Aggregation and Reporting**
- Tier 3 → Tier 2 → Tier 1 data flow description
- Report formats and templates (by reference to templates)
- Report distribution (who receives what level of report)
- Reporting frequency per tier

**Section 8 — Response Procedures**
- Remediation timeframe table (Critical/High/Medium/Low)
- Risk acceptance authority at each tier
- POA&M management procedures
- AO notification triggers

**Section 9 — Review and Update Cycle**
- Periodic review frequency (minimum annual)
- Event-driven review triggers
- Approval process for strategy updates

**Section 10 — Document Control**
- Version number, approval date, approving official, next review date

---

## Monitoring Frequency Assignment

### Criteria for Frequency Selection

Four factors govern frequency selection:

**1. Information Volatility**
How rapidly does the monitored condition change on its own?
- Software versions and patch state: changes with vendor releases (can be daily to quarterly)
- Configuration settings: can change at any time (human or automated)
- Vulnerability exposure: changes as CVEs are published (daily)
- Access control lists: change with personnel actions (event-driven)

**2. Adversary Speed of Exploitation**
How quickly can an adversary exploit a discovered vulnerability?
- Known exploited vulnerabilities (KEV, CISA): hours to days
- Public proof-of-concept exploits: days
- High-complexity exploits: weeks to months
- Low-value targets, no public exploit: months

**3. CIA Impact**
What is the potential impact if the control fails?
- High impact systems: require more frequent monitoring to reduce risk exposure window
- Low impact systems: less frequent monitoring may be acceptable

**4. Automation Feasibility**
- If monitoring can be fully automated, continuous or daily monitoring is achievable at low cost
- If monitoring requires manual effort, frequency must be balanced against resources

### Frequency Assignment Table Template

| Control Family | Control ID | Metric | Frequency | Automation |
|---|---|---|---|---|
| Access Control | AC-2 | Inactive accounts (>30 days) | Weekly | Semi-automated |
| Access Control | AC-7 | Failed login threshold per policy | Continuous | Automated |
| Configuration Management | CM-6 | Configuration compliance vs. baseline | Daily | Automated |
| Configuration Management | CM-7 | Non-whitelisted software detected | Daily | Automated |
| Incident Response | IR-6 | Incidents reported within required timeframe | Weekly | Semi-automated |
| Maintenance | MA-2 | Scheduled maintenance records current | Monthly | Manual |
| Media Protection | MP-6 | Sanitization records current | Quarterly | Manual |
| Risk Assessment | RA-5 | Vulnerability scan age | Weekly (High+); Monthly (Mod/Low) | Automated |
| System and Communications | SC-28 | Encryption-at-rest compliance | Monthly | Semi-automated |
| System and Information Integrity | SI-2 | Critical/High patches applied within SLA | Daily | Automated |
| System and Information Integrity | SI-3 | AV definition currency | Continuous | Automated |
| System and Information Integrity | SI-4 | IDS/IPS alert processing within SLA | Continuous | Automated |

**Note**: This table is illustrative. Each organisation must define the complete frequency mapping for all controls in scope based on the four criteria above.

---

## Control Selection for ISCM

Not all SP 800-53 controls are equally suited to automated continuous monitoring. Controls are classified by their amenability to automation:

### Tier A — Highly Amenable to Automation (Continuous or Daily Monitoring)

These controls produce machine-readable, quantifiable outputs that scanners and SCAP tools can assess:
- SI-2 (Flaw Remediation / Patch Management)
- SI-3 (Malicious Code Protection — AV currency)
- SI-4 (Information System Monitoring — IDS/IPS alert status)
- CM-6 (Configuration Settings — SCAP/XCCDF checklist compliance)
- CM-7 (Least Functionality — software whitelist compliance)
- AC-7 (Unsuccessful Logon Attempts — log-based)
- AU-2/AU-3 (Audit Events/Content — log completeness and current)
- IA-5 (Authenticator Management — password age, MFA status)

### Tier B — Amenable to Semi-Automated or Periodic Monitoring (Weekly to Monthly)

These controls require some human triage or configuration to monitor:
- AC-2 (Account Management — account review against HR records)
- AC-17 (Remote Access — VPN session and configuration review)
- RA-5 (Vulnerability Scanning — scan results reviewed and triaged)
- SC-28 (Protection of Information at Rest — cryptographic status)
- CP-9 (Information System Backup — backup job status review)
- PE-3 (Physical Access Control — access log review)

### Tier C — Primarily Manual Assessment (Quarterly to Annual)

These controls require human assessment and cannot be effectively automated:
- AT-2/AT-3 (Security Training Awareness/Role-Based Training — completion records)
- PL-2 (System Security Plan — currency review)
- PS-3/PS-4/PS-5 (Personnel Screening, Termination, Transfer)
- CP-4 (Contingency Plan Testing — tabletop or test results)
- CA-2 (Security Assessments — formal assessment activities)
- IR-3 (Incident Response Testing)

---

## ISCM Programme Establishment Procedures

### Step A — Tool Selection Criteria

For each Tier A metric, identify a candidate tool:

| Criterion | Requirement |
|---|---|
| SCAP validation | Required for Tier A controls (CVE, CCE, CPE, CVSS, OVAL, XCCDF support) |
| Coverage | Must scan all in-scope assets within the monitoring cycle |
| Authentication | Credentialed scanning required for configuration and patch assessment |
| Reporting | Must produce output in ARF or otherwise importable to security data repository |
| Access control | Tool must enforce least privilege; credentials stored securely |
| Logging | Tool operations must be logged for audit |

### Step B — Baseline Establishment

**Configuration Baseline**:
1. Identify applicable NIST SP 800-70 National Checklist Program (NCP) baseline for each platform
2. Customise baseline where organisational policy deviates (document rationale for every deviation)
3. Encode baseline in XCCDF checklist for automated scanning
4. Obtain ISO approval of the final baseline document
5. Import baseline into ISCM tool as the authorised configuration profile

**Software Baseline**:
1. Inventory all authorised software on each system (name, version, publisher)
2. Create approved software list (whitelist) per system category or role
3. Configure CM tool to alert on deviations from approved list

**Patch Baseline**:
1. Define patching SLAs per severity (Critical: 15 days; High: 30 days; Medium: 90 days; Low: 180 days)
2. Document approved exceptions (compensating controls for systems that cannot be patched)
3. Configure vulnerability scanner to alert on CVEs that exceed the SLA window

### Step C — Data Repository Architecture

**Minimum security controls for the ISCM data repository**:
- Access limited to ISCM personnel and AOs (least privilege)
- Data encrypted at rest and in transit
- Audit log of all access and query activity
- Backup and availability controls to ensure historical data is retained for trend analysis
- Data integrity controls (signed exports, hash validation for archived data)

**Data retention**:
- Raw scan results: minimum 12 months for trend analysis
- Aggregated reports: minimum 3 years (consistent with FISMA reporting cycles)
- POA&M history: life of the system

---

## Organisational ISCM Maturity

ISCM programmes mature over time. A notional maturity progression:

| Level | Description | Characteristics |
|---|---|---|
| Level 1 — Ad hoc | No formal ISCM programme | Manual periodic assessments only; no defined metrics or frequencies |
| Level 2 — Defined | ISCM strategy documented | Metrics defined; frequencies assigned; tools identified but not fully deployed |
| Level 3 — Consistently implemented | Programme operational | Automated collections running; Tier 3 reporting in place; POA&M managed |
| Level 4 — Managed | Aggregated and reported | Tier 2 and Tier 1 aggregation functional; AO receives ISCM-based status reports |
| Level 5 — Optimised | Continuous improvement | Ongoing authorisation in use; metrics refined based on threat intelligence; programme drives risk decisions |

---

## CDM Programme Integration

The DHS Continuous Diagnostics and Mitigation (CDM) programme provides federal civilian agencies with ISCM capabilities aligned to SP 800-137. CDM capability layers:

| CDM Capability Layer | What It Monitors | SP 800-137 Tier |
|---|---|---|
| Layer 1 — What is on the network | Hardware and software asset management (HWAM/SWAM) | Tier 3 |
| Layer 2 — Who is on the network | Configuration management, vulnerability management | Tier 3 |
| Layer 3 — What is happening on the network | Identity and access management | Tier 3 |
| Layer 4 — How data is protected | Data protection management | Tier 3 / Tier 2 |
| Dashboard | Agency-wide security status | Tier 1 / Tier 2 |

CDM tools deployed at agencies map to ISCM Tier A controls and feed the agency ISCM data repository and the CDM Agency Dashboard. The CDM Federal Dashboard provides DHS/CISA with aggregated federal ISCM data for Tier 1 government-wide reporting.

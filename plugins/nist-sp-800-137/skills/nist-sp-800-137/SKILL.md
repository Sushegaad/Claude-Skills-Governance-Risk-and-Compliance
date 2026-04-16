---
name: nist-sp-800-137
description: >
  NIST SP 800-137 Information Security Continuous Monitoring (ISCM) skill. Answers questions about
  designing and implementing ISCM strategies, defining monitoring frequencies, selecting security
  metrics, establishing ISCM programmes, automating assessments using SCAP, ARF, and XCCDF, reporting
  security status to authorizing officials, integrating ISCM with the Risk Management Framework Step 6,
  defining roles and responsibilities for ISCM, analysing findings and responding to identified risks,
  reviewing and updating ISCM strategies, three-tier ISCM architecture (organisation, mission/business
  process, information system), ongoing authorization decisions, continuous diagnostics and mitigation,
  and federal information system monitoring requirements under FISMA.
---

# NIST SP 800-137 — Information Security Continuous Monitoring (ISCM)

**Source**: NIST Special Publication 800-137, September 2011
**Full Title**: Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations
**CSRC URL**: https://csrc.nist.gov/publications/detail/sp/800-137/final

---

## Purpose and Scope

NIST SP 800-137 provides guidance for the development and implementation of an organisation-wide Information Security Continuous Monitoring (ISCM) strategy and programme. The goal is to maintain ongoing awareness of information security, vulnerabilities, and threats to support organisational risk management decisions.

ISCM gives officials the information they need to maintain awareness of information security risk, apply security controls to address that risk, and take appropriate corrective action. ISCM is not a replacement for periodic assessments; it supplements them with near-real-time status information.

---

## Definition of ISCM

ISCM is defined as: **maintaining ongoing awareness of information security, vulnerabilities, and threats to support organizational risk management decisions**.

Three ISCM requirements:
1. **Situational awareness** — what assets exist, what controls are deployed, and the operational status of those controls
2. **Visibility** — current security state relative to threats, vulnerabilities, and organisational risk tolerance
3. **Traceability** — ability to track security state changes over time to support trend analysis

---

## Three-Tier ISCM Architecture

ISCM operates across three hierarchical tiers defined in NIST SP 800-39:

### Tier 1 — Organisation Level
- Establishes the ISCM strategy
- Sets organisational risk tolerance and metrics
- Assigns roles and responsibilities
- Defines monitoring frequencies and aggregation approach
- Responsible officials: CIO, SAISO, Risk Executive (Function)

### Tier 2 — Mission/Business Process Level
- Implements ISCM in support of mission/business functions
- Ensures security of information flows between systems
- Monitors common controls not assigned to individual systems
- Responsible officials: Mission/Business Process Owner, Common Control Provider

### Tier 3 — Information System Level
- Implements system-level monitoring
- Monitors system-specific controls
- Reports status upward to Tier 2 and Tier 1 as required
- Responsible officials: Information System Owner (ISO), ISSO, System Security Engineer

**Information flow**: Security status information flows from Tier 3 upward through Tier 2 to Tier 1. Risk decisions and guidance flow downward from Tier 1 through Tier 2 to Tier 3.

---

## Six-Step ISCM Process

### Step 1 — Define ISCM Strategy

Define the ISCM strategy at the organisation level, specifying:
- Organisational risk tolerance
- Metrics to be monitored
- Monitoring frequencies
- Methods for data collection
- Analytical procedures
- Reporting requirements and formats

The strategy must address all three tiers and be approved by senior leadership (CIO and/or Risk Executive Function).

**Key outputs**:
- ISCM strategy document
- Risk tolerance statement
- Approved metrics catalogue

### Step 2 — Establish ISCM Programme

Establish the programme by:
- Selecting security metrics (implementation metrics, operational effectiveness metrics, risk management metrics)
- Assigning monitoring frequencies per control or metric
- Identifying automated and manual collection mechanisms
- Establishing reporting thresholds and escalation paths
- Selecting ISCM supporting tools and technologies

**Key outputs**:
- Security metrics baseline
- Monitoring frequency schedule
- Tool inventory

### Step 3 — Implement ISCM Programme

Implement the programme by:
- Deploying tools and technologies (e.g., SCAP-validated scanners, log aggregators, SIEM)
- Executing automated collection processes
- Collecting manual assessment data not amenable to automation
- Establishing the data repository (security information repository)

**Key outputs**:
- Operational ISCM tool set
- Security data feeds
- Data repository

### Step 4 — Analyse and Report Findings

Analyse collected data and report to appropriate officials:
- Compare results to established metrics and baselines
- Aggregate findings from Tier 3 through Tier 2 to Tier 1
- Produce status reports at each tier
- Report to Authorizing Official (AO) for authorization decisions
- Provide trend analysis when historical data is available

**Key outputs**:
- Security status reports (system, mission/business, organisational)
- Trend reports
- Updated system security plans (SSPs) reflecting current security status

### Step 5 — Respond to Findings

Respond to identified deficiencies and vulnerabilities:
- Update Plan of Action and Milestones (POA&M) for identified weaknesses
- Implement corrective actions within established remediation timeframes
- Apply risk responses: accept, avoid, mitigate, share/transfer
- Report significant changes to AO for authorization re-evaluation
- Document residual risk accepted by officials with authorisation authority

**Key outputs**:
- Updated POA&M
- Corrective action documentation
- Risk acceptance decisions

### Step 6 — Review and Update ISCM Strategy and Programme

Periodically review and update the ISCM strategy and programme:
- Re-evaluate metrics against current threat landscape
- Adjust monitoring frequencies based on observed risk changes
- Update tools and technologies as needed
- Review effectiveness of the ISCM programme
- Revise the strategy document at the organisation level

**Review triggers**:
- Significant changes to mission, organisation, or environment
- Significant system changes (major modifications)
- Identified deficiencies in the ISCM programme's effectiveness
- Changes in threat landscape or risk tolerance
- Periodic review (typically annual at a minimum)

---

## Monitoring Frequencies

Monitoring frequency is determined by the volatility of the information, the speed at which an adversary can exploit a vulnerability, and the CIA impact of the information or system.

| Frequency | Definition | Example Use Cases |
|---|---|---|
| Ongoing (continuous) | Automated, near-real-time collection | Network traffic, event logs, IDS/IPS alerts, patch status |
| Daily | Collected and reviewed every business day | Vulnerability scan results, authentication failures, AV update status |
| Weekly | Collected and reviewed weekly | Configuration deviation reports, user access reviews for high-risk roles |
| Monthly | Collected and reviewed monthly | Configuration management baseline comparisons, account reviews |
| Quarterly | Collected and reviewed quarterly | Access control reviews, security training completion status |
| Annually | Collected and reviewed annually | Full security assessment, policy reviews, disaster recovery tests |

**Frequency selection criteria**:
1. **Volatility**: How quickly does the security-relevant information change?
2. **Adversary speed**: How quickly can an adversary exploit a discovered vulnerability?
3. **CIA impact**: What is the potential loss if the control fails or the vulnerability is exploited?
4. **Automation feasibility**: Can the collection be automated or must it be manual?

---

## Security Metrics

Metrics must be measurable, actionable, and tied to risk management decisions.

### Implementation Status Metrics
Measure whether security controls are deployed as planned:
- Percentage of systems with current patch levels (by criticality)
- Percentage of accounts with MFA enabled
- Percentage of systems with AV definitions current
- Percentage of configurations meeting approved baseline (configuration compliance rate)
- Percentage of users with current security awareness training (by role)

### Operational Effectiveness Metrics
Measure whether deployed controls are operating as intended:
- Mean time to detect (MTTD) security events
- Mean time to respond (MTTR) to security incidents
- False positive and false negative rates for automated security tools
- Percentage of security events escalated vs. dismissed automatically
- Scan coverage rate (percentage of in-scope assets scanned)

### Risk Management Metrics
Measure current risk posture:
- Number of open critical/high/medium/low vulnerabilities (by system, by mission)
- POA&M age distribution (time open by severity)
- Number of systems with current Authorization to Operate (ATO)
- Number of systems operating under Interim ATOs or expired ATOs
- Percentage of controls assessed in the last authorisation cycle

**Metric attributes (for each metric)**:
- **Name**: Short descriptive name
- **Description**: What is being measured
- **Rationale**: Why is this important
- **Method**: How is data collected (automated tool, manual review)
- **Frequency**: How often collected
- **Threshold**: At what value is a finding triggered
- **Reporting level**: Tier 1/2/3 or all

---

## Roles and Responsibilities

### Chief Information Officer (CIO)
- Develops and maintains the organisation-wide ISCM strategy
- Ensures the ISCM programme is resourced
- Reports ISCM results to the head of agency as required

### Senior Agency Information Security Officer (SAISO)
- Implements the ISCM strategy under CIO direction
- Manages the ISCM programme day-to-day
- Provides ISCM guidance to system owners and ISSOs

### Risk Executive (Function)
- Establishes organisational risk tolerance
- Reviews aggregated ISCM findings at the organisation level
- Supports AO decisions based on ISCM data

### Authorizing Official (AO)
- Uses ISCM data to make ongoing authorisation decisions
- Determines if residual risk is acceptable based on current security status
- Takes action when risk exceeds acceptable threshold (e.g., suspend authorisation)

### Information System Owner (ISO)
- Ensures Tier 3 ISCM is implemented for assigned systems
- Reviews system-level ISCM results
- Initiates response actions for system-level findings
- Reports system-level security status to mission/business process owner

### Information System Security Officer (ISSO)
- Executes day-to-day ISCM activities for assigned systems
- Operates and maintains ISCM tools at the system level
- Produces and transmits system-level security status reports
- Updates SSP and POA&M based on ISCM findings

### Common Control Provider
- Monitors common (inherited) controls
- Reports common control status to all systems that inherit those controls
- Included in Tier 2 ISCM reporting

---

## ISCM Tools and Technologies

### Security Content Automation Protocol (SCAP)
SCAP is a set of specifications for automating security measurements and compliance checking:

| SCAP Component | Function |
|---|---|
| CVE (Common Vulnerabilities and Exposures) | Standard vulnerability identifiers |
| CCE (Common Configuration Enumeration) | Standard configuration issue identifiers |
| CPE (Common Platform Enumeration) | Standard product/platform identifiers |
| CVSS (Common Vulnerability Scoring System) | Severity scoring for vulnerabilities |
| OVAL (Open Vulnerability and Assessment Language) | Machine-readable system state descriptions |
| XCCDF (Extensible Configuration Checklist Description Format) | Machine-readable security checklists |

### Asset Reporting Format (ARF)
ARF (NISTIR 7694) provides a standard format for expressing information about assets and reporting the relationship between assets and security-relevant information. ARF enables aggregation of results from multiple SCAP tools.

### Automation Capability Levels
| Level | Description | Use |
|---|---|---|
| Fully automated | No human intervention; tool collects and reports data | Patch status, AV definitions, port scanning |
| Semi-automated | Tools collect data; human analysis required | Log review, vulnerability scan triage |
| Fully manual | Human must perform all collection and analysis | Social engineering tests, physical security reviews |

---

## Integration with RMF

ISCM implements RMF Step 6 (Monitor) from NIST SP 800-37 Rev 2:

| RMF Step 6 Task | ISCM Corresponding Action |
|---|---|
| TASK M-1: System and Environment Changes | ISCM monitors for significant changes triggering re-authorisation |
| TASK M-2: Ongoing Assessments | ISCM provides continuous assessment of selected controls |
| TASK M-3: Ongoing Risk Response | ISCM Step 5 (Respond) provides corrective action and POA&M update |
| TASK M-4: Authorisation Package Updates | ISCM findings update SSP and SAR |
| TASK M-5: Security and Privacy Reporting | ISCM Step 4 (Analyse/Report) provides Tier 1, 2, 3 reporting |
| TASK M-6: Ongoing Authorisation | AO uses ISCM data for ongoing authorisation decisions |
| TASK M-7: System Disposal | ISCM terminates when system is decommissioned |

**Ongoing Authorisation**: ISCM enables an AO to grant an ongoing authorisation (previously "continuous ATO") rather than a time-bound authorisation. The AO establishes a maximum acceptable risk threshold; ISCM monitors whether current risk stays within that threshold. If risk exceeds the threshold, the AO takes action.

---

## ISCM Strategy Document

An ISCM strategy document at the organisation level must address:

1. **Scope**: Systems, assets, and environments covered
2. **Risk tolerance**: Organisational acceptable risk level
3. **Metrics catalogue**: Approved set of metrics with attributes
4. **Monitoring frequency assignments**: Frequency per metric or control
5. **Data collection mechanisms**: Tool inventory and methods per metric
6. **Aggregation procedures**: How Tier 3 data rolls up to Tier 2 and Tier 1
7. **Analysis procedures**: How findings are evaluated against thresholds
8. **Reporting formats and frequencies**: Standard report formats and distribution
9. **Roles and responsibilities**: Per SP 800-137 Table 1
10. **Review and update cycle**: How often the strategy itself is reviewed

---

## Significant Changes Requiring Re-evaluation

The following changes trigger re-evaluation of authorisation or ISCM strategy:
- Installation of new or replacement hardware, software, or firmware
- Changes to mission, business functions, or organisational priorities
- Change in authorising official
- Changes to applicable laws, regulations, or policy
- Changes to the operational environment (e.g., new threat disclosures, new vulnerabilities)
- Changes to the security plan (e.g., changes to common controls)
- Deficiencies found through ISCM (findings that exceed accepted risk thresholds)

---

## ISCM and FISMA Compliance

FISMA (Federal Information Security Modernization Act) requires federal agencies to implement a programme of continuous monitoring. NIST SP 800-137 provides the guidance to fulfil this requirement.

Key FISMA connections:
- OMB Circular A-130 requires ISCM programmes for federal agencies
- OMB memoranda (e.g., M-14-03) require CDM (Continuous Diagnostics and Mitigation) programme participation
- Annual reporting to OMB and Congress uses ISCM data (CyberStat, FISMA metrics)
- DHS CDM programme provides tools and dashboards for ISCM capabilities

---

## Reference Files

- `references/iscm-process.md` — Detailed six-step ISCM process with task checklists, input/output tables, and step-by-step procedures
- `references/monitoring-strategy.md` — ISCM strategy structure, frequency assignment guidance, control selection rationale, and programme establishment procedures
- `references/metrics-reporting.md` — Security metrics catalogue format, reporting templates, aggregation procedures, and AO reporting formats

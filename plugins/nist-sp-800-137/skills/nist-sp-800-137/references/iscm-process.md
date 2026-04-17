# NIST SP 800-137 — ISCM Six-Step Process Detail

**Source**: NIST SP 800-137, September 2011, Sections 3–8

---

## Overview

The ISCM process is a six-step cycle. It is not a one-time activity but an ongoing programme that is continually refined. The cycle operates simultaneously at Tier 1 (Organisation), Tier 2 (Mission/Business Process), and Tier 3 (Information System), with information flowing upward and guidance flowing downward across tiers.

---

## Step 1 — Define ISCM Strategy

### Inputs
- Organisational mission and business objectives
- Applicable laws, regulations, and policies (FISMA, NIST publications, OMB circulars)
- Existing risk management programme documentation
- Inventory of information systems (from SP 800-37 RMF Step 1)

### Tasks

**Task 1.1 — Establish Organisational Risk Tolerance**
- Define quantitative or qualitative acceptable risk thresholds
- Document risk tolerance by system impact level (Low, Moderate, High)
- Obtain approval from head of agency or designated official (Risk Executive Function)

**Task 1.2 — Define ISCM Metrics**
- Identify metrics aligned with organisational risk priorities
- Include implementation metrics, operational effectiveness metrics, and risk management metrics
- Define attributes per metric (name, description, rationale, method, frequency, threshold, reporting level)
- Document approved metrics in an ISCM metrics catalogue

**Task 1.3 — Define Monitoring Frequencies**
- Assign frequency (ongoing/continuous, daily, weekly, monthly, quarterly, annual) per metric or SP 800-53 control
- Base frequency on volatility, adversary speed, and CIA impact (see frequency criteria)
- Prioritise automation for high-frequency metrics

**Task 1.4 — Define Collection, Analysis, and Reporting Procedures**
- Identify data collection mechanisms per metric (tool, manual procedure)
- Define aggregation procedures for rolling Tier 3 data to Tier 2 and Tier 1
- Define report formats, distribution lists, and escalation paths
- Define threshold-based alerting for out-of-compliance conditions

**Task 1.5 — Define Roles and Responsibilities**
- Assign ISCM roles to named positions (CIO, SAISO, Risk Executive Function, AO, ISO, ISSO, Common Control Provider)
- Document accountability for each ISCM task
- Define escalation procedures

### Outputs
- Approved ISCM strategy document
- Metrics catalogue
- Monitoring frequency schedule
- Roles and responsibilities matrix

---

## Step 2 — Establish ISCM Programme

### Inputs
- Approved ISCM strategy (Step 1)
- System security plans and current security assessment results
- System and common control inventory

### Tasks

**Task 2.1 — Select and Implement ISCM Tools**
- Identify tools capable of automated data collection per approved metrics
- Validate tools against SCAP specifications where applicable (OVAL, XCCDF, ARF)
- Ensure tools support the monitoring frequencies defined in the strategy
- Address tool coverage gaps with manual procedures

**Task 2.2 — Establish Security Data Repository**
- Deploy or designate a repository for ISCM-collected data
- Ensure data integrity, availability, and appropriate access controls
- Define retention periods aligned to reporting and trend analysis requirements
- Implement data normalisation if aggregating from multiple tools

**Task 2.3 — Establish Baselines**
- Define approved configuration baselines (using NIST SP 800-70 National Checklists where applicable)
- Document approved software lists per system
- Document approved network topology and trust boundaries
- Establish patch compliance baseline (current approved patch state)

**Task 2.4 — Establish Reporting Thresholds**
- Define numeric thresholds per metric (e.g., patch compliance below 95% triggers finding)
- Define escalation thresholds (e.g., critical vulnerability unpatched > 30 days requires AO notification)
- Document exception and risk acceptance procedures

### Outputs
- ISCM tool inventory with coverage mapping
- Security data repository operational
- Documented baselines
- Reporting thresholds and escalation procedures

---

## Step 3 — Implement ISCM Programme

### Inputs
- Established ISCM programme (Step 2)
- System security plans and authorisation packages

### Tasks

**Task 3.1 — Execute Automated Collections**
- Run scheduled automated scans and collections per frequency schedule
- Collect data across all in-scope systems (Tier 3) and aggregation points (Tier 2)
- Archive raw collection results in the security data repository

**Task 3.2 — Execute Manual Collections**
- Execute manual assessment procedures for controls not amenable to automation
- Document manual collection results in standardised format
- Ensure manual collection is performed at the approved frequency

**Task 3.3 — Collect Common Control Status**
- Common Control Providers collect and report status for inherited controls
- Data feeds into Tier 2 and Tier 1 aggregation

**Task 3.4 — Maintain ISCM Tool Set**
- Update tool signatures, definitions, and configurations
- Validate tool outputs periodically to ensure accuracy (no false positives, no missed assets)
- Maintain tool inventory currency

### Outputs
- Security data repository populated with current collections
- Raw assessment results archived
- Common control status feeds operational

---

## Step 4 — Analyse and Report Findings

### Inputs
- Security data from Step 3
- Approved baselines and thresholds from Step 2
- Prior reporting cycle data (for trend analysis)

### Tasks

**Task 4.1 — Analyse Collected Data**
- Compare results to baselines and detection thresholds
- Identify findings (deviations from baseline; unpatched vulnerabilities; misconfigurations)
- Classify findings by severity (Critical, High, Medium, Low) using CVSS and SP 800-30 risk approach
- Correlate findings across metrics (e.g., unpatched critical CVE on an internet-facing system)

**Task 4.2 — Produce System-Level Reports (Tier 3)**
- Document findings per system
- Include metric status (compliant/non-compliant), finding details, trend delta from prior cycle
- Transmit to ISO and ISSO; copy to Tier 2 aggregation

**Standard Tier 3 Security Status Report Contents**:
| Section | Content |
|---|---|
| System identification | Name, system identifier, FIPS 199 impact level, AO |
| Reporting period | Start and end dates; collection timestamps |
| Metric status summary | Table of all metrics: metric name, threshold, current value, status (pass/fail) |
| Findings | New findings; sustained findings; resolved findings |
| Trend analysis | Delta from prior period per metric |
| POA&M status | Open items, closed this period, newly opened |
| Significant changes | Any Tier 3 significant changes since last report |

**Task 4.3 — Aggregate to Mission/Business Process Level (Tier 2)**
- Aggregate Tier 3 reports for all systems supporting the mission/business process
- Identify cross-system trends or common vulnerabilities across the portfolio
- Report to Mission/Business Process Owner and Common Control Provider

**Task 4.4 — Aggregate to Organisation Level (Tier 1)**
- CIO/SAISO aggregates Tier 2 reports
- Produce organisation-wide security status dashboard
- Present to Risk Executive Function and AO
- Update OMB FISMA reporting data (CyberStat/FISMA metrics)

**Task 4.5 — AO Reporting**
- Provide AO with current system risk posture based on ISCM data
- Highlight any findings that may affect the authorisation decision
- AO determines if residual risk remains within accepted threshold

### Outputs
- Tier 3 security status reports (system level)
- Tier 2 aggregated reports (mission/business process level)
- Tier 1 organisation-level security status dashboard
- AO notification where findings exceed threshold
- Updated FISMA reporting data

---

## Step 5 — Respond to Findings

### Inputs
- Findings from Step 4
- Current POA&M
- Risk acceptance decisions

### Tasks

**Task 5.1 — Update POA&M**
- Open new POA&M items for newly identified findings
- Track findings by: weakness description, affected system, responsible party, estimated completion date, current status
- Close POA&M items for findings resolved in current cycle
- Escalate overdue high/critical items to ISSO and ISO

**Remediation Timeframe Guidance**:
| Severity | Maximum Time to Remediate |
|---|---|
| Critical | 15 days (or immediate AO notification and risk acceptance) |
| High | 30 days |
| Medium | 90 days |
| Low | 180 days or accepted as residual risk |

**Task 5.2 — Apply Risk Responses**
- Mitigate: apply patches, correct configuration, implement additional controls
- Accept: document risk acceptance by authorised official with rationale and re-evaluation date
- Avoid: retire system component or capability generating the risk
- Transfer/Share: use shared services or transfer responsibility where permitted

**Task 5.3 — Report Significant Changes to AO**
- Report any finding that introduces risk outside the accepted threshold to the AO immediately
- AO reviews and determines action (continue authorisation, accept additional risk, suspend or revoke authorisation)

**Task 5.4 — Update SSP and Authorisation Package**
- Reflect current security state, open findings, and risk acceptance decisions in SSP
- Update SAR findings if formal reassessment occurred
- Update POA&M and transmit updated authorisation package to AO repository

### Outputs
- Updated POA&M
- Remediation action documentation
- Risk acceptance records
- Updated SSP and authorisation package

---

## Step 6 — Review and Update ISCM Strategy and Programme

### Inputs
- ISCM strategy and programme documentation
- Findings from prior cycles
- Changes in mission, threats, or organisational risk tolerance

### Tasks

**Task 6.1 — Review ISCM Programme Effectiveness**
- Assess whether current metrics are capturing meaningful security information
- Review whether monitoring frequencies are appropriate given observed threat activity
- Identify controls or metrics with persistent findings (indicates systemic issue, not monitoring gap)
- Review tool coverage gaps and automation opportunities

**Task 6.2 — Review Organisational Risk Tolerance**
- Confirm with Risk Executive Function whether risk tolerance has changed
- Update strategy document if tolerance thresholds have changed

**Task 6.3 — Update the ISCM Strategy**
- Revise metrics catalogue (add, remove, modify metrics)
- Revise frequency assignments
- Revise reporting formats and distribution
- Obtain re-approval from CIO and Risk Executive Function

**Task 6.4 — Update the ISCM Programme**
- Update tool configurations and baselines
- Update data collection procedures and thresholds
- Re-train ISCM personnel on changed procedures

### Review Triggers (event-driven, in addition to periodic review)
| Trigger | Action |
|---|---|
| New threat intelligence (e.g., new CVE campaign) | Review frequency for affected controls; increase if warranted |
| Significant system change (major modification) | Re-evaluate Tier 3 monitoring for changed system |
| New organisational mission | Review Tier 2 metrics for new mission/business process |
| Persistent POA&M findings | Review whether monitoring is detecting root cause |
| FISMA reporting gap | Review if ISCM data is satisfying federal reporting requirements |
| Annual review (minimum) | Full periodic review of strategy and programme |

### Outputs
- Updated and re-approved ISCM strategy
- Updated ISCM programme documentation
- Updated tool configurations and baselines

---

## ISCM Process Checklist

### Step 1 — Define Strategy
- [ ] Risk tolerance documented and approved
- [ ] Metrics catalogue defined with all required attributes
- [ ] Monitoring frequencies assigned per metric
- [ ] Collection, analysis, and reporting procedures documented
- [ ] Roles and responsibilities matrix complete and approved
- [ ] ISCM strategy document approved by CIO/Risk Executive Function

### Step 2 — Establish Programme
- [ ] ISCM tools selected and validated (SCAP where applicable)
- [ ] Security data repository established with access controls
- [ ] Configuration and software baselines documented
- [ ] Reporting thresholds and escalation procedures defined
- [ ] Coverage gaps identified and manual procedures established

### Step 3 — Implement Programme
- [ ] Automated collections executing on schedule
- [ ] Manual collections being performed per frequency
- [ ] Common control feeds operational
- [ ] Tool maintenance procedures in place

### Step 4 — Analyse and Report
- [ ] Tier 3 reports produced per reporting cycle
- [ ] Tier 2 aggregation completed
- [ ] Tier 1 dashboard updated
- [ ] AO notified of threshold-exceeding findings
- [ ] FISMA reporting data updated

### Step 5 — Respond
- [ ] POA&M updated with new and resolved findings
- [ ] Remediation actions tracked within timeframes
- [ ] Risk acceptances documented with authorised signatures
- [ ] SSP and authorisation package updated

### Step 6 — Review
- [ ] ISCM programme effectiveness reviewed
- [ ] Risk tolerance confirmed with Risk Executive Function
- [ ] Strategy and programme updated as needed
- [ ] Updates approved by CIO/Risk Executive Function

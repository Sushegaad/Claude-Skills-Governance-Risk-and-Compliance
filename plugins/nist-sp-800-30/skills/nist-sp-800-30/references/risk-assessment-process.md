# NIST SP 800-30 Rev 1 — Risk Assessment Process (Detailed)

Source: NIST Special Publication 800-30 Rev 1, September 2012
https://doi.org/10.6028/NIST.SP.800-30r1

---

## Overview

NIST SP 800-30 Rev 1 defines a structured four-step process for conducting risk assessments. The process supports all three tiers of risk management: organisation (Tier 1), mission/business process (Tier 2), and information system (Tier 3).

---

## Step 1: Prepare for the Risk Assessment

### Task 1-1: Identify the Purpose
Define why the risk assessment is being conducted. Common purposes include:
- Support an Authorisation to Operate (ATO) decision
- Inform control selection (RMF Step 2 — Select)
- Assess residual risk after remediation
- Evaluate a proposed system change
- Support annual risk review obligations

### Task 1-2: Identify the Scope
Define boundaries for the risk assessment:
- **Organisational scope**: Which organisational units, functions, or assets are included
- **System scope**: Which information systems, components, or data types are in scope
- **Information scope**: How sensitive the system and information are (FIPS 199 categorisation)
- **Temporal scope**: Whether the assessment covers current state, future state, or both

### Task 1-3: Identify Assumptions and Constraints
Document:
- Assessment assumptions (e.g., threat intel sources assumed current)
- Constraints: time, budget, access to systems, availability of data
- Dependencies: what the assessment results will feed into (ATO package, risk register)
- Stakeholder limitations: who can be interviewed or surveyed

### Task 1-4: Identify Information Sources
Authoritative and supplementary sources include:

| Category | Sources |
|----------|---------|
| Threat intelligence | CISA advisories, DHS reports, sector-specific ISACs, MS-ISAC, MITRE ATT&CK |
| Vulnerability data | NIST NVD, CISA KEV, CERT/CC, vendor security advisories |
| Organisational data | Previous risk assessments, audit reports, incident logs, POA&M |
| System data | System Security Plan (SSP), architecture diagrams, data flows |
| Regulatory | FIPS 199, SP 800-60, SP 800-53 control baseline |

### Task 1-5: Identify the Risk Model and Analytic Approaches

The risk model defines the risk factors and how they combine to produce a risk level.

**Risk equation (simplified):**
> Risk = f(Likelihood of Threat Event, Magnitude of Impact)

**Likelihood = f(Likelihood of Threat Initiation, Likelihood of Adverse Impact)**

**Analytic approaches:**

| Approach | Scale Type | Best For |
|----------|-----------|----------|
| Qualitative | Descriptive (Very Low – Very High) | Broad surveys; when data precision is low |
| Semi-quantitative | Numerical (0–10 or 1–100 mapped to descriptors) | Most federal assessments |
| Quantitative | Dollar values, probabilities | Financial impact analysis; when actuarial data exists |

---

## Step 2: Conduct the Risk Assessment

### Task 2-1: Identify Threat Sources

**Adversarial Threat Sources (Appendix D, Table D-1):**

| Threat Source | Description | Characteristics |
|---------------|-------------|----------------|
| Nation-State | Foreign intelligence entities with strategic objectives | High capability, specific targeting, patient adversary |
| Cyber Criminal | Organised criminal groups motivated by financial gain | High capability, broad targeting, rapid exploitation |
| Hacktivist | Groups/individuals motivated by ideology or notoriety | Variable capability, public targeting, disruptive methods |
| Insider (Malicious) | Current or former employees/contractors with authorised access | Privileged access, knows system internals, unpredictable motivation |
| Insider (Inadvertent) | Authorised users causing harm through error or negligence | No hostile intent, high frequency, broad impact |
| Business Competitor | Entities seeking competitive intelligence | Variable capability, targeted, economic motivation |
| Terrorist | Entities seeking to cause widespread harm or disruption | Variable capability, target critical infrastructure |
| Script Kiddie | Inexperienced individuals using available exploit tools | Low capability, opportunistic, broad targeting |

**Non-Adversarial Threat Sources (Appendix D, Table D-2):**

| Threat Source | Description |
|---------------|-------------|
| Accidental user action | Unintentional modification, deletion, or disclosure by authorised users |
| Hardware failure | Component failure (disk, memory, network hardware) through age or defect |
| Software failure | Application bugs, OS crashes, firmware issues |
| Environmental | Natural or man-made environmental events (weather, power, building) |

### Task 2-2: Identify Threat Events

**Adversarial Threat Events (Appendix E, Table E-2 — representative):**

| Category | Event Examples |
|----------|---------------|
| Reconnaissance | Network scanning, open-source intelligence gathering, social engineering reconnaissance |
| Initial Access | Spear phishing, supply chain compromise, exploitation of public-facing application, use of valid accounts |
| Execution and Persistence | Malware installation, scheduled task creation, registry modification, remote access trojans |
| Privilege Escalation | Exploitation of misconfigured permissions, credential theft, pass-the-hash |
| Lateral Movement | Internal network scanning, use of stolen credentials across systems |
| Exfiltration | Data copying to removable media, upload to adversary-controlled cloud storage, covert channel |
| Impact | Ransomware deployment, data destruction, denial of service, corruption of critical data |
| Supply Chain | Malicious code in commercial software, hardware implants, compromised update mechanism |

**Non-Adversarial Threat Events:**

| Category | Event Examples |
|----------|---------------|
| Accidental destruction | Unintentional deletion of critical files, database corruption, accidental overwrite |
| Structural failure | Disk array failure, UPS failure, network switch hardware fault |
| Environmental disruption | Power outage, flooding of data centre, fire, physical access interruption |
| Human error | Misconfigured firewall rule, incorrect patch applied, wrong access level granted |

### Task 2-3: Identify Vulnerabilities and Predisposing Conditions

**Vulnerability Categories:**

| Category | Examples |
|----------|---------|
| Software | Unpatched CVEs, insecure coding practices, missing input validation |
| Configuration | Default credentials, excessive permissions, open ports, disabled logging |
| Process | Inadequate change management, lack of security review in SDLC |
| Access control | Overly permissive access, missing MFA, shared accounts |
| Physical | Unlocked server rooms, unescorted visitors, inadequate CCTV |
| Supply chain | Unverified software components, insufficient vendor vetting |

**Predisposing Conditions (Appendix F, Table F-5):**
Conditions that increase or decrease the likelihood that a threat event leads to adverse impact:
- Architectural decisions (e.g., flat network with no segmentation increases lateral movement risk)
- Organisational culture (e.g., high security awareness reduces social engineering success)
- Data sensitivity concentration (e.g., all PII in one system increases impact if compromised)
- Geographic exposure (e.g., coastal data centre increases flood risk)

### Task 2-4: Determine Likelihood of Occurrence

**Step 1 — Assess likelihood of threat initiation (Table G-2):**
Base this on adversary capability, intent, and current threat intelligence.

**Step 2 — Assess likelihood that attack succeeds/causes impact (Table G-3):**
Based on vulnerability severity and effectiveness of current controls.

**Overall Likelihood Matrix (Table I-2):**

|  | Very Low Impact-Susceptibility | Low | Moderate | High | Very High |
|--|-------------------------------|-----|----------|------|-----------|
| **Very High Initiation** | Low | Moderate | High | Very High | Very High |
| **High Initiation** | Very Low | Low | Moderate | High | Very High |
| **Moderate Initiation** | Very Low | Low | Moderate | Moderate | High |
| **Low Initiation** | Very Low | Very Low | Low | Low | Moderate |
| **Very Low Initiation** | Very Low | Very Low | Very Low | Low | Low |

### Task 2-5: Determine Magnitude of Impact

**Impact Areas per Appendix H:**

Core impact considerations for federal systems:
1. **Mission/business effectiveness** — Can the organisation accomplish its mission?
2. **Reputation and trust** — Does the incident erode public confidence?
3. **Financial loss** — Direct costs (remediation, legal) and indirect costs (lost revenue)
4. **Legal/regulatory** — Violation of federal law, FISMA obligations, agency policy
5. **Physical harm** — Personal safety of individuals affected
6. **Critical infrastructure** — Impact on interdependent national-level systems

**Mapping to FIPS 199 Impact Levels:**

| Impact Level | Potential Impact | Description |
|-------------|-----------------|-------------|
| HIGH | Severe or catastrophic | Could cause severe degradation or loss of mission capability; major financial harm; severe harm to people |
| MODERATE | Serious | Could cause significant degradation; significant financial loss; significant harm |
| LOW | Limited | Could cause minor degradation; minor loss; minor harm |

### Task 2-6: Determine Risk

**Risk Score Matrix (Table I-4):**

Use likelihood × impact to determine risk level:

| Likelihood ↓ / Impact → | Very Low | Low | Moderate | High | Very High |
|------------------------|---------|-----|----------|------|-----------|
| Very High | Low | Moderate | High | Very High | Very High |
| High | Low | Moderate | Moderate | High | Very High |
| Moderate | Low | Low | Moderate | High | High |
| Low | Very Low | Low | Low | Moderate | High |
| Very Low | Very Low | Very Low | Low | Low | Moderate |

---

## Step 3: Communicate Risk Assessment Results

### Risk Assessment Report Template

**Document Control Block:**
| Field | Value |
|-------|-------|
| Title | Risk Assessment Report — [System/Organisation Name] |
| Version | 1.0 |
| Date | [Date] |
| Classification | [e.g., For Official Use Only] |
| Author | [Name, Role] |
| Reviewed By | [Authorising Official / Risk Executive] |

**Required Sections:**
1. Executive Summary
2. Scope and Methodology
3. Assumptions and Constraints
4. Risk Assessment Results (risk register table)
5. Summary and Priority Risk List
6. Recommended Risk Responses
7. Appendices

### Risk Register Table Format

| Risk ID | Threat Source | Threat Event | Vulnerability | Likelihood | Impact | Risk Level | Uncertainty | Risk Response |
|---------|--------------|-------------|--------------|-----------|--------|-----------|------------|--------------|
| RA-001 | | | | | | | | |

---

## Step 4: Maintain the Risk Assessment

### Refresh Triggers
- **Periodic**: Annually at minimum for all federal systems; more frequently for HIGH-impact systems
- **Event-driven**: Following a security incident; significant configuration change; system upgrade; new threat intelligence indicating active exploitation
- **RMF-driven**: Prior to ATO renewal; when continuous monitoring reveals degraded control effectiveness

### Integration with SP 800-137 (Continuous Monitoring)
- Risk assessment provides baseline risk tolerance and accepted risk levels
- Continuous monitoring data (SIEM alerts, vulnerability scan results, control assessments) feeds back into risk factor updates per Task 4-1
- Risk register maintained as a living document updated from monitoring output

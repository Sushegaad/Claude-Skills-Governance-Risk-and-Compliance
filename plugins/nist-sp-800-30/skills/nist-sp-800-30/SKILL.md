---
name: nist-sp-800-30
description: >
  Expert NIST SP 800-30 Rev 1 risk assessment advisor. Use this skill whenever a user asks
  about conducting risk assessments using NIST SP 800-30, including: identifying threat sources
  and threat events, assessing vulnerabilities and predisposing conditions, determining
  likelihood of occurrence, determining magnitude of impact, calculating risk levels, building
  risk registers, communicating and sharing risk assessment results, preparing risk assessment
  reports, integrating risk assessments into the NIST Risk Management Framework (RMF),
  selecting risk assessment approaches (quantitative, qualitative, semi-quantitative),
  or questions about NIST SP 800-30 tasks and steps. Also trigger for: "how do I perform
  a risk assessment?", "what is the NIST risk model?", "help me build a risk register",
  "threat source identification", "risk likelihood and impact scales", or any federal
  information system risk assessment question.
---

# NIST SP 800-30 Rev 1 — Risk Assessment Skill

You are an expert risk assessment advisor specialising in **NIST Special Publication 800-30 Revision 1: Guide for Conducting Risk Assessments** (September 2012). You assist **federal agencies, contractors, security teams, and risk management professionals** in conducting rigorous, structured risk assessments for federal information systems and organisations in accordance with NIST guidance.

This skill is grounded exclusively in NIST SP 800-30 Rev 1. All guidance, scales, tables, and processes referenced are drawn directly from that publication.

---

## How to Respond

Match your output to the task type:

| Task | Output Format |
|------|--------------|
| Risk assessment planning | Structured plan: purpose, scope, assumptions, information sources, risk model |
| Threat source identification | Table: Threat Source | Type | Description | Adversarial Capability | Intent | Range of Effects |
| Threat event identification | Table: Threat Event | Source | Relevance | Likelihood of Initiation |
| Vulnerability/predisposing conditions | Table: Vulnerability | Predisposing Condition | Severity | Pervasiveness |
| Likelihood determination | Table: Threat Event | Initiation Likelihood | Impact Severity | Overall Likelihood |
| Impact analysis | Table: Threat Event | Affected Asset | Impact Type | Impact Magnitude |
| Risk determination | Risk register: Threat Event | Likelihood | Impact | Risk Level | Uncertainty |
| Risk assessment report | Full structured report with executive summary and risk tables |
| RMF integration guidance | Narrative with mapping to RMF steps |
| General question | Clear, concise prose with SP 800-30 task/appendix citations |

---

## NIST SP 800-30 Rev 1 Overview

### Purpose and Scope
NIST SP 800-30 Rev 1 provides guidance for conducting risk assessments as part of an overall risk management process. It supports the **NIST Risk Management Framework (RMF)** defined in SP 800-37 and the enterprise risk management approach in SP 800-39. Risk assessments inform decision-makers at all three tiers:

| Tier | Level | Description |
|------|-------|-------------|
| Tier 1 | Organisation | Strategic risk decisions, mission/business functions |
| Tier 2 | Mission/Business Process | Risk to business processes supporting the mission |
| Tier 3 | Information System | Operational system-level risk |

### Relationship to Other NIST Publications
- **SP 800-39**: Organisational information security risk management (provides the overarching risk management process)
- **SP 800-37**: RMF — Categorise, Select, Implement, Assess, Authorise, Monitor
- **SP 800-53**: Security and privacy controls for federal information systems
- **SP 800-53A**: Guide for Assessing Security and Privacy Controls
- **SP 800-137**: Information Security Continuous Monitoring

---

## The Four-Step Risk Assessment Process

### Step 1 — Prepare for the Risk Assessment

**Purpose**: Establish the context and parameters for the assessment before collection of threat, vulnerability, and impact data.

**Tasks:**

| Task | Description | Key Output |
|------|-------------|-----------|
| 1-1 | Identify the purpose of the risk assessment | Purpose statement |
| 1-2 | Identify the scope of the risk assessment | Scope boundaries (organisational, system, information) |
| 1-3 | Identify assumptions and constraints | Documented assumptions, resource constraints, time-box |
| 1-4 | Identify sources of threat, vulnerability, and impact information | List of authoritative/supplementary sources (threat intel, CVEs, NVD etc.) |
| 1-5 | Identify the risk model and analytic approaches (Table C-2 applies) | Defined risk model, likelihood function, impact methodology |

**Risk Model Elements (per SP 800-30 Section 2.2):**
- **Threat sources** (adversarial, accidental, structural, environmental)
- **Threat events** (specific actions or incidents)
- **Vulnerabilities** (weaknesses that enable exploitation)
- **Predisposing conditions** (conditions that increase susceptibility)
- **Likelihood of occurrence** (probability that a threat event is initiated and causes harm)
- **Magnitude of impact** (severity of harm)
- **Risk** (function of likelihood and impact)

**Analytic Approaches:**
| Approach | Description | When to Use |
|----------|-------------|-------------|
| Quantitative | Numerical values for all risk factors (e.g., ALE = AV × EF × ARO) | When data supports numerical precision |
| Qualitative | Descriptive scales (Very Low–Very High) | Most federal assessments; easier to communicate |
| Semi-quantitative | Numbered scales (1–10) mapped to qualitative descriptors | Balance of precision and communicability |

---

### Step 2 — Conduct the Risk Assessment

**Purpose**: Identify threats, vulnerabilities, and adverse impacts; determine likelihood and magnitude; calculate risk levels.

**Tasks:**

#### Task 2-1: Identify Threat Sources

Threat sources are categorised into four types per **Appendix D, Table D-1**:

| Type | Definition | Examples |
|------|-----------|---------|
| **Adversarial** | Individuals or groups seeking to exploit information systems | Nation-states, cyber criminals, hacktivists, insiders, competitors |
| **Accidental** | Non-malicious human errors by authorised users | Misconfigured systems, accidental deletion, user error |
| **Structural** | Failure of equipment, environmental controls, or software | Hardware failure, software bugs, infrastructure decay |
| **Environmental** | Natural disasters and uncontrollable physical events | Flood, earthquake, hurricane, power outage, pandemic |

For each adversarial threat source, document:
- **Capability**: Very Low / Low / Moderate / High / Very High (relative technical sophistication)
- **Intent**: Confirmed hostile intent, suspected, or opportunistic
- **Targeting**: Specific (targeted) / General (untargeted)

#### Task 2-2: Identify Threat Events

A **threat event** is an event or situation initiated by a threat source that has the potential to cause harm. Use **Appendix E, Table E-2** as the basis.

**Adversarial Threat Event Categories (Appendix E):**
- Reconnaissance, intelligence gathering, targeting
- Exploitation of vulnerabilities (software, configuration, supply chain)
- Exfiltration, extraction, and theft
- Exploitation of supply chain (malicious code in hardware, software, services)
- Targeted attacks (watering hole, spear phishing, social engineering)
- Denial and disruption (DDoS, ransomware, data destruction)
- Corruption and modification of information

**Non-Adversarial Threat Event Categories:**
- Accidental destruction, loss, alteration of information
- Structural failure of information systems
- Environmental disruption (floods, power)
- Human error by privileged users

For each identified threat event, record:
- Source (which threat source initiates it)
- Description
- Relevance (Not Relevant / Relevant / Very Relevant)
- Estimated likelihood of initiation

#### Task 2-3: Identify Vulnerabilities and Predisposing Conditions

**Vulnerabilities** are weaknesses in systems, procedures, or controls that can be exploited.
**Predisposing conditions** are characteristics of systems or organisations that make threat events more or less likely to have adverse impacts.

| Factor | Description | Scale |
|--------|-------------|-------|
| Vulnerability severity | Degree to which the vulnerability increases risk | Very Low / Low / Moderate / High / Very High |
| Pervasiveness | How widely the vulnerability or predisposing condition is present | Very Low / Low / Moderate / High / Very High |

Sources for vuln identification:
- NIST National Vulnerability Database (NVD)
- CISA Known Exploited Vulnerabilities (KEV) catalogue
- NIST SP 800-53 control assessment results (from SP 800-53A)
- Security assessment reports
- Penetration test results
- SIEM and continuous monitoring data

#### Task 2-4: Determine Likelihood of Occurrence

Likelihood of occurrence is a **two-part determination** per SP 800-30 Section 3.2.4:

**Part 1 — Likelihood of threat event initiation** (adversarial) or occurrence (non-adversarial):

| Qualitative | Semi-Quantitative | Description |
|-------------|------------------|-------------|
| Very High | 96–100 | Near certainty the adversary will initiate the threat event |
| High | 80–95 | Highly likely the adversary will initiate the threat event |
| Moderate | 21–79 | Somewhat likely the adversary will initiate the threat event |
| Low | 5–20 | Unlikely the adversary will initiate the threat event |
| Very Low | 0–4 | Highly unlikely the adversary will initiate the threat event |

**Part 2 — Likelihood that the threat event causes adverse impact** (given initiation):

| Qualitative | Description |
|-------------|-------------|
| Very High | Near certain that the threat event results in adverse impact |
| High | Highly likely that the threat event results in adverse impact |
| Moderate | Somewhat likely that the threat event results in adverse impact |
| Low | Unlikely that the threat event results in adverse impact |
| Very Low | Highly unlikely that the threat event results in adverse impact |

**Overall Likelihood** = combination of Part 1 and Part 2, using the Likelihood of Occurrence matrix (Appendix I, Table I-2).

#### Task 2-5: Determine Magnitude of Impact

Impact is assessed per **Appendix H** and across impact types:

**Impact Types (per FIPS 199 / SP 800-60):**
- Confidentiality
- Integrity
- Availability

| Level | Qualitative | Description |
|-------|-------------|-------------|
| 5 | Very High | Multiple severe or catastrophic adverse effects on organisational operations, assets, individuals, or national security |
| 4 | High | Severe degradation of capability; major damage to important organisational assets; major harm to individuals |
| 3 | Moderate | Significant degradation; significant damage to organisational assets; significant harm to individuals |
| 2 | Low | Limited degradation; minor damage to assets; minor harm |
| 1 | Very Low | Negligible diminishment; negligible damage; negligible adverse effects on individuals |

**Impact Areas (beyond CIA triad, per Appendix H):**
- Mission effectiveness
- Reputation and trust
- Financial
- Legal, regulatory, contractual
- Physical infrastructure and safety
- Human safety

#### Task 2-6: Determine Risk

**Risk** is a function of the **likelihood of occurrence** and the **magnitude of impact**. SP 800-30 uses a 5×5 risk matrix:

**Risk Determination Matrix (Appendix I, Table I-4):**

|  | Very Low Impact | Low Impact | Moderate Impact | High Impact | Very High Impact |
|--|----------------|-----------|----------------|------------|----------------|
| **Very High Likelihood** | Low | Moderate | High | Very High | Very High |
| **High Likelihood** | Low | Moderate | Moderate | High | Very High |
| **Moderate Likelihood** | Low | Low | Moderate | High | High |
| **Low Likelihood** | Very Low | Low | Low | Moderate | High |
| **Very Low Likelihood** | Very Low | Very Low | Low | Low | Moderate |

Risk values: Very Low / Low / Moderate / High / Very High

Also document **uncertainty** alongside each risk determination:
- **Uncertainty** reflects limitations in data, confidence in threat intelligence, and model assumptions.
- Express as: Low / Moderate / High uncertainty with a brief explanation.

---

### Step 3 — Communicate Risk Assessment Results

**Purpose**: Communicate results to organisational decision-makers to support risk response decisions.

**Tasks:**

| Task | Description | Output |
|------|-------------|--------|
| 3-1 | Communicate risk assessment results to risk executives, authorising officials, and mission/business owners | Risk assessment report (structured) |
| 3-2 | Share risk-related information with stakeholders organisation-wide as appropriate | Risk register updates, briefings, dashboards |

**Risk Assessment Report Structure:**
1. Executive Summary (purpose, scope, overall risk posture)
2. Risk Assessment Methodology (risk model, analytic approach, assumptions)
3. Threat Sources (list with characteristics)
4. Threat Events (list with descriptions and relevance)
5. Vulnerabilities and Predisposing Conditions
6. Risk Determination Table (all identified risks with likelihood, impact, level, uncertainty)
7. Summary of Key Risks (top risks requiring immediate attention)
8. Appendices (supporting data, sources, methodology details)

---

### Step 4 — Maintain the Risk Assessment

**Purpose**: Keep the risk assessment current and relevant as the threat landscape, system, and organisational context evolve.

**Tasks:**

| Task | Description | Trigger |
|------|-------------|---------|
| 4-1 | Monitor the risk factors that contribute to changes in risk | Continuous monitoring output, threat intelligence |
| 4-2 | Update the risk assessment to reflect the current risk environment | Significant change in system, threat landscape, or mission |

**Integration with Continuous Monitoring (SP 800-137):**
- Risk assessment results feed into the continuous monitoring strategy
- Security control effectiveness data from ongoing assessments updates risk factors
- Risk assessment refresh recommended: annually at minimum; following significant system changes; following security incidents

---

## Core Workflows

### 1. Conducting a Risk Assessment (End-to-End)

1. Clarify: tier level (Org/Mission/System), system type (categorisation), and assessment approach (qualitative/semi-quantitative)
2. Work through all 6 tasks in Step 2 sequentially
3. Produce a risk register table:

| # | Threat Source | Threat Event | Vulnerability | Likelihood | Impact | Risk Level | Uncertainty | Recommended Response |
|---|--------------|-------------|--------------|-----------|--------|-----------|------------|---------------------|
| 1 | | | | | | | | |

4. Summarise top risks by risk level (Very High → Very Low)
5. Offer to generate a risk assessment report

### 2. Risk Register Generation
When building a risk register:
- Use the 5-column format: Threat Event | Likelihood | Impact | Risk Level | Uncertainty
- Group by threat source type (adversarial, accidental, structural, environmental)
- Assign risk IDs (e.g., RA-001, RA-002)
- Flag any risks rated High or Very High for immediate executive attention
- Note residual risk after proposed controls

### 3. RMF Integration
Risk assessment outputs map to RMF steps (SP 800-37 Rev 2):

| RMF Step | SP 800-30 Integration |
|----------|----------------------|
| Categorise (Step 1) | Risk assessment informs system categorisation (FIPS 199 impact level) |
| Select (Step 2) | Risk assessment results guide tailoring of SP 800-53 control baselines |
| Assess (Step 4) | Security assessment results update risk factors in task 4-1 |
| Authorise (Step 5) | Risk assessment report is key input to Authorization Package |
| Monitor (Step 6) | Continuous monitoring triggers risk assessment updates per task 4-1/4-2 |

### 4. Threat Modelling Support
When helping to identify and prioritise threat sources and events:
1. Use Table D-1 (adversarial) and D-2 (non-adversarial) as the starting taxonomy
2. Consider the organisation's sector, mission criticality, and known adversary targeting
3. Apply relevance filtering: is this threat source known to target this type of organisation?
4. Cross-reference CISA advisories and sector-specific threat reports for adversarial assessment
5. For each relevant threat event, trace the kill chain: Initial Access → Execution → Persistence → Privilege Escalation → Exfiltration

---

## Qualitative Risk Scales Reference

### Likelihood of Threat Event Initiation (Adversarial) — Table G-2
| Value | Qualitative | Description |
|-------|-------------|-------------|
| 10 | Very High | Adversary is highly capable and motivated; attacks of this type are common against similar targets |
| 8 | High | Adversary is capable and motivated; attacks of this type occur regularly against similar targets |
| 5 | Moderate | Adversary has some capability and motivation; attacks of this type occur occasionally |
| 2 | Low | Adversary has limited capability or motivation; attacks of this type occur rarely |
| 0 | Very Low | Adversary has very limited capability or motivation; attacks of this type are very rare |

### Likelihood of Adverse Impact (Vulnerability Severity Predicate) — Table G-3
| Value | Qualitative | Description |
|-------|-------------|-------------|
| 10 | Very High | Vulnerabilities are highly exploitable and widely present; controls are largely absent |
| 8 | High | Vulnerabilities are likely exploitable; controls are mostly absent or ineffective |
| 5 | Moderate | Vulnerabilities are somewhat exploitable; controls exist but have gaps |
| 2 | Low | Vulnerabilities are difficult to exploit; effective controls are in place |
| 0 | Very Low | Vulnerabilities are very difficult to exploit; comprehensive controls exist |

### Impact Levels — Table H-3
| Value | Level | Description |
|-------|-------|-------------|
| 10 | Very High | Multiple severe/catastrophic effects on operations, assets, individuals, national security |
| 8 | High | Severe degradation; major damage; major harm |
| 5 | Moderate | Significant degradation; significant damage; significant harm |
| 2 | Low | Limited degradation; minor damage; minor harm |
| 0 | Very Low | Negligible effects; negligible damage; negligible harm |

---

## Reference Files

Load the appropriate reference file based on the task:

- `references/risk-assessment-process.md` — Detailed task-by-task process guide with all SP 800-30 tables
- `references/threat-taxonomy.md` — Complete threat source and threat event taxonomy from Appendices D and E
- `references/impact-likelihood-scales.md` — All qualitative and semi-quantitative scales for likelihood, impact, and risk determination

**When to load:**
- Conducting a risk assessment → load `references/risk-assessment-process.md`
- Identifying threats → load `references/threat-taxonomy.md`
- Setting scales or scoring risks → load `references/impact-likelihood-scales.md`

---

## Disclaimer

This skill provides guidance based on NIST SP 800-30 Rev 1 (NIST, September 2012), a freely available public publication. This skill does not constitute legal, audit, or professional compliance advice. Organisations should engage qualified risk assessment professionals and consult current NIST publications and CISA advisories to validate their risk assessment approach, particularly for high-impact federal information systems.

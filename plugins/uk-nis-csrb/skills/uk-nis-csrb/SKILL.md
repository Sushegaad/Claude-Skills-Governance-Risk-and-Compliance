---
name: uk-nis-csrb
description: >
  Expert advisor on the UK Cyber Security and Resilience Bill (CSRB), announced in the King's
  Speech on 17 July 2024. Use this skill whenever a user asks about the CSRB, Cyber Security
  and Resilience Bill, UK cybersecurity legislation reform, expansion of NIS Regulations scope
  to managed service providers (MSPs), new incident reporting obligations under the CSRB,
  enhanced regulator powers under the Bill, data centre security obligations, critical national
  infrastructure (CNI) cyber resilience, CSRB readiness assessments, transition planning from
  NIS Regulations 2018, CSRB regulatory framework, or any question about how the CSRB changes
  existing UK cyber regulatory requirements. Also trigger for comparisons between the NIS
  Regulations 2018 and the CSRB, or questions about how to prepare for CSRB obligations before
  the Bill comes into force. When in doubt, use this skill.
---

# UK Cyber Security and Resilience Bill (CSRB) — Compliance Skill

You are an expert advisor on the UK Cyber Security and Resilience Bill (CSRB). You help organisations understand the proposed legislative changes, assess their readiness, plan transition from the NIS Regulations 2018, and prepare for new obligations that the Bill will create when enacted.

> **Important — Bill Status:** The Cyber Security and Resilience Bill is proposed UK legislation announced in the King's Speech on 17 July 2024. As of the date of this skill, the Bill has been introduced to Parliament but has not yet received Royal Assent and is not yet law. The provisions described in this skill are based on the Bill's stated policy objectives, Department for Science, Innovation and Technology (DSIT) consultations, and published impact assessments. The final legislation may differ from the proposals described here. Always verify the current status at bills.parliament.uk.

> **Legal disclaimer:** This guidance is for informational purposes only and does not constitute legal advice. For formal compliance conclusions, consult a qualified legal or regulatory specialist.

---

## Quick Reference: What Does the User Need?

| User Goal | Go To |
|---|---|
| "What is the CSRB?" / overview | [CSRB Overview](#1-csrb-overview) |
| "Are we in scope?" / expanded scope | [Scope and Applicability](#2-scope-and-applicability) |
| New incident reporting requirements | [Enhanced Incident Reporting](#3-enhanced-incident-reporting) |
| Enhanced regulator powers | [Regulator Powers](#4-regulator-powers) |
| Readiness assessment / gap analysis | [CSRB Readiness Assessment](#5-csrb-readiness-assessment) |
| Transitioning from NIS Regulations 2018 | [Transition from NIS Regulations](#6-transition-from-nis-regulations) |
| Policy and document generation | [Policy and Document Generation](#7-policy-and-document-generation) |
| Comparing CSRB with NIS Regs / EU NIS2 | [Comparative Analysis](#8-comparative-analysis) |

---

## 1. CSRB Overview

### 1.1 Why the CSRB Is Being Introduced

The UK government identified that the NIS Regulations 2018 (SI 2018/506), while effective at the time of enactment, have become insufficient to address the evolving cyber threat landscape. The stated policy rationale for the CSRB includes:

- **Expanding scope to managed service providers:** MSPs were recognised as a significant attack vector (as demonstrated by high-profile incidents such as the MOVEit exploitation in 2023 and the Capita breach). MSPs are not currently captured by the NIS Regulations.
- **Improving incident reporting:** The existing NIS incident reporting regime focusses on significant impacts that have already occurred. The CSRB is designed to capture a broader set of incidents and near-misses to enable earlier regulatory and government intervention.
- **Strengthening regulator powers:** Competent Authorities under the NIS Regulations have limited proactive powers. The CSRB would give regulators stronger information-gathering and enforcement tools.
- **Protecting data centres:** Large data centres were assessed to represent critical national infrastructure but were not in scope of the NIS Regulations. The CSRB addresses this.
- **Modernising the framework:** The CSRB reflects the cyber threat landscape of the 2020s, including supply chain attacks, ransomware, and the criticality of cloud and managed services.

### 1.2 Key Policy Announcements and Timeline

| Event | Date |
|-------|------|
| Cyber Security and Resilience Bill announced in King's Speech | 17 July 2024 |
| DSIT published background to the Bill | July 2024 |
| DSIT consultation on expanded scope (MSPs and data centres) | 2023-2024 (pre-announcement) |
| Bill introduced to Parliament | 2025 |
| Parliamentary passage | In progress (as of 2026) |
| Expected Royal Assent | Subject to parliamentary process |
| Expected commencement | Subject to secondary legislation after Royal Assent |

### 1.3 High-Level Changes

The CSRB is designed to:
1. **Expand the scope** of the existing NIS regulatory framework to include managed service providers, data centres, and potentially other categories not currently covered
2. **Strengthen incident reporting** to require reporting of a wider category of incidents with more standardised details and potentially shorter timelines
3. **Enhance regulator powers** to enable Competent Authorities to be more proactive in assessing and enforcing compliance
4. **Introduce new security duties** that reflect current best practice
5. **Align more closely** with equivalent frameworks internationally (EU NIS2 Directive, which came into force October 2024)

---

## 2. Scope and Applicability

### 2.1 Retained Scope from NIS Regulations 2018

The CSRB retains the full scope of the NIS Regulations 2018. Existing OES and DSPs remain in scope:

**Operators of Essential Services (OES) sectors:**
- Energy: electricity, oil, gas
- Transport: air, rail, road, maritime
- Health
- Drinking water
- Digital infrastructure: IXPs, DNS providers, TLD registries

**Digital Service Providers (DSPs):**
- Online marketplaces
- Online search engines
- Cloud computing services (IaaS, PaaS, SaaS — above the small enterprise threshold)

Load `references/scope-expansion.md` for full scope detail, including new categories.

### 2.2 New In-Scope Categories Under the CSRB

#### Managed Service Providers (MSPs)

A managed service provider (MSP) is an entity that remotely manages a customer's IT infrastructure and/or end-user systems, typically on an ongoing subscription basis.

**Why MSPs are newly in scope:**
The CSRB recognises that MSPs occupy a privileged position in customer environments — they typically have elevated access to IT systems, data, and security controls. A compromise of an MSP can cascade to multiple customers simultaneously, creating systemic risk across critical sectors.

**Indicative scope criteria for MSPs:**
- The MSP provides ongoing remote management of IT infrastructure or security services to customers in critical sectors (OES sectors or public sector)
- The MSP's compromise could affect multiple organisations or essential services
- Size thresholds (to be defined by secondary legislation — likely connected to number of critical sector customers or revenue from such services)

**Services likely to be in scope:**
- Managed Detection and Response (MDR)
- Managed Security Operations Centre (SOC) services
- Managed Network Services
- Managed Backup and Disaster Recovery
- Managed Cloud Services

**Services less likely to be in scope (indicative, based on policy intent):**
- Software-as-a-service providers without ongoing management of customer infrastructure
- IT resellers without managed services
- Break-fix IT support without ongoing remote access

#### Large Data Centres

The CSRB is expected to designate large-scale data centres as a category of critical infrastructure in scope of mandatory security and resilience obligations.

**Indicative scope criteria for data centres:**
- Data centre operators above a certain capacity threshold (exact threshold subject to secondary legislation)
- Data centres hosting critical or government systems
- Colocation data centre operators (not just cloud service provider-operated facilities)

**Key concern:** A successful attack on a large data centre can affect multiple tenants simultaneously, creating cascading impacts across critical services.

### 2.3 Determining CSRB Scope (Readiness Assessment)

Until the CSRB receives Royal Assent and secondary legislation defines precise thresholds, organisations should assess their likely scope using the following questions:

| Question | If YES — likely in scope |
|----------|--------------------------|
| Is your organisation currently designated as OES or DSP? | Continuing obligations under CSRB |
| Do you provide IT/security management services to critical sector organisations? | Likely MSP scope |
| Do you operate a data centre above significant scale? | Likely data centre scope |
| Do you have elevated remote access to multiple organisations' systems? | Consider MSP scope |
| Could a compromise of your systems cascade to essential services? | CSRB likely applies |

---

## 3. Enhanced Incident Reporting

### 3.1 Key Changes from NIS Regulations 2018

The CSRB proposes material changes to the incident reporting regime:

| Aspect | NIS Regulations 2018 | CSRB (Proposed) |
|--------|---------------------|-----------------|
| Threshold for reporting | Significant/substantial impact on service continuity | Lower threshold — broader set of incidents |
| Timeline | As soon as reasonably practicable (72 hours guidance) | Compressed timeline likely (potential 24-hour initial notification) |
| Scope of reportable incidents | Incidents with impact on essential/digital service | Including near-misses; precursor events; supply chain incidents |
| Who reports | Individual OES/DSP | Including MSPs |
| Regulator visibility | Post-incident notification | More real-time reporting capability |
| Standardisation | No standard format specified | Standardised reporting formats expected |

### 3.2 New Categories of Reportable Events

The CSRB policy intent includes expanding reporting to cover:

1. **Near-miss incidents** — Events that could have had significant impact but were contained before service disruption
2. **Ransomware attacks** — Including ransomware deployments that are contained before service impact (potentially creating a separate reporting track for ransomware events)
3. **Supply chain compromise** — Incidents involving compromise of a supplier that has access to the organisation's systems
4. **Data exfiltration events** — Theft of data from systems underpinning critical services
5. **Precursor activity** — Detected reconnaissance or preparatory activity that indicates potential imminent attack

### 3.3 Improved Information Sharing Objective

The CSRB is designed to give the government (DSIT, NCSC) better visibility of the cyber threat landscape across critical sectors. This means:

- Incident reports may be shared (in anonymised or aggregated form) across sectors
- NCSC may issue threat advisories based on reported patterns
- Cross-sector intelligence will inform national cyber defence

### 3.4 Practical Preparation for Enhanced Reporting

Organisations should prepare for CSRB reporting requirements by:

1. **Reviewing detection capability** — Ensure security monitoring can detect the wider range of reportable events (near-misses, precursor activity)
2. **Updating incident classification** — Expand incident classification frameworks to capture CSRB reportable categories
3. **Reducing reporting timelines** — Update Incident Response Plans to operate on 24-hour reporting timelines, not just 72 hours
4. **Standardising report content** — Prepare for structured reporting formats
5. **Reviewing supply chain monitoring** — Build processes to detect and report supplier-side incidents

Load `references/incident-reporting-csrb.md` for detailed guidance and templates.

---

## 4. Regulator Powers

### 4.1 Enhanced Competent Authority Powers

The CSRB provides Competent Authorities with stronger proactive and enforcement tools compared with the NIS Regulations 2018:

| Power | NIS Regs 2018 | CSRB (Proposed) |
|-------|--------------|-----------------|
| Information requests | Yes (reactive) | Yes — with expanded proactive capability |
| Security audits | Yes (can commission) | Yes — with stronger mandate |
| Inspections | Yes | Yes — more extensive |
| Directions to improve security | Enforcement notice after failure | Proactive notices/directions before failure |
| Enforcement notices | Yes — after failure | Yes |
| Financial penalties | Up to 17M GBP | May increase — to be specified in legislation |
| Sharing of information | Limited | Enhanced cross-CA information sharing |

### 4.2 Proactive Powers

A key shift in the CSRB is the move from reactive enforcement to **proactive oversight**:

- Competent Authorities may issue directions requiring organisations to undertake specific security assessments or audits before any failure occurs
- CAs may share threat intelligence directly with in-scope organisations
- CAs may require evidence of compliance testing (penetration tests, CAF self-assessments) on a scheduled basis rather than only following incidents

### 4.3 New Competent Authorities (MSPs / Data Centres)

The CSRB will designate Competent Authorities for newly in-scope categories:
- **MSPs:** Likely DSIT or Ofcom (to be confirmed in secondary legislation)
- **Large data centres:** Likely DSIT (to be confirmed in secondary legislation)

Existing CAs retain responsibility for their current sectors.

### 4.4 Implications for Organisations

- Expect more frequent CA engagement (proactive audits, directed assessments)
- Ensure documented evidence of security measures is readily available
- Compliance programme should be continuous, not just audit-responsive
- Designated security contacts should be maintained and accessible

---

## 5. CSRB Readiness Assessment

### Step 1: Determine Current NIS Status

Confirm:
- Is the organisation currently an OES or DSP under the NIS Regulations 2018?
- If yes, what is its current compliance posture against the NCSC CAF?
- Identify any outstanding gaps from the most recent CAF self-assessment

### Step 2: Assess CSRB Expansion Impact

Assess whether the organisation falls into new CSRB categories:
- MSP: Does it provide managed IT or security services to critical sector organisations?
- Data centre: Does it operate data centre facilities above likely thresholds?
- New Competent Authority: Identify who the new CA will be

### Step 3: Review Incident Reporting Capability

Gap analysis against CSRB reporting requirements:

| Capability | Current State | CSRB Gap |
|-----------|--------------|----------|
| Detection of near-miss events | [Describe] | [Gap] |
| Detection of precursor / reconnaissance | [Describe] | [Gap] |
| 24-hour reporting workflow | [Yes/No] | [Gap] |
| Standardised incident classification | [Describe] | [Gap] |
| Supply chain incident monitoring | [Describe] | [Gap] |

### Step 4: Review Security Controls

Ensure existing CAF/NIS controls are current:
- Latest CAF self-assessment date?
- Any outstanding NIS Conditions from Competent Authority?
- Are controls tested (penetration testing, exercises)?

### Step 5: Produce Readiness Report

Structure readiness output as:

```
## CSRB Readiness Assessment — [Organisation Name]

**Assessment Date:** [YYYY-MM-DD]
**Current NIS Status:** [OES / DSP / Not currently in scope]
**Likely CSRB Status:** [OES (continuing) / DSP (continuing) / MSP (new) / Data Centre (new) / Multiple]
**Anticipated Competent Authority:** [CA name]

### Current Compliance Foundation (NIS Regs 2018)
[Summary of CAF status and gaps]

### CSRB Expansion Impact
[Whether organisation falls into new categories and implications]

### Incident Reporting Gaps
| Gap | Priority | Action | Owner | Target Date |
|-----|----------|--------|-------|-------------|
| ... | ... | ... | ... | ... |

### Security Control Gaps (CSRB-specific)
[Any additional controls required beyond current CAF]

### Recommended Actions
1. [Priority 1 action]
2. [Priority 2 action]

*This assessment is based on CSRB policy proposals as of [date]. Verify against enacted legislation once available.*
```

---

## 6. Transition from NIS Regulations

### 6.1 CSRB Transition Principles

When the CSRB is enacted:
- Existing OES and DSP designations will carry over automatically — no redesignation process expected
- Existing CAF assessments and compliance programmes provide a foundation but must be reviewed against any new CSRB obligations
- New categories (MSPs, data centres) will have a transition/grace period for designation and compliance (exact timelines subject to secondary legislation)

### 6.2 Transition Checklist for Current OES/DSPs

```
PRE-ENACTMENT (Actions to take now):
[ ] Review current CAF self-assessment — ensure it is current (within 12 months)
[ ] Remediate outstanding CAF gaps (especially A1, A2, D1)
[ ] Update Incident Response Plan to accommodate expanded reporting categories
[ ] Reduce internal incident reporting workflows to 24-hour timeline
[ ] Map third-party/MSP dependencies and review their security posture
[ ] Brief board/senior management on CSRB changes and timeline
[ ] Establish a CSRB monitoring process (track bill progress at bills.parliament.uk)

POST-ENACTMENT (Actions once CSRB receives Royal Assent):
[ ] Review final legislation against these guidance notes for any changes
[ ] Update NIS Compliance Policy to reference CSRB provisions
[ ] Navigate any new designation/registration process required by CSRB
[ ] Engage with Competent Authority on new reporting format/portal when available
[ ] Update supplier contracts to reflect CSRB supply chain obligations
[ ] Conduct fresh CAF/CSRB gap assessment against final legislative requirements
```

### 6.3 Transition Checklist for Newly In-Scope MSPs

```
PRE-ENACTMENT:
[ ] Assess whether CSRB MSP definitions likely apply to your services
[ ] Review your own security posture against the NIS CAF framework (as a baseline)
[ ] Review customer contracts for cyber incident notification obligations
[ ] Identify the likely Competent Authority for MSPs in your sector
[ ] Monitor DSIT consultations and secondary legislation announcements

POST-ENACTMENT:
[ ] Confirm scope status and register with Competent Authority as required
[ ] Build a NIS/CSRB-compliant information security management system
[ ] Implement security measures to at least CAF standard
[ ] Establish CSRB-compliant incident reporting capability
[ ] Update customer contracts to reflect your CSRB obligations
```

---

## 7. Policy and Document Generation

When generating CSRB readiness documents, include:
- Organisation name: `[ORGANISATION NAME]`
- Document version: `[VERSION]`
- Bill status note: "Based on CSRB as [published/introduced/enacted] — review following Royal Assent"
- Date: `[DATE]`

Load `references/templates-csrb.md` for CSRB-specific policy and document templates.

### Key CSRB Documents to Prepare in Advance

| Document | Purpose | Priority |
|----------|---------|----------|
| CSRB Readiness Assessment | Baseline gap analysis | High — do now |
| Updated Incident Response Plan | Accommodate CSRB reporting | High — do now |
| CSRB Compliance Roadmap | Action plan for transition | High — do now |
| Updated NIS/CSRB Compliance Policy | When enacted | Medium |
| MSP Customer Security Addendum | For MSPs | Medium |
| Board CSRB Briefing | Leadership awareness | High — do now |

---

## 8. Comparative Analysis

### 8.1 CSRB vs NIS Regulations 2018

| Aspect | NIS Regulations 2018 | CSRB |
|--------|---------------------|------|
| Legislative basis | SI 2018/506 (retained from EU NIS Directive) | Primary UK legislation |
| Sectors | 5 (energy, transport, health, water, digital infrastructure) | 5 existing + MSPs + data centres + potentially more |
| MSPs in scope | No | Yes |
| Data centres in scope | Only if operating DNS/IXP/TLD | Yes (large data centres) |
| Incident reporting | Significant/substantial impact on service continuity | Broader — includes near-misses and precursor events |
| Reporting timeline | As soon as reasonably practicable (72hr guidance) | Likely compressed (24hr initial) |
| CA powers | Reactive enforcement | Proactive oversight + reactive enforcement |
| Financial penalties | Up to 17M GBP | Expected to remain significant; exact figure in legislation |
| Technical standard | NCSC CAF | NCSC CAF (expected to remain primary standard) |

### 8.2 CSRB vs EU NIS2 Directive

The EU NIS2 Directive (Directive (EU) 2022/2555) came into force on 16 January 2023 and was required to be transposed by EU member states by 17 October 2024. The UK is not subject to NIS2 (post-Brexit) but NIS2 informed CSRB policy development.

| Aspect | EU NIS2 | UK CSRB |
|--------|---------|---------|
| Effective | 17 October 2024 (transposition deadline) | Subject to Royal Assent and commencement |
| Entities covered | Essential entities and important entities across broader sector list | OES, DSPs, MSPs, data centres |
| MSPs in scope | Yes (important entities) | Yes |
| Incident reporting timeline | 24 hours (early warning), 72 hours (incident notification) | Likely similar |
| Supply chain security | Explicit requirement | Implicit through CAF; may be made explicit |
| Penalties | Up to 10M EUR or 2% global turnover (essential); 7M EUR or 1.4% (important) | TBD — likely significant |
| Certification | Creates pathway for national cybersecurity certification schemes | NCSC CAF remains primary standard |

---

## Reference Files

| File | Load When |
|------|-----------|
| `references/scope-expansion.md` | Scope determination, MSP and data centre categorisation |
| `references/incident-reporting-csrb.md` | CSRB incident reporting obligations and templates |
| `references/regulator-powers-csrb.md` | Regulator powers, enforcement, and proactive oversight |
| `references/templates-csrb.md` | CSRB readiness documents, gap assessment templates, IRP updates |

Load **all** reference files for comprehensive CSRB readiness assessments or programme-level reviews.

---
name: uk-nis
description: >
  Expert UK NIS Regulations 2018 compliance advisor. Use this skill whenever a user asks about
  UK NIS, the Network and Information Systems Regulations 2018 (SI 2018/506), Operators of
  Essential Services (OES), Digital Service Providers (DSPs), the NCSC Cyber Assessment
  Framework (CAF), NIS incident reporting, NIS competent authorities (Ofgem, CAA, ORR, DfT,
  DHSC, DWI, Ofcom, ICO), NIS enforcement notices, NIS security requirements, NIS gap
  assessments, CAF self-assessments, or cybersecurity obligations for UK critical national
  infrastructure. Also trigger for questions about UK NIS post-Brexit retention, the 14 CAF
  security principles, critical sectors (energy, transport, health, water, digital
  infrastructure), or NIS fines (up to 17 million GBP). When in doubt, use this skill.
---

# UK NIS Regulations 2018 — Compliance Skill

You are an expert advisor on the UK Network and Information Systems (NIS) Regulations 2018 (SI 2018/506). You assist compliance teams, security professionals, and operators of essential services (OES) and digital service providers (DSPs) across all aspects of NIS compliance.

> **Legal disclaimer:** This guidance is for informational purposes only and does not constitute legal advice. For formal compliance determinations, consult a qualified legal or regulatory specialist.

---

## Quick Reference: What Does the User Need?

| User Goal | Go To |
|---|---|
| "Are we in scope?" / scope determination | [Scope & Applicability](#1-scope--applicability) |
| Gap assessment / readiness review | [Gap Assessment Workflow](#2-gap-assessment-workflow) |
| Understanding security requirements | [Security Requirements & CAF](#3-security-requirements--caf) |
| Incident reporting obligations | [Incident Reporting](#4-incident-reporting) |
| Competent authority guidance | [Competent Authorities](#5-competent-authorities) |
| Enforcement, penalties & appeals | [Enforcement & Penalties](#6-enforcement--penalties) |
| Policy or document generation | [Policy & Document Generation](#7-policy--document-generation) |
| CAF objective deep-dive | [CAF Objectives Reference](#8-caf-objectives-reference) |

---

## 1. Scope & Applicability

### 1.1 Legislative Basis

The NIS Regulations 2018 (Statutory Instrument 2018/506) came into force on **10 May 2018**. They implement the EU NIS Directive (Directive (EU) 2016/1148) into UK domestic law. Following Brexit, the Regulations were retained in UK law by the European Union (Withdrawal) Act 2018 and continue to apply in full.

### 1.2 Who Is In Scope?

The Regulations apply to two categories of entity:

#### Operators of Essential Services (OES)

An OES is an entity that:
1. Provides a service which is essential for the maintenance of critical societal or economic activities
2. The provision of that service depends on network and information systems
3. An incident would have significant disruptive effects on the provision of that service

**Designated OES sectors and sub-sectors:**

| Sector | Sub-sector |
|--------|-----------|
| Energy | Electricity (generation, transmission, distribution, supply) |
| Energy | Oil (transport, distribution, storage) |
| Energy | Gas (transmission, distribution, storage, LNG facilities, supply) |
| Transport | Air transport |
| Transport | Rail transport |
| Transport | Road transport (if designated — limited scope) |
| Transport | Water transport (inland waterways, sea ports, shipping) |
| Health | Healthcare providers (NHS Trusts, independent providers) |
| Drinking Water | Water supply and distribution |
| Digital Infrastructure | Internet Exchange Points (IXPs) |
| Digital Infrastructure | Domain Name System (DNS) service providers |
| Digital Infrastructure | Top-Level Domain (TLD) name registries |

OES status is determined by relevant **Competent Authorities** (not self-declared). Competent Authorities issue designation decisions and maintain registers of OES within their sectors.

#### Digital Service Providers (DSPs)

Any legal person that provides one of the following digital services to recipients established in the UK, where the provider has its EU/UK establishment or (if outside the EU/UK) its designated UK representative:

| DSP Type | Description |
|----------|------------|
| Online marketplace | Platform enabling consumers/traders to conclude online contracts |
| Online search engine | Platform enabling searches across all websites on a given input |
| Cloud computing service | IaaS, PaaS, or SaaS services (excluding micro and small enterprises with fewer than 50 employees and annual turnover/balance sheet not exceeding 10 million EUR) |

**Exemptions:**
- Micro and small enterprises (fewer than 50 employees AND annual turnover/balance sheet total not exceeding 10 million EUR) are exempt from DSP requirements
- Public electronic communications networks and services (covered by NIS but under Ofcom competence)
- Trust service providers covered by the eIDAS Regulation

### 1.3 Threshold Determination

When assessing whether an entity is in scope, consider:

**For OES designation:**
- Is the service essential to critical societal/economic activity?
- Does it depend on NIS?
- Would an incident cause significant disruption?
- The relevant Competent Authority makes the formal designation

**For DSPs:**
- Is the entity providing online marketplace, search engine, or cloud services?
- Does the entity have 50 or more employees OR exceed 10 million EUR in turnover/balance sheet?
- Is the entity established in the UK or serving UK recipients?

---

## 2. Gap Assessment Workflow

### Step 1: Determine Entity Type and Scope
1. Confirm whether the entity is an OES or DSP (or both)
2. Identify the relevant Competent Authority
3. Confirm which systems are in scope (NIS systems that underpin the essential/digital service)

### Step 2: Map Against CAF Objectives (OES) or DSP Security Measures

For OES: Use the **14 CAF outcomes** as the assessment framework (see Section 3)
For DSPs: Use the **DSP Security Principles** (see Section 3.3)

### Step 3: Collect Evidence

For each CAF objective/outcome:
- Review existing policies, procedures, and technical controls
- Interview key personnel
- Review logs, audit records, and test results
- Check supplier/third-party arrangements

### Step 4: Rate Each Outcome

| Rating | Meaning |
|--------|---------|
| Achieved | All Indicators of Good Practice (IGP) are met; no Indicators of Poor Practice (IPP) apply |
| Partially Achieved | Some IGP met; no critical IPP; work in progress |
| Not Achieved | Critical IGP not met; significant IPP apply |
| Not Applicable | Outcome is not relevant to this system (document justification) |

### Step 5: Produce Gap Report

Structure output as:

```
## NIS Compliance Gap Assessment — [Entity Name]

**Entity Type:** OES / DSP
**Sector:** [Sector]
**Competent Authority:** [CA name]
**Assessment Date:** [YYYY-MM-DD]
**Assessor:** [Name/Role]

### Executive Summary
[Brief overview of compliance posture and critical gaps]

### CAF Objective Assessment

| Objective | Outcome | Rating | Evidence Reviewed | Gaps / Issues | Priority |
|-----------|---------|--------|-------------------|---------------|----------|
| A1 | Governance | Partial | IS Policy v2.1 | No board-level cyber sign-off | High |
| ... | ... | ... | ... | ... | ... |

### Key Findings
1. [Finding 1 — severity, objective reference]
2. [Finding 2]

### Recommended Actions
| Priority | Action | Objective | Owner | Target Date |
|----------|--------|-----------|-------|-------------|
| Critical | ... | A1 | CISO | 30 days |

*This assessment uses the NCSC Cyber Assessment Framework (CAF) version 3.2 as the technical standard.*
```

---

## 3. Security Requirements & CAF

### 3.1 Security Obligation (Regulation 10)

OES must take **appropriate and proportionate** technical and organisational measures to manage risks to the security of NIS used for providing essential services. Proportionality is assessed against:
- The state of the art in security
- The risk presented
- Prevention and minimisation of impact of security incidents

Regulation 10 does not prescribe specific controls — the **NCSC Cyber Assessment Framework (CAF)** is the UK government's primary technical standard for demonstrating compliance.

### 3.2 CAF Overview

The CAF was developed by the NCSC and is the primary assessment framework used by UK NIS Competent Authorities. It is structured around **4 objectives** and **14 contributing outcomes**.

Load `references/caf-objectives.md` for the full detail of each outcome, its Indicators of Good Practice (IGP), and Indicators of Poor Practice (IPP).

#### CAF Structure Summary

| Objective | ID | Contributing Outcome |
|-----------|-----|---------------------|
| **A. Managing Security Risk** | A1 | Governance |
| | A2 | Risk Management |
| | A3 | Asset Management |
| | A4 | Supply Chain |
| **B. Protecting Against Cyber Attack** | B1 | Service Protection Policies and Processes |
| | B2 | Identity and Access Control |
| | B3 | Data Security |
| | B4 | System Security |
| | B5 | Resilient Networks and Systems |
| | B6 | Staff Awareness and Training |
| **C. Detecting Cyber Security Events** | C1 | Security Monitoring |
| | C2 | Proactive Security Event Discovery |
| **D. Minimising Impact of Cyber Security Incidents** | D1 | Response and Recovery Planning |
| | D2 | Improvements |

### 3.3 DSP Security Measures (Regulation 12)

DSPs must take appropriate and proportionate technical and organisational measures to manage risks to security of NIS, addressing:

| Security Measure | Description |
|-----------------|-------------|
| Security of systems and facilities | Physical and logical security of network and information systems |
| Incident handling | Documented procedures for responding to incidents |
| Business continuity management | Measures for maintaining or restoring service delivery |
| Monitoring, auditing and testing | Regular assessment of security measures effectiveness |
| Compliance with international standards | Alignment with ISO/IEC 27001 or equivalent standards |

DSPs also have incident reporting obligations to the **ICO** (Information Commissioner's Office) as the designated Competent Authority for DSPs in the UK.

---

## 4. Incident Reporting

### 4.1 OES Reporting Obligations (Regulation 11)

OES must notify their relevant Competent Authority of any incident that has a **significant impact** on the continuity of the essential service.

**Significant impact factors (Regulation 11(3)):**

| Factor | Description |
|--------|-------------|
| Number of users affected | The number of users relying on the service affected by the incident |
| Duration | The length of time the incident lasted |
| Geographic spread | The geographic area affected by the incident |
| Extent of disruption | The degree to which the functioning of the service has been affected |
| Extent of impact | The extent of impact on economic and societal activities |

**Notification timeline:**

There is no specific statutory deadline stated in the NIS Regulations 2018 for initial notification. However, guidance from Competent Authorities (and the NCSC) consistently requires notification **as soon as reasonably practicable** — typically within 72 hours of becoming aware of a significant incident.

**Notification must include:**
- Description of the incident
- Impacts on the continuity of the service
- Any cross-border impacts (where known)

### 4.2 DSP Reporting Obligations (Regulation 13)

DSPs must notify the ICO of incidents having **substantial impact** on the provision of a digital service.

**Substantial impact factors:**

| Factor | Description |
|--------|-------------|
| Number of users affected | Particularly those relying on the service for professional purposes |
| Duration | Hours of disruption |
| Geographic spread | Regions affected |
| Extent of disruption | Degree of impairment |
| Impact significance | Affected societal or economic functions |
| System integrity affected | Whether personal data security was compromised |

**DSP notification timeline:** Without undue delay after becoming aware, and where feasible within 72 hours.

### 4.3 Notification Template

Load `references/incident-reporting.md` for structured notification templates for both OES and DSP incident reports.

### 4.4 NCSC Reporting

The NCSC is the technical advisory body for NIS in the UK. OES and DSPs are encouraged (and in some cases expected) to also report to the NCSC via the NCSC reporting portal at report.ncsc.gov.uk for technical assistance and national-level coordination.

---

## 5. Competent Authorities

### 5.1 OES Competent Authorities by Sector

| Sector | Competent Authority | Website |
|--------|-------------------|---------|
| Electricity | Ofgem (Office of Gas and Electricity Markets) | ofgem.gov.uk |
| Oil | BEIS (Dept for Energy Security and Net Zero from 2023) | gov.uk/desnz |
| Gas | Ofgem | ofgem.gov.uk |
| Air transport | Civil Aviation Authority (CAA) | caa.co.uk |
| Rail transport | Office of Rail and Road (ORR) | orr.gov.uk |
| Road transport | Dept for Transport (DfT) | gov.uk/dft |
| Water transport (maritime) | Dept for Transport / Maritime and Coastguard Agency (MCA) | gov.uk/mca |
| Health | Department of Health and Social Care (DHSC) / NHS England | england.nhs.uk |
| Drinking water | Drinking Water Inspectorate (DWI) | dwi.gov.uk |
| Digital infrastructure (IXPs, DNS, TLDs) | Ofcom | ofcom.org.uk |

### 5.2 DSP Competent Authority

| DSP Type | Competent Authority |
|----------|-------------------|
| Online marketplaces, online search engines, cloud computing | Information Commissioner's Office (ICO) |

### 5.3 Lead Government Authority

The **Department for Science, Innovation and Technology (DSIT)** (formerly DCMS) has overall policy responsibility for UK NIS and coordination between Competent Authorities.

### 5.4 CA Powers

Competent Authorities have powers to:
- Request information from OES/DSPs to assess compliance
- Carry out security audits (directly or via approved third parties)
- Issue enforcement notices requiring specific security measures
- Issue penalty notices for non-compliance

---

## 6. Enforcement & Penalties

### 6.1 Enforcement Notices (Regulation 18)

A Competent Authority may issue an **enforcement notice** where it is satisfied that an OES or DSP has failed, is failing, or is likely to fail to comply with the Regulations. The notice must specify:
- The nature of the failure
- The steps required to remedy the failure
- The time period for compliance

### 6.2 Penalty Notices (Regulation 19)

Following an enforcement notice, if the OES or DSP fails to comply, the Competent Authority may issue a **penalty notice** imposing a financial penalty.

**Maximum financial penalties:**
- OES: up to **£17,000,000**
- DSP: up to **£17,000,000**

These are maximum penalties; actual penalties are set proportionately based on:
- Severity and duration of the failure
- Whether the failure was deliberate or negligent
- Steps taken to mitigate damage
- Degree of cooperation with the Competent Authority
- Prior contraventions

### 6.3 Appeals

Appeals against enforcement notices and penalty notices are made to the **First-tier Tribunal (General Regulatory Chamber)** under Schedule 4 of SI 2018/506.

### 6.4 No Criminal Liability

The NIS Regulations 2018 do not create criminal offences. Non-compliance leads to civil enforcement notices and financial penalties only.

---

## 7. Policy & Document Generation

When generating NIS compliance documents, always include:
- Organisation name: `[ORGANISATION NAME]`
- Document version: `[VERSION]`
- Date: `[DATE]`
- Review cycle: `[REVIEW CYCLE]`
- Owner: `[OWNER/ROLE]`
- Reference to the specific NIS Regulation or CAF outcome satisfied

### Common Documents

| Document | NIS/CAF Reference | Template In |
|----------|------------------|-------------|
| NIS Compliance Policy | Reg 10, CAF A1 | references/templates.md |
| Risk Assessment & Register | Reg 10, CAF A2 | references/templates.md |
| Asset Register | CAF A3 | references/templates.md |
| Supplier Security Policy | CAF A4 | references/templates.md |
| Incident Response Plan | CAF D1, Reg 11 | references/templates.md |
| NIS Incident Notification | Reg 11 / Reg 13 | references/incident-reporting.md |
| CAF Self-Assessment Record | All CAF | references/caf-objectives.md |
| Business Continuity Plan | CAF D1, B5 | references/templates.md |
| Security Monitoring Procedure | CAF C1 | references/templates.md |

---

## 8. CAF Objectives Reference

Load `references/caf-objectives.md` for the complete CAF framework including all 14 outcomes with their full descriptions, Indicators of Good Practice (IGP), and Indicators of Poor Practice (IPP).

### Quick Objective Summary

**A — Managing Security Risk**
- A1 Governance: Board-level oversight of cyber risk; assigned accountability; integration into corporate governance
- A2 Risk Management: Systematic identification, assessment, and treatment of risks to NIS
- A3 Asset Management: Identification and classification of NIS assets; understanding of their role in service delivery
- A4 Supply Chain: Oversight and management of third-party and supply chain cyber risks

**B — Protecting Against Cyber Attack**
- B1 Service Protection Policies & Processes: Documented, board-endorsed security policies; security by design; change management
- B2 Identity and Access Control: Least privilege; strong authentication; privileged account management; user lifecycle management
- B3 Data Security: Data classification; protection of sensitive data; media handling; data-in-transit and at-rest security
- B4 System Security: Secure configuration; patch management; vulnerability management; endpoint protection; software security
- B5 Resilient Networks and Systems: Network architecture; segregation; defence in depth; backups; fault tolerance
- B6 Staff Awareness and Training: Security awareness programme; role-based training; social engineering prevention

**C — Detecting Cyber Security Events**
- C1 Security Monitoring: Centralised log collection; SIEM; alerting; user behaviour analytics; 24/7 monitoring capability
- C2 Proactive Security Event Discovery: Vulnerability scanning; penetration testing; threat hunting; threat intelligence

**D — Minimising Impact of Cyber Security Incidents**
- D1 Response and Recovery Planning: Documented IRP; tested response procedures; business continuity; backups; recovery time objectives
- D2 Improvements: Post-incident reviews; lessons learned integration; root cause analysis; improvements to controls

---

## Reference Files

| File | Load When |
|------|-----------|
| `references/caf-objectives.md` | CAF deep-dive, gap assessment, policy mapping, control guidance |
| `references/incident-reporting.md` | Drafting incident notifications, understanding reporting thresholds |
| `references/oes-sectors.md` | Scope determination, OES sector detail, Competent Authority mapping |
| `references/templates.md` | Generating NIS policies, registers, plans, and compliance documents |

Load **all** reference files for broad compliance reviews or programme-level assessments.

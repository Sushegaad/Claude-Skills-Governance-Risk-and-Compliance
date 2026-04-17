# SOC for Cybersecurity Reference

## Overview

SOC for Cybersecurity is an entity-level examination engagement introduced by the AICPA in
**2017**. It provides assurance over an organization's **cybersecurity risk management program**
— the full enterprise-wide set of policies, processes, and controls used to identify, assess,
and respond to cybersecurity risks. Unlike SOC 2, which is scoped to a defined system, SOC for
Cybersecurity covers the entire organization.

**Governing standard:** SSAE 18, AT-C Section 205 (*Examination Engagements*)  
**Description criteria:** AICPA DC-4 — *Description Criteria for Management's Description of an Entity's Cybersecurity Risk Management Program* (2017)  
**Measurement criteria:** AICPA Trust Services Criteria for Security (CC1–CC9), 2017 version with 2022 Revised Points of Focus  
**Distribution:** General use — the report may be shared with any stakeholder

**Authoritative source:** AICPA *Reporting on an Entity's Cybersecurity Risk Management Program and Controls* guide (2017).

---

## When SOC for Cybersecurity Applies

| Scenario | Applies? |
|---|---|
| Large enterprise wants board-level cybersecurity assurance | Yes |
| Organization applying for cyber insurance | Yes |
| Public company disclosing cybersecurity risk management to investors | Yes |
| Technology vendor customer requires enterprise security assurance | Yes |
| Service organization wants assurance limited to a specific service | No — use SOC 2 |
| Organization wants unrestricted general use report on security | Yes |
| Healthcare organization subject to HIPAA cybersecurity oversight | May apply alongside HIPAA compliance |
| Government contractor needing formal security examination | May apply alongside other frameworks |

---

## DC-4 Description Criteria — Full Detail

Management's description of the entity's cybersecurity risk management program must address
all nine criteria groups in DC-4. The description must be sufficiently detailed for users to
understand the program.

---

### DC-4.1 — Nature of the Business and Operations

**What must be described:**
- The nature of the entity's business and operations.
- How the entity uses information technology in its business.
- The regulatory environment the entity operates in.
- Third parties with whom the entity shares information or on whom it relies for cybersecurity.

**Why this matters for the examination:**
The practitioner uses this context to understand the cybersecurity risk environment and evaluate
whether the cybersecurity risk management objectives are appropriate.

---

### DC-4.2 — Cybersecurity Objectives

**What must be described:**
- The entity's cybersecurity risk management objectives.
- How cybersecurity objectives align with the entity's business objectives.
- Key commitments to customers, business partners, regulators, or other stakeholders related
  to cybersecurity (e.g., contractual security clauses, regulatory requirements).

---

### DC-4.3 — Factors That Have a Significant Effect on Inherent Cybersecurity Risks

**What must be described:**
- Factors that significantly affect the entity's inherent cybersecurity risks, including:
  - Types and sensitivity of information assets (personal data, financial data, intellectual property).
  - Technologies used (cloud, mobile, OT/ICS, legacy systems).
  - Internal and external threats relevant to the entity.
  - Changes in the technology environment during the period.
  - Third-party connections and dependencies.
  - Workforce factors (remote work, contractors, temporary staff).

---

### DC-4.4 — Cybersecurity Risk Governance Structure

**What must be described:**
- Governance structure for cybersecurity risk management:
  - Board and executive oversight of cybersecurity.
  - Roles and responsibilities (CISO, CIO, risk committee, etc.).
  - Policies that govern cybersecurity (security policy, acceptable use, classification).
  - Accountability mechanisms (consequence management, performance objectives).
- How cybersecurity accountability is established at all levels of the organization.

---

### DC-4.5 — Cybersecurity Risk Identification and Assessment Processes

**What must be described:**
- How the entity identifies cybersecurity risks (threat intelligence sources, vulnerability scanning, penetration testing, audit findings, vendor risk).
- How identified risks are assessed and prioritized (likelihood, impact, risk scoring methodology).
- How the risk appetite and tolerance levels are defined and applied.
- How risk assessments are updated (frequency, trigger events).

---

### DC-4.6 — Cybersecurity Risk Response and Mitigation

**What must be described:**
- How the entity responds to identified cybersecurity risks: accept, mitigate, transfer (insurance), or avoid.
- Risk treatment decisions and their documentation.
- How risk treatment effectiveness is evaluated.
- Key risk mitigation controls implemented.

---

### DC-4.7 — Cybersecurity Monitoring Processes

**What must be described:**
- How the entity monitors its cybersecurity environment:
  - Continuous monitoring of controls.
  - Security event monitoring (SIEM, log management, alerting).
  - Vulnerability management and patch tracking.
  - Penetration testing and red team exercises.
- Frequency of monitoring activities.
- How monitoring results are reported and acted upon.

---

### DC-4.8 — Cybersecurity Communications

**What must be described:**
- **Internal communications:** How cybersecurity information flows within the organization (reporting to the board, metrics to executives, alerts to operations teams).
- **External communications:** How cybersecurity information is communicated to external parties:
  - Customer notification of data breaches or incidents.
  - Regulatory disclosure obligations.
  - Vendor and third-party communication on security incidents.
  - Public disclosure policies.

---

### DC-4.9 — Cybersecurity Control Processes

**What must be described:**
- The control processes in place to detect, prevent, and respond to cybersecurity threats.
- These must cover relevant aspects of the Trust Services Criteria for Security (CC1–CC9).
- Key control categories to address:
  - Identity and access management
  - Network and perimeter security
  - Endpoint protection
  - Data protection and encryption
  - Secure software development
  - Physical security
  - Incident response
  - Business continuity and disaster recovery
  - Third-party risk management

---

## Measurement Criteria — TSC for Security (CC1–CC9)

The practitioner evaluates the effectiveness of the cybersecurity risk management program
against the AICPA Trust Services Criteria for Security across the entire organization.

| Criterion | Title | Key Focus |
|---|---|---|
| CC1 | Control Environment | Integrity, ethical values, board oversight, accountability structure, talent management |
| CC2 | Communication and Information | Internal and external communication of security responsibilities; information quality |
| CC3 | Risk Assessment | Risk identification, analysis, and response; fraud risk assessment |
| CC4 | Monitoring Activities | Ongoing monitoring; separate evaluations; tracking deficiencies |
| CC5 | Control Activities | Policies and procedures; technology controls; segregation of duties |
| CC6 | Logical and Physical Access Controls | Access provisioning and deprovisioning; authentication; physical security |
| CC7 | System Operations | Incident detection and response; security monitoring; backup and recovery |
| CC8 | Change Management | Change authorization; configuration management; software development lifecycle |
| CC9 | Risk Mitigation | Vendor/third-party risk; insurance; business disruption recovery |

For SOC for Cybersecurity, all nine CC criteria apply to the entity's entire program — not just
a specific system. The practitioner evaluates each CC criterion across the program as described
in management's DC-4 description.

---

## SOC for Cybersecurity vs SOC 2 — Detailed Comparison

| Attribute | SOC 2 | SOC for Cybersecurity |
|---|---|---|
| Scope | A specific, defined system or service | The entire entity's cybersecurity risk management program |
| Who it applies to | Service organizations | Any entity |
| Description framework | SSAE 18 system description requirements | DC-4 (nine criteria groups) |
| Measurement framework | TSC (Security required; Availability, C, PI, P optional) | TSC Security (CC1–CC9) only |
| Distribution | Restricted use | General use |
| Primary audience | User entities, user auditors, sophisticated customers | Board, investors, insurers, regulators |
| Focus | Controls implemented on a defined system | Entity-wide governance, risk management, and controls |
| Suitable for board reporting? | Not typically | Yes — designed for board-level audience |
| Can coexist? | Yes | Yes — can issue both for same period |

---

## SOC for Cybersecurity — Readiness Assessment

Use this gap assessment template before engaging a CPA firm for examination.

### DC-4 Coverage Assessment

| DC-4 Criteria | Assessment Questions | Status |
|---|---|---|
| DC-4.1 Business and Operations | Is the entity's business context, technology use, and regulatory environment documented? | [ ] Met / [ ] Partial / [ ] Gap |
| DC-4.2 Objectives | Are cybersecurity objectives documented and aligned to business objectives? | [ ] Met / [ ] Partial / [ ] Gap |
| DC-4.3 Inherent Risk Factors | Have inherent cybersecurity risk factors been identified and documented? | [ ] Met / [ ] Partial / [ ] Gap |
| DC-4.4 Governance | Is there a cybersecurity governance structure with board oversight, defined roles, and policies? | [ ] Met / [ ] Partial / [ ] Gap |
| DC-4.5 Risk Identification and Assessment | Is there a formal risk identification and assessment process? | [ ] Met / [ ] Partial / [ ] Gap |
| DC-4.6 Risk Response | Are risk treatment decisions documented with supporting rationale? | [ ] Met / [ ] Partial / [ ] Gap |
| DC-4.7 Monitoring | Is there continuous monitoring with defined metrics and management reporting? | [ ] Met / [ ] Partial / [ ] Gap |
| DC-4.8 Communications | Are internal and external cybersecurity communication protocols defined and followed? | [ ] Met / [ ] Partial / [ ] Gap |
| DC-4.9 Controls | Are technical and operational controls documented and operational for all CC1–CC9 areas? | [ ] Met / [ ] Partial / [ ] Gap |

### CC1–CC9 Coverage Assessment

| Criterion | Key Question | Common Gap |
|---|---|---|
| CC1 — Control Environment | Does leadership demonstrate commitment to cybersecurity? Is there a code of conduct and an ethics program? | No board-level cybersecurity agenda; no security KPIs tied to performance |
| CC2 — Communication | Are cybersecurity roles, policies, and responsibilities communicated to all relevant personnel? | Policies exist but are not distributed or acknowledged; external disclosures not defined |
| CC3 — Risk Assessment | Is there a formal, documented enterprise cybersecurity risk assessment? | Risk assessments ad-hoc; no risk register; no defined risk tolerance |
| CC4 — Monitoring | Are controls monitored for effectiveness on an ongoing basis? | Controls designed but never tested; no deficiency tracking mechanism |
| CC5 — Control Activities | Are security policies implemented as controls across the organization? | Policies exist but controls are inconsistently implemented |
| CC6 — Access Controls | Are access provisioning, deprovisioning, and review processes implemented? | No formal access reviews; privileged accounts not tracked; weak authentication |
| CC7 — System Operations | Is there a security operations capability with incident detection and response? | No SIEM; no IR plan; no tabletop exercises; DR not tested |
| CC8 — Change Management | Are changes to systems controlled, authorized, and tested? | Ad-hoc changes; no change advisory board; no test environment |
| CC9 — Risk Mitigation | Is third-party risk managed? Is cyber insurance in place? | No vendor risk program; no cyber insurance; no BCP |

---

## Preparing the DC-4 Description — Writing Guidance

The management description is the central artifact in a SOC for Cybersecurity engagement.
It must be sufficiently detailed, accurate, and honestly reflect the program as it operates —
not as it is intended to operate.

**Common mistakes in DC-4 descriptions:**
- Describing aspirational or planned controls as if they are in place.
- Omitting significant risk factors (e.g., legacy technology) because they are unflattering.
- Generic language that could apply to any organization (the description must be specific).
- Failing to describe incidents that occurred during the period (DC-4.9 requires disclosure).
- Describing monitoring activities without specifying frequency or scope.

**Structure recommendation:**
Follow the nine DC-4 groups in sequence. Each section should:
1. State what the entity does (factually).
2. Reference specific policies, tools, and processes.
3. Identify the responsible role or team.
4. State the frequency of key activities.

---

## Frequently Asked Questions

**Q: Can any organization get a SOC for Cybersecurity report?**  
Yes. Unlike SOC 1 and SOC 2, which apply specifically to service organizations, SOC for
Cybersecurity can be obtained by any type of entity: manufacturers, financial institutions,
healthcare organizations, government contractors, or any organization that wants board-level
or stakeholder assurance over its cybersecurity program.

**Q: Does SOC for Cybersecurity replace SOC 2?**  
No. SOC for Cybersecurity and SOC 2 address different questions. SOC 2 assesses controls on
a specific service system against TSC; SOC for Cybersecurity assesses the entity's complete
cybersecurity risk management program. Both can coexist and are complementary for service
organizations.

**Q: Is the SOC for Cybersecurity report publicly available?**  
It may be. Unlike SOC 1 and SOC 2, which are restricted-use documents, the SOC for
Cybersecurity report is general use and may be distributed freely. The entity and practitioner
decide the distribution.

**Q: Can the DC-4 description disclose a cybersecurity incident?**  
Yes — and it must, if incidents occurred during the period. DC-4.9 requires that the
description include cybersecurity incidents experienced during the period. The management
description should describe the nature of any incidents, how they were detected, and how
they were managed. The practitioner will evaluate whether the response was consistent with
the entity's stated procedures.

**Q: What does a "pass" look like for SOC for Cybersecurity?**  
The practitioner issues an unmodified opinion stating that: (1) management's description is
presented in accordance with DC-4 criteria, and (2) the controls within the cybersecurity
risk management program were effective throughout the period to achieve the entity's
cybersecurity objectives. There is no point-by-point pass/fail for each DC-4 criterion.

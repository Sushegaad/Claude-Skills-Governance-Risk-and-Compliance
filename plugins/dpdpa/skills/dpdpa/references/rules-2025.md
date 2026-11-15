# DPDP Rules, 2025 - Rule-by-Rule Reference

Digital Personal Data Protection Rules, 2025. Notified: 13 November 2025.
23 Rules total, published as a **flat list - the Rules are not divided into chapters.**

Published by the Ministry of Electronics and Information Technology (MeitY) under
the rule-making power in the Digital Personal Data Protection Act, 2023 (Section 40).

---

## Overview: Rules Structure and Commencement

The Rules are a single flat sequence of 23 rules with Schedules. Commencement is **staggered**:

| Rules | In force from |
|-------|---------------|
| Rules 1, 2, and 17–21 (preliminary, definitions, Board constitution/operations) | 13 November 2025 |
| Rule 4 (Consent Manager registration) | 13 November 2026 |
| All remaining rules (including 3, 5–16, 22, 23) | 13 May 2027 |

| Rule | Subject |
|------|---------|
| 1 | Short title and commencement |
| 2 | Definitions |
| 3 | Notice to Data Principal |
| 4 | Registration and obligations of Consent Managers |
| 5 | Processing by the State for subsidies, benefits, services, etc. |
| 6 | Reasonable security safeguards |
| 7 | Intimation of personal data breach |
| 8 | Time periods for erasure (retention) |
| 9 | Contact person for Data Principal queries |
| 10 | Verifiable consent for processing children's data |
| 11 | Verifiable consent of lawful guardians |
| 12 | Exemptions from certain children's-data obligations |
| 13 | Additional obligations of Significant Data Fiduciaries |
| 14 | Exercise of Data Principal rights |
| 15 | Processing outside India (cross-border transfers) |
| 16 | Exemption for research, archiving, and statistical purposes |
| 17–21 | Data Protection Board - constitution, appointments, and operations |
| 22 | Appeal to the Appellate Tribunal (TDSAT) |
| 23 | Power to call for information |

---

## Rule 1 - Short Title and Commencement

These Rules are called the Digital Personal Data Protection Rules, 2025. Rules 1, 2, and
17–21 came into force on publication (13 November 2025); Rule 4 comes into force on
13 November 2026; the remaining rules come into force on 13 May 2027.

> **Practical note:** During the transition, organisations should treat the Rules as
> operative for planning and system design - implementing compliance programmes so they
> are ready by 13 May 2027 (notice redesign, consent infrastructure, age-gate systems
> for children's data, breach intimation pipelines).

---

## Rule 2 - Definitions

Terms used in the Rules carry the meanings assigned in the Act (Section 2), with
supplementary definitions set out in the Rule itself. Consult the gazetted text for the
exact definitional entries; do not rely on paraphrases for definitional disputes.

---

## Rule 3 - Notice to Data Principal

**Source authority:** Section 5 of the Act.

The notice given by a Data Fiduciary must:
- Be understandable independently of any other information (standalone presentation)
- Be in clear and plain language
- Contain an itemised description of the personal data and the specified purposes
- Describe how the Data Principal can exercise rights, withdraw consent, and complain to the Board

**Common gap:** Notices buried in terms and conditions, generic purpose statements, and
missing Board complaint pathways do not meet Rule 3.

---

## Rule 4 - Registration and Obligations of Consent Managers

**Source authority:** Sections 6(7)–(9) of the Act. **In force from 13 November 2026.**

- Consent Managers must be registered with the Data Protection Board before operating
- Registration conditions (including incorporation in India and net-worth and capacity
  criteria) are set out in the First Schedule to the Rules
- Consent Managers enable Data Principals to give, manage, review, and withdraw consent
  across Data Fiduciaries through an interoperable platform

---

## Rule 5 - Processing by the State

Conditions and standards applicable where the State and its instrumentalities process
personal data to provide subsidies, benefits, services, certificates, licences, or
permits (the Section 7(b) legitimate use), as detailed in the Rules' Schedule.

---

## Rule 6 - Reasonable Security Safeguards

**Source authority:** Section 8(5) of the Act.

Rule 6 is **technology-neutral**. It requires reasonable security safeguards including,
at minimum:

- Securing personal data through measures such as **encryption, obfuscation, masking, or
  the use of virtual tokens**
- Appropriate control of access to the systems used to process personal data
- Visibility through **logs and monitoring** to detect, investigate, and remediate
  unauthorised access
- Retention of **logs and relevant personal data for one year** to enable breach
  detection and investigation (unless another law requires otherwise)
- Contractual provisions requiring Data Processors to maintain equivalent safeguards
- Technical and organisational measures to ensure continued processing in the event of
  compromise (such as backups)

> **Important:** Rule 6 does **not** prescribe specific technologies, protocol versions,
> cipher standards, or patch windows. Any mapping to specific controls (TLS versions,
> AES key lengths, patch SLAs) is an implementation choice, not a Rule 6 requirement.

**Penalty linkage:** Failure to take reasonable security safeguards (Section 8(5)) carries
the highest Schedule penalty: up to ₹250 crore.

---

## Rule 7 - Intimation of Personal Data Breach

**Source authority:** Section 8(6) of the Act.

On becoming aware of a personal data breach, the Data Fiduciary must:

1. **Intimate each affected Data Principal directly, without delay** - in clear and plain
   language, through their user account or registered mode of communication - describing
   the breach, its likely consequences, the measures being taken, safety measures the
   Data Principal may take, and contact details of a person able to respond to queries
2. **Intimate the Board without delay** - an initial description of the breach
3. **Provide the Board a detailed report within 72 hours** of becoming aware (or a longer
   period the Board allows on request), covering updated and detailed breach information,
   circumstances and reasons, mitigation measures, findings about the person who caused
   the breach, remedial measures, and the report of intimations given to Data Principals

**Key operational points:**
- Data Principal intimation is a **direct obligation of the Data Fiduciary** - it is not
  contingent on a Board direction
- There is no risk-of-harm threshold: breaches must be intimated
- The 72-hour clock applies to the detailed Board report and is extendable on request

**Penalty linkage:** Failure to give notice of a personal data breach carries up to
₹200 crore under the Schedule.

---

## Rule 8 - Time Periods for Erasure (Retention)

**Source authority:** Section 8(7) of the Act.

Rule 8 specifies the time periods after which personal data must be erased for specified
classes of Data Fiduciaries and purposes (set out in the Rules' Schedule), where the Data
Principal has not engaged with the Fiduciary for the specified purpose. Data Fiduciaries
should maintain a documented retention schedule mapping each data category to its erasure
trigger and verify applicable periods against the gazetted Schedule.

---

## Rule 9 - Contact Person

Data Fiduciaries must prominently publish the business contact information of a person
able to answer Data Principal questions about the processing of their personal data (the
Data Protection Officer, where applicable).

---

## Rule 10 - Verifiable Consent for Children's Data

**Source authority:** Section 9(1) of the Act.

Data Fiduciaries must adopt appropriate technical and organisational measures to obtain
**verifiable consent of a parent** before processing a child's personal data, ensuring
that the person identifying as the parent is an **identifiable adult**, using details of
identity and age available with the Fiduciary or voluntarily provided identity details,
or a **virtual token** mapped to identity and age (including tokens issued via Digital
Locker service providers).

**Practical methods:**
- Reliance on identity/age details already held by the Data Fiduciary
- Voluntarily provided identity details verified against government-issued credentials
- Virtual tokens issued by entities entrusted by law or government (including DigiLocker)

---

## Rule 11 - Verifiable Consent of Lawful Guardians

Equivalent verifiable-consent measures where consent is given by a **lawful guardian**
(including for persons with disabilities who have a lawful guardian), ensuring the
guardian's identity and authority are verified.

---

## Rule 12 - Exemptions for Certain Children's-Data Processing

**Source authority:** Section 9 of the Act.

Specified classes of Data Fiduciaries (such as healthcare, educational, and childcare
contexts set out in the Rules' Schedule) are exempt from certain Section 9 obligations,
to the extent and subject to the conditions specified. Exemptions must be narrowly
construed; where doubt exists, apply the full Section 9 standard.

---

## Rule 13 - Significant Data Fiduciaries: Additional Obligations

**Source authority:** Section 10 of the Act.

Additional obligations for notified SDFs include:
- Periodic **Data Protection Impact Assessment** and **audit**, with significant
  observations reported to the Board
- Due diligence to verify that algorithmic software used does not pose a risk to the
  rights of Data Principals
- **Localisation-style measures enter only through this rule:** an SDF must ensure that
  specified personal data (and traffic data related to its flow) identified by the
  Central Government **by notification** is not transferred outside India. No such
  notification has issued as of the last verification date; there is no general
  localisation mandate in the Act or Rules absent that notification.

---

## Rule 14 - Exercise of Data Principal Rights

**Source authority:** Sections 11–14 of the Act.

Data Fiduciaries and Consent Managers must publish the means by which Data Principals can
exercise their rights, the particulars required to identify requests, and the time periods
within which grievances will be addressed. Verify specific published periods against each
Fiduciary's stated mechanism and the gazetted text.

---

## Rule 15 - Processing Outside India (Cross-Border Transfers)

**Source authority:** Section 16 of the Act.

Transfers of personal data outside India are subject to any requirements the Central
Government specifies by order, including requirements concerning making personal data
available to foreign states or their agencies. The Act's blacklist mechanism (Section 16)
otherwise permits transfer to any country not notified as restricted; no countries have
been notified as restricted as of the last verification date.

---

## Rule 16 - Research, Archiving, and Statistics Exemption

**Source authority:** Section 17(2)(b) of the Act.

Processing necessary for **research, archiving, or statistical purposes** is exempt from
specified provisions of the Act where it is carried out in accordance with the standards
set out in the Rules' Schedule and is not used to take decisions specific to a Data
Principal.

> **Correction note:** Rule 16 is the research/archiving/statistics exemption. There is
> **no rule on Data Processing Agreements** in the DPDP Rules 2025; processor contracts
> are governed by Section 8(2) of the Act.

---

## Rules 17–21 - Data Protection Board: Constitution and Operations

**In force from 13 November 2025.**

These rules cover the constitution and functioning of the Data Protection Board of India,
including appointment of the Chairperson and Members (search-cum-selection process), their
terms and conditions of service, and the Board's functioning as a digital office with
techno-legal procedures.

---

## Rule 22 - Appeal to the Appellate Tribunal

**Source authority:** Section 29 of the Act.

Appeals against Board orders lie to the **Telecom Disputes Settlement and Appellate
Tribunal (TDSAT)**, filed digitally, with fees and procedure as specified.

---

## Rule 23 - Power to Call for Information

The Central Government may call for information from Data Fiduciaries and intermediaries
for purposes specified in the Rules' Schedule, within the time periods specified.

---

## Summary: Key Implementation Timelines

| Milestone | Date |
|-----------|------|
| Rules notified; Rules 1, 2, 17–21 in force (Board constitution/operations) | 13 November 2025 |
| Rule 4 in force (Consent Manager registration) | 13 November 2026 |
| Remaining rules in force; full compliance deadline | 13 May 2027 |

> **Monitoring requirement:** Several provisions reference Schedules, notified classes,
> and time periods specified by notification. These are published via MeitY's Official
> Gazette and the Board's website. Organisations should maintain a monitoring programme
> for supplementary notifications throughout the transition period.

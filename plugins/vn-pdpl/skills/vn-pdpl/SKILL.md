---
name: vn-pdpl
description: "Expert Vietnam Personal Data Protection Law (PDPL) compliance advisor for Law No. 91/2025/QH15 and implementing Decree 356/2025/ND-CP (effective January 1, 2026). Use this skill for gap analysis against the Vietnam PDPL, data subject rights fulfilment workflows, cross-border data transfer impact assessments, privacy notices and internal policies, breach notification procedures, sector-specific obligations (finance, AI, cloud, blockchain), and DPO qualification reviews. Trigger whenever a user mentions Vietnam data privacy, VN-PDPL, Nghị định 356, Vietnamese personal data, or cross-border transfers involving Vietnamese citizens' data."
---

# Vietnam Personal Data Protection Law (PDPL) Skill

> **Last verified:** 2026-09-05

## Overview

You are an expert advisor on Vietnam's **Law on Personal Data Protection No. 91/2025/QH15** (passed 26 June 2025, effective **1 January 2026**) and its implementing regulation **Decree 356/2025/ND-CP** (31 December 2025). This is Vietnam's first comprehensive personal data protection law, administered by the **Ministry of Public Security** (specialized agency for personal data protection).

The law applies to:
- Vietnamese organisations and individuals processing personal data in Vietnam
- Foreign organisations and individuals processing data of Vietnamese data subjects (extraterritorial reach)

**Always read the relevant reference file before drafting detailed guidance:**
- `references/articles-overview.md` — law structure, definitions, data categories, rights, obligations, penalties
- `references/decree-356-implementation.md` — sector rules, consent methods, DPO qualifications, response timeframes

---

## Core Concepts

### Data Categories

**Basic personal data (11 items):** full name, date/place of birth and death, gender, current and permanent address, nationality, personal image, phone number, ID/passport/license plate numbers, marital status, family relationships, digital account information.

**Sensitive personal data (13 items):** racial/ethnic origin, political views, religious/philosophical views, private life/personal secrets/family secrets, health and medical status, biometric and genetic data, sexual life and orientation, criminal records/convictions, location and movement data, electronic account credentials and ID card images, banking/financial/credit/transaction data, social media behavioural tracking data. **Sensitive data requires explicit, separate consent.**

### Key Roles

| Role | Definition |
|---|---|
| **Data Subject** | The individual identified by the data |
| **Personal Data Controller** | Decides purpose and means of processing |
| **Personal Data Processor** | Processes data at the controller's request |
| **Controlling-and-Processing Party** | Decides purpose AND directly processes |
| **Third Party** | Any other participant in processing |

### Data Subject Rights (6 rights — Article 4)

1. **Right to be informed** about processing activities
2. **Right to consent / withdraw consent** — granular, per-purpose; silence ≠ consent
3. **Right to access and rectify** their personal data
4. **Right to delete, restrict, object** to processing
5. **Right to file complaints, lawsuits, and seek compensation**
6. **Right to request protection measures** from competent authorities

### Key Deadlines

| Obligation | Timeline |
|---|---|
| Respond to data subject request (acknowledgement) | 2 working days |
| Fulfil access/correction requests | 10 working days |
| Fulfil deletion requests | 20 working days |
| Fulfil withdrawal/restriction requests | 15 working days |
| Breach notification to authority | **72 hours** |
| Submit cross-border transfer impact assessment | Within 60 days of first transfer |
| Update cross-border impact assessment | Every 6 months or on material changes |
| Submit domestic DPIA | Within 60 days of first processing (Article 21) |
| SME exemption period (Articles 21, 22, 33(2)) | 5 years from effective date |

---

## Skill Workflows

### Workflow 1 — Compliance Gap Analysis

**When to use:** Organisation wants to assess readiness against VN-PDPL.

**Steps:**
1. Identify the organisation's role (controller / processor / both) and sectors.
2. Map data inventory: what personal data is collected, categories (basic vs sensitive), purposes, legal bases.
3. Check consent mechanisms against Article 9 requirements (voluntary, explicit, specific, per-purpose; record-keeping).
4. Assess data subject rights response procedures and timelines (Decree 356 Article 5).
5. Review cross-border transfer flows — Article 20 impact assessment obligations.
6. Review DPIA (Article 21) obligations — note SME exemptions.
7. Assess data security measures and breach notification readiness (72-hour rule).
8. Check DPO appointment requirement and qualifications (Decree 356 Article 13).
9. Produce a prioritised gap register with remediation owners and timelines.

**Output format:**
```
## VN-PDPL Gap Analysis — [Organisation Name]
### Executive Summary
### Gap Register
| Control Area | Current State | Gap | Risk | Remediation |
### Priority Actions
### SME Exemptions Applicable (if any)
```

### Workflow 2 — Data Subject Rights Fulfilment

**When to use:** Handling data subject requests or building a rights fulfilment process.

**Steps:**
1. Identify the right being exercised (one of 6 from Article 4).
2. Verify identity of the requestor.
3. Confirm the applicable response deadline from Decree 356 Article 5.
4. Check whether any Article 19 processing-without-consent exception applies.
5. Draft acknowledgement (within 2 working days) and fulfilment response.
6. Document the request and response for audit trail.

**Key rule:** Consent withdrawal must be honoured; it does not affect the lawfulness of prior processing.

### Workflow 3 — Impact Assessments (DPIA & Cross-Border Transfer)

**When to use:** Starting new processing activities or planning to transfer data outside Vietnam.

**Domestic DPIA (Article 21):**
- Mandatory within 60 days of first processing
- SMEs (small and micro) exempt for 5 years unless processing sensitive data or at large scale
- Must include: data categories, purpose, retention period, security measures, risk assessment

**Cross-Border Transfer Impact Assessment (Article 20):**
- Submit dossier to Ministry of Public Security within 60 days of first transfer
- Update every 6 months or on: change in purpose, data types, recipient, or security measures
- Ministry may suspend transfer if national/public security risk identified
- Exceptions: state agencies exercising statutory functions; employee HR data in cloud storage; data subject initiating own transfer

**Output:** Provide a structured impact assessment template pre-filled with client's specific facts.

### Workflow 4 — Privacy Notices and Internal Policies

**When to use:** Drafting or reviewing privacy notices, consent forms, data processing policies.

**Privacy Notice must include:**
- Identity and contact details of controller/processor
- Purposes and legal basis for each processing activity
- Categories of data processed (basic vs sensitive — note separately)
- Recipients and third parties
- Cross-border transfer details (if any)
- Retention periods
- Data subject rights and how to exercise them
- Breach notification procedures
- DPO contact (if appointed)

**Consent form rules (Decree 356 Article 6):** Consent may be given in writing, recorded telephone call, SMS syntax, email, website/app form, or other verifiable electronic format. **Silence, pre-ticked boxes, and inaction do not constitute consent.**

**Sector-specific overlays:** Read `references/decree-356-implementation.md` for finance/banking, AI, cloud, blockchain, and big data requirements.

### Workflow 5 — Breach Notification and Response

**When to use:** A personal data breach has occurred or is suspected.

**Response sequence:**
1. Contain — isolate affected systems, prevent further exposure.
2. Assess — determine scope, data categories affected (sensitive vs basic), number of data subjects.
3. Notify authority — within **72 hours** of becoming aware; notify data subjects simultaneously or as soon as practicable.
4. Document — maintain an internal breach register.
5. Remediate — patch root cause, update controls.
6. Review — post-incident lessons learned and control improvements.

**Breach notification content:**
- Nature of the breach
- Categories and approximate number of data subjects affected
- Categories and approximate number of records affected
- Contact details of DPO or responsible officer
- Likely consequences of the breach
- Measures taken or proposed to address the breach

---

## Penalties — Decree 330/2026/ND-CP (effective August 19, 2026)

**The sanctions regime is now operative.** Decree No. 330/2026/ND-CP (issued and effective **August 19, 2026**; 82 articles, 33 on personal data protection) implements the penalty framework of Law 91/2025 (Article 8) and Decree 356/2025. State this decree in every penalties answer.

| Violation | Penalty (organisations; individuals = half) |
|---|---|
| Serious cross-border violations — CPDTIA failure/concealment/misdeclaration with breach or loss of citizens' data | **% of prior-year Vietnam-market revenue**: 1–2% (10k–<100k data subjects), 2–3% (100k–<1M), **3–5% (≥1M subjects or national defence/security impact)**. Where no Vietnam revenue or the % is below the fixed tier: VND 200–500M / 500M–1B / **1–3B** respectively |
| Unlawful data trading (Art. 53) | **2×–10× unlawful proceeds**; where indeterminable: VND 500M–1B (basic data ≥10k people or sensitive data ≥2k), **VND 1–3B** where seriously affecting national security, public order, macroeconomy, or life/health/dignity |
| Plain CPDTIA non-filing / late updates | VND 30–50M |
| Consent violations | VND 30–50M; silence-as-consent or processing after withdrawal: VND 50–70M |
| PDPIA falsification / non-cooperation | VND 50–100M |
| DPO / appointment failures | VND 10–30M |

**Remedial measures** beyond fines: suspension of processing or cross-border transfers, compulsory data destruction, disgorgement of unlawful proceeds, confiscation. **Transition:** pre-Aug 19, 2026 conduct is judged under the law in force at the time unless Decree 330 is more lenient. The compliance stack: **Law 91/2025** (substance) + **Decree 356/2025** (PDPIA/CTIA dossiers, 60-day A05 submission, 6-monthly updates) + **Decree 330/2026** (penalties).

---

## SME Exemptions

Small and micro enterprises may opt out of Articles 21 (DPIA), 22 (security measures requirements), and 33(2) (certain processor obligations) for **5 years** from 1 January 2026, **unless** they process sensitive personal data or process data at large scale. Micro-enterprises are fully exempt from these articles unless they process sensitive data or at large scale.

---

## Relationship to Other Laws

- **Cybersecurity Law 2018 (Law 24/2018/QH14):** VN-PDPL is lex specialis for personal data; Cybersecurity Law continues to apply for broader data localisation and system security obligations.
- **Consumer Protection Law:** Data subject rights under VN-PDPL are in addition to consumer rights.
- **Labour Code:** Employee personal data processing is subject to VN-PDPL; Decree 356 Article 8 covers finance/banking sector-specific employer obligations.
- **GDPR comparison:** VN-PDPL is broadly GDPR-inspired. Key differences: 6 rights vs GDPR's 8; 72-hour breach notification applies to both authority AND data subjects; cross-border transfer mechanism is impact assessment (not adequacy/SCCs); no data portability right; SME exemptions are time-bound.

---

> *This skill provides general compliance information, not legal advice. Verify current requirements against official sources; consult qualified counsel or an accredited assessor for decisions.*

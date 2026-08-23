# India Digital Personal Data Protection Act (DPDPA) Skill for Claude

> **Disclaimer:** This skill provides informational guidance based on the Digital Personal Data
> Protection Act, 2023 and the Digital Personal Data Protection Rules, 2025. It does not
> constitute legal advice. For matters involving significant compliance risk, Data Protection Board
> proceedings, or complex cross-border scenarios, consult a qualified Indian data protection lawyer
> or your Data Protection Officer. Guidance on items pending Central Government notification
> (SDF designation, restricted transfer countries, prescribed timelines) is explicitly flagged
> as provisional.

---

## 1. What Does the Skill Do?

This skill gives Claude deep expertise in India's **Digital Personal Data Protection Act, 2023**
(DPDPA) — passed by Parliament on 11 August 2023 — and the **Digital Personal Data Protection
Rules, 2025**, notified by the Ministry of Electronics and Information Technology (MeitY) on
13 November 2025. The full compliance deadline is **13 May 2027** (18 months from Rules
notification), with the Data Protection Board of India (DPBI) operational from November 2025.

The skill covers every chapter of the Act and all 23 Rules: the two-lawful-basis framework
(consent under Section 6 and the eight enumerated Legitimate Uses under Section 7), Data
Fiduciary obligations across Sections 4–10 (notice requirements, security safeguards, breach
notification, data erasure, and children's data protections), Data Principal rights under
Sections 11–15, cross-border transfer rules under Section 16, Significant Data Fiduciary (SDF)
additional obligations under Section 10 and Rule 13, and the Data Protection Board's adjudicatory
powers and the full penalty schedule under Section 33.

The skill uses precise DPDPA terminology throughout — Data Fiduciary, Data Principal, Data
Processor, Significant Data Fiduciary, Data Protection Board — mapping these to GDPR equivalents
once when useful, then maintaining DPDPA language. Every obligation is cited to its governing
Section or Rule (e.g., "Notice must be provided per Section 5 and Rule 3 of the DPDP Rules 2025").
Items pending Central Government notification — including SDF designations, restricted countries
list under Section 16, startup exemptions, and prescribed response timelines — are always flagged
as provisional.

The skill is equally valuable for Indian organisations building compliance programmes and for
global companies that process personal data of individuals located in India, which triggers
extra-territorial application under Section 3. It produces structured gap analysis tables,
standalone notice drafts meeting all Rule 3 requirements, Data Processing Agreement reviews
against Rule 16, breach notification step-by-step procedures against the 72-hour Board timeline,
SDF self-assessment checklists, GDPR vs DPDPA side-by-side comparisons, and children's data
compliance reviews under Section 9 and Rules 10 and 12.

---

## 2. Intended Audiences

| Role | How They Use the Skill |
|------|----------------------|
| Privacy & DPO Teams | Gap analysis, notice drafting, consent mechanism review, breach notification SOPs |
| Legal Counsel | Section/Rule citations for legal opinions, GDPR vs DPDPA comparison, Board complaint process |
| Compliance Managers | End-to-end compliance roadmap, penalty risk assessment, processing register mapping |
| Technology & Product Teams | Consent UI/UX review, children's age-gate requirements, data erasure workflows |
| CISOs & Security Teams | Section 8(3)/Rule 7 security safeguard requirements, breach notification 72-hour process |
| Global/Multinational Organisations | Extra-territorial scope analysis (Section 3), cross-border transfer guidance (Section 16) |
| Vendors & Data Processors | Rule 16 contract requirements, sub-processor obligations |
| Startups & SMEs | Scoping analysis, startup exemption monitoring, proportionate compliance roadmap |

---

## 3. Common Use Cases

### Gap Analysis and Readiness

- "Perform a DPDPA gap analysis for our SaaS platform serving Indian users."
- "We have GDPR compliance in place. What additional steps are needed for DPDPA?"
- "Which sections of the DPDPA apply to our company based in Singapore with Indian customers?"
- "What evidence do we need to demonstrate Section 8(3) security safeguard compliance?"
- "Map our data processing activities to DPDPA lawful bases — we've been using legitimate interests."

### Notice and Consent

- "Draft a standalone data collection notice meeting all Rule 3 requirements for our mobile app."
- "Review our current privacy policy for DPDPA compliance gaps."
- "Our consent is bundled with our Terms of Service. Is this valid under Section 6?"
- "How do we implement a consent withdrawal mechanism that satisfies Section 6(4)?"
- "What are the pre-ticked box and dark pattern prohibitions under the DPDPA?"

### Children's Data (Section 9)

- "What age verification methods are acceptable under Rule 12 for our platform?"
- "We run targeted advertising — what changes are required for child users under Section 9?"
- "Does our use of session analytics on child accounts violate Section 9(2)?"
- "Draft a verifiable parental consent workflow using DigiLocker."

### Breach Notification

- "Walk me through the 72-hour breach notification process to the Data Protection Board."
- "Draft a breach notification template for both the Board (Rule 6) and Data Principals."
- "What constitutes a 'personal data breach' under the DPDPA and when must we notify?"

### Significant Data Fiduciaries

- "Are we likely to be designated an SDF? What criteria apply under Section 10?"
- "What additional obligations apply to SDFs under Section 10 and Rule 13?"
- "Our DPO is based in the UK — does this satisfy Section 10's India-resident requirement?"
- "What must an annual Data Protection Impact Assessment cover for an SDF?"

### Cross-Border Data Transfers

- "Can we transfer Indian user data to our data centres in Ireland under Section 16?"
- "What is the difference between DPDPA's blacklist approach and GDPR's whitelist approach?"
- "How do we prepare for future restricted-country notifications under Section 16?"

### Data Principal Rights

- "What rights do Data Principals have under the DPDPA and within what timeframes?"
- "Draft a rights request handling procedure covering Sections 11–14."
- "Can we refuse an erasure request under Section 12? Under what circumstances?"
- "What is the nomination right under Section 14 and how do we operationalise it?"

### Vendor and Processor Management

- "Review our standard vendor agreement for DPDPA compliance against Rule 16."
- "What mandatory terms must Data Processing Agreements include under Rule 16?"

---

## 4. How to Use the Skill

### Installation

1. Download `dpdpa.skill` from this folder.
2. In Claude, go to **Settings → Skills**.
3. Click **Upload Skill** and select `dpdpa.skill`.
4. The skill is now active across your Claude sessions.

### Triggering the Skill

The skill activates automatically when DPDPA-related topics arise. No special command is needed.
Example phrases that trigger it:

- *"DPDPA gap analysis"* or *"India data privacy compliance"*
- *"Data Fiduciary obligations"* or *"Data Principal rights"*
- *"Section 6 consent"*, *"Section 9 children's data"*, *"Section 10 SDF"*
- *"Rule 6 breach notification"*, *"Rule 13 SDF obligations"*, *"Rule 16 DPA terms"*
- *"Data Protection Board complaint"*, *"DPDP Rules 2025"*
- *"verifiable parental consent India"*, *"DPDPA vs GDPR"*
- *"India privacy law"*, *"MeitY data protection"*, *"cross-border transfer India"*

### Example Prompts

```
Perform a DPDPA gap analysis for our B2C e-commerce platform with 2 million Indian users.
We currently rely on GDPR consent mechanisms. Produce a gap table covering all Data Fiduciary
obligations under Chapter II.
```

```
Draft a standalone data collection notice for our mobile app under Section 5 and Rule 3.
We collect: name, email, phone number, location, and purchase history. We share data with
payment processors and logistics partners. Include all mandatory Rule 3 elements.
```

```
We've had a security incident. 50,000 customer records including payment data were exposed.
Walk me through our obligations under Section 8(6) and Rule 6, including the 72-hour
Board notification timeline and Data Principal notification requirements.
```

```
Compare the DPDPA and GDPR across the following dimensions: lawful bases, data subject/principal
rights, cross-border transfer mechanisms, enforcement body powers, and penalty levels.
Produce a side-by-side table for our global privacy team.
```

```
We run an educational platform for children under 18 in India. Review our current practices
against Section 9 and Rules 10 and 12. We use session analytics, recommend content, and
serve advertisements. Identify all compliance gaps.
```

---

## 5. Skill Implementation Details

### Architecture

```
dpdpa/
├── SKILL.md                          # Core skill — DPDPA expertise, response formats,
│                                     #   all Chapter II-VIII obligations, penalty schedule
└── references/
    ├── sections-reference.md         # All 44 sections of the Act with obligation summaries
    ├── rights-and-obligations.md     # Deep-dive: Data Fiduciary obligations, Data Principal
    │                                 #   rights, children's data, breach notification, Rule 16
    ├── rules-2025.md                 # DPDP Rules 2025 rule-by-rule guide (Rules 1–23)
    │                                 #   with operational requirements
    └── gdpr-comparison.md            # DPDPA vs GDPR: 8 substantive differences for
                                      #   compliance teams transitioning from GDPR
```

### What's in SKILL.md

- **Identity and scope**: Expert India DPDPA compliance advisor persona covering the Act (2023) and Rules (2025)
- **Foundational rules**: 7 rules governing every response — digital-only scope, two lawful bases only, DPDPA terminology, section/rule citations, Act vs Rules distinction, phase-aware guidance, unnotified items flagging
- **Response format table**: Output format for each task type (gap analysis, notice drafting, rights handling, breach notification, GDPR comparison, etc.)
- **DPDPA at a Glance**: Key dates, enforcement body, Chapter-by-Chapter structure
- **Chapter II deep-dive**: Sections 4–10 — all Data Fiduciary obligations with specific requirements
- **Chapter III**: Sections 11–15 — Data Principal rights and duties
- **Chapter IV**: Sections 16–17 — cross-border transfers and exemptions
- **Chapter V**: Board powers, limitations, and complaint process
- **Penalty schedule**: Section 33 and Schedule — penalty amounts for all violation categories
- **Gap analysis templates**: Three gap tables (all Data Fiduciaries, children's data, SDFs)
- **Reference file pointers**: When and which reference files to load

### What's in the reference files

| File | Contents |
|------|----------|
| `sections-reference.md` | All 44 Act sections annotated with obligation summaries, applicability notes, and cross-references to Rules |
| `rights-and-obligations.md` | Extended treatment of Data Fiduciary obligations (Sec. 4–10), Data Principal rights (Sec. 11–15), children's data (Sec. 9/Rules 10, 12), breach notification procedures (Sec. 8(6)/Rule 6), and Data Processing Agreement mandatory terms (Rule 16) |
| `rules-2025.md` | Rule-by-rule guide to all 23 DPDP Rules 2025: Rule 3 notice requirements, Rule 6 breach notification, Rule 7 security safeguards, Rule 10 age verification, Rule 12 parental consent methods, Rule 13 SDF obligations, Rule 16 processor contracts, Rule 17 grievance mechanism |
| `gdpr-comparison.md` | Eight substantive DPDPA vs GDPR differences: lawful bases, consent standard, cross-border transfer mechanism, enforcement body model, penalty structure, children's data approach, data subject/principal duties, territorial scope |

### Inputs used to build the skill

| Source | Description |
|--------|-------------|
| Digital Personal Data Protection Act, 2023 | Full text — all 44 sections across 8 Chapters |
| Digital Personal Data Protection Rules, 2025 | All 23 Rules notified 13 November 2025 by MeitY |
| Ministry of Electronics and Information Technology (MeitY) guidance | Official circulars and regulatory context |
| GDPR (EU) 2016/679 | For comparative analysis and transition guidance |
| Data Protection Board of India framework | Board structure, complaint process, penalty determination factors |

### Skill trigger phrases

`DPDPA`, `DPDP Act`, `DPDP Rules 2025`, `India data privacy`, `India personal data protection`,
`Data Fiduciary`, `Data Principal`, `Significant Data Fiduciary`, `Data Protection Board of India`,
`Section 6 consent`, `Section 7 legitimate uses`, `Section 9 children's data`, `Section 10 SDF`,
`Section 16 cross-border`, `Rule 6 breach notification`, `Rule 13 SDF obligations`,
`Rule 16 processor contract`, `verifiable parental consent India`, `DPDPA gap analysis`,
`DPDPA vs GDPR`, `India privacy law global company`, `MeitY data protection`,
`13 May 2027 compliance`, `72-hour breach notification India`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.8.0 — August 2026

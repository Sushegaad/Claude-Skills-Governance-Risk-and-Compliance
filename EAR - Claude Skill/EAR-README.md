# Export Administration Regulations (EAR) Skill for Claude

> **Disclaimer:** This skill provides informational guidance based on 15 CFR Parts 730–774
> administered by the U.S. Department of Commerce, Bureau of Industry and Security (BIS). It
> does not constitute legal advice or a formal export control classification. ECCN determinations,
> license requirement analyses, and restricted party screening decisions with material compliance
> consequences should be reviewed by a qualified export control attorney or licensed export
> compliance professional. This skill does not address ITAR (22 CFR Parts 120–130) — if your
> item may be subject to ITAR, submit a Commodity Jurisdiction (CJ) request to DDTC.

---

## 1. What Does the Skill Do?

This skill gives Claude comprehensive expertise in the **Export Administration Regulations (EAR)**
— 15 CFR Parts 730–774 — administered by the U.S. Department of Commerce, Bureau of Industry
and Security (BIS) under the authority of the Export Control Reform Act of 2018 (ECRA, 50 U.S.C.
§ 4801 et seq.). The EAR governs the export, reexport, and in-country transfer of dual-use
items: commodities, software, and technology not exclusively controlled by another U.S. agency.

The skill implements the full eight-step EAR compliance workflow: jurisdiction determination
(EAR vs. ITAR Order of Review), ECCN classification across all 10 CCL categories (0–9) and
5 product groups (A–E), license requirement analysis via the Commerce Country Chart in Part 738,
license exception evaluation across all 14 exceptions (LVS, GBS, CIV, TMP, RPL, GOV, TSU, ENC,
TSR, APP, BAG, AVS, ACE, GFT), end-user and end-use controls under Part 744 including all five
restricted party lists, the Foreign Direct Product Rule (FDPR) under § 736.2(b)(3), deemed
export rules under § 734.13, de minimis thresholds under § 734.4, SNAP-R license applications
under Part 748, recordkeeping under Part 762, and Export Compliance Program (ECP) design covering
all seven elements of an effective programme.

Every response cites the specific Part and Section (e.g., "§ 740.17," "15 CFR § 736.2(b)(1)").
The skill distinguishes precisely between "export," "reexport," and "transfer (in-country)"
per §§ 734.14–734.16, and applies the correct Order of Review before any classification analysis.
It covers the full enforcement regime under Part 764 including civil and criminal penalties,
voluntary self-disclosure (VSD) procedures, and penalty mitigation factors.

The skill is built for exporters, manufacturers, technology companies, universities and research
institutions, freight forwarders, and compliance professionals who need structured classification
analysis, restricted party screening guidance, license exception applicability reviews, FDPR
impact assessments, and ECP gap analysis — all with precise regulatory citations.

---

## 2. Intended Audiences

| Role | How They Use the Skill |
|------|----------------------|
| Export Control Managers | ECCN classification, license requirement analysis, ECP gap reviews, VSD preparation |
| Trade Compliance Teams | Restricted party screening guidance, transaction red flag review, Country Chart analysis |
| Legal Counsel | Regulatory citations for legal opinions, FDPR scope analysis, penalty exposure assessment |
| Technology Companies | Deemed export analysis for foreign national employees, software/technology ECCN classification |
| Semiconductor & Defence Manufacturers | Advanced chip FDPR (Entity List FDPR), Category 3 classification, CCL 0-9 analysis |
| University Research Offices | Fundamental research exclusion, deemed export compliance, publication controls |
| Freight Forwarders & Logistics | EEI filing obligations (Part 758), licence documentation, shipper's letter of instruction |
| Compliance Auditors | 7-element ECP assessment, recordkeeping audit (Part 762), training programme review |

---

## 3. Common Use Cases

### ECCN Classification

- "Classify this network security appliance with AES-256 encryption — what is its ECCN?"
- "Is our machine learning accelerator chip classified under 3A090 or another ECCN?"
- "We export biological reagents. Which CCL Category 1 ECCNs might apply?"
- "Our software performs signal processing. Walk me through classifying it under CCL Category 5."
- "This item isn't on the CCL. Can we confirm it's EAR99 and what restrictions still apply?"

### Jurisdiction Determination (EAR vs. ITAR)

- "Is this satellite component subject to EAR or ITAR? How do I apply the Order of Review?"
- "Our product was designed from a USML item that was CJ'd to EAR. What's our classification?"
- "When should I submit a CCATS request to BIS versus a CJ request to DDTC?"

### License Requirement Analysis

- "We're exporting 3A001 electronics to China. What does the Country Chart say and do we need a licence?"
- "Can we use licence exception ENC for our encryption software export to Russia under current E:2 controls?"
- "What licence exceptions are available for NS-controlled items going to Country Group D:1?"
- "Does licence exception TMP cover our equipment being sent for a trade show in India?"
- "Walk me through the Country Chart check for a 5E002 technology export to UAE."

### Restricted Party Screening

- "Our customer appears on the Entity List. What licence requirements apply and are any exceptions available?"
- "What is the difference between the Denied Persons List, Entity List, and Unverified List?"
- "How do we handle a transaction where an intermediate consignee appears on the MEU List?"
- "Describe the red flag indicators under § 732.6 we should train our sales team on."
- "How do we conduct compliant end-use checks and when must we obtain an end-use certificate?"

### Foreign Direct Product Rule (FDPR)

- "Does the Entity List FDPR apply to our foreign-made chips if they were fabricated using US equipment?"
- "We produce semiconductors outside the US using US-origin EDA software. Does the General FDPR apply?"
- "Explain the 2022 advanced computing FDPR and how it affects our product line for China."

### Deemed Exports

- "We're hiring an engineer from China to work on our 3E001 technology. Do we need a deemed export licence?"
- "What counts as 'releasing' technology to a foreign national under § 734.13?"
- "How does deemed reexport differ from deemed export and when does it apply?"

### Export Compliance Programme

- "Review our ECP against the seven-element framework. We have a written policy but no training records."
- "Draft a restricted party screening policy for our procurement team."
- "We've discovered a potential violation. Walk us through the voluntary self-disclosure (VSD) process."
- "What records must we retain under Part 762 and for how long?"

---

## 4. How to Use the Skill

### Installation

1. Download `ear.skill` from this folder.
2. In Claude, go to **Settings → Skills**.
3. Click **Upload Skill** and select `ear.skill`.
4. The skill is now active across your Claude sessions.

### Triggering the Skill

The skill activates automatically when EAR-related topics arise. No special command is needed.
Example phrases that trigger it:

- *"ECCN classification"* or *"Commerce Control List"*
- *"EAR99 determination"* or *"dual-use export"*
- *"BIS licence"*, *"licence exception ENC"*, *"SNAP-R application"*
- *"Entity List"*, *"denied party screening"*, *"Unverified List"*
- *"Foreign Direct Product Rule"* or *"deemed export"*
- *"15 CFR Part 740"*, *"Country Chart"*, *"Order of Review"*
- *"export compliance programme"*, *"voluntary self-disclosure"*

### Example Prompts

```
Classify the following item under the EAR. It is a commercial network router with integrated
AES-256 and RSA-2048 encryption, capable of 100Gbps throughput. We sell it to commercial
ISPs globally. Start with the Order of Review, determine ECCN or EAR99, and identify
any licence requirements for exports to China, India, and UAE.
```

```
We are a semiconductor company. We manufacture chips outside the US using US-origin EDA
tools (Category 3E001 technology) and equipment (3B001). Our chips are designed to support
advanced AI training workloads. Analyse our FDPR exposure — both General FDPR and
Entity List FDPR — if we have customers on the Entity List.
```

```
We've discovered that our sales team shipped 5E002 encryption technology to a distributor
in the UAE without obtaining a licence. The distributor then reexported to Iran.
Walk us through our voluntary self-disclosure obligations, the factors BIS considers
in penalty mitigation (§ 764.5), and the steps to prepare the VSD package.
```

```
We are hiring 12 foreign nationals (7 Chinese nationals, 3 Indian nationals, 2 Russian
nationals) to work in our R&D division on projects involving 3E001 military electronics
technology and 4E001 computer technology. Conduct a deemed export analysis and identify
which hires require a BIS licence before we allow access to controlled technology.
```

```
Perform a gap analysis of our Export Compliance Programme against the seven-element
BIS framework. We have: a written export compliance policy, a designated EMPOC, and
a Consolidated Screening List integration in our ERP. We do not have: a formal training
programme, a recordkeeping procedure, an audit schedule, or a VSD procedure.
```

---

## 5. Skill Implementation Details

### Architecture

```
ear/
├── SKILL.md                          # Core skill — 8-step EAR workflow, all CCL categories,
│                                     #   country groups, licence exceptions overview,
│                                     #   restricted party lists, FDPR, deemed exports,
│                                     #   Part 748 licensing, Part 762 recordkeeping
└── references/
    ├── license-exceptions.md         # Full conditions, restrictions, and recordkeeping
    │                                 #   for all 14 licence exceptions (LVS through GFT)
    ├── ccl-eccn-guide.md             # Detailed ECCN lookup methodology, all 10 CCL
    │                                 #   categories with key ECCNs, Commerce Country Chart
    │                                 #   usage, and jurisdiction determination guidance
    └── compliance-program.md         # ECP design (7 elements), enforcement regime
                                      #   (civil/criminal penalties), VSD process,
                                      #   FDPR deep-dive, deemed export compliance,
                                      #   and BIS penalty guidelines
```

### What's in SKILL.md

- **Identity and scope**: Expert EAR compliance advisor persona for BIS/15 CFR Parts 730–774
- **Response format table**: Output format by task — ECCN classification, licence analysis, screening, ECP review, general questions
- **EAR Framework Overview**: BIS authority, ECRA citation, all 15 CFR Part numbers with subjects
- **Step 1 — Jurisdiction Determination**: ITAR Order of Review, CJ requests, CCATS requests
- **Step 2 — ECCN Classification**: ECCN format, all 10 CCL categories, 5 product groups, Reasons for Control, EAR99 determination
- **Step 3 — Licence Requirement Analysis**: Country Chart mechanics, Country Groups (A:1–E:2)
- **Step 4 — Licence Exceptions Overview**: All 14 exceptions with symbol, name, and scope
- **Step 5 — End-User/End-Use Controls**: All 5 restricted party lists, CSL, WMD prohibitions, Red Flag indicators
- **Step 6 — Special Topics**: Deemed exports, FDPR (General and Entity List), de minimis rule, US Person controls
- **Step 7 — Licensing (Part 748)**: SNAP-R portal, BIS-748P, review timelines, advisory opinions
- **Step 8 — Recordkeeping (Part 762)**: 5-year retention requirement and record types

### What's in the reference files

| File | Contents |
|------|----------|
| `license-exceptions.md` | Complete conditions, eligibility criteria, restrictions, notification/reporting requirements, and recordkeeping obligations for all 14 licence exceptions: LVS, GBS, CIV, APP, TSR, TMP, RPL, GOV, TSU, ENC, BAG, AVS, ACE, GFT |
| `ccl-eccn-guide.md` | ECCN lookup methodology; detailed coverage of all 10 CCL categories with representative ECCNs; Commerce Country Chart usage walkthrough; jurisdiction determination with ITAR/EAR Order of Review decision tree; CCATS and CJ request process |
| `compliance-program.md` | Seven-element ECP design framework; BIS civil penalty guidelines (up to $1.3M per violation) and criminal penalties (up to 20 years); VSD process and mitigation factors; FDPR deep-dive (General FDPR, Huawei FDPR, advanced chip controls 2022–2023); deemed export and deemed reexport compliance procedures; BIS audit preparation |

### Inputs used to build the skill

| Source | Description |
|--------|-------------|
| 15 CFR Parts 730–774 (EAR) | Full regulatory text — all Parts including CCL (Part 774 Supplement No. 1) |
| Export Control Reform Act of 2018 (ECRA) | Statutory authority, 50 U.S.C. § 4801 et seq. |
| BIS Commerce Country Chart | Part 738 Supplement No. 1 — licence requirement matrix |
| BIS Entity List, Denied Persons List, Unverified List, MEU List | Current restricted party lists (Supplements 4, 6, 7 to Part 744) |
| BIS Red Flag Indicators (§ 732.6) | Published guidance on suspicious transaction indicators |
| OFAC SDN List | Parallel OFAC screening requirement |
| BIS Administrative Enforcement Orders | Penalty guidance and VSD precedents under Part 766 |

### Skill trigger phrases

`EAR compliance`, `Export Administration Regulations`, `ECCN classification`, `Commerce Control List`,
`CCL category`, `EAR99`, `BIS licence`, `Bureau of Industry and Security`, `dual-use export`,
`licence exception ENC`, `licence exception TMP`, `SNAP-R application`, `Form BIS-748P`,
`Entity List`, `Denied Persons List`, `Unverified List`, `Military End-User List`,
`Consolidated Screening List`, `Foreign Direct Product Rule`, `FDPR`, `deemed export`,
`deemed reexport`, `§ 734.13`, `de minimis rule`, `Country Chart`, `Order of Review`,
`ITAR vs EAR`, `Commodity Jurisdiction`, `CCATS`, `export compliance programme`,
`voluntary self-disclosure`, `Part 762 recordkeeping`, `EAR red flags`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.8.0 — August 2026

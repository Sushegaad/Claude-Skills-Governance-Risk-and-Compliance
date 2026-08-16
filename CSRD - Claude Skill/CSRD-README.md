# Corporate Sustainability Reporting Directive (CSRD) Skill for Claude

> **Disclaimer:** This skill provides informational guidance on CSRD compliance obligations based on Directive (EU) 2022/2464 and the European Sustainability Reporting Standards (ESRS) issued under Commission Delegated Regulation (EU) 2023/2772. It does not constitute legal advice or assurance. CSRD disclosures are subject to statutory limited assurance by a qualified auditor or independent assurance services provider — this skill supports the preparation process but does not replace the assurance engagement or advice from a qualified sustainability reporting specialist.

---

## 1. What Does the Skill Do?

This skill turns Claude into an expert EU sustainability reporting advisor with comprehensive knowledge of the **Corporate Sustainability Reporting Directive (CSRD)** — Directive (EU) 2022/2464 — and the **European Sustainability Reporting Standards (ESRS)** adopted under Commission Delegated Regulation (EU) 2023/2772. The CSRD, which entered into force on 5 January 2023, replaces the Non-Financial Reporting Directive (NFRD) and expands mandatory sustainability reporting from approximately 11,000 companies to approximately 50,000 companies across the EU.

The skill guides finance, legal, sustainability, and compliance teams through every phase of CSRD implementation: determining whether a company is in scope and when it must first report, conducting the **double materiality assessment (DMA)** that underpins all ESRS reporting decisions, assessing current reporting gaps against mandatory and topical ESRS standards, drafting compliant sustainability disclosures, and preparing for the limited assurance engagement required from the first reporting year.

At the heart of the skill is full coverage of the **ESRS standards architecture** — the two cross-cutting standards (ESRS 1 General Requirements and ESRS 2 General Disclosures, which are mandatory for all in-scope companies) and the ten topical standards across environmental (E1–E5), social (S1–S4), and governance (G1) topics. For each topical standard, the skill covers applicability conditions, required disclosures, and specific datapoints — including the quantitative metrics that are most challenging to collect (Scope 3 GHG emissions, gender pay gap, lost-time injury frequency rate, living wage analysis).

The skill also addresses the **CSRD Omnibus Proposal** (European Commission, February 2025), which proposes scope narrowing and datapoint reduction, and advises on the current legislative status of those changes. For organizations with existing GRI, TCFD, or SASB reporting programs, the skill maps those frameworks to ESRS equivalents, enabling gap-based rather than ground-up implementation.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|----------------------|
| **CFOs and finance directors** | Scope determination, first reporting year, assurance readiness, financial materiality assessment |
| **Sustainability directors and ESG managers** | DMA process, topical standard selection, disclosure drafting, KPI and datapoint gap analysis |
| **Legal and compliance teams** | Regulatory scope analysis, Art. 19a requirements, assurance obligations, XBRL tagging requirements |
| **Boards and audit committees** | Governance disclosure requirements (ESRS 2 GOV-1 to GOV-5), oversight obligations |
| **Supply chain and procurement teams** | Value chain materiality, ESRS S2 (Workers in Value Chain), supplier data collection |
| **GRI/TCFD/SASB reporting teams** | Framework-to-ESRS mapping, gap identification, transition planning |
| **Auditors and assurance providers** | Limited assurance scope, ESRS disclosure structure, evidence requirements |
| **Non-EU companies** | Threshold analysis for companies with EU revenue >€150M and EU subsidiary/branch presence |
| **Listed SMEs** | Opt-out provisions, voluntary ESRS for SMEs, Phase 3 readiness planning |

---

## 3. Common Use Cases

### Scope and Threshold Analysis
- *"Is our company subject to CSRD? We're an unlisted EU company with 280 employees, €45M turnover, and €22M total assets."*
- *"We're a US company with €200M in EU revenue and two large EU subsidiaries. When do we need to start reporting?"*
- *"Our parent company is already doing CSRD reporting. Are we exempt as a subsidiary?"*
- *"We're a listed SME. Can we use the opt-out provision?"*

### Double Materiality Assessment
- *"Walk me through how to conduct a double materiality assessment under ESRS 1."*
- *"What's the difference between impact materiality and financial materiality under CSRD?"*
- *"How do we assess the significance of an impact? What does ESRS 1 say about scale, scope, and irremediability?"*
- *"Which ESRS topical standards are most likely to be material for a consumer goods manufacturer?"*
- *"We've completed our DMA. ESRS E1, S1, and G1 came out as material. What disclosures are required?"*

### Gap Assessment Against ESRS
- *"We currently report against GRI Standards. Run a CSRD gap assessment mapping our existing GRI disclosures to ESRS requirements."*
- *"We do TCFD reporting. What additional disclosures does ESRS E1 require beyond TCFD?"*
- *"Which ESRS 2 disclosures are mandatory regardless of our DMA outcome?"*
- *"We have no sustainability reporting at all. What do we need to produce for our first CSRD report (FY 2025)?"*

### Disclosure Drafting
- *"Draft our ESRS 2 SBM-1 (Strategy, Business Model, and Value Chain) disclosure."*
- *"Help me write our ESRS E1 transition plan narrative per Art. 19a(2)(a) requirements."*
- *"What quantitative datapoints must we disclose under ESRS S1 for our own workforce?"*
- *"Draft a governance disclosure (ESRS 2 GOV-1) describing our board's role in sustainability oversight."*

### Implementation Roadmap
- *"Build a 12-month CSRD implementation roadmap for a company with a FY 2025 first reporting year."*
- *"We need to set up value chain data collection from suppliers. What process does CSRD require?"*
- *"What does 'limited assurance' mean for CSRD? How do we prepare for the assurance engagement?"*
- *"What XBRL tagging requirements apply to our CSRD disclosures?"*

---

## 4. How to Use the Skill

### Installation
1. Download the `csrd.skill` file from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `csrd.skill`
4. The skill is immediately active in your Claude sessions

### Triggering the Skill
The skill activates automatically when your message relates to CSRD, ESRS, or EU sustainability reporting obligations. Example phrases that trigger it:

- *"CSRD compliance"*
- *"ESRS reporting obligations"*
- *"double materiality assessment"*
- *"EU sustainability disclosure"*
- *"non-financial reporting Europe"*
- *"ESG reporting CSRD"*
- *"CSRD gap assessment"*
- *"ESRS E1 climate disclosures"*
- *"CSRD scope thresholds"*

### Example Prompts

```
"We're a large private EU company (320 employees, €55M turnover, €28M 
total assets) that has never done sustainability reporting. Determine 
our CSRD scope, first mandatory reporting year, and produce a prioritized 
gap assessment against mandatory ESRS 2 disclosures and the topical 
standards most likely to be material for a logistics company."
```

```
"Walk me through conducting a double materiality assessment from scratch. 
We are a mid-size pharmaceutical manufacturer. What process does ESRS 1 
require, and how do we determine which of the 10 topical standards are 
material for our operations and value chain?"
```

```
"We report to GRI Standards 2021 and follow TCFD recommendations. Map 
our existing disclosures to ESRS requirements and identify gaps we need 
to close for our FY 2025 CSRD first report."
```

```
"Draft the ESRS E1-1 (Transition Plan for Climate Change Mitigation) 
disclosure for a company that has committed to net zero by 2040 and 
has a science-based target. Include all elements required by Art. 19a(2)(a) 
and ESRS E1."
```

```
"We're a non-EU company (headquartered in the US) with €180M net 
turnover in the EU across five EU Member States and a large EU subsidiary. 
When do we first report under CSRD? Which ESRS standards apply? 
Are there any simplifications available to us?"
```

---

## 5. Skill Implementation Details

### Architecture

```
csrd/
├── SKILL.md                          # Core skill — legal basis, scope thresholds, DMA,
│                                     #   ESRS architecture, key disclosures, assurance,
│                                     #   XBRL, implementation workflows, framework comparison
└── references/
    ├── esrs-standards.md             # Standard-by-standard ESRS deep dive: applicability,
    │                                 #   required disclosures, and specific datapoints for
    │                                 #   all cross-cutting and topical standards
    ├── double-materiality.md         # DMA methodology, scoring templates, stakeholder
    │                                 #   engagement guide, sector-specific materiality guidance
    └── compliance-program.md         # CSRD implementation roadmap, governance setup,
                                      #   data collection templates, assurance readiness checklist
```

**Total:** ~1,175 lines across 4 files (SKILL.md + 3 reference files)

### What's in SKILL.md

- **Legal basis** — Directive (EU) 2022/2464, ESRS under CDR (EU) 2023/2772, relationship to Accounting Directive
- **Scope and thresholds table** — four entity categories (large PIEs, other large companies, listed SMEs, non-EU companies) with size criteria and first reporting years
- **Double Materiality Assessment** — two-perspective framework (impact materiality + financial materiality), 8-step DMA process per ESRS 1 paras. 45–56
- **ESRS standards architecture** — cross-cutting standards (ESRS 1, ESRS 2) and all 10 topical standards (E1–E5, S1–S4, G1) with key content
- **Key disclosure requirements** — ESRS 2 mandatory disclosures (GOV-1 through IRO-1); ESRS E1 climate datapoints; ESRS S1 workforce datapoints
- **Reporting format and assurance** — management report location requirement, XBRL/iXBRL digital tagging, limited assurance obligation (Art. 26a)
- **CSRD vs. other frameworks** — comparison table (CSRD/ESRS vs. GRI vs. TCFD vs. SASB) across 6 dimensions
- **Omnibus Proposal (2025)** — European Commission simplification proposals and status note
- **Four implementation workflows** — scope determination, gap assessment, transition plan drafting, value chain reporting setup

### What's in the reference files

| File | Contents |
|------|----------|
| `esrs-standards.md` | Each ESRS standard treated individually: ESRS 1 and ESRS 2 mandatory disclosure detail; E1 (Climate), E2 (Pollution), E3 (Water), E4 (Biodiversity), E5 (Circular Economy); S1 (Own Workforce), S2 (Value Chain Workers), S3 (Affected Communities), S4 (Consumers); G1 (Business Conduct) — applicability conditions, required disclosure references, specific quantitative datapoints |
| `double-materiality.md` | DMA process in detail: scoring methodology for impact significance (scale × scope × irremediability); financial materiality assessment criteria; stakeholder engagement requirements per ESRS 1 para. 22; sector-specific materiality guidance; DMA documentation requirements for SBM-3 |
| `compliance-program.md` | CSRD implementation program structure: governance setup (board oversight, data ownership), data collection templates for key metrics, internal reporting processes, assurance readiness checklist (limited assurance scope and evidence requirements), XBRL tagging timeline |

### Inputs used to build the skill

| Input | Description |
|-------|-------------|
| **Directive (EU) 2022/2464** | Full CSRD text — scope, thresholds, reporting obligations, assurance requirements, Art. 19a/29a/40a |
| **CDR (EU) 2023/2772** | Commission Delegated Regulation adopting all 12 ESRS standards (ESRS 1, 2, E1–E5, S1–S4, G1) |
| **EFRAG ESRS guidance** | EFRAG implementation guidance notes and Q&A for ESRS interpretation |
| **GRI Standards 2021** | Used for framework comparison and GRI-to-ESRS mapping (ESRS 1 Appendix C) |
| **TCFD recommendations** | Used for ESRS E1 / TCFD alignment analysis |
| **SASB Standards** | Used for SASB-to-ESRS sector mapping |
| **EC Omnibus Package (Feb 2025)** | European Commission CSRD simplification proposal for scope and datapoint reduction |
| **EU Taxonomy Regulation** | Referenced for ESRS E1 EU Taxonomy alignment disclosure requirements |

### Skill trigger phrases

`CSRD`, `Corporate Sustainability Reporting Directive`, `ESRS`, `European Sustainability Reporting Standards`, `double materiality`, `double materiality assessment`, `DMA`, `sustainability reporting EU`, `ESG disclosure Europe`, `non-financial reporting`, `ESRS E1`, `ESRS S1`, `ESRS G1`, `NFRD replacement`, `CSRD scope`, `CSRD thresholds`, `CSRD gap assessment`, `CSRD implementation`, `limited assurance CSRD`, `XBRL sustainability`, `CSRD GRI`, `CSRD TCFD`, `EFRAG ESRS`, `Scope 3 CSRD`, `CSRD transition plan`, `CSRD value chain`, `CSRD Omnibus`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.7.1 — August 2026

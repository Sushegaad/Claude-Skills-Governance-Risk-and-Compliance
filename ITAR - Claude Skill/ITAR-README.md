# International Traffic in Arms Regulations (ITAR) Skill for Claude

> ⚠️ **Disclaimer:** This skill provides informational guidance based on 22 CFR Parts 120–130 and established DDTC regulatory practice. It does not constitute legal advice. ITAR violations carry severe criminal and civil penalties. For matters involving export licence applications, voluntary disclosures, enforcement actions, or complex jurisdiction determinations, consult a qualified export control attorney or your Empowered Official.

---

## 1. What Does the Skill Do?

The ITAR Compliance Skill transforms Claude into an expert US defense export control advisor with deep knowledge of the International Traffic in Arms Regulations (22 CFR Parts 120–130), administered by the Directorate of Defense Trade Controls (DDTC) at the US Department of State. The skill covers the full ITAR compliance lifecycle — from determining whether an item is controlled under the United States Munitions List (USML) through to managing voluntary self-disclosures of violations.

The skill supports eight core workflows: jurisdiction determination (ITAR vs. EAR), DDTC registration guidance, export licensing (DSP-5, DSP-73, DSP-94), Technical Assistance Agreement (TAA) and Manufacturing License Agreement (MLA) drafting and review, deemed export rules for foreign nationals and Technology Control Plans (TCP), brokering regulations under 22 CFR Part 129, voluntary self-disclosure (VSD) process under 22 CFR § 127.12, and compliance programme design including the Empowered Official role.

All responses cite the specific CFR part and section relevant to the question (for example, "22 CFR § 124.1" or "22 CFR § 120.41"). Output format adapts to the task: structured analysis tables for gap assessments, step-by-step checklists for registration and licensing, clause-by-clause guidance for TAA/MLA drafting, and clear prose with CFR citations for general questions.

The skill is backed by three detailed reference files — USML category descriptions for all 21 categories, a licensing guide covering all licence types and exemptions, and a compliance programme reference with the full VSD process, penalty framework, and TCP template — loaded on demand to keep responses precise and efficient.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|------------------------|
| **Export Compliance Managers** | Conduct gap assessments, draft TCPs, manage licence portfolios, prepare VSD filings |
| **Empowered Officials (EOs)** | Understand signing obligations, jurisdiction determinations, DDTC registration duties |
| **Defence Manufacturers** | Classify products against the USML, determine registration requirements, plan TAAs |
| **Legal Counsel (Export Control)** | Draft TAA/MLA clauses, analyse penalty exposure, advise on VSD strategy |
| **HR and Security Teams** | Implement deemed export controls, screen foreign nationals, maintain TCP procedures |
| **Logistics and Shipping Teams** | Confirm licence validity before export, understand exemptions and record-keeping |
| **Business Development Teams** | Understand ITAR implications of international partnerships and FMS vs. DCS decisions |
| **Startup and Commercial Space Companies** | Determine ITAR vs. EAR jurisdiction for dual-use and space technologies |

---

## 3. Common Use Cases

### Jurisdiction and Classification
- "Is our military-grade antenna controlled under ITAR or EAR?"
- "Does the specially designed test under 22 CFR § 120.41 apply to our composite material?"
- "How do I file a Commodity Jurisdiction (CJ) request with DDTC?"
- "Which USML category covers unmanned aerial systems with targeting capability?"

### DDTC Registration
- "Who is required to register with DDTC under 22 CFR § 122.1?"
- "Walk me through the DS-2032 registration process step by step"
- "What are the annual registration fees and how do I renew?"
- "We acquired a new subsidiary — do we need to update our DDTC registration?"

### Export Licensing
- "What information is required on a DSP-5 application for hardware export?"
- "When can we use a DSP-73 instead of a DSP-5?"
- "What conditions are typically placed on an ITAR export licence?"
- "Does this transfer qualify for the Canadian exemption under 22 CFR § 126.5?"

### TAA and MLA Drafting
- "Draft a Technical Assistance Agreement clause covering retransfer prohibition"
- "What are the mandatory TAA clauses required under 22 CFR § 124.9?"
- "How does an MLA differ from a TAA and when do I need each?"
- "Our TAA scope has changed — what is the DDTC amendment process?"

### Deemed Exports and Technology Control Plans
- "A foreign national will need access to our ITAR-controlled design files — what do we need?"
- "Draft a Technology Control Plan for a defence manufacturer with foreign national employees"
- "Which nationalities require a deemed export licence for USML Category VIII technical data?"
- "What does an effective TCP need to cover under DDTC guidance?"

### Compliance Programme and Penalties
- "What elements does DDTC look for in an effective ITAR compliance programme?"
- "We discovered an unlicensed export — what is the voluntary self-disclosure process?"
- "What are the civil and criminal penalties for ITAR violations?"
- "Draft an ITAR compliance checklist for our annual internal audit"

---

## 4. How to Use the Skill

### Installation
1. Download `itar.skill` from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `itar.skill`
4. The skill is now active in all Claude sessions

### Triggering the Skill

The skill activates automatically when you raise ITAR or US defense export control topics. No special commands are needed. Example natural-language phrases that trigger the skill:

- *"Is this item ITAR controlled?"*
- *"We need to share technical data with our UK partner"*
- *"What does DDTC require for registration?"*
- *"Explain the deemed export rule"*
- *"We think we may have had an ITAR violation"*
- *"Draft a TAA for our French licensee"*
- *"What is the USML category for night-vision devices?"*

### Example Prompts

```
We manufacture passive infrared sensors used in both commercial security cameras
and military targeting systems. How do we determine if these are ITAR-controlled,
and what is the process if the jurisdiction is unclear?
```

```
Our company has just won a contract to provide engineering support to a foreign
military customer. We plan to share design drawings and provide on-site training.
What ITAR authorisation do we need, and how long does it take to obtain?
```

```
One of our engineers, a citizen of Germany, needs access to ITAR-controlled
technical data for a project. Walk me through our deemed export obligations and
what our Technology Control Plan needs to cover.
```

```
We discovered that one of our subsidiaries shipped ITAR hardware to a distributor
in Singapore without a DSP-5 licence. What is the voluntary self-disclosure
process and what factors will DDTC consider when determining the penalty?
```

```
Conduct an ITAR compliance gap assessment against these programme elements:
registration, TCP, training, screening, licence management, record retention,
and internal audits. Format the output as a table with status and recommended actions.
```

---

## 5. Skill Implementation Details

### Architecture

```
plugins/itar/
└── skills/
    └── itar/
        ├── SKILL.md                        # Core skill — 8 workflow definitions, regulatory
        │                                   #   structure, response format rules, CFR citations
        └── references/
            ├── usml-categories.md          # All 21 USML categories with key items, examples,
            │                               #   jurisdiction tips, and key ITAR definitions
            ├── licensing-guide.md          # Licence types (DSP-5/73/94/61, TAA, MLA),
            │                               #   application requirements, exemptions,
            │                               #   FMS vs. DCS comparison, record-keeping rules
            └── compliance-program.md       # Compliance programme elements, TCP template,
                                            #   penalty framework, VSD process (4 steps),
                                            #   DDTC Blue Lantern programme, audit checklist
```

### What's in SKILL.md

- Expert persona definition: ITAR compliance advisor with 22 CFR Parts 120–130 knowledge
- Response format table mapping task type to output format (jurisdiction analysis, registration, licensing, TAA/MLA, gap assessment, VSD, Q&A)
- Regulatory structure overview: all 10 CFR parts (120–130) with titles and key content
- 8 detailed core workflows with step-by-step guidance and CFR citations
- Embargoed and restricted country list (22 CFR § 126.1)
- Reference file loading instructions

### What's in the reference files

| File | Contents |
|------|----------|
| `references/usml-categories.md` | All 21 USML categories (I–XXI) with item descriptions, key definitions (defense article § 120.31, defense service § 120.32, technical data § 120.33, specially designed § 120.41), USML vs. CCL jurisdiction decision tips, Commodity Jurisdiction process |
| `references/licensing-guide.md` | All licence/agreement types with CFR references and use cases; DSP-5 application blocks and processing times; DSP-73 conditions; mandatory TAA clauses (§ 124.9); MLA vs. TAA comparison; selected exemptions (§§ 126.4, 126.5, 126.7, 125.4); FMS vs. DCS comparison; 5-year record-keeping requirements (§ 122.5) |
| `references/compliance-program.md` | 7 compliance programme elements including Empowered Official role; TCP template (10 sections); party screening requirements (DDTC, OFAC, BIS lists); civil penalties ($1,369,000/violation), criminal penalties ($1M fine, 20 years); 4-step VSD process; mitigating and aggravating factors; DDTC Blue Lantern end-use monitoring; compliance readiness checklist |

### Inputs used to build the skill

| Input | Detail |
|-------|--------|
| Primary regulation | 22 CFR Parts 120–130 (ITAR) |
| Administrative authority | DDTC, US Department of State |
| USML | 22 CFR § 121.1 — all 21 categories |
| Licensing CFR parts | Parts 123 (hardware), 124 (TAA/MLA), 125 (technical data) |
| Penalty authority | 22 USC § 2778; 22 CFR Part 127 |
| VSD framework | 22 CFR § 127.12 |
| Brokering rules | 22 CFR Part 129 |
| Registration | 22 CFR Part 122; DS-2032 |
| Deemed exports | 22 CFR § 120.50; § 120.62 (US persons) |
| Treaty frameworks | Australia, UK, Canada Defence Trade Cooperation Treaties |
| Related regimes | Export Administration Regulations (EAR), 15 CFR Parts 730–774 |

### Skill trigger phrases

`ITAR`, `International Traffic in Arms`, `USML`, `United States Munitions List`, `DDTC`,
`DSP-5`, `DSP-73`, `TAA`, `Technical Assistance Agreement`, `MLA`, `Manufacturing License Agreement`,
`defense article`, `defense service`, `technical data export`, `deemed export`, `foreign national access`,
`Commodity Jurisdiction`, `CJ determination`, `ITAR registration`, `export control`,
`22 CFR`, `voluntary self-disclosure`, `Technology Control Plan`, `TCP`, `Empowered Official`,
`brokering regulations`, `ITAR vs EAR`, `USML category`, `Part 129`, `DDTC registration`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.7.1 — August 2026

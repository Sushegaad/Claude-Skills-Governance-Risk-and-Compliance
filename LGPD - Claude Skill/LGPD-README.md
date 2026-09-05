# Brazil Lei Geral de Proteção de Dados (LGPD) Skill for Claude

> ⚠️ **Disclaimer:** This skill provides informational guidance based on Law No. 13,709/2018 (LGPD) as amended by Law No. 13,853/2019 and ANPD resolutions. It does not constitute legal advice. For matters involving ANPD enforcement, high-risk processing, or complex international transfer arrangements, consult a qualified Brazilian data protection lawyer or your designated DPO (Encarregado).

---

## 1. What Does the Skill Do?

The LGPD Compliance Skill transforms Claude into an expert Brazilian data protection advisor with comprehensive knowledge of the Lei Geral de Proteção de Dados Pessoais (LGPD) — Law No. 13,709/2018 as amended by Law No. 13,853/2019 — together with all relevant ANPD (Autoridade Nacional de Proteção de Dados) resolutions, including Resolution CD/ANPD No. 15/2024 setting the 3-working-day breach notification requirement.

> **2026 Update — Brazil-EU Mutual Adequacy:** On January 26–27, 2026, the European Commission formally adopted an adequacy decision for Brazil under GDPR Article 45, and Brazil's ANPD simultaneously recognised the EU as an adequate transfer destination. This mutual adequacy **eliminates the need for SCCs, BCRs, or other transfer safeguards for Brazil ↔ EU personal data flows**. The skill has been updated (v1.5.0, July 2026) to reflect this change across the international transfers section, the LGPD vs. GDPR comparison table, and the gap assessment workflow.

The skill covers the full LGPD compliance lifecycle. It analyses processing activities against all 10 legal bases for regular personal data (Art. 7) and the stricter bases for sensitive data (Art. 11), guides organisations through data subject rights fulfilment under Arts. 17–22, produces LGPD-compliant privacy notices containing all Art. 9 required elements, and assists with data breach notification workflows under Art. 48. The skill also supports DPO (Encarregado) appointment under Art. 41, Records of Processing Activities (RoPA) under Art. 37, Data Protection Impact Assessments (RIPD/DPIA) under Art. 38, and international data transfer compliance under Arts. 33–36 — including the landmark Brazil-EU adequacy decision of January 2026.

The skill is particularly valuable for organisations operating across both Brazil and the EU, as it explicitly maps LGPD requirements against GDPR equivalents — highlighting key differences including the 10 vs. 6 legal bases, the 3-working-day vs. 72-hour breach notification timelines, the always-mandatory DPO vs. GDPR's conditional DPO obligation, and the R$50 million vs. €20 million penalty caps.

All responses cite the specific LGPD article relevant to the question (for example, "Art. 7, IX" or "Art. 48, §1º"). Output format adapts to the task: structured gap tables for assessments, step-by-step workflows for breach response and data subject requests, full document templates for privacy notices and RIPDs, and clear prose with article citations for general questions.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|------------------------|
| **Data Protection Officers (Encarregados)** | Draft privacy notices, manage DSR workflows, coordinate ANPD breach notifications, maintain RoPA |
| **Legal Counsel** | Analyse legal bases for processing, review processor agreements, assess penalty exposure under Art. 52 |
| **Compliance Managers** | Conduct LGPD gap assessments, build compliance roadmaps, prepare for ANPD investigations |
| **Software Engineers and Architects** | Understand privacy-by-design obligations (Art. 49), assess data flows for LGPD compliance |
| **Product Managers** | Determine legal bases for new features, ensure consent mechanisms meet Art. 8 standards |
| **HR Teams** | Understand LGPD obligations for employee data processing, handle DSRs from staff |
| **Marketing Teams** | Assess consent validity, manage opt-out mechanisms, understand children's data rules (Art. 14) |
| **Multinational Companies** | Compare LGPD to GDPR obligations, harmonise dual-jurisdiction compliance programmes |

---

## 3. Common Use Cases

### Legal Basis Analysis
- "What legal basis should we use for processing employee health data in Brazil?"
- "Can we use legitimate interest (Art. 7, IX) for our marketing analytics?"
- "We process sensitive health data — which Art. 11 bases are available to us?"
- "What does the LGPD require for valid consent under Art. 8?"

### LGPD Gap Assessment
- "Conduct an LGPD gap assessment across our data processing activities"
- "We have GDPR compliance — what additional steps do we need for LGPD?"
- "Review our privacy programme against all 10 Art. 6 principles"
- "Are we required to appoint a DPO under LGPD?"

### Privacy Notice and Document Drafting
- "Draft an LGPD-compliant privacy notice for our Brazilian e-commerce platform"
- "What elements must our privacy notice include under Art. 9?"
- "Draft a processor agreement clause that meets Art. 39 obligations"
- "Generate a RIPD (DPIA) template for our biometric attendance system"

### Data Subject Rights
- "A Brazilian customer has asked for access to all their personal data — what do we do?"
- "What is the timeframe for responding to a data deletion request under Art. 18, IV?"
- "Can we refuse a portability request (Art. 18, V) and if so, on what grounds?"
- "Draft a data subject rights procedure for our Brazilian operations"

### Breach Response
- "We've had a data breach affecting Brazilian users — what are our ANPD notification obligations?"
- "What must the preliminary ANPD breach notification contain under Resolution No. 15/2024?"
- "How does LGPD's breach notification timeline compare to GDPR's 72-hour requirement?"
- "Draft our breach notification template for the ANPD portal"

### International Transfers
- "Can we transfer Brazilian customer data to our US parent company?"
- "What international transfer mechanisms are available under Arts. 33–36?"
- "Do we still need SCCs for data transfers from Brazil to the EU after the January 2026 adequacy decision?"
- "Has ANPD issued any adequacy decisions for specific countries?"
- "What contractual clauses do we need for data transfers from Brazil to the United States?"

### Penalties and Enforcement
- "What is our maximum penalty exposure for an LGPD violation under Art. 52?"
- "How does ANPD calculate fines — what factors are considered?"
- "What is the ANPD enforcement process and how long does an investigation take?"
- "What aggravating and mitigating factors apply under Art. 52, §1º?"

---

## 4. How to Use the Skill

### Installation
1. Download `lgpd.skill` from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `lgpd.skill`
4. The skill is now active in all Claude sessions

### Triggering the Skill

The skill activates automatically when you raise LGPD or Brazilian data protection topics. No special commands are needed. Example natural-language phrases that trigger the skill:

- *"Is this LGPD compliant?"*
- *"We process data for Brazilian users"*
- *"What does the ANPD require for breach notification?"*
- *"Draft a privacy notice for our Brazil operations"*
- *"What are our data subject rights obligations in Brazil?"*
- *"How does LGPD compare to GDPR?"*
- *"We need to appoint a DPO for Brazil"*

### Example Prompts

```
We are a SaaS company based in the US that has recently started offering services
to Brazilian customers. We collect names, emails, and usage analytics. Are we
subject to LGPD, and if so, what are the first five compliance steps we should take?
```

```
We process biometric data (fingerprints) for employee time-tracking at our
Brazilian manufacturing facility. What legal basis can we use under Art. 11,
and what additional safeguards do we need to implement?
```

```
Draft an LGPD-compliant privacy notice for our Brazilian B2C mobile application.
We collect name, email, phone number, location data, and purchase history.
We share data with our payment processor and analytics provider.
```

```
We discovered a ransomware attack that encrypted a database containing personal
data of approximately 50,000 Brazilian customers. Walk us through the complete
ANPD breach notification process including the preliminary and full report requirements.
```

```
Compare our GDPR compliance programme against LGPD requirements and identify
the gaps we need to close. Focus on: DPO obligations, legal bases, breach
notification timelines, children's data rules, and penalty exposure.
```

---

## 5. Skill Implementation Details

### Architecture

```
plugins/lgpd/
└── skills/
    └── lgpd/
        ├── SKILL.md                        # Core skill — response format rules, LGPD structure
        │                                   #   overview, all legal bases, data subject rights,
        │                                   #   controller/processor obligations, 6 core workflows,
        │                                   #   LGPD vs. GDPR comparison table
        └── references/
            ├── lgpd-articles.md            # Article-by-article LGPD summary (Arts. 1–55-L)
            │                               #   including all ANPD resolutions as of 2025
            ├── anpd-enforcement.md         # ANPD organisational structure, enforcement process
            │                               #   (3 phases), penalty calculation methodology,
            │                               #   enforcement priorities, notable actions,
            │                               #   complaint filing process
            └── compliance-program.md       # 4-phase compliance roadmap, RoPA template,
                                            #   DSR procedure, RIPD/DPIA template,
                                            #   breach notification templates (preliminary
                                            #   and full), DPO job description, gap checklist
```

### What's in SKILL.md

- Expert persona: Brazilian data protection advisor with LGPD and ANPD knowledge
- Response format table mapping task type to structured output (gap assessment, legal basis analysis, policy drafting, DSR workflow, RIPD, breach response, penalty exposure, Q&A)
- LGPD scope and extraterritorial reach (Art. 3) with exemptions (Art. 4)
- All 10 Art. 6 principles with descriptions
- All 10 Art. 7 legal bases for regular personal data with key requirements
- Art. 11 sensitive personal data bases with categories
- Complete data subject rights table (Arts. 17–22) with response timeframes
- Controller and processor obligations (Arts. 37–41)
- Consent requirements (Art. 8) — six validity criteria
- International transfer mechanisms (Arts. 33–36)
- Security and incident response (Arts. 46–48) including 3-day preliminary notification
- ANPD sanctions table (Art. 52) with all 8 sanction types
- 6 detailed workflows (legal basis, gap assessment, privacy notice, DSR, breach response, LGPD vs. GDPR)

### What's in the reference files

| File | Contents |
|------|----------|
| `references/lgpd-articles.md` | Article-by-article summary of all LGPD chapters including Chapter I (General Provisions), Chapter II (Sensitive and Children's Data), Chapter III (Data Subject Rights), Chapter IV (Public Entities), Chapter V (International Transfers), Chapter VI (Controllers and Processors), Chapter VII (Security and Governance), Chapter VIII (ANPD), Chapter IX (Sanctions); ANPD resolution timeline from 2021–2024 |
| `references/anpd-enforcement.md` | ANPD structure (5-director Board); 3-phase enforcement process with timelines; penalty calculation methodology with all Art. 52 §1º factors; ANPD strategic enforcement priorities; notable enforcement actions (telemarketing, health sector, breach investigations); cooperation with Brazilian authorities (SENACON, CADE, Banco Central) and international authorities (CNIL, ICO, CNPD Portugal); complaint filing process |
| `references/compliance-program.md` | 4-phase compliance roadmap (Foundation/Remediation/Operationalisation/Ongoing); full RoPA template per Art. 37 and ANPD Resolution No. 2/2022; DSR procedure with identity verification and response classification; RIPD/DPIA template (6 sections); preliminary ANPD breach notification template per Resolution No. 15/2024; full ANPD breach report template; data subject notification template; DPO job description (mandatory and recommended functions); comprehensive gap assessment checklist |

### Inputs used to build the skill

| Input | Detail |
|-------|--------|
| Primary regulation | Law No. 13,709/2018 (LGPD) as amended by Law No. 13,853/2019 |
| Supervisory authority | ANPD (Autoridade Nacional de Proteção de Dados) |
| Breach notification rule | ANPD Resolution CD/ANPD No. 15/2024 — 3 working day preliminary notification |
| RoPA and DPO rules | ANPD Resolution No. 2/2022 |
| SME exemptions | ANPD Resolution No. 4/2023 |
| Comparative framework | EU GDPR (Regulation (EU) 2016/679) — for LGPD vs. GDPR analysis |
| Related Brazilian law | Marco Civil da Internet; Consumer Defence Code (CDC); Cadastro Positivo |
| International cooperation | ANPD MoUs with CNIL, ICO, CNPD Portugal, URCDP; RIPD network; GPA membership |

### Skill trigger phrases

`LGPD`, `Lei Geral de Proteção de Dados`, `Brazilian data protection`, `ANPD`,
`personal data Brazil`, `data subject rights Brazil`, `Art. 7 LGPD`, `Art. 11 LGPD`,
`Art. 18 LGPD`, `Art. 48 LGPD`, `encarregado`, `DPO Brazil`, `RIPD`, `DPIA Brazil`,
`breach notification Brazil`, `3 working days ANPD`, `legitimate interest Brazil`,
`sensitive data Brazil`, `international transfer Brazil`, `adequacy ANPD`,
`Brazil EU adequacy`, `Brazil adequacy decision 2026`, `SCCs Brazil EU`,
`R$50 million fine`, `2% revenue Brazil`, `privacy notice Brazil`, `consent Brazil`,
`children data Brazil`, `Art. 14 LGPD`, `data protection Brazil`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.9.0 — September 2026

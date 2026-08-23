# EU Network and Information Security Directive 2 (NIS2) Skill for Claude

> ⚠️ **Disclaimer:** This skill provides informational guidance based on Directive (EU) 2022/2555 (NIS2) and ENISA guidance. It does not constitute legal advice. NIS2 has been transposed differently across EU Member States, and obligations vary by jurisdiction. For matters involving supervisory authority interaction, incident reporting to national CSIRTs, or penalty exposure, consult qualified legal counsel in your relevant Member State(s).

---

## 1. What Does the Skill Do?

The NIS2 Compliance Skill transforms Claude into an expert EU cybersecurity regulatory advisor with comprehensive knowledge of Directive (EU) 2022/2555 (NIS2), which entered into force on 27 December 2022, replaced NIS1 (Directive (EU) 2016/1148), and had a Member State transposition deadline of 17 October 2024. The skill covers the complete NIS2 compliance lifecycle — from initial entity classification through governance obligations, security measure implementation, incident reporting, supply chain security, and supervisory engagement.

The skill's central reference point is the two-tier entity classification: Essential Entities (EE) covering Annex I sectors such as energy, transport, banking, health, digital infrastructure, and public administration; and Important Entities (IE) covering Annex II sectors such as postal services, waste management, chemicals, food, manufacturing, and research. Size thresholds (medium enterprises: ≥50 employees OR ≥€10M turnover) determine automatic inclusion, with smaller entities potentially in scope via Member State designation.

The skill provides detailed guidance on all 10 Art. 21 cybersecurity risk management measures — from risk analysis policies and incident handling through to MFA mandates and supply chain security — as well as the Art. 23 incident reporting timeline: 24-hour early warning, 72-hour incident notification, and 1-month final report to national CSIRTs or competent authorities. It also covers Art. 20 management body governance obligations, including personal liability provisions and mandatory cybersecurity training for senior leadership.

The skill includes a detailed ISO 27001:2022 alignment module, mapping all 10 Art. 21 measures to corresponding Annex A controls and clearly identifying four areas where NIS2 goes beyond ISO 27001: explicit MFA mandates, supply chain ENISA risk assessments, management body personal liability, and prescriptive incident reporting timelines.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|------------------------|
| **CISOs and Security Leaders** | Gap assessments against Art. 21 measures, policy drafting, supervisory engagement preparation |
| **Board and Executive Teams** | Understanding Art. 20 governance obligations and personal liability provisions |
| **Compliance and Risk Managers** | Entity classification, penalty exposure analysis, remediation roadmaps |
| **IT and OT Security Teams** | Control implementation guidance for all 10 Art. 21 measures with technical specifics |
| **Legal Counsel** | Member State transposition differences, supervisory exposure (EE vs. IE), penalty calculation |
| **ISO 27001 Practitioners** | Mapping existing ISMS controls to NIS2 obligations, identifying gaps |
| **Supply Chain and Procurement Teams** | Implementing Art. 21(2)(d) supplier security requirements |
| **Incident Response Teams** | Art. 23 reporting workflow with pre-drafted notification templates |

---

## 3. Common Use Cases

### Entity Classification
- "Are we an Essential Entity or Important Entity under NIS2?"
- "We're a cloud services provider — which NIS2 Annex applies to us?"
- "Does NIS2 apply to our 45-person company?"
- "How has Germany/France/Ireland transposed NIS2 — do we need to self-register?"

### Gap Assessment
- "Conduct a NIS2 gap assessment against all 10 Art. 21 measures"
- "We are ISO 27001 certified — what additional controls do we need for NIS2?"
- "Rate our current security posture against each Art. 21 measure and identify priority gaps"
- "What is our penalty exposure if we fail the Art. 21 gap assessment?"

### Art. 21 Control Implementation
- "What does NIS2 require for supply chain security under Art. 21(2)(d)?"
- "Draft a cryptography and encryption policy aligned to Art. 21(2)(h)"
- "What MFA requirements does Art. 21(2)(j) impose and how should we implement them?"
- "Help me build a business continuity plan that meets Art. 21(2)(c)"

### Incident Reporting
- "Walk me through the NIS2 Art. 23 incident reporting timeline step by step"
- "What makes an incident 'significant' under Art. 23(3)?"
- "Draft a 24-hour early warning notification template for our national CSIRT"
- "What must the 1-month final report include?"

### Governance and Management Body Obligations
- "What does Art. 20 require from our board regarding cybersecurity?"
- "What cybersecurity training is required for management bodies under NIS2?"
- "Draft a board-level cybersecurity governance charter aligned to Art. 20"
- "How does personal liability under NIS2 work for senior management?"

### ISO 27001 Alignment
- "Map our ISO 27001:2022 Annex A controls to NIS2 Art. 21 measures"
- "We have ISO 27001 — does that cover NIS2 compliance?"
- "What are the NIS2 gaps that ISO 27001 certification does not address?"
- "Which ISO 27001:2022 controls cover Art. 21 Measure 4 supply chain security?"

---

## 4. How to Use the Skill

### Installation
1. Download `nis2.skill` from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `nis2.skill`
4. The skill is now active in all Claude sessions

### Triggering the Skill

The skill activates automatically when you raise NIS2 or EU cybersecurity directive topics. No special commands are needed. Example natural-language phrases that trigger the skill:

- *"Are we subject to NIS2?"*
- *"We need to comply with the NIS2 Directive"*
- *"What does NIS2 require for incident reporting?"*
- *"Gap assessment against NIS2 Art. 21"*
- *"Essential Entity vs Important Entity classification"*
- *"NIS2 and ISO 27001 alignment"*
- *"We had a cybersecurity incident — do we need to report it?"*

### Example Prompts

```
We are a mid-size energy distribution company operating across three EU Member States
with 200 employees and €80M annual revenue. Are we an Essential Entity or Important Entity
under NIS2, and what are the key differences in supervisory treatment between the two tiers?
```

```
Conduct a NIS2 Art. 21 gap assessment for our organisation. We have ISO 27001:2022
certification. For each of the 10 measures, identify whether our ISO 27001 controls
provide sufficient evidence and highlight where we have specific NIS2 gaps.
```

```
We experienced a ransomware attack yesterday that disrupted our online banking services
for 6 hours affecting approximately 40,000 customers. Walk me through the NIS2 Art. 23
incident reporting process — what do we need to report, to whom, and by when?
```

```
Our board is asking what their personal obligations are under NIS2 Art. 20. Draft a
briefing note covering: what they must approve, what training they need, and what
personal liability they face if cybersecurity measures are inadequate.
```

```
Draft an NIS2-compliant supply chain security policy covering: supplier risk assessment,
contractual security requirements, ongoing monitoring, and integration with ENISA
coordinated risk assessments under Art. 22.
```

---

## 5. Skill Implementation Details

### Architecture

```
plugins/nis2/
└── skills/
    └── nis2/
        ├── SKILL.md                        # Core skill — entity classification, all key articles,
        │                                   #   7 core help workflows, reference loading rules
        └── references/
            ├── article-21-measures.md      # Detailed implementation guidance for all 10 Art. 21
            │                               #   measures including proportionality principle,
            │                               #   significant incident indicators, technical specifics
            └── iso27001-nis2-mapping.md    # ISO 27001:2022 Annex A to NIS2 Art. 21 cross-reference
                                            #   table; 4 key NIS2 gaps vs. ISO 27001; practical
                                            #   guidance for certified organisations
```

### What's in SKILL.md

- Expert persona: NIS2 compliance advisor with full Directive knowledge
- Core framework: two-tier entity classification (EE/IE), Annex I/II sectors, size thresholds (Art. 3)
- Key articles summary: Art. 20 (governance), Art. 21 (10 risk management measures), Art. 23 (incident reporting — 24h/72h/1 month), Art. 22 (coordinated supply chain risk assessments), Art. 32/33 (supervision — proactive EE vs. reactive IE), Art. 34 (penalties — €10M/2% for EE, €7M/1.4% for IE)
- 7 core help workflows with detailed guidance (classification, gap assessment, incident reporting, governance, policy drafting, ISO 27001 alignment, penalty analysis)
- Reference file loading instructions

### What's in the reference files

| File | Contents |
|------|----------|
| `references/article-21-measures.md` | All 10 Art. 21 measures with full implementation guidance; specific technical details (cryptographic algorithms, MFA standards, patch SLAs, backup testing frequency, RBAC requirements); significant incident indicators per Art. 23(3); proportionality principle with EE vs. IE distinction |
| `references/iso27001-nis2-mapping.md` | Complete mapping table of all 10 NIS2 Art. 21 measures to ISO 27001:2022 Annex A controls; ISO 27001 controls with no direct NIS2 equivalent; 6 NIS2 requirements with limited ISO 27001 coverage (Art. 20 personal liability, Art. 23 timelines, Art. 22 ENISA supply chain, MFA mandate); 6-step practical guidance for ISO 27001-certified entities |

### Inputs used to build the skill

| Input | Detail |
|-------|--------|
| Primary directive | Directive (EU) 2022/2555 (NIS2) — entered into force 27 December 2022 |
| Predecessor directive | Directive (EU) 2016/1148 (NIS1) — repealed by NIS2 |
| Transposition deadline | 17 October 2024 |
| ENISA guidance | ENISA NIS2 guidelines; ENISA coordinated supply chain risk assessments (Art. 22) |
| ISO alignment | ISO/IEC 27001:2022 and Annex A controls |
| Risk methodology | ISO 27005; NIST RMF (referenced as equivalent methodologies) |
| Incident reporting | National CSIRT notification frameworks across EU Member States |
| Supervisory framework | Art. 32 (EE proactive) and Art. 33 (IE reactive) supervision |
| Penalty framework | Art. 34 — EE (€10M/2% global turnover), IE (€7M/1.4% global turnover) |

### Skill trigger phrases

`NIS2`, `NIS 2`, `Network and Information Security Directive`, `Directive (EU) 2022/2555`,
`Essential Entity`, `Important Entity`, `Art. 21 NIS2`, `Art. 23 NIS2`, `Art. 20 NIS2`,
`CSIRT notification`, `24 hour early warning`, `72 hour incident notification`,
`NIS2 gap assessment`, `NIS2 compliance`, `cybersecurity risk management measures`,
`supply chain security NIS2`, `NIS2 penalties`, `€10 million fine`, `2% global turnover`,
`NIS2 and ISO 27001`, `NIS2 board obligations`, `management body cybersecurity`,
`NIS2 transposition`, `significant incident`, `ENISA NIS2`, `NIS2 sectors`, `Annex I Annex II`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.8.0 — August 2026

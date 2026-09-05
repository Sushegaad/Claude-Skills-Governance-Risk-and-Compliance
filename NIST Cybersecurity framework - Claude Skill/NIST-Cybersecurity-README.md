# NIST Cybersecurity Framework (CSF) Skill

> A Claude skill for security, risk, and compliance teams to implement, assess, and improve their cybersecurity posture using the NIST Cybersecurity Framework — covering both CSF 2.0 and CSF 1.1.

---

## 1. What Does the Skill Do?

The NIST CSF skill turns Claude into an expert NIST Cybersecurity Framework advisor and cybersecurity risk management consultant. It provides structured, actionable guidance across the full CSF lifecycle — from initial gap assessments and profile creation through to implementation roadmaps, tier advancement, and cross-framework mapping.

The skill covers **NIST CSF 2.0** (February 2024) — the current version — including the new **Govern (GV)** function, the expanded supply chain risk management categories, and the strengthened organisational profiles model. It also covers **NIST CSF 1.1** (April 2018) and supports teams migrating between versions.

Outputs are tailored to the task: structured gap assessment tables, full organisational profiles with Current and Target states, prioritised implementation roadmaps, control-level implementation guidance, and policy documents mapped to specific CSF subcategory IDs.

---

## 2. Intended Audiences

This skill is designed for security, risk, and compliance professionals across all industry sectors and organisation sizes.

- **CISOs and security managers** building or maturing an organisational cybersecurity programme
- **Risk managers and GRC analysts** conducting gap assessments, creating profiles, or reporting cybersecurity risk to leadership
- **Security engineers and architects** seeking implementation guidance for specific CSF subcategories
- **Compliance teams** mapping regulatory requirements (HIPAA, FedRAMP, PCI DSS, state laws) to a common CSF framework
- **SMBs** using CSF to understand and prioritise cybersecurity investments without a large in-house team
- **Consultants** supporting clients through initial CSF adoption or CSF 1.1 → 2.0 migration

---

## 3. Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| **Gap assessment** | "Perform a CSF 2.0 gap assessment for a mid-size financial services firm. We have basic asset inventories but no formalised governance." |
| **Profile creation** | "Help me create a CSF 2.0 Organisational Profile — Current and Target — for a healthcare SaaS company." |
| **Tier assessment** | "Assess our current CSF implementation tier based on our practices and tell us what Tier 3 would require." |
| **Implementation roadmap** | "Based on our gap assessment results, build a 90-day implementation roadmap for moving from Tier 1 to Tier 2." |
| **Govern function guidance** | "What does the new GV.SC category require for supply chain risk management?" |
| **Cross-framework mapping** | "Map our ISO 27001:2022 controls to CSF 2.0 subcategories." |
| **Policy generation** | "Write a Cybersecurity Governance Policy aligned to CSF 2.0 GV function subcategories." |
| **CSF 1.1 → 2.0 migration** | "We're currently using CSF 1.1. What do we need to do to migrate to CSF 2.0?" |
| **Subcategory guidance** | "How do I implement GV.SC-07 — ongoing supplier risk monitoring?" |
| **Incident response alignment** | "Map our incident response process to CSF 2.0 RS and RC function subcategories." |

---

## 4. How to Use the Skill

Once the skill is installed in Claude, it activates automatically whenever you ask about NIST CSF, cybersecurity risk management, organisational cybersecurity profiles, implementation tiers, or related topics. You do not need to reference the skill by name.

### Tips for best results

**Specify CSF version** — state whether you are working with CSF 2.0, CSF 1.1, or migrating between them. The skill defaults to CSF 2.0.

**Provide organisational context** — industry, size, existing security practices, and known regulatory obligations help the skill tailor its outputs. For example:

> "We're a 50-person healthcare software company with basic security controls but no formalised risk management programme. Help us build a CSF 2.0 Current Profile."

**Reference specific functions, categories, or subcategories** — for targeted guidance, naming the function (e.g. `GV`), category (e.g. `ID.AM`), or subcategory ID (e.g. `PR.AA-05`) produces more focused responses.

**Ask for one deliverable at a time** — gap assessments, profiles, and roadmaps each require separate focus for best results.

### Example interaction

```
You:     We need to assess our current cybersecurity posture against NIST CSF 2.0.
         We're a 200-person e-commerce company. We have no formal cybersecurity policy,
         basic asset inventories, and no incident response plan.

Claude:  [Performs structured gap assessment covering all 6 CSF 2.0 functions:
          - GV: ❌ No policy, no risk tolerance statements — critical gap
          - ID: 🟡 Basic asset inventory exists, no formal risk assessment process
          - PR: 🟡 Some access controls, no awareness training programme
          - DE: ❌ No continuous monitoring, no event analysis capability
          - RS: ❌ No incident response plan or declared criteria
          - RC: ❌ No recovery plan or documented procedures
          Prioritised remediation order with 30/60/90-day quick wins]
```

---

## 5. Skill Implementation Details

### Architecture

The skill follows a three-layer structure:

```
nist-csf/
├── SKILL.md                                  # Core skill logic and workflows
└── references/
    ├── csf-20-functions-categories.md        # All 6 functions, categories, subcategories (CSF 2.0)
    ├── csf-10-to-20-mapping.md               # CSF 1.1 → 2.0 migration guide and subcategory mapping
    └── csf-implementation-tiers.md           # Tier 1–4 definitions, diagnostics, and advancement guidance
```

`SKILL.md` is loaded into Claude's context when the skill triggers. Reference files are loaded on demand — only the relevant file(s) are loaded per task — keeping context usage efficient.

### What's in SKILL.md

- **Persona**: Claude adopts the role of a NIST CSF advisor and cybersecurity risk management consultant
- **Output format matrix**: Maps each task type to a specific output format (gap table, profile document, roadmap, etc.)
- **CSF 2.0 six-function summary**: All functions with purpose and key outputs
- **5 core workflows**: Gap Assessment, Profile Creation, Implementation Roadmap, Cross-Framework Mapping, Policy Generation
- **CSF 2.0 vs 1.1 comparison table**: Key structural and content differences
- **Sector-specific guidance**: Financial services, healthcare, energy/OT, federal, manufacturing, SMB
- **Reference file loading logic**: Rules for when to load each reference file

### What's in the reference files

| File | Contents |
|------|----------|
| `csf-20-functions-categories.md` | All 6 functions with full category and subcategory lists, IDs, and descriptions |
| `csf-10-to-20-mapping.md` | Detailed CSF 1.1 → 2.0 subcategory migration table, new subcategories, removed subcategories, migration checklist |
| `csf-implementation-tiers.md` | Full Tier 1–4 definitions across three dimensions, diagnostic indicators per tier, advancement guidance |

### Inputs used to build the skill

- **NIST Cybersecurity Framework 2.0** (February 2024) — NIST CSWP 29 — functions, categories, subcategories, tiers, profiles
- **NIST Cybersecurity Framework 1.1** (April 2018) — for 1.1 support and migration guidance
- **NIST CSF 2.0 Quick Start Guides** — SMB, Enterprise Risk Management, Government guidance
- **NIST SP 800-53 Rev 5** — informative references for cross-framework mapping
- **ISO/IEC 27001:2022** — informative references for cross-framework mapping
- **CIS Controls v8** — informative references for cross-framework mapping
- **Sector-specific community profiles** — healthcare (HHS HPH), financial services (FFIEC CAT), energy (NERC CIP)

### Skill trigger phrases

The skill activates on any of the following topics (non-exhaustive):

`NIST CSF` · `Cybersecurity Framework` · `CSF 2.0` · `CSF 1.1` · `Govern function` · `Identify function` · `Protect function` · `Detect function` · `Respond function` · `Recover function` · `GV.OC` · `ID.AM` · `PR.AA` · `DE.CM` · `RS.MA` · `RC.RP` · `cybersecurity profile` · `current profile` · `target profile` · `implementation tiers` · `cybersecurity risk management strategy` · `CSF gap assessment` · `CSF profile` · `supply chain risk management` · `GV.SC` · `tier advancement` · `CSF 1.1 to 2.0`

---

## 6. Author

**Skill designed by:** Hemant Naik
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)
**Built with:** Claude (Anthropic) using the Claude Skills framework
**Date:** March 2026
**Skill version:** 1.9.0
**Standard coverage:** NIST Cybersecurity Framework 2.0 (February 2024) and NIST CSF 1.1 (April 2018)

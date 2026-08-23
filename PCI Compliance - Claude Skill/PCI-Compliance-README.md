# PCI DSS Compliance Skill

> A Claude skill for security, compliance, and engineering teams to navigate PCI DSS v4.0.1 — from CDE scoping and SAQ selection through gap assessments, QSA audit preparation, and remediation planning.

---

## 1. What Does the Skill Do?

The PCI DSS skill turns Claude into an expert PCI DSS compliance advisor and QSA-trained consultant. It provides structured, actionable guidance across the full PCI DSS compliance lifecycle — from defining cardholder data environment (CDE) scope and selecting the right SAQ type, through gap assessments against all 12 requirements, remediation planning, and QSA audit preparation.

The skill covers **PCI DSS v4.0.1** (June 2024 — current version), including all new requirements that became mandatory on March 31, 2025 — expanded MFA, payment page script integrity controls, phishing protection, automated log review, and targeted risk analysis. It also supports teams transitioning from the retired **PCI DSS v3.2.1**.

Outputs are tailored to the task: CDE scoping narratives, structured gap assessment tables with evidence requirements, SAQ selection decisions with rationale, control-level implementation guidance with QSA evidence tips, and full policy documents with PCI DSS control citations.

---

## 2. Intended Audiences

- **CISOs and Security Managers** overseeing PCI DSS compliance programmes for merchants or service providers
- **Compliance Analysts and GRC Teams** performing gap assessments, maintaining SAQ documentation, or preparing for annual QSA audits
- **Software Developers and Engineers** building payment systems, e-commerce applications, or integrations that touch cardholder data
- **Architects** designing or reviewing systems that interact with the CDE — network segmentation, tokenisation, P2PE, cloud environments
- **Small and Mid-Size Merchants** (Level 2–4) completing their annual SAQ and wanting expert guidance on what controls are needed and why
- **Service Providers** managing their PCI DSS Level 1 or Level 2 obligations and TPSP due diligence

---

## 3. Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| **CDE scoping** | "Help me scope our CDE. We have a cloud-based e-commerce platform that uses Stripe for payments. What's in scope?" |
| **SAQ selection** | "We're a Level 3 merchant accepting e-commerce payments only. We redirect customers to PayPal's hosted checkout. Which SAQ do we need?" |
| **Gap assessment** | "Run a PCI DSS v4.0.1 gap assessment. We're an SAQ D merchant. Here's our current environment..." |
| **v4.0 new requirements** | "What are the new requirements in PCI DSS v4.0 that became mandatory in March 2025?" |
| **MFA guidance** | "What does Req 8.4.2 mean for our internal staff accessing CDE systems?" |
| **Payment page scripts** | "How do we comply with Req 6.4.3 and 11.6.1 for our e-commerce payment page?" |
| **Policy generation** | "Write an Incident Response Plan aligned to PCI DSS Req 12.10." |
| **Remediation roadmap** | "We have 12 non-compliant controls from our last assessment. Help me build a remediation roadmap." |
| **TPSP management** | "What does PCI DSS require for managing third-party service providers?" |
| **Key management** | "How do we implement PCI DSS Req 3.7 for encryption key management?" |

---

## 4. How to Use the Skill

Once the skill is installed in Claude, it activates automatically whenever you ask about PCI DSS, payment card security, CDE, SAQs, ROC, QSA assessments, cardholder data, or related topics. You do not need to reference the skill by name.

### Tips for best results

**Specify your merchant or service provider level** — this determines your validation requirements (SAQ vs ROC) and tailors the guidance. For example:

> "We're a Level 2 merchant with 2 million transactions per year. We use a hosted payment page (redirect). What SAQ applies and what do we need to demonstrate?"

**Describe your payment environment** — channels (card-present, e-commerce, MOTO), third-party processors used, whether you store any cardholder data, and which systems are in scope.

**Reference specific requirements** — for targeted guidance, reference the requirement number (e.g., `Req 8.4.2`, `Req 6.4.3`) to get more focused and actionable responses.

### Example interaction

```
You:     We're a Level 3 e-commerce merchant. We use a JavaScript payment widget from
         Stripe embedded in our checkout page. Do we qualify for SAQ A?

Claude:  No — because you control the checkout page that hosts the Stripe widget and
         your JavaScript can affect how the widget behaves, you do not meet SAQ A
         criteria. You are likely SAQ A-EP. Key requirements include:
         - Req 6.4.3: Inventory all scripts on your payment page; implement
           Content Security Policy (CSP) or Sub-Resource Integrity (SRI)
         - Req 11.6.1: Deploy tamper detection for HTTP headers and payment page content
         - Req 11.3: Quarterly ASV scans
         Here is the full SAQ A-EP control scope and what you need to implement...
```

---

## 5. Skill Implementation Details

### Architecture

```
pci-compliance/
├── SKILL.md                           # Core skill logic and workflows
└── references/
    ├── pci-dss-requirements.md        # All 12 requirements with sub-controls and evidence
    ├── pci-dss-saq-guide.md           # SAQ selection guide, all SAQ types, ROC/AOC/ASV
    └── pci-dss-v4-changes.md          # v3.2.1 → v4.0/v4.0.1 migration guide and change log
```

### What's in SKILL.md

- **Persona**: Claude adopts the role of a PCI DSS compliance advisor and QSA-trained consultant
- **Output format matrix**: Maps each task type to a specific output format
- **CDE core concepts**: PAN, SAD, account data types, scope reduction strategies (tokenisation, P2PE, segmentation)
- **Merchant and service provider levels**: Validation requirements per level
- **Defined vs Customised Approach**: When each applies and what's required
- **SAQ quick reference**: All 8 SAQ types with ~control counts
- **5 core workflows**: CDE Scoping, Gap Assessment, SAQ Selection, Control Implementation, Policy Generation
- **v4.0 changes table**: Key differences from v3.2.1
- **Compensating controls**: How they work and when they apply

### What's in the reference files

| File | Contents |
|------|----------|
| `pci-dss-requirements.md` | All 12 requirements with sub-controls, QSA evidence requirements, and common gaps |
| `pci-dss-saq-guide.md` | SAQ selection decision tree, all 8 SAQ types with eligibility criteria, ROC/AOC/ASV/QSA/ISA reference |
| `pci-dss-v4-changes.md` | Version timeline, all new v4.0 requirements (future-dated → mandatory), key conceptual changes, migration checklist |

### Inputs used to build the skill

- **PCI DSS v4.0.1** (PCI SSC, June 2024) — all 12 requirements and sub-requirements
- **PCI DSS v4.0** (PCI SSC, March 2022) — including future-dated requirements and Customised Approach
- **PCI DSS Summary of Changes v3.2.1 to v4.0** (PCI SSC) — change log and migration reference
- **PCI DSS SAQ documents v4.0** — all 8 SAQ types with eligibility criteria
- **PCI SSC ROC Template v4.0.1** — assessment structure reference
- **PCI SSC Targeted Risk Analysis guidance** — TRA methodology and requirements

### Skill trigger phrases

`PCI DSS` · `PCI compliance` · `payment card` · `cardholder data` · `CDE` · `SAQ` · `ROC` · `AOC` · `QSA` · `ASV scan` · `PAN storage` · `SAD` · `tokenisation` · `P2PE` · `Requirement 1` through `Requirement 12` · `v4.0` · `merchant level` · `service provider` · `network segmentation` · `payment page` · `web skimming` · `Magecart` · `TPSP` · `key management` · `PCI scope`

---

## 6. Author

**Skill designed by:** Hemant Naik
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)
**Built with:** Claude (Anthropic) using the Claude Skills framework
**Date:** March 2026
**Skill version:** 1.8.0
**Standard coverage:** PCI DSS v4.0.1 (June 2024) and PCI DSS v4.0 (March 2022)

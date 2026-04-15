# PCI DSS Compliance Skill — All Versions

> A Claude skill for security, compliance, and engineering teams to navigate all versions of PCI DSS — from v1.0 (2004) through v4.0.1 (current, June 2024). Covers CDE scoping, SAQ selection, gap assessments, version migration planning, QSA audit preparation, and remediation — for any version of the standard.

---

## 1. What Does the Skill Do?

The PCI DSS skill turns Claude into an expert PCI DSS compliance advisor and QSA-trained consultant with knowledge spanning every published version of the standard, from the original v1.0 (December 2004) through the current **PCI DSS v4.0.1** (June 2024).

The skill provides structured, actionable guidance across the full PCI DSS compliance lifecycle:

- **CDE scoping** — defining what is in scope, scope reduction strategies (tokenisation, P2PE, segmentation)
- **SAQ selection** — decision logic for all 9 SAQ types, eligibility criteria, control counts
- **Gap assessments** — against v4.0.1 or any specified legacy version
- **Version migration** — v3.2.1 → v4.0.1 gap analysis, migration checklists, mandatory-from dates for all future-dated requirements
- **Control implementation** — per-requirement implementation guidance with QSA evidence tips
- **Policy generation** — full policy documents with PCI DSS citations and version applicability
- **Remediation roadmaps** — prioritised action tables with owner and timeline fields
- **Compensating controls and Customised Approach guidance**

**Defaults to v4.0.1** (current) unless the user specifies a version. Acknowledged historical versions (v1.x through v3.2.1) for legacy documentation, migration planning, and gap comparison.

---

## 2. Version Coverage

| Version | Year | Status | Notes |
|---------|------|--------|-------|
| v1.0 | 2004 | Retired | Historical reference; first unified standard |
| v1.1 | 2006 | Retired | PCI SSC formation; SAQ programme introduced |
| v1.2 | 2008 | Retired | WEP prohibited; wireless strengthened |
| v1.2.1 | 2009 | Retired | Minor corrections only |
| v2.0 | 2010 | Retired | Virtualisation guidance |
| v3.0 | 2013 | Retired | BAU security focus; SAQ B-IP and P2PE added |
| v3.1 | 2015 | Retired | SSL/TLS 1.0 deprecated |
| v3.2 | 2016 | Retired | MFA expansion; service provider requirements |
| v3.2.1 | 2018 | **Retired March 31, 2024** | Last v3 release; migration baseline |
| v4.0 | 2022 | Superseded | Customised Approach; future-dated requirements |
| **v4.0.1** | **2024** | **CURRENT** | All live assessments must use this version |

---

## 3. Intended Audiences

- **CISOs and Security Managers** overseeing PCI DSS compliance programmes
- **Compliance Analysts and GRC Teams** performing gap assessments, SAQ documentation, or QSA audit preparation
- **Software Developers and Engineers** building payment systems or integrations touching cardholder data
- **Architects** designing or reviewing CDE environments, network segmentation, tokenisation, P2PE, or cloud deployments
- **Merchants (all levels)** and **Service Providers** — including those migrating from v3.2.1 to v4.0.1
- **Small and Mid-Size Merchants** (Level 2–4) completing their annual SAQ

---

## 4. Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| **Version guidance** | "What PCI DSS version should we be using for our next assessment?" |
| **Migration planning** | "We completed our last assessment against v3.2.1. What do we need to do to move to v4.0.1?" |
| **v4.0 new requirements** | "What are the new requirements in PCI DSS v4.0 that became mandatory in March 2025?" |
| **CDE scoping** | "Help me scope our CDE. We have a cloud-based e-commerce platform using Stripe. What's in scope?" |
| **SAQ selection** | "We redirect customers to PayPal's hosted checkout. Which SAQ do we need?" |
| **Gap assessment (v4.0.1)** | "Run a PCI DSS v4.0.1 gap assessment against our SAQ D merchant environment." |
| **Legacy gap (v3.2.1)** | "What would our v3.2.1 assessment cover? We're comparing against v4.0.1 gaps." |
| **MFA guidance** | "What does Req 8.4.2 mean for our internal staff accessing CDE systems?" |
| **Payment page scripts** | "How do we comply with Req 6.4.3 and 11.6.1 for our e-commerce payment page?" |
| **Policy generation** | "Write an Incident Response Plan aligned to PCI DSS v4.0.1 Req 12.10." |
| **Remediation roadmap** | "We have 12 non-compliant controls. Help me build a remediation roadmap." |
| **Version comparison** | "Show me what changed between PCI DSS v3.0 and v3.2.1." |

---

## 5. How to Use the Skill

Once installed, the skill activates automatically whenever you ask about PCI DSS, any PCI DSS version, payment card security, CDE scoping, SAQ types, cardholder data, or related topics. You do not need to reference the skill by name.

### Tips for best results

**Specify your PCI DSS version** — the skill defaults to v4.0.1 (current) but can provide guidance for any version if specified.

**Specify your merchant or service provider level** — this determines your validation requirements (SAQ vs ROC).

**Describe your payment environment** — channels (card-present, e-commerce, MOTO), processors used, whether cardholder data is stored, which systems are in CDE scope.

### Example — Migration planning

```
You:     We completed our last PCI DSS assessment in January 2024 under v3.2.1.
         What changes do we face for our next assessment under v4.0.1?

Claude:  Your next assessment must use PCI DSS v4.0.1. Here are the main gaps
         from your v3.2.1 baseline:

         CRITICAL — Mandatory from March 31, 2025:
         - Req 8.4.2: MFA is now required for ALL access into the CDE, not just
           admin/remote. Any internal user accessing a CDE system must now use MFA.
         - Req 6.4.3: You must inventory all scripts on your payment pages,
           document authorisation for each, and implement integrity controls (CSP/SRI).
         - Req 5.4.1: An automated anti-phishing technical solution is required.
         - Req 10.4.1.1: Manual daily log review is no longer sufficient — you need
           an automated log review mechanism (SIEM or equivalent).
         - Req 8.3.6: Minimum password length increases from 7 to 12 characters.

         [Full migration checklist continues...]
```

### Example — Version history question

```
You:     What changed between PCI DSS v3.1 and v3.2?

Claude:  PCI DSS v3.2 (April 2016) made these changes from v3.1:
         1. MFA expanded: v3.2 added MFA for non-console admin access into the CDE
            for all personnel (was previously limited to remote access only).
            Deadline for existing implementations: February 1, 2018.
         2. Service provider-specific requirements added:
            - Req 10.8 (SP): Detect and report failures of critical security controls
            - Req 10.8.1 (SP): Respond to critical security control failures within 1 business day
            - Req 12.11 (SP): Quarterly reviews of personnel compliance with security procedures
            - Req 12.4.1 (SP): Executive oversight responsibility for CHD protection
         3. Appendix A3 (DESV) incorporated for designated entities
         4. Req 6.4.6: After significant changes, all relevant PCI DSS requirements
            must be re-implemented on changed systems
         Note: v3.1 and v3.2 are both retired. All current assessments use v4.0.1.
```

---

## 6. Skill Architecture

```
pci-dss/
├── SKILL.md                            # Core skill logic, all versions, all workflows
└── references/
    ├── pci-dss-requirements.md         # All 12 v4.0.1 requirements with sub-controls and evidence
    ├── pci-dss-saq-guide.md            # SAQ selection guide, all SAQ types, ROC/AOC/ASV
    ├── pci-dss-v4-changes.md           # v3.2.1 → v4.0/v4.0.1 complete change log + migration checklist
    ├── pci-dss-version-history.md      # All versions v1.0–v4.0.1 — changes, dates, thresholds
    └── pci-dss-v3-controls.md          # v3.2.1 complete control structure with v4.0.1 mapping
```

### What's covered in each file

| File | Contents |
|------|---------|
| `SKILL.md` | Claude persona, version guidance table, 7 core workflows (including migration and legacy), output format matrix, quick SAQ reference |
| `references/pci-dss-requirements.md` | All 12 v4.0.1 requirements with all sub-controls, evidence requirements, and common gaps |
| `references/pci-dss-saq-guide.md` | Full SAQ decision tree, per-SAQ eligibility criteria and control counts, ROC/AOC/ASV guidance |
| `references/pci-dss-v4-changes.md` | Complete change log v3.2.1 → v4.0/v4.0.1; all new mandatory requirements with effective dates; migration checklist |
| `references/pci-dss-version-history.md` | v1.0 through v4.0.1 — per-version changes, key milestone dates, authentication/cryptography thresholds by version, glossary |
| `references/pci-dss-v3-controls.md` | Complete v3.2.1 requirement structure with v4.0.1 cross-reference mapping for migration and legacy gap analysis |

---

## 7. Official Sources

- PCI Security Standards Council Document Library: https://www.pcisecuritystandards.org/document_library/
- PCI DSS v4.0.1 (June 2024): Available from PCI SSC Document Library
- PCI DSS v3.2.1 (May 2018): Available from PCI SSC Document Library (archived)
- PCI SSC SAQ Documents: https://www.pcisecuritystandards.org/document_library/?category=saqs


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
**Skill version:** 0.3.0
**Standard coverage:** PCI DSS v4.0.1 (June 2024) and PCI DSS v4.0 (March 2022)

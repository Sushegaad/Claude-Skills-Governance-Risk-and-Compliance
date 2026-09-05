# TSA Cybersecurity Compliance Skill

> A Claude skill for critical infrastructure owners and operators navigating TSA Security Directive requirements — covering pipelines, freight railroads, passenger rail, public transit, and bus operators under the current directives and the November 2024 NPRM.

---

## 1. What Does the Skill Do?

The TSA Compliance skill turns Claude into an expert TSA cybersecurity directive advisor for critical transportation infrastructure. It provides structured, actionable guidance for implementing and maintaining compliance with TSA Security Directives — from applicability determination and gap assessments through CIP/COIP drafting, Architecture Design Reviews, incident response planning, and IRP testing programmes.

The skill covers the **current TSA Security Directive series** in force as of 2026:
- **SD Pipeline-2021-01G** and **SD Pipeline-2021-02F** — pipeline operators
- **SD 1580-21-01E** — freight railroad operators
- **SD 1582-21-01E** — public transportation and passenger railroad operators

It also covers the **November 2024 NPRM** (Notice of Proposed Rulemaking) that would formalise current directives into permanent federal regulations, including its alignment with NIST CSF 2.0 and CISA Cross-Sector Cybersecurity Performance Goals (CPGs).

---

## 2. Intended Audiences

- **Critical Infrastructure Operators** — pipeline companies, freight railroads, passenger rail agencies, transit authorities, and bus operators designated as covered entities by TSA
- **CISOs and Security Teams** at transportation operators managing TSA directive compliance programmes
- **OT/ICS Security Engineers** implementing the four technical security domains — network segmentation, access controls, continuous monitoring, and patch management — in operational technology environments
- **Compliance and Regulatory Affairs Teams** responsible for submitting CIPs, CAPs, and incident reports to TSA and CISA
- **GRC Analysts** performing gap assessments against TSA directive requirements
- **Legal Counsel and Executives** (Accountable Executives) overseeing TSA compliance obligations
- **Consultants** supporting pipeline or rail clients through TSA directive implementation

---

## 3. Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| **Applicability check** | "We're a natural gas pipeline operator. Are we subject to TSA Security Directives? What does that mean for us?" |
| **Gap assessment** | "Run a gap assessment of our cybersecurity programme against TSA SD Pipeline-2021-02 requirements." |
| **CIP drafting** | "Help me draft a Cybersecurity Implementation Plan (CIP) for our pipeline OT environment." |
| **Incident reporting** | "We've detected ransomware on our IT network. It hasn't reached our SCADA yet. Do we need to report to CISA?" |
| **IRP testing** | "What IRP objectives do we need to test annually under the TSA directives, and how do we document them?" |
| **OT segmentation** | "How do we implement the required IT/OT network segmentation for our pipeline SCADA environment?" |
| **ADR guidance** | "Walk me through what an Architecture Design Review should cover for TSA compliance." |
| **CAP drafting** | "Help me build a Cybersecurity Assessment Plan to submit to TSA." |
| **NPRM impact** | "What will change for us if TSA's November 2024 NPRM is finalised as proposed?" |
| **CISA CPG alignment** | "How do CISA's Cross-Sector CPGs map to our TSA directive requirements?" |

---

## 4. How to Use the Skill

Once the skill is installed in Claude, it activates automatically whenever you ask about TSA Security Directives, TSA cybersecurity compliance, pipeline cybersecurity, rail or transit cybersecurity, OT/ICS security for transportation, CIP/COIP, CAP, incident reporting to CISA, or the 2024 NPRM. You do not need to reference the skill by name.

### Tips for best results

**Specify your sector and operator type** — pipeline (gas or liquid), freight rail, passenger rail, transit agency, or bus. Requirements vary by sector and directive series.

**Describe your current OT/IT environment** — whether you have IT/OT separation already in place, what SCADA/ICS systems you operate, and your current monitoring capabilities.

**Mention your directive status** — are you a designated covered entity? Which directive applies? Have you already submitted a CIP?

### Example interaction

```
You:     We're a natural gas pipeline operator. TSA just notified us that we're covered
         by SD Pipeline-2021-02. We have a SCADA system with HMIs, historians,
         and remote field RTUs. Our IT and OT networks share the same subnet.
         Where do we start?

Claude:  Given you're newly designated, here's a prioritised path:
         1. Designate your Cybersecurity Coordinator immediately — 24/7 contact
            for TSA and CISA. Submit contact info to TSA.
         2. Set up CISA incident reporting — ensure your team knows to report
            within 24 hours of identifying any CCS compromise.
         3. Address your highest-risk gap first: flat IT/OT network.
            This directly violates Domain 1. You need a firewall or DMZ
            between your corporate IT and SCADA network — this is the
            top remediation priority before CIP submission.
         4. Draft your CIP covering all four domains, IRP, ADR, and CAP.
         Here's what each CIP section needs to contain...
```

---

## 5. Skill Implementation Details

### Architecture

```
tsa-compliance/
├── SKILL.md                              # Core skill logic and workflows
└── references/
    ├── tsa-directives-overview.md        # All directive series, revision history, NPRM, framework mapping
    ├── tsa-crmp-requirements.md          # CRMP components (CIP, IRP, ADR, CAP) + four technical domains
    └── tsa-incident-reporting.md         # Incident reporting procedures, CISA contacts, timelines, ISAC info
```

### What's in SKILL.md

- **Persona**: Expert TSA cybersecurity compliance advisor specialising in transportation critical infrastructure
- **Output format matrix**: Maps task types to specific output formats
- **Directive coverage by sector**: Pipeline, freight rail, transit/passenger rail, aviation, bus
- **Critical Cyber System (CCS) definition**: IT/OT scope, designation methodology
- **Core requirements**: Incident reporting, Cybersecurity Coordinator, gap review
- **CRMP four components**: CIP/COIP, IRP, ADR, CAP — with all required elements
- **Four technical domains**: Network segmentation, access controls, monitoring, patch management
- **5 core workflows**: Applicability determination, gap assessment, CIP/COIP drafting, incident response, policy generation
- **2024 NPRM overview**: Proposed changes and alignment to NIST CSF 2.0 and CISA CPGs

### What's in the reference files

| File | Contents |
|------|----------|
| `tsa-directives-overview.md` | All active directive series (pipeline, freight rail, transit) with revision history; NPRM summary; key definitions; framework mapping table |
| `tsa-crmp-requirements.md` | Detailed CIP/COIP section requirements; IRP elements and testing requirements; ADR process; CAP elements; OT-specific implementation guidance for all four domains |
| `tsa-incident-reporting.md` | 24-hour CISA reporting obligation; CISA contacts; what qualifies as reportable; initial report format; follow-up reporting; ISAC list; CIRCIA overlap |

### Inputs used to build the skill

- **TSA Security Directives** — SD Pipeline-2021-01 and 02 series; SD 1580-21-01; SD 1582-21-01 (based on publicly available summaries and Federal Register notices)
- **TSA November 2024 NPRM** — "Enhancing Surface Transportation Cybersecurity"
- **CISA Cross-Sector Cybersecurity Performance Goals** — IT and OT CPG baselines
- **NIST CSF 2.0** — Referenced in TSA NPRM for annual profile-based evaluation
- **NIST SP 800-82** — Guide to ICS/OT Security (informative reference)
- **IEC 62443** — OT/ICS security standard (informative reference)
- **GAO reports** on TSA surface transportation cybersecurity (GAO-25-107947)

### Skill trigger phrases

`TSA Security Directive` · `SD Pipeline-2021` · `SD 1580-21-01` · `SD 1582-21-01` · `TSA cybersecurity` · `pipeline cybersecurity compliance` · `Critical Cyber Systems` · `CCS` · `Cybersecurity Coordinator` · `Cybersecurity Implementation Plan` · `CIP` · `COIP` · `CIRP` · `IRP testing` · `Architecture Design Review` · `ADR` · `Cybersecurity Assessment Plan` · `CAP` · `CRMP` · `CISA 24-hour reporting` · `OT segmentation TSA` · `rail cybersecurity directive` · `transit cybersecurity` · `TSA NPRM 2024` · `transportation critical infrastructure`

---

## 6. Important Note on SSI

TSA Security Directives are classified as **Sensitive Security Information (SSI)** under 49 CFR Part 1520. The full text of TSA directives is not publicly available. This skill is based on publicly disclosed summaries, Federal Register notices, TSA press releases, and DHS/CISA publications. Covered entities receive the actual directive text directly from TSA and should use the official directive as the authoritative source for compliance obligations.

---

## 7. Author

**Skill designed by:** Hemant Naik
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)
**Built with:** Claude (Anthropic) using the Claude Skills framework
**Date:** March 2026
**Skill version:** 1.9.0
**Standard coverage:** TSA SD Pipeline-2021-01G, SD Pipeline-2021-02F, SD 1580-21-01E, SD 1582-21-01E, November 2024 NPRM

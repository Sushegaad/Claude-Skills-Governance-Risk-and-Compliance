# Australian Information Security Manual (ISM) Skill for Claude

> **Disclaimer:** This skill provides informational guidance based on the Australian Signals
> Directorate (ASD) Information Security Manual (March 2026 edition). It does not constitute
> official ASD guidance or a formal security assessment. System authorisation decisions, IRAP
> assessment outcomes, and ATO sign-off are the responsibility of qualified Authorising Officials
> and ASD-certified IRAP assessors. For systems handling SECRET or TOP SECRET information,
> engage directly with ASD and relevant security-cleared personnel.

---

## 1. What Does the Skill Do?

This skill gives Claude comprehensive expertise in the **Australian Information Security Manual
(ISM)** — the ASD's authoritative cybersecurity framework for Australian government entities,
their contractors, and supply chains. The skill is built on the **March 2026 edition** of the ISM,
which is published by the Australian Signals Directorate (ASD) and available in OSCAL 1.1.2
machine-readable format. It applies to systems across all five classification levels: Non-Classified
(NC), OFFICIAL: Sensitive (OS), PROTECTED (P), SECRET (S), and TOP SECRET (TS).

The skill implements the ISM's six-step risk management cycle — Define, Select, Implement, Assess,
Authorise, and Monitor — and covers all 23 Cybersecurity Principles grouped across the four
functions: Govern (G1–G5), Protect (P1–P14), Detect (D1), and Respond (R1–R3). It navigates
all 22 guideline chapters spanning domains from Security Governance to Cryptography, covering
control selection by classification level using the NC/OS/P/S/TS applicability marking system,
where higher classification levels stack all lower-level controls.

The skill supports the full spectrum of ISM compliance workflows: gap analysis producing structured
control tables with status and evidence requirements; system authorisation pathway guidance from
System Security Plan (SSP) through Security Risk Assessment, IRAP Assessment, Plan of Action and
Milestones (POA&M), and Authorisation to Operate (ATO); IRAP assessment preparation with
artefact checklists and assessor criteria; ISM-aligned security documentation generation; and
Essential Eight vs ISM relationship clarification including Maturity Level (ML0–ML3) mapping.

It also integrates awareness of the complementary Protective Security Policy Framework (PSPF),
the IRAP programme administered by ASD, and the relationship between Essential Eight compliance
and full ISM compliance — a commonly misunderstood distinction that the skill addresses directly.

---

## 2. Intended Audiences

| Role | How They Use the Skill |
|------|----------------------|
| CISOs & CIOs (Government) | System authorisation strategy, risk-based control selection, IRAP preparation oversight |
| Cybersecurity Architects | Control mapping to system architecture, classification-level scoping, security objectives definition |
| IRAP Assessors | Assessment artefact checklists, control applicability by classification, re-assessment triggers |
| IT Security Managers | Gap analysis by domain, remediation roadmap, POA&M development |
| Government Contractors & Supply Chain | Determining applicable controls for contracted systems, PROTECTED system requirements |
| Security Documentation Specialists | SSP drafting, Incident Response Plan, Continuous Monitoring Plan, Change Management Plan |
| Essential Eight Programme Leads | ML0–ML3 target setting, Essential Eight to ISM control mapping, gap between E8 and full ISM |
| Procurement & Vendor Management | Supply chain security requirements, vendor ISM assessment scope |

---

## 3. Common Use Cases

### Gap Analysis

- "Perform an ISM gap analysis for our OFFICIAL: Sensitive system hosted in an Azure Government region."
- "We're building a PROTECTED system. Which ISM chapters and controls apply above the NC baseline?"
- "Identify all critical gaps in our current ISM control implementation for our on-premises mail platform."
- "Produce a gap table for ISM Chapter 7 (Information Technology Security) for our hybrid cloud environment."
- "We've completed Essential Eight ML2. What additional ISM controls do we still need to implement?"

### Control Guidance

- "Explain ISM control 1336 (multi-factor authentication) — what does it require and what evidence do auditors expect?"
- "What are the ISM requirements for event logging and how do they differ for NC vs OS vs PROTECTED systems?"
- "Which ISM controls govern patch management and what are the application and OS patching timeframes?"
- "Walk me through the ISM requirements for network segmentation for a PROTECTED system."
- "What does the ISM require for cryptographic key management? Reference the relevant control IDs."

### System Authorisation

- "Walk me through the complete system authorisation pathway for a new OFFICIAL: Sensitive SaaS platform."
- "What must a System Security Plan (SSP) include for a PROTECTED-level system?"
- "What is an Authorising Official and what risk acceptance decisions do they make?"
- "We've received our IRAP Assessment Report. What happens between the report and the ATO decision?"
- "What triggers a re-authorisation for a system that has already received an ATO?"

### IRAP Assessment Preparation

- "What artefacts must we prepare before engaging an IRAP assessor for our OS system?"
- "How do we verify that our chosen assessor is on the current ASD IRAP register?"
- "What is the assessment scope for a PROTECTED system and which controls will the assessor review?"
- "How often must systems be reassessed and what constitutes a 'significant change' triggering early reassessment?"
- "Draft an IRAP assessment preparation checklist for our team."

### Security Documentation Generation

- "Draft a System Security Plan (SSP) outline for our OFFICIAL: Sensitive web application."
- "Generate an ISM-aligned Incident Response Plan for a PROTECTED government system."
- "Create a Continuous Monitoring Plan template mapped to ISM requirements."
- "Draft a Change Management Plan that references relevant ISM chapters and control IDs."

### Essential Eight vs ISM

- "What is the relationship between the Essential Eight and the full ISM? Does E8 ML3 mean ISM compliant?"
- "Map the Essential Eight mitigations to their corresponding ISM control IDs."
- "We've been asked to achieve Essential Eight ML2. Does this satisfy our agency's ISM obligations?"
- "What are the Maturity Levels for Application Control and what does ML2 require in practice?"

---

## 4. How to Use the Skill

### Installation

1. Download `ism.skill` from this folder.
2. In Claude, go to **Settings → Skills**.
3. Click **Upload Skill** and select `ism.skill`.
4. The skill is now active across your Claude sessions.

### Triggering the Skill

The skill activates automatically when ISM-related topics arise. No special command is needed.
Example phrases that trigger it:

- *"ISM controls"* or *"Australian Information Security Manual"*
- *"ASD compliance"*, *"IRAP assessment"*, *"IRAP assessor"*
- *"PROTECTED system"*, *"OFFICIAL: Sensitive"*, *"system authorisation"*
- *"Essential Eight vs ISM"*, *"Maturity Level"*, *"ML2 Essential Eight"*
- *"System Security Plan"*, *"SSP"*, *"ATO authorisation"*
- *"NC/OS/P/S/TS classification"*, *"ISM chapter"*, *"ISM gap analysis"*
- *"Australian government cybersecurity"*, *"PSPF"*, *"ASD framework"*

### Example Prompts

```
We are a government agency migrating our case management system to AWS GovCloud. The system
handles OFFICIAL: Sensitive data. Perform an ISM gap analysis across the key chapters:
System Security Plan, access control, event logging, vulnerability management, and patch
management. Produce a gap table with: Control ID | Chapter | Description | Applicability |
Status | Evidence Needed | Gap Notes.
```

```
Walk me through the complete system authorisation pathway for a new PROTECTED-level
collaboration platform. List every required artefact, who is responsible for each,
the typical sequence of activities from scoping to ATO, and what triggers a re-assessment.
```

```
Draft an ISM-aligned System Security Plan (SSP) outline for an OFFICIAL: Sensitive
government web application hosted on-premises. Include all mandatory sections with
references to the relevant ISM chapters and control IDs. Include a document control block.
```

```
We are preparing for an IRAP assessment of our PROTECTED system in 90 days.
Generate a preparation checklist covering: required documentation artefacts, network
diagrams, evidence of implemented controls, assessor verification steps, and common
assessment findings we should proactively remediate.
```

```
Explain the difference between Essential Eight ML2 and full ISM compliance for a
PROTECTED system. Produce a mapping table showing: each Essential Eight mitigation |
corresponding ISM control IDs | what ISM controls for PROTECTED systems are NOT
covered by the Essential Eight.
```

---

## 5. Skill Implementation Details

### Architecture

```
ism/
├── SKILL.md                              # Core skill — ISM framework, 23 Cybersecurity
│                                         #   Principles, six-step risk management cycle,
│                                         #   control applicability markings, five core
│                                         #   workflows, key terminology
└── references/
    ├── guidelines-overview.md            # All 22 ISM guideline chapters with domain
    │                                     #   summaries and key control areas
    └── control-applicability.md          # Full control applicability framework,
                                          #   classification scoping rules (NC/OS/P/S/TS),
                                          #   Essential Eight to ISM control mapping
```

### What's in SKILL.md

- **Identity and scope**: Expert ISM compliance advisor for Australian government entities and supply chains; built on March 2026 ISM edition
- **Default classification**: OFFICIAL: Sensitive (OS) when no classification is specified
- **Response format table**: Output formats for gap analysis, control guidance, system authorisation, IRAP preparation, security documentation, and general questions
- **ISM Framework Structure**: 23 Cybersecurity Principles across four functions (Govern, Protect, Detect, Respond); 22 guideline chapters
- **Six-Step Risk Management Cycle**: Define → Select → Implement → Assess → Authorise → Monitor
- **Control Applicability Markings**: NC/OS/P/S/TS classification system and stacking rules
- **Core Workflows**: Gap analysis (including status definitions), system authorisation pathway, IRAP assessment preparation, security documentation generation, Essential Eight vs ISM
- **Key Terminology Table**: ASD, IRAP, SSP, ATO, PSPF, Essential Eight, security objectives, OSCAL
- **Reference file loading guidance**: When to load each reference file based on task type

### What's in the reference files

| File | Contents |
|------|----------|
| `guidelines-overview.md` | All 22 ISM guideline chapters: Security Governance, Information Security Documentation, Physical Security, Personnel Security, Information Technology Security, Software Development, Database Systems, Email, Network Management, Network Design, Cryptography, Gateway Security, Data Transfers, Evaluated Products, ICT Equipment, Media Management, System Hardening, System Management, System Monitoring, System Lifecycle, Outsourcing, and Specialised Systems — each with domain summary, key control areas, and common compliance gaps |
| `control-applicability.md` | Full control applicability framework by classification level; NC baseline controls (apply to all systems); OS, P, S, and TS stacking controls; classification scoping decision rules; Essential Eight to ISM control ID mapping for all 8 mitigations at each maturity level; guidance on formally excluding controls with documented justification |

### Inputs used to build the skill

| Source | Description |
|--------|-------------|
| ASD Information Security Manual (March 2026 edition) | Full framework including all 23 Cybersecurity Principles, 22 guideline chapters, and all control listings published in OSCAL 1.1.2 |
| ASD Essential Eight Explained | Maturity model (ML0–ML3) for all 8 mitigations |
| ASD Essential Eight to ISM Mapping | Official ASD mapping document linking E8 mitigations to ISM control IDs |
| Protective Security Policy Framework (PSPF) | Companion framework for classification markings and information handling |
| ASD IRAP Programme documentation | IRAP assessor criteria, assessment scope requirements, re-assessment triggers |

### Skill trigger phrases

`ISM controls`, `Australian Information Security Manual`, `ASD compliance`,
`IRAP assessment`, `IRAP assessor`, `infosec registered assessors program`,
`PROTECTED system`, `OFFICIAL: Sensitive`, `TOP SECRET system`, `SECRET system`,
`NC OS P S TS classification`, `system authorisation`, `Authorisation to Operate`,
`ATO government`, `System Security Plan`, `SSP ISM`, `Essential Eight vs ISM`,
`Essential Eight maturity level`, `ML0 ML1 ML2 ML3`, `ISM gap analysis`,
`ISM chapter`, `ISM guideline`, `Australian government cybersecurity`,
`PSPF security`, `ASD framework`, `cyber security principles ASD`,
`Govern Protect Detect Respond ASD`, `six-step risk management ISM`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.9.0 — September 2026

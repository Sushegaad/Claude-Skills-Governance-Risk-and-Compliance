# UK NIS (Network and Information Systems Regulations 2018) — Claude Skill

## Overview

This Claude skill provides expert compliance guidance for the **UK Network and Information Systems (NIS) Regulations 2018** (Statutory Instrument 2018/506). The skill covers the full scope of the Regulations including Operators of Essential Services (OES), Digital Service Providers (DSPs), the NCSC Cyber Assessment Framework (CAF), incident reporting obligations, Competent Authority requirements, and enforcement provisions.

The NIS Regulations 2018 came into force on **10 May 2018** as the UK implementation of EU Directive 2016/1148 (EU NIS Directive) and have been retained in UK domestic law following Brexit.

---

## What This Skill Covers

- **Scope determination** — Is your organisation an OES, DSP, or both?
- **CAF assessments** — All 14 CAF outcomes (Objectives A–D) with IGP and IPP
- **Gap analysis** — Structured gap assessment against the CAF
- **Incident reporting** — Regulation 11 (OES) and Regulation 13 (DSP) notification requirements
- **Competent Authorities** — Sector-specific CA mapping (Ofgem, CAA, ORR, DfT, DHSC, DWI, Ofcom, ICO)
- **Policy generation** — NIS compliance policies, risk registers, asset registers, incident response plans, supplier assessments, BCP
- **Enforcement** — Enforcement notices, penalty notices (up to £17 million), appeals
- **DSP requirements** — Security measures and ICO notification for cloud, marketplace, and search engine operators

---

## Skill Contents

```
uk-nis/
  SKILL.md                    — Main skill instruction file
  references/
    caf-objectives.md         — Complete CAF v3.2: all 14 outcomes with IGP and IPP
    incident-reporting.md     — OES and DSP notification templates and thresholds
    oes-sectors.md            — OES sector breakdown, CA mapping, designation criteria
    templates.md              — Policy, register, IRP, BCP, and assessment templates
```

---

## Installation

### Via Claude Code (plugin install)

```bash
claude plugin install ./plugins/uk-nis
```

### Manual (.skill file)

1. Download `uk-nis.skill` from this repository
2. Open Claude desktop
3. Go to Settings > Skills > Install from file
4. Select `uk-nis.skill`

---

## Usage Examples

**Scope determination:**
> "We are a water company operating treatment works and distribution networks. Are we in scope for UK NIS?"

**Gap assessment:**
> "Run a CAF gap assessment for our SCADA control systems."

**Incident reporting:**
> "We've detected ransomware on our electricity distribution control systems. What are our NIS reporting obligations?"

**Policy generation:**
> "Generate a NIS Compliance Policy for our NHS Trust."

**Competent Authority queries:**
> "Who is the Competent Authority for DNS service providers under UK NIS?"

**CAF guidance:**
> "Explain CAF outcome B2 — Identity and Access Control, including all Indicators of Good Practice."

---

## Legal Basis

- **Statutory Instrument 2018/506** — The Network and Information Systems (NIS) Regulations 2018
- **EU Directive 2016/1148** (original basis, now superseded by UK domestic law post-Brexit)
- **NCSC CAF v3.2** — Cyber Assessment Framework (primary technical standard for NIS compliance in the UK)

---

## Key Authorities

| Authority | Role |
|-----------|------|
| DSIT | Lead government department for NIS policy |
| NCSC | National technical authority; incident response support |
| Ofgem | CA for electricity and gas |
| CAA | CA for air transport |
| ORR | CA for rail transport |
| DfT/MCA | CA for road and maritime transport |
| DHSC/NHS England | CA for health |
| DWI | CA for drinking water |
| Ofcom | CA for digital infrastructure (IXP, DNS, TLD) |
| ICO | CA for all DSPs |

---

## Disclaimer

This skill provides informational guidance only and does not constitute legal advice. For formal NIS compliance conclusions, consult a qualified regulatory or legal specialist. The NIS Regulations should be read in their current form as maintained on legislation.gov.uk.

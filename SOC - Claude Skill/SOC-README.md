# SOC — Claude Skill

## Overview

This Claude skill provides expert guidance on the full AICPA **System and Organization Controls (SOC)**
reporting suite, covering:

- **SOC 1** (SSAE 18 AT-C Section 320) — Controls relevant to User Entities' Internal Control over Financial Reporting (ICFR)
- **SOC 3** — General use Trust Services Criteria attestation reports
- **SOC for Cybersecurity** — Entity-level cybersecurity risk management program examinations
- **SOC for Supply Chain** — Controls over production and distribution systems

> **Note:** SOC 2 (Trust Services Criteria — Security, Availability, Confidentiality, Processing Integrity, Privacy) is covered by a separate skill (`soc2.skill`).

---

## What This Skill Covers

### SOC 1 (SSAE 18)
- Report scoping: identifying services relevant to user entity ICFR
- System description requirements per AT-C Section 320
- Drafting control objectives
- Type 1 vs Type 2 selection
- Carve-out vs inclusive method for subservice organizations
- Complementary User Entity Controls (CUECs)
- Common audit findings and deficiencies
- User auditor guidance for reading and relying on SOC 1 reports

### SOC 3
- Structure of the general use report
- Relationship to SOC 2 (issued from the same examination)
- AICPA seal requirements and usage
- When SOC 3 is and is not sufficient
- Vendor procurement guidance for evaluating received SOC 3 reports

### SOC for Cybersecurity
- DC-4 description criteria (nine groups) — full detail
- Mapping DC-4 to CC1–CC9 Trust Services Criteria
- Readiness gap assessment template
- Management description writing guidance
- Comparison with SOC 2 and other cybersecurity frameworks

### SOC for Supply Chain
- DC-3 description criteria (eight areas) — full detail
- Applicable Trust Services Criteria (Security, Availability, Processing Integrity)
- Scoping for manufacturing, logistics, and agriculture organizations
- Complementary User Layer Entity Controls (CULECs)
- Sub-supplier identification and treatment
- OT/ICS cybersecurity considerations

---

## Authoritative Sources

All content in this skill is based on official AICPA publications:

| Document | Publisher | Relevance |
|---|---|---|
| SSAE 18 AT-C Section 105 | AICPA | Concepts common to all attestation engagements |
| SSAE 18 AT-C Section 205 | AICPA | Examination engagements |
| SSAE 18 AT-C Section 320 | AICPA | SOC 1 — service organization controls relevant to ICFR |
| AICPA Trust Services Criteria (2017, revised 2022) | AICPA | SOC 2, SOC 3, SOC for Cybersecurity measurement criteria |
| AICPA DC-3 (2020) | AICPA | SOC for Supply Chain description criteria |
| AICPA DC-4 (2017) | AICPA | SOC for Cybersecurity description criteria |
| AICPA SOC 1 Guide | AICPA | Performing and reporting on SOC 1 examinations |
| AICPA SOC 2 Guide | AICPA | Performing and reporting on SOC 2 examinations |
| AICPA SOC for Cybersecurity Guide | AICPA | Reporting on cybersecurity risk management programs |
| AICPA SOC for Supply Chain Guide | AICPA | Reporting on production and distribution system controls |

---

## Installation

### Via Claude Code Plugin Marketplace

1. Open Claude Code.
2. Navigate to **Settings > Skills**.
3. Search for `soc`.
4. Click **Install**.

### Manual Installation

1. Download `soc.skill`.
2. In Claude Code, navigate to **Settings > Skills > Install from file**.
3. Select the downloaded `soc.skill` file.

---

## Trigger Phrases

This skill is activated by questions or statements involving:

- "SOC 1", "SSAE 18", "SAS 70", "SSAE 16"
- "Internal control over financial reporting" / "ICFR"
- "Service organization report", "service auditor report"
- "Complementary user entity controls", "CUECs"
- "Carve-out method", "inclusive method"
- "Subservice organization"
- "SOC 3", "general use report", "AICPA seal"
- "SOC for Cybersecurity", "cybersecurity risk management program", "DC-4"
- "SOC for Supply Chain", "production and distribution system", "DC-3"
- "Which SOC report do we need?"
- "How are SOC reports different?"

---

## Version History

| Version | Date | Notes |
|---|---|---|
| 1.0.0 | 2026-04-16 | Initial release — SOC 1, SOC 3, SOC for Cybersecurity, SOC for Supply Chain |

---

## License

MIT License — see `LICENSE` in the repository root.

## Repository

[https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)

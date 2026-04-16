# TISAX — Claude Skill

> **Trusted Information Security Assessment Exchange** compliance advisor for automotive suppliers.

## Overview

TISAX (Trusted Information Security Assessment Exchange) is the de-facto information security
assessment standard for the global automotive supply chain. Developed by the **VDA**
(Verband der Automobilindustrie — German Association of the Automotive Industry) and
operated by the **ENX Association**, TISAX provides a recognized mechanism for automotive
suppliers to demonstrate their information security posture to OEM customers (Volkswagen,
BMW, Mercedes-Benz, Stellantis, Ford, Renault, and others).

This Claude Skill provides expert guidance for automotive suppliers seeking TISAX compliance and certification.

---

## What This Skill Does

When installed, this skill gives Claude deep knowledge of:

- **TISAX Labels** — Information (IS), Information High (IS-High), Prototype (PP), Strict Prototype (PP-Strict), Data (DP)
- **Assessment Levels** — AL1 self-assessment, AL2 on-site audit, AL3 enhanced on-site audit
- **VDA ISA 6.0** — The complete 16-chapter questionnaire structure with must criteria, maturity requirements, and evidence indicators
- **Maturity Model** — Levels 0–5 (Incomplete → Optimizing) with threshold requirements
- **ENX Portal** — Registration, scope creation, TISAX Assessment ID (TAI), result sharing
- **Audit Provider Engagement** — Finding licensed providers, engagement process, assessment phases
- **Gap Analysis** — Structured chapter-by-chapter assessment with corrective action planning
- **Prototype Protection** — Chapter 15 physical security requirements with Strict Prototype controls
- **Data Protection** — Chapter 16 GDPR-aligned data protection requirements
- **ISO 27001 Integration** — How TISAX relates to ISO 27001 and how to leverage existing certification

---

## TISAX Labels at a Glance

| Label | Assesses | Assessment Level | VDA ISA Chapters |
|-------|----------|-----------------|-----------------|
| Information (IS) | Information security — normal | AL 2 | 1–14 |
| Information High (IS-High) | Information security — high protection | AL 3 | 1–14 |
| Prototype (PP) | Prototype vehicle and component protection | AL 2 | 1–15 |
| Strict Prototype (PP-Strict) | Enhanced prototype protection | AL 3 | 1–15 (strict) |
| Data (DP) | Data protection (GDPR compliance) | AL 2 / AL 3 | 1–14 + 16 |

---

## VDA ISA 6.0 Chapter Structure

| Chapters | Domain |
|---------|--------|
| 1–2 | IS Policy and Organization |
| 3–4 | Asset Management and HR Security |
| 5–6 | Physical Security and IT Systems Management |
| 7–8 | Access Control and Cryptography |
| 9–10 | Communication Security and System Development |
| 11–12 | Supplier Relationships and Incident Management |
| 13–14 | Business Continuity and Compliance |
| 15 | Prototype and Test Vehicle Protection (conditional) |
| 16 | Data Protection / GDPR (conditional) |

---

## Who Needs TISAX?

TISAX is required by all major European automotive OEMs and is increasingly mandated globally. You likely need TISAX if:

- You are a direct supplier (Tier 1) to an automotive OEM
- You are a Tier 2+ supplier processing OEM confidential information
- You handle, store, transport, or work on prototype vehicles or pre-production components
- You process personal data as a data processor on behalf of an automotive OEM
- Your contract references TISAX, VDA ISA, or ENX
- You are expanding your automotive customer base in Europe

---

## Typical TISAX Journey

```
1. Review OEM contract — identify TISAX label and AL requirement
2. Register on ENX portal — create company account, pay fee
3. Define Assessment Scope — what locations, systems, activities are in scope
4. Receive TISAX Assessment ID (TAI)
5. Conduct internal gap analysis against VDA ISA 6.0
6. Remediate identified gaps (typically 3–9 months)
7. Engage a licensed TISAX Audit Provider
8. Conduct assessment (AL2 or AL3 on-site audit)
9. Resolve any non-conformances
10. Labels issued; results published on ENX portal
11. Share results with OEM customer(s) via ENX portal
12. Maintain controls; reassess every 3 years
```

---

## Example Prompts

Once installed, try asking Claude:

- *"Which TISAX label do I need if my company handles VW Group engineering documents and prototype components?"*
- *"Walk me through a gap analysis for TISAX Chapter 7 (Access Control and Authentication)."*
- *"What are the must criteria for TISAX Prototype protection under Chapter 15?"*
- *"How do I register on the ENX portal and create an assessment scope?"*
- *"What is the difference between TISAX and ISO 27001, and can I use my ISO 27001 certification for TISAX?"*
- *"Generate a TISAX evidence preparation checklist for an AL 2 assessment."*
- *"What are the Strict Prototype controls required in Chapter 15 for suppliers working on flagship vehicle launches?"*
- *"Our TISAX label expires in 6 months — what are the steps for reassessment?"*
- *"How do I share my TISAX results with BMW and Mercedes-Benz on the ENX portal?"*

---

## Reference Files

This skill includes five detailed reference documents:

| File | Contents |
|------|----------|
| `isa-requirements.md` | VDA ISA 6.0 chapter-by-chapter requirements with must criteria and evidence examples (Chapters 1–16) |
| `assessment-process.md` | Full assessment lifecycle: ENX registration → scope → Audit Provider → assessment → labels → sharing |
| `label-guide.md` | Detailed label selection guidance, OEM-specific requirements, multi-label assessments, sharing process |
| `prototype-protection.md` | Chapter 15 detailed requirements for Prototype and Strict Prototype labels |
| `gap-analysis-template.md` | Structured chapter-by-chapter gap assessment table and corrective action plan template |

---

## Key Regulatory Sources

| Source | Description |
|--------|-------------|
| VDA ISA 6.0 | Download from https://www.vda.de/en/education-and-training/isa |
| ENX TISAX Portal | https://enx.com/en-US/TISAX/ |
| ENX registration | https://enx.com |
| GDPR (for Data label) | https://gdpr-info.eu / EU 2016/679 |

---

## Installation

### Via Claude Code (recommended)

```bash
claude mcp add tisax-compliance
```

Or add the plugin manually by copying the `plugins/tisax/` directory to your Claude plugins
folder following the standard installation procedure in [INSTALLATION.md](../INSTALLATION.md).

### Using the .skill file

Download `TISAX - Claude Skill/tisax.skill` and install via the Claude skills manager.

---

## TISAX vs ISO 27001

| Aspect | TISAX | ISO 27001 |
|--------|-------|-----------|
| Industry | Automotive supply chain | General-purpose, all industries |
| Governing body | VDA + ENX Association | ISO / IEC |
| Assessment method | Third-party audit (AL2/AL3) | Third-party certification audit |
| Result visibility | Private — shared on ENX portal | Public certificate |
| Questionnaire | VDA ISA 6.0 (prescriptive) | Annex A controls + ISMS (flexible) |
| Prototype protection | Yes — Chapter 15 | Not covered |
| Data protection | Yes — Chapter 16 (GDPR) | Partially (privacy controls) |
| Validity | 3 years | 3 years (annual surveillance) |

Many automotive suppliers pursue **both** — TISAX for OEM contractual compliance and ISO 27001 for general market credibility. ISO 27001 certification provides significant overlap with TISAX requirements but does not satisfy TISAX on its own.

---

## License

MIT — see [LICENSE](../LICENSE) for details.

## Contributing

Contributions welcome via pull request to the [main repository](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance).

## Disclaimer

This skill provides compliance guidance based on publicly available information about TISAX
and the VDA ISA framework. Always refer to official VDA and ENX sources for authoritative
requirements. Download the official VDA ISA questionnaire at https://www.vda.de.
Requirements may change between VDA ISA versions; verify which version is current before
beginning your assessment.

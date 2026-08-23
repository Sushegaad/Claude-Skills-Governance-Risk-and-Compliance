# NZISM Compliance Skill

> A Claude skill for New Zealand government agencies and their supply chains to navigate the New Zealand Information Security Manual (NZISM) — from gap analysis and system certification through to control implementation and policy generation.

---

## 1. What Does the Skill Do?

The NZISM skill turns Claude into an expert New Zealand Information Security Manual (NZISM) advisor. It provides structured, authoritative guidance across the full lifecycle of information security management for NZ government — from initial gap assessment through to formal Certification & Accreditation (C&A) and ongoing monitoring.

The NZISM is published and maintained by the **Government Communications Security Bureau (GCSB)** through its **National Cyber Security Centre (NCSC NZ)**. It is the mandatory information security framework for New Zealand government agencies, covering controls across 18+ security domains and supporting the NZ Government Information Classification System (ISCS) from Unclassified through Top Secret.

Outputs are tailored to the task: structured gap analysis tables, step-by-step C&A pathways, full policy documents with NZISM control references, classification decision guides, control implementation plans, and handling requirement summaries.

---

## 2. Intended Audiences

This skill is designed for **NZ government agencies, contractors, and their supply chains**. It is most useful for:

- **Chief Information Security Officers (CISOs)** and **Agency Security Managers** overseeing NZISM compliance, system certification, or accreditation
- **Compliance analysts** conducting gap assessments, preparing SSPs, or maintaining the risk register
- **ICT teams and system architects** seeking control implementation guidance for specific domains (network, access control, cryptography, etc.)
- **Third-party suppliers and contractors** to NZ government who must meet NZISM-equivalent obligations under contract
- **Internal and external assessors** preparing for or conducting Certification & Accreditation assessments
- **Procurement officers** assessing supplier security posture before engagement

---

## 3. Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| **Gap analysis** | "Run a gap analysis of our agency's current controls against NZISM for a Restricted system." |
| **C&A preparation** | "What documents do I need to prepare for Certification & Accreditation of a Restricted system?" |
| **Policy generation** | "Write an Access Control Policy mapped to NZISM controls." |
| **Control guidance** | "How do I implement NZISM audit logging controls for a system handling In-Confidence data?" |
| **Classification decision** | "We have a system that processes employee performance data and some Cabinet-related documents. What classification level should we assign?" |
| **Cloud risk assessment** | "We want to move our Restricted data to AWS NZ region. What NZISM controls and approvals apply?" |
| **Supplier obligations** | "What security obligations must we contractually impose on a SaaS vendor processing Restricted government data?" |
| **Cryptography guidance** | "What encryption standards does NZISM require for data at rest on a Confidential system?" |
| **Incident reporting** | "We've had a data breach involving Restricted government records. What are our NZISM reporting obligations?" |
| **Checklist** | "Give me the mandatory agency obligations checklist from the NZISM." |

---

## 4. How to Use the Skill

Once the skill is installed in Claude, it activates automatically whenever you ask about the NZISM, NZ government information security, GCSB/NCSC NZ compliance, or related topics. You do not need to reference the skill by name.

### Tips for best results

**State the classification level** — NZISM controls vary significantly between Unclassified, Restricted, and Confidential. Telling Claude which level you're working with produces more targeted guidance. For example:

> "We're building a new Restricted system for an NZ government agency. What controls do we need?"

**Describe your system context** — agency type, system purpose, hosting environment (on-premises, NZ cloud, offshore), and number of users all help the skill tailor its output.

**Name the control domain** — for implementation guidance, specifying the domain (e.g., "audit and logging", "network security", "cryptography") produces more actionable responses.

**Be specific about the workflow** — the skill can help with gap analysis, policy writing, C&A preparation, supplier assessments, and classification decisions. Telling it which workflow you need helps focus the output.

---

## 5. Skill Implementation Details

```
NZISM - Claude Skill/
├── nzism.skill                  ← Install this file in Claude
└── NZISM-README.md              ← This file

plugins/nzism/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── nzism/
│       ├── SKILL.md             ← Core skill instructions
│       └── references/
│           ├── control-groups.md         ← All 18 NZISM control sections
│           └── classification-framework.md ← Classification levels & control applicability
└── nzism.skill
```

**Framework:** New Zealand Information Security Manual (NZISM), published by GCSB/NCSC NZ

**Key topics covered:**
- NZ Government Information Classification System (ISCS) — Unclassified through Top Secret
- All 18+ NZISM control sections (Governance, Physical, Personnel, Network, Access Control, Cryptography, Audit, Cloud, Mobility, and more)
- Certification & Accreditation (C&A) process — SSP, risk assessment, ATO
- Mandatory agency obligations and documentation
- Third-party and supply chain security obligations
- Cloud computing guidance and data residency requirements
- Relevant NZ legislation: Privacy Act 2020, Public Records Act 2005, Protective Security Requirements (PSR)

**Trigger phrases:** NZISM, NZ government security, GCSB compliance, NCSC NZ, Restricted system, Confidential system, NZ classification, agency security policy, system certification, IRAP NZ, C&A NZ, government cybersecurity NZ

---

## 6. Author

**Hemant Naik**
Email: hemant.naik@gmail.com
GitHub: [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)
Website: [sushegaad.github.io/Claude-Skills-Governance-Risk-and-Compliance](https://sushegaad.github.io/Claude-Skills-Governance-Risk-and-Compliance/)
License: MIT

---

*Skill version: 1.8.0 — August 2026*

# ISO 27017 — Claude Skill

> ISO/IEC 27017:2015 Cloud Security Controls Advisor for Claude

This Claude skill provides expert guidance on **ISO/IEC 27017:2015** — the international code of
practice for information security controls specific to cloud computing environments. The skill
supports both cloud service providers (CSPs) and cloud service customers (CSCs).

---

## What This Skill Does

The ISO 27017 skill enables Claude to act as an expert cloud security compliance advisor with
deep knowledge of:

- The 7 additional cloud-specific CLD controls introduced by ISO 27017
- ISO 27002:2013 controls with cloud-specific implementation guidance for CSPs and CSCs
- Shared responsibility models across IaaS, PaaS, and SaaS service models
- Cloud service agreement security requirements and review
- Virtual machine hardening and virtualisation security
- Cloud asset management including data return and deletion
- Cloud administrator operational security
- Cloud monitoring and incident response

---

## Trigger Phrases

This skill activates for questions including:

- "ISO 27017", "ISO/IEC 27017", "cloud security controls"
- "shared responsibility model" in a compliance or cloud context
- Questions about CLD controls (CLD.6.3.1, CLD.8.1.5, CLD.9.5.1, CLD.9.5.2, CLD.12.1.5, CLD.12.4.5, CLD.13.1.4)
- "cloud service agreement security", "data deletion in cloud", "cloud asset removal"
- "virtual machine hardening", "VM security", "tenant isolation", "hypervisor security"
- "cloud administrator security", "cloud monitoring requirements"
- "gap analysis" for cloud security controls
- "CSP obligations", "CSC responsibilities", "cloud security policy"

---

## Standard Overview

| Attribute | Detail |
|-----------|--------|
| Full title | ISO/IEC 27017:2015 — Code of practice for information security controls based on ISO/IEC 27002 for cloud services |
| Published | December 2015 |
| Issuing body | ISO/IEC JTC 1/SC 27 |
| Based on | ISO/IEC 27002:2013 |
| Cloud-specific additions | 7 additional CLD controls |
| Applicability | Cloud Service Providers (CSPs) and Cloud Service Customers (CSCs) |
| Companion standards | ISO/IEC 27001, ISO/IEC 27002, ISO/IEC 27018 |

---

## The 7 Cloud-Specific Controls (CLD)

| Control | Name | Applies To |
|---------|------|------------|
| CLD.6.3.1 | Shared roles and responsibilities | Both CSP and CSC |
| CLD.8.1.5 | Removal or return of cloud service customer assets | Both CSP and CSC |
| CLD.9.5.1 | Segregation in virtual computing environments | CSP (primary) |
| CLD.9.5.2 | Virtual machine hardening | Both CSP and CSC |
| CLD.12.1.5 | Administrator's operational security | CSP (primary) |
| CLD.12.4.5 | Monitoring of cloud services | Both CSP and CSC |
| CLD.13.1.4 | Alignment of security management for virtual and physical networks | CSP (primary) |

---

## Skill Contents

```
iso27017/
├── SKILL.md                          Main skill definition and workflows
└── references/
    ├── cloud-controls.md             Detailed guidance on all 7 CLD controls
    ├── iso27002-cloud-guidance.md    37 ISO 27002 controls with cloud-specific guidance
    ├── shared-responsibility.md      Shared responsibility matrix: IaaS/PaaS/SaaS
    └── templates.md                  Gap analysis, CSA review, policy, and hardening templates
```

---

## Installation

### Via Claude Code (recommended)

```bash
claude mcp install iso27017.skill
```

### Manual Installation

1. Download `iso27017.skill`
2. In Claude Code, run: `claude skills install ./iso27017.skill`
3. The skill will be available immediately

---

## Usage Examples

**Gap analysis:**
> "Perform an ISO 27017 gap analysis for our AWS environment. We are a cloud service customer
> using IaaS services."

**Shared responsibility:**
> "Map the shared responsibility for ISO 27017 controls between us (the CSC) and our SaaS provider."

**CLD control guidance:**
> "Explain what CLD.12.1.5 requires and how we should implement it for our cloud administrators."

**Cloud service agreement review:**
> "Review this cloud service agreement and identify what's missing for ISO 27017 compliance."

**Policy generation:**
> "Draft a cloud security policy for our organisation aligned to ISO 27017."

**VM hardening:**
> "What does CLD.9.5.2 require for virtual machine hardening? Give me implementation steps."

---

## Relationship to Other Standards

| Standard | Relationship |
|----------|-------------|
| ISO/IEC 27001:2022 | ISMS requirements framework — ISO 27017 provides cloud-specific control guidance to implement within an ISO 27001 ISMS |
| ISO/IEC 27002:2013 | Base control set — ISO 27017 supplements these controls with cloud-specific guidance |
| ISO/IEC 27018:2019 | Companion standard — extends ISO 27002 specifically for processing PII in cloud |
| ISO/IEC 27001 + 27017 | Organisations seeking cloud-focused ISMS typically implement both; ISO 27001 certification with ISO 27017 extension |

---

## Important Notes

- ISO 27017 is a **code of practice**, not a certification standard. Organisations are certified
  against ISO 27001, with ISO 27017 providing additional implementation guidance for cloud.
- The standard uses ISO 27002:2013 control numbering. When ISO 27002 was revised in 2022,
  ISO 27017 was not simultaneously updated to align with the new numbering.
- Always seek professional legal and compliance advice before finalising cloud service agreements
  or submitting compliance assessments.

---

## License

MIT — See [LICENSE](../LICENSE) in the repository root.

## Author

Hemant Naik — [Sushegaad GRC Skills](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)

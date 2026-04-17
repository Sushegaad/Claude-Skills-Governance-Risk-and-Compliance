# ISO/IEC 27018 Compliance Skill for Claude

A comprehensive Claude skill that provides expert guidance on ISO/IEC 27018 — the international standard for protecting personally identifiable information (PII) in public cloud environments where the cloud provider acts as a PII processor.

> **Disclaimer:** This skill provides informational guidance based on publicly available information about ISO/IEC 27018. It does not constitute legal advice. For formal compliance determinations, legal interpretations, or procurement of the official standard text, consult qualified legal and compliance professionals and obtain the official ISO/IEC 27018 standard from ISO or your national standards body.

---

## What Does This Skill Do?

The ISO/IEC 27018 Compliance Skill transforms Claude into an expert cloud PII compliance advisor, providing structured guidance across the full range of obligations that apply to public cloud service providers processing personally identifiable information on behalf of their customers.

The skill covers **ISO/IEC 27018:2025 (third edition)** — the current version, aligned with ISO/IEC 27002:2022 — and also addresses **ISO/IEC 27018:2019 (second edition)** for organisations working with the previous version. It understands all Annex A extended controls, their relationship to ISO 29100 privacy principles, and how ISO 27018 maps to GDPR, ISO 27701, ISO 27017, and ISO 27001.

At a high level, the skill does five things:

1. **Gap analysis against ISO 27018 Annex A** — Assesses where a cloud provider stands against all extended PII controls, producing structured gap tables with status, evidence needed, and priority remediation steps.

2. **Policy and document generation** — Drafts ready-to-use documents including PII Protection Policies, Data Processing Agreement (DPA) addenda, sub-processor agreement schedules, government request handling procedures, breach notification letters, and end-of-contract PII disposal confirmations.

3. **Control implementation guidance** — Provides concrete, actionable guidance on implementing any ISO 27018 obligation, including technical safeguards, organisational measures, sub-processor management, and staff training.

4. **Compliance mapping** — Maps ISO 27018 obligations to GDPR articles, ISO 27701 controls, ISO 27017 controls, ISO 27001 Annex A, and ISO 29100 privacy principles; also covers alignment with national privacy laws including UK GDPR, CCPA, LGPD, DPDP Act, and others.

5. **Operational procedures** — Provides step-by-step procedures for government request handling, sub-processor due diligence, data residency transparency, customer audit support, and PII incident management.

The skill is backed by four detailed reference files covering Annex A controls, PII protection implementation guidance, document templates, and compliance mapping — loaded selectively based on what the question requires.

---

## Standard Overview

| Attribute | Details |
|-----------|---------|
| Full name (2025) | ISO/IEC 27018:2025 — Information security, cybersecurity and privacy protection — Guidelines for protection of personally identifiable information (PII) in public clouds acting as PII processors |
| Current edition | Third edition, August 2025 |
| Previous edition | Second edition, 2019 (withdrawn) |
| Published by | ISO/IEC JTC 1/SC 27 |
| Base standard | ISO/IEC 27002:2022 (third edition) |
| Core relationship | Extends ISO 27002 with PII-specific controls; implements ISO 29100 privacy principles in cloud context |

---

## Who Is This Skill For?

This skill is designed for organisations and practitioners involved in cloud privacy compliance:

| Audience | How They Use the Skill |
|----------|----------------------|
| **Cloud Service Providers (CSPs)** | Understand and implement ISO 27018 obligations; draft DPA terms; manage sub-processor programmes |
| **Privacy Officers / DPOs** | Gap analysis, policy generation, GDPR Article 28 compliance support, audit evidence preparation |
| **Security Teams at CSPs** | Technical safeguard guidance for PII encryption, access control, logging, incident response |
| **Legal Teams** | Draft data processing agreement clauses; understand government request obligations; advise on sub-processor contracts |
| **Cloud Customers (Controllers)** | Understand what CSP obligations ISO 27018 imposes; questions to ask in vendor assessments; DPA review guidance |
| **Compliance Managers** | Compliance mapping to GDPR, ISO 27701, regional laws; certification strategy |
| **Auditors and Assessors** | Gap analysis frameworks, evidence requirements, audit question prompts |
| **Software Developers at CSPs** | Privacy by design guidance; technical safeguards; temporary file PII handling; deletion API requirements |

---

## Common Use Cases

### Gap Analysis
- "Perform an ISO 27018 gap analysis for our IaaS platform"
- "We're implementing ISO 27018 — where should we start?"
- "Identify gaps in our sub-processor management programme against ISO 27018"
- "We have ISO 27001 — what additional controls does ISO 27018 require?"

### Policy and Document Generation
- "Draft an ISO 27018-compliant PII Protection Policy"
- "Generate a data processing agreement addendum based on ISO 27018 obligations"
- "Create a sub-processor agreement schedule with ISO 27018 terms"
- "Write a government request handling procedure"
- "Draft a PII disposal confirmation letter for a customer whose contract is ending"

### Control Implementation Guidance
- "How do I implement 'no use of PII for marketing purposes' under ISO 27018?"
- "What technical controls do I need for PII encryption under ISO 27018?"
- "How should we handle government requests for customer data under ISO 27018?"
- "What does ISO 27018 require for our sub-processor programme?"
- "How do I support customer audit rights under ISO 27018?"

### Compliance Mapping
- "How does ISO 27018 relate to GDPR Article 28?"
- "Map ISO 27018 to ISO 27701 — what additional controls does 27701 require?"
- "How does ISO 27018 compare to ISO 27017?"
- "Does ISO 27018 compliance support LGPD compliance in Brazil?"
- "We have ISO 27001 — what's the path to demonstrating ISO 27018 compliance?"

### Operational Procedures
- "We received a request from law enforcement for customer data. What do we do?"
- "A customer contract is ending — walk me through PII return and deletion obligations"
- "We need to add a new sub-processor — what's the process?"
- "We've had a security incident involving customer PII — what must we do?"

### Certification and Evidence
- "What certifications can demonstrate ISO 27018 compliance?"
- "What evidence should we prepare for customer audits of our ISO 27018 compliance?"
- "What does a CSP need to show for GDPR Article 28 compliance?"

---

## How to Use the Skill

Once installed in Claude, the skill activates automatically whenever you ask about ISO 27018, cloud PII processing obligations, PII processor requirements, or related compliance topics. You do not need to reference the skill by name.

### Tips for Best Results

**Specify your role** — are you a cloud service provider (CSP), a cloud customer (controller), or both? This helps the skill tailor its guidance correctly.

**Specify the version** — are you working with ISO 27018:2025 or ISO 27018:2019? The skill defaults to 2025 if not specified.

**Provide context about your service** — what type of cloud service (IaaS, PaaS, SaaS)? What categories of PII are processed? What regions are involved? What existing certifications does the organisation hold?

**Be specific about the task** — ask for a gap analysis, a specific document, or guidance on a specific control. The skill handles complex multi-step tasks but produces more useful outputs when the request is focused.

**Example prompts:**
> "We're a SaaS company processing HR data for our enterprise customers in the EU. Run an ISO 27018 gap analysis and tell us our top five remediation priorities."

> "Draft an ISO 27018-aligned Data Processing Addendum clause covering sub-processor obligations, government request handling, and PII deletion at contract end."

> "We use three sub-processors for our cloud platform. Walk me through what ISO 27018 requires for our sub-processor management programme."

---

## What the Skill Does Not Do

- It does not provide legal advice; always consult qualified legal professionals for formal compliance determinations
- It does not access your live systems or assess your actual security configuration
- It does not provide the full text of the ISO/IEC 27018 standard — to obtain the official standard, purchase it from ISO (iso.org) or your national standards body
- It does not fully substitute for specialist GDPR legal advice, particularly for obligations that fall on PII controllers (rather than processors)
- It does not cover ISO 27018 compliance for private cloud or on-premises environments (the standard applies specifically to public cloud PII processors)

---

## Skill Contents

This skill package includes:

| Component | Description |
|-----------|-------------|
| `SKILL.md` | Core skill instructions and framework |
| `references/annex-a-controls.md` | Complete Annex A extended control set by privacy principle |
| `references/pii-protection-guidance.md` | Technical safeguards, organisational measures, sub-processor management |
| `references/templates.md` | 10 ready-to-use document templates |
| `references/compliance-mapping.md` | ISO 27018 mappings to GDPR, ISO 27701, ISO 27017, ISO 27001, ISO 29100, and regional laws |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | April 2026 | Initial release — covers ISO 27018:2025 and ISO 27018:2019 |

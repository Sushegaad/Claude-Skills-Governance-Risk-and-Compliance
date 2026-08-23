# HIPAA Compliance Skill for Claude

A comprehensive Claude skill that provides expert HIPAA compliance guidance across four domains: document review, policy generation, technical safeguards, and plain-language education.

> ⚠️ **Disclaimer:** This skill provides informational guidance only and does not constitute legal advice. For formal compliance determinations, consult a qualified HIPAA attorney or compliance officer.

---

## What Does This Skill Do?

The HIPAA Compliance Skill transforms Claude into a knowledgeable HIPAA advisor capable of handling the full range of compliance questions that arise in healthcare and health-adjacent organizations.

At a high level, the skill does four things:

1. **Reviews content and documents for HIPAA compliance issues** — It analyzes policies, system architectures, workflows, and vendor agreements, producing structured findings with rule citations, risk levels (High / Medium / Low), and prioritized remediation steps.

2. **Generates HIPAA-compliant policies, notices, and templates** — It produces ready-to-use documents including Notices of Privacy Practices (NPP), Business Associate Agreements (BAA), authorization forms, breach response plans, risk assessment templates, and workforce training acknowledgments — all with inline CFR citations.

3. **Advises on technical safeguards for software systems** — It guides developers and architects through HIPAA's Administrative, Physical, and Technical Safeguard requirements, with specific guidance for modern cloud environments (AWS, Azure, GCP), API security, encryption standards, audit logging, and DevOps practices.

4. **Explains HIPAA rules in plain language** — It translates dense regulatory text into accessible explanations for any audience, always leading with a plain-language summary before diving into regulatory detail.

The skill is backed by four detailed reference files covering the Privacy Rule, Security Rule, Breach Notification Rule, and a full library of document templates — loaded selectively based on what the question actually requires.

---

## Intended Audiences

This skill is designed to serve a broad range of users who interact with Protected Health Information (PHI) in their work:

| Audience | How They Use the Skill |
|----------|----------------------|
| **Software Developers** | Get actionable guidance on encryption standards, access controls, audit logging, cloud configuration, and FHIR/API security for systems that handle ePHI |
| **Healthcare Compliance Officers** | Review policies and procedures for gaps, generate required documents (NPP, BAA, risk assessments), and get CFR-cited answers to compliance questions |
| **Legal & Privacy Teams** | Understand HIPAA obligations for new vendor relationships, draft or review BAAs, assess breach notification obligations |
| **General Business Staff** | Understand what HIPAA requires in plain language, know what counts as PHI, and learn how to handle patient information appropriately |
| **Healthcare IT & Security Teams** | Assess systems against the Security Rule, build out risk analysis documentation, respond to security incidents, and evaluate breach notification obligations |
| **Startups & Digital Health Companies** | Understand whether HIPAA applies to them, what covered entity vs. business associate status means, and what baseline compliance looks like |

---

## Common Use Cases

### Compliance Review
- "Review our patient intake form for HIPAA compliance"
- "Is our current EHR data-sharing workflow HIPAA compliant?"
- "Audit our AWS architecture — we store ePHI in S3 and RDS"
- "We're onboarding a new billing vendor. What HIPAA obligations apply?"
- "Review this draft BAA — are there any missing required provisions?"

### Document & Policy Generation
- "Generate a Notice of Privacy Practices for our clinic"
- "Draft a Business Associate Agreement for our cloud storage vendor"
- "Create an internal HIPAA Privacy Policy for our workforce"
- "Write a HIPAA Authorization Form for releasing records to a third party"
- "Generate a Security Incident Report template for our team"
- "Create a HIPAA compliance checklist for our annual review"

### Technical Safeguards
- "What encryption is required for a mobile app that stores patient data?"
- "What audit logs do we need to maintain for HIPAA, and for how long?"
- "We use Google Cloud — do we need a BAA? What services are HIPAA-eligible?"
- "What does HIPAA require for user authentication in our patient portal?"
- "We're building a FHIR API — what security controls do we need?"
- "Can we use real patient data in our dev/test environment?"

### Education & Explanation
- "What is the difference between a Covered Entity and a Business Associate?"
- "What are the 18 HIPAA identifiers?"
- "What does 'minimum necessary' mean in practice?"
- "When is a security incident a reportable breach vs. not?"
- "What are the penalties for a HIPAA violation?"
- "Does HIPAA apply to my employer wellness app?"

### Breach Response
- "We had a laptop stolen — do we need to report this?"
- "An employee emailed PHI to the wrong patient. Is this a breach?"
- "Walk me through the 4-factor breach risk assessment"
- "What are our notification deadlines if we confirm a breach?"
- "Draft a breach notification letter for affected individuals"

---

## How to Use the Skill

### Installation
Download `hipaa-compliance.skill` and install it in Claude's skill settings. Once installed, the skill activates automatically when your conversation involves HIPAA-related topics.

### Triggering the Skill
The skill is designed to trigger on a wide range of healthcare and compliance-related language. You don't need special syntax — just describe what you need naturally. Trigger phrases include:

- Direct mentions: *HIPAA, PHI, ePHI, covered entity, business associate, BAA*
- Document requests: *"draft a privacy notice," "generate a BAA," "create a risk assessment"*
- Compliance questions: *"is this HIPAA compliant?", "what does HIPAA require for...?"*
- System reviews: *"review our architecture," "audit our data handling"*
- Breach scenarios: *"we had a data incident," "employee accessed the wrong records"*

### Example Prompts

```
# Document review
"Here is our current data sharing agreement with our billing vendor.
Please review it for HIPAA compliance and flag any missing provisions."

# Template generation
"Generate a Notice of Privacy Practices for Valley Medical Group,
a multi-specialty outpatient clinic in California. Effective date: January 1, 2025."

# Technical guidance
"We're building a telehealth platform on AWS. What HIPAA technical safeguards
do we need to implement? We're using EC2, RDS (PostgreSQL), S3, and SES."

# Breach assessment
"An employee sent a spreadsheet containing names, DOBs, and diagnoses for
47 patients to the wrong email address. The recipient responded saying
they didn't open it. Walk me through whether we have a reportable breach."

# Education
"Explain the minimum necessary standard and give me three concrete
examples of how it applies in a hospital setting."
```

### Output Format
Depending on the request type, outputs follow structured formats:

- **Compliance Reviews** → Findings table (Issue / CFR Reference / Risk Level / Recommendation) + prioritized action items
- **Templates** → Complete documents with `[PLACEHOLDER]` fields and inline CFR citations
- **Technical Assessments** → Safeguard checklist organized by Administrative / Physical / Technical
- **Education** → Plain-language summary followed by regulatory detail and examples

---

## Skill Implementation Details

### Architecture

```
hipaa-compliance/
├── SKILL.md                          # Core skill — workflows, prompts, quick-reference tables
└── references/
    ├── privacy-rule.md               # 45 CFR Part 164, Subparts A & E — full Privacy Rule
    ├── security-rule.md              # 45 CFR Part 164, Subpart C — full Security Rule
    ├── breach-notification.md        # 45 CFR Part 164, Subpart D — Breach Notification Rule
    └── templates.md                  # 9 ready-to-use HIPAA document templates
```

The skill uses **progressive disclosure** — Claude loads only the reference file(s) relevant to the specific question, keeping context efficient while ensuring comprehensive coverage when needed.

### Reference File Coverage

| File | Key Content |
|------|------------|
| `privacy-rule.md` | Patient rights (access, amendment, accounting, restrictions), NPP requirements, minimum necessary standard, authorization rules, permitted disclosures (TPO + §164.512), special PHI categories, 18 identifiers, de-identification methods, marketing/fundraising rules |
| `security-rule.md` | All 54 Security Rule implementation specifications with Required/Addressable designations, risk analysis methodology (NIST SP 800-30 aligned), cloud architecture guidance (AWS/Azure/GCP), mobile/BYOD, DevOps/CI-CD, full implementation checklist |
| `breach-notification.md` | 4-Factor breach risk assessment, notification timelines and methods, HHS reporting portal guidance, BA notification chain, civil and criminal penalty tiers, breach response workflow, common scenario table |
| `templates.md` | NPP, BAA, HIPAA Privacy Policy, Authorization Form, Workforce Training Acknowledgment, Security Incident Report, Breach Risk Assessment, Risk Analysis Template, HIPAA Compliance Checklist |

### Inputs Used to Build This Skill

The skill was built based on the following requirements provided during design:

| Input | Value |
|-------|-------|
| **Core capabilities** | Compliance review, policy/template generation, technical safeguards advice, plain-language education |
| **Target audiences** | Developers, compliance officers, legal teams, general business staff (all of the above) |
| **Reference depth** | Detailed — full coverage of Privacy Rule, Security Rule, and Breach Notification Rule |
| **Regulatory basis** | 45 CFR Parts 160 and 164 (HIPAA), as amended by HITECH (2009) |
| **Technical scope** | Cloud environments (AWS/Azure/GCP), modern application architecture, FHIR APIs, mobile/BYOD, DevOps |
| **Document templates** | 9 templates covering the most commonly needed HIPAA compliance documents |
| **Skill format** | Claude Skill (`.skill` file) with `SKILL.md` + 4 bundled reference files |

### Design Decisions

**Audience-aware tone:** The skill is explicitly instructed to adjust depth and language based on who is asking — developers get technical specifics and code-level guidance, compliance officers get CFR citations, and general staff get plain-language explanations.

**Risk stratification:** All compliance findings are categorized as High / Medium / Low risk to help users prioritize remediation effort.

**Legal disclaimer:** Every compliance output includes a disclaimer that this is informational guidance, not legal advice, to ensure users understand the appropriate role of this tool.

**State law flag:** The skill is designed to note when state law may impose stricter requirements than HIPAA (particularly for mental health, HIV/AIDS, and reproductive health information).

**Encryption guidance:** The skill correctly represents encryption as "addressable" under HIPAA while communicating that AES-256 / TLS 1.2+ is the industry standard — an important nuance that generic compliance tools often get wrong.

---

## Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

*Skill created using the Claude Skill framework. Reference content is based on 45 CFR Parts 160 and 164 and HHS guidance current as of the build date. Always verify against the latest HHS publications and consult legal counsel for formal compliance determinations.*

---

*Skill version: 1.8.0 — August 2026*

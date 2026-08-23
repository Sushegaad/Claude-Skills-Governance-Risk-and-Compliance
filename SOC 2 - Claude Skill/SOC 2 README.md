# SOC 2 Compliance Skill for Claude

## 1. What Does the Skill Do?

This skill turns Claude into an expert SOC 2 compliance advisor. It provides deep, structured guidance across the full lifecycle of a SOC 2 engagement — from initial readiness assessment through policy writing, control documentation, audit evidence preparation, and third-party vendor risk management.

The skill is grounded in the **AICPA 2017 Trust Services Criteria (TSC) with 2022 Revised Points of Focus**, the authoritative standard for SOC 2 audits. It covers all five Trust Services Criteria:

| Criteria | Code | Status |
|---|---|---|
| Security (Common Criteria) | CC1–CC9 | Always required |
| Availability | A1 | Optional |
| Confidentiality | C1 | Optional |
| Processing Integrity | PI1 | Optional |
| Privacy | P1–P8 | Optional |

Rather than generic compliance advice, the skill routes each request to a dedicated knowledge area — producing criterion-specific gap assessments, auditor-ready control statements, policy drafts with mandatory clauses, evidence checklists, and vendor questionnaires — all using precise AICPA language and criteria codes.

---

## 2. Intended Audiences

The skill is designed to serve anyone involved in a SOC 2 program, and automatically adapts its tone and depth based on context:

**Startups and SMBs going through SOC 2 for the first time**
Teams with no prior compliance experience who need concepts explained, templates provided, and plain-language guidance on where to start.

**Security and compliance teams at mature organizations**
Practitioners who want to move fast — jump straight to gap matrices, criterion-specific control statements, evidence catalogs, and audit-ready documentation without hand-holding.

**Auditors and consultants**
Professionals who need precise AICPA criteria language, control test procedures, sampling guidance, and structured output they can use directly in client work.

**Engineering and DevOps teams**
Developers and infrastructure engineers who need to understand what controls are required for their systems (access management, change control, logging, patching) and what evidence they need to produce.

**Legal and procurement teams**
Staff handling vendor contracts, data processing agreements, and third-party risk who need questionnaire templates, CUEC tracking, and contractual requirements guidance.

---

## 3. Common Use Cases

### Gap Analysis & Readiness Assessment
- Conducting a self-assessment against all in-scope TSC criteria before a formal audit
- Identifying 🔴 gaps, 🟡 partial controls, and 🟢 met criteria with remediation priorities
- Building a remediation roadmap with owners, timelines, and evidence requirements
- Scoping a SOC 2 report (Type 1 vs Type 2, which TSC to include, system boundary)

### Policy & Procedure Writing
- Drafting any of the 12 core SOC 2 policies (Information Security, Access Control, Incident Response, Change Management, Risk Assessment, Vendor Management, BCP/DR, Data Classification, Acceptable Use, Privacy Notice, Encryption, Vulnerability Management)
- Reviewing existing policies for missing mandatory clauses, weak language ("should" vs "must"), or missing TSC mappings
- Writing annual policy review documentation

### Control Documentation
- Documenting controls in the standard format: Control ID, TSC criterion, type, owner, frequency, description, evidence, and test procedure
- Building a full controls matrix mapped to in-scope TSC criteria
- Translating existing practices into auditor-testable control statements
- Identifying gaps between preventive, detective, and corrective control coverage

### Audit Evidence Preparation
- Generating a complete evidence checklist for each in-scope criterion
- Understanding what artifacts prove a control for Type 1 vs Type 2 audits
- Knowing auditor sampling expectations by control frequency
- Organizing evidence folders to mirror TSC structure
- Catching common evidence pitfalls before they become audit findings

### Vendor Risk Questionnaires
- Tiering the vendor inventory (Critical / High / Medium / Low) with appropriate review cadences
- Sending and scoring a 32-question vendor security questionnaire
- Reviewing a vendor's SOC 2 report — evaluating the opinion, exceptions, and system description
- Identifying and tracking Complementary User Entity Controls (CUECs) from vendor SOC 2 reports
- Drafting contractual security requirements (DPA, security addendum, breach notification SLAs)

---

## 4. How to Use the Skill

### Installation
1. Download the `soc2.skill` file
2. In Claude, go to **Settings → Skills**
3. Upload the `.skill` file
4. The skill will activate automatically for relevant conversations

### Triggering the Skill
The skill activates automatically when your message relates to SOC 2 or adjacent compliance topics. You don't need to use a specific keyword — it triggers on natural language such as:

- *"We need to get our SOC 2 done by Q3, where do we start?"*
- *"Can you write an Incident Response Policy for us?"*
- *"What evidence do I need for CC6 access controls?"*
- *"A customer asked us to fill out their vendor security questionnaire"*
- *"We just got our AWS SOC 2 report — how do I review it?"*
- *"Draft a control statement for our change management process"*

### Example Prompts

```
"Run a SOC 2 gap analysis for a 30-person SaaS startup. We have MFA on 
most systems, a basic incident response process, but no formal policies 
and no vendor risk program."

"Write an Access Control Policy for a company that uses AWS, Okta, 
GitHub, and Salesforce."

"What evidence do I need to collect for a SOC 2 Type 2 audit covering 
Security and Availability? We use AWS and have a 12-month audit period."

"Here's our current list of vendors. Help me tier them by risk and tell 
me what due diligence is required for each tier."

"Write a control statement for our quarterly access review process 
mapping to CC6.5."
```

### Adapting the Output
The skill automatically adjusts based on your context:
- Mention you're new to SOC 2 → plain language, more explanation, step-by-step guidance
- Use TSC criteria codes in your question → detailed technical output, auditor-style language
- Mention a specific tool (e.g., Drata, Vanta, Secureframe) → it will tailor guidance to that platform's evidence format

---

## 5. Skill Implementation Details

### File Structure

```
soc2/
├── SKILL.md                    # Main skill — task routing, TSC reference, core workflows
└── references/
    ├── controls.md             # Control matrix with per-criterion examples and test procedures
    ├── policies.md             # Policy templates and writing standards for all 12 policies
    ├── evidence.md             # Evidence catalog by criterion, sampling guide, quality checklist
    └── vendor.md               # Vendor questionnaire, SOC 2 report review guide, CUEC tracking
```

**Total size:** ~1,276 lines across 5 files

### Architecture

The skill uses a **progressive disclosure pattern**:

- `SKILL.md` is always loaded when the skill triggers. It contains the TSC quick reference, a task router table, and concise workflow instructions for each of the five major use cases.
- The four `references/` files are loaded on-demand when Claude needs to go deeper — for example, `references/controls.md` is read when drafting control statements, and `references/vendor.md` is read when handling vendor risk questions.

This keeps the always-in-context content lean while making comprehensive reference material available when needed.

### Inputs Used to Build the Skill

The skill was built using the following inputs:

| Input | Description |
|---|---|
| **AICPA 2017 TSC (2022 Points of Focus)** | Authoritative source for all criteria codes, definitions, and points of focus (CC1–CC9, A1, C1, PI1, P1–P8) |
| **SOC 2 audit methodology** | Control design principles, Type 1 vs Type 2 distinctions, auditor test procedures, and sampling expectations |
| **Real-world gap patterns** | Most commonly flagged gaps across CC1–CC9 sourced from published readiness assessments and audit firm guidance |
| **Policy writing standards** | Security policy best practices including mandatory clauses, language standards ("must" vs "should"), and scope requirements |
| **Evidence best practices** | Evidence quality criteria (contemporaneous, attributable, complete), common pitfalls, and artifact naming conventions |
| **Vendor risk frameworks** | CC9.2 vendor risk tiering, CUEC management, SOC 2 report review methodology, and contractual security requirements |
| **Skill creator framework** | Built using the Claude skill creator pattern with YAML frontmatter, progressive disclosure architecture, and reference file separation |

### Design Decisions

**TSC criteria codes throughout** — Every control, policy, evidence item, and gap is tagged with its AICPA criteria code (e.g., CC6.3) so output is directly usable in audit documentation without needing translation.

**Audience-adaptive output** — Rather than a single response style, the skill explicitly instructs Claude to detect the user's maturity level (startup vs practitioner vs auditor) and adjust language, depth, and format accordingly.

**No prescriptive control list** — Consistent with AICPA guidance, the skill does not mandate specific controls. It provides examples and templates while reminding users that controls must be tailored to their organization's environment.

**Separation of concerns across reference files** — Each reference file handles one major workflow, keeping files focused and under ~280 lines each for clarity and fast loading.

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

---

*Skill version: 1.8.0 — August 2026*

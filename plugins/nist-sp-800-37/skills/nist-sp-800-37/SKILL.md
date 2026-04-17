---
name: nist-sp-800-37
description: >
  Expert NIST SP 800-37 Rev 2 Risk Management Framework (RMF) advisor. Use this skill
  whenever a user asks about the NIST RMF, the six RMF steps (Categorise, Select, Implement,
  Assess, Authorise, Monitor), FISMA compliance, Authorisation to Operate (ATO), system
  security plans (SSP), security assessment reports (SAR), plans of action and milestones
  (POA&M), authorization packages, control tailoring, common control inheritance, continuous
  monitoring strategies, RMF roles (ISSO, ISSM, SO, AO, CCP), privacy integration into the
  RMF, or linking the RMF to the NIST Cybersecurity Framework (CSF). Also trigger for:
  "how do I get an ATO?", "what is the RMF process?", "help me prepare an authorization
  package", "what is a common control provider?", "how do I do control tailoring?", or
  any federal system security authorisation question.
---

# NIST SP 800-37 Rev 2 — Risk Management Framework (RMF) Skill

You are an expert RMF advisor and federal information security consultant specialising in **NIST Special Publication 800-37 Revision 2: Risk Management Framework for Information Systems and Organizations** (December 2018). You assist **federal agencies, contractors (under FISMA), and organisational risk management teams** in implementing and navigating the full RMF lifecycle.

This skill is grounded exclusively in SP 800-37 Rev 2. All tasks, roles, inputs, outputs, and processes are drawn directly from that publication.

---

## How to Respond

Match your output to the task type:

| Task | Output Format |
|------|--------------|
| RMF step guidance | Structured step overview with tasks, inputs, outputs, and roles |
| System categorisation | FIPS 199 impact level table with rationale |
| Control baseline selection | Table: Control | Baseline | Tailoring Action | Justification |
| SSP assistance | SSP section templates and guidance |
| Authorization package checklist | Checklist: document | status | notes |
| POA&M guidance | Table: Weakness | Control | Severity | Remediation Plan | Milestones | Responsible Party |
| Continuous monitoring strategy | Structured strategy document |
| Role clarification | Narrative with responsibilities per role |
| General question | Clear, concise prose with SP 800-37 task citations |

---

## RMF Overview

### Purpose
SP 800-37 Rev 2 describes the **Risk Management Framework** — an integrated, system-level approach to managing information security and privacy risk. The RMF establishes a disciplined and structured process for integrating security, privacy, and cyber supply chain risk management activities into the SDLC.

### Key Changes in Rev 2 (from Rev 1)
| Topic | Rev 1 | Rev 2 |
|-------|-------|-------|
| Privacy | Separate from security | Fully integrated |
| Supply chain | Not covered | Explicitly included (new Prepare step) |
| Step count | 6 steps | 7 steps (added Prepare) |
| CSF alignment | Implicit | Explicit mapping |
| Automation | Not addressed | Addressed in Prepare and Monitor |
| Missions/business | System-centric | Explicitly multi-tier |

### The Seven RMF Steps

| # | Step | Purpose |
|---|------|---------|
| 0 | **Prepare** | Establish context and priorities; assign roles; identify common controls; develop enterprise risk strategy |
| 1 | **Categorise** | Categorise the system and information processed, stored, transmitted based on adverse impact |
| 2 | **Select** | Select, tailor, and supplement security and privacy controls based on risk assessment |
| 3 | **Implement** | Implement controls; document in System Security Plan |
| 4 | **Assess** | Assess whether controls are implemented correctly, operating as intended, producing desired outcomes |
| 5 | **Authorise** | Authorise the system (or controls) based on a determination that residual risk is acceptable |
| 6 | **Monitor** | Continuously monitor control effectiveness; report security and privacy posture; conduct ongoing risk assessment |

---

## Step 0 — Prepare

### Purpose
Prepare the organisation for RMF execution by establishing roles, responsibilities, risk management strategies, and common control programs. This step is performed at both the **organisation level** and the **system level**.

### Organisation-Level Tasks

| Task | Description | Key Output |
|------|-------------|-----------|
| P-1 | Assign risk management roles | Senior Agency Official for Privacy (SAOP), AO, AODR, ISSO, System Owner roles assigned |
| P-2 | Establish risk management strategy and risk tolerance | Organisation-wide risk management strategy document |
| P-3 | Conduct organisation-wide risk assessment | Identifies high-priority threats and risks informing system-level decisions |
| P-4 | Establish organisation-wide control assignments | Common control register; common control providers identified |
| P-5 | Identify, align, and deduplicate missions and business functions | Mission/business function analysis |
| P-6 | Define information types and establish baseline | Organisation-wide information types catalogue aligned to SP 800-60 |
| P-7 | Identify and document common controls | Common control catalogue; inheritance register |
| P-8 | Build organisational-level tailoring guidance | Organisation-specific tailoring policies and scoping guidance |
| P-9 | Develop enterprise architecture | Security and privacy architecture; authorised technologies list |
| P-10 | Define requirements and capabilities | Security and privacy requirements derived from legislation, executive orders, directives |

### System-Level Prepare Tasks

| Task | Description | Key Output |
|------|-------------|-----------|
| P-11 | Identify stakeholders | Stakeholder register |
| P-12 | Assign system-level roles | ISSO, ISSM, system administrator, and other system-specific roles |
| P-13 | Identify assets needing protection | Asset inventory |
| P-14 | Conduct system-level risk assessment | System-specific risk assessment feeding categorisation |
| P-15 | Define authorisation boundary | System boundary documentation |
| P-16 | Register the system | System registered in the agency's ISCM/GRC tool |
| P-17 | Identify applicable laws and regulations | Legal, statutory, and policy requirements register |
| P-18 | Identify common control providers | Inheritance documentation |

---

## Step 1 — Categorise

### Purpose
Categorise the information system and the information processed, stored, and transmitted by the system based on an analysis of the potential impact if confidentiality, integrity, or availability is compromised.

### Process (FIPS 199 / SP 800-60)

1. Identify all information types processed, stored, or transmitted (refer to SP 800-60 taxonomy)
2. For each information type, determine provisional impact values for C, I, and A (Low / Moderate / High)
3. Adjust provisional values based on organisational factors (mission criticality, aggregation effects)
4. Determine the **system security category** = highest impact value across all information types (the "high-water mark")
5. Document in the **Security Categorisation document** and the **System Security Plan**

### FIPS 199 Impact Level Definitions

| Impact | Confidentiality | Integrity | Availability |
|--------|----------------|-----------|-------------|
| **LOW** | Limited adverse effect: minor mission degradation; minor financial loss; minor harm to individuals | Limited adverse effect | Limited adverse effect |
| **MODERATE** | Serious adverse effect: significant mission degradation; significant loss; significant harm | Serious adverse effect | Serious adverse effect |
| **HIGH** | Severe or catastrophic: severe mission impairment or loss; major financial damage; severe individual harm or loss of life | Severe or catastrophic | Severe or catastrophic |

### Control Baselines (SP 800-53 Rev 5)
- **LOW system (SC = LOW)** → SP 800-53 Low Baseline
- **MODERATE system (SC = MODERATE)** → SP 800-53 Moderate Baseline
- **HIGH system (SC = HIGH)** → SP 800-53 High Baseline

### Outputs
- Security Categorisation document
- System description update
- System registration update

---

## Step 2 — Select

### Purpose
Select, tailor, and supplement the initial set of security and privacy controls based on the categorisation and risk assessment results.

### Process

1. **Select baseline**: Map system categorisation to SP 800-53 baseline (Low/Moderate/High)
2. **Apply scoping considerations**: Eliminate controls that are not applicable given system environment/technology
3. **Apply tailoring**: Add/remove controls to address specific risk factors, technologies, or regulatory requirements
4. **Add overlays**: Apply sector-specific control overlays where applicable (e.g., Intelligence Community, DoD, healthcare)
5. **Document**: Record all tailoring decisions in the SSP with justifications
6. **Assign controls to system/common/hybrid**: Determine whether each control is system-specific, inherited (common), or hybrid

### Tailoring Actions

| Action | Description | Required Documentation |
|--------|-------------|----------------------|
| **Scoping** | Remove control where it does not apply (e.g., no wireless — remove wireless controls) | Documented rationale in SSP |
| **Parameterisation** | Fill in organisation-defined values for controls with parameters | SSP parameter table |
| **Compensating controls** | Alternative controls where standard controls are not feasible | SSP with compensating control justification |
| **Adding controls** | Add controls not in baseline but required by risk, law, or regulation | SSP with addition rationale |
| **Overlays** | Community-defined control modifications for specific environments | Overlay documentation |

### Control Assignment Types
| Type | Description |
|------|-------------|
| **System-specific** | Implemented and managed by the system owner for this system only |
| **Common (Inherited)** | Provided by an external organisation or common control provider; system inherits this control |
| **Hybrid** | Part common (inherited), part system-specific |

### Outputs
- Completed SSP (control selection section)
- Privacy Plan (if applicable)
- Supply Chain Risk Management Plan (if applicable)

---

## Step 3 — Implement

### Purpose
Implement the security and privacy controls in the information system and in the environment of operation.

### Process

1. Implement each selected control (or confirm inheritance)
2. Document implementation details in the SSP for each control:
   - Control narrative: how the control is implemented
   - Responsible entity
   - Implementation status (implemented/planned/not applicable/inherited)
3. Update system architecture documentation if implementation requires changes
4. Address supply chain risk management requirements during acquisition/development
5. Document deviations or compensating implementations

### SSP Control Implementation Documentation Format

For each control in the SSP:
```
Control ID:     [e.g., AC-2]
Control Name:   [e.g., Account Management]
Assignment:     [System-specific / Common / Hybrid]
Status:         [Implemented / Planned / Not Applicable / Inherited]
Implementation: [Narrative describing HOW the control is implemented]
Responsible:    [Org unit or role responsible]
Evidence:       [Location of evidence/audit artefacts]
Inherited From: [Common control provider name, if applicable]
```

### Outputs
- Updated SSP (implementation details)
- Security and privacy plans
- Procurement documents with security requirements

---

## Step 4 — Assess

### Purpose
Assess whether security and privacy controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting the security and privacy requirements.

### Process (per SP 800-53A)

1. **Develop Security Assessment Plan (SAP)**: Define scope, methods, depth/coverage, and timeline
2. **Conduct assessments**: Use assessment procedures from SP 800-53A for each control
3. **Analyse results**: Identify deficiencies and weaknesses
4. **Initial risk assessment**: Determine risk posed by identified weaknesses
5. **Produce Security Assessment Report (SAR)**: Document findings, deficiencies, and recommendations
6. **Develop/update POA&M**: Document weaknesses that are not immediately remediated

### Assessment Methods (SP 800-53A)

| Method | Description |
|--------|-------------|
| **Examine** | Review documentation, specifications, mechanisms, and activities |
| **Interview** | Conduct discussions with individuals or groups responsible for controls |
| **Test** | Execute mechanisms and follow activities to compare actual with expected behaviour |

### Assessment Depth and Coverage

| Attribute | Values |
|-----------|--------|
| Depth | Basic / Focused / Comprehensive |
| Coverage | Representative sample / All instances |

### Security Assessment Report (SAR) Contents
1. Assessment scope and methodology
2. Control-by-control findings (Satisfied / Other Than Satisfied / Not Applicable)
3. Weaknesses identified (with severity: Critical/High/Moderate/Low/Informational)
4. Risk determination per weakness
5. Recommendations for remediation

### Plan of Action and Milestones (POA&M)
POA&M columns:

| Column | Description |
|--------|-------------|
| POA&M ID | Unique identifier |
| Weakness | Description of the control deficiency |
| Related Control | SP 800-53 control ID(s) |
| Weakness Severity | Critical / High / Moderate / Low |
| Source | Assessment finding, audit, incident, or self-identified |
| Responsible POC | Individual or team responsible for remediation |
| Estimated Completion | Target remediation date |
| Milestones | Intermediate milestones with dates |
| Status | Open / In Progress / Completed / Risk Accepted |
| Resources Required | Staff, budget, tools needed |

### Outputs
- Security Assessment Plan (SAP)
- Security Assessment Report (SAR)
- Plan of Action and Milestones (POA&M)
- Updated SSP

---

## Step 5 — Authorise

### Purpose
Provide accountability by requiring a senior official (Authorising Official) to formally accept the risk to organisational operations, assets, individuals, and the nation based on the implementation of an agreed-upon set of security and privacy controls.

### Authorization Types

| Type | Description |
|------|-------------|
| **Authorization to Operate (ATO)** | Full authorisation for a specific period (typically 3 years) |
| **Authorization to Use (ATU)** | Authorisation to use an external common control or service |
| **Ongoing Authorization** | Continuous ATO maintained through real-time security posture monitoring (replaces periodic reauthorisation) |
| **Denial of Authorization to Operate (DATO)** | System must cease operation; unacceptable risk level |

### Authorization Package Contents

| Document | Description |
|----------|-------------|
| System Security Plan (SSP) | Complete system description, boundary, categorisation, controls, and implementation narratives |
| Security Assessment Report (SAR) | Assessment findings and deficiency determination |
| Plan of Action and Milestones (POA&M) | Open weaknesses and remediation plans |
| Executive Summary | Brief risk posture summary for AO decision-making |
| (Optional) Risk Assessment Report | If conducted as separate artefact |
| (Optional) Privacy Plan + Assessment | Required if processing PII |

### Authorisation Decision Factors
The AO considers:
1. Completeness of the authorization package
2. Level of residual risk (from SAR + risk assessment)
3. Acceptability of POA&M milestones
4. Organisational risk tolerance
5. Legal, regulatory, and policy obligations

### Outputs
- Authorization Decision document
- Authorization Decision memo (signed by AO)
- Updated SSP, SAR, POA&M
- Risk acceptance documentation

---

## Step 6 — Monitor

### Purpose
Maintain ongoing awareness of security and privacy posture through continuous monitoring; assess control effectiveness as the system and threat environment change; report on security and privacy status; and conduct ongoing risk assessments to support authorisation decisions.

### Continuous Monitoring Tasks

| Task | Description | Frequency |
|------|-------------|-----------|
| M-1 | Define continuous monitoring strategy | Initial setup + annual review |
| M-2 | Establish monitoring program | Initial setup |
| M-3 | Analyse and report security and privacy posture | Per monitoring strategy (typically monthly/quarterly) |
| M-4 | Ongoing control assessments | Per monitoring strategy (subset of controls at each cycle) |
| M-5 | Ongoing risk response | As needed based on monitoring findings |
| M-6 | Authorisation updates | When significant changes trigger reauthorisation consideration |
| M-7 | System disposal | When system is decommissioned |

### Continuous Monitoring Strategy Elements
1. **Metrics**: Define security and privacy metrics to collect
2. **Assessment frequencies**: Which controls are assessed at which intervals
3. **Reporting**: How and to whom security posture is reported
4. **Triggers**: Events that trigger immediate notification or reauthorisation (significant changes, incidents)
5. **Automation**: Tools used for automated collection (SIEM, SCAP, vulnerability scanners)

### Significant Change Definition
Events that may require reauthorisation consideration:
- Changes to system boundary (new components, services, interconnections)
- Changes to authorisation environment (new hosting location, new provider)
- Changes to threat environment (new applicable threat intelligence)
- Performance or functionality changes affecting the SP 800-53 control baselines
- Agency policy changes

---

## RMF Roles and Responsibilities

| Role | Full Name | Key Responsibilities |
|------|-----------|---------------------|
| **AO** | Authorising Official | Signs the ATO; accepts organisational risk; has budget/mission authority over the system |
| **AODR** | AO Designated Representative | Acts on behalf of AO for day-to-day RMF activities |
| **SO** | System Owner | Responsible for the system's procurement, development, integration, and operation |
| **ISSO** | Information System Security Officer | Day-to-day security oversight; maintains SSP and POA&M; coordinates assessment activities |
| **ISSM** | Information System Security Manager | Manages the ISSO function across multiple systems; escalation point for security issues |
| **CCP** | Common Control Provider | Provides and maintains common inherited controls; documents in a Common Control Plan |
| **SAOP/CPO** | Senior Agency Official for Privacy / Chief Privacy Officer | Privacy integration into RMF; privacy impact assessments |
| **Mission/Business Owner** | Mission/Business Process Owner | Defines mission requirements and risk tolerance |
| **Risk Executive (Function)** | Enterprise Risk Management | Ensures system-level risks are consistent with organisational risk tolerance |
| **SCA** | Security Control Assessor | Independent assessor conducting Step 4 assessments; should be organisationally independent of ISSO |
| **CISO** | Chief Information Security Officer | Agency-wide information security program; FISMA reporting |

---

## Core Workflows

### 1. Preparing an Authorization Package
When helping to build an ATO package:
1. Verify SSP completeness (boundary, environment, all controls with implementation narratives)
2. Confirm SAR has been completed by an independent SCA
3. Verify POA&M covers all open findings from SAR with realistic milestones
4. Prepare AO briefing package with executive summary and risk summary
5. Include or reference risk assessment report
6. Check that all interconnection and common control inheritance agreements are current

Checklist format:
| Document | Status | Notes |
|----------|--------|-------|
| SSP — complete with all control narratives | | |
| SSP — categorisation section (FIPS 199) | | |
| SAR — signed by SCA | | |
| POA&M — all SAR findings addressed | | |
| Risk assessment report | | |
| Privacy plan (if PII processed) | | |
| Interconnection Security Agreements (ISAs) | | |
| Memoranda of Understanding/Agreement (MOU/MOA) | | |

### 2. Control Tailoring Guidance
When asked to tailor a control baseline:
1. Start with the applicable baseline (Low/Moderate/High) from SP 800-53
2. Apply scoping guidance from SP 800-53 Appendix D
3. Remove controls that are genuinely not applicable (with documented justification)
4. Set all organisation-assigned parameter values
5. Add controls required by applicable law, regulation, or executive directive
6. Identify common/inherited controls and document inheritance agreements
7. Review NIST guidance document for the technology type (cloud, mobile, ICS/OT in separate overlays)

### 3. Continuous Monitoring Strategy Development
1. Define the organisation's monitoring tier and automation capability
2. Select metrics aligned to the 17 SP 800-53 control families
3. Assign monitoring frequencies: monthly (high-risk controls), quarterly (standard), annual (low-change controls)
4. Define reporting: automated dashboards, monthly security posture briefs to AO, annual reviews
5. Define triggers for reauthorisation or escalation
6. Document in a Continuous Monitoring Strategy document

---

## Reference Files

Load the appropriate reference file based on the task:

- `references/rmf-steps-tasks.md` — All RMF steps with complete task tables, inputs, outputs, and role assignments
- `references/authorization-package.md` — Complete authorization package guidance, SSP template, SAR structure, POA&M format, and ATO decision criteria
- `references/roles-and-responsibilities.md` — All RMF roles with detailed responsibilities, appointment requirements, and organisational relationships

**When to load:**
- Working through an RMF step → load `references/rmf-steps-tasks.md`
- Building or reviewing an authorization package → load `references/authorization-package.md`
- Clarifying roles or assigning responsibilities → load `references/roles-and-responsibilities.md`

---

## Disclaimer

This skill provides guidance based on NIST SP 800-37 Rev 2 (NIST, December 2018), a freely available public publication. This skill does not constitute legal, audit, or professional compliance advice. Federal agencies are bound by FISMA and agency-specific policies that may impose additional requirements beyond this publication. Organisations should engage qualified FISMA/RMF specialists to validate their authorisation approach for high-impact systems.

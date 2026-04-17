# HITRUST Assessment Guide
## Assessment Types, Process, Scoring, and Certification Lifecycle

---

## Table of Contents
1. [Assessment Type Comparison](#1-assessment-type-comparison)
2. [e1 — Entry-Level Assessment](#2-e1--entry-level-assessment)
3. [i1 — Implemented 1-Year Assessment](#3-i1--implemented-1-year-assessment)
4. [r2 — Risk-Based 2-Year Assessment](#4-r2--risk-based-2-year-assessment)
5. [HITRUST Maturity Model and Scoring](#5-hitrust-maturity-model-and-scoring)
6. [Assessment Process Steps](#6-assessment-process-steps)
7. [Corrective Action Plans (CAPs)](#7-corrective-action-plans-caps)
8. [MyCSF Platform](#8-mycsf-platform)
9. [HITRUST Authorized External Assessors](#9-hitrust-authorized-external-assessors)
10. [Certification Maintenance and Renewal](#10-certification-maintenance-and-renewal)
11. [Interim Assessment Requirements](#11-interim-assessment-requirements)

---

## 1. Assessment Type Comparison

| Feature | e1 | i1 | r2 |
|---------|-----|-----|-----|
| Number of control requirements | 44 | 219 (v11) | Variable (risk-tailored) |
| Certification period | 1 year | 1 year | 2 years |
| Interim assessment at 12 months | No | No | Yes (required) |
| Control set type | Fixed | Fixed (Defined Baseline) | Risk-tailored |
| Maturity levels assessed | 3 (Policy, Procedure, Implemented) | 3 (Policy, Procedure, Implemented) | All 5 levels |
| Assessor required | Yes (CPA firm) | Yes (HITRUST Authorized External Assessor) | Yes (HITRUST Authorized External Assessor) |
| HITRUST QA review | Streamlined | Standard | Full QA + validation |
| Primary use case | Basic cyber hygiene attestation | Moderate assurance for business partners | Highest assurance; major healthcare enterprises |
| Typical effort | Low | Moderate | Significant |
| Typical cost (indicative) | Lower | Moderate | Higher |
| Suitable for first-time HITRUST | Yes | Yes | Yes (with preparation) |
| Demonstrates HIPAA compliance support | Partial | Strong | Comprehensive |

**Note:** Cost and timeline estimates vary significantly based on organization size, existing
programme maturity, and assessor fees. Engage a HITRUST Authorized External Assessor for
specific engagement scoping.

---

## 2. e1 — Entry-Level Assessment

### Purpose
The e1 assessment is designed to provide a basic, certifiable attestation of fundamental
cyber hygiene practices. It is the entry point into the HITRUST Assurance Program and is
suitable for organizations that are new to HITRUST or that need a low-cost foundational
attestation.

### Scope
- 44 essential control requirements
- Fixed set — identical for all organizations regardless of risk factors
- Controls drawn from across the full HITRUST CSF control categories

### Maturity Levels Assessed
For e1, each control is assessed at three maturity levels:
- Level 1: Policy
- Level 2: Procedure
- Level 3: Implemented

Levels 4 and 5 (Measured and Managed) are not assessed in e1.

### Assessor Requirements
- Assessment must be performed and validated by a CPA firm that is a HITRUST Authorized
  External Assessor (AEA)
- The organization completes a self-assessment in MyCSF
- The AEA reviews and validates the responses

### Evidence Expectations
For each of the 44 control requirements, the assessor will review:
- Policy documentation addressing the control
- Procedure documentation
- Evidence of implementation (screenshots, configuration exports, process records)

### Key e1 Control Areas
The 44 e1 requirements cover foundational areas including:
- Basic access control (user provisioning, password requirements, MFA)
- Information security policy existence
- Security awareness training
- Malware protection
- Patch management and vulnerability management
- Audit logging
- Incident response plan existence
- Backup and recovery
- Network boundary protection

---

## 3. i1 — Implemented 1-Year Assessment

### Purpose
The i1 assessment demonstrates that an organization has a well-implemented security
programme meeting a defined baseline of controls. It provides moderate assurance and is
appropriate for organizations that have matured beyond entry-level practices and need a
stronger attestation for business partners or regulators.

### Scope
- 219 control requirements (v11 Defined Baseline)
- Fixed set — same controls for all organizations in scope
- Covers all 14 control categories of the HITRUST CSF

### Maturity Levels Assessed
For i1, each control is assessed at three maturity levels:
- Level 1: Policy
- Level 2: Procedure
- Level 3: Implemented

### Assessor Requirements
- Assessment must be performed and validated by a HITRUST Authorized External Assessor (AEA)
- Full on-site or remote validation engagement
- Assessor submits validated responses to HITRUST for review

### Certification Period
- 1 year from date of HITRUST certification letter issuance
- No interim assessment required (unlike r2)
- Renewal requires a new i1 assessment

---

## 4. r2 — Risk-Based 2-Year Assessment

### Purpose
The r2 assessment is the most comprehensive HITRUST assessment type. It demonstrates that
an organization has a robust, measured, and managed security programme across a risk-tailored
set of controls. The r2 is the most commonly recognized and demanded certification type in
healthcare and highly regulated industries.

### Scope
- Variable number of control requirements based on risk factor scoring
- Typically ranges from approximately 150 to 500+ requirements
- The final set of in-scope controls is determined by HITRUST scoping factors populated in MyCSF
  before the assessment begins

### How Scoping Works for r2
HITRUST uses "risk factors" to determine which control specifications are required for a
given organization. Each risk factor adds additional control requirements to the base set.
Key risk factors include:
- **Organization type** (Covered Entity, Business Associate, etc.)
- **Number of individuals whose records are processed**
- **Types of sensitive data processed** (ePHI, PII, payment card data)
- **Regulatory environment** (HIPAA, PCI DSS, CMS, state laws)
- **Technology factors** (cloud, mobile, web applications, remote access)
- **Geographic reach**

See `hitrust-scoping-factors.md` for full factor details.

### Maturity Levels Assessed
For r2, all five maturity levels are assessed:
- Level 1: Policy (25% weight)
- Level 2: Procedure (25% weight)
- Level 3: Implemented (25% weight)
- Level 4: Measured (15% weight)
- Level 5: Managed (10% weight)

### Certifiable Threshold
- Each control requirement must achieve a minimum score of 62 (out of 100) to be certifiable
- Controls below 62 require a Corrective Action Plan (CAP) before certification can be issued
- Controls scoring 75 or above are fully certifiable

### Interim Assessment
- Required at the 12-month mark of the 2-year certification period
- The interim assessment validates that controls remain operational
- Failure to complete the interim assessment will result in certification suspension
- Interim assessment covers a subset of the originally assessed controls

### Assessor Requirements
- Full engagement with a HITRUST Authorized External Assessor
- HITRUST performs its own QA and validation review of the assessor's work
- HITRUST issues the final certification letter (not the assessor)

### Certification Period
- 2 years from date of HITRUST certification letter
- Interim assessment required at 12 months
- Renewal assessment required before expiry

---

## 5. HITRUST Maturity Model and Scoring

### Five Maturity Levels

HITRUST scores each control specification against five maturity levels derived from the
Carnegie Mellon PRISMA (Program Review for Information Security Management Assistance) model:

**Level 1 — Policy**
- Is there a written policy that addresses and mandates this control?
- The policy must be approved by management, formally published, and accessible to relevant
  personnel
- Scoring weight: 25%

**Level 2 — Procedure**
- Are there documented procedures that describe how the policy is implemented?
- Procedures must be detailed enough for staff to follow; they must specify who does what,
  when, and how
- Scoring weight: 25%

**Level 3 — Implemented**
- Is the control actually operational? Is there evidence demonstrating implementation?
- Evidence includes screenshots, configuration exports, access logs, training records, etc.
- Scoring weight: 25%

**Level 4 — Measured**
- Is performance of the control measured and monitored?
- Metrics, KPIs, compliance dashboards, and exception reports are typical evidence
- Scoring weight: 15%

**Level 5 — Managed**
- Is the control process continuously reviewed and improved?
- Evidence includes management review records, improvement initiatives, programme maturity
  reports, and periodic effectiveness testing
- Scoring weight: 10%

### Scoring Scale Per Level

For each maturity level, the assessor evaluates and scores 0–3:
- **0 (Non-Compliant)**: No evidence; requirement not met
- **1 (Somewhat Compliant)**: Partial evidence but significant gaps
- **2 (Partially Compliant)**: Evidence present but incomplete or inconsistent
- **3 (Fully Compliant)**: Comprehensive evidence; requirement fully met

### Aggregate Score Calculation

The aggregate score per control is calculated as:

```
Score = (L1_score/3 * 25%) + (L2_score/3 * 25%) + (L3_score/3 * 25%)
      + (L4_score/3 * 15%) + (L5_score/3 * 10%)
      * 100
```

A perfect score = 100. Minimum certifiable = 62.

### Score Interpretation

| Score Range | Classification | CAP Required? |
|------------|----------------|---------------|
| 75–100 | Certifiable | No |
| 62–74 | Near-Certifiable (Partially Compliant finding) | CAP recommended |
| 0–61 | Non-Certifiable | CAP required |

For **r2** certification, all assessed controls must score 62 or above to proceed
to certification. Controls at 62–74 require observation-level CAPs but do not block
certification. Controls below 62 require substantive CAPs that must be reviewed by HITRUST
before a certification letter can be issued.

---

## 6. Assessment Process Steps

### Phase 1 — Preparation (Pre-Assessment)

**Step 1: Determine Assessment Type**
- Determine whether e1, i1, or r2 is appropriate based on organizational requirements,
  customer demands, and regulatory landscape
- Consult with a HITRUST Authorized External Assessor

**Step 2: Select an Assessor**
- Engage a HITRUST Authorized External Assessor (AEA)
- For e1: A CPA firm that is a HITRUST AEA
- For i1 and r2: Any HITRUST AEA organization
- The assessor registers the engagement in MyCSF

**Step 3: Create/Access MyCSF Account**
- The organization must have an active MyCSF account
- The assessor creates the assessment in MyCSF linked to the organization's account

**Step 4: Complete Scoping (r2 only)**
- For r2 assessments, complete the scoping questionnaire in MyCSF
- HITRUST uses the scoping responses to generate the in-scope control set
- Review the generated control set with the assessor before proceeding

**Step 5: Readiness Assessment (Recommended)**
- Conduct an internal readiness assessment or engage the AEA for a readiness review
- Identify gaps and develop CAPs before the formal validated assessment begins
- Address critical gaps (controls likely to score below 62) before scheduling the full assessment

### Phase 2 — Validated Assessment

**Step 6: Organization Self-Assessment**
- Complete self-assessment responses in MyCSF for all in-scope controls
- Upload evidence for each maturity level being assessed
- Assign evidence to specific control requirements
- Ensure all Level 1 (Policy) and Level 2 (Procedure) responses reference specific documents

**Step 7: Assessor Validation**
- The AEA reviews all self-assessment responses and uploaded evidence
- The assessor may request additional evidence or schedule interviews and site visits
- For r2, the assessor conducts comprehensive testing activities (interviews, observations,
  system demonstrations, configuration reviews)
- The assessor scores each control at each maturity level
- Where the assessor disagrees with the organization's self-assessment, corrections are
  documented with rationale

**Step 8: Findings and CAP Development**
- The assessor identifies non-certifiable and near-certifiable findings
- For each finding, a Corrective Action Plan (CAP) must be documented in MyCSF
- CAPs must include: root cause, remediation plan, responsible owner, and target date
- CAPs for non-certifiable findings must be reviewed and accepted by HITRUST before
  the assessment can proceed to certification

### Phase 3 — HITRUST Review and Certification

**Step 9: HITRUST QA Review**
- The completed and validated assessment is submitted to HITRUST
- HITRUST performs a quality assurance review of the assessment
- HITRUST may request clarifications from the assessor or additional documentation
- For r2, HITRUST performs a more intensive review

**Step 10: Certification Decision**
- If all certifiable thresholds are met (all controls score 62+) and CAPs are in place for
  any findings, HITRUST issues the certification letter
- The certification letter is the official documentation of HITRUST certification status
- The letter specifies: organization name, certification scope, assessment type, issue date,
  and expiration date

**Step 11: Post-Certification**
- For r2: Interim assessment required at 12 months
- Certification must be renewed before the expiration date
- Changes to the assessed environment that materially affect the control environment should
  be communicated to the assessor

---

## 7. Corrective Action Plans (CAPs)

### What is a CAP?
A Corrective Action Plan is a formal documented plan to address a finding identified during
the HITRUST assessment. CAPs are mandatory for non-certifiable controls and recommended for
near-certifiable controls.

### CAP Lifecycle
1. **Identified**: Finding identified by assessor during validated assessment
2. **Created**: CAP documented in MyCSF with required details
3. **In Remediation**: Organization actively working the remediation plan
4. **Submitted for Review**: Organization indicates remediation is complete
5. **Reviewed**: Assessor or HITRUST reviews CAP closure evidence
6. **Closed**: CAP closes when sufficient evidence demonstrates remediation

### CAP Requirements
Each CAP record must include:
- **Finding description**: What the deficiency is and which control is affected
- **Root cause analysis**: Why the deficiency exists (not just what the deficiency is)
- **Remediation plan**: Specific steps to address the root cause
- **Implementation owner**: The person or role responsible for remediation
- **Target completion date**: Realistic date for remediation completion
- **Milestone dates**: Intermediate checkpoints for larger remediation efforts
- **Evidence plan**: What evidence will be provided to demonstrate closure

### CAP Example Template

```
CAP ID:             CAP-2024-001
Control:            09.l.1 — Information Backup
Assessment Type:    r2
Finding:            Backup recovery testing is not performed. Backups exist but no documented
                    evidence of restoration testing within the past 12 months.
Maturity Gap:       Level 3 (Implemented) — Testing is not performed; Level 4 (Measured) —
                    No metrics on backup success/failure or recovery time.
Root Cause:         Backup procedures do not include a test restoration step.
                    No formal schedule for recovery testing exists.
Remediation Plan:   1. Update Backup and Recovery Procedure to include quarterly restoration
                       testing requirement.
                    2. Schedule and complete initial recovery test for all critical systems.
                    3. Document results in a Backup Test Log.
                    4. Implement monitoring alerts for backup job failures.
Owner:              IT Infrastructure Manager
Target Date:        [DATE — within 90 days of finding]
Milestones:         [30 days] Procedure updated and approved
                    [60 days] Initial recovery test completed and documented
                    [90 days] Monitoring implemented; first month of backup metrics collected
Evidence Plan:      Updated Backup and Recovery Procedure (v2.0), Backup Test Log with
                    results, monitoring dashboard screenshots, backup job success reports
Status:             Open — In Remediation
```

---

## 8. MyCSF Platform

### Overview
MyCSF (myCSF.net) is HITRUST's online assessment management platform. All HITRUST assessments
are conducted, tracked, and submitted through MyCSF.

### Key Capabilities
- **Assessment creation and management**: Assessors and organizations create and manage
  assessment engagements
- **Control scoping**: For r2 assessments, risk factor questionnaires generate the in-scope
  control set
- **Self-assessment responses**: Organizations document their control posture and upload evidence
- **Assessor validation**: Assessors review, test, and score each control
- **CAP management**: Organizations and assessors track CAP lifecycle from creation to closure
- **Evidence repository**: Centralized repository for all assessment evidence
- **Inheritance management**: Organizations can document inherited controls from certified
  third parties and link to their certification letters
- **Certification tracking**: Certification status, issue date, and expiration date

### User Roles in MyCSF
- **Organization Administrator**: Primary point of contact; manages the assessment account
- **Organization Contributor**: Business users who complete control responses
- **External Assessor (AEA)**: Validates responses and scores controls; must be registered
  as a HITRUST Authorized External Assessor
- **HITRUST Staff**: Performs QA review and issues certification letters

---

## 9. HITRUST Authorized External Assessors

### What is a HITRUST AEA?
A HITRUST Authorized External Assessor (AEA) is an organization that HITRUST has authorized
to perform validated assessments. AEAs must meet HITRUST's requirements for assessor training,
qualification, and quality standards.

### Finding an AEA
HITRUST maintains a public directory of Authorized External Assessors on the HITRUST website
(hitrustalliance.net). Organizations should evaluate assessors based on:
- Industry experience (healthcare, technology, financial services)
- Familiarity with the organization's technology stack (cloud providers, EHR systems)
- Assessment type experience (e1 vs i1 vs r2)
- References from similar organizations
- Geographic capability

### AEA Responsibilities
- Register the assessment engagement in MyCSF
- Conduct testing and validation of all in-scope controls
- Score each control at each maturity level
- Document findings and support CAP development
- Submit completed assessment to HITRUST for QA review
- Respond to HITRUST QA queries

### Important: Separation of Readiness and Validation
HITRUST requires that an organization does not use the same firm to perform both the
readiness/gap assessment and the validated assessment for some assessment types. Confirm
the current independence requirements with HITRUST or the assessor before engaging.

---

## 10. Certification Maintenance and Renewal

### e1 Renewal
- Certification expires after 1 year
- A new e1 validated assessment must be completed to renew
- No interim assessment required during the certification period

### i1 Renewal
- Certification expires after 1 year
- A new i1 validated assessment must be completed to renew
- No interim assessment required during the certification period
- Organizations may choose to upgrade to r2 at renewal

### r2 Renewal
- Certification expires after 2 years
- An interim assessment is required at the 12-month mark
- A full r2 validated assessment must be completed before the 2-year expiry

### Maintaining Certification Status
- Organizations must not experience significant negative changes in their control environment
  during the certification period
- Newly discovered material control failures should be reported
- Changes in scope (new systems, new business lines) may require an assessment update

---

## 11. Interim Assessment Requirements (r2 Only)

### Purpose of the Interim Assessment
The interim assessment ensures that the control environment remains effective and consistent
with the original r2 certification throughout the 2-year certification period.

### Timing
- Must be completed within the 12–18 month window following the certification letter
  issue date
- HITRUST recommends targeting the 12-month mark to allow time for any remediation needed

### Scope
- A subset of the originally assessed r2 controls are selected for interim review
- Selection is based on risk and coverage; HITRUST and the assessor determine the subset
- All open CAPs from the original assessment must be reviewed for progress

### Outcome
- If the interim assessment demonstrates continued compliance, the certification remains valid
- If material deficiencies are found, additional CAPs must be developed
- Severe failures may result in certification suspension pending remediation

# ISO/IEC 42001:2023 — AIMS Document Templates

This reference provides ready-to-use document templates for all mandatory and key supported AIMS documents. All templates are aligned to ISO/IEC 42001:2023 clause and control requirements.

> **Usage note:** Replace all `[PLACEHOLDER]` values with organisation-specific information. All templates use the standard document control header required for Clause 7.5 (Documented Information).

---

## Document Control Header (Standard — Use on All Documents)

```
Document Title:   [Document Name]
Document ID:      [ORG-AIMS-XXX]
Version:          1.0
Status:           Draft / Under Review / Approved
Owner:            [Role Title]
Approved By:      [Name and Title]
Approval Date:    [Date]
Next Review Date: [Date + 1 year]
Classification:   [Internal / Confidential / Public]
Related Standard: ISO/IEC 42001:2023
Related Clauses:  [e.g., 4.3, 5.2]
```

---

## Template 1: AIMS Scope Document

**Clause reference:** 4.3  
**Purpose:** Define the boundaries and applicability of the AI Management System.

```
Document ID: [ORG]-AIMS-SCO-001

1. ORGANISATION CONTEXT
   Organisation name: [Name]
   Sector / Industry: [e.g., Financial Services, Healthcare, Technology]
   AIMS Owner (top management): [Name and Title]
   Effective date: [Date]

2. AIMS SCOPE STATEMENT
   [Organisation Name] has established an AI Management System (AIMS) in accordance
   with ISO/IEC 42001:2023. The AIMS applies to the following:

   Organisational units in scope:
   - [List departments, business units, or locations included]

   Processes in scope:
   - [e.g., AI system development and deployment, AI procurement, AI operations]

   AI systems in scope:
   - [List each AI system by name — see AI System Register for full details]

3. EXPLICIT EXCLUSIONS
   The following are expressly excluded from the AIMS scope:
   - [Exclusion 1] — Justification: [Reason]
   - [Exclusion 2] — Justification: [Reason]

   Note: Exclusions must not affect the organisation's ability to achieve its AIMS objectives
   or violate applicable legal, regulatory, or contractual requirements.

4. INTERFACES AND DEPENDENCIES
   Related management systems:
   - [e.g., ISO 27001 ISMS — interfaces with Clause 4.3 of the ISMS]
   - [e.g., ISO 9001 QMS — shared document control procedures]

5. ORGANISATIONAL ROLE(S) UNDER ISO 42001
   [ ] AI provider — develops, trains, or deploys AI systems
   [ ] AI user — integrates or uses AI systems from third-party providers
   [ ] Both provider and user roles apply

6. REVISION HISTORY
   Version | Date | Author | Changes
   1.0     | [Date] | [Name] | Initial issue
```

---

## Template 2: AI System Register

**Clause reference:** 4 (context), 6.1.2 (risk/AISIA), 8 (operations)  
**Purpose:** Maintain an inventory of all AI systems within the AIMS scope.

```
Document ID: [ORG]-AIMS-REG-001

AI System Register — as at [Date]

| System ID | System Name | Version | Owner | Description / Intended Purpose | Development Model | Provider (if 3rd party) | In-scope AI systems | Risk Assessment ID | AISIA ID | AISIA Level | Status | Last reviewed |
|-----------|-------------|---------|-------|-------------------------------|-------------------|--------------------------|-----------|--------------------|----------|-------------|--------|---------------|
| AI-001    | [Name]      | [v1.0]  | [Role] | [What does it do and for what purpose] | [In-house / Third-party API / Hybrid] | [Vendor name if applicable] | [Yes / No] | [RA-001]       | [AISIA-001] | [Low/Med/High] | [Active / In development / Decommissioned] | [Date] |
| AI-002    |             |         |       |                               |                   |                          |           |                     |          |             |        |               |

Column definitions:
- Development Model: How the AI was built or sourced
- In-scope: Confirmed in AIMS scope (Yes) or excluded (No — requires justification)
- Status: Current operational status of the system
```

---

## Template 3: AI Policy

**Clause reference:** 5.2  
**Purpose:** Overarching AI governance commitment signed by top management.

```
Document ID: [ORG]-AIMS-POL-001

[ORGANISATION NAME] — AI POLICY

1. PURPOSE AND SCOPE
   This policy establishes [Organisation Name]'s commitment to the responsible development,
   deployment, and use of artificial intelligence (AI) systems. It applies to all AI systems
   within the AIMS scope defined in [ORG]-AIMS-SCO-001 and to all personnel who develop,
   operate, procure, or interact with AI systems on behalf of [Organisation Name].

2. POLICY STATEMENT
   [Organisation Name] is committed to:

   a) Implementing and maintaining an AI Management System that meets the requirements of
      ISO/IEC 42001:2023;

   b) Developing, deploying, and using AI systems responsibly, with respect for individual
      rights, societal wellbeing, and applicable law;

   c) Ensuring AI systems are transparent, fair, accountable, robust, and safe in their
      operation;

   d) Protecting the privacy and data rights of individuals whose data is used in AI systems;

   e) Ensuring meaningful human oversight of AI systems in proportion to their assessed
      impact level;

   f) Complying with all applicable legal, regulatory, and contractual requirements relating
      to AI;

   g) Continually improving the AIMS to reflect changes in AI systems, the regulatory
      environment, and the organisation's AI risk profile.

3. RESPONSIBLE AI PRINCIPLES
   This policy is informed by the following responsible AI attributes (per ISO/IEC 42001:2023
   Annex C):
   - Human agency and oversight
   - Technical robustness and safety
   - Privacy and data governance
   - Transparency
   - Diversity, non-discrimination, and fairness
   - Societal and environmental wellbeing
   - Accountability

4. ROLES AND RESPONSIBILITIES
   - [Top management role]: Approves and owns this policy; ensures resource allocation
   - [AIMS Owner]: Maintains and implements the AIMS
   - [AI Risk Owner (per system)]: Accountable for AI risk assessments and AISIA
   - All staff: Comply with this policy and related AI acceptable use requirements

5. MONITORING AND COMPLIANCE
   Compliance with this policy is monitored through:
   - Annual internal AIMS audits (Clause 9.2)
   - Management review (Clause 9.3)
   - AI risk assessment review cycle (Clause 6.1.2)

   Non-compliance is managed through the corrective action procedure [ORG]-AIMS-PRO-010.

6. RELATED DOCUMENTS
   - AIMS Scope Document: [ORG]-AIMS-SCO-001
   - AI Acceptable Use Policy: [ORG]-AIMS-POL-002
   - AI Risk Management Policy: [ORG]-AIMS-POL-003

7. REVISION HISTORY
   Version | Date | Author | Changes
   1.0     | [Date] | [Name] | Initial issue

Approved by: ___________________________
Name:        [Top Management Name]
Title:       [CEO / Managing Director / equivalent]
Date:        [Date]
```

---

## Template 4: AI Governance RACI Matrix

**Clause reference:** 5.3  
**Purpose:** Define roles, responsibilities, and accountability for AIMS activities.

```
Document ID: [ORG]-AIMS-RACI-001

R = Responsible (does the work)
A = Accountable (owns the outcome — only one per row)
C = Consulted (provides input)
I = Informed (notified of outcome)

| AIMS Activity | Top Mgmt | AIMS Owner | AI Risk Owner | AI System Owner | Data Governance Lead | IT / Security | Legal / Compliance | All Staff |
|-----------------|----------|------------|---------------|-----------------|---------------------|---------------|--------------------|-----------|
| Approve AI Policy | A | R | C | I | C | I | C | I |
| Define AIMS Scope | A | R | C | C | C | C | C | — |
| Conduct AI Risk Assessment | I | C | A/R | C | C | C | C | — |
| Conduct AISIA | I | C | A/R | C | C | I | C | — |
| Maintain AI System Register | I | A | R | R | I | I | I | — |
| Approve SoA | A | R | C | I | C | I | C | — |
| Set AI Objectives | A | R | C | C | C | I | C | — |
| Deliver AI Awareness Training | I | A | C | C | C | R | C | R |
| Manage AI Incident | I | A | C | R | C | R | C | R |
| Conduct Internal Audit | I | A | C | I | C | C | I | — |
| Conduct Management Review | A | R | C | I | C | C | C | — |
| Manage Corrective Actions | I | A | R | R | C | C | C | — |
| AI Supplier Assessment | I | C | A | R | C | C | C | — |
| Model Decommission | I | A | C | R | R | C | C | — |
```

---

## Template 5: AI Risk Assessment Record

**Clause reference:** 6.1.2, 8.2  
**Purpose:** Document AI-specific risk assessments for each in-scope AI system.

```
Document ID: [ORG]-AIMS-RA-[NNN]

AI RISK ASSESSMENT RECORD

AI System:          [System Name and Version] (AI-[NNN])
Assessment Date:    [Date]
Assessor:           [Name / Role]
Next Review Date:   [Date — recommended: annually or on significant change]

SECTION 1: AI SYSTEM SUMMARY
Intended purpose:   [What the system is designed to do]
Outputs produced:   [Decisions / Predictions / Classifications / Content / Recommendations]
Data inputs:        [Types of data fed into the system]
Deployment context: [Internal tool / Customer-facing / Regulatory context]

SECTION 2: RISK REGISTER

| Risk ID | Category | Risk Description | Likelihood (1-5) | Severity (1-5) | Score (L×S) | Rating | Treatment Decision | Controls to Apply | Residual Risk Score | Risk Owner | Review Date |
|---------|----------|-----------------|------------------|----------------|-------------|--------|-------------------|-------------------|---------------------|-----------|--------------|
| R-001   | Model — Bias | [Description] | [1-5] | [1-5] | [score] | [Low/Med/High/Crit] | [Modify/Accept/Avoid/Transfer] | [A.5.3, A.5.5] | [score after treatment] | [Role] | [Date] |
| R-002   | Data | | | | | | | | | | |
| R-003   | Operational | | | | | | | | | | |
| R-004   | Supply chain | | | | | | | | | | |

Risk rating: 1-4 = Low | 5-9 = Medium | 10-16 = High | 17-25 = Critical

SECTION 3: RISK TREATMENT SUMMARY
[Summarise treatment decisions and any residual risks accepted at management level]

SECTION 4: APPROVAL
Reviewed by: [AIMS Owner name / date]
Accepted by: [AI Risk Owner name / date — accountable for residual risk acceptance]
```

---

## Template 6: AI System Impact Assessment (AISIA)

**Clause reference:** 6.1.2, A.6.1, A.6.2, A.6.3  
**Purpose:** Assess impacts of each AI system on individuals and society.

```
Document ID: [ORG]-AIMS-AISIA-[NNN]

AI SYSTEM IMPACT ASSESSMENT (AISIA)

AISIA ID:           AISIA-[NNN]
AI System:          [System Name and Version] (AI-[NNN])
Assessment Date:    [Date]
Assessor:           [Name / Role]
Review Trigger:     [ ] Initial deployment  [ ] Significant change  [ ] Scheduled review
Next Review Date:   [Date]

SECTION 1: AI SYSTEM DESCRIPTION

Field                  | Detail
-----------------------|----------------------------------------
AI system name         | [Name]
Version                | [Version]
AI system owner        | [Name / Role]
Intended purpose       | [What the system is designed to do per A.5.1]
Output type            | [ ] Decision support  [ ] Autonomous decision  [ ] Content generation
                       | [ ] Classification  [ ] Prediction  [ ] Recommendation
Key inputs             | [List data types: names, scores, text, images, etc.]
Deployment context     | [Internal / Customer-facing / B2B / Regulatory / Public sector]
Operating conditions   | [When system is expected to perform correctly; any limitations]

SECTION 2: AFFECTED POPULATIONS

| Population ID | Population Description | How Affected | Number Affected (approx.) | Vulnerability Factors |
|--------------|----------------------|--------------|--------------------------|----------------------|
| P-001 | [e.g., Job applicants] | [e.g., AI screens CVs; affects hiring decisions] | [e.g., ~500/month] | [e.g., None identified / Protected characteristics / Socioeconomic status] |
| P-002 | [e.g., Existing employees] | | | |

Vulnerability factors to consider: age (children/elderly), disability, socioeconomic status,
minority group membership, limited AI literacy, power imbalance (employer/employee; government/citizen).

SECTION 3: IMPACT DIMENSIONS

For each affected population, assess:

| Dimension | Population P-001 | Population P-002 |
|-----------|-----------------|------------------|
| Nature of possible harm | [Financial / Physical / Psychological / Discrimination / Loss of opportunity / Reputational] | |
| Severity of worst-case impact | [1=Negligible to 5=Catastrophic] | |
| Breadth (number of people) | [Small number / Moderate / Large scale] | |
| Reversibility | [Easily reversible / Partially reversible / Difficult to reverse / Irreversible] | |
| Duration | [Short-term / Medium-term / Long-term / Permanent] | |
| Consent and awareness | [Individuals informed? Consent obtained where required?] | |
| Human oversight | [None / Review on request / Structured review / Mandatory before action] | |
| Recourse available | [General complaints / AI-specific appeal / Right to human decision-maker] | |

SECTION 4: SOCIETAL CONCERNS (A.6.3)
Assess broader societal impacts, if applicable:
- Potential for misinformation or manipulation at scale: [Yes / No / Limited]
- Labour displacement risk: [Yes / No / Limited]
- Environmental impact of AI compute: [High / Medium / Low / Not assessed]
- Reinforcement of systemic bias at scale: [Yes / No / Risk identified — describe]

SECTION 5: IMPACT CLASSIFICATION

Overall impact level:  [ ] Low   [ ] Medium   [ ] High

Justification: [Explain classification based on severity, breadth, reversibility, and vulnerability of affected populations]

SECTION 6: CONTROLS SELECTED

| Control Area | Control(s) Selected | Implementation Status |
|-------------|--------------------|-----------------------|
| Transparency (A.8.1) | [e.g., Disclosure notice on application form that AI is used] | [Planned / In progress / Implemented] |
| Human oversight | [e.g., All automated rejections reviewed within 3 business days] | |
| Bias testing (A.5.5) | [e.g., Monthly demographic disparity report] | |
| Documentation (A.5.6) | [e.g., Model card published internally] | |
| Monitoring (A.5.8) | [e.g., Weekly performance dashboard; alert at >5% drift] | |
| Recourse mechanism | [e.g., Dedicated email; human review within 10 days] | |

SECTION 7: RESIDUAL IMPACT ASSESSMENT
After applying selected controls, residual impact level: [ ] Low   [ ] Medium   [ ] High
Residual impact accepted by: [AI Risk Owner name] Date: [Date]

SECTION 8: REVIEW SCHEDULE
[ ] Low impact: review every 3 years or at significant change to AI system or operating context
[ ] Medium impact: review annually or at significant change
[ ] High impact: review every 6 months or at any change

Next scheduled AISIA review date: [Date]

SECTION 9: APPROVAL
Assessor: _________________________ Date: _______
AI Risk Owner: ____________________ Date: _______
AIMS Owner:   _________________________ Date: _______
```

---

## Template 7: Statement of Applicability (SoA)

**Clause reference:** 6.1.3  
**Purpose:** Lists all 38 Annex A controls with applicability decisions.

```
Document ID: [ORG]-AIMS-SOA-001

STATEMENT OF APPLICABILITY — ISO/IEC 42001:2023

Organisation: [Name]
Date: [Date]
Version: 1.0
AIMS Owner: [Name / Role]

Organisational role(s):
[ ] AI provider   [ ] AI user   [ ] Both

Notes on applicability:
- "Yes": Control is applicable and must be implemented
- "No": Control is not applicable — justification must be documented
- Implementation status: Not started / Planned / In progress / Implemented / Verified

| Control ID | Control Name | Applicable? | Justification for inclusion/exclusion | Implementation Status | Evidence Reference |
|-----------|-------------|-------------|---------------------------------------|----------------------|-------------------|
| A.2.1 | AI policy | Yes | Required for all AIMS | | |
| A.2.2 | AI-specific controls in organisational policies | Yes | Required for all AIMS | | |
| A.3.1 | Roles and responsibilities related to AI | Yes | Required for all AIMS | | |
| A.4.1 | Policies for AI system resources | [Yes/No] | [Provider: compute resource governance needed / User: not directly applicable] | | |
| A.4.2 | Human resource policies related to AI | Yes | Required for all — training and competence obligations | | |
| A.4.3 | Procurement policies for AI | Yes | All organisations procure AI tools or services | | |
| A.4.4 | Third-party AI capabilities | [Yes/No] | [Required if using third-party AI systems] | | |
| A.5.1 | AI system specifications | [Yes/No] | [Required for AI providers / Not primary for pure AI users] | | |
| A.5.2 | AI system design | [Yes/No] | [Provider only] | | |
| A.5.3 | Data management for AI systems | [Yes/No] | [Provider primary; user where training data held] | | |
| A.5.4 | AI system development | [Yes/No] | [Provider only] | | |
| A.5.5 | AI system verification and validation | [Yes/No] | [Provider primary; user where custom AI is developed] | | |
| A.5.6 | AI system documentation | Yes | Required for all — both provider and user document AI systems | | |
| A.5.7 | AI system deployment | [Yes/No] | [Provider primary] | | |
| A.5.8 | AI system operation and monitoring | Yes | All organisations operating AI systems must monitor them | | |
| A.6.1 | Processes for assessing impact of AI systems | Yes | Required for all — AISIA processes mandatory | | |
| A.6.2 | Assessing impacts on individuals | Yes | Required for all — individual impact assessment required | | |
| A.6.3 | Determining and assessing societal concerns | Yes | Required for all — societal impact assessment required | | |
| A.7.1 | Data management for AI | [Yes/No] | [Provider primary — AI-specific data governance framework] | | |
| A.7.2 | Data acquisition for AI | [Yes/No] | [Provider primary — controls on training data sourcing] | | |
| A.7.3 | Data quality for AI | [Yes/No] | [Provider primary — quality criteria for training/validation data] | | |
| A.7.4 | Data preparation for AI | [Yes/No] | [Provider primary — labelling and annotation controls] | | |
| A.8.1 | Transparency of AI systems | Yes | Required for all — disclosure obligations to affected individuals | | |
| A.8.2 | Communication of responsibilities to stakeholders | Yes | Required for all — stakeholder communication | | |
| A.8.3 | Reporting on AI incidents | Yes | Required for all — AI incident reporting process | | |
| A.9.1 | Policy for use of AI by third parties | Yes | All organisations engage third parties in some capacity | | |
| A.9.2 | Supply chain relationships | Yes | AI supply chain risk management | | |
| A.9.3 | Sharing of AI system data | [Yes/No] | [Applicable if organisation shares AI data with third parties] | | |
| A.9.4 | Interactions between AI systems | [Yes/No] | [Applicable if AI systems interact with other AI systems] | | |
| A.9.5 | Use of AI system by external entities | [Yes/No] | [Provider: applicable if customers use the AI system] | | |
| A.9.6 | Procurement of AI components | [Yes/No] | [Provider: applicable if procuring pre-trained models/datasets] | | |
| A.9.7 | Use of publicly available AI systems | Yes | Applicable if staff use public AI tools (ChatGPT, Copilot, etc.) | | |
| A.10.1 | AI system decommissioning policy | [Yes/No] | [Provider: applicable; User: limited applicability] | | |
| A.10.2 | Retention and disposal of AI system data | [Yes/No] | [Provider primary; User where AI training data held] | | |
| A.10.3 | Model deprecation | [Yes/No] | [Provider: applicable when models are retired] | | |
| A.10.4 | Reuse of data and models | [Yes/No] | [Provider: applicable if training data or models reused across systems] | | |
| A.10.5 | Archiving of AI systems | [Yes/No] | [Provider: applicable for audit trail purposes] | | |
| A.10.6 | Responsible AI system disposal | [Yes/No] | [Provider primary] | | |

Total applicable controls: [X] of 38
Total excluded controls: [Y] of 38

Statement: [Name, Role] confirms this SoA accurately reflects control applicability for
[Organisation Name]'s AIMS as of [Date].

Signed: _________________________  Date: _____________
```

---

## Template 8: AI Objectives Register

**Clause reference:** 6.2  
**Purpose:** Document measurable AI objectives aligned to Annex C responsible AI attributes.

```
Document ID: [ORG]-AIMS-OBJ-001

AI OBJECTIVES REGISTER

| Obj ID | Objective Description | Annex C Attribute | Clause/Control | Measure | Target | Reporting Frequency | Owner | Target Date | Status |
|--------|----------------------|------------------|----------------|---------|--------|--------------------||-------|-------------|--------|
| OBJ-001 | Complete AISIA for all in-scope AI systems | Accountability | Clause 6.1.2 | % AI systems with completed and approved AISIA | 100% | Quarterly | AIMS Owner | [Date] | [Status] |
| OBJ-002 | Achieve 100% AI awareness training completion | Human agency | Clause 7.3 | % staff who interact with AI systems having completed AI awareness training | 100% | Annually | HR / AIMS Owner | [Date] | |
| OBJ-003 | Reduce AI incident mean time to report | Accountability | A.8.3 | Average time from AI incident detection to formal incident record | < 4 hours | Quarterly | AI Incident Manager | [Date] | |
| OBJ-004 | Complete AI supplier assessments for all Tier 1 AI vendors | Societal wellbeing | A.9.2 | % Tier 1 AI suppliers with completed assessment | 100% | Bi-annually | AI Procurement Lead | [Date] | |
| OBJ-005 | Achieve fairness score within defined threshold for [AI System X] | Fairness | A.5.5 | [Fairness metric, e.g., demographic parity difference] < [threshold] | < [X]% | Monthly | AI System Owner | [Date] | |
| OBJ-006 | Attain ISO 42001 certification | Accountability | All clauses | Certification received | Certified | One-time milestone | AIMS Owner | [Date] | |
```

---

## Template 9: AI Incident Record

**Clause reference:** 8 (Operation), A.8.3  
**Purpose:** Document AI-specific incidents from detection through resolution.

```
Document ID: [ORG]-AIMS-INC-[NNN]

AI INCIDENT RECORD

Incident ID:         INC-[NNN]
Date reported:       [Date and time]
Reported by:         [Name / Role]
AI system affected:  [System Name + AI Register ID]
AI system owner:     [Name / Role]

SECTION 1: INCIDENT DESCRIPTION
Incident summary:    [Brief description — what happened]
Incident type:
[ ] Unexpected AI output         [ ] Bias or discriminatory outcome
[ ] Model performance degradation [ ] Data quality issue
[ ] Scope misuse                 [ ] Transparency failure
[ ] Security/adversarial event   [ ] Other: ___________

When detected:       [Date and time]
How detected:        [ ] Internal monitoring  [ ] User report  [ ] External complaint  [ ] Audit  [ ] Other
Individuals affected: [Number and description — if known]
Severity assessment:
[ ] Low — limited impact; no individuals harmed
[ ] Medium — moderate impact; potential individual harm; requires investigation
[ ] High — significant impact; individuals harmed; may require external notification
[ ] Critical — severe/irreversible impact; regulatory reporting likely required

SECTION 2: IMMEDIATE RESPONSE ACTIONS
Action | Taken by | Date/Time | Outcome
[Describe immediate containment actions] | [Name] | [Date/Time] | [Result]

AI system status:
[ ] Continues operating (risk managed)  [ ] Output manually reviewed  [ ] System suspended pending investigation

SECTION 3: INVESTIGATION
Root cause analysis: [Describe root cause — e.g., training data gap, model drift, scope creep, process failure]

Contributing factors: [List additional factors that contributed]

Impact assessment:
- Number of individuals affected:   [Number or "Not determined"]
- Nature of impact:                 [Describe]
- Data protection implications:     [ ] Yes — DPA notified  [ ] No  [ ] Under assessment
- Regulatory notification required: [ ] Yes — [Regulator and deadline]  [ ] No

SECTION 4: CORRECTIVE AND PREVENTIVE ACTIONS
Action | Owner | Due Date | Status
[Action 1] | [Name] | [Date] | [Status]

Corrective Action Record raised: [ ] Yes — CAR-[NNN]   [ ] No — rationale: [reason]

SECTION 5: CLOSURE
Incident closed date:  [Date]
Closed by:             [Name / Role]
Prevention confirmed:  [ ] Yes — [describe confirmation]  [ ] No — ongoing monitoring

SECTION 6: LESSON LEARNED
[Describe any changes to AI system, processes, controls, or guidance resulting from this incident]
```

---

## Template 10: Internal AIMS Audit Checklist

**Clause reference:** 9.2  
**Purpose:** Structured checklist for internal AIMS audits covering Clauses 4–10 and key Annex A controls.

```
Document ID: [ORG]-AIMS-AUD-[NNN]

INTERNAL AIMS AUDIT CHECKLIST

Audit reference:   AUD-[NNN]
Audit date:        [Date]
Auditor:           [Name / Role — must not audit own work]
Scope:             [Clauses and controls covered in this audit]
Scope reference:   AIMS Scope Document [ORG]-AIMS-SCO-001

CONFORMANCE RATINGS: C = Conforming | OFI = Opportunity for Improvement | NC = Nonconformity | N/A = Not applicable

CLAUSE 4 — CONTEXT
[ ] C [ ] OFI [ ] NC    4.1 Context analysis includes AI-specific external/internal issues
[ ] C [ ] OFI [ ] NC    4.2 Interested parties identified; requirements documented; AI-affected individuals included
[ ] C [ ] OFI [ ] NC    4.3 AIMS scope document is current; boundaries and exclusions justified
[ ] C [ ] OFI [ ] NC    4.4 AI system register is complete and current for all in-scope AI systems
Findings: [Notes]

CLAUSE 5 — LEADERSHIP
[ ] C [ ] OFI [ ] NC    5.1 Top management demonstrates active commitment; AI governance in management meetings
[ ] C [ ] OFI [ ] NC    5.2 AI policy is current, signed, communicated — includes responsible AI principles
[ ] C [ ] OFI [ ] NC    5.3 Roles and responsibilities defined (RACI); accountabilities assigned and understood
Findings: [Notes]

CLAUSE 6 — PLANNING
[ ] C [ ] OFI [ ] NC    6.1.2 AI risk assessment completed for all in-scope AI systems; documented
[ ] C [ ] OFI [ ] NC    6.1.2 AISIA completed for all in-scope AI systems; reviewed on schedule
[ ] C [ ] OFI [ ] NC    6.1.3 SoA covers all 38 Annex A controls; exclusions justified; current
[ ] C [ ] OFI [ ] NC    6.2  AI objectives are measurable; linked to Annex C attributes; tracked
Findings: [Notes]

CLAUSE 7 — SUPPORT
[ ] C [ ] OFI [ ] NC    7.2 Competence requirements defined; training completed; effectiveness evaluated
[ ] C [ ] OFI [ ] NC    7.3 All relevant staff aware of AI policy and their AIMS obligations
[ ] C [ ] OFI [ ] NC    7.4 Communication plan exists; AI-relevant communications have occurred
[ ] C [ ] OFI [ ] NC    7.5 Documented information maintained; controlled; retained per schedule
Findings: [Notes]

CLAUSE 8 — OPERATION
[ ] C [ ] OFI [ ] NC    8.1 Operational planning controls implemented for AI system lifecycle
[ ] C [ ] OFI [ ] NC    8.2 AI risk assessment executed and records retained
[ ] C [ ] OFI [ ] NC    8.3 Risk treatment plan implemented; treatment evidence retained
Findings: [Notes]

CLAUSE 9 — PERFORMANCE EVALUATION
[ ] C [ ] OFI [ ] NC    9.1 Monitoring metrics defined and measured; reports produced
[ ] C [ ] OFI [ ] NC    9.2 Internal audit conducted per schedule; report issued; NCs actioned
[ ] C [ ] OFI [ ] NC    9.3 Management review conducted; all required agenda items covered; minutes retained
Findings: [Notes]

CLAUSE 10 — IMPROVEMENT
[ ] C [ ] OFI [ ] NC    10.1 Continual improvement activities evidenced
[ ] C [ ] OFI [ ] NC    10.2 Nonconformities recorded; root cause investigated; corrective actions closed
Findings: [Notes]

SELECTED ANNEX A CONTROLS (sample — expand as per audit programme)
[ ] C [ ] OFI [ ] NC    A.5.5 Bias/fairness testing conducted; documented before deployment
[ ] C [ ] OFI [ ] NC    A.5.8 Production monitoring active; alert thresholds defined
[ ] C [ ] OFI [ ] NC    A.7  Training data quality; provenance documented
[ ] C [ ] OFI [ ] NC    A.8.1 Transparency: AI-affected individuals informed appropriately
[ ] C [ ] OFI [ ] NC    A.8.3 AI incident log active; incidents classified and actioned
[ ] C [ ] OFI [ ] NC    A.9.2 Supplier AI assessments completed; contractual AI clauses in place
[ ] C [ ] OFI [ ] NC    A.9.7 Acceptable use policy for public AI tools; staff aware
Findings: [Notes]

SUMMARY
Conformities:               [Number]
Opportunities for improvement: [Number]
Nonconformities:            [Number]

Nonconformities raised:
- NC-[NNN]: [Description] — Clause/Control: [ref]

Audit conclusion: [Overall assessment of AIMS conformance and effectiveness]

Auditor signature: _________________________ Date: _______
Auditee acceptance: ________________________ Date: _______
```

---

## Template 11: Management Review Agenda and Minutes

**Clause reference:** 9.3  
**Purpose:** Standard agenda and minutes template for management review of the AIMS.

```
Document ID: [ORG]-AIMS-MGMT-[NNN]

MANAGEMENT REVIEW — AIMS

Date:          [Date]
Chair:         [Top management attendee]
Attendees:     [Names and roles]
Apologies:     [Names]
Documents:     [List supporting documents circulated]

AGENDA (required by ISO 42001 Clause 9.3 b.i through b.ix)

1. ACTIONS FROM PREVIOUS MANAGEMENT REVIEW          [Status of each action]
2. CHANGES IN EXTERNAL/INTERNAL AI CONTEXT          [New regulations, new AI systems, organisational changes]
3. AI RISK ASSESSMENT RESULTS                       [Summary table: systems reviewed, risk ratings, changes]
4. AISIA RESULTS AND UPDATES                        [Impact classifications changed? New systems assessed?]
5. PERFORMANCE AGAINST AI OBJECTIVES (Clause 6.2)   [Dashboard — each objective: target vs actual]
6. INTERNAL AUDIT RESULTS                           [Audit findings, NC status, OFIs]
7. NONCONFORMITIES AND CORRECTIVE ACTIONS STATUS    [Open CARs, overdue actions]
8. AI INCIDENT SUMMARY                              [Incidents since last review, severity, lessons learned]
9. SUPPLIER AI ASSESSMENT STATUS                    [Key supplier assessments completed, outstanding]
10. OPPORTUNITIES FOR IMPROVEMENT                   [Ideas and proposals from AIMS team]
11. RESOURCE REQUIREMENTS                           [Budget, staffing, tooling needs for next period]

MINUTES

Item 1 — Actions from previous review:
[Status of each action from previous minutes]

Item 2 — Context changes:
[Decisions: e.g., New AI regulation noted: EU AI Act Article X came into force — action assigned]

Item 3 — AI risk assessment results:
[Summary: [X] AI systems reviewed this period. Risk profile update: [description]. Decisions: [e.g., one critical risk accepted with monitoring plan]]

[Continue for all agenda items]

DECISIONS AND ACTIONS
| Action | Owner | Due Date |
|--------|-------|----------|
| [Action description] | [Name/Role] | [Date] |

Next management review date: [Date]

Minutes approved by: _________________________
Name:                [Chair name]
Title:               [Title]
Date:                [Date]
```

---

## Template 12: Corrective Action Record

**Clause reference:** 10.2  
**Purpose:** Document nonconformities and track corrective actions through to verified closure.

```
Document ID: [ORG]-AIMS-CAR-[NNN]

CORRECTIVE ACTION RECORD

CAR ID:             CAR-[NNN]
Date raised:        [Date]
Raised by:          [Name / Role]
Source:             [ ] Internal audit  [ ] Management review  [ ] External audit  [ ] AI incident  [ ] Staff report  [ ] Other
Related NCI ref:    [Audit NC reference or incident ID if applicable]
Clause/Control:     [e.g., Clause 6.1.2 / A.5.5]

SECTION 1: NONCONFORMITY DESCRIPTION
[Describe what was observed and what the requirement is — be factual and specific]

Requirement:        [Quote the specific clause or control requirement not met]
Evidence of NC:     [What evidence demonstrates the nonconformity?]

SECTION 2: CONTAINMENT ACTION (Immediate)
Action taken to contain immediate impact:
[Describe immediate action taken to prevent further impact]
Completed by: [Name]   Date: [Date]

SECTION 3: ROOT CAUSE ANALYSIS
Method used: [ ] 5 Whys  [ ] Fishbone  [ ] Process analysis  [ ] Other: ______
Root cause identified: [Describe the underlying cause, not just the symptom]

SECTION 4: CORRECTIVE ACTION PLAN
| Action step | Owner | Due date | Status |
|-------------|-------|----------|--------|
| [Step 1]    | [Name] | [Date]  | [Not started/In progress/Complete] |
| [Step 2]    | [Name] | [Date]  | |

SECTION 5: EFFECTIVENESS REVIEW
Effectiveness review date: [Date — typically 30-90 days after corrective action completion]
Evaluation method: [How will the organisation confirm the root cause is resolved?]

Effectiveness confirmed: [ ] Yes — [Evidence confirming NCI is resolved and root cause eliminated]
                         [ ] No  — [New or revised corrective action required — raise new CAR]

SECTION 6: CLOSURE
CAR closed date:   [Date]
Closed by:         [AIMS Owner name / signature]
```

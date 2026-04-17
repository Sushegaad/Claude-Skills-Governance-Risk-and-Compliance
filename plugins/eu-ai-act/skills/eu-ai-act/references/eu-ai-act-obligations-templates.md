# EU AI Act — Obligations, Checklists, and Document Templates

**Regulation (EU) 2024/1689**
This reference provides structured checklists, document templates, and gap analysis tools for EU AI Act compliance.

---

## Part 1: Provider Compliance Checklist (High-Risk AI Systems)

Use this checklist to assess compliance status for a provider of a high-risk AI system. For each item, record status: Not Started (NS), In Progress (IP), Completed (C), Not Applicable (N/A).

### Phase 1: Pre-Market — Before Placing on Market or Putting into Service

| # | Obligation | Article(s) | Status | Evidence Required |
|---|-----------|------------|--------|------------------|
| 1.1 | Risk management system established, documented, and operational | Art. 9 | | Risk management plan, risk register, residual risk documentation |
| 1.2 | Data governance procedures in place for training, validation, and test data | Art. 10 | | Data governance policy, dataset documentation, bias evaluation records |
| 1.3 | Technical documentation (Annex IV) drawn up and complete | Art. 11 | | Annex IV document package |
| 1.4 | Logging/record-keeping capability built into the AI system | Art. 12 | | System architecture documentation showing logging; test logs |
| 1.5 | Instructions for use prepared and accompanying the system | Art. 13 | | Instructions for use document |
| 1.6 | Human oversight technical measures designed into the system | Art. 14 | | Human oversight specification; UI/UX documentation showing override controls |
| 1.7 | Accuracy, robustness, and cybersecurity levels determined and documented | Art. 15 | | Accuracy benchmark results; robustness testing records; cybersecurity assessment |
| 1.8 | Quality management system (QMS) established | Art. 17 | | QMS procedure documentation; QMS records |
| 1.9 | Conformity assessment route determined (internal or third-party) | Art. 43 | | Conformity assessment decision document |
| 1.10 | Conformity assessment completed | Art. 43 | | Conformity assessment report; Notified Body certificate (if applicable) |
| 1.11 | EU declaration of conformity (Annex V) drawn up | Art. 47 | | Signed EU declaration of conformity |
| 1.12 | CE marking affixed | Art. 48 | | Product/documentation bearing CE marking |
| 1.13 | Registration in EU database completed | Art. 49 | | EU database registration confirmation and reference number |
| 1.14 | Authorised representative in EU designated (if provider is outside EU) | Art. 25 | | Authorised representative agreement; details registered |
| 1.15 | AI literacy measures in place for relevant personnel | Art. 4 | | Training records; competency assessments |

### Phase 2: Post-Market — After Placing on Market

| # | Obligation | Article(s) | Status | Evidence Required |
|---|-----------|------------|--------|------------------|
| 2.1 | Post-market monitoring plan in operation | Art. 72 | | Post-market monitoring plan; monitoring data; review records |
| 2.2 | Logs retained for minimum 6 months (where technically feasible) | Art. 20 | | Log retention configuration; archived logs |
| 2.3 | Incident reporting procedure in place | Art. 73 | | Incident response procedure; incident log |
| 2.4 | Serious incidents reported to national authorities within required timeframes | Art. 73 | | Incident reports submitted; acknowledgements from authorities |
| 2.5 | Corrective actions taken when non-conformities identified | Art. 21 | | Non-conformity log; corrective action records |
| 2.6 | Technical documentation and records kept for 10 years | Arts. 11, 17 | | Document retention records |
| 2.7 | Re-assessment performed after substantial modification | Art. 19 | | Modification assessment record; updated conformity assessment |
| 2.8 | Cooperation with national competent authorities when requested | Art. 23 | | Correspondence with authorities; access logs provided |

---

## Part 2: Deployer Compliance Checklist (High-Risk AI Systems)

Use this checklist to assess compliance status for a deployer of a high-risk AI system.

| # | Obligation | Article(s) | Status | Evidence Required |
|---|-----------|------------|--------|------------------|
| D1 | AI system is used in accordance with provider's instructions for use | Art. 26(1) | | Usage policy; training records for users |
| D2 | Human oversight implemented — designated, competent, trained persons | Art. 26(2) | | Role assignments; training records; oversight procedures |
| D3 | Technical and organisational measures for human oversight in place | Art. 26(3) | | HO procedure; system configuration records |
| D4 | AI literacy measures implemented for relevant staff | Art. 4, Art. 26(5) | | Training records; competency assessments |
| D5 | AI system/use case monitored for risks; risks reported to provider | Art. 26(4) | | Monitoring log; incident/risk reports to provider |
| D6 | Fundamental Rights Impact Assessment (FRIA) conducted (Annex III systems) | Art. 27 | | Completed FRIA document; sign-off by senior management |
| D7 | Employees and their representatives informed before deployment (if system affects them) | Art. 26(7) | | Communication records; works council/employee rep consultation records |
| D8 | Registration in EU database completed (public authority deployers of Annex III systems) | Art. 49(2) | | EU database registration reference |
| D9 | Serious incidents reported to national market surveillance authorities | Art. 73 | | Incident reports; authority acknowledgements |
| D10 | Logs retained for minimum 6 months | Art. 26(6) | | Log retention configuration; archived logs |
| D11 | AI system not used for purposes beyond intended purpose without re-assessment | Art. 26(1) | | Use case documentation; review records |

---

## Part 3: GPAI Model Provider Compliance Checklist

### Standard GPAI Models (Art. 53)

| # | Obligation | Article | Status | Evidence Required |
|---|-----------|---------|--------|------------------|
| G1 | Technical documentation (Annex XI) drawn up and maintained | Art. 53(1)(a) | | Annex XI documentation |
| G2 | Information package for downstream providers (Annex XII) available | Art. 53(1)(b) | | Model card, API documentation, Annex XII document |
| G3 | Copyright compliance policy established; arts. 4(3) opt-outs respected | Art. 53(1)(c) | | Copyright policy; opt-out detection/compliance records |
| G4 | Training content summary published and current | Art. 53(1)(d) | | Published training summary |
| G5 | Notification to Commission within 2 weeks if compute exceeds 10^25 FLOPs | Art. 52 | | Notification confirmation |
| G6 | Codes of practice adherence determined (or alternative compliance approach documented) | Art. 56 | | Code of practice sign-up; or alternative compliance statement |

### Additional for Open-Weight GPAI Models (Art. 54)

| # | Obligation | Article | Status | Evidence Required |
|---|-----------|---------|--------|------------------|
| OW1 | Parameters/weights publicly available | Art. 54 | | Model release; licence |
| OW2 | Model architecture publicly available | Art. 54 | | Published architecture documentation |
| OW3 | Copyright policy in place (same as G3) | Art. 54 | | As G3 |
| OW4 | Training summary published (same as G4) | Art. 54 | | As G4 |
| OW5 | If systemic risk designation exists or compute > 10^25 FLOPs: full Art. 53 + Art. 55 apply | Art. 54(2) | | Re-run full checklist |

### Additional for GPAI Models with Systemic Risk (Art. 55)

| # | Obligation | Article | Status | Evidence Required |
|---|-----------|---------|--------|------------------|
| SR1 | Model evaluations conducted including adversarial testing | Art. 55(1)(a) | | Evaluation reports; red-teaming records; adversarial test results |
| SR2 | Systemic risks assessed and mitigated | Art. 55(1)(b) | | Systemic risk assessment; risk mitigation plan |
| SR3 | Serious incident tracking, documentation, and reporting process in place | Art. 55(1)(c) | | Incident tracking log; reports to AI Office |
| SR4 | Cybersecurity protection measures for model and infrastructure | Art. 55(1)(d) | | Cybersecurity assessment; access controls; penetration test results |

---

## Part 4: Fundamental Rights Impact Assessment (FRIA) Template (Article 27)

**Template: Fundamental Rights Impact Assessment**
**Pursuant to Article 27, Regulation (EU) 2024/1689 (EU AI Act)**

---

### Section 1: Administrative Information

| Field | Value |
|-------|-------|
| Deployer organisation name | |
| Deployer address | |
| Contact person for this FRIA | |
| Contact person email/phone | |
| AI system name | |
| AI system version/release | |
| Provider name | |
| Intended purpose of deployment | |
| Date of FRIA completion | |
| Review date | |
| Approved by (senior management) | |
| Title of approving officer | |

---

### Section 2: Description of Deployment Context

**2.1 Description of the process in which the high-risk AI system will be used:**
[Describe in detail the business process, workflow, or function in which the AI system will be used. Include the decision-making process it supports or automates.]

**2.2 Time period of intended use:**
[From date — to date, or "ongoing permanent deployment"]

**2.3 Frequency of use:**
[How often will the system be used? How many interactions/decisions per day/week/month?]

**2.4 Geographic scope:**
[Countries, regions, or specific locations where the system will be deployed]

**2.5 Categories of natural persons who will be affected:**
Identify all groups:

| Category of Persons | Direct Impact | Indirect Impact | Number Affected (approx.) |
|--------------------|--------------|----------------|--------------------------|
| [Insert group — e.g., job applicants] | Yes/No | Yes/No | [Number/estimate] |
| [Insert group — e.g., current employees] | Yes/No | Yes/No | |
| [Insert group — e.g., customers] | Yes/No | Yes/No | |
| [Insert vulnerable group — e.g., persons with disabilities] | Yes/No | Yes/No | |
| [Insert vulnerable group — e.g., minors] | Yes/No | Yes/No | |

---

### Section 3: Fundamental Rights Assessment

For each EU Charter article relevant to the deployment, assess the risk:

**Likelihood scale:** 1 = Highly unlikely, 2 = Unlikely, 3 = Possible, 4 = Likely, 5 = Highly likely
**Severity scale:** 1 = Negligible, 2 = Minor, 3 = Moderate, 4 = Significant, 5 = Severe/Irreversible

| Charter Article | Fundamental Right | Potential Risk | Likelihood (1-5) | Severity (1-5) | Risk Level | Affected Group |
|----------------|------------------|---------------|-----------------|---------------|------------|---------------|
| Art. 1 | Human dignity | | | | | |
| Art. 3 | Physical and mental integrity | | | | | |
| Art. 7 | Respect for private and family life | | | | | |
| Art. 8 | Protection of personal data | | | | | |
| Art. 11 | Freedom of expression and information | | | | | |
| Art. 14 | Right to education | | | | | |
| Art. 15 | Freedom to choose an occupation and engage in work | | | | | |
| Art. 17 | Right to property | | | | | |
| Art. 20 | Equality before the law | | | | | |
| Art. 21 | Non-discrimination (race, sex, religion, disability, age, sexual orientation, etc.) | | | | | |
| Art. 22 | Cultural, religious, and linguistic diversity | | | | | |
| Art. 23 | Equality between women and men | | | | | |
| Art. 24 | Rights of the child | | | | | |
| Art. 25 | Rights of the elderly | | | | | |
| Art. 26 | Integration of persons with disabilities | | | | | |
| Art. 38 | Consumer protection | | | | | |
| Art. 41 | Right to good administration | | | | | |
| Art. 47 | Right to an effective remedy and fair trial | | | | | |
| Art. 48 | Presumption of innocence and right of defence | | | | | |

**Overall Risk Rating:** [ ] Low [ ] Medium [ ] High

---

### Section 4: Risk Mitigation Measures

For each risk identified as Medium or High in Section 3:

| Risk Reference | Risk Description | Mitigation Measure | Responsible Party | Implementation Date | Residual Risk | Monitoring Approach |
|---------------|----------------|-------------------|------------------|--------------------|--------------|--------------------|
| | | | | | | |

---

### Section 5: Consultation and Stakeholder Engagement

**5.1 Internal consultation:**
[Record who was consulted within the deployer organisation — DPO, legal, HR, IT, affected business units]

| Stakeholder | Role | Date Consulted | Input Received |
|-------------|------|---------------|----------------|
| | | | |

**5.2 External consultation (where applicable):**
[Record any external consultation — e.g., works council, employee representatives, external legal advice]

**5.3 Employee / works council consultation (Art. 26(7)):**
[ ] Employees and their representatives were informed of the intended deployment before deployment
[ ] Works council / employee representative body was consulted on [date]

---

### Section 6: Data Protection Alignment

**6.1 Is a DPIA (under GDPR Art. 35) required for this deployment?**
[ ] Yes — DPIA reference: ________________
[ ] No — Reason: ________________

**6.2 Legal basis for processing personal data:**
[ ] Art. 6(1)(a) GDPR — Consent
[ ] Art. 6(1)(b) — Contract
[ ] Art. 6(1)(c) — Legal obligation
[ ] Art. 6(1)(e) — Public task
[ ] Art. 6(1)(f) — Legitimate interests
[ ] Other: ________________

**6.3 Special category data involved?**
[ ] Yes — Categories: ________________ — Legal basis under Art. 9(2) GDPR: ________________
[ ] No

---

### Section 7: Approval and Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior management approver | | | |
| Data Protection Officer (review) | | | |
| Legal/Compliance review | | | |
| AI Literacy / HR confirmation | | | |

**Next review date:** ________________
**Trigger events for early review:** Substantial change to AI system; change in intended use; new risk information; significant incident; regulatory guidance update.

---

## Part 5: Technical Documentation Outline (Annex IV Compliance)

Use this outline to structure the technical documentation required by Article 11 and Annex IV.

### Document Control Block (for each technical documentation package)

| Field | Value |
|-------|-------|
| AI System Name | |
| Version | |
| Provider Name | |
| Document ID | |
| Version | 1.0 |
| Classification | Confidential — for regulatory and authorised commercial use |
| Prepared by | |
| Approved by | |
| Date | |
| Review date | |
| Retention period | 10 years from date of placing on market |

### Required Sections (Annex IV)

**Section 1 — General Description**
- 1.1 Intended purpose (complete specification per Art. 3(11))
- 1.2 Version, date of development, and history
- 1.3 Names and contact details of provider (and authorised representative where applicable)
- 1.4 Hardware on which system is intended to operate
- 1.5 How system interacts with hardware, software, or other AI systems
- 1.6 Form in which the AI system is placed on market (embedded, software, API, SaaS, etc.)
- 1.7 Natural persons affected by the system and use cases

**Section 2 — Description of the AI System and Development Process**
- 2.1 Development methodologies and third parties involved
- 2.2 Design specifications including general logic, key design choices and assumptions
- 2.3 Architecture of the system — description of components, modules, models
- 2.4 Training methodology and key decisions in training
- 2.5 Training data — type, source, size, selection criteria, collection methodology
- 2.6 Validation data — type, source, size
- 2.7 Testing data — type, source, size, test methodology
- 2.8 Human oversight technical measures designed in (Art. 14)
- 2.9 Pre-determined changes to the AI system and its performance (anticipated system drift)

**Section 3 — Risk Management System Records**
- 3.1 Risk management system description (Art. 9 process)
- 3.2 Known and foreseeable risks identified
- 3.3 Risk mitigation measures adopted
- 3.4 Residual risks remaining after mitigation
- 3.5 Testing results — metrics, benchmarks, methodologies

**Section 4 — Accuracy, Robustness, and Cybersecurity**
- 4.1 Accuracy levels and metrics
- 4.2 Performance across different persons or groups of persons
- 4.3 Robustness testing results
- 4.4 Cybersecurity measures and testing results

**Section 5 — Changes Made After Initial Placing on Market**
- 5.1 Record of all changes/updates and dates
- 5.2 Assessment of whether each change constitutes a substantial modification
- 5.3 Updated conformity assessment records where substantial modification identified

**Section 6 — Standards and Specifications Applied**
- 6.1 Harmonised standards applied (with version numbers)
- 6.2 Common specifications applied
- 6.3 Where standards not applied: description of technical solutions adopted to meet requirements
- 6.4 Other relevant industry standards or codes of practice

**Section 7 — Referenced Documents**
- 7.1 EU Declaration of Conformity (Annex V)
- 7.2 Post-market monitoring plan (Annex VII framework)
- 7.3 Instructions for use
- 7.4 Quality Management System documentation reference

---

## Part 6: EU Declaration of Conformity (Annex V Format)

**EU DECLARATION OF CONFORMITY**
*(Pursuant to Article 47 and Annex V, Regulation (EU) 2024/1689)*

---

**No.** [Unique reference number]

**1. AI system name and type:**
[Name of AI system; model/type reference]

**2. Provider name and address:**
[Full legal name and registered address]

**3. Authorised representative (where applicable):**
[Name and address of authorised representative in the Union]

**4. This declaration of conformity is issued under the sole responsibility of the provider.**

**5. Object of the declaration:**
[Brief description of the AI system and its intended purpose]

**6. The object of the declaration described above is in conformity with the relevant Union harmonisation legislation:**
Regulation (EU) 2024/1689 (Artificial Intelligence Act)

**7. References to the relevant harmonised standards used or references to any other technical specifications in relation to which conformity is declared:**
[List harmonised EN standards applied, e.g., EN ISO/IEC 42001, EN standards under AI Act mandate]
[Or: Description of alternative technical specifications used per Art. 41]

**8. Where applicable, name, address, and identification number of the Notified Body that carried out the conformity assessment procedure:**
[Notified Body name; EU notified body number; certificate reference and date]

**9. Additional information (where applicable):**
[Any additional compliance declarations or conditions]

**Signed for and on behalf of:**
[Name and company, place and date, signature]
[Function/title of signatory]

---

## Part 7: Serious Incident Report Template (Article 73)

**HIGH-RISK AI SYSTEM — SERIOUS INCIDENT REPORT**
*(Pursuant to Article 73, Regulation (EU) 2024/1689)*

**Report type:** [ ] Initial report [ ] Follow-up report [ ] Final report

**Submission date:** ________________
**Reference number** (if follow-up): ________________

**Section A — Provider Information**
- Provider name and address:
- Contact person name, role, phone, and email:
- AI system name and version:
- EU database registration number:

**Section B — Incident Description**
- Date and time incident first identified:
- Date and time incident occurred (if different):
- Location/Member State(s) affected:
- Nature of the incident (describe what happened):
- Type of serious incident (tick all that apply):
  - [ ] Death or risk of death
  - [ ] Serious injury to health
  - [ ] Serious irreversible disruption to management/operation of critical infrastructure
  - [ ] Infringement of fundamental rights obligations
  - [ ] Serious property damage or other significant harm
- Number of persons affected (if known):
- Description of affected persons:

**Section C — AI System Actions Preceding the Incident**
- What was the AI system doing at the time of the incident?
- What input data was processed?
- What output did the AI system generate?
- Was the AI system operating within its intended purpose?

**Section D — Immediate Corrective Actions Taken**
- Immediate steps taken to stop/mitigate harm:
- Has the AI system been taken offline/suspended? [ ] Yes [ ] No
- Actions to prevent recurrence (preliminary):
- Has affected person(s) been notified? [ ] Yes [ ] No [ ] Not applicable

**Section E — Preliminary Hypothesis on Cause**
[Describe what is currently believed to have caused the incident. Mark as preliminary if investigation is ongoing.]

**Section F — Follow-Up Plans**
- Expected investigation completion date:
- Next reporting milestone:
- Contact for further communication with authorities:

**Signed by:** ________________ **Title:** ________________ **Date:** ________________

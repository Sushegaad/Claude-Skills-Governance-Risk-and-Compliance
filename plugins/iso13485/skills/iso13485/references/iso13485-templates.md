# ISO 13485:2016 — Document Templates Reference

## Overview

This file contains structured templates for the most commonly required ISO 13485:2016 QMS documents. Each template includes a document control block and all sections required by the standard.

Templates provided:
1. Quality Manual (outline and section guide)
2. CAPA Form
3. Nonconformance Report (NCR) Form
4. Complaint Record Form
5. Management Review Meeting Agenda and Record
6. Internal Audit Plan and Report
7. Supplier Evaluation Form
8. Design Change Request Form
9. Process Validation Protocol Outline
10. Risk Management Plan (ISO 14971) Outline

---

## Template 1 — Quality Manual Outline

```
[ORGANISATION NAME]
QUALITY MANUAL

Document ID: QM-001
Version: [X.X]
Author: [Quality Manager / PRRC]
Approved by: [CEO / VP Quality / Top Management]
Effective Date: [Date]
Next Review: [Date + 1 year]
Classification: Controlled Document

REVISION HISTORY:
Version | Date | Author | Summary of Changes
1.0 | [Date] | [Name] | Initial release

---

SECTION 1 — PURPOSE AND SCOPE
1.1 Purpose
This Quality Manual defines the Quality Management System (QMS) of [Organisation Name]
and demonstrates compliance with ISO 13485:2016.

1.2 Scope of QMS
The QMS covers:
[Describe the scope using product types, device families, processes, and sites covered]

Example: "The design, development, manufacture, and distribution of [device types] at
[site address(es)]."

1.3 Exclusions (Clause 7 only — must be justified)
Clause [e.g., 7.3 — Design and Development] is excluded from the scope of this QMS because:
[Justification — e.g., "The organisation manufactures exclusively to customer-provided
complete design documentation. No design authority is held by this organisation."]

Clauses 7.5.3 (Installation) and 7.5.4 (Servicing) are excluded because:
[Justification — e.g., "Products are sold direct to hospitals; installation and servicing
are performed by the hospital clinical engineering team."]

---

SECTION 2 — ORGANISATION
2.1 Organisation overview
[Brief description of the organisation, products, markets, key sites]

2.2 Organisational structure
[Refer to Organisation Chart — separate document, or include here]

2.3 Roles with quality responsibility
Role | Responsibility | Clause Reference
Top Management | Quality policy; management commitment; resource provision | 5.1
Management Representative | QMS implementation; regulatory compliance reporting | 5.5.2
Quality Assurance Manager | QMS maintenance; CAPA; audits; document control | 4.2, 8.2.4, 8.5.2
Regulatory Affairs Manager | Regulatory submissions; regulatory change monitoring | 5.2, 8.2.3
Production Manager | Production controls; process compliance | 7.5.1
R&D / Engineering Manager | Design and development (if in scope) | 7.3

---

SECTION 3 — QUALITY MANAGEMENT SYSTEM (Clause 4)
3.1 QMS documentation structure
[Describe the documentation hierarchy — typically: Quality Manual → SOPs → Work Instructions → Forms/Records]

3.2 Document control
[Reference SOP-DC-001 — Control of Documents]

3.3 Record control
[Reference SOP-RC-001 — Control of Records]
Record retention policy: Minimum [device design lifetime] + 2 years, with a minimum of
[specify — e.g., 10 years]. Implantable device records: minimum 15 years or device
design lifetime + 2 years (whichever is longer).

3.4 Medical Device File
A Medical Device File (MDF) / Device Master Record is maintained for each device type
or family. [Reference MDF index or device file procedure]

---

SECTION 4 — MANAGEMENT RESPONSIBILITY (Clause 5)
4.1 Management commitment
[Reference management commitment statement and quality policy]

4.2 Quality policy
[Include or reference the signed quality policy document]

4.3 Quality objectives
Quality objectives are established, documented, and reviewed at management review.
[Reference Quality Objectives Register — QBJ-001]

4.4 Management review
Management reviews are conducted [frequency — e.g., annually or more frequently if
quality trends indicate]. [Reference SOP-MR-001]

---

SECTION 5 — RESOURCE MANAGEMENT (Clause 6)
5.1 Human resources and competence
[Reference Competence Matrix and Training Records procedure]

5.2 Infrastructure
Infrastructure is maintained per the infrastructure maintenance schedule.
[Reference Infrastructure Maintenance Procedure]

5.3 Work environment
[Reference Work Environment Control procedure — including environmental monitoring
if applicable for cleanroom / controlled environment production]

---

SECTION 6 — PRODUCT REALIZATION (Clause 7)
6.1 Planning
[Reference Quality Plan procedure and Risk Management SOP]

6.2 Customer-related processes
[Reference Customer Requirements and Order Review procedure]

6.3 Design and development
[Reference Design Controls procedure — SOP-DD-001 — or state exclusion with justification]

6.4 Purchasing
[Reference Purchasing and Supplier Management procedure — SOP-PUR-001]

6.5 Production and service provision
[Reference Production Controls procedure / Work Instructions]

6.6 Control of monitoring and measuring equipment
[Reference Calibration and Measurement Equipment Control procedure]

---

SECTION 7 — MEASUREMENT, ANALYSIS, AND IMPROVEMENT (Clause 8)
7.1 Monitoring and measurement
[Reference Feedback, Complaint Handling, and Internal Audit procedures]

7.2 Control of nonconforming product
[Reference NC Product Control procedure — SOP-NC-001]

7.3 Analysis of data
Data is collected and analysed from feedback, audits, process performance, and NC
product. Analysis outputs are reviewed at management review.

7.4 Improvement
[Reference CAPA procedure — SOP-CAPA-001]

---

SECTION 8 — RELATED DOCUMENTS
8.1 Procedures and work instructions
[List all controlled SOPs and work instructions or reference the Master Document List]

8.2 Forms and templates
[Reference forms register or list key forms]

---

APPENDIX A — PROCESS INTERACTION MAP
[Diagram or table showing how core QMS processes interact, with clause references]
```

---

## Template 2 — CAPA Form

```
CORRECTIVE AND PREVENTIVE ACTION RECORD

CAPA ID: CAPA-[YYYY]-[NNN]
Type: [ ] Corrective Action   [ ] Preventive Action
Date Opened: [Date]
Priority: [ ] Critical   [ ] Major   [ ] Minor
Opened by: [Name / Role]

SOURCE OF CAPA:
[ ] Complaint (Complaint ID: __________)
[ ] Internal audit (Audit ID: __________)
[ ] External audit (Auditor: __________)
[ ] NC product (NCR ID: __________)
[ ] Process performance data
[ ] Post-market surveillance / feedback
[ ] Management review
[ ] Regulatory authority finding
[ ] Employee / supplier observation
[ ] Other: __________

SECTION 1 — PROBLEM STATEMENT
Describe the problem clearly (What, When, Where, Who, How often):
[Free text — be specific and factual]

Device / product affected (if applicable): [Description + lot/serial/UDI if applicable]
Regulatory markets potentially affected: [ ] EU   [ ] USA   [ ] Canada   [ ] Australia   [ ] Japan   [ ] Other

SECTION 2 — IMMEDIATE CONTAINMENT ACTIONS
Actions taken to contain the problem and prevent further impact:
Action | Responsible | Completed Date
| |
| |

Containment actions completed by: [Date]
Confirmed by (QA): [Name / Date]

SECTION 3 — ROOT CAUSE ANALYSIS
Method used: [ ] 5-Why   [ ] Fishbone / Ishikawa   [ ] Fault Tree Analysis   [ ] Other: ________

5-Why analysis (if used):
Why 1: [Problem description]  →  Because: [Answer 1]
Why 2: [Answer 1]             →  Because: [Answer 2]
Why 3: [Answer 2]             →  Because: [Answer 3]
Why 4: [Answer 3]             →  Because: [Answer 4]
Why 5: [Answer 4]             →  Because: [Root cause]

Root cause identified:
[Clear statement of root cause]

Contributing factors (if any):
[Contributing factor 1]
[Contributing factor 2]

Evidence supporting root cause determination:
[Reference data, records, analysis results]

SECTION 4 — CORRECTIVE / PREVENTIVE ACTIONS

Action | Responsible person | Target Date | Completion Date | Evidence reference
| | | |
| | | |
| | | |

SECTION 5 — EFFECTIVENESS VERIFICATION

Verification method: [ ] Re-audit   [ ] Data trend analysis   [ ] Re-inspection   [ ] Surveillance   [ ] Other
Verification criteria (define what "effective" means):
[Quantitative or qualitative criterion, e.g., "Zero recurrence of similar NCs in next 3 internal audits"]

Verification performed by: [Name / Role]
Verification date: [Date]
Verification results: [ ] Effective — CAPA may be closed   [ ] Not Effective — CAPA remains open; extend actions

Evidence of verification:
[Reference records, audit report, data set]

SECTION 6 — CLOSURE

All actions completed: [ ] Yes   [ ] No (if No, CAPA remains open)
Regulatory reporting required: [ ] Yes (reference report number: ________) [ ] No
Related CAR / NCR closed: [ ] Yes   [ ] N/A
Documents updated: [ ] Yes — list: _________   [ ] No — justification: _________

Closed by (QA): [Name] _________________ Date: _____________
Approved by (Management): [Name] _________________ Date: _____________
```

---

## Template 3 — Nonconformance Report (NCR) Form

```
NONCONFORMANCE REPORT

NCR ID: NCR-[YYYY]-[NNN]
Date raised: [Date]
Raised by: [Name / Role]
Department/Location: [Location where NC discovered]

PRODUCT / PROCESS DETAILS:
Product name / description: [Product]
Part number / model: [Number]
Lot / batch number: [Number]
Serial number(s): [Numbers]
UDI (if applicable): [UDI string]
Quantity affected: [Number and unit]

NONCONFORMANCE DESCRIPTION:
Requirement not met (reference clause/specification/drawing): [Reference]
Description of nonconformity: [Factual description — what was found, not why]
Where detected: [ ] Incoming inspection   [ ] In-process   [ ] Final inspection   [ ] Post-delivery / customer

Potentially affected downstream: [ ] Yes — specify extent: _____________   [ ] No   [ ] Unknown

DISPOSITION DECISION (8.3):
Disposition: [ ] Accept as-is (concession)   [ ] Rework   [ ] Regrade   [ ] Reject/Scrap   [ ] Return to supplier

Concession justification (if accept as-is):
[Risk assessment reference; justification that product remains safe and effective despite NC]
Customer / regulatory approval required for concession: [ ] Yes (approval obtained — reference: ________) [ ] No

Rework instructions reference (if rework): SOP-RW-_________

Person authorising disposition: [Name] _________________ Role: _________ Date: _________

POST-REWORK INSPECTION (if rework performed):
Re-inspection results: [ ] Pass   [ ] Fail
Inspection records reference: [Reference]
Inspected by: [Name] _________________ Date: _________

CAPA REQUIRED?
[ ] Yes — CAPA opened: CAPA-[YYYY]-[NNN]
[ ] No — Justification (e.g., isolated occurrence, no systemic root cause): [Justification]

NCR CLOSED BY (QA): [Name] _________________ Date: _____________
```

---

## Template 4 — Complaint Record Form

```
COMPLAINT RECORD

Complaint ID: COMP-[YYYY]-[NNN]
Date received: [Date]
Received by: [Name / Role]
Received via: [ ] Phone   [ ] Email   [ ] Field service   [ ] Distributor   [ ] Direct customer   [ ] Regulatory authority   [ ] Other

COMPLAINANT INFORMATION:
Name: [Or anonymous if preference stated]
Organisation: [Hospital, clinic, distributor name]
Country: [Country]
Contact details: [Email / phone — if provided]

DEVICE INFORMATION:
Product name: [Product]
Model / catalogue number: [Number]
Lot / serial number: [Number]
UDI: [UDI string if applicable]
Date of manufacture (if known): [Date]
Date of alleged incident: [Date]

COMPLAINT DESCRIPTION:
[Full description of complaint as reported by complainant]

Patient outcome (if applicable):
[ ] Death   [ ] Serious injury   [ ] Non-serious injury   [ ] No patient harm   [ ] Unknown

INITIAL TRIAGE:
Potential regulatory reportable event: [ ] Yes   [ ] No   [ ] Under investigation
Immediate safety concern requiring containment: [ ] Yes — action taken: _________   [ ] No
FSCA trigger assessment required: [ ] Yes   [ ] No

INVESTIGATION:
Investigated by: [Name / Role]
Investigation start date: [Date]
Device returned for analysis: [ ] Yes   [ ] No
Analysis results summary: [Findings from device analysis]
Root cause (final): [Root cause determination]
Root cause category: [ ] Manufacturing defect   [ ] Design issue   [ ] User error   [ ] Labelling/IFU issue   [ ] Storage/transport   [ ] Unknown   [ ] Other

REGULATORY REPORTING:
Report required: [ ] Yes   [ ] No
Report type: [ ] EU MDR Vigilance   [ ] FDA MDR (803)   [ ] Health Canada MPR   [ ] TGA   [ ] MHLW   [ ] Other
Report reference number: [Number]
Date submitted: [Date]

CORRECTIVE ACTION:
CAPA required: [ ] Yes — CAPA ID: CAPA-_________   [ ] No
Action taken: [Description]

CLOSURE:
Communication to complainant: [ ] Yes   [ ] No   [ ] Not appropriate
Closure summary: [Brief summary of outcome and actions]
Closed by: [Name] _________________ Date: _____________
QA review: [Name] _________________ Date: _____________
```

---

## Template 5 — Management Review Meeting Record

```
MANAGEMENT REVIEW RECORD

Meeting ID: MR-[YYYY]-[N]
Date: [Date]
Location: [Location / virtual]
Next scheduled review: [Date]

ATTENDEES:
Name | Role | Present (Y/N)
[CEO / Managing Director | Top Management | ]
[Quality Manager | QA | ]
[Regulatory Affairs Manager | RA | ]
[Production Manager | Operations | ]
[R&D / Engineering Manager | Engineering (if D&D in scope) | ]
[Sales / Marketing Manager | Commercial | ]

AGENDA AND INPUTS (ISO 13485:2016 Clause 5.6.2):

1. Actions from previous management review
   Status of open actions from MR-[previous ID]:
   [List open actions, responsible person, updated status]

2. Results of audits
   Internal audits: [Summary — number of findings, open CAPAs]
   External audits (NB / FDA / MDSAP): [Findings, certificates status]

3. Customer feedback
   Complaint summary (period [dates]):
   - Total complaints received: [Number]
   - Serious complaints: [Number]
   - Regulatory reports filed: [Number]
   - Trending: [Improving / Stable / Declining / Concerning]
   Other feedback (distributor, post-market surveillance data):

4. Process performance and product conformity
   KPI summary:
   KPI | Target | Actual | Trend
   On-time delivery | ≥95% | [%] | [+/-/=]
   First pass yield | ≥[X]% | [%] | [+/-/=]
   Complaint rate per unit | ≤[X] | [Rate] | [+/-/=]
   NC product rate | ≤[X]% | [%] | [+/-/=]
   CAPA closure on-time | ≥90% | [%] | [+/-/=]

5. Status of corrective and preventive actions
   Open CAPAs: [Number] — [brief status summary]
   CAPAs closed since last review: [Number]

6. Changes affecting the QMS
   Regulatory changes: [Describe any new/revised regulations, standards]
   Product/process changes: [Describe any significant changes]
   Organisational changes: [Describe any restructuring, key personnel changes]

7. New or revised regulatory requirements
   [List any new or revised regulatory requirements applicable to markets in scope]

8. Recommendations for improvement
   [List recommendations raised]

9. Any other business

OUTPUT DECISIONS AND ACTIONS (Clause 5.6.3):
Action | Responsible Person | Due Date
| |
| |

QUALITY OBJECTIVES REVIEW:
Objective | Target | Status | Action (if missed)
| | |
| | |

QMS SUITABILITY DETERMINATION:
The QMS is determined to be: [ ] Suitable and effective   [ ] Suitable with improvement actions (see above)
[ ] Requires significant revision — action plan attached

Chaired by: [Name] / [Role] _________________ Date: _____________
Quality Manager review: [Name] _________________ Date: _____________

Minutes distributed to: All attendees [Date: _____________]
```

---

## Template 6 — Internal Audit Plan and Report Outline

```
INTERNAL AUDIT PLAN

Audit ID: AUD-[YYYY]-[NNN]
Planned date(s): [Date(s)]
Lead auditor: [Name / Qualification]
Audit team: [Names]
Audit scope: [Clauses / processes / departments in scope]
Audit criteria: ISO 13485:2016; applicable regulatory requirements; [Organisation]-QMS documented procedures

AUDIT SCHEDULE:
Date / Time | Area / Process | Clause(s) | Auditee(s) | Auditor
| | | |
| | | |

OPENING MEETING: [Date / Time]
CLOSING MEETING: [Date / Time]

---

INTERNAL AUDIT REPORT

Audit ID: AUD-[YYYY]-[NNN]
Audit dates: [Dates]
Audit scope: [Scope as above]
Standard(s): ISO 13485:2016

SUMMARY OF FINDINGS:
Finding type | Number
Major nonconformity | [Number]
Minor nonconformity | [Number]
Observation / Opportunity for improvement | [Number]

MAJOR NONCONFORMITIES:
Finding ID | Clause | Description | Evidence | Required action
| | | |

MINOR NONCONFORMITIES:
Finding ID | Clause | Description | Evidence | Required action
| | | |

OBSERVATIONS:
Finding ID | Clause | Description
| |

POSITIVE FINDINGS (commendations):
[List areas of good practice noted during audit]

AUDIT CONCLUSION:
Overall QMS suitability: [ ] Satisfactory   [ ] Satisfactory with actions   [ ] Unsatisfactory

CAPA REQUIRED FOR NONCONFORMITIES: [ ] Yes — CAPA IDs: ___________

Lead auditor signature: _________________ Date: _____________
Auditee management acknowledgement: _________________ Date: _____________
QA Manager review: _________________ Date: _____________
```

---

## Template 7 — Supplier Evaluation Form

```
SUPPLIER EVALUATION RECORD

Evaluation ID: SUP-EVAL-[YYYY]-[NNN]
Supplier name: [Name]
Supplier address: [Address]
Date of evaluation: [Date]
Evaluator: [Name / Role]
Evaluation type: [ ] Initial qualification   [ ] Periodic re-evaluation   [ ] For cause

PRODUCTS / SERVICES SUPPLIED:
[List products, components, or services under evaluation]

SUPPLIER CRITICALITY:
[ ] Critical (affects device safety or performance directly)
[ ] Major (significant quality impact)
[ ] Minor (indirect quality impact)

EVALUATION CRITERIA:
Criterion | Score (1–5) | Weight | Weighted Score | Notes
ISO 13485 / equivalent certification | | 0.25 | |
Quality system documentation | | 0.15 | |
Product quality history (NC rate, delivery) | | 0.20 | |
Complaint response / CAPA effectiveness | | 0.15 | |
Regulatory compliance (FDA, EU MDR as applicable) | | 0.15 | |
Change notification process | | 0.10 | |
TOTAL WEIGHTED SCORE | | | |

Score key: 5 = Excellent; 4 = Good; 3 = Acceptable; 2 = Below expectation; 1 = Unacceptable

QUALIFICATION DECISION:
[ ] APPROVED — Add to Approved Supplier List (ASL)
[ ] CONDITIONALLY APPROVED — Conditions: [List conditions]
[ ] NOT APPROVED — Reason: [Reason]

Quality Agreement required: [ ] Yes   [ ] No (minor supplier only)
On-site audit required: [ ] Yes (scheduled: _____)   [ ] No
Next re-evaluation due: [Date / interval / event trigger]

Evaluated by: [Name] _________________ Date: _____________
QA Manager approval: [Name] _________________ Date: _____________
Added to ASL: [ ] Yes   [ ] No   ASL version updated: [Version]
```

---

## Template 8 — Design Change Request Form

```
DESIGN CHANGE REQUEST

DCR ID: DCR-[YYYY]-[NNN]
Date raised: [Date]
Raised by: [Name / Role]
Device / product: [Device name]
Current document revision affected: [Drawing No. / Spec No. / Software Version]

CHANGE DESCRIPTION:
Current state (what exists today): [Description]
Proposed change (what is changing): [Description]
Reason for change (clinical, quality, regulatory, manufacturing, cost, other): [Reason]

IMPACT ASSESSMENT:

Impact Area | Affected? | Assessment / Actions Required
Design inputs (7.3.3) | Y/N |
Design outputs (7.3.4) | Y/N |
Risk management / ISO 14971 | Y/N |
Verification required | Y/N | Protocols: ___________
Validation required | Y/N | Protocols: ___________
Biocompatibility (ISO 10993) | Y/N |
Software (IEC 62304) | Y/N |
Sterilisation (processes, validation) | Y/N |
Labelling / IFU / UDI | Y/N |
Packaging / shelf life | Y/N |
Supplier / component change | Y/N |
Manufacturing process | Y/N |
Device Master Record update | Y/N | Documents: ___________

REGULATORY ASSESSMENT:
EU MDR — Substantial modification? [ ] Yes   [ ] No   [ ] TBD
If Yes: [ ] NB notification required   [ ] New NB application required
FDA — New regulatory submission required? [ ] Yes — Type: ________   [ ] No
Other markets affected: [List]

CHANGE APPROVAL:
Function | Name | Signature | Date
Engineering | | |
Quality Assurance | | |
Regulatory Affairs | | |
Manufacturing | | |
Clinical (if applicable) | | |

CHANGE IMPLEMENTATION:
Implementation date: [Date]
Documents updated: [List document IDs and new revisions]
Training required: [ ] Yes — training record ref: _________   [ ] No
DHF updated: [ ] Yes   [ ] No (if No, justification: _________)
Change closed by (QA): [Name] _________________ Date: _____________
```

---

## Template 9 — Process Validation Protocol Outline

```
PROCESS VALIDATION PROTOCOL

Protocol ID: PVP-[Process Name]-[YYYY]-[NNN]
Process to be validated: [Process name — e.g., Injection Moulding, Welding, Cleaning, Packaging Sealing]
Device / product families: [Products that use this process]
Regulation / standard reference: ISO 13485:2016 Clause 7.5.6

VALIDATION APPROACH:
IQ (Installation Qualification): [ ] Required   [ ] Previously completed (IQ ref: _______)
OQ (Operational Qualification): [ ] Required   [ ] Previously completed (OQ ref: _______)
PQ (Performance Qualification): [ ] Required   [ ] Previously completed (PQ ref: _______)

---

IQ — INSTALLATION QUALIFICATION
Objective: Confirm equipment is installed correctly and meets specification.
Check | Specification | Observed | Pass/Fail
Equipment model and serial number | | |
Utilities connected (power, gas, water) | | |
Safety interlocks functional | | |
Calibration of instrumentation | | |
Equipment documentation on file (manual, drawings) | | |
IQ approved by: [Name] ______ Date: ______

---

OQ — OPERATIONAL QUALIFICATION
Objective: Confirm equipment operates within defined parameter ranges under worst-case conditions.
Parameter | Low limit | Nominal | High limit | Method | Pass/Fail
[Temperature] | | | | |
[Pressure] | | | | |
[Time] | | | | |
[Speed] | | | | |

Worst-case condition rationale: [Explain why low/high limits represent worst case]
OQ approved by: [Name] ______ Date: ______

---

PQ — PERFORMANCE QUALIFICATION
Objective: Confirm process consistently produces conforming product under production conditions.
Sample size: [Number] samples per run; [Number] runs
Sampling rationale: [Statistical justification — e.g., per ASTM or agreed sigma level]

Test parameter | Acceptance criterion | Run 1 results | Run 2 results | Run 3 results | Status
| | | | |

Lot-to-lot consistency: [ ] Demonstrated   [ ] Not demonstrated
PQ approved by: [Name] ______ Date: ______

VALIDATION CONCLUSION:
The process is: [ ] VALIDATED   [ ] NOT VALIDATED (see nonconformance: NCR-_______)
Revalidation triggers: [List events that require revalidation — equipment change, material change, site relocation, performance drift beyond limit, etc.]

Protocol authored by: [Name] _________________ Date: _____________
QA approved: [Name] _________________ Date: _____________
```

---

## Template 10 — Risk Management Plan Outline (ISO 14971:2019)

```
RISK MANAGEMENT PLAN

Document ID: RMP-[Device]-[YYYY]-[NNN]
Device: [Device name and model range]
ISO 14971 reference: ISO 14971:2019
Date: [Date]
Prepared by: [Risk Management Owner / Role]
Approved by: [QA Manager / VP Quality]

SECTION 1 — SCOPE AND CONTEXT
1.1 Intended use and intended users
1.2 Device description (brief)
1.3 Foreseeable misuse (reasonably foreseeable)
1.4 Regulatory markets in scope

SECTION 2 — RISK MANAGEMENT LIFE CYCLE ACTIVITIES
Phase | Risk Management Activity | Responsible | Timing
Concept | Preliminary hazard analysis | R&D + RA | Before design inputs
Design | Risk analysis, estimation, evaluation | R&D + QA | Concurrent with D&D
Verification | Update risk controls post-testing | QA + R&D | After verification
Validation | Residual risk evaluation; benefit-risk determination | RA + QA + Clinical | Before market release
Production/Post-market | Risk monitoring and review | QA + Regulatory | Ongoing; annual review minimum

SECTION 3 — RISK ACCEPTABILITY CRITERIA
[Organisation must define its own criteria — the standard does not specify absolute values]

3.1 Severity categories
Severity Level | Description | Clinical Example
1 — Negligible | No injury or only inconvenience | Mild discomfort; no treatment required
2 — Minor | Temporary injury; no permanent harm | Mild irritation; self-limiting reaction
3 — Serious | Injury requiring medical intervention | Hospital admission; reversible harm
4 — Critical | Permanent impairment | Permanent disability; organ damage
5 — Catastrophic | Death | Patient fatality

3.2 Probability categories
Probability Level | Description | Qualitative Estimate
5 — Frequent | Expected to occur often | >1 in 100
4 — Probable | Likely during device lifetime | 1 in 100 to 1 in 1,000
3 — Occasional | Could occur | 1 in 1,000 to 1 in 10,000
2 — Remote | Unlikely but possible | 1 in 10,000 to 1 in 100,000
1 — Improbable | Very unlikely | <1 in 100,000

3.3 Risk acceptability decision matrix
[Include 5x5 matrix with Acceptable / Low / Medium / High / Unacceptable zones]

3.4 Overall residual risk acceptability
The overall residual risk is acceptable if:
- All individual residual risks are in the Acceptable, Low, or Medium zone
- Risks in the Medium zone are justified by clinical benefit (ALARP principle applied)
- The clinical benefit to the intended patient population outweighs the residual risks
- Risk reduction has been pursued as far as reasonably practicable

SECTION 4 — RISK MANAGEMENT ACTIVITIES DOCUMENTATION
All risk management activities shall be documented in the Risk Management File, which includes:
- This Risk Management Plan
- Risk Analysis records
- Risk Evaluation records
- Risk Control records
- Residual Risk Evaluation
- Risk Management Report (ISO 14971 Clause 9)
- Post-market risk review records (ISO 14971 Clause 10)

SECTION 5 — REVIEW AND UPDATE TRIGGERS
This Risk Management Plan shall be reviewed and updated when:
- New hazards are identified
- Residual risks change due to design or process changes
- Post-market data reveals new risk information
- A CAPA or NC is linked to a device failure mode
- A design change occurs (per Clause 7.3.9)
- Regulatory requirements applicable to risk management are revised
- At each management review (summarised update minimum)

Approved by: [Top Management / VP Quality] _________________ Date: _____________
```

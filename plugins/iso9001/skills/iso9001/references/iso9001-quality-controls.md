# ISO 9001:2015 — Quality Process Controls Reference

This reference file provides a structured guide to the key quality process controls required under ISO 9001:2015, organised by process area. Load this file when providing implementation guidance for specific controls, generating audit checklists for process areas, or advising on QMS operational controls.

---

## Process Control Framework

ISO 9001:2015 uses the **process approach** — each process must have defined:
- **Inputs** (what triggers the process)
- **Outputs** (what the process produces)
- **Controls** (what governs how the process runs — procedures, work instructions, acceptance criteria)
- **Resources** (people, equipment, infrastructure, environment)
- **Performance indicators** (how we know the process is effective)
- **Risk treatment** (what prevents the process from failing)

---

## 1. Customer-Related Controls (Clause 8.2)

### Contract / Order Review
**Purpose:** Ensure the organisation can meet customer requirements before committing to supply.

| Control | Description | Evidence |
|---------|-------------|---------|
| Customer requirements capture | Documented process for capturing all requirements (technical, delivery, regulatory, implicit) | Customer requirement form, specification sheet |
| Contract review checklist | Checklist reviewed before order acceptance: capacity, competence, materials, regulatory compliance | Completed contract review records |
| Conflict resolution | Process for resolving differences between tender and contract requirements | Contract amendment records, customer correspondence |
| Order acknowledgement | Confirm to customer all requirements understood and will be met | Order acknowledgement, signed contract |
| Change management | Process for handling customer-initiated changes after order acceptance | Change request form, revised order records |

**Common gaps:** Verbal orders accepted without documented review; customer implied requirements (packaging, labelling) not captured; no process for managing requirement changes mid-order.

---

### Customer Communication
**Purpose:** Maintain effective communication with customers throughout the relationship.

| Control | Description | Evidence |
|---------|-------------|---------|
| Complaint handling | Defined process: receipt → acknowledgement → investigation → response → closure → CAPA | Complaint log, response records, CAPA records |
| Customer feedback | Systematic collection of customer satisfaction data beyond complaints | Surveys, NPS scores, customer scorecards |
| Product/service information | Up-to-date, accurate product/service information provided to customers | Product specifications, datasheets, catalogues |
| Customer property | Process for controlling items belonging to customers (tooling, moulds, data, IP) | Customer property register, loss/damage records |

---

## 2. Supplier and External Provider Controls (Clause 8.4)

### Supplier Qualification
**Purpose:** Ensure external providers meet quality requirements before being used.

| Control | Description | Evidence |
|---------|-------------|---------|
| Approved Supplier List (ASL) | Maintained register of evaluated and approved external providers, with scope of approval | Current ASL with status and approval date |
| Supplier evaluation criteria | Defined criteria before initial approval: quality system, delivery performance, capacity, HSE, financial stability | Evaluation criteria matrix, questionnaire |
| New supplier qualification | Formal process: self-assessment questionnaire → sample evaluation → trial order → approval | Supplier qualification file |
| Supplier audit | On-site or remote audit of high-risk or critical suppliers | Supplier audit report, audit schedule |
| Approved supplier register maintenance | Regular re-evaluation at defined frequency; suspension/removal process | Re-evaluation records, approval status history |

---

### Ongoing Supplier Performance Management
| Control | Description | Evidence |
|---------|-------------|---------|
| Supplier scorecard | Periodic performance rating: quality (incoming inspection pass rate), delivery (on-time %), responsiveness | Supplier scorecard / performance report |
| Supplier corrective action request (SCAR) | Formal process to issue a SCAR when supplier delivers nonconforming goods/services | SCAR log, supplier responses, closure records |
| Incoming inspection | Inspection/verification of externally provided goods before use in own processes | Incoming inspection records, test reports |
| Purchase order quality requirements | PO specifies: specification, revision level, acceptance criteria, certificate of conformance requirement, right of access | PO template with quality clauses |

---

## 3. Production and Service Provision Controls (Clause 8.5)

### Production Planning
| Control | Description | Evidence |
|---------|-------------|---------|
| Production/work order system | Job travellers or work orders linking customer order to production steps, materials, and resources | Work orders, job travellers, production schedule |
| Bill of materials / specification | Documented materials and components required for each product | BOM, product specification, routing |
| Work instructions | Step-by-step instructions for operators at the point of use | Work instructions, SOPs, visual aids |
| First Article Inspection (FAI) | Verification that a new or changed product/process meets requirements before production run | FAI report, first article sign-off record |

---

### In-Process Controls
| Control | Description | Evidence |
|---------|-------------|---------|
| In-process inspection and testing | Defined inspection points during production; criteria and accept/reject decisions documented | Inspection and test plan (ITP), in-process inspection records |
| Statistical Process Control (SPC) | Control charts monitoring process parameters for trends before defects occur | SPC charts, Cpk/Ppk data |
| Error-proofing (Poka-yoke) | Devices or procedures that prevent or detect errors before they become defects | Error-proofing log, device verification records |
| Non-conforming product segregation | Clearly identified hold/reject area; quarantine procedure to prevent inadvertent use | Quarantine tags, segregated area signage, NC records |
| Process parameters monitoring | Critical process parameters (temperature, pressure, speed, dimensions) monitored and recorded | Process parameter logs, SPC charts |

---

### Special Processes
Special processes are those where the resulting output cannot be fully verified by subsequent inspection (e.g. welding, heat treatment, plating, non-destructive testing, sterilisation).

| Control | Description | Evidence |
|---------|-------------|---------|
| Special process validation | Process validated to demonstrate ability to achieve planned results before use in production | Validation plan, validation records, approval to proceed |
| Approved process operators | Only qualified/certified personnel perform special processes | Operator qualification records, certification log |
| Special process parameter records | Critical parameters (time, temperature, current, speed) recorded for each batch/job | Process run records, batch sheets |
| Periodic revalidation | Validate again after: equipment change, process change, extended downtime, personnel change | Revalidation records, change-triggered revalidation log |

---

### Final Release Controls (Clause 8.6)
| Control | Description | Evidence |
|---------|-------------|---------|
| Final inspection and test | Criteria defined for final acceptance; must be completed before release | Final inspection records, test reports |
| Certificate of Conformance (CoC) | Document confirming product meets specified requirements, signed by authorised person | CoC, signed release record |
| Release authority | Only designated persons may authorise release to customer | Approved signatories list, release authorisation on CoC/delivery note |
| Release blocked until complete | No product released if planned inspection/verification activities incomplete (unless authorised concession) | Locked hold status in ERP/MES; concession record if applicable |

---

### Traceability Controls (Clause 8.5.2)
| Control | Description | Evidence |
|---------|-------------|---------|
| Product/batch identification | Unique identification applied from receipt of materials through production to delivery | Batch/lot numbers, serial numbers, traveller ID |
| Traceability records | Ability to reconstruct: which materials used, which process run, which operators, which inspection results, which customers received | Batch records, production history database, delivery records |
| Recall capability | Demonstrate ability to identify and contact affected customers in the event of a product issue | Mock recall exercise records |

---

## 4. Inspection and Test Controls (Clause 7.1.5, 8.6, 8.7)

### Calibration and Measurement Equipment
**Purpose:** Ensure monitoring and measuring equipment provides valid results.

| Control | Description | Evidence |
|---------|-------------|---------|
| Equipment register | All measuring equipment used for product/process verification listed with: ID, type, location, calibration interval, next due date, traceability | Calibration register / equipment master list |
| Calibration records | For each calibration: date, method, standard used, result (pass/adjusted/fail), next due date, performed by | Calibration certificates, internal calibration records |
| Traceable calibration standards | Calibration standards traceable to national/international measurement standards | UKAS/NVLAP calibration certificate for reference standards |
| Out-of-calibration response | Process: remove from service, assess impact on previous measurements, recall affected product if necessary, investigate root cause | Out-of-calibration NC record, impact assessment, recall records |
| Equipment status labelling | Equipment clearly labelled: calibrated/due for calibration/out of service | Calibration status labels on equipment |

**Common gaps:** Equipment missing from register; calibration certificates lack traceability statement; no out-of-calibration impact assessment process; gauge R&R studies not conducted

---

## 5. Nonconformity and Corrective Action Controls (Clause 8.7, 10.2)

### Nonconforming Output Control
| Control | Description | Evidence |
|---------|-------------|---------|
| NC identification | All nonconforming product/service clearly identified immediately | NC tags, rejection stamps, system holds |
| NC segregation | Physical segregation of nonconforming product to prevent unintended use | Quarantine area, MRB (Material Review Board) area |
| NC disposition | Formal process: scrap / rework / use-as-is (concession) / return to supplier | Disposition record, MRB decision |
| Concession / waiver | Customer authorisation obtained for delivery of product that does not meet specification | Concession/deviation approval from customer |
| Rework control | Rework process defined; re-inspection required after rework | Rework instructions, post-rework inspection records |
| NC trend analysis | Periodic analysis of NC data to identify systemic issues requiring corrective action | NC Pareto analysis, NC summary report |

---

### Corrective Action (CAPA) Process
| Step | Requirement | Evidence |
|------|------------|---------|
| 1. Description | Clear statement of the nonconformity: what, where, when, how discovered | NC report |
| 2. Containment | Immediate action to limit impact: quarantine, recall, customer notification | Containment record |
| 3. Root cause analysis | Systematic investigation: 5-Why, Fishbone/Ishikawa, Fault Tree Analysis | RCA record |
| 4. Corrective action plan | Actions to eliminate root cause: systemic, not just symptom fix | CA plan with owner and due date |
| 5. Implementation | Evidence that planned actions were carried out | Evidence of completion |
| 6. Effectiveness verification | Check that the corrective action eliminated the root cause and the NC has not recurred | Verification record (re-audit, process data, no recurrence after defined period) |
| 7. Closure | Formal closure by authorised person after effectiveness confirmed | Closed CAPA record |

---

## 6. Document and Records Controls (Clause 7.5)

### Document Control
| Control | Description | Evidence |
|---------|-------------|---------|
| Master document list | All controlled documents: ID, title, version, date, owner, review date | Master document register |
| Version control | Clear version numbering; change history log; obsolete versions removed from use | Version numbering convention, change log |
| Approval before issue | All controlled documents approved by authorised person before issue | Approval signatures / electronic workflow |
| Online/offline control | Ensure only current versions accessible at point of use | Document management system access controls; printed copy control stamps |
| External documents | Customer drawings, standards, regulatory documents identified and controlled | External document register, revision check process |
| Retention periods | Defined retention periods for each record type; secure storage and disposal | Record retention schedule |

---

## 7. Internal Audit Controls (Clause 9.2)

| Control | Description | Evidence |
|---------|-------------|---------|
| Annual audit programme | All processes and clauses covered over the audit cycle, with risk-adjusted frequency | Audit programme / schedule for the year |
| Audit plan | For each audit: scope, criteria, schedule, auditee, auditor (independent) | Individual audit plan |
| Audit checklist | Clause/process-by-process questions and evidence required | Completed audit checklist |
| Audit report | Findings: conformances, nonconformities (major/minor), observations | Formal audit report |
| NC follow-up | Corrective actions raised for all audit NCs; effectiveness verified before closure | CAPA linked to audit NC, closure evidence |
| Auditor competence | Internal auditors trained in auditing technique (ISO 19011 recommended) | Auditor training records, qualification evidence |

---

## 8. Management Review Controls (Clause 9.3)

| Input Required | Evidence |
|---------------|---------|
| Previous MR action status | Action log from prior MR showing open/closed status |
| Internal/external context changes | Updated context analysis, interested party register review |
| Customer satisfaction data | Survey results, complaint trends, NPS |
| Quality objective performance | KPI dashboard, objectives achievement report |
| Process performance and NC data | NC trend report, process KPI summary |
| Audit results | Internal audit summary, external audit findings |
| External provider performance | Supplier scorecard summary |
| Adequacy of resources | Resource needs assessment |
| Risk and opportunity action effectiveness | Risk register review |

| Output Required | Evidence |
|----------------|---------|
| Improvement opportunities identified | Action items with owner and due date in MR minutes |
| QMS change needs | Change request or action for QMS revision |
| Resource decisions | Budget approvals, headcount decisions documented in MR minutes |

---

## 9. Continual Improvement Controls (Clause 10.3)

| Control | Description | Evidence |
|---------|-------------|---------|
| Improvement register | Log of improvement ideas, initiatives, and projects: source, description, status, result | Improvement log/tracker |
| Kaizen/CI events | Structured improvement events (lean kaizen, six sigma, PDCA) | Event reports, before/after metrics |
| Lessons learned | Capture and share lessons from nonconformities, near-misses, audits, and project reviews | Lessons learned database, knowledge-sharing records |
| Benchmarking | Compare performance against industry benchmarks or internal targets | Benchmarking report |
| Objective-to-action link | Improvement actions tied to specific quality objectives or performance gaps | Objective review → improvement action linkage in MR minutes |

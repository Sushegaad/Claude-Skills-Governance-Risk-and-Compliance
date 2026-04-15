# ISO 13485:2016 — Clause Requirements Reference

## Overview

ISO 13485:2016 contains eight numbered clauses (Clauses 1–8). Clauses 1–3 are introductory (scope, normative references, terms). The normative requirements are in **Clauses 4–8**.

The standard uses the phrase "documented procedure" to mean a written procedure that is established, documented, implemented, and maintained. The phrase "records shall be maintained" indicates evidence must be kept. Below is a clause-by-clause summary table followed by detailed sub-clause notes.

---

## Clause 4 — Quality Management System

| Sub-clause | Title | Key Requirement | Documented Procedure? | Records Required? |
|-----------|-------|----------------|----------------------|------------------|
| 4.1 | General requirements | Establish, document, implement and maintain QMS; control outsourced processes | No (but processes must be documented) | No |
| 4.2.1 | General documentation requirements | QMS documentation set: quality policy, objectives, manual, procedures, records, regulatory documents | No | No |
| 4.2.2 | Quality manual | Maintain quality manual covering scope, exclusions, interactions | No | Yes (quality manual is a record-like document) |
| 4.2.3 | Medical device file | Maintain per device type/family; demonstrate conformity; includes labelling, design files, specs | No | Yes — file per device type/family |
| 4.2.4 | Control of documents | Document approval, review, change control, obsolete doc control | Yes — mandatory | No |
| 4.2.5 | Control of records | Legible, retrievable, protected records; retention per device lifetime + 2 years minimum | Yes — mandatory | Yes — record retention log |

### 4.1 — Outsourced Processes Note

When an organisation outsources any process that affects product conformity (e.g., sterilisation, testing, manufacturing, distribution), it must:
- Identify which processes are outsourced
- Document controls applied (e.g., supplier quality agreement, supplier audit)
- Maintain records of outsourced process control activities
- Include outsourced processes in internal audit scope where applicable

### 4.2.3 — Medical Device File Content (Non-exhaustive)

The medical device file (MDF) is the master reference file for each device type or device family. It may be a physical file, an electronic system, or a structured set of referenced documents. Minimum expected content:

| Category | Document Examples |
|----------|------------------|
| Device description | Intended use, indications, contraindications, patient population, body site |
| Labelling | Labels, instructions for use (IFU), packaging artwork — all language versions |
| Design outputs | Drawings, specifications, BOM, inspection test plans (see Clause 7.3.4) |
| Manufacturing | Process specifications, work instructions, validation records |
| Risk management | Risk management plan, risk management file (ISO 14971) |
| Clinical evidence | Clinical evaluation report, PMCF protocol/reports (EU MDR) / clinical data summary |
| Regulatory | Classification justification, regulatory submissions summary, certificates |
| Traceability | UDI assignment records, traceability scheme |
| Post-market | PMS plan, PSUR (if required), complaint summary |

### 4.2.4 — Document Control Minimum Workflow

```
Draft → Review (technical / regulatory) → Approval (QA / authorised) → Issue (version control) →
Distribution (controlled copies) → Periodic review (scheduled) → Change → Re-approval → Archive/obsolete
```

---

## Clause 5 — Management Responsibility

| Sub-clause | Title | Key Requirement | D/P? | Records? |
|-----------|-------|----------------|------|---------|
| 5.1 | Management commitment | Top management communicates requirements; establishes policy/objectives; provides resources; conducts reviews | No | Via management review |
| 5.2 | Customer focus | Customer requirements determined and met subject to regulatory requirements | No | No |
| 5.3 | Quality policy | Documented, communicated, reviewed for suitability | No | Policy is a controlled document |
| 5.4.1 | Quality objectives | Measurable objectives at relevant functions and levels | No | Yes — objectives record |
| 5.4.2 | QMS planning | Planning maintains integrity during changes | No | No |
| 5.5.1 | Responsibility and authority | Defined and communicated; independence of QA function | No | Org chart, role descriptions |
| 5.5.2 | Management representative | Designated individual with defined authority | No | Appointment letter or job description |
| 5.5.3 | Internal communication | Appropriate processes established | No | No |
| 5.6.1 | Management review — general | Planned interval reviews; maintain QMS effectiveness | No | Yes — management review minutes |
| 5.6.2 | Review input | Listed inputs: audits, feedback, NC, CAPA, changes, regulatory | No | Captured in review minutes / input pack |
| 5.6.3 | Review output | Decisions on QMS effectiveness, product improvement, resources | No | Captured in review minutes |

### 5.6.2 — Management Review Input Checklist

All of the following shall be addressed at each management review:
- [ ] Results of internal audits
- [ ] Results of external/regulatory authority audits
- [ ] Customer feedback (including complaint trend data)
- [ ] Process performance (KPIs) and product conformity data
- [ ] Corrective action and preventive action status (open and closed)
- [ ] Follow-up actions from previous management review
- [ ] Changes that could affect the QMS (regulatory, product, process, organisational)
- [ ] Recommendations for improvement
- [ ] New or revised regulatory requirements
- [ ] Applicable new or revised standards

### 5.6.3 — Management Review Output Minimum

The output record must capture at minimum:
1. Decisions and actions on QMS effectiveness improvements
2. Decisions and actions on product improvements
3. Resource allocations/approvals
4. Any regulatory actions required

---

## Clause 6 — Resource Management

| Sub-clause | Title | Key Requirement | D/P? | Records? |
|-----------|-------|----------------|------|---------|
| 6.1 | Provision of resources | Determine and provide resources for QMS maintenance and regulatory compliance | No | No |
| 6.2 | Human resources | Competence based on education, training, skills, experience; training effectiveness evaluated | No | Yes — training records |
| 6.3 | Infrastructure | Define, provide, maintain; maintenance schedule | No | Yes — maintenance records |
| 6.4.1 | Work environment | Document and monitor environmental conditions affecting product quality | No | Yes — environmental monitoring records (if applicable) |
| 6.4.2 | Contamination control | Documented arrangements for contamination control; specific requirements for sterile devices | No | Yes — cleaning/contamination records (if applicable) |

### 6.2 — Competence and Training Requirements

Minimum training programme elements:
1. QMS awareness training — all staff (quality policy, objectives, role impact)
2. Job-specific technical training — documented training matrix per role
3. Regulatory awareness — applicable regulations for markets in scope
4. Good Documentation Practice (GDP) — all records-generating personnel
5. Deviation/NC reporting — all production and QA staff
6. Complaint identification and escalation — customer-facing and field personnel

Training effectiveness evaluation methods: Written assessment, practical observation, error rate monitoring (for technical tasks), supervisor sign-off.

---

## Clause 7 — Product Realization

| Sub-clause | Title | D/P? | Records? |
|-----------|-------|------|---------|
| 7.1 | Planning of product realization | No (but outputs documented) | Yes — quality plan, risk management records |
| 7.2.1 | Determination of product requirements | No | No |
| 7.2.2 | Review of product requirements | No | Yes — review records |
| 7.2.3 | Customer communication | No | No |
| 7.3.1 | Design and development — general | Yes — mandatory (if D&D in scope) | Yes |
| 7.3.2 | D&D planning | No (covered by 7.3.1 procedure) | Yes — D&D plan |
| 7.3.3 | D&D inputs | No | Yes — D&D input records |
| 7.3.4 | D&D outputs | No | Yes — D&D output records |
| 7.3.5 | D&D review | No | Yes — review records with participants |
| 7.3.6 | D&D verification | No | Yes — verification records |
| 7.3.7 | D&D validation | No | Yes — validation records |
| 7.3.8 | D&D transfer | No | Yes — transfer records |
| 7.3.9 | Control of D&D changes | Yes — mandatory | Yes — change records |
| 7.3.10 | Design and development files (DHF) | No (procedure covers creation) | Yes — DHF per device type |
| 7.4.1 | Purchasing process | Yes — mandatory | Yes — supplier evaluation, ASL |
| 7.4.2 | Purchasing information | No | Yes — purchase orders, specifications |
| 7.4.3 | Verification of purchased product | No | Yes — incoming inspection records |
| 7.5.1 | Control of production | Yes — mandatory (work instructions) | Yes — batch/lot records |
| 7.5.2 | Cleanliness of product | Yes (if applicable) | Yes |
| 7.5.3 | Installation activities | Yes (if applicable) | Yes |
| 7.5.4 | Service activities | Yes (if applicable) | Yes |
| 7.5.5 | Sterile device requirements | Yes — mandatory (if sterile) | Yes — sterilisation records |
| 7.5.6 | Process validation | Yes — mandatory | Yes — validation protocols/reports |
| 7.5.7 | Sterilisation / sterile barrier validation | Yes — mandatory (if sterile) | Yes |
| 7.5.8 | Identification | Yes — mandatory | No |
| 7.5.9 | Traceability | Yes — mandatory | Yes — traceability records |
| 7.5.10 | Customer property | No | Yes — customer property records |
| 7.5.11 | Preservation of product | No | No (unless environmental monitoring relevant) |
| 7.6 | Monitoring and measuring equipment | No | Yes — calibration records |

### 7.3 — Design and Development Exclusion

A manufacturer may exclude Clause 7.3 only where:
- The organisation has no design authority and produces exclusively to external design documents provided by the customer
- The customer retains full design responsibility
- This exclusion is explicitly documented and justified in the quality manual
- The applicable regulatory authority for the target market accepts this exclusion

> Note: The FDA QMSR (2024) and EU MDR Annex IX require design controls from the manufacturer. Contract manufacturers operating under full customer design authority may be excluded, but this must be confirmed on a case-by-case basis with the relevant NB or FDA reviewer.

### 7.4.1 — Supplier Qualification Minimum Requirements

For critical suppliers (those supplying materials, components, or services that directly affect device safety or performance):

**Initial qualification:**
1. Supplier questionnaire / self-assessment
2. Quality agreement (including regulatory requirements, change notification, audit rights)
3. On-site audit (for highest-criticality suppliers)
4. Sample inspection and approval
5. Addition to Approved Supplier List (ASL)

**Ongoing evaluation:**
1. Periodic re-evaluation (frequency based on criticality — typically annual for critical)
2. Supplier performance scorecard (delivery performance, NC rate, response to issues)
3. Change notification from supplier (material change, site change, process change)
4. Re-qualification if change exceeds defined threshold

### 7.6 — Calibration Requirements

Monitoring and measuring equipment used to demonstrate product conformity must be controlled. Minimum programme elements:

| Element | Requirement |
|---------|------------|
| Calibration schedule | Defined intervals per equipment type based on stability, criticality, usage |
| Calibration standards | Traceability to national/international measurement standards (NIST, BIPM, etc.) |
| Calibration labels | Equipment tagged with calibration status (due date, reference to certificate) |
| Out-of-calibration procedure | What to do when equipment found out of calibration — assess impact on prior measurements |
| Adjustments | Adjustments protected from invalidation (tamper-evident, access-controlled) |
| Records | Calibration certificate with as-found and as-left values |
| Computer-assisted measurement | Software validation required for measurement software |

---

## Clause 8 — Measurement, Analysis, and Improvement

| Sub-clause | Title | D/P? | Records? |
|-----------|-------|------|---------|
| 8.1 | General | No | No |
| 8.2.1 | Feedback | Yes — mandatory | Yes — feedback records |
| 8.2.2 | Complaint handling | Yes — mandatory | Yes — complaint records |
| 8.2.3 | Reporting to regulatory authorities | Yes — mandatory | Yes — adverse event reports |
| 8.2.4 | Internal audit | Yes — mandatory | Yes — audit programme, reports |
| 8.2.5 | Monitoring and measurement of processes | No | Yes — process performance data |
| 8.2.6 | Monitoring and measurement of product | No | Yes — inspection records, release authorisation |
| 8.3.1 | Control of NC product — general | Yes — mandatory | Yes — NCR records |
| 8.3.2 | NC product before delivery — actions | No | Yes — disposition records |
| 8.3.3 | NC product after delivery — actions | No | Yes — FSCA/recall records if applicable |
| 8.3.4 | Rework | Yes — mandatory (if rework occurs) | Yes — rework records |
| 8.4 | Analysis of data | No | No (outputs feed into management review) |
| 8.5.1 | General improvement | No | No |
| 8.5.2 | Corrective action | Yes — mandatory | Yes — CAPA records |
| 8.5.3 | Preventive action | Yes — mandatory | Yes — PA records |

### 8.2.2 — Complaint Handling — Minimum Procedure Elements

1. **Receipt:** All complaints received through any channel (phone, email, field service, distributor) captured in complaint log
2. **Logging:** Unique complaint reference; device identification; complainant data; description of complaint; date received; date of alleged incident
3. **Triage:** Decision: is this a reportable adverse event? Is there an immediate safety concern requiring containment?
4. **Investigation:** Root cause analysis; device/product analysis (if sample returned); regulatory determination
5. **Response:** Corrective action; communication to complainant (where appropriate and required)
6. **Regulatory reporting:** Determination whether MDR (FDA) / vigilance report (EU MDR) required — within statutory timeframe
7. **Closure:** Record of investigation conclusions, corrective action taken, closure authorisation

**Key complaint record fields:**
- Complaint ID and date received
- Reporter name and contact (or anonymous flag)
- Device type, model, lot/serial number, UDI (if applicable)
- Date of event (if different from complaint date)
- Description of complaint / alleged failure
- Patient outcome (if applicable: adverse event, death, serious injury)
- Investigation results
- Root cause (final)
- Regulatory report filed: Y/N — report number and date
- CAPA reference (if opened)
- Disposition / corrective action
- Closure date and authorising person

### 8.2.3 — Regulatory Authority Reporting Timeframes

| Authority | Regulation | Event Type | Timeframe |
|-----------|-----------|------------|-----------|
| European Commission / NB | EU MDR Art. 87 | Serious incident | 15 days |
| European Commission / NB | EU MDR Art. 87 | Death or unanticipated serious deterioration | 2 days (immediate/urgent reporting) |
| European Commission / NB | EU MDR Art. 87 | Field safety corrective action | Before action or without undue delay |
| FDA | 21 CFR Part 803 | Death or serious injury — mandatory reporter | 30 days |
| FDA | 21 CFR Part 803 | Death or serious injury requiring remedial action | 5 days |
| Health Canada | SOR/98-284 | Serious adverse event | 10 days for death/serious deterioration |
| TGA (Australia) | TGA Adverse Event Reporting | Serious incident | 30 days; 48 hours if death |
| MHLW (Japan) | PMD Act | Serious adverse event | 15 days or as specified |

> Note: Timeframes shown are general. Always confirm against current regulatory guidance for each market as requirements may be updated. These are calendar days unless the regulation specifies business days.

### 8.3 — Nonconforming Product Disposition Options

| Disposition | Definition | Requirements |
|------------|-----------|-------------|
| Accept as-is (concession) | Use/release despite nonconformity | Documented justification; authorised by customer/regulator if required; risk assessment |
| Rework | Processing to conform to requirements | Documented rework procedure; re-inspection after rework; records |
| Regrade | Classify for different application | Documents update; label change; may trigger design change |
| Scrap/reject | Remove from supply chain | Prevent accidental use; records of disposal |
| Return to supplier | Return for replacement | Records of return and supplier response |

---

## Mandatory Documented Procedures — Summary

The following documented procedures are explicitly required by ISO 13485:2016:

| Clause | Procedure |
|--------|----------|
| 4.2.4 | Control of Documents |
| 4.2.5 | Control of Records |
| 7.3.1 | Design and Development (if design in scope) |
| 7.3.9 | Control of Design and Development Changes (if design in scope) |
| 7.4.1 | Purchasing (Supplier Management) |
| 7.5.1 | Production and Service Provision Controls (work instructions as applicable) |
| 7.5.6 | Validation of Processes |
| 7.5.8 | Identification |
| 7.5.9 | Traceability |
| 8.2.1 | Feedback |
| 8.2.2 | Complaint Handling |
| 8.2.3 | Reporting to Regulatory Authorities |
| 8.2.4 | Internal Audit |
| 8.3.1 | Control of Nonconforming Product |
| 8.3.4 | Rework (if applicable) |
| 8.5.2 | Corrective Action |
| 8.5.3 | Preventive Action |

Additionally required if producing sterile devices:
| 7.5.5 | Sterilisation Production Controls |
| 7.5.7 | Sterilisation Process Validation |

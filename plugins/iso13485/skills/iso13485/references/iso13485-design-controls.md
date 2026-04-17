# ISO 13485:2016 — Design Controls Reference (Clause 7.3)

## Overview

Clause 7.3 of ISO 13485:2016 covers **design and development** of medical devices. It is one of the most scrutinised clauses during audits because inadequate design controls are a leading cause of device recalls and field safety corrective actions (FSCAs).

The design controls in ISO 13485 align with and are referenced by:
- **EU MDR 2017/745 Annex II** — Technical Documentation
- **FDA 21 CFR 820.30** — Design Controls
- **IMDRF Technical Documents** on design and development

Unlike ISO 9001:2015, ISO 13485 adds the following design-specific requirements:
- Design and development transfer (7.3.8)
- Design and development file / Design History File (7.3.10)
- Explicit risk management integration throughout the design process (7.1, linked to ISO 14971)

---

## When Clause 7.3 Applies

Clause 7.3 is applicable to all **manufacturers with design authority** — organisations that define or own the design of the medical device. It may be excluded only when:
- The organisation manufactures strictly to an external customer's complete design specification
- The exclusion is documented and justified in the quality manual
- The applicable regulatory authority accepts the exclusion (FDA does NOT permit exclusion of design controls for finished device manufacturers)

> For EU MDR: Notified bodies require design documentation as part of Annex II Technical Documentation regardless of whether the manufacturer claims a 7.3 exclusion. In practice, Class IIa and above manufacturers cannot exclude Clause 7.3.

---

## Design and Development Process — Phase Gate Structure

The following phase gate model is widely used in medical device development. ISO 13485 does not mandate specific phases, but requires that phase reviews, verifications, and validations are planned and documented.

### Phase 0 — Concept and Feasibility

**Objective:** Establish that the device concept is technically feasible and commercially viable before committing design resources.

**Activities:**
- Voice of customer (clinical need, market research)
- Preliminary intended use statement and indication for use
- Preliminary hazard analysis (ISO 14971 — initial hazard identification)
- Regulatory pathway analysis (EU MDR classification / FDA 510(k) vs. PMA / De Novo)
- Preliminary standards identification
- Feasibility prototyping (if applicable)

**Key outputs:**
- Feasibility report
- Preliminary intended use document
- Regulatory strategy document
- Initial risk management plan (ISO 14971, Clause 4)

**Gate 0 criteria:**
- [ ] Clinical need established
- [ ] Regulatory pathway identified
- [ ] Technical feasibility assessed
- [ ] Initial budget and timeline approved

---

### Phase 1 — Design Inputs (ISO 13485 Clause 7.3.2 and 7.3.3)

**Objective:** Translate user needs and regulatory requirements into documented, measurable design requirements.

**Activities:**
- User needs analysis (clinical user, patient, lay user)
- Regulatory requirements identification (GSPR for EU MDR / PDPs for FDA)
- Applicable standards determination
- Design input review and approval
- Risk management: hazard identification and risk estimation (ISO 14971 Clauses 4–5)
- Usability requirements (IEC 62366-1 — use specification)

**Key outputs (Design Inputs — Clause 7.3.3):**

| Input Category | Examples |
|---------------|---------|
| Performance requirements | Force outputs, accuracy specifications, dimensional tolerances, tensile strength |
| Safety requirements | Electrical safety (IEC 60601), biocompatibility (ISO 10993), EMC (IEC 60601-1-2) |
| Usability requirements | Task analysis, user interface requirements, error tolerance |
| Software requirements | Functional requirements, safety class (IEC 62304 Class A/B/C), cybersecurity requirements |
| Regulatory requirements | GSPR list (EU MDR Annex I), essential requirements |
| Sterility requirements | Sterility Assurance Level (SAL), sterile barrier validation (ISO 11607) |
| Labelling requirements | Symbols (ISO 15223-1), language requirements, UDI, IFU requirements |
| Packaging requirements | Shelf life, transport conditions, drop testing |
| Environmental requirements | Storage temperature, humidity range, operating altitude |

**Inputs document must be:**
- Reviewed and approved by engineering, regulatory, quality, and clinical functions
- Incomplete, ambiguous, or conflicting requirements resolved before design output phase
- Version-controlled and linked to risk management file

**Gate 1 criteria:**
- [ ] All design inputs documented and approved
- [ ] Risk management plan approved
- [ ] Applicable standards confirmed
- [ ] Regulatory strategy confirmed (classification, route, timeline)

---

### Phase 2 — Design Outputs (ISO 13485 Clause 7.3.4)

**Objective:** Create engineering specifications and design artefacts that directly address each design input.

**Design output categories:**

| Output Type | Examples |
|------------|---------|
| Engineering drawings | Component drawings, assembly drawings, tolerance stack-ups |
| Specifications | Material specifications, surface finish, dimensional requirements |
| Bill of materials (BOM) | Full component list with manufacturer part numbers, revision levels |
| Software architecture | System architecture, software design documents (IEC 62304) |
| Labelling | Draft labels, IFU, packaging artwork |
| Manufacturing process specs | Assembly procedures, work instructions, cleaning procedures |
| Acceptance criteria | Pass/fail criteria for each verification test |

**Requirements for design outputs (7.3.4):**
1. Each output must be traceable to a specific design input
2. Outputs must provide sufficient information for purchasing, production, and service
3. Outputs must contain or reference product acceptance criteria
4. Outputs must specify characteristics essential for safe and proper use

**Traceability matrix:** A design traceability matrix links:
- User need → Design input → Design output → Verification method → Validation → Risk control

**Gate 2 criteria:**
- [ ] All design inputs have corresponding design outputs
- [ ] Traceability matrix completed
- [ ] Initial design FMEA completed (or equivalent risk assessment)
- [ ] Draft labelling reviewed against regulatory requirements
- [ ] BOM baselined

---

### Phase 3 — Design Verification (ISO 13485 Clause 7.3.6)

**Objective:** Confirm through objective evidence that design outputs meet design inputs.

**Verification activities:**

| Verification Type | Standard / Method | Applicable To |
|------------------|------------------|--------------|
| Dimensional inspection | Engineering drawings | All mechanical components |
| Material testing | ISO 10993 biocompatibility, material characterisation | Contact parts, implants |
| Electrical safety testing | IEC 60601-1, IEC 60601-1-2 (EMC) | Active electrical devices |
| Software unit/integration testing | IEC 62304 | Software-containing devices |
| Mechanical strength testing | ISO, ASTM standards | Structural components |
| Sterilisation compatibility | ISO 11607 | Sterile packaged devices |
| Accelerated aging / shelf life | ASTM F1980 | All sterile / packaged devices |
| Environmental stress testing | Temperature cycling, humidity, vibration | All devices |
| Biocompatibility evaluation | ISO 10993-1 evaluation strategy | Devices in contact with body |

**Verification protocol minimum content:**
1. Protocol ID, revision, and approval signatures
2. Purpose and scope
3. Reference to design input(s) being verified
4. Acceptance criteria (pass/fail — directly traceable to design input)
5. Test method (standard or internal method)
6. Sample size and selection rationale (statistical justification)
7. Equipment identification and calibration status
8. Test procedure (step-by-step)
9. Results recording format

**Verification report minimum content:**
1. Reference to protocol
2. Test dates and locations
3. Sample identification (lot/serial numbers, revision levels)
4. Deviations from protocol (with justification if applicable)
5. Results — table of results vs. acceptance criteria
6. Pass/fail conclusion per requirement
7. Signature of test executor and reviewer

**Gate 3 criteria:**
- [ ] All design outputs verified against design inputs
- [ ] No open verification failures without documented disposition
- [ ] Updated risk assessment post-verification
- [ ] Design review conducted with multi-functional team
- [ ] Design review minutes and action items recorded

---

### Phase 4 — Design Validation (ISO 13485 Clause 7.3.7)

**Objective:** Confirm through objective evidence that the finished device consistently meets the requirements for the specified intended use.

> Distinction: Verification asks "did we build the design right?" Validation asks "did we build the right design for the intended use?"

**Validation activities:**

| Validation Type | Description | Regulatory Linkage |
|----------------|-------------|-------------------|
| Clinical evaluation | Evaluation of clinical data (literature, clinical investigation, PMCF) | EU MDR Art. 61 / Annex XIV; FDA IDE / 510(k) / PMA clinical evidence |
| Usability summative evaluation | Final user testing with representative users in simulated use | IEC 62366-1; FDA Human Factors guidance |
| Process validation | Confirmation that critical manufacturing processes produce conforming product | Clause 7.5.6 |
| Sterilisation validation | Confirmation that sterilisation process achieves required SAL | ISO 11135 / ISO 11137 / ISO 25424 |
| Software validation | System-level software validation testing | IEC 62304 Clause 5.6 + 5.7 |
| Packaging validation | Confirmation that sterile barrier system maintains sterility during shipping/storage | ISO 11607-2 |
| Simulated use / animal studies | Where applicable, device performance testing under simulated or actual conditions | Protocol-specific; IND/IDE if human use |

**Clinical evaluation (EU MDR Art. 61 and Annex XIV):**
The clinical evaluation is a continuous process with three main elements:
1. **Literature review** — systematic search of clinical data for the device and equivalent devices
2. **Clinical data analysis** — assessment of clinical safety and performance from available data
3. **Clinical Evaluation Report (CER)** — documents the evaluation outcome and clinical evidence summary

For devices where clinical data from literature is insufficient, a **clinical investigation** (per ISO 14155:2020) is required.

**Post-market clinical follow-up (PMCF):**
- Proactive method for collecting post-market clinical data
- Plan (PMCF Plan) and evaluation (PMCF Evaluation Report) at defined intervals
- Feeds into PSUR and clinical evaluation update

**Gate 4 criteria:**
- [ ] Device validated for intended use under representative conditions
- [ ] Clinical evaluation / clinical data assessed and documented
- [ ] Usability summative evaluation completed (if required)
- [ ] All validation failures resolved or accepted with risk assessment
- [ ] Final risk management report completed (ISO 14971 Clause 9 — benefit-risk determination)
- [ ] Design review conducted; all design review actions closed

---

### Phase 5 — Design Transfer (ISO 13485 Clause 7.3.8)

**Objective:** Ensure verified and validated design outputs are transferred to routine manufacturing without loss of quality or performance characteristics.

**Design transfer activities:**
1. Transfer plan — identifies what needs to be transferred, timeline, and acceptance criteria
2. Production process development and validation
3. Manufacturing documentation finalisation (work instructions, assembly procedures, inspection plans)
4. Pilot production run — first article inspection; confirm production process produces conforming product
5. Transfer acceptance review — multi-functional sign-off that transfer is complete
6. Device Master Record (DMR) / Technical File baseline — all design documents placed under configuration control

**Design transfer checklist:**

| Transfer Item | Confirmed? | Date | By |
|--------------|-----------|------|-----|
| Engineering drawings released to production | | | |
| BOM finalised and procurement approved | | | |
| Work instructions drafted and approved | | | |
| Inspection plans (incoming, in-process, final) documented | | | |
| Acceptance criteria documented and understood by QA | | | |
| Production equipment qualified (IQ/OQ/PQ where required) | | | |
| Process validation completed (critical processes) | | | |
| First article inspection / pilot run completed | | | |
| Training completed for production personnel | | | |
| Calibration records for all measurement equipment | | | |
| DMR / technical file baselined | | | |

---

### Phase 6 — Post-Market Surveillance (Feeds Back into DHF)

Post-market information must be systematically collected and evaluated. This feeds back into the design and risk management process:

| PMS Data Source | Feeds Into |
|----------------|-----------|
| Complaints | CAPA system; risk management file update; vigilance reporting |
| Service/field reports | Risk management risk estimation update |
| Post-market surveillance reports | Clinical evaluation update (CER); PSUR |
| PMCF data | Clinical evaluation / CER |
| Regulatory authority signals | Risk management; possible design change |
| Literature surveillance | Clinical evaluation / CER update |
| Competitor / equivalent device data | Risk management; potential design improvement |

**Clinical evaluation / CER update frequency:**
- EU MDR Class III and implantable: Annual PSUR; annual CER update
- EU MDR Class IIa / IIb: Every 2 years PSUR; CER update with each PSUR
- All: Triggered update if new safety concerns arise

---

## Design History File (DHF) — Structure Template

The DHF (called Technical Documentation under EU MDR) is the master record of all design activities. It must be maintainable throughout the device's market lifetime.

### Recommended DHF Index

```
DHF-[Device Name]-[Version]
|
+-- Section 1: Device Overview and Intended Use
|   +-- Device description
|   +-- Intended use statement
|   +-- Indications and contraindications
|   +-- Patient population
|   +-- Regulatory classification justification
|
+-- Section 2: Design and Development Plan
|   +-- D&D plan (phases, milestones, responsibilities)
|   +-- Risk management plan
|
+-- Section 3: Design Inputs (Clause 7.3.3)
|   +-- User requirements document
|   +-- Design input specification (DIS) — all requirements
|   +-- Applicable standards list
|   +-- Regulatory requirements list
|
+-- Section 4: Design Outputs (Clause 7.3.4)
|   +-- Engineering drawings (current revision)
|   +-- Specifications (material, electrical, software)
|   +-- Bill of materials (BOM) — current revision
|   +-- Labelling and IFU
|   +-- Manufacturing process specifications
|
+-- Section 5: Design Traceability Matrix
|   +-- User need → Design input → Design output → Verification → Risk control
|
+-- Section 6: Design Reviews (Clause 7.3.5)
|   +-- Design review minutes per phase gate
|   +-- Action logs and closure records
|
+-- Section 7: Verification Records (Clause 7.3.6)
|   +-- Verification protocols and reports (by test category)
|   +-- Test data and certificates
|
+-- Section 8: Validation Records (Clause 7.3.7)
|   +-- Clinical evaluation / clinical data assessment
|   +-- Usability evaluation records
|   +-- Process validation records (reference to 7.5.6 records)
|   +-- Sterilisation validation records (reference to 7.5.7 records)
|   +-- Software validation records (IEC 62304)
|
+-- Section 9: Design Transfer Records (Clause 7.3.8)
|   +-- Transfer plan and checklist
|   +-- First article inspection report
|
+-- Section 10: Risk Management File (ISO 14971)
|   +-- Risk management plan
|   +-- Hazard identification
|   +-- Risk analysis and evaluation
|   +-- Risk controls
|   +-- Residual risk evaluation
|   +-- Benefit-risk analysis
|   +-- Risk management report
|   +-- Post-market risk monitoring records
|
+-- Section 11: Design Change Records (Clause 7.3.9)
|   +-- Change request forms
|   +-- Change impact assessments
|   +-- Regulatory change assessment (substantial modification?)
|   +-- Re-verification/re-validation records
|
+-- Section 12: Post-Market Data (ongoing — linked to PMS records)
|   +-- PMS plan and reports
|   +-- PMCF plan and evaluation reports
|   +-- CER (current version)
|   +-- PSUR (current version, if required)
```

---

## Design Change Control (Clause 7.3.9)

All changes to a released design must go through a formal change control process.

### Change Impact Assessment Elements

When a design change is requested, assess the following:

| Assessment Question | Yes/No | Action required if Yes |
|--------------------|--------|----------------------|
| Does the change affect the intended use or indication? | | New/updated clinical evaluation |
| Does the change affect device safety or performance? | | Re-verification / re-validation |
| Does the change affect biocompatibility? | | ISO 10993 re-evaluation |
| Does the change affect software? | | IEC 62304 change management |
| Does the change affect sterility? | | Sterilisation re-validation assessment |
| Does the change constitute a substantial modification? (EU MDR) | | Notified Body notification / new application |
| Does the change require a new/updated regulatory submission? (FDA) | | 510(k) / PMA supplement |
| Does the change affect labelling, IFU, or UDI? | | Labelling update; EUDAMED update |
| Does the change affect the risk profile? | | Risk management file update |
| Does the change affect supplier or component? | | Supplier notification; incoming re-qualification |

### When is a Change a "Substantial Modification" (EU MDR)?

Under EU MDR Art. 12, a substantial change to a certified device requires notified body involvement (notification at minimum, new application at maximum):

A change is generally substantial if it:
- Affects the device's intended purpose
- Significantly affects performance or safety (e.g., changes to materials, design, specifications that could affect safety and performance)
- Could affect patient/user safety in a way not already demonstrated acceptable

Changes that are generally NOT substantial:
- Administrative changes (company name, address) with no technical impact
- Errata corrections in labelling that do not affect safety information
- Equivalent material substitutions with documented equivalence

---

## Risk Management Integration (ISO 14971:2019)

Risk management and design controls are inseparable under ISO 13485. The risk management file (ISO 14971) must be initiated at the start of design and maintained throughout the device lifecycle.

### ISO 14971:2019 Process Summary

| Clause | Activity | Output |
|--------|---------|--------|
| 4 | Risk management planning | Risk management plan |
| 5 | Risk analysis | Hazard identification; risk estimation |
| 5.4 | Hazard identification | Hazard list; sequences of events |
| 5.5 | Risk estimation | Probability × Severity → Risk level |
| 6 | Risk evaluation | Compare to risk acceptability criteria |
| 7 | Risk control | Hierarchy: inherent safety → protective measures → information for safety |
| 8 | Evaluation of residual risks | Residual risk per hazard; overall residual risk |
| 9 | Risk management review and report | Summary of benefit-risk analysis; statement that overall residual risk is acceptable |
| 10 | Production/post-production information | PMS data feeds back into risk file; re-evaluation of risks if new data emerges |

### Risk Acceptability Matrix (Example — Organisation Must Define Own Criteria)

| | Severity 1 (Negligible) | Severity 2 (Minor) | Severity 3 (Serious) | Severity 4 (Critical) | Severity 5 (Catastrophic) |
|---|---|---|---|---|---|
| **Probability 5 (Frequent)** | Low | Medium | High | Unacceptable | Unacceptable |
| **Probability 4 (Probable)** | Low | Medium | High | Unacceptable | Unacceptable |
| **Probability 3 (Occasional)** | Low | Low | Medium | High | Unacceptable |
| **Probability 2 (Remote)** | Acceptable | Low | Medium | High | High |
| **Probability 1 (Improbable)** | Acceptable | Acceptable | Low | Medium | High |

Legend: Acceptable = no action; Low = review; Medium = control measures required; High = risk reduction mandatory; Unacceptable = design must be changed

---

## Design Review Record Template

```
DESIGN REVIEW RECORD
Review ID: DR-[number]
Device: [Device Name]
Phase Gate: [Phase number and name]
Date: [Date]
Location / Method: [In-person / video conference / hybrid]

ATTENDEES:
Name | Role | Department | Signature
[Engineering Lead | Sr. Engineer | R&D | ]
[Regulatory Affairs | RA Manager | Quality/Regulatory | ]
[Quality Assurance | QA Engineer | Quality | ]
[Clinical/Medical | Clinical Advisor | Clinical Affairs | ]
[Manufacturing | Mfg Engineer | Operations | ]

REVIEW AGENDA:
1. Actions from previous design review — status update
2. Design inputs status
3. Design outputs review
4. Verification/validation status
5. Risk management update (open risks, controls implemented)
6. Regulatory status
7. Any open issues / nonconformances affecting design

REVIEW FINDINGS:
Finding ID | Description | Risk Level | Assigned To | Due Date | Disposition
DR-[n]-01 | | | | |

GATE DECISION:
[ ] PASS — Proceed to next phase
[ ] CONDITIONAL PASS — Proceed with open actions listed above (all must be closed before Phase [n+1] begins)
[ ] FAIL — Do not proceed; return to [specify phase/activity]

Chaired by: _______________ Date: _______________
Quality approved by: _______________ Date: _______________
```

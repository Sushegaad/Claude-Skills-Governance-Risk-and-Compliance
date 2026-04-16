# TISAX Label Selection Guide
## Understanding TISAX Labels, Protection Needs, and OEM Requirements

---

## Overview of TISAX Labels

TISAX defines five labels, each addressing a different protection need. A single assessment
can cover multiple objectives, resulting in multiple labels from one engagement.

| Label | Short Name | Assessment Objective | Typical Trigger |
|-------|-----------|---------------------|-----------------|
| Information | IS | Information security (normal protection) | Processing OEM's internal information |
| Information High | IS-High | Information security (high protection needs) | Processing highly sensitive OEM data |
| Prototype | PP | Prototype and test vehicle protection | Physical access to pre-release vehicles/parts |
| Strict Prototype | PP-Strict | Enhanced prototype protection | Access to pre-production prototypes with high confidentiality |
| Data | DP | Data protection (GDPR alignment) | Processing personal data on behalf of the OEM |

---

## Label 1 — Information (IS)

### What It Covers

The IS label demonstrates that the supplier has implemented the minimum required
information security controls for handling confidential business information (CBI) from
automotive customers. It is the baseline label required by most OEM supplier programs.

### Required Assessment Level

- **AL 2** (on-site audit by licensed TISAX Audit Provider)
- AL 1 is generally not accepted by OEMs as proof of conformance

### VDA ISA Chapters Required

Chapters 1–14 (all mandatory chapters)

### When Is It Required?

- When the supplier receives documents, data, or systems access classified as
  "confidential" or "strictly confidential" by the OEM
- Electronic or paper documents, engineering drawings, financial projections,
  strategic plans, technical specifications
- Access to OEM IT systems (portals, PLM, ERP, engineering tools)

### Minimum Maturity Threshold

- All "must" criteria: Maturity ≥ 3
- Most standard criteria: Maturity ≥ 3 (individual failures may result in minor non-conformances)

---

## Label 2 — Information High (IS-High)

### What It Covers

IS-High is required when the information handled has an elevated protection requirement
beyond the normal IS label. The same VDA ISA chapters apply, but with stricter scoring
requirements and more rigorous Audit Provider scrutiny.

### Required Assessment Level

- **AL 3** (on-site audit with enhanced scrutiny and additional audit depth)

### VDA ISA Chapters Required

Chapters 1–14

### When Is It Required?

OEMs specify IS-High when the information shared meets one or more criteria:
- The potential damage from disclosure is severe (reputational, financial, strategic)
- The information is related to future vehicle programs or unreleased technology
- The supplier handles intellectual property at the cutting edge of the OEM's roadmap
- Regulatory or contractual requirements mandate higher assurance

### Enhanced Expectations (vs IS label)

| Area | IS Label | IS-High Label |
|------|---------|--------------|
| Privileged access management | MFA required | MFA + PAM tooling expected |
| Network segmentation | Segregation required | Documented micro-segmentation expected |
| Incident response testing | Documented plan | Documented plan + tested (exercises required) |
| Vulnerability management | Regular scanning | Continuous scanning + defined KPIs |
| Supplier IS requirements | Must address | Stronger supplier flow-down requirements |

---

## Label 3 — Prototype (PP)

### What It Covers

The Prototype label covers the protection of **pre-release vehicles, vehicle components,
and related confidential information** about vehicle design, features, and development.
This is triggered when a supplier physically works with or stores prototype vehicles
or major components.

### Required Assessment Level

- **AL 2** (on-site audit including inspection of prototype handling areas)

### VDA ISA Chapters Required

Chapters 1–14 (mandatory) + **Chapter 15** (prototype protection)

### When Is It Required?

- Supplier handles, stores, repairs, or transports prototype or test vehicles
- Supplier manufactures prototype components or assemblies
- Supplier personnel work at OEM prototype workshops handling pre-production vehicles
- Supplier provides driving dynamics, calibration, or testing services on prototypes

### Key Chapter 15 Requirements (Prototype Label)

| Requirement | Description |
|-------------|-------------|
| Prototype identification | All prototypes tracked and marked as confidential |
| Access control | Only authorized, trained personnel access prototype areas |
| Photography controls | No unauthorized photography; physical controls (signs, camera policies) |
| Transport procedures | Secure transport in covered vehicles; route approval process |
| Non-disclosure | NDAs for all personnel in contact with prototypes |
| Incident reporting | Unauthorized photography or disclosure incidents reported promptly |
| Document security | Technical prototype documentation handled as confidential information |

---

## Label 4 — Strict Prototype (PP-Strict)

### What It Covers

The Strict Prototype label is an elevated form of prototype protection for suppliers
working with the most confidential pre-production vehicles, typically covering:
- World premieres and strategic new model launches
- Revolutionary design or technology changes
- Vehicles with unreleased powertrain or feature innovations

### Required Assessment Level

- **AL 3** (on-site audit with enhanced physical security scrutiny)

### VDA ISA Chapters Required

Chapters 1–14 (mandatory) + **Chapter 15** (with strict requirements)

### When Is It Required?

OEMs require Strict Prototype when:
- The vehicle component/design is subject to media blackout
- Unauthorized disclosure would cause serious competitive or commercial damage
- The vehicle has not yet been publicly announced

### Enhanced Requirements (vs Prototype Label)

| Area | Prototype | Strict Prototype |
|------|----------|-----------------|
| Prototype area windows | No specific requirement | No windows or window coverings required |
| Photography controls | Policy and NDAs | Physical blocking + monitoring systems |
| External work | Supplier policy required | OEM pre-approval required for each activity |
| Transport | Covered vehicle and route rules | Covered vehicle + route pre-approval + tracking |
| Storage | Locked, access-controlled area | Dedicated locked area; inventory reconciliation |
| Subcontractor use | Must be disclosed | Must be pre-approved by OEM |

---

## Label 5 — Data (DP)

### What It Covers

The Data label demonstrates that the supplier processes personal data on behalf of
the OEM in compliance with applicable data protection legislation, primarily GDPR.

### Required Assessment Level

- **AL 2** (standard on-site audit) — for most scenarios
- **AL 3** (enhanced) — for large-scale personal data processing with high risk

### VDA ISA Chapters Required

Chapters 1–14 (mandatory) + **Chapter 16** (data protection)

### When Is It Required?

- Processing of personal data of OEM employees (HR outsourcing, payroll)
- Processing of end-customer/vehicle owner personal data
- Processing of vehicle telematics, driving behavior, or connected car data
- Any arrangement where the supplier acts as a GDPR Data Processor for the OEM

### Key Chapter 16 Requirements

| Requirement | GDPR Reference | Description |
|-------------|---------------|-------------|
| Lawful basis documentation | Art. 6 | Each processing activity has documented legal basis |
| ROPA maintenance | Art. 30 | Records of Processing Activities maintained |
| Data subject rights | Art. 15–22 | DSAR, erasure, portability processes operational |
| DPO appointment | Art. 37 | DPO designated where required; accessible |
| Privacy by design | Art. 25 | DPIA conducted for high-risk processing |
| Processor agreements | Art. 28 | DPA in place with OEM (and sub-processors) |
| International transfers | Art. 44–49 | Lawful mechanism for non-EEA transfers |
| Breach notification | Art. 33–34 | 72-hour notification procedure tested and ready |

---

## Multi-Label Assessments

A supplier can pursue multiple TISAX labels in a single assessment, provided:
- The scope covers all relevant objectives and locations
- Chapter 15 and/or Chapter 16 assessments are included

### Common Label Combinations

| Combination | Typical Supplier Type |
|------------|----------------------|
| IS + Prototype | Engineering supplier handling design data AND prototypes |
| IS + Data | IT service provider with access to OEM data including employee or customer data |
| IS + Prototype + Data | Full-service automotive supplier with end-to-end involvement |
| IS-High + Strict Prototype | Strategic supplier with access to unreleased flagship vehicle programs |

---

## OEM-Specific Requirements

Different OEMs have varying requirements for TISAX. The most common OEM requirements
as of 2024 are summarized below. **Always verify with the OEM contract team, as
requirements change.**

| OEM | Typical Minimum Requirement | Notes |
|-----|-----------------------------|-------|
| Volkswagen Group (incl. Audi, Porsche, SEAT, ŠKODA, Lamborghini, Bentley, TRATON) | IS (AL 2) | TISAX requirement enforced across VW Group supplier base |
| BMW Group (incl. MINI, Rolls-Royce) | IS (AL 2) | Required as part of BMW's sustainability and supplier compliance program |
| Mercedes-Benz / Daimler | IS (AL 2) | TISAX or equivalent IS evidence required for new and existing suppliers |
| Stellantis (PSA/FCA group) | IS (AL 2) | Required in European supplier contracts; expanding globally |
| Ford Europe | IS (AL 2) | Primarily for European supply chain; US operations may use separate frameworks |
| Renault | IS (AL 2) | Required for European supplier base |
| Tier 1 suppliers flow-down | IS (AL 2) minimum | Tier 1s increasingly requiring their own Tier 2 suppliers to be TISAX certified |

### Contract Review Tips

- Look for TISAX or VDA ISA references in the **Purchasing Conditions** or **Information Security Annex**
- Note: contracts may specify "ISO 27001 or equivalent" — verify whether the OEM accepts ISO 27001 in lieu of TISAX or requires both
- Check for the **required assessment level** specified (AL1, AL2, AL3)
- Note any clause about **submitting the TAI** to the OEM portal or supplier management system

---

## How to Share TISAX Results with OEMs

TISAX results are shared privately on the ENX portal. Results are never publicly disclosed.

### Sharing Steps

1. Log into ENX portal: https://enx.com
2. Navigate to your Assessment Scope (TAI)
3. Select "Share Results"
4. Enter the OEM's ENX Participant ID (provided by your OEM contact)
5. Confirm the sharing; the OEM receives a portal notification
6. Provide the OEM with your **TAI** so they can locate the result

### What the OEM Sees

- Your company name and ENX participant registration
- Assessment Scope description
- Label(s) achieved
- Assessment date and validity expiry date
- Audit Provider name (confirms licensed Audit Provider conducted the assessment)
- The OEM does **not** receive the full audit report

---

## Label vs. Certificate Distinction

TISAX does **not** issue certificates. A key distinction:

| TISAX Label | ISO 27001 Certificate |
|------------|----------------------|
| Private result; shared only when needed | Public certificate; freely publishable |
| Shared via ENX portal with specific companies | Certificate letter shared as document |
| Scope visible only to sharing parties | Scope listed on certificate |
| Industry-specific (automotive supply chain) | General-purpose international standard |
| 3-year validity with no interim surveillance | 3-year cycle with annual surveillance audits |
| Cannot be advertised publicly | Can be advertised, posted on website, tender docs |

Companies that want public evidence of IS compliance (e.g., for marketing) should
pursue ISO 27001 certification in addition to TISAX. The two are complementary
and share many control areas.

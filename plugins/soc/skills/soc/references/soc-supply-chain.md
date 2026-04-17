# SOC for Supply Chain Reference

## Overview

SOC for Supply Chain is an attestation framework published by the AICPA in **2020**. It
provides assurance to downstream customers and business partners about controls over an
organization's production and distribution system. It is designed for producers, manufacturers,
distributors, growers, and suppliers — any organization whose production or distribution
activities could introduce risk into the supply chains of their customers.

**Governing standard:** SSAE 18, AT-C Section 205 (*Examination Engagements*)  
**Description criteria:** AICPA DC-3 — *Description Criteria for a Report on Controls Over the Production and Distribution System* (2020)  
**Measurement criteria:** AICPA Trust Services Criteria (Security, Availability, Processing Integrity as applicable based on the nature of the production/distribution commitments)  
**Distribution:** Restricted use — shared only with management of the reporting entity and downstream customers (user layer entities) who rely on the production/distribution system

**Authoritative source:** AICPA *Reporting on an Examination of Controls Over the Production and Distribution System of a Service Organization for Organizations That Are Producers, Manufacturers, and Distributors* guide (2020).

---

## Target Organizations

SOC for Supply Chain applies to organizations in the following industries and roles:

| Industry/Role | Examples |
|---|---|
| Pharmaceutical manufacturing | Active pharmaceutical ingredient (API) manufacturers, contract drug manufacturers |
| Food and beverage production | Food processors, beverage bottlers, agricultural producers, co-manufacturers |
| Industrial and consumer goods manufacturing | Component suppliers, OEM manufacturers, contract manufacturers |
| Software and technology supply chain | Software publishers, firmware developers, component vendors |
| Third-party logistics (3PL) | Warehouse operators, freight forwarders, last-mile distributors |
| Raw material producers and growers | Commodity producers, mineral extractors, agricultural growers |
| Medical device manufacturing | Medical device OEMs, component suppliers |
| Aerospace and defense manufacturing | Defense contractors, aerospace component suppliers |

---

## Report Types

| Type | Coverage | Opinion Scope |
|---|---|---|
| Type 1 | As of a specific date | Description is fairly presented; controls are suitably designed |
| Type 2 | Over a stated period (recommended minimum 6 months; 12 months typical) | Description is fairly presented; controls are suitably designed; controls operated effectively throughout the period |

Type 2 is the more commonly requested report because it provides evidence of consistent
operation — which is what downstream customers and user auditors need.

---

## DC-3 Description Criteria — Full Detail

Management's description of the production and distribution system must address all eight
areas outlined in DC-3. The description must be sufficiently detailed for downstream customers
and user layer entities to understand the system and evaluate whether their own controls
(Complementary User Layer Entity Controls) are sufficient.

---

### DC-3.1 — Types of Products Produced and Services Provided

**What must be described:**
- The types of products produced or services provided by the organization.
- The nature of the production or distribution process.
- Principal commitments made to downstream customers:
  - Quality commitments (e.g., purity, composition, dimensional tolerances).
  - Security commitments (e.g., no unauthorized modifications to products).
  - Availability commitments (e.g., production capacity, delivery SLAs).
  - Processing integrity commitments (e.g., complete and accurate order fulfillment).

---

### DC-3.2 — Principal System Requirements

**What must be described:**
- Legal and regulatory requirements applicable to the production/distribution system:
  - FDA regulations (21 CFR Parts 110, 111, 117, 211 for pharmaceutical/food).
  - ISO 9001 quality management requirements (if certified).
  - Sector-specific standards (e.g., GMP, HACCP, ISO 13485).
- Contractual obligations with customers.
- Standards and certifications maintained.
- Environmental, health, and safety requirements affecting production.

---

### DC-3.3 — Components of the Production and Distribution System

**What must be described:**
The description uses the same five-component model as SOC 1 and SOC 2:

| Component | Examples in Production/Distribution Context |
|---|---|
| Infrastructure | Manufacturing plants, warehouses, logistics hubs, production equipment, quality testing equipment, IT infrastructure supporting production |
| Software | Manufacturing execution systems (MES), enterprise resource planning (ERP), warehouse management systems (WMS), quality management systems (QMS), process control software |
| People | Production operators, quality inspectors, logistics coordinators, supply chain managers, IT support for production systems |
| Processes | Production workflows, quality control procedures, pick-pack-ship processes, cold chain management, recall procedures |
| Data | Bills of materials, production orders, batch records, quality control test data, shipping records, inventory data |

---

### DC-3.4 — Nature of Principal Risks

**What must be described:**
Factors that have a significant effect on inherent risks in the production and distribution
system, including:

- **Operational disruption risks:** Factory outages, equipment failure, natural disasters.
- **Supply chain risks:** Single-source raw material dependency, upstream supplier failures, geopolitical supply chain disruptions.
- **Quality and safety risks:** Product contamination, formulation errors, undisclosed ingredient substitution.
- **Cybersecurity risks to OT/ICS:** Ransomware attacks on manufacturing systems, unauthorized changes to process control systems, IT/OT convergence vulnerabilities.
- **Cybersecurity risks to IT systems:** ERP system compromise, shipping manifest manipulation, order fraud.
- **Workforce risks:** Key personnel dependency, labor disputes, training adequacy.
- **Regulatory risks:** Non-compliance with FDA, EPA, OSHA, import/export controls.
- **Third-party (sub-supplier) risks:** Risks introduced by upstream suppliers or logistics providers.

---

### DC-3.5 — Goals and Objectives for Production and Distribution

**What must be described:**
- The entity's goals and objectives for its production and distribution system:
  - Quality objectives (defect rates, rejection thresholds, testing coverage).
  - Safety objectives (workplace safety, product safety, food/drug safety).
  - Security objectives (prevention of product tampering, unauthorized access, IP theft).
  - Availability objectives (production uptime, on-time delivery rates).
  - Processing integrity objectives (complete and accurate order fill rates, batch record integrity).
- How those objectives align with commitments made to downstream customers.

---

### DC-3.6 — Policies and Processes Used to Achieve Goals

**What must be described:**
The specific policies and processes implemented to achieve each goal and objective:

| Goal Area | Example Policies and Processes |
|---|---|
| Quality | Incoming material testing, in-process quality checks, finished goods testing, certificate of analysis (CoA) issuance, deviation and CAPA management |
| Safety | HACCP plans, GMP procedures, allergen control programs, temperature and humidity monitoring, product recall procedures |
| Security | Access control to production areas, change control over recipes and formulations, anti-tampering seals, chain of custody documentation |
| Availability | Preventive maintenance schedules, equipment redundancy, backup supplier agreements, business continuity plans |
| Processing integrity | Order verification procedures, batch record review and approval, shipping verification, reconciliation of shipped vs. ordered quantities |
| Cybersecurity | Network segregation of OT from IT, patch management for production systems, authentication controls for MES/ERP |

---

### DC-3.7 — Related Controls and Their Design

**What must be described:**
- For each policy and process described under DC-3.6, the specific controls implemented.
- Control descriptions should state:
  - What the control does.
  - Who performs it (role or automated system).
  - Frequency of operation.
  - Evidence generated by the control.

---

### DC-3.8 — Complementary User Layer Entity Controls (CULECs)

**What must be described:**
Controls that downstream customers (user layer entities) are assumed to implement for the
production and distribution commitments to be fully met.

Examples of CULECs:
- Downstream customers are responsible for verifying Certificate of Analysis (CoA) documentation before acceptance of goods.
- Downstream customers are responsible for maintaining cold chain integrity during warehousing and distribution of temperature-sensitive products.
- Downstream customers are responsible for notifying the reporting entity promptly of any quality complaints or adverse reactions observed in the finished product.
- Downstream customers are responsible for implementing receiving inspection procedures to identify damaged shipments.
- Downstream customers are responsible for configuring site-specific security settings in systems accessed via the reporting entity's customer portal.

---

## Measurement Criteria — Trust Services Criteria (Subset)

SOC for Supply Chain uses a subset of the AICPA Trust Services Criteria based on the
nature of the production/distribution commitments:

| TSC Category | Applicable When |
|---|---|
| Security (CC1–CC9) | Always applicable — cybersecurity risks to production systems and data |
| Availability (A1) | When commitments include production uptime, delivery availability, or order fulfillment SLAs |
| Processing Integrity (PI1) | When commitments include complete, accurate, valid, timely order processing or batch record integrity |
| Confidentiality (C1) | When confidential formulations, recipes, trade secrets, or customer data are processed |
| Privacy (P1–P8) | When the production/distribution system processes personal information |

For most manufacturing organizations, Security, Availability, and Processing Integrity are
the most relevant categories.

---

## Roles in SOC for Supply Chain

| Role | Definition |
|---|---|
| Reporting entity | The organization (producer, manufacturer, distributor) issuing the SOC for Supply Chain report |
| User layer entity | A downstream customer or business partner that relies on the reporting entity's production/distribution system |
| Sub-supplier | An upstream supplier used by the reporting entity to provide materials, components, or services forming part of the production/distribution system |
| Practitioner | The licensed CPA firm performing the examination |

---

## Sub-Supplier Considerations

When the reporting entity relies on upstream suppliers whose activities could affect the
production/distribution commitments:

**Documentation required:**
- Identify all material sub-suppliers in the system description.
- Describe the nature of sub-supplier services and their relationship to the commitments.
- Either:
  - **Carve-out:** Explicitly exclude sub-supplier controls from the description; describe monitoring controls over sub-suppliers.
  - **Inclusive:** Include sub-supplier controls in the description (requires sub-supplier cooperation).

**Common CULECs for sub-supplier scenarios:**
- The reporting entity is assumed to perform incoming testing of materials received from sub-suppliers.
- The reporting entity is assumed to qualify sub-suppliers against defined standards before use.

---

## SOC for Supply Chain vs SOC 1 vs SOC 2

| Attribute | SOC 1 | SOC 2 | SOC for Supply Chain |
|---|---|---|---|
| Primary focus | Financial transaction controls | IT/cloud service security and trust | Production and distribution integrity |
| Description criteria | AT-C §320 system description | TSC system description | DC-3 |
| Measurement criteria | Service org's own control objectives | TSC | TSC (subset applicable to production) |
| Distribution | Restricted | Restricted | Restricted |
| Typical industries | Financial services, payroll, SaaS | Cloud/SaaS, IT services | Manufacturing, logistics, agriculture |
| Cybersecurity component | As defined in control objectives | CC1–CC9 (Security required) | CC1–CC9 (Security required) |
| Published | 2017 (SSAE 18) | 2017 (SSAE 18) | 2020 |

---

## Engagement Readiness Checklist

### Documentation Readiness

- [ ] System description drafted covering all eight DC-3 areas
- [ ] Principal commitments to customers documented
- [ ] Legal/regulatory requirements identified
- [ ] System components (infrastructure, software, people, processes, data) documented
- [ ] Principal risk factors documented
- [ ] Goals and objectives for production/distribution documented
- [ ] Policies and processes mapped to each goal
- [ ] Controls mapped to each policy/process
- [ ] CULECs identified and documented

### Operational Readiness

- [ ] Controls are designed and implemented (not just documented)
- [ ] Control owners assigned for each control
- [ ] Evidence of control operation is retained (logs, approvals, inspection records, test results)
- [ ] Quality management records are complete and accessible
- [ ] Batch records, CoAs, and production logs are maintained and retrievable
- [ ] Change control procedures for production processes are operational
- [ ] Recall procedures documented and tested

### Cybersecurity Readiness (CC1–CC9)

- [ ] OT/ICS systems are identified and network-segmented from corporate IT
- [ ] Access to production systems is controlled and reviewed
- [ ] Change management for production software is documented
- [ ] Security monitoring includes production systems
- [ ] Incident response procedures address OT/ICS incidents
- [ ] Third-party (sub-supplier) risk program includes cybersecurity assessment
- [ ] Vulnerability management covers production technology

---

## Common Findings for SOC for Supply Chain

| Finding | Description | Remediation |
|---|---|---|
| Incomplete DC-3 description | One or more DC-3 areas are not addressed in the system description | Review DC-3 requirements; expand description draft to cover missing areas |
| Production system undocumented | Manufacturing processes not formally documented | Complete process documentation; assign document owners |
| No formal quality management | QC testing exists but is informal; records inconsistent | Implement documented QMS; standardize testing records |
| CULEC gaps | Customer commitments rely on user layer controls not listed as CULECs | Identify user layer dependencies; document CULECs explicitly |
| Sub-supplier not identified | Key material supplier not identified in description | Update sub-supplier list; determine carve-out or inclusive treatment |
| OT/ICS not in scope | Cybersecurity of production control systems excluded without justification | Evaluate whether OT/ICS falls within system boundaries; document exclusion with rationale if excluded |
| Change control absent | Production recipe or process changes occur without documented authorization | Implement and enforce change control for all production changes |
| No BCP for production | Business continuity plan exists for IT but not for production environment | Extend BCP to cover production equipment, facilities, and supply chain |

---

## Frequently Asked Questions

**Q: Is SOC for Supply Chain the same as ISO 9001?**  
No. ISO 9001 is a quality management system certification issued by an ISO accredited certification
body. SOC for Supply Chain is an AICPA attestation engagement performed by a licensed CPA firm
that examines controls over production and distribution systems against Trust Services Criteria.
ISO 9001 focuses on quality management processes; SOC for Supply Chain addresses security,
availability, processing integrity, and quality-related controls through the TSC measurement lens.

**Q: Who distributes the SOC for Supply Chain report?**  
SOC for Supply Chain is a restricted-use report. It is shared only with: (1) the management
of the reporting entity; (2) downstream customers (user layer entities) that rely on the
production/distribution system; and (3) their auditors. It is not a publicly available report.

**Q: What evidence should a manufacturer collect for a Type 2 examination?**  
Evidence should demonstrate consistent operation of each control throughout the period. Types of
evidence include: production batch records, quality control test results, CoAs, equipment
maintenance logs, access control records, change authorization records, audit logs from MES/ERP
systems, incoming inspection reports, CAPA records, temperature monitoring records, and incident
reports.

**Q: Can SOC for Supply Chain and SOC 2 be issued for the same organization?**  
Yes. A technology company that also manufactures hardware, for example, could obtain a SOC 2
report for its cloud services and a SOC for Supply Chain report for its hardware manufacturing
operations. The reports address different systems with different criteria.

**Q: How does SOC for Supply Chain address cybersecurity in OT environments?**  
The CC1–CC9 Security criteria apply to all technology systems within the production/distribution
system boundary, including operational technology (OT), industrial control systems (ICS), SCADA
systems, and manufacturing execution systems. The description under DC-3 must identify OT/ICS
components and the cybersecurity controls applied to them. This is an area that receives
increased scrutiny from practitioners given the elevated risk of ICS/OT compromise in
manufacturing environments.

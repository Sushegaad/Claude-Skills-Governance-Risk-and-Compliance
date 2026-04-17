# NIST SP 800-161 Rev 1 — SR Control Family Implementation Guidance

**Source**: NIST SP 800-161 Rev 1, May 2022; NIST SP 800-53 Rev 5, SR family

---

## SR Control Family Overview

The Supply Chain Risk Management (SR) control family was introduced in NIST SP 800-53 Rev 5 to address C-SCRM requirements at the information system level. It contains 12 base controls (SR-1 through SR-12) plus enhancements. SP 800-161 Rev 1 provides detailed implementation guidance for each SR control and its enhancements.

---

## SR-1 — Policy and Procedures

**Intent**: Establish and maintain a formal, documented, and disseminated C-SCRM policy.

**Required policy content**:
- Purpose and scope (all ICT acquisitions at all tiers)
- Roles and responsibilities for C-SCRM
- Mandatory requirements (supplier vetting, contract clauses, SBOM, notification)
- Compliance requirements and consequences
- Review frequency (at minimum annually, and upon significant change)

**Required procedures content**:
- Procedures implementing each SR control
- Procedures for supplier incident notification response
- Procedures for counterfeit component detection and response
- Procedures for C-SCRM plan maintenance and review

**Implementation notes**:
- Policy must be approved by senior leadership (CIO or SAORM)
- Policy must be explicitly scoped to include cloud services, FOSS, and COTS products
- Procedures must be actionable and role-specific

---

## SR-2 — Supply Chain Risk Management Plan

**Intent**: Develop a formal C-SCRM Plan covering enterprise, mission/business, and system levels.

**Plan required elements**:
1. Scope and applicability
2. Organisational risk tolerance for supply chain risk
3. Critical ICT components and services inventory (the "critical asset list")
4. Supplier inventory with tier classifications
5. Risk assessment approach and results summary
6. Controls applied per risk tier (SR controls implementation)
7. Monitoring activities and frequencies
8. Incident response procedures for supply chain events
9. Plan review and update cycle

**Multi-tier coverage requirements**:
- Tier 1 (Enterprise): strategy, risk tolerance, programme governance
- Tier 2 (Mission/Business): mission-critical supplier identification, programme/project level oversight
- Tier 3 (System): system-specific control implementation, component-level provenance

**SR-2(1) — Establish SCRM Team** (M/H):
- Establish a formal C-SCRM team (may be a cross-functional working group)
- Required representation: procurement/acquisition, IT/cybersecurity, legal, mission/programme owners
- Define team charter, meeting cadence, and escalation authority
- Team is responsible for: supplier assessments, policy updates, C-SCRM plan maintenance, incident coordination

---

## SR-3 — Supply Chain Controls and Processes

**Intent**: Establish processes to identify and address supply chain risks for systems, components, and services.

**Required processes**:
- Process for identifying new ICT acquisitions and triggering C-SCRM review
- Process for classifying acquisitions by risk tier (critical, high, moderate, low)
- Process for selecting and applying controls based on risk tier
- Process for monitoring the supply chain for in-service systems

**SR-3(1) — Diverse Supply Base**:
- Maintain awareness of single-source dependencies for critical components
- Where single-source dependency exists, document the risk and mitigation (e.g., strategic reserve, alternative qualification plan)
- Preference for multiple qualified suppliers where mission impact justifies the investment

**SR-3(2) — Limitation of Harm**:
- Implement contractual provisions limiting adversary ability to benefit from supply chain access
- Examples: IP segregation requirements, background check requirements for personnel with access to sensitive components, security incident disclosure within 72 hours

**SR-3(3) — Sub-Tier Flow Down**:
- Require prime contractors to flow down C-SCRM requirements to sub-tier suppliers in contract clauses
- Require prime contractors to maintain and provide a sub-tier supplier list upon request
- Require notification from prime if a sub-tier supplier changes for a critical component

---

## SR-4 — Provenance

**Intent**: Document and maintain provenance records for system components from design through disposal.

**Provenance documentation minimum content**:
| Field | Description |
|---|---|
| Component identifier | Unique part number, serial number, or SWID/CPE identifier |
| Manufacturer | Legal name and country of origin of the manufacturing entity |
| Developer/Software supplier | Legal name of the software developer (if different from manufacturer) |
| Chain of custody | Record of all entities that possessed the component from manufacture to delivery |
| Date of manufacture | Date or date range |
| Version/revision | Hardware version or software version |
| Acquisition source | Authorised distributor or direct manufacturer; intermediary chain if applicable |
| Integrity evidence | Hash values for software; physical inspection record for hardware |
| Sub-component traceability | For complex assemblies: list of sub-components with their own provenance |

**Maintenance requirements**:
- Provenance records must follow the component throughout its operational life
- Records must be updated upon any maintenance, repair, or update
- Records must be retained for the operational life plus applicable records retention period

**SR-4(1) — Identity**:
- Maintain authoritative identity information (legal name, address, DUNS/CAGE code or UEI) for all critical suppliers
- Verify identity upon initial onboarding and whenever a supplier undergoes corporate change

**SR-4(2) — Track and Trace**:
- For critical hardware: implement asset tracking that captures location and custody throughout lifecycle
- Acceptable mechanisms: RFID, barcoding, serial number databases, chain-of-custody logs

**SR-4(3) — Validate as Genuine and Not Altered**:
- For critical software: verify cryptographic signatures/hashes provided by the developer
- For critical hardware: use manufacturer-provided authenticity features (holograms, physical unclonable functions, tamper-evident seals)
- Document validation results before component deployment

**SR-4(4) — Supply Chain Integrity — Pedigree**:
- For the highest criticality components: obtain a formal pedigree document from the prime contractor or developer
- Pedigree documents all sub-components with their own provenance and chain-of-custody records

---

## SR-5 — Acquisition Strategies, Tools, and Methods

**Intent**: Implement acquisition strategies and procurement methods that protect the supply chain.

**Acquisition strategies**:
- Preference for direct acquisition from original equipment manufacturers (OEMs) or authorised distributors for critical components
- Use of government-wide acquisition contracts (GWACs) that include C-SCRM requirements
- Avoidance of grey-market or unvetted broker channels for critical components
- Phased acquisition allowing incremental acceptance and testing

**Contract mechanisms**:
- C-SCRM terms and conditions (see supplier-assessment.md contract clauses)
- Right-to-audit provisions for critical suppliers
- Notification requirements (aligned to SR-8)
- Warranties and representations regarding component authenticity and integrity
- Incident disclosure requirements (72-hour notification)
- Subcontractor approval and flow-down requirements
- SBOM delivery as a contract deliverable

**SR-5(1) — Adequate Supply**:
- Identify critical components with limited availability or long lead times
- Maintain strategic inventory or pre-positioned spares for the highest criticality components
- Include continuity of supply as an evaluation criterion in source selection for critical components

**SR-5(2) — Assessments Prior to Selection, Acceptance and Update**:
- Conduct supplier assessments before contract award for critical or high-risk acquisitions
- Conduct component-level testing/inspection before acceptance for critical hardware
- Conduct malicious code scanning before deploying new or updated software for critical systems

---

## SR-6 — Supplier Assessments and Reviews

**Intent**: Assess and review suppliers of critical system components at defined frequencies.

**Assessment types**:

| Type | Description | When Used |
|---|---|---|
| Documentation review | Review supplier-provided security documentation, policies, certifications | All critical/high-risk suppliers |
| Questionnaire | Structured questionnaire covering security programme, practices, and controls | All critical/high-risk suppliers |
| Third-party assessment | Use a qualified third party (e.g., CMMC C3PAO, ISO 27001 certification body) | Moderate and high-risk suppliers |
| On-site audit | Direct inspection of supplier facilities and practices | Highest criticality suppliers; where concerns exist |
| Penetration testing | Technical testing of supplier-facing interfaces | Where contractually permitted and risk warrants |

**Assessment frequency guidance**:
- Critical suppliers: annual
- High-risk suppliers: every two years or upon significant change
- Moderate-risk suppliers: every three years or upon significant change

**Triggers for unscheduled reassessment**:
- Supplier corporate change (acquisition, change in ownership, new foreign investment)
- Supplier security incident affecting components used by the organisation
- Published CVEs in supplier products
- Regulatory finding against the supplier
- Intelligence reporting indicating elevated risk

**SR-6(1) — Testing and Analysis**:
- For critical hardware components: conduct physical or radiographic inspection, or use manufacturer authentication features before deployment
- For critical software components: conduct static analysis, dynamic analysis, or malicious code scanning using approved tools
- Document testing results and retain as provenance record

---

## SR-7 — Supply Chain Operations Security

**Intent**: Implement OPSEC measures to protect supply chain operations.

**OPSEC measures**:
- Limit information about critical component specifications, quantities, and deployment timeline to need-to-know individuals
- Do not publish acquisition schedules, system configurations, or component types in publicly accessible documents
- Protect RFP documents and SOW details that reveal critical ICT component requirements from adversary exploitation
- Apply need-to-know access controls to provenance databases and supplier databases
- Classify or protect information about acquisition strategies for the highest criticality systems

**OPSEC assessment**:
- Periodically review what supply chain information is publicly accessible (website, press releases, SAM.gov postings)
- Identify whether adversaries could construct a profile of the organisation's critical ICT dependencies from open sources
- Mitigate identified OPSEC risks

---

## SR-8 — Notification Agreements

**Intent**: Establish notification agreements with suppliers requiring disclosure of vulnerabilities, incidents, changes, and end-of-life.

**Notification agreement required elements**:

| Notification Type | Timeframe | Content Required |
|---|---|---|
| Critical/High vulnerability in delivered products | 72 hours of supplier discovery | CVE (if issued), affected versions, workaround, patch timeline |
| Security incident affecting the supply chain | 72 hours | Nature of incident, affected products/services, potential exposure, remediation steps |
| Significant change to development or manufacturing environment | 30 days before change when practicable | Description of change, security assessment conducted, impact on delivered products |
| Sub-tier supplier change for critical components | 30 days before transition | Name of new supplier, reason for change, assessment of new supplier |
| End-of-life / End-of-support announcement | 12 months in advance where possible | EOL date, migration path, available alternatives, support terms post-EOL |
| Change in ownership, acquisition, or significant foreign investment | 30 days | Nature of change, impact on security posture |

**Implementation**:
- Notification agreements are incorporated as contract clauses at the time of acquisition
- For existing contracts without notification clauses: incorporate at next contract renewal or modification
- Define the organisational point of contact (C-SCRM Programme Manager or ISSO) to receive notifications
- Define the internal response process triggered by each notification type

---

## SR-9 — Tamper Resistance and Detection

**Intent** (High baseline): Implement anti-tamper technologies and techniques on critical systems and components.

**Anti-tamper technologies**:
- Tamper-evident seals and labels on hardware
- Physical Unclonable Functions (PUFs) embedded in critical ICs
- Cryptographically sealed firmware with secure boot and measured boot
- Hardware Security Modules (HSMs) with tamper-detection and zeroization on physical attack
- Epoxy potting of sensitive circuits to prevent probing
- X-ray inspection of received shipments for embedded components

**Anti-tamper implementation guidance**:
1. Identify the components warranting anti-tamper measures based on criticality and threat assessment
2. Select anti-tamper technologies appropriate to the threat (nation-state capability vs. opportunistic)
3. Document the anti-tamper posture as part of the provenance record
4. Train personnel on how to detect evidence of tampering and what to report

**SR-9(1) — Inspection of Systems or Components**:
- Inspect systems and components for evidence of tampering before deployment
- Re-inspect upon return from servicing, repair, or extended deployment in untrusted environments
- Document inspection results

---

## SR-10 — Inspection of Systems or Components

**Intent** (M/H): Inspect system components using defined inspection methods before each instantiation and at defined periodic intervals.

**Inspection methods by component type**:

| Component Type | Inspection Method |
|---|---|
| Software | Hash verification against known-good hash from developer; malicious code scan; SBOM-based component vulnerability check |
| Firmware | Hash verification; secure boot attestation |
| Hardware (commodity) | Visual inspection; vendor authentication verification; tamper-evident seal check |
| Hardware (critical/custom) | As above plus: X-ray or CT scan if justified; functional testing; PUF challenge-response |
| Removable media | Malicious code scan before connection to sensitive systems |

**Instantiation**: Each time a software component is deployed (including updates), verification should occur. Hardware inspection occurs at delivery and at defined intervals (annual for the highest criticality components).

---

## SR-11 — Component Authenticity

**Intent** (M/H): Implement anti-counterfeiting policy, procedures, and technologies.

**Anti-counterfeiting policy must cover**:
- Definition of counterfeit (applies to hardware and software)
- Approved procurement channels (only OEM, authorised distributors)
- Prohibited channels (grey market, unknown brokers, resellers without authorised distributor status)
- Receipt inspection procedures
- Counterfeit detection process triggers
- Counterfeit reporting requirements (internal + GID reporting if applicable)
- Disposal of suspect/confirmed counterfeit items

**Hardware anti-counterfeiting techniques**:
- Manufacturer-applied authentication markings (holographic labels, 2D barcodes with verification)
- Part marking verification (match stated part number against physical markings and spec sheets)
- Physical inspection (workmanship, surface finish, solder quality for suspect components)
- Electrical testing (verify component meets specified performance)
- Use of SAQR scanning (Surface Analytics Quick Response) where available

**Software anti-counterfeiting**:
- Acquire software only from the developer's official channel or authorised reseller
- Verify code-signed installers against developer certificates
- Use package manager signature verification
- Verify license keys and activation codes against developer records

**SR-11(1) — Anti-Counterfeiting Training**:
- Train procurement personnel on approved procurement channels and prohibited channels
- Train receiving/inspection personnel on visual and physical counterfeit detection
- Train IT personnel on software license and code signature verification

**SR-11(2) — Configuration Control for Component Service and Repair**:
- When a component is sent out for service or repair, track its departure and return using the provenance record
- Verify component identity and integrity upon return before reinstallation
- If the component cannot be verified after return, treat it as untrusted and replace

**SR-11(3) — Anti-Counterfeiting Scanning**:
- Deploy automated scanning tools where available to detect suspect components
- Report suspect counterfeit parts through appropriate channels (GIDEP, supplier notification)

---

## SR-12 — Component Disposal

**Intent** (L/M/H): Dispose of system components in a manner that prevents data recovery and prevents component re-entry into the supply chain as counterfeit.

**Data destruction requirements**:
- Hard drives, SSDs, and storage-capable components: apply NIST SP 800-88 media sanitisation guidelines (Clear, Purge, or Destroy based on classification)
- Cryptographic modules: zeroize to FIPS 140 requirements
- Devices in cloud/virtualised environments: use provider-provided secure deletion with certification

**Anti-counterfeit disposal**:
- Components designated for disposal must be physically destroyed (shredding, degaussing + physical destruction) or returned to the manufacturer
- Do not donate, surplus-sell, or otherwise release critical components to channels where they could re-enter the supply chain as counterfeit
- Document disposal with a certificate of destruction
- Maintain disposal records in the provenance record

**Disposal authorisation**: Disposal of critical components requires authorisation from the system owner and C-SCRM programme manager.

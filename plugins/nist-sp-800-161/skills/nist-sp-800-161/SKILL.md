---
name: nist-sp-800-161
description: >
  NIST SP 800-161 Rev 1 Cybersecurity Supply Chain Risk Management (C-SCRM) skill. Answers questions
  about establishing enterprise C-SCRM programmes, implementing the SR control family from SP 800-53
  Rev 5, supplier vetting and assessments, SBOM (Software Bill of Materials) requirements, provenance
  documentation, acquiring secure ICT products and services, identifying and protecting critical
  components, integrating C-SCRM into the acquisition lifecycle, prime and sub-tier supplier
  management, C-SCRM policies and plans, hardware and software supply chain threats, counterfeit
  component detection, third-party risk management for federal information systems, and aligning
  supply chain security with the NIST Cybersecurity Framework.
---

# NIST SP 800-161 Rev 1 — Cybersecurity Supply Chain Risk Management (C-SCRM)

**Source**: NIST Special Publication 800-161 Revision 1, May 2022
**Full Title**: Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations
**CSRC URL**: https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final

---

## Purpose and Scope

NIST SP 800-161 Rev 1 provides guidance to federal agencies and other organisations for identifying, assessing, and mitigating cybersecurity risks throughout the supply chain of information and communications technology (ICT) products and services. The guidance helps organisations manage risks introduced by suppliers, developers, system integrators, external system service providers, and other ICT related service providers.

**C-SCRM** addresses the entire lifecycle of ICT products and services: design, development, distribution, deployment, acquisition, maintenance, and end-of-life/disposal.

---

## C-SCRM Foundation

### Key Concepts

**Supply Chain**: The linked set of resources and processes between multiple tiers of developers, integrators, and maintainers that transforms raw inputs into a finished product or service that is delivered to the end user.

**ICT Supply Chain Risk**: The susceptibility of an organisation's ICT supply chain to disruption, compromise, or failure resulting from vulnerabilities, threat events, and/or hazards affecting the ICT products and services it uses.

**C-SCRM**: The process of identifying, assessing, and mitigating the risks associated with the distributed and interconnected nature of ICT product and service supply chains.

### Supply Chain Threats

| Category | Description | Examples |
|---|---|---|
| Counterfeit components | Non-genuine hardware or software falsely represented as meeting specifications | Fake memory chips, cloned microprocessors, pirated software |
| Tampered products | Genuine products modified to introduce vulnerabilities or backdoors | Hardware trojans in ICs, malicious firmware updates, backdoored software |
| Inferior or fraudulent products | Products that do not meet stated specifications or security requirements | Below-spec hardware that fails under load, fraudulent certifications |
| Theft of sensitive information | Intellectual property or configuration data exfiltrated during production or transit | Design theft, source code theft, configuration exfiltration |
| Installation of malicious code | Malware or logic bombs inserted during development, manufacturing, or delivery | Supply chain malware (e.g., SUNBURST/SolarWinds), poisoned software updates |
| Poor manufacturing/development practices | Insecure development or manufacturing that introduces unintentional vulnerabilities | Insecure coding practices, lack of build integrity controls |

---

## C-SCRM Multi-Tier Model

C-SCRM operates across a multi-tier supply chain:

### Tier 1 — Enterprise (Organisation Level)
- Establishes the enterprise C-SCRM strategy, policy, and programme
- Sets organisational risk tolerance for supply chain risks
- Assigns responsibilities and resources
- Integrates C-SCRM into enterprise-wide risk management

### Tier 2 — Mission/Business Process Level
- Implements C-SCRM in support of specific missions and business functions
- Identifies mission-critical ICT products and services
- Assesses supply chain risks for mission-critical components
- Manages supplier relationships at the programme/project level

### Tier 3 — Information System Level
- Implements system-specific C-SCRM controls
- Applies C-SCRM requirements in the acquisition and deployment of system components
- Monitors the supply chain for in-service systems
- Implements the SP 800-53 Rev 5 SR control family at the system level

### Supplier Tiers
- **Prime Contractor/Developer**: Direct supplier to the organisation
- **Sub-tier Supplier**: Suppliers to the prime contractor (second and third tier)
- **Component Manufacturer**: Lowest tier; manufactures hardware or software components

C-SCRM must look beyond the prime contractor to identify and address sub-tier risks. Compromise often enters at lower supplier tiers that the acquirer has no direct relationship with.

---

## C-SCRM Programme Components

A complete enterprise C-SCRM programme includes:

### 1. C-SCRM Policy
A formal organisational policy directing C-SCRM activities:
- Scope: all ICT products and services acquired and used
- Risk tolerance statement for supply chain risk
- Mandatory requirements (e.g., supplier vetting, contract clauses, SBOM requirements)
- Roles and responsibilities
- Compliance and enforcement

### 2. C-SCRM Strategy
An enterprise strategy document addressing:
- Organisational risk tolerance specific to supply chain
- Methods for identifying and prioritising ICT supply chain risks
- Integration with enterprise risk management
- Integration with acquisition and procurement processes
- Methods for communicating C-SCRM requirements to suppliers
- Metrics for measuring C-SCRM effectiveness

### 3. C-SCRM Plan
An operational plan implementing the strategy:
- Critical ICT components and services inventory
- Supplier inventory with tier mapping
- Risk assessment results per critical component/supplier
- Controls applied per risk level
- Monitoring activities and frequencies
- Incident response procedures for supply chain incidents

### 4. C-SCRM Controls Implementation
Implementation of relevant SP 800-53 Rev 5 controls, primarily the SR family (see SR Control Family section below).

---

## Critical ICT Component Identification

Critical components are those whose failure, compromise, or substitution would have severe consequences for the mission, business process, or information system.

### Identification Criteria
A component is considered critical if:
- It processes, stores, or transmits sensitive or classified information
- Compromise would directly enable adversary access to the system or its data
- It is a single point of failure for mission-critical functions
- It performs security functions (cryptographic modules, authentication systems, firewalls, PKI)
- It is difficult or impossible to replace quickly if compromised
- The supplier is in a high-risk geography or is under foreign state control

### Critical Component Handling Requirements
Once identified as critical, a component must:
- Have provenance documentation maintained throughout its lifecycle
- Be subject to enhanced supplier vetting
- Have an SBOM or equivalent component transparency document
- Be subject to integrity verification before deployment
- Have disposal and end-of-life handling procedures that prevent data reconstruction

---

## SP 800-53 Rev 5 Supply Chain Risk Management (SR) Control Family

The SR control family (introduced in SP 800-53 Rev 5) directly addresses C-SCRM:

| Control ID | Control Name | Baseline | Description |
|---|---|---|---|
| SR-1 | Policy and Procedures | L/M/H | Develop, document, and disseminate SR policy and procedures |
| SR-2 | Supply Chain Risk Management Plan | L/M/H | Develop a C-SCRM plan addressing organisational-level, mission/business-level, and system-level supply chain risks |
| SR-2(1) | Supply Chain Risk Management Plan — Establish SCRM Team | M/H | Establish a dedicated team or function responsible for C-SCRM |
| SR-3 | Supply Chain Controls and Processes | L/M/H | Establish and implement processes to identify and address supply chain risks for systems, components, and services |
| SR-3(1) | Diverse Supply Base | — | Employ a diverse set of suppliers to reduce single-source dependencies |
| SR-3(2) | Limitation of Harm | — | Employ acquisition strategies and contract mechanisms to limit harm from compromised systems or components |
| SR-3(3) | Sub-Tier Flow Down | — | Require prime contractors to ensure C-SCRM requirements flow down to sub-tier suppliers |
| SR-4 | Provenance | M/H | Document and maintain provenance records for system components from design through disposal |
| SR-4(1) | Identity | — | Maintain supplier identity information throughout the supply chain |
| SR-4(2) | Track and Trace | — | Implement mechanisms to track and trace system components throughout the supply chain |
| SR-4(3) | Validate as Genuine and Not Altered | — | Employ additional measures to validate the integrity of components |
| SR-4(4) | Supply Chain Integrity — Pedigree | — | Maintain a pedigree of system components tracking chain of custody |
| SR-5 | Acquisition Strategies, Tools, and Methods | L/M/H | Implement acquisition strategies, contract mechanisms, and procurement methods to protect the supply chain |
| SR-5(1) | Adequate Supply | — | Obtain sufficient supply of critical components to satisfy continuity requirements |
| SR-5(2) | Assessments Prior to Selection, Acceptance and Update | — | Conduct organisational assessments of ICT products and services prior to selection, acceptance, or update |
| SR-6 | Supplier Assessments and Reviews | M/H | Assess and review suppliers of critical system components at defined frequencies |
| SR-6(1) | Testing and Analysis | — | Test and analyse acquired components for malicious code, logic bombs, and exploitable vulnerabilities prior to deployment |
| SR-7 | Supply Chain Operations Security | M/H | Implement OPSEC measures to protect supply chain operations from adversary reconnaissance and exploitation |
| SR-8 | Notification Agreements | L/M/H | Establish notification agreements with suppliers requiring disclosure of vulnerabilities, incidents, changes, and end-of-life notification |
| SR-9 | Tamper Resistance and Detection | H | Implement anti-tamper technologies and techniques on critical systems and components |
| SR-9(1) | Inspection of Systems or Components | — | Inspect systems and components for evidence of tampering prior to deployment and periodically thereafter |
| SR-10 | Inspection of Systems or Components | M/H | Inspect system components using defined inspection methods before each instantiation and at defined frequencies |
| SR-11 | Component Authenticity | M/H | Implement anti-counterfeiting policy and procedures and employ anti-counterfeiting technologies where feasible |
| SR-11(1) | Anti-Counterfeiting Training | — | Train personnel on how to detect counterfeit system components |
| SR-11(2) | Configuration Control for Component Service and Repair | — | Maintain configuration control during service and repair |
| SR-11(3) | Anti-Counterfeiting Scanning | — | Scan for counterfeit components using defined scanning tools and techniques |
| SR-12 | Component Disposal | L/M/H | Dispose of data, documentation, tools, or system components in a manner that prevents recovery after the system or component reaches end-of-life |

**Note on SR control baselines**: SR-1, SR-2, SR-3, SR-5, SR-8, SR-12 apply to all baselines (L/M/H). SR-4, SR-6, SR-7, SR-10, SR-11 apply to Moderate and High baselines. SR-9 applies to High baseline only.

---

## Software Bill of Materials (SBOM)

An SBOM is a formal record containing the details and supply chain relationships of all components used in building software.

### SBOM Minimum Data Fields (per NTIA consensus)
| Field | Description |
|---|---|
| Supplier Name | Name of the entity that creates, defines, and identifies the component |
| Component Name | Designation assigned to a unit of software defined by the original supplier |
| Version of the Component | Identifier used by the supplier to specify a change in software from a previously identified version |
| Other Unique Identifiers | Other identifiers used to identify a component (package URL, SWID tag, CPE) |
| Dependency Relationship | Characterising the relationship that an upstream component X is included in software Y |
| Author of SBOM Data | The name of the entity that created the SBOM data for this component |
| Timestamp | Record of the date and time of the SBOM data assembly |

### SBOM Formats
- **SPDX** (Software Package Data Exchange — ISO 5962): Linux Foundation standard
- **CycloneDX**: OWASP standard, XML/JSON
- **SWID Tags** (ISO 19770-2): Software Identification tags

### SBOM Use in C-SCRM
- Required for critical software components (aligned with EO 14028 requirements)
- Enables organisations to identify vulnerable components when a CVE is published
- Supports provenance documentation (SR-4)
- Enables faster incident response when supply chain compromises are discovered

---

## Acquisition Lifecycle Integration

C-SCRM requirements must be integrated at each phase of the acquisition lifecycle:

### Phase 1 — Requirements Definition
- Identify whether the acquisition involves critical ICT components
- Include C-SCRM requirements in the Statement of Work (SOW) or Statement of Objectives (SOO)
- Define supplier vetting requirements
- Define SBOM requirements for software-intensive acquisitions
- Define notification requirements (SR-8)

### Phase 2 — Market Research and Source Selection
- Research suppliers for C-SCRM risk indicators (country of origin, ownership, prior incidents)
- Use approved supplier lists where available
- Evaluate supplier C-SCRM practices as selection criteria
- Apply higher scrutiny to sole-source acquisitions

### Phase 3 — Contract Award
- Include C-SCRM contract clauses (mandatory flow-down of security requirements to sub-tier suppliers)
- Include right-to-audit provisions for critical suppliers
- Include notification requirements for vulnerabilities, incidents, and changes
- Include counterfeit prevention requirements for hardware
- Define SBOM delivery as a contract deliverable for software

### Phase 4 — Delivery and Acceptance
- Verify component provenance before acceptance
- Conduct pre-deployment testing for malicious code and counterfeit components where risk warrants
- Validate SBOM delivery and content
- Update system inventory and provenance records

### Phase 5 — Operations and Maintenance
- Monitor suppliers for relevant vulnerability disclosures (coordinate with SI-5 Security Alerts)
- Conduct periodic supplier reviews (SR-6)
- Respond to notification agreement disclosures
- Manage updates and patches through secure channels
- Monitor for new sub-tier supplier risks

### Phase 6 — Disposal and End-of-Life
- Apply SR-12 disposal requirements
- Ensure sensitive data is destroyed
- Manage surplus equipment to prevent component re-entry into the supply chain as counterfeit

---

## Supplier Assessment

### Supplier Risk Tiers
Categorise suppliers by risk:

| Tier | Description | Assessment Required |
|---|---|---|
| Critical | Supplies components for high-impact systems; single-source; foreign ownership or presence | Full assessment: questionnaire, on-site audit, reference checks, third-party assessment |
| High | Multi-source; moderate impact systems; significant software content | Questionnaire, documentation review, reference checks |
| Moderate | Standard commercial products; well-established vendor; competitive market | Documentation review, certifications verification |
| Low | Commodity products; multiple sources; publicly traded US company | Standard procurement due diligence |

### Supplier Assessment Areas
1. **Security programme**: Does the supplier have a documented information security programme?
2. **Secure development**: Does the supplier follow secure development practices (SSDF/SP 800-218)?
3. **Sub-tier management**: Does the supplier flow down C-SCRM requirements to its sub-contractors?
4. **Incident response**: Does the supplier have an incident response capability and a notification process?
5. **Physical security**: Are manufacturing and development facilities appropriately secured?
6. **Personnel security**: Background checks, insider threat programme?
7. **Provenance and integrity**: Can the supplier provide documentation of component provenance and integrity verification?
8. **Certifications**: Does the supplier hold relevant certifications (ISO 27001, CMMC, SOC 2)?

---

## Roles and Responsibilities

| Role | C-SCRM Responsibilities |
|---|---|
| Chief Information Officer (CIO) | Owns enterprise C-SCRM strategy; ensures C-SCRM integration with IT governance |
| Chief Acquisition Officer | Integrates C-SCRM into procurement and contracting processes |
| Senior Accountable Official for Risk Management (SAORM) | Oversees enterprise C-SCRM risk posture; approves risk tolerance |
| C-SCRM Programme Manager | Day-to-day C-SCRM programme management; maintains supplier inventory; coordinates assessments |
| Information System Owner | Implements system-level C-SCRM requirements; maintains system component provenance |
| ISSO | Implements SR control family at system level; monitors supply chain events affecting the system |
| Contracting Officer | Incorporates C-SCRM contract clauses; enforces contractual C-SCRM requirements |
| Legal Counsel | Reviews C-SCRM contract terms; advises on enforceability |

---

## Reference Files

- `references/sr-control-family.md` — Complete SR control family with detailed implementation guidance for each control
- `references/supplier-assessment.md` — Supplier risk tiering, assessment questionnaire, contract clauses, and SBOM requirements
- `references/c-scrm-programme.md` — C-SCRM programme establishment, policy templates, plan structure, and acquisition lifecycle procedures

# NIST SP 800-39 — Three-Tier Risk Management Model

Source: NIST Special Publication 800-39, March 2011
https://doi.org/10.6028/NIST.SP.800-39

---

## Overview

NIST SP 800-39 organises information security risk management into a **three-tier hierarchy** representing the organisational, mission/business, and information system perspectives. Risk management activities flow both downward (strategy and direction) and upward (risk information and reporting).

---

## Tier 1 — Organisation View

### Purpose
Establish the governance, strategy, and culture for organisation-wide information security risk management. All decisions at Tiers 2 and 3 occur within the context and boundaries established at Tier 1.

### Primary Functions

| Function | Description | Key Artefact |
|----------|-------------|-------------|
| Risk governance | Establish accountable leadership and governance structure for risk management | Risk governance charter; risk executive designation |
| Risk strategy | Develop and maintain the organisation's risk management strategy | Risk management strategy document |
| Risk tolerance | Establish explicit risk tolerance and risk appetite | Risk tolerance statement |
| Security policy | Develop and maintain organisation-wide security policies | Information security policy framework |
| Investment alignment | Ensure security investment is proportional to risk | Security investment portfolio |
| Threat awareness | Maintain awareness of the organisation-wide threat environment | Threat assessment (organisation level) |

### Tier 1 Artefacts

| Artefact | Description |
|----------|-------------|
| Risk Executive Function | Governance body (individual or committee) accountable for enterprise risk management |
| Risk Management Strategy | Document defining how risk management is conducted across the organisation |
| Risk Tolerance Statement | Explicit statements of acceptable and unacceptable risk levels by type and dimension |
| Information Security Policy | Top-level security policy signed by organisational head |
| Mission-Critical Asset Register | Identifies the organisation's most critical information, systems, and functions |
| Organisational Risk Framing Document | Defines all context for how risk assessments and responses are conducted |

### Tier 1 Roles

| Role | Responsibility |
|------|---------------|
| Head of Organisation / Board | Ultimate accountability for risk acceptance; approves risk strategy |
| Risk Executive (Function) | Day-to-day governance of the enterprise risk programme |
| CISO / Senior Agency Information Security Officer (SAISO) | Executes security programme; reports risk status to leadership |
| Senior Agency Official for Privacy (SAOP) | Integrates privacy risk into enterprise risk |
| Legal / General Counsel | Advises on legal risk, privacy law, and regulatory obligations |

---

## Tier 2 — Mission/Business Process View

### Purpose
Translate Tier 1 risk strategy and tolerance into specific risk decisions for mission and business processes. Identify which information systems and capabilities are critical to mission success and ensure proportionate protection.

### Primary Functions

| Function | Description | Key Artefact |
|----------|-------------|-------------|
| Enterprise architecture | Define security and privacy architecture supporting all business processes | Security architecture baseline |
| Business process mapping | Map information systems to mission/business processes to understand operational dependencies | System-to-mission dependency map |
| Risk context | Apply Tier 1 risk tolerance to specific business process risk decisions | Process-level risk context documents |
| Common controls | Identify and implement controls applicable across multiple systems | Common control register and CCP assignment |
| Supply chain governance | Establish governance for acquisition risk and vendor/supplier risk management | SCRM policy; supplier risk assessment |
| Business continuity | Ensure critical processes can continue under adverse conditions | BIA; continuity plans |

### Tier 2 Artefacts

| Artefact | Description |
|----------|-------------|
| Enterprise Security Architecture | Logical and physical architecture showing security zones, data flows, and control coverage |
| System-to-Mission Mapping | Table linking each information system to the mission functions it supports |
| Business Impact Analysis (BIA) | Assessment of the impact to mission if each system or process is unavailable or compromised |
| Common Control Register | List of all common controls provided enterprise-wide with their providers |
| Supply Chain Risk Management Policy | Policy governing vendor selection, contract requirements, and supplier monitoring |
| Tier 2 Risk Assessment | Risk assessment covering mission/business processes, cross-system dependencies, and systemic risks |

### Tier 2 Roles

| Role | Responsibility |
|------|---------------|
| Mission/Business Owner | Accountable for mission outcomes; defines process requirements and risk priorities |
| Enterprise Architect | Designs and maintains security architecture |
| Common Control Provider (CCP) | Implements and maintains common/inherited controls |
| Supply Chain Risk Manager | Manages third-party and supplier risk |
| Business Continuity Manager | Plans and tests operational continuity |

---

## Tier 3 — Information System View

### Purpose
Execute system-level risk management through the NIST Risk Management Framework (SP 800-37). All Tier 3 activity occurs within the context, boundaries, and constraints established by Tiers 1 and 2.

### Primary Functions

| Function | RMF Step | Key Artefact |
|----------|----------|-------------|
| System categorisation | Categorise (Step 1) | Security category per FIPS 199 |
| Control selection and tailoring | Select (Step 2) | Tailored SSP control list |
| Control implementation | Implement (Step 3) | SSP implementation narratives |
| Control assessment | Assess (Step 4) | SAR, POA&M |
| Authorisation | Authorise (Step 5) | ATO |
| Continuous monitoring | Monitor (Step 6) | Security posture reports |

### Tier 3 Artefacts

| Artefact | Description |
|----------|-------------|
| System Security Plan (SSP) | Complete system description, boundary, and control implementation |
| Security Assessment Report (SAR) | Findings from independent control assessment |
| Plan of Action and Milestones (POA&M) | Open weaknesses with remediation plans |
| Security Categorisation Document | FIPS 199 impact determination |
| Authorisation to Operate (ATO) | Signed decision accepting residual risk |
| Security Posture Report | Ongoing monitoring output |

---

## Information Flows Between Tiers

### Top-Down (Direction and Context)
| From | To | What Flows |
|------|----|-----------|
| Tier 1 | Tier 2 | Risk management strategy; policy; risk tolerance; priorities |
| Tier 1 | Tier 3 | Enterprise-wide policies; minimum control baselines; risk framing context |
| Tier 2 | Tier 3 | Process-specific risk context; common control inheritance; architecture requirements |

### Bottom-Up (Risk Information)
| From | To | What Flows |
|------|----|-----------|
| Tier 3 | Tier 2 | System risk assessment results; control assessment findings; ATO status; incidents |
| Tier 3 | Tier 1 | Aggregated risk posture; POA&M status; security metrics |
| Tier 2 | Tier 1 | Business process risk assessments; systemic risk patterns; supply chain risks |

### Horizontal (Within-Tier Sharing)
| Within | What Is Shared |
|--------|---------------|
| Tier 1 | Organisation-wide threat intelligence; policy decisions |
| Tier 2 | Common vulnerabilities shared across processes; architecture standards |
| Tier 3 | Known vulnerabilities across similar systems; common control deficiencies |

---

## Relationship Between SP 800-39, SP 800-37, and SP 800-30

| Aspect | SP 800-39 | SP 800-37 | SP 800-30 |
|--------|-----------|-----------|-----------|
| Scope | Enterprise (all tiers) | System lifecycle (Tier 3) | Risk assessment (all tiers) |
| Focus | Governance, strategy, and programme | RMF lifecycle steps | Assessment process and methodology |
| Risk framing | Defined here | Inputs consumed from here | Frames the assessment context |
| Risk assessment | Directed from here | Step 1 (categorise), Step 4 (assess) inform | How to conduct the assessment |
| Risk response | Defined here at enterprise level | Authorisation step accepts/mitigates | Informs response selection |
| Risk monitoring | Directed from here | Step 6 (monitor) | Updates risk registers |

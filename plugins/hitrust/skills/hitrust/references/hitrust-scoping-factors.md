# HITRUST Scoping Factors Reference
## r2 Assessment Scoping, Risk Factors, Inheritance, and Control Selection

---

## Table of Contents
1. [Overview of r2 Scoping](#1-overview-of-r2-scoping)
2. [HITRUST Risk Factors](#2-hitrust-risk-factors)
3. [Scoping Questionnaire Categories](#3-scoping-questionnaire-categories)
4. [Organization Type Factors](#4-organization-type-factors)
5. [Data Volume and Sensitivity Factors](#5-data-volume-and-sensitivity-factors)
6. [Technology and Infrastructure Factors](#6-technology-and-infrastructure-factors)
7. [Regulatory and Compliance Factors](#7-regulatory-and-compliance-factors)
8. [HITRUST Inheritance Program](#8-hitrust-inheritance-program)
9. [System Scoping — What is In-Scope](#9-system-scoping--what-is-in-scope)
10. [Scoping Decisions and Documentation](#10-scoping-decisions-and-documentation)

---

## 1. Overview of r2 Scoping

The r2 (Risk-Based 2-Year) assessment is specifically designed to be risk-tailored. Unlike
the e1 and i1 assessments, which use a fixed set of controls for all organizations, the r2
assessment determines which of the 156 HITRUST CSF control specifications apply to a given
organization based on its unique risk profile.

### How Scoping Works
1. The organization and assessor complete the scoping questionnaire in MyCSF before beginning
   the assessment
2. HITRUST uses the questionnaire responses to generate the specific set of in-scope control
   requirements for that organization
3. Each risk factor activates additional control specifications relevant to that factor
4. The final in-scope control set is locked before the assessment begins

### Base Control Set
All r2 assessments begin with a base set of control specifications that apply to every
organization regardless of risk factors. These cover fundamental security practices across
all 14 control categories. The base set is non-negotiable.

### Additional Controls from Risk Factors
Organizations with additional risk factors (e.g., internet-facing systems, cloud infrastructure,
large PHI volumes, specific regulatory requirements) will have additional control specifications
added to their base set.

---

## 2. HITRUST Risk Factors

HITRUST organises its risk factors into several groups. Each risk factor corresponds to a set
of additional control specifications that become required when that factor is present.

Risk factors operate cumulatively — if multiple factors apply, all their associated
controls are added to the in-scope set, with no duplication.

### Risk Factor Categories

| Factor Category | Description | Controls Impact |
|----------------|-------------|-----------------|
| Organization type | CE, BA, sub-BA, payer, provider, etc. | Activates HIPAA-specific controls |
| Record volume | Number of individual records in the system | Higher volumes add proportionally more controls |
| Business programmes | Services offered (billing, telecoms, email, etc.) | Service-specific controls |
| Regulatory requirements | Applicable regulations beyond HIPAA | Activates regulation-specific controls |
| Technology infrastructure | Cloud, mobile, web apps, remote access, BYOD | Technology-specific controls |
| Data sensitivity | Types of data (ePHI, PII, payment data, financial) | Data-type-specific controls |
| Geographic operations | Multi-state, international | Jurisdiction-specific controls |

---

## 3. Scoping Questionnaire Categories

The MyCSF scoping questionnaire covers the following areas. Organizations must complete all
sections accurately — scoping responses are reviewed by the assessor and by HITRUST.

### Section A — Organization Profile
- Organization type (healthcare provider, health plan, healthcare clearinghouse, business
  associate, sub-business associate, non-healthcare)
- Primary business activities
- Number of employees
- Number of covered locations / facilities

### Section B — Data Holdings
- Types of personally identifiable information (PII) held
- Whether ePHI is stored, processed, or transmitted
- Whether payment card data (CHD/SAD) is stored, processed, or transmitted
- Number of individuals whose records are held
- Physical vs. electronic records breakdown

### Section C — Business Activities / Services
- Whether the organization provides billing services, claims processing, revenue cycle
- Whether the organization operates a call centre
- Whether the organization provides telemedicine or telehealth services
- Whether the organization operates a pharmacy or conducts pharmaceutical research
- Whether the organization provides laboratory services

### Section D — Technology Infrastructure
- Whether the organization uses public cloud infrastructure (IaaS, PaaS)
- Whether the organization uses SaaS applications for processing of sensitive data
- Whether the organization has internet-facing applications or portals
- Whether employees use mobile devices (corporate-issued or BYOD) to access sensitive data
- Whether remote access to internal systems is provided to employees or third parties
- Whether the organization uses point-of-sale (POS) systems
- Whether wireless networks are in use

### Section E — Regulatory Requirements
- HIPAA / HITECH applicability
- PCI DSS applicability
- CMS ARS applicability
- State-specific requirements (e.g., California CMIA, Texas HIPAA equivalent)
- GDPR or other international privacy law applicability
- FTC oversight
- FERPA (educational records)
- 42 CFR Part 2 (substance use disorder records)

### Section F — Third Parties and Vendors
- Whether the organization relies on third-party service providers with access to sensitive data
- Number of business associates or subcontractors with access to ePHI
- Whether third parties have network access or remote access to internal systems

---

## 4. Organization Type Factors

The organization type is one of the most significant scoping factors. Different organization
types have different regulatory obligations and risk profiles.

| Organization Type | HITRUST Classification | Regulatory Context |
|------------------|----------------------|-------------------|
| Healthcare Provider | Covered Entity (CE) | HIPAA Privacy Rule, Security Rule, Breach Notification Rule |
| Health Plan / Payer | Covered Entity (CE) | HIPAA Privacy Rule, Security Rule, Breach Notification Rule |
| Healthcare Clearinghouse | Covered Entity (CE) | HIPAA Privacy Rule, Security Rule |
| Business Associate (direct) | Business Associate (BA) | HIPAA Security Rule in full; Privacy Rule via BAA |
| Sub-Business Associate | Sub-BA | HIPAA obligations flow through BA agreement |
| Non-Healthcare (pursuing HITRUST) | Other | Framework harmonisation and voluntary adoption |

### Healthcare Provider
- All Privacy Rule controls relevant (Category 13 — Privacy Practices in full)
- Patient rights obligations (access, amendment, accounting of disclosures, NPP)
- Minimum necessary standard applies to all disclosures

### Health Plan / Payer
- Full Privacy Rule and Security Rule applicability
- Marketing and fundraising restrictions
- Employer plan exceptions may apply

### Business Associate
- Security Rule applies in full
- Portions of the Privacy Rule apply via BAA terms
- Must flow down obligations to sub-BAs
- Must report breaches and security incidents to the Covered Entity within contract terms
  (typically 60 days; HITRUST recommends and best practice is 30 days or sooner)

---

## 5. Data Volume and Sensitivity Factors

### Record Volume Tiers

HITRUST uses approximate record volume thresholds to calibrate the control scope. Higher
volumes generally correspond to more prescriptive control requirements.

| Volume Tier | Approximate Range | Impact on Controls |
|------------|-------------------|--------------------|
| Minimal | Fewer than 25,000 individuals | Base control set |
| Small | 25,000 – 100,000 individuals | Incremental controls for monitoring and access |
| Medium | 100,000 – 500,000 individuals | Additional controls for data protection and third-party management |
| Large | 500,000 – 2,000,000 individuals | Broader controls across all categories |
| Very Large | More than 2,000,000 individuals | Maximum scope; all relevant controls activated |

**Note:** Record volume thresholds in the actual HITRUST scoping questionnaire should be
confirmed in MyCSF. HITRUST may update these thresholds between framework versions.

### Sensitive Data Types

The presence of specific data types activates corresponding control requirements:

| Data Type | Activated Control Areas |
|-----------|------------------------|
| ePHI (electronic Protected Health Information) | Category 13 (Privacy); strengthened Category 01 and 09 controls |
| PII (Personally Identifiable Information) | Category 06.d; privacy breach procedures |
| Payment Card Data (PAN / SAD) | PCI DSS-aligned controls in Categories 01, 09, 10 |
| Financial account information | Additional access and transfer controls |
| Substance use disorder records (42 CFR Part 2) | Heightened prohibition on re-disclosure |
| Psychotherapy notes | Additional access restriction controls |
| Genetic information (GINA) | Additional privacy protections |
| Records of minors | Parental access and consent controls |

---

## 6. Technology and Infrastructure Factors

Technology risk factors add specific technical controls to the r2 scope.

### Cloud Infrastructure (IaaS/PaaS)

If the organization uses public cloud infrastructure (e.g., AWS, Microsoft Azure, Google Cloud)
to store, process, or transmit sensitive data, the following additional controls are commonly
activated:

- Cloud configuration management and hardening (Category 09)
- Cloud-specific access control (multi-factor authentication, IAM policies) (Category 01)
- Virtual network boundary protection (Category 01.i)
- Cloud asset inventory (Category 07)
- Key management for cloud encryption (Category 10.g)
- Data residency and sovereignty considerations (Category 06)
- Shared responsibility clarity and documentation

**Inheritance consideration:** If a cloud provider (e.g., AWS) holds a HITRUST certification
covering the infrastructure services used, the organization may be able to inherit applicable
controls. See Section 8 — Inheritance.

### SaaS Applications

If the organization uses SaaS applications to process sensitive data:
- Vendor security review requirements (Category 05.k)
- BAA or equivalent agreement requirements (if SaaS vendor processes ePHI)
- Third-party access and connection controls (Category 01.q)
- SaaS configuration management

### Internet-Facing Applications and Web Portals

If the organization operates internet-facing systems (patient portals, web apps, APIs):
- Web application security controls (Category 10.b — input validation, OWASP Top 10 mitigations)
- External vulnerability scanning (Category 06.g, Category 10.h)
- WAF or equivalent controls for internet-facing applications
- API security controls (authentication, authorisation, rate limiting)
- Annual penetration testing requirement (minimum)

### Mobile Devices

If employees or contractors use mobile devices (corporate-issued or BYOD) to access
sensitive data:
- Mobile Device Management (MDM) requirements (Category 01.p)
- Remote wipe capability
- Mobile device encryption
- BYOD policy and acceptable use
- Application controls preventing data leakage from mobile applications

### Remote Access

If remote access to internal systems is provided:
- VPN or equivalent encrypted remote access (Category 01.q)
- Multi-factor authentication for remote access mandatory
- Remote session monitoring and logging
- Remote access usage policy

### Wireless Networks

If wireless networks are in use in locations where sensitive data is accessed:
- Wireless encryption (minimum WPA2 / WPA3) (Category 01.p)
- Rogue access point detection
- Separation of guest and corporate wireless networks
- Wireless access logging

---

## 7. Regulatory and Compliance Factors

Each regulatory requirement that applies to the organization may activate additional control
specifications or strengthen existing requirements.

### HIPAA / HITECH
- Activates all relevant HIPAA Security Rule controls across Categories 01, 07, 09, 10
- Activates all Privacy Practices controls (Category 13)
- Activates Breach Notification Rule requirements in Category 11
- HITECH increases penalties and adds Meaningful Use requirements

### PCI DSS
- If the organization stores, processes, or transmits payment card data
- Activates additional access control, encryption, and monitoring requirements
- Requires quarterly external vulnerability scans
- Requires annual penetration testing
- Requires network segmentation between PCI and non-PCI environments

### CMS Acceptable Risk Safeguards (ARS)
- Applies to organizations processing Medicare, Medicaid, or other CMS data
- Activates NIST SP 800-53 alignment controls beyond standard HIPAA requirements
- Typically adds controls in Categories 01, 03, 06, and 09

### 42 CFR Part 2 (Substance Use Disorder Records)
- More restrictive than HIPAA for records relating to substance use disorder treatment
- Prohibits most re-disclosures without patient consent
- Activates heightened access restriction and disclosure controls

### State Privacy Laws
- Various states (e.g., California, New York, Texas) have enacted health privacy laws that
  may be more stringent than HIPAA in certain respects
- California Confidentiality of Medical Information Act (CMIA) may activate additional
  controls beyond HIPAA

---

## 8. HITRUST Inheritance Program

### What is Inheritance?
HITRUST inheritance allows an organization (the "Inheritor") to inherit responsibility for
certain HITRUST controls from a third-party service provider (the "Inheritee") that is
currently HITRUST certified. This recognizes that in cloud and outsourced service arrangements,
the service provider bears responsibility for some controls.

### How Inheritance Works
1. The Inheritee must hold a current HITRUST certification letter that covers the controls
   being inherited
2. The Inheritee provides their HITRUST certification letter to the Inheritor
3. The Inheritor documents the inherited controls in MyCSF and links the certification letter
   as evidence
4. The assessor validates the inheritance relationship:
   - Confirms the Inheritee has a valid, unexpired certification
   - Confirms the certification scope covers the controls being inherited
   - Confirms the contractual relationship (e.g., BAA or service agreement) is in place
5. Inherited controls receive credit toward the Inheritor's assessment

### Inheritance Limitations
- Inheritance is only available for controls that the service provider is operationally
  responsible for
- Controls that are the customer's responsibility cannot be inherited (e.g., customer's
  own access control policy)
- Partial inheritance is possible where the provider controls some but not all aspects
  of a requirement
- The Inheritor remains responsible for ensuring the service agreement addresses security
  obligations

### Common Inheritance Scenarios

| Inheritee | What Can Typically Be Inherited |
|-----------|--------------------------------|
| AWS (if HITRUST certified for scope) | Physical security (Category 08), data centre environmental controls (Category 08.d-h), hardware maintenance (08.j) |
| Microsoft Azure (if HITRUST certified) | Physical security, network infrastructure controls, core IaaS controls |
| Epic (EHR vendor, if certified) | Application-level controls specific to Epic's SaaS scope |
| Hosting / colocation provider (if certified) | Data centre physical security, power, HVAC |

### Shared Responsibility Matrix Format

When documenting inheritance:

```
| Control ID | Control Title | Responsibility | Inheritance Source | Certificate ID | Expiry |
|-----------|--------------|---------------|-------------------|---------------|--------|
| 08.a.1    | Physical Security Perimeter | Fully Inherited | AWS-HITRUST | [Cert #] | [Date] |
| 08.b.1    | Physical Entry Controls | Fully Inherited | AWS-HITRUST | [Cert #] | [Date] |
| 01.a.1    | Access Control Policy | Customer | N/A | N/A | N/A |
| 09.l.1    | Information Backup | Shared | AWS (infrastructure); Customer (data backup config) | [Cert #] | [Date] |
```

---

## 9. System Scoping — What is In-Scope

### In-Scope System Definition

For a HITRUST assessment, the "system" or "environment" in scope must be clearly defined.
This is analogous to the "system boundary" in other frameworks (e.g., FedRAMP System
Security Plan boundary).

**Systems that are typically in scope:**
- Systems that store, process, or transmit ePHI or other sensitive data being assessed
- Systems that directly support, protect, or manage in-scope systems (security tools,
  identity providers, network infrastructure connecting in-scope systems)
- Third-party systems with direct access to in-scope data

**Systems that may be out of scope (with documented justification):**
- Systems with no access to or impact on the sensitive data environment
- Fully isolated business units or subsidiaries with separate data environments
- Systems for which controls are fully inherited from a certified third party

### Scope Documentation
The scope of the assessment must be documented and agreed upon between the organization
and the assessor before the assessment begins. Scope documentation must include:
- Description of the system or environment
- Boundaries (logical and physical)
- Data types in scope
- Locations in scope
- Key systems and applications
- Third-party components

---

## 10. Scoping Decisions and Documentation

### Common Scoping Mistakes to Avoid

| Mistake | Risk | Mitigation |
|---------|------|-----------|
| Excluding systems that have direct connectivity to in-scope data | Assessor may expand scope; controls gaps may exist | Map all data flows before finalizing scope |
| Over-scoping to include systems with no access to sensitive data | Increases cost and effort unnecessarily | Document scope exclusions with rationale |
| Inaccurately answering scoping questionnaire | HITRUST may reject or question the assessment | Complete questionnaire with the assessor; document rationale |
| Not considering cloud infrastructure | Cloud controls may be absent | Inventory all cloud services in use before scoping |
| Ignoring sub-processors | Third-party chain creates unaccounted risk | Map all third parties with access to in-scope data |

### Scope Change During Assessment
If the scope must change during the assessment (e.g., a new system is identified as in-scope):
- Notify the assessor immediately
- Assessor and organization must agree on how to handle the change
- Significant scope changes may require restarting certain assessment activities
- HITRUST should be informed of material scope changes

### Scoping for Inherited Controls
Controls that are fully inherited do not need to be actively assessed by the organization, but:
- The inheritance must be documented in MyCSF
- The certification letter from the Inheritee must be available and current
- The assessor must validate the inheritance
- Missing or expired inheritance documentation will result in the controls falling to
  the organization's own assessment scope

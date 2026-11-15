---
name: eu-cra
description: "Expert EU Cyber Resilience Act (CRA) advisor for Regulation (EU) 2024/2847 - mandatory cybersecurity and vulnerability handling requirements for all products with digital elements (PDEs) sold in the EU. Use this skill for gap analysis, product classification (Default / Class I / Class II), conformity assessment route selection, CE marking, SBOM requirements, vulnerability and incident reporting to ENISA/CSIRTs, support period obligations, and manufacturer/importer/distributor duties. Trigger for EU CRA, Cyber Resilience Act, PDE compliance, Annex I requirements, SBOM EU, CE marking cybersecurity, or connected product security EU."
---

# EU Cyber Resilience Act (CRA) Skill

> **Last verified:** 2026-11-15

## Overview

You are an expert advisor on **Regulation (EU) 2024/2847 - the EU Cyber Resilience Act (CRA)**, published in the Official Journal on 20 November 2024. The CRA entered into force on **10 December 2024** and applies in a staggered timeline:

| Milestone | Date |
|---|---|
| Entry into force | 10 December 2024 |
| Vulnerability & incident reporting obligations | **11 September 2026 - NOW IN FORCE** |
| Chapter IV (Arts. 35–51, notified bodies) applies | 11 June 2026 |
| Art. 35(2) target for Member States to strive for sufficient notified bodies | 11 December 2026 |
| **Full application (all obligations)** | **11 December 2027** |

The CRA applies to all **Products with Digital Elements (PDEs)** - any hardware or software with network connectivity - sold or made available in the EU. It covers manufacturers, importers, and distributors in the supply chain.

**Read the reference files before drafting detailed guidance:**
- `references/essential-requirements.md` - Annex I essential requirements, product categories, support period, SBOM, vulnerability handling, reporting obligations
- `references/conformity-assessment.md` - conformity assessment routes by product class, CE marking process, DoC, notified bodies, market surveillance, penalties

---

## Core Concepts

### Scope - What is a Product with Digital Elements (PDE)?

A PDE is any **software or hardware product and its remote data processing solutions** that has at least one network interface enabling data communication. This includes:

- IoT devices (smart home, industrial sensors, wearables)
- Network equipment (routers, switches, firewalls, modems)
- Software products (operating systems, applications, games - including commercial off-the-shelf software)
- Mobile applications, cloud-connected products
- Virtualised products, containers

**Exclusions:** Medical devices (MDR/IVDR), aviation products (EASA), automotive (type-approval), marine equipment, military/national security products, products developed for classified information. Open-source software not placed on the market commercially is generally excluded.

### Product Classification

| Class | Description | Examples | Conformity Route |
|---|---|---|---|
| **Default** | All PDEs not listed in Annex III or Annex IV | Generic IoT devices, general software, games, simple smart devices | Self-assessment (Module A) |
| **Class I** (Annex III - important products) | 19 categories | Identity management systems and PAM software, password managers, standalone and embedded browsers, anti-malware, VPN products, network management systems, SIEM, boot managers, PKI and digital certificate software, network interfaces, operating systems, routers/modems/switches, microprocessors and microcontrollers with security functionalities, ASICs/FPGAs with security functionalities, smart home virtual assistants, smart home security products, connected toys with interaction features, personal wearables with health monitoring | Self-assessment OR third-party (manufacturer's choice) |
| **Class II** (Annex III - important products) | 4 categories | Hypervisors and container runtime systems; firewalls, intrusion detection and prevention systems; tamper-resistant microprocessors; tamper-resistant microcontrollers | **Mandatory third-party** (Notified Body) |
| **Critical** (Annex IV - critical products) | 3 categories | Hardware devices with security boxes; smart meter gateways; smartcards or similar devices including secure elements | May be made subject to **mandatory EU cybersecurity certification** |

### Roles and Responsibilities

| Role | Definition | Key Obligations |
|---|---|---|
| **Manufacturer** | Designs, develops, produces, or has PDEs designed/developed/produced under their name | All Annex I requirements; vulnerability handling; incident reporting; DoC; CE marking; 10-year record-keeping |
| **Authorised Representative** | EU-based entity acting for a non-EU manufacturer | Holds DoC and technical documentation for authorities |
| **Importer** | Brings PDEs from outside the EU into the EU market | Verify manufacturer compliance; affix own name/address; notify authorities of risk; 10-year records |
| **Distributor** | Makes PDEs available on EU market other than manufacturer/importer | Verify CE marking and DoC; not knowingly distribute non-compliant products |
| **Open-Source Software Steward** | Entity that supports open-source software placed on the market commercially | Light-touch obligations; cybersecurity policy; cooperation with authorities |

---

## Skill Workflows

### Workflow 1 - Product Classification and Scope Assessment

**When to use:** Determining whether a product is in scope and which class it falls into.

**Steps:**
1. Identify whether the product has at least one network interface (direct or indirect connectivity).
2. Check exclusions (medical devices, aviation, automotive, military, etc.).
3. Check Annex III (important products: Class I, 19 categories; Class II, 4 categories) - does the product fit any?
4. Check Annex IV (critical products, 3 categories) - does the product fit any?
5. If neither Annex applies, the product is Default class.
6. Identify the organisation's role: manufacturer, importer, or distributor.
7. If a non-EU manufacturer, determine whether an EU authorised representative is required.

**Output format:**
```
## CRA Scope and Classification - [Product Name]
### Scope Determination: In scope / Excluded (reason)
### Product Class: Default / Class I / Class II
### Applicable Annex: N/A / Annex III item X / Annex IV item X
### Organisation Role: Manufacturer / Importer / Distributor
### Conformity Assessment Route: Self-assessment (Module A) / Third-party (Notified Body)
### Key Obligations Summary
```

### Workflow 2 - Annex I Essential Requirements Gap Analysis

**When to use:** Assessing a product or development process against CRA mandatory requirements.

**Annex I - Part I: Security Properties (Products must be designed/developed/produced to):**
1. No known exploitable vulnerabilities at time of placing on market
2. Secure by default configuration - minimal attack surface, unnecessary functions disabled
3. Protection against unauthorised access - appropriate authentication, access control
4. Confidentiality - protection of data at rest and in transit (encryption)
5. Integrity - protection against manipulation; signed software updates
6. Minimal data processing - data minimisation and privacy by design
7. Protection of availability - resilience against denial of service
8. Limited negative impact on other devices/networks
9. Exploit mitigation mechanisms
10. Security-relevant information disclosed to users

**Annex I - Part II: Vulnerability Handling (exactly 8 requirements; manufacturers must):**
1. Identify and document vulnerabilities and components, including a Software Bill of Materials (SBOM)
2. Remediate vulnerabilities without delay, including through free security updates
3. Apply effective and regular tests and reviews of the product's security
4. Publicly disclose information about fixed vulnerabilities once updates are available
5. Put in place and enforce a coordinated vulnerability disclosure policy
6. Facilitate the sharing of information about potential vulnerabilities (including a point of contact)
7. Provide mechanisms to securely distribute updates
8. Disseminate free, timely security updates

**Note:** The 24h/72h reporting of actively exploited vulnerabilities and severe
incidents is an **Article 14** obligation (24h early warning, 72h notification,
final report), not an Annex I Part II item. Support-period and end-of-life duties
sit in **Article 13 and Annex II**.

**Steps for gap analysis:**
1. Map current product security controls against each Part I requirement.
2. Assess vulnerability management programme against each Part II requirement.
3. Confirm existence of VDP and public point of contact.
4. Confirm SBOM capability (at minimum, top-level open-source components).
5. Determine support period commitment.
6. Identify gaps, assign risk ratings, and propose remediation timeline.

### Workflow 3 - Conformity Assessment and CE Marking

**When to use:** Preparing for market placement - selecting the right conformity route and preparing documentation.

**Read `references/conformity-assessment.md` for full details.**

**High-level steps:**
1. Confirm product class (Default → self-assessment; Class I → self-assessment or third-party; Class II → mandatory Notified Body).
2. Prepare technical documentation (TD) - required elements per Annex VII.
3. Conduct conformity assessment against Annex I requirements.
4. For Notified Body routes: select an accredited NB, submit application, complete assessment.
5. Draft and sign the EU Declaration of Conformity (DoC) - required elements per Annex V.
6. Affix CE marking - visible, legible, indelible on the product or packaging.
7. Retain TD and DoC for 10 years after placing on market.

**Technical Documentation (Annex VII) must include:**
- General product description and intended use
- Design and development documentation (architecture diagrams, threat model)
- Security risk assessment
- Cybersecurity measures implemented
- Test reports and evidence of conformity
- SBOM (at minimum, top-level dependencies)
- Vulnerability handling policies and procedures

### Workflow 4 - Vulnerability Handling Programme

**When to use:** Building or reviewing a vulnerability management and disclosure programme.

**Programme elements:**
1. **Internal vulnerability tracking** - inventory of components and dependencies; process to identify new CVEs affecting products.
2. **Coordinated Vulnerability Disclosure (CVD) policy** - published VDP; named point of contact; acknowledgement timeline; responsible disclosure expectations.
3. **Security update process** - free-of-charge security updates; signed updates; update mechanism that cannot be disabled by users.
4. **SBOM management** - machine-readable SBOM (SPDX, CycloneDX formats recommended) for at least top-level open-source components; kept current.
5. **Art. 14 reporting pipeline (LIVE since September 11, 2026)** - operational process to file via the **ENISA Single Reporting Platform**: 24-hour early warning, 72-hour notification, and final report (14 days after a corrective measure is available for exploited vulnerabilities; 1 month after the 72-hour notice for severe incidents); notify affected users.
6. **Support period governance** - define and commit to the support period (minimum 5 years for most products); publish end-of-life notice at least 1 year before support ends.
7. **Third-party component management** - track vulnerabilities in integrated open-source and third-party components; request SBOM from upstream suppliers.

**Output:** Provide a vulnerability handling programme gap assessment and a recommended programme design.

### Workflow 5 - Support Period and End-of-Life Obligations

**When to use:** Defining support commitments and planning product end-of-life.

**Support period rules:**
- Must be at least **5 years**, or the expected product lifetime if shorter
- Manufacturers must clearly communicate the support period to users
- Security updates must be free-of-charge and delivered promptly throughout the support period
- Updates must not degrade product security or functionality
- At end of support: notify users at least **1 year in advance**; if possible, provide a migration path or final cumulative security update

**When a separate support period from a software component applies:** Manufacturers integrating third-party software components must ensure the support period of their product does not exceed the security update support provided by upstream.

---

## Reporting Is LIVE - Art. 14 via the ENISA SRP (state in every reporting answer)

**Since September 11, 2026** manufacturers must report **actively exploited vulnerabilities** and **severe incidents** affecting products with digital elements - including products already on the market before December 2027 (Art. 69(3)). The clock is **awareness-based** (no retroactive duty for pre-Sept-11 awareness).

| Stage | Exploited vulnerability | Severe incident (Art. 14(5): impact on ability to protect sensitive data/functions, or malicious code introduced/executed) |
|---|---|---|
| Early warning | **24h** from awareness | **24h** |
| Notification + initial assessment | **72h** | **72h** |
| Final report | **≤14 days after a corrective/mitigating measure is available** | **≤1 month after the 72h notification** |

**The Single Reporting Platform (SRP)** launched September 11, 2026 (ENISA, Art. 16(1); portal.cra-srp.enisa.europa.eu). Filing workflow: an **Assigned Representative** registers with an EU Login account (MFA required), selects the **CSIRT Designated as Coordinator** of the Member State of main establishment (Art. 14(7); non-EU cascade: authorised representative → importer → distributor → most users), accepts the legal agreement, and becomes Primary AR (up to 20 Secondary ARs). CSIRT validation runs in parallel - up to 20 notifications may be filed before verification completes; ENISA advises registering **when a notification is needed**, not pre-emptively. Notifications route to the CDaC and simultaneously to ENISA (unless Particular Exceptional Circumstances, Art. 16(2); dissemination-delay rules in Delegated Regulation (EU) 2026/881). **Fallback**: if the SRP is temporarily unavailable, contact the designated CSIRT directly for urgent matters - but the notification must still be filed via the SRP once restored. Launch limitations: English-only, no API. Companion guidance: Commission Communication C(2026) 5252 (July 27, 2026) and the Commission CRA FAQs. **Open-source software stewards** report from December 11, 2027 (Arts. 24(3)/71(2)); the CRA's main obligations (essential requirements, CE marking) also apply from December 11, 2027.

## Penalties Quick Reference (Article 64)

| Violation | Maximum Penalty |
|---|---|
| Non-compliance with Annex I essential requirements | €15 million or **2.5% of global annual turnover** (higher of the two) |
| Non-compliance with the other obligations listed in Art. 64(2) | €10 million or **2% of global annual turnover** |
| Incorrect, incomplete, or misleading information to authorities | €5 million or **1% of global annual turnover** |
| SMEs and micro-enterprises | Historical turnover figure used; proportionality applies |

---

## Key Dates Summary

| Obligation | Applies From |
|---|---|
| Vulnerability/incident reporting to ENISA + CSIRTs | **11 September 2026 - in force; SRP live** |
| Chapter IV (Arts. 35–51, notified bodies) | 11 June 2026 (11 December 2026 is only the Art. 35(2) target for Member States to strive for sufficient notified bodies) |
| All manufacturer, importer, distributor obligations | **11 December 2027** |
| Products already on market (transitional) | If unchanged, have until 11 December 2027 to comply |

---

## Relationship to Other EU Regulations

- **NIS2 Directive:** NIS2 applies to operators of essential/important services; CRA applies to product manufacturers. A product could be subject to CRA while its manufacturer/operator is also under NIS2. No conflict - they are complementary.
- **GDPR:** CRA's data minimisation and security requirements under Annex I align with GDPR Article 25 (privacy by design) and Article 32 (security of processing). Products must implement both.
- **EU AI Act:** AI systems embedded in hardware PDEs must comply with both the AI Act and CRA. The AI Act takes precedence for AI-specific requirements; CRA covers the hardware/connectivity security layer.
- **RED (Radio Equipment Directive 2014/53/EU):** Products subject to RED's cybersecurity delegated acts (Article 3(3)(d)(e)(f)) that are also PDEs - manufacturers may use RED compliance to demonstrate partial CRA conformity. ENISA and the Commission are expected to publish guidance on this overlap.
- **MDR/IVDR:** Medical devices are excluded from CRA. However, software components embedded in medical devices that are marketed separately may be in scope.

---

> *This skill provides general compliance information, not legal advice. Verify current requirements against official sources; consult qualified counsel or an accredited assessor for decisions.*

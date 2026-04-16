# CMMC 2.0 Scoping Guidance
## Source: CMMC 2.0 Scoping Guidance Documents — DoD CIO (December 2021, updated 2024)

---

## Overview

Scoping is the process of identifying which systems, components, and people are included
in the CMMC assessment boundary. Correct scoping is critical: too broad wastes resources,
too narrow creates compliance gaps.

**Official source:** CMMC Level 2 Scoping Guidance and CMMC Level 3 Scoping Guidance
published by the Office of the DoD Chief Information Officer (DoD CIO).

---

## Data Types That Drive Scope

### Federal Contract Information (FCI)

**Definition (FAR 4.1901):**
Information, not intended for public release, that is provided by or generated for the
Government under a contract to develop or deliver a product or service to the Government.

FCI **does NOT include:**
- Information provided by the Government to the public (public websites, reports)
- Simple transactional information (payments, schedules, administrative correspondence)

**CMMC implication:** FCI presence requires minimum Level 1.

### Controlled Unclassified Information (CUI)

**Definition:** Information the Government creates or possesses (or an entity creates or
possesses for or on behalf of the Government) that a law, regulation, or Government-wide
policy requires or permits handling using safeguarding or dissemination controls.

**CUI Registry:** Published by the National Archives and Records Administration (NARA) at
https://www.archives.gov/cui

**Common DoD CUI Categories:**
- Controlled Technical Information (CTI)
- Export Controlled (ITAR, EAR)
- Proprietary Business Information
- Critical Infrastructure Information
- DoD-specific CUI categories per DoD Instruction 5200.48

**CUI markings:** Documents containing CUI are marked "CUI" with applicable CUI category
indicator, handling instructions, and authority block per NARA CUI Marking Handbook.

**CMMC implication:** CUI presence requires Level 2 minimum; Level 3 if designated by DoD.

---

## Asset Categories

The CMMC Program defines six asset categories for scoping purposes. Categorization
determines which practices apply to each asset.

### 1. CUI Assets

**Definition:** These assets process, store, or transmit CUI.

**Examples:**
- Workstations running applications that access CUI repositories
- File servers storing technical data, drawings, specifications marked CUI
- Email servers where CUI is communicated
- Databases containing program plans or bids with CUI
- Cloud storage (SharePoint, OneDrive, S3 buckets) holding CUI documents
- Printers that print documents containing CUI

**Scope:** ALL 110 Level 2 practices (or 134 Level 3 practices) apply.

**Key test:** "Does this asset process, store, OR transmit CUI?"

---

### 2. Security Protection Assets (SPAs)

**Definition:** Assets that provide security functions to the CUI environment, protecting
CUI Assets from unauthorized access or attack — even if they do not directly touch CUI.

**Examples:**
- Firewalls and routers that protect the CUI network segment
- Identity providers (Active Directory, LDAP, Azure AD) authenticating CUI users
- SIEM (Security Information and Event Management) systems monitoring CUI environment
- Vulnerability scanners scanning CUI systems
- PAM (Privileged Access Management) systems managing privileged access to CUI
- Endpoint Detection and Response (EDR) platforms on CUI assets
- Multi-factor authentication (MFA) systems
- Backup systems protecting CUI

**Scope:** ALL applicable CMMC practices apply. SPAs are fully in-scope because
if compromised, they defeat the protection of CUI assets.

---

### 3. Contractor Risk Managed Assets (CRMAs)

**Definition:** Assets that can reach (i.e., have network connectivity to) CUI or Security
Protection Assets but do **not** directly process, store, or transmit CUI.

**Examples:**
- IT administration workstations that can reach the CUI network but are not used for CUI work
- Jump hosts used for network management (if not handling CUI)
- Management servers for hypervisors hosting CUI VMs
- Monitoring systems with read-only access to CUI network infrastructure logs

**Scope:** The organization must document and assess the risk these assets pose to CUI
and SPAs, and implement controls commensurate with that risk. Not all 110 practices
automatically apply — but the organization must document which apply and justify any
exclusions.

**Key distinction from CUI Assets:** The critical test is whether the asset CAN access
CUI or security controls, not whether it IS USED for CUI. If it can reach CUI, it is
a CRMA at minimum.

---

### 4. Specialized Assets

**Definition:** Assets that are used in the CUI environment but which present unique
challenges for implementation of standard CMMC practices. These require specific
risk-based treatment.

**Sub-categories:**

| Sub-category | Description | Examples |
|-------------|-------------|---------|
| Government Furnished Equipment (GFE) | Equipment provided by the Government | Government-issued laptops, hardware provided on contract |
| Operational Technology (OT) / Industrial Control Systems (ICS) | Equipment in manufacturing or process control | CNC machines, PLCs, SCADA systems |
| Internet of Things (IoT) | Networked devices with limited management capability | Smart sensors, building management systems |
| Test Equipment | Devices used for testing that interact with CUI | Oscilloscopes connected to test workstations, spectrum analyzers |
| Restricted Information Systems | Legacy or specialized systems with operational constraints | Legacy mainframes, air-gapped systems |

**Scope:** CMMC practices apply to the extent they can be implemented. Where practices
cannot be applied, the organization must document the risk, implement compensating controls,
and include in the SSP. For GFE: responsibility for compliance lies with the Government
component that owns the equipment.

---

### 5. Out-of-Scope Assets

**Definition:** Assets that do **not** process, store, or transmit CUI AND have **no
connectivity** (network or physical) to CUI assets or SPAs.

**Conditions for out-of-scope classification:**
1. The asset does not touch CUI (not process, store, transmit)
2. The asset cannot reach CUI assets or SPAs via any network path
3. The asset is not used in the maintenance or security of CUI systems
4. The isolation is documented, verified, and maintained

**Examples (when properly isolated):**
- HR or accounting systems on a separate, isolated network with no path to CUI
- Guest Wi-Fi networks with no path to CUI environment
- Employee personal devices never connected to CUI systems and not used for CUI work

**Important:** If there is ANY network path — even through DMZ or VPN — the asset is NOT
out-of-scope. Air-gap requirement is strict.

---

### 6. External Service Providers (ESPs)

**Definition:** Companies or cloud services that process, store, or transmit CUI on behalf
of the contractor, or provide security services to the CUI environment.

**Examples:**
- Cloud service providers (AWS, Azure, Google Cloud) hosting CUI workloads
- Managed Security Service Providers (MSSPs) monitoring CUI systems
- Co-location data centers where CUI servers are housed
- SaaS platforms where CUI is uploaded (e.g., document management, collaboration tools)
- IT support vendors with access to CUI systems (MSPs)

**Scope requirements for ESPs:**

| ESP Type | Requirement |
|---------|------------|
| Cloud Service Provider (IaaS/PaaS/SaaS) storing/processing CUI | Must be FedRAMP Authorized at Moderate baseline OR assessed via CMMC/equivalent |
| MSSP providing security services to CUI environment | Must be CMMC certified to at least Level 2 (or demonstrate equivalent) |
| Co-location / data center | Physical controls must be documented; contractor retains responsibility for logical controls |
| IT support vendors (MSPs) | Must meet CMMC requirements commensurate with their access level |

**Flow-down clause:** Prime contractors must include DFARS 252.204-7021 in subcontracts
where subcontractors will process, store, or transmit CUI or provide security protection
services. Subcontractors must be CMMC certified to the same level as the prime for the
work they perform.

---

## Scoping Process — Step-by-Step

### Step 1: Identify CUI

- Review contracts for CUI requirements and markings
- Inventory all CUI received, generated, or stored during performance
- Assign CUI categories per NARA CUI Registry
- Document where CUI flows (data flow diagram)

### Step 2: Map CUI Asset Locations

For each CUI category, identify all locations:
- File servers and storage systems
- Endpoints (workstations, laptops) used to access CUI
- Applications and databases
- Email systems
- Cloud services
- Removable media
- Paper/physical records (out of CMMC scope, but needed for full picture)

### Step 3: Identify SPAs

For each CUI Asset, identify what provides security protection:
- Authentication systems
- Network security controls (firewalls, IDS/IPS)
- Logging and monitoring systems
- EDR/AV platforms
- Backup systems

### Step 4: Identify CRMAs

Map all systems that have network connectivity to CUI Assets or SPAs but do not directly
process CUI. Document the purpose and level of access for each CRMA.

### Step 5: Identify Specialized Assets

List OT/ICS, IoT, GFE, test equipment, and restricted systems within or near the CUI environment.

### Step 6: Identify ESPs

List all external services that touch the CUI environment, document their authorization status,
and determine flow-down obligations.

### Step 7: Isolate Out-of-Scope Systems

Verify that systems claimed as out-of-scope have no network path to CUI assets or SPAs.
Document the isolation controls.

### Step 8: Document in SSP

The System Security Plan must include:
- Network boundary diagram showing all asset categories
- Data flow diagram showing CUI movement
- Asset inventory categorized by scope type
- Explanation of out-of-scope determinations
- ESP list with authorization status

---

## Network Segmentation Recommendations for Scope Reduction

Reducing the CMMC scope reduces assessment cost and complexity. Common strategies:

| Strategy | How It Reduces Scope |
|---------|---------------------|
| VLAN isolation of CUI workstations | Keeps CUI on separate network segment; limits CRMA expansion |
| Jump server for CUI administration | Limits number of admin workstations that reach CUI |
| FedRAMP-authorized cloud for CUI storage | Shifts responsibility for cloud controls to authorized provider |
| Dedicated CUI workstations | Prevents personal/HR/finance systems from reaching CUI |
| Air-gapped OT/ICS systems | Removes OT equipment from CMMC scope entirely |
| MSSP providing security services | Moves some SPA obligations to certified third party |

---

## Common Scoping Mistakes

| Mistake | Consequence |
|---------|------------|
| Claiming systems are out-of-scope without verifying network isolation | Systems incorrectly excluded; assessor may flag and force scope expansion |
| Not including email systems | Most CUI is transmitted via email; email servers are CUI Assets |
| Forgetting about backup systems | Backups of CUI are themselves CUI assets |
| Not scoping cloud services | Cloud services storing CUI are ESPs and must meet FedRAMP or equivalent |
| Scoping out home-office workstations | Remote workers using personal devices for CUI work bring those devices in-scope |
| Not including IT support MSP | MSP with privileged access to CUI systems is an ESP |
| Forgetting mobile devices | Mobile devices with CUI (email, apps) are in-scope CUI Assets or CRMAs |

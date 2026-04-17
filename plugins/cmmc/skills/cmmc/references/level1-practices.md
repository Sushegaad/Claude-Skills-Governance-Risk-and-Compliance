# CMMC Level 1 — Foundational (17 Practices)
## Source: FAR 52.204-21 and CMMC 2.0 Final Rule (32 CFR Part 170)

---

## Overview

CMMC Level 1 applies to organizations that handle **Federal Contract Information (FCI)**
but do not process, store, or transmit **Controlled Unclassified Information (CUI)**.

**Definition of FCI (FAR 4.1901):**
> Information, not intended for public release, that is provided by or generated for the
> Government under a contract to develop or deliver a product or service to the Government,
> but not including information provided by the Government to the public (e.g., on public
> Web sites) or simple transactional information, such as that necessary to process payments.

**Assessment Type:** Annual self-assessment by the organization
**Evidence Required:** Organization must retain evidence sufficient to support the affirmation
**Affirmation:** Annual senior-official affirmation required via DIBNet portal

---

## The 17 Level 1 Practices

These 17 practices derive from FAR 52.204-21, "Basic Safeguarding of Covered Contractor
Information Systems." Two pairs of practices overlap in intent with others but are each
independently counted in the CMMC practice numbering.

### Domain: Access Control (AC) — 4 Practices

| Practice ID | Practice Title | Requirement |
|------------|---------------|-------------|
| AC.L1-3.1.1 | Authorized Access Control | Limit information system access to authorized users, processes acting on behalf of authorized users, or devices (including other information systems). |
| AC.L1-3.1.2 | Transaction & Function Control | Limit information system access to the types of transactions and functions that authorized users are permitted to execute. |
| AC.L1-3.1.20 | External Connections | Verify and control/limit connections to external information systems. |
| AC.L1-3.1.22 | Control Public Information | Control information posted or processed on publicly accessible information systems. |

### Domain: Identification and Authentication (IA) — 2 Practices

| Practice ID | Practice Title | Requirement |
|------------|---------------|-------------|
| IA.L1-3.5.1 | Identification | Identify information system users, processes acting on behalf of users, or devices. |
| IA.L1-3.5.2 | Authentication | Authenticate (or verify) the identities of those users, processes, or devices before allowing access. |

### Domain: Media Protection (MP) — 1 Practice

| Practice ID | Practice Title | Requirement |
|------------|---------------|-------------|
| MP.L1-3.8.3 | Media Disposal | Sanitize or destroy information system media containing FCI before disposal or reuse. |

### Domain: Physical Protection (PE) — 4 Practices

| Practice ID | Practice Title | Requirement |
|------------|---------------|-------------|
| PE.L1-3.10.1 | Limit Physical Access | Limit physical access to organizational information systems, equipment, and the respective operating environments to authorized individuals. |
| PE.L1-3.10.3 | Escort Visitors | Escort visitors and monitor visitor activity. |
| PE.L1-3.10.4 | Audit Physical Access | Maintain audit logs of physical access. |
| PE.L1-3.10.5 | Manage Physical Access | Control and manage physical access devices. |

### Domain: System and Communications Protection (SC) — 2 Practices

| Practice ID | Practice Title | Requirement |
|------------|---------------|-------------|
| SC.L1-3.13.1 | Boundary Protection | Monitor, control, and protect organizational communications at the external boundaries and key internal boundaries. |
| SC.L1-3.13.5 | Public-Access System Separation | Implement subnetworks for publicly accessible system components that are physically or logically separated from internal networks. |

### Domain: System and Information Integrity (SI) — 4 Practices

| Practice ID | Practice Title | Requirement |
|------------|---------------|-------------|
| SI.L1-3.14.1 | Flaw Remediation | Identify, report, and correct information and information system flaws in a timely manner. |
| SI.L1-3.14.2 | Malicious Code Protection | Provide protection from malicious code at appropriate locations within organizational information systems. |
| SI.L1-3.14.4 | Update Malicious Code Protection | Update malicious code protection mechanisms when new releases are available. |
| SI.L1-3.14.5 | System & Security Scanning | Perform periodic scans of the information system and real-time scans of files from external sources as files are downloaded, opened, or executed. |

---

## Level 1 Self-Assessment Methodology

### Step 1 — Determine Scope

Identify all assets that process, store, or transmit FCI:
- Workstations and laptops used by employees working on federal contracts
- File servers holding contract deliverables or government-provided information
- Email systems used for contract communications
- Cloud storage containing government-provided documents

### Step 2 — Assess Each Practice

For each of the 17 practices, determine:
- **MET** — The practice is fully implemented for all in-scope assets
- **NOT MET** — The practice is partially or not implemented

### Step 3 — Calculate SPRS Score

CMMC Level 1 uses a simplified scoring model:
- Total possible: 17 practice points
- For Level 1, SPRS scoring uses the same 110-point deduction model but limited to Level 1 practices
- Report score to SPRS via DIBNet before contract award

### Step 4 — Document and Affirm

- Document the self-assessment results
- Brief a senior company official on findings
- Senior official submits annual affirmation via DIBNet portal

---

## Level 1 Evidence Examples

| Practice | Evidence Examples |
|---------|------------------|
| AC.L1-3.1.1 | User account list, Active Directory group policy, access control policy |
| AC.L1-3.1.2 | Role-based access configuration, application access control settings |
| AC.L1-3.1.20 | Firewall rules, network diagram showing external connections list |
| AC.L1-3.1.22 | Web server configuration, content management records, approval procedures |
| IA.L1-3.5.1 | User account naming convention documentation, unique ID assignment records |
| IA.L1-3.5.2 | Password policy, authentication system logs, MFA configuration |
| MP.L1-3.8.3 | Media disposal records, certificate of destruction, data sanitization software logs |
| PE.L1-3.10.1 | Badge/key allocation records, facility access logs, physical security policy |
| PE.L1-3.10.3 | Visitor log, escort policy, visitor badge records |
| PE.L1-3.10.4 | Physical access logs, badge reader system export, CCTV records |
| PE.L1-3.10.5 | Key management log, badge deactivation records, physical device inventory |
| SC.L1-3.13.1 | Firewall configuration, boundary protection policy, network diagram |
| SC.L1-3.13.5 | VLAN configuration, DMZ documentation, network segmentation diagram |
| SI.L1-3.14.1 | Patch management records, vulnerability scan reports, patching policy |
| SI.L1-3.14.2 | AV/EDR deployment records, malicious code protection policy |
| SI.L1-3.14.4 | AV definition update logs, automatic update configuration |
| SI.L1-3.14.5 | Scheduled scan logs, AV real-time scan configuration |

---

## Common Level 1 Deficiencies

1. **No documented scope** — Organization cannot identify all FCI-touching systems
2. **Shared accounts** — Multiple users sharing login credentials (violates AC.L1-3.1.1, IA.L1-3.5.1)
3. **No AV on all workstations** — Not every endpoint has active, up-to-date malware protection
4. **No physical visitor log** — Visitors not logged or escorted (violates PE.L1-3.10.3, PE.L1-3.10.4)
5. **No media disposal process** — Old hard drives with FCI not sanitized before disposal
6. **No patching cadence** — System patches applied irregularly or not documented
7. **Public website has FCI** — Government data inadvertently posted publicly (violates AC.L1-3.1.22)
8. **No SPRS submission** — Organization has never uploaded a score to DIBNet portal

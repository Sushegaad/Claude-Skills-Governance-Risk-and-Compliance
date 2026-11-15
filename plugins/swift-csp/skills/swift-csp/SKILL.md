---
name: swift-csp
description: >
  Expert SWIFT Customer Security Programme (CSP) advisor covering the Customer Security
  Controls Framework (CSCF v2026). Use this skill whenever a user asks about SWIFT CSP,
  CSCF controls, SWIFT security attestation, KYC-SA portal, SWIFT architecture types
  (A1/A2/A3/A4/B), mandatory vs advisory controls, independent assessment, SWIFT secure
  zone, secure flow zone, MFA for operators, SWIFT messaging security, payment fraud
  prevention on SWIFT, gap analysis for CSCF, or compliance with SWIFT's 32 controls
  (26 mandatory, 6 advisory in v2026) across the three objectives: Secure Your
  Environment, Know and Limit Access, Detect and Respond. Control 2.4 (Back-Office
  Data Flow Security) is now mandatory in v2026. v2026 attestation window is July 1–
  December 31, 2026. Trigger for any SWIFT CSP or CSCF compliance question.
---

# SWIFT Customer Security Programme (CSP) - CSCF v2026

> **Last verified:** 2026-11-15

You are an expert advisor on the **SWIFT Customer Security Programme (CSP)** and the **Customer Security Controls Framework (CSCF) v2026**. You help financial institutions, custodians, brokers, and service bureaux achieve and maintain mandatory compliance with SWIFT's 32 security controls across the global payment network.

---

## Framework Overview

| Attribute | Detail |
|-----------|--------|
| **Framework name** | SWIFT Customer Security Controls Framework (CSCF) |
| **Current version** | v2026 (effective July 2026; v2025 valid until June 2026) |
| **Total controls** | 32 - **26 Mandatory + 6 Advisory** |
| **Key v2026 change** | Control 2.4 (Back-Office Data Flow Security) promoted from Advisory → **Mandatory** |
| **Attestation** | Annual - submitted via KYC Security Attestation (KYC-SA) portal |
| **v2026 attestation window** | July 1 – December 31, 2026 |
| **Assessment type** | Community-standard independent assessment (formerly self-attestation for smaller users) |
| **Applies to** | All SWIFT users: banks, brokers, custodians, corporates, service bureaux |
| **Consequence of non-compliance** | Counterparty notifications; potential suspension; regulatory escalation |
| **Next version** | CSCF v2027 expected to be published July 2026 |

---

## Architecture Types

The applicable controls depend on the **SWIFT connectivity architecture** in use:

| Type | Description | Typical User |
|------|-------------|-------------|
| **A1** | User owns BOTH the messaging interface and the communication interface on premises - the fullest local footprint | Large banks, broker-dealers |
| **A2** | User owns the messaging interface; the communication interface is at a service provider | Banks splitting the stack with a provider |
| **A3** | SWIFT connector on the user's premises for application-to-application connectivity (no full interfaces locally) | Mid-tier banks, asset managers |
| **A4** | Customer connector - the user's own server/application connects application-to-application to a service provider's or SWIFT's services (incl. API-based connectors) | Cloud-connected FIs, API integrators |
| **B** | No SWIFT-specific local footprint - access via GUI/browser or fully outsourced (e.g., service bureau) | Smaller banks using bureaux |

> The more SWIFT-related infrastructure you own and operate, the more controls apply.

> **Critical scoping step:** Before assessing any control, confirm which architecture type applies - it determines which controls are mandatory, advisory, or not applicable.

---

## The Three Security Objectives

### Objective 1 - Secure Your Environment (Controls 1.x, 2.x, 3.x)
Protect the SWIFT infrastructure from external and internal threats by isolating it and reducing its attack surface.

### Objective 2 - Know and Limit Access (Controls 4.x, 5.x)
Enforce strong authentication and least-privilege access to SWIFT systems and data.

### Objective 3 - Detect and Respond (Controls 6.x, 7.x)
Detect anomalies, protect data integrity, and respond effectively to cyber incidents.

---

## Control Summary Table (CSCF v2026)

> ⚠️ **v2026 Change**: Control 2.4 is now **Mandatory** (was Advisory in v2025). Institutions with back-office connections to SWIFT that previously skipped 2.4 must now implement it before their 2026 attestation.

| Control | Name | Status (v2026) | Objective |
|---------|------|----------------|-----------|
| **1.1** | SWIFT Environment Protection | Mandatory | 1 |
| **1.2** | OS Privileged Account Control | Mandatory | 1 |
| **1.3** | Virtualisation or Cloud Platform Protection | Mandatory | 1 |
| **1.4** | Restriction of Internet Access | Mandatory | 1 |
| **1.5** | Customer Environment Protection | Mandatory | 1 |
| **2.1** | Internal Data Flow Security | Mandatory | 1 |
| **2.2** | Security Updates | Mandatory | 1 |
| **2.3** | System Hardening | Mandatory | 1 |
| **2.4** | Back-Office Data Flow Security | **Mandatory** *(NEW in v2026 - was Advisory in v2025)* | 1 |
| **2.5A** | External Transmission Data Protection | Advisory | 1 |
| **2.6** | Operator Session Confidentiality and Integrity | Mandatory | 1 |
| **2.7** | Vulnerability Scanning | Mandatory | 1 |
| **2.8** | Outsourced Critical Activity Protection | Mandatory | 1 |
| **2.9** | Transaction Business Controls | Mandatory | 1 |
| **2.10** | Application Hardening | Mandatory | 1 |
| **2.11A** | RMA Business Controls | Advisory | 1 |
| **3.1** | Physical Security | Mandatory | 1 |
| **4.1** | Password Policy | Mandatory | 2 |
| **4.2** | Multi-Factor Authentication | Mandatory | 2 |
| **5.1** | Logical Access Controls | Mandatory | 2 |
| **5.2** | Token Management | Mandatory | 2 |
| **5.3A** | Staff Screening Process | Advisory | 2 |
| **5.4** | Physical and Logical Password Storage | Mandatory | 2 |
| **6.1** | Malware Protection | Mandatory | 3 |
| **6.2** | Software Integrity | Mandatory | 3 |
| **6.3** | Database Integrity | Mandatory | 3 |
| **6.4** | Logging and Monitoring | Mandatory | 3 |
| **6.5A** | Intrusion Detection | Advisory | 3 |
| **7.1** | Cyber Incident Response Planning | Mandatory | 3 |
| **7.2** | Security Training and Awareness | Mandatory | 3 |
| **7.3A** | Penetration Testing | Advisory | 3 |
| **7.4A** | Scenario-based Risk Assessment | Advisory | 3 |

*(A = Advisory control)*

---

## Control 2.4 - Back-Office Data Flow Security (Now Mandatory)

This is the most significant change in CSCF v2026. Organizations that skipped 2.4 as advisory must now implement it. Control 2.4 targets back-office data-flow security for first-hop flows; it is **not applicable to architecture B** (no SWIFT-specific local footprint).

**What Control 2.4 requires:**
- All data flows between the SWIFT secure zone and back-office systems must be protected
- Encryption of data in transit between SWIFT and back-office (trading systems, core banking, payment hubs)
- Authentication of back-office systems connecting to the SWIFT zone
- Prevention of unauthorized data exfiltration via back-office channels
- Network segmentation between SWIFT zone and back-office environment

**Common gaps when 2.4 was advisory:**
- Unencrypted messaging between SWIFT Alliance and back-office payment hub
- No mutual TLS or equivalent authentication on back-office connections
- Shared network segments between SWIFT zone and general back-office VLAN

**Remediation approach:**
1. Map all data flows between SWIFT secure zone and back-office systems
2. Implement TLS 1.2+ with certificate-based mutual authentication on all connections
3. Place all back-office connections through a dedicated interface within the secure zone
4. Apply firewall rules restricting back-office access to named IP addresses/ports only
5. Log all back-office connection events to the SIEM

---

## Current Status - September 2026 (state where relevant)

- **CSCF v2026 is the operative framework** (32 controls: **26 mandatory + 6 advisory** - Control 2.4 dropped its advisory-era "2.4A" suffix on promotion; 2.4 is **not applicable to architecture B**). v2026 also expanded mandatory assessment of **customer client connectors under 14 controls** (1.2, 1.3, 1.4, 2.2, 2.3, 2.6, 2.7, 3.1, 4.1, 4.2, 5.1, 5.4, 6.1, 6.4) - some architecture B users reclassify as A4. Pre-announced for **v2028**: protection of legacy back-office flows becomes mandatory.
- **CSCF v2027: no public confirmation as of September 14, 2026** - Swift's public document centre still lists v2026 as latest (the next-year CSCF is typically released ~July via the login-gated Knowledge Centre; "v2027 readiness" webinars are running). Do not assert v2027 content; advise checking the Knowledge Centre.
- **KYC-SA attestation season is decisive now**: the new controls version appears in KYC-SA in early July; attest July–December, **no later than December 31**, and every attestation must be supported by an **independent assessment** (Independent Assessment Framework). Consequences of missing/non-compliant attestation: Swift reports users to their **supervisor via a dedicated real-time application** and status is **visible to counterparties** in KYC-SA (the published lever is reporting/visibility, not disconnection). Assessment capacity tightens from October - book assessors now.

## How to Respond

Match your output to the task type:

| Task | Output Format |
|------|--------------|
| Gap assessment | Table: Control ID \| Control Name \| Status (🔴/🟡/🟢) \| Evidence Required \| Gap Notes |
| Architecture scoping | Table mapping architecture type to applicable controls |
| Control deep-dive | Structured narrative: Purpose → Requirement → Implementation steps → Evidence artifacts |
| KYC-SA attestation prep | Checklist by control with attestation status and evidence pointers |
| Incident response | Step-by-step procedure with SWIFT notification obligations |
| Cross-framework mapping | Side-by-side table (CSCF ↔ ISO 27001 / PCI DSS / NIST CSF) |
| v2025 → v2026 gap | Focus specifically on Control 2.4 mandatory upgrade requirements |

Always cite the specific **control number** (e.g., 4.2, 6.4) - not just the control name.

---

## Key Implementation Priorities

The following controls are the **highest-risk** and most commonly cited in SWIFT assessments:

1. **4.2 - Multi-Factor Authentication**: MFA required for all interactive operator sessions to the SWIFT environment; hardware tokens or equivalent required
2. **2.4 - Back-Office Data Flow Security**: Now mandatory in v2026; encrypt and authenticate all back-office connections
3. **1.1 - SWIFT Environment Protection**: Dedicated secure zone; no browsing from SWIFT servers; network segregation with firewall rules
4. **6.4 - Logging and Monitoring**: All SWIFT system events and transactions logged; anomaly alerts; minimum 1-year retention
5. **2.2 - Security Updates**: Timely application of vendor and SWIFT security updates, prioritised by severity, with documented exceptions and compensating controls
6. **6.2 - Software Integrity**: Verify integrity of SWIFT software before installation and after updates
7. **2.3 - System Hardening**: CIS Benchmark hardening or equivalent; remove all unnecessary services
8. **1.4 - Internet Restriction**: SWIFT infrastructure must not have direct internet access; jump servers required

---

## Annual Assessment and Attestation Timeline

| Activity | Timing |
|----------|--------|
| v2026 attestation window opens | **July 1, 2026** |
| Assessment period | July 1 – December 31, 2026 |
| KYC-SA attestation deadline | **December 31, 2026** *(v2026 window)* |
| Counterparty visibility of attestation | Immediately upon submission |
| Non-attesting user flagged to counterparties | After deadline |
| CSCF v2027 publication expected | July 2026 |

> **Note**: The traditional annual deadline of July 31 applied under prior cycles. For v2026, SWIFT has opened an extended attestation window (July 1 – December 31, 2026). Verify current PMO guidance at swift.com/myswift.

---

## Common Findings and Remediation

| Control | Common Finding | Remediation |
|---------|---------------|-------------|
| 2.4 | Back-office connections unencrypted or unauthenticated *(now mandatory)* | Implement mutual TLS 1.2+ on all back-office data flows; segment with dedicated firewall rules |
| 4.2 | Software-based OTP rather than hardware token | Deploy hardware authentication tokens for all SWIFT operators |
| 1.1 | SWIFT servers on shared network segment | Create dedicated VLAN/zone with stateful firewall rules; no dual-homing |
| 2.2 | Security updates applied late or inconsistently | Establish a risk-based patch management process that applies security updates in a timely manner per control 2.2; document exceptions with compensating controls |
| 6.4 | Logs not reviewed; no SIEM coverage of SWIFT events | Configure SIEM to ingest Alliance Access/Gateway logs; set alert rules |
| 5.1 | Shared operator accounts; no least privilege | Enforce individual accounts; audit roles quarterly; remove stale access |
| 2.7 | Vulnerability scans not covering all SWIFT components | Include all SWIFT-connected systems in quarterly credentialed scan scope |
| 7.1 | Incident response plan not SWIFT-specific | Document SWIFT-specific IRP: detection triggers, escalation to SWIFT, evidence preservation |
| 3.1 | Server room access not logged | Implement card access with audit trail; restrict to named individuals |

---

## Reference Files

For deeper content, read these files as needed:
- **references/swift-controls.md** - All 32 controls with full implementation requirements, evidence artifacts, and architecture applicability by type (A1/A2/A3/A4/B); includes v2025→v2026 change summary
- **references/swift-assessment.md** - KYC-SA attestation process, independent assessor requirements, cross-framework mapping (ISO 27001, PCI DSS, NIST CSF), and SWIFT-specific incident reporting obligations

---

> *This skill provides general compliance information, not legal advice. Verify current requirements against official sources; consult qualified counsel or an accredited assessor for decisions.*

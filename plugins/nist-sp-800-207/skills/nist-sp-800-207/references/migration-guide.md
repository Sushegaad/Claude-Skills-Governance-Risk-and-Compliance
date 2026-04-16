# NIST SP 800-207 — ZTA Migration Guide, CISA ZTMM, and SP 800-53 Alignment

**Source**: NIST SP 800-207, August 2020; CISA Zero Trust Maturity Model v2.0, April 2023

---

## ZTA Migration Assessment

Before beginning migration, assess the organisation's current state and readiness:

### Current-State Assessment Checklist

**Identity and Access Management**
- [ ] Single authoritative IdP exists (or a federated set with clear hierarchy)
- [ ] MFA deployed for at least privileged accounts
- [ ] MFA deployed for all remote access
- [ ] Phishing-resistant MFA deployed for all privileged accounts (FIDO2, PIV)
- [ ] Role-based access control enforced; no shared accounts
- [ ] Password policy aligned to SP 800-63B (length over complexity; no mandatory rotation)
- [ ] Service accounts inventoried; credentials managed; non-interactive where possible

**Device Management**
- [ ] All enterprise-managed devices enrolled in MDM
- [ ] Device inventory complete and current
- [ ] Patch compliance rate >= 95% for critical patches
- [ ] Endpoint detection and response (EDR) deployed on all managed devices
- [ ] Device compliance policies defined and enforced
- [ ] Unmanaged device access policy defined

**Network**
- [ ] Network flow map exists and is current
- [ ] East-west traffic visibility available (NetFlow, NDR, or equivalent)
- [ ] No flat internal network with full lateral movement capability (some segmentation exists)
- [ ] Remote access uses MFA (even if VPN; ZTNA migration pending)

**Applications and Workloads**
- [ ] Application inventory exists and is current
- [ ] Applications classified by sensitivity (Low/Moderate/High)
- [ ] Critical applications support modern authentication (SAML, OIDC)
- [ ] Legacy applications with no modern auth support identified (migration challenge)

**Data**
- [ ] Data classified and labelled (sensitivity classifications applied)
- [ ] Sensitive data locations known (on-premises data stores, cloud, SaaS)
- [ ] Data access audit logging enabled

**Monitoring and Analytics**
- [ ] SIEM collecting logs from all critical systems
- [ ] Access logs centralised
- [ ] Anomaly detection or UEBA capability available or planned

---

## ZTA Migration Roadmap

### Phase 1 — Foundation (Months 1–6)
Priority: Build the identity and visibility foundation on which ZTA depends.

| Activity | Owner | Success Criterion |
|---|---|---|
| Deploy phishing-resistant MFA for all privileged accounts | IAM Team | 100% of privileged accounts on FIDO2 or PIV |
| Enroll all managed devices in MDM | Endpoint Team | 100% of managed devices enrolled |
| Complete device inventory | Asset Management | Full device inventory, classified managed/unmanaged |
| Complete application inventory and sensitivity classification | Security Architecture | All applications inventoried and classified |
| Centralise log collection for all critical systems | SIEM Team | All critical systems logging to SIEM |
| Establish network flow visibility for east-west traffic | Network Team | East-west flows visible from SIEM/NDR |

### Phase 2 — First ZTA Controls (Months 6–12)
Priority: Apply ZTA protection to the highest-sensitivity resources.

| Activity | Owner | Success Criterion |
|---|---|---|
| Deploy identity-aware proxy for top 10 highest-sensitivity applications | Security Architecture + IAM | Proxy in place; legacy direct access removed |
| Enable device posture signals in access policy for high-sensitivity apps | IAM + Endpoint Teams | Compliance status checked at every access request |
| Deploy ZTNA for remote access to high-sensitivity applications | Network + Security Teams | Remote users accessing high-sensitivity apps via ZTNA |
| Implement microsegmentation for database tier | Network + Security Teams | Database tier isolated; only approved app tiers can reach DBs |
| Establish behavioural analytics baseline | SIEM/UEBA Team | 90-day baseline established for active users |

### Phase 3 — Broad ZTA Coverage (Months 12–24)
Priority: Extend ZTA to all resources; retire legacy implicit trust paths.

| Activity | Owner | Success Criterion |
|---|---|---|
| Extend identity-aware proxy to all applications | Security Architecture | All applications behind PEP |
| Enforce MFA for all enterprise resource access | IAM Team | 100% MFA coverage across all access paths |
| Extend microsegmentation to all workload tiers | Network + Security Teams | All workload communication enforced via segmentation policy |
| Replace VPN with ZTNA for all remote access | Network Team | Legacy VPN decommissioned for covered user population |
| Define and enforce unmanaged device policy | IAM + Endpoint Teams | Unmanaged devices restricted to approved applications only |
| Enable anomaly detection alerts from behavioural analytics | SOC | SOC receiving and triaging UEBA alerts |

### Phase 4 — Optimise (Months 24+)
Priority: Achieve ongoing authorisation, automated policy, and continuous improvement.

| Activity | Owner | Success Criterion |
|---|---|---|
| Implement just-in-time (JIT) privileged access | IAM + PAM Teams | No standing privileged access; all privilege granted on-demand |
| Enable automated policy adjustment from threat intelligence | PE/SOC Teams | PE trust algorithm incorporating live threat intel |
| Data-layer ZTA (ABAC at data service level) | Data + Security Teams | Data access enforced by attributes at the data service level |
| ZTA coverage audit complete | Security Architecture | No resource accessible without ZTA PEP |
| Achieve CISA ZTMM Advanced level across all five pillars | CISO | ZTMM self-assessment showing Advanced in all pillars |

---

## CISA Zero Trust Maturity Model (ZTMM) Alignment

The CISA ZTMM v2.0 (April 2023) defines maturity across five pillars. Each pillar has four stages.

### Pillar 1 — Identity

| Stage | Characteristics |
|---|---|
| Traditional | Static, manual lifecycle management; limited MFA use; centralised IdP absent |
| Initial | Some MFA; limited centralisation; limited attribute-based access |
| Advanced | MFA fully deployed; risk-based access decisions; phishing-resistant MFA for privileged; automated lifecycle management |
| Optimal | Continuous validation; dynamic access based on full context; passwordless; ML-assisted anomaly detection |

**SP 800-207 Alignment**: Identity is Approach 1 (EIG). NIST SP 800-63B defines the authentication assurance levels (AAL) that feed the ZTA trust algorithm.

### Pillar 2 — Devices

| Stage | Characteristics |
|---|---|
| Traditional | Limited device inventory; manual patching; no integration with access decisions |
| Initial | MDM deployed for managed devices; device compliance partially integrated |
| Advanced | All devices inventoried; compliance enforced in access policy; EDR fully deployed |
| Optimal | Continuous device trust assessment; automated isolation of non-compliant devices; AI/ML device anomaly detection |

**SP 800-207 Alignment**: Device posture is a key trust algorithm input (Tenet 5). CDM provides device compliance data.

### Pillar 3 — Networks

| Stage | Characteristics |
|---|---|
| Traditional | Flat internal network; VPN for remote access; minimal segmentation |
| Initial | Some macro-segmentation (VLANs); VPN with MFA |
| Advanced | Microsegmentation of critical workloads; ZTNA deployed for remote access |
| Optimal | All resources behind ZTA PEP; no implicit trust based on network location; dynamic segmentation; all remote access through ZTNA |

**SP 800-207 Alignment**: Approach 2 (microsegmentation) and Approach 3 (SDN/ZTNA) address this pillar.

### Pillar 4 — Applications and Workloads

| Stage | Characteristics |
|---|---|
| Traditional | Applications not integrated with IdP; no per-application access control; limited logging |
| Initial | Some applications integrated with IdP; basic per-application access control |
| Advanced | Most applications integrated with IdP; per-application access policy; workload-to-workload authentication |
| Optimal | All applications behind ZTA PEP; continuous authorisation during session; API security enforced; CI/CD pipeline security |

**SP 800-207 Alignment**: PEP coverage of all applications is core to ZTA. Workload identity maps to Approach 2 and service mesh implementations.

### Pillar 5 — Data

| Stage | Characteristics |
|---|---|
| Traditional | No data classification; no data access audit; encryption inconsistent |
| Initial | Some data classification; encryption at rest and in transit for sensitive data |
| Advanced | Consistent data classification and labelling; attribute-based access control at data layer; DLP deployed |
| Optimal | All data classified and labelled; access enforced at the data level (ABAC); automated data protection based on classification; full data access audit |

**SP 800-207 Alignment**: Data-layer ZTA is the most mature ZTA application. SP 800-207 Tenet 1 (all data is a resource) drives data-layer enforcement.

---

## ZTA and SP 800-53 Rev 5 Control Alignment

ZTA implementation contributes to or satisfies the following SP 800-53 controls:

| SP 800-53 Control | ZTA Component/Approach | Contribution |
|---|---|---|
| AC-2 Account Management | IdP + EIG | Centralised account lifecycle management; inactive account detection |
| AC-3 Access Enforcement | PE + PEP | Per-session, attribute-based access enforcement at every resource |
| AC-4 Information Flow Enforcement | PEP + Microsegmentation | Microsegmentation enforces information flow policy |
| AC-17 Remote Access | ZTNA / Approach 3 | ZTNA replaces VPN; provides ZTA-aligned remote access |
| AC-20 Use of External Systems | ZTNA + EIG | Third-party and BYOD access controlled through ZTA |
| AU-2/AU-3 Audit Events/Content | ZTA logging | All PE decisions and PEP events logged to SIEM |
| IA-2 Identification and Authentication | IdP + MFA | Phishing-resistant MFA; AAL-aligned authentication |
| IA-3 Device Identification | Device identity + MDM | Cryptographic device identity as trust input |
| IA-5 Authenticator Management | IdP | Centralised credential lifecycle; MFA enforcement |
| SC-3 Security Function Isolation | ZTA control plane separation | PE/PA isolated from data plane |
| SC-7 Boundary Protection | PEP | PEP is the micro-boundary for every resource |
| SC-8 Transmission Confidentiality | ZTA encrypted sessions | All ZTA sessions use mutual TLS or equivalent |
| SC-39 Process Isolation | Microsegmentation | Workload isolation prevents cross-workload access |
| SI-4 System Monitoring | ZTA telemetry + SIEM | Access event monitoring; behavioural analytics for anomaly detection |

---

## ZTA Threat Mitigation Summary

| Threat | ZTA Controls That Mitigate It |
|---|---|
| Phishing (credential theft) | Phishing-resistant MFA (FIDO2, PIV) removes password from the authentication equation |
| Lateral movement after initial compromise | Microsegmentation prevents compromised workload from accessing other resources; per-session authorisation prevents reuse of prior access |
| Privilege escalation | JIT privileged access; PE evaluates every privileged access request; no standing privilege |
| Stolen device | Device health check fails for stolen/wiped device; MDM remote wipe; session revocation |
| Insider threat | Least privilege enforced by PE; no implicit access; all access logged; UEBA anomaly detection |
| Compromised service account | Service accounts have minimum required scope; workload identity per-request authorisation; UEBA on service account behaviour |
| Man-in-the-middle attack | Mutual TLS for all ZTA control plane and data plane communication; certificate pinning where supported |
| Ransomware lateral movement | Microsegmentation (Approach 2) blocks east-west spread; device quarantine on EDR alert through PE policy update |

---

## Key ZTA Terms and Definitions

| Term | Definition |
|---|---|
| Zero Trust | Security model in which implicit trust is never granted based on network location, physical location, or asset ownership |
| Zero Trust Architecture (ZTA) | Enterprise architecture applying ZTA principles; includes people, process, technology, and policy |
| Implicit trust | Trust granted based on network location (e.g., "you are on the corporate network, therefore you are trusted") — removed in ZTA |
| Policy Engine (PE) | ZTA component that makes the access grant/deny decision |
| Policy Administrator (PA) | ZTA component that executes the PE decision by configuring the PEP |
| Policy Enforcement Point (PEP) | ZTA component that controls the communication path between subject and resource |
| Trust Algorithm | Logic used by the PE to compute an access decision from input signals |
| Microsegmentation | Security practice of placing individual security perimeters around workloads |
| Software-Defined Perimeter (SDP) | Network security approach where resources are invisible until authenticated |
| ZTNA | Zero Trust Network Access — commercial product category implementing SDP-style access |
| Enhanced Identity Governance (EIG) | ZTA approach where identity is the primary access control signal |
| Session-based access | Access granted per session, not per user — each session is independently evaluated |
| Continuous validation | Re-evaluation of access conditions throughout a session, not only at session start |

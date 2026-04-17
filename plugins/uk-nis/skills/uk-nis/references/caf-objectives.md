# UK NIS — CAF Objectives Reference
## NCSC Cyber Assessment Framework (CAF) v3.2

The Cyber Assessment Framework (CAF) was developed by the National Cyber Security Centre (NCSC) and is the primary technical standard used by UK NIS Competent Authorities to assess compliance with the security requirements of the NIS Regulations 2018 (Regulation 10).

The CAF is organised into **4 top-level objectives** and **14 contributing outcomes**. Each outcome has a set of **Indicators of Good Practice (IGP)** — characteristics of organisations that are achieving the outcome — and **Indicators of Poor Practice (IPP)** — characteristics indicating the outcome is not being met.

---

## Objective A — Managing Security Risk

Appropriate organisational structures, policies, and processes are in place to understand, assess, and systematically manage security risks to the network and information systems supporting essential services.

---

### A1 — Governance

**Outcome:** The organisation has effective organisational structures, policies, and processes in place to understand, assess, and systematically manage security risks to the network and information systems supporting the operation of essential services.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| A1.a | Board or senior management has overall accountability for cyber security and demonstrates active engagement |
| A1.b | There are clearly defined and widely understood roles and responsibilities for security of NIS across the organisation |
| A1.c | Decisions about security risk are taken at the appropriate level within the organisation (proportionate to risk) |
| A1.d | There are documented security policies relevant to the essential service, approved at board/senior management level |
| A1.e | Policies are communicated effectively to all relevant staff and third parties |
| A1.f | The organisation has processes for managing the security of NIS through transition or change |
| A1.g | There is a named individual with overall responsibility for cyber security (such as a CISO or equivalent) |
| A1.h | Cyber risk is included in the organisation's overall risk management framework |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| A1.i | There is no board-level or senior management ownership of cyber security risk |
| A1.ii | Security responsibilities are unclear, unassigned, or not communicated |
| A1.iii | Security policies are absent, outdated (not reviewed in 2+ years), or not approved by senior management |
| A1.iv | There is no mechanism to escalate security concerns to appropriate decision-makers |

---

### A2 — Risk Management

**Outcome:** The organisation takes a systematic approach to assessing and managing security risks to the network and information systems supporting the operation of essential services.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| A2.a | The organisation has a documented, systematic risk assessment process covering NIS |
| A2.b | Risk assessments are regularly reviewed and updated (at minimum annually, and following significant change) |
| A2.c | Risk treatment decisions are documented and approved by appropriate authority |
| A2.d | A risk register exists that covers cyber risks to NIS |
| A2.e | Residual risk is understood and accepted at the appropriate level within the organisation |
| A2.f | Threat intelligence is used to inform risk assessments |
| A2.g | Risk assessments consider insider threats, not just external threats |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| A2.i | No documented risk assessment process exists |
| A2.ii | Risk assessments have not been reviewed in over 12 months or following significant change |
| A2.iii | The risk register is absent, incomplete, or not linked to treatment actions |
| A2.iv | Risk treatment decisions are not documented or approved |

---

### A3 — Asset Management

**Outcome:** Everything required to deliver, maintain, or support essential services is determined and understood. This covers data, technology, facilities, and people.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| A3.a | The organisation has an up-to-date inventory of all NIS assets (hardware, software, data, people, facilities) |
| A3.b | Assets are classified by their criticality to essential service delivery |
| A3.c | Data flows to and from NIS are understood and documented |
| A3.d | Asset ownership is assigned for all critical assets |
| A3.e | The organisation understands interdependencies between assets and how failures could affect essential services |
| A3.f | The asset inventory is reviewed and updated regularly (at minimum annually and following changes) |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| A3.i | No asset inventory exists |
| A3.ii | The asset inventory is significantly incomplete or outdated |
| A3.iii | Asset criticality is not assessed or understood |
| A3.iv | Data flows are not mapped or understood |

---

### A4 — Supply Chain

**Outcome:** The organisation understands and manages security risks to its essential services from the supply chain, including third-party suppliers of technology, people, or facilities.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| A4.a | The organisation has identified all third-party suppliers who have access to, or influence over, NIS |
| A4.b | Security requirements are included in supplier contracts and service level agreements |
| A4.c | Suppliers are assessed for their cyber security practices prior to engagement and periodically thereafter |
| A4.d | Security incidents or changes by suppliers are reported to the organisation and managed appropriately |
| A4.e | There is a process for managing supplier termination and ensuring secure offboarding |
| A4.f | The organisation understands the security implications of software and hardware in the supply chain (e.g. SBOM awareness, firmware integrity) |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| A4.i | Suppliers with access to NIS are not identified |
| A4.ii | Contracts with critical suppliers contain no security requirements |
| A4.iii | Suppliers are never assessed for their security practices |
| A4.iv | Supplier incidents or changes are not reported to or acted upon by the organisation |

---

## Objective B — Protecting Against Cyber Attack

Proportionate security measures are in place to protect the essential service's network and information systems from cyber attack.

---

### B1 — Service Protection Policies and Processes

**Outcome:** The organisation defines, implements, communicates, and enforces appropriate policies and processes that direct its overall approach to securing systems and data that support delivery of the essential service.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| B1.a | Security policies are documented, approved by senior management, and actively communicated to relevant staff |
| B1.b | Security requirements are integrated into system and service design processes ("security by design") |
| B1.c | There is a documented change management process that includes security assessment of proposed changes to NIS |
| B1.d | The organisation has processes for scanning and testing to identify security vulnerabilities |
| B1.e | Security configurations are documented, maintained, and enforced |
| B1.f | There is a documented software development or procurement security standard |
| B1.g | Policies cover physical security of systems and facilities used to deliver vulnerable essential services |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| B1.i | No security policies exist or they are not followed in practice |
| B1.ii | Security is not considered during system design or procurement |
| B1.iii | Changes to NIS are not assessed for security impact |
| B1.iv | No vulnerability management process exists |

---

### B2 — Identity and Access Control

**Outcome:** The organisation understands, documents, and controls access to systems and functions that support delivery of the essential service. Access is controlled on a principle of least privilege.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| B2.a | User accounts are issued with the minimum privileges necessary for their role (least privilege) |
| B2.b | Privileged access is tightly controlled; the number of users with privileged access is minimised |
| B2.c | Multi-factor authentication (MFA) is in use for privileged access, remote access, and access to critical NIS |
| B2.d | Accounts are reviewed regularly and deprovisioned promptly when no longer required (e.g. on staff departure) |
| B2.e | Authentication credentials (especially passwords) are managed securely (no default credentials, password policies enforced) |
| B2.f | Access to NIS is logged; logs are reviewed |
| B2.g | Remote access is secured (e.g. via VPN, MFA, IP allowlisting) |
| B2.h | Service accounts are managed; credentials are unique and not shared |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| B2.i | Default credentials are in use on systems |
| B2.ii | Privileged access is not controlled or monitored |
| B2.iii | MFA is not used for privileged or remote access |
| B2.iv | Departed staff accounts are not removed promptly |
| B2.v | Access review processes do not exist |

---

### B3 — Data Security

**Outcome:** Data stored, processed, and transmitted by the networks and information systems supporting essential services is protected against unauthorised access, modification, or loss.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| B3.a | Sensitive data is identified, classified, and handled according to its classification |
| B3.b | Data at rest is encrypted where appropriate to the risk |
| B3.c | Data in transit is encrypted using appropriate protocols (e.g. TLS 1.2+) |
| B3.d | Removable media is controlled and encrypted; procedures exist for secure disposal |
| B3.e | Personal data (including PII linked to essential services) is handled in accordance with data protection requirements |
| B3.f | Backups of critical data are taken regularly, stored securely, and recovery is tested |
| B3.g | There are procedures for managing data throughout its lifecycle, including secure deletion |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| B3.i | Sensitive data is not identified or classified |
| B3.ii | Unencrypted data is transmitted or stored where encryption is appropriate |
| B3.iii | Backups are not taken or not tested |
| B3.iv | Removable media is uncontrolled |

---

### B4 — System Security

**Outcome:** Network and information systems used to deliver essential services are protected from exploitation of known vulnerabilities.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| B4.a | Systems are built and configured securely against an approved baseline configuration |
| B4.b | Patches and security updates are applied in a timely manner proportionate to risk (critical patches within 14 days as a benchmark) |
| B4.c | End-of-life systems are identified; either mitigating controls are in place or there is a plan to replace them |
| B4.d | Anti-malware protections are deployed where appropriate |
| B4.e | All software and hardware assets are inventoried; unauthorised assets and software are detected |
| B4.f | Security testing (e.g. penetration testing) is carried out regularly on NIS |
| B4.g | Secure software development practices are in use where software is developed in-house |
| B4.h | Systems are hardened; unnecessary services, ports, and protocols are disabled |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| B4.i | Critical patches are not applied within a reasonable timeframe |
| B4.ii | End-of-life systems are in use with no mitigation or replacement plan |
| B4.iii | Default system configurations are in use |
| B4.iv | No anti-malware deployed on applicable systems |

---

### B5 — Resilient Networks and Systems

**Outcome:** The organisation builds resilience against cyber attack and system failure into the design and operation of the networks and information systems that support essential services.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| B5.a | Network architecture is designed with security in mind; zones and segmentation are used to limit the impact of a compromise |
| B5.b | Critical NIS components have redundancy and failover in place |
| B5.c | There is documented and tested business continuity/disaster recovery capability for essential services |
| B5.d | Recovery time objectives (RTOs) and recovery point objectives (RPOs) are defined for critical systems |
| B5.e | NIS components are protected against denial-of-service attacks (e.g. DDoS mitigation) |
| B5.f | Network traffic is monitored; anomalous traffic can be detected and blocked |
| B5.g | Operational Technology (OT) and IT networks are appropriately segregated |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| B5.i | No network segmentation; a single compromise could affect the entire NIS or essential service |
| B5.ii | No redundancy or failover for critical systems |
| B5.iii | Business continuity or disaster recovery plans have not been tested |
| B5.iv | RT/RPOs are not defined |

---

### B6 — Staff Awareness and Training

**Outcome:** Staff have appropriate awareness and skills to support the security of network and information systems that deliver essential services.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| B6.a | All staff receive regular cyber security awareness training appropriate to their role |
| B6.b | Staff with specific security responsibilities receive role-appropriate technical training |
| B6.c | Awareness training includes recognition of phishing, social engineering, and insider threats |
| B6.d | Training completion is tracked and records are maintained |
| B6.e | Awareness programme content is reviewed and updated regularly (at minimum annually) |
| B6.f | Board/senior management receive appropriate cyber security briefings |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| B6.i | No security awareness training programme exists |
| B6.ii | Training has not been delivered or updated in over 12 months |
| B6.iii | Completion is not tracked |
| B6.iv | Senior management have received no cyber security briefing |

---

## Objective C — Detecting Cyber Security Events

Proportionate capabilities to detect cyber security events affecting, or with the potential to affect, essential services are in place.

---

### C1 — Security Monitoring

**Outcome:** The organisation monitors the security status of the networks and information systems supporting the delivery of essential services, to detect potential security problems and to track the ongoing effectiveness of protective measures.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| C1.a | Logs are collected from critical NIS components (servers, network devices, authentication systems, endpoints) |
| C1.b | Logs are centralised and retained for an appropriate period (minimum 6 months as a benchmark; longer for high-risk systems) |
| C1.c | Alerts are generated for security-relevant events; monitoring is continuous |
| C1.d | There is a defined process for reviewing and acting on security alerts |
| C1.e | The organisation has, or has access to, a Security Operations Centre (SOC) capability |
| C1.f | User and entity behaviour analytics (UEBA) or equivalent is used for detecting anomalous behaviour |
| C1.g | Monitoring capability includes detection of lateral movement, privilege escalation, and data exfiltration |
| C1.h | Out-of-hours monitoring or escalation procedures are in place |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| C1.i | Logging is absent or incomplete on critical systems |
| C1.ii | Logs are not reviewed; there is no alerting |
| C1.iii | Log retention is insufficient |
| C1.iv | There is no process for acting on alerts |

---

### C2 — Proactive Security Event Discovery

**Outcome:** Systems that support the delivery of essential services are checked for indications of compromise or malicious activity by proactive investigation of potential security breaches.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| C2.a | Regular vulnerability scanning is conducted on NIS |
| C2.b | Penetration testing is conducted periodically (minimum annually for high-risk systems, following significant changes) |
| C2.c | Threat intelligence is used to hunt for indicators of compromise in the organisation's NIS |
| C2.d | Results from testing and scanning are tracked and drive remediation actions |
| C2.e | The organisation participates in or accesses threat intelligence sharing (e.g. NCSC Early Warning, sector ISACs) |
| C2.f | Automated tools are used to detect misconfigurations and deviations from baseline in NIS |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| C2.i | No vulnerability scanning or penetration testing is conducted |
| C2.ii | Testing results are not acted upon or tracked |
| C2.iii | No threat intelligence is consumed or applied |

---

## Objective D — Minimising the Impact of Cyber Security Incidents

Capabilities to minimise the impact of a cyber security incident on the delivery of essential services are in place, including the restoration of those services where necessary.

---

### D1 — Response and Recovery Planning

**Outcome:** There are tested, organisation-specific response and recovery plans in place for cyber security incidents affecting systems supporting essential services.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| D1.a | A documented Incident Response Plan (IRP) exists that is specific to the organisation's NIS |
| D1.b | The IRP is tested at least annually (e.g. tabletop exercises, simulations) |
| D1.c | Roles and responsibilities during incident response are clearly defined and known |
| D1.d | Contact details for key personnel, Competent Authorities, NCSC, law enforcement, and critical suppliers are maintained and up to date |
| D1.e | Business continuity plans exist for essential services and are linked to the IRP |
| D1.f | Recovery plans include steps to restore systems from clean backups |
| D1.g | The organisation has procedures for communicating during an incident (internal staff, regulator, media, public) |
| D1.h | NIS incident notification procedures are documented and staff are aware of reporting obligations |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| D1.i | No IRP exists |
| D1.ii | The IRP has not been tested |
| D1.iii | Response roles are not defined or communicated |
| D1.iv | Contact information is unavailable or outdated |

---

### D2 — Improvements

**Outcome:** When a cyber security incident has occurred, steps are taken to understand its causes and reduce the risk of a similar incident occurring in future.

#### Indicators of Good Practice (IGP)

| IGP Ref | Description |
|---------|-------------|
| D2.a | Post-incident reviews are conducted following significant incidents |
| D2.b | Root cause analysis is performed and documented |
| D2.c | Lessons learned from incidents are fed back into risk assessments, policies, and controls |
| D2.d | Near-misses and security events (not just confirmed incidents) are reviewed for learning opportunities |
| D2.e | Changes to controls and processes resulting from lessons learned are tracked and implemented |
| D2.f | The organisation shares appropriate lessons learned with the relevant Competent Authority and NCSC where relevant |

#### Indicators of Poor Practice (IPP)

| IPP Ref | Description |
|---------|-------------|
| D2.i | No post-incident review process exists |
| D2.ii | Lessons learned are not documented or acted upon |
| D2.iii | The same type of incident recurs without control improvements |

---

## CAF Assessment Rating Guidance

### Rating Scale

| Rating | Meaning | CAF Criteria |
|--------|---------|-------------|
| Achieved | All IGP are met; no IPP apply | Full compliance with the outcome |
| Partially Achieved | Most IGP are met; minor gaps; no critical IPP apply | Substantial progress but room for improvement |
| Not Achieved | Critical IGP not met; significant IPP apply | Material non-compliance |
| Not Applicable | The outcome is not relevant to this organisation's NIS | Documented justification required |

### Prioritisation Framework

When producing remediation plans, prioritise:
1. **Objectives A1 and A2** (Governance and Risk Management) — foundational to all other outcomes
2. **Objective D1** (Response and Recovery) — directly affects NIS resilience and regulatory reporting
3. **Objective B2** (Identity and Access Control) — high-impact protective control
4. **Objective C1** (Security Monitoring) — required for incident detection

---

## Version Note

This reference is based on **CAF v3.2** as published by the NCSC. The CAF is subject to revision; always verify against the current version at ncsc.gov.uk/collection/caf.

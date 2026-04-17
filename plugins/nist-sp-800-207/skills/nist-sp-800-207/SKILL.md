---
name: nist-sp-800-207
description: >
  NIST SP 800-207 Zero Trust Architecture (ZTA) skill. Answers questions about the seven ZTA tenets,
  the logical ZTA components (Policy Engine, Policy Administrator, Policy Enforcement Point), three
  ZTA deployment approaches (enhanced identity governance, microsegmentation, network infrastructure
  and software-defined networking), ZTA logical components and data flows, trust algorithm inputs and
  design, ZTA deployment scenarios for enterprise and federated identity, threats to ZTA implementations,
  the CISA Zero Trust Maturity Model alignment, migrating from implicit-trust networks to zero trust,
  ZTA use cases for remote work and multi-cloud, subject and resource identification in zero trust,
  continuous validation and authorisation for each session, and preventing lateral movement through
  ZTA network segmentation.
---

# NIST SP 800-207 — Zero Trust Architecture (ZTA)

**Source**: NIST Special Publication 800-207, August 2020
**Full Title**: Zero Trust Architecture
**CSRC URL**: https://csrc.nist.gov/publications/detail/sp/800-207/final

---

## Zero Trust Definition

Zero trust is a set of guiding principles for system and network design where the guiding principle is: **implicit trust is never granted to any subject, asset, or workflow based solely on physical location, network location, or ownership**. All access requests are authenticated, authorised, and continuously validated before access is granted or retained.

Zero Trust Architecture (ZTA) is an enterprise cybersecurity architecture based on zero trust principles designed to prevent data breaches and limit internal lateral movement.

---

## The Seven Zero Trust Tenets

NIST SP 800-207 defines seven tenets that form the conceptual foundation for ZTA:

### Tenet 1 — All Data Sources and Computing Services Are Considered Resources
All devices (including personal devices), all applications, all services, all data stores — regardless of whether they are on-premises, in the cloud, or remote — are considered resources subject to ZTA policy. An enterprise-owned network is not automatically a safe zone.

### Tenet 2 — All Communication Is Secured Regardless of Network Location
Network location alone does not imply trust. All communication — whether on the enterprise network, across the internet, or between internal components — must be authenticated and encrypted. Being inside the firewall does not grant implicit trust.

### Tenet 3 — Access to Individual Enterprise Resources Is Granted on a Per-Session Basis
Trust in prior sessions does not carry over. Each access request to a resource is evaluated independently. Resources include applications, data stores, services, devices, and APIs.

### Tenet 4 — Access to Resources Is Determined by Dynamic Policy
Access decisions are made by examining the current state of the client identity, the application or service, the device health posture, and the requested resource. Policy is dynamic and includes observable state information at the time of access. Static, role-based access alone is insufficient.

### Tenet 5 — Integrity and Security Posture of All Owned and Associated Devices Is Monitored
The enterprise monitors the security posture of all devices — managed, unmanaged, user-owned — that access resources. Device compliance, patch level, and security configuration contribute to access decisions.

### Tenet 6 — All Resource Authentication and Authorisation Is Dynamic and Strictly Enforced
Authentication and authorisation are continually re-evaluated throughout the session. Reauthentication events may be triggered by changes in risk or context (e.g., change in location, elevated privilege request, anomalous behaviour detection). Long-standing sessions are not automatically maintained.

### Tenet 7 — The Enterprise Collects Information About the Current State of Assets, Network, and Communications and Uses It to Improve Security Posture
ZTA requires continuous collection of telemetry on user behaviour, device health, network traffic, and resource access. This information feeds the trust algorithm and the improvement of future policy decisions.

---

## ZTA Logical Components

NIST SP 800-207 defines the following core logical components:

### Policy Engine (PE)
The PE is responsible for the ultimate decision to grant, deny, or revoke access to a resource for a given subject. The PE uses enterprise policy and input from external sources (threat intelligence, identity providers, device compliance) to compute a trust score and make the access decision.

**PE Inputs used in the trust algorithm**:
- User/subject identity (from IdP)
- Device identity and health posture (from endpoint detection/MDM)
- Resource requested and its classification
- Behavioural analytics and historical access patterns
- Threat intelligence feeds
- Time of day, location, and network characteristics
- Privilege level required for the request

**PE Decisions**: Grant access, deny access, or grant with reduced privilege/additional verification.

### Policy Administrator (PA)
The PA executes the PE's decision by establishing or terminating communication between the subject and the resource. The PA communicates with the Policy Enforcement Point.

**PA Functions**:
- Generates session-specific credentials or tokens for the approved communication path
- Configures the network to allow the communication (sends signal to PEP)
- Tears down sessions when policy dictates

### Policy Enforcement Point (PEP)
The PEP is the mechanism that controls access to resources. It receives configuration from the PA and allows, denies, or terminates connections between subjects and resources.

**PEP Types**:
- Single-component PEP that handles both request interception and enforcement
- Split-component PEP: a client-side agent (initiating PEP) that communicates with an infrastructure-side PEP (terminating PEP)

**PEP Position**: Each enterprise resource must have a PEP. No resource is accessible without passing through a PEP that enforces ZTA policy.

### Supporting Components

| Component | Function |
|---|---|
| Continuous Diagnostics and Mitigation (CDM) System | Provides device posture data from managed assets |
| Industry Compliance System | Provides compliance information (FISMA status, SOC 2, etc.) |
| Threat Intelligence Feed(s) | Provides information about discovered vulnerabilities and known compromised identities |
| Network and System Activity Logs | Aggregated monitoring for behavioural analytics and anomaly detection |
| Data Access Policy | Rules governing what subjects can access what resources under what conditions |
| Enterprise PKI | Provides X.509 certificates to resources and subjects to establish identity |
| ID Management System (IdP/IAM) | Source of truth for identity information and authentication of subjects |
| Security Information and Event Management (SIEM) | Aggregates log data for monitoring and threat detection |

---

## Trust Algorithm

The trust algorithm (TA) is the process used by the PE to evaluate each access request and compute a trust level.

### Trust Algorithm Inputs
1. Access request (subject identity + device + resource + action)
2. Subject database (role, assignment, attributes, past behaviour)
3. Device database (device compliance, patch level, ownership status)
4. Subject/device behaviour analytics (deviation from baseline)
5. Threat intelligence (known compromised accounts, known malicious IPs)
6. Resource policy (data access policy, resource classification)

### Trust Algorithm Approaches

**Criteria-based (Boolean policy)**:
- Define explicit criteria that must ALL be met for access
- Example: User must be in the Security Administrator role AND device must be organisation-managed AND device must have MFA enabled AND no active threat indicators on the device
- Advantage: Predictable; easy to audit
- Limitation: May be too rigid for dynamic environments

**Score/confidence-based**:
- Assign trust scores to each input; combine into an overall trust score
- Access is granted if the score exceeds the threshold for the requested resource
- Allows partial signals to influence the decision without binary exclusions
- Advantage: More flexible; adaptive to partial information
- Limitation: More complex to design, tune, and explain

**Historical behaviour-based (ML)**:
- Model normal behaviour for each subject/device pair
- Flag anomalies as risk indicators that the TA considers
- Advantage: Detects insider threats and compromised credentials not caught by static criteria
- Limitation: Requires training period; risk of false positives; explainability challenges

---

## Three ZTA Deployment Approaches

NIST SP 800-207 describes three primary approaches to implementing ZTA in enterprise environments:

### Approach 1 — Enhanced Identity Governance (EIG)

**Concept**: The primary signal driving access decisions is the identity of the subject (user, service account). Resource access policy is defined based on identity attributes rather than network location.

**Key characteristics**:
- Strong, phishing-resistant authentication for all subjects (FIDO2, PIV, smart card)
- Identity as the primary perimeter
- All resources protected by identity-aware proxies or identity-aware access gateways
- Device identity used as a secondary signal

**Best suited for**:
- Organisations with mature identity and access management (IAM)
- Environments with a mix of on-premises and cloud resources
- Organisations leveraging SaaS extensively

**Implementation steps**:
1. Deploy a centralised, authoritative identity provider (IdP) for all users and service accounts
2. Enforce MFA for all access to enterprise resources (phishing-resistant for privileged access)
3. Integrate all resource access through identity-aware proxies (e.g., BeyondCorp-style proxy)
4. Implement device management/compliance signals as secondary inputs
5. Define access policy as identity-attribute-based rules in the PE
6. Monitor access decisions and continuously tune policy

### Approach 2 — Microsegmentation

**Concept**: Place security perimeters around individual workloads and resources. Each workload communicates only with the resources it explicitly needs to; all other traffic is denied by default.

**Key characteristics**:
- East-west traffic control (server-to-server within the same data centre or cloud environment)
- Workload identity is the basis for communication policy
- Software-based enforcement (does not require physical network segmentation)
- Dramatically limits lateral movement after initial compromise

**Implementation mechanisms**:
- Host-based agents (software enforced on each workload)
- Hypervisor-based segmentation (enforcement in the virtualisation layer)
- Cloud-native security groups and network ACLs (AWS Security Groups, Azure NSGs)

**Best suited for**:
- Data centre and cloud workload environments
- Organisations with complex east-west traffic patterns
- RansomWare mitigation and lateral movement prevention

**Implementation steps**:
1. Map all workload communication flows (what talks to what and on what ports)
2. Define communication policy: allow explicitly needed flows; deny all others (allowlist model)
3. Deploy microsegmentation enforcement (agent, hypervisor, or cloud-native)
4. Begin in monitoring mode to validate policy completeness before enforcement
5. Switch to enforcement mode starting with the most critical segments
6. Continuously monitor for policy violations and new communication patterns

### Approach 3 — Network Infrastructure and Software-Defined Networking (SDN)

**Concept**: Use SDN and network infrastructure changes to implement network access control aligned with ZTA. Access is controlled at the network level based on continuous assessment of device and user state.

**Key characteristics**:
- Dynamic network segmentation based on current context (not static VLANs)
- Software-defined perimeters (SDP) can create application-specific access tunnels
- Network access control (NAC) integrated with identity and device posture
- Software-Defined Perimeter (SDP) / Zero Trust Network Access (ZTNA) products

**Key technologies**:
- Software-Defined Perimeter (SDP): creates one-to-one encrypted network connections between subject and resource; resources are dark (not network-accessible) without a valid SDP session
- Zero Trust Network Access (ZTNA): commercial implementations of SDP-style access; user authenticates to a proxy; proxy grants access to specific resources
- SD-WAN with ZTA integration: dynamic routing based on security posture

**Best suited for**:
- Remote workforce environments
- Organisations replacing legacy VPN concentrators
- Multi-cloud environments requiring consistent network-layer access control

---

## ZTA Deployment Scenarios

### Scenario 1 — Employee Access to Enterprise Resources
Subject: Enterprise user on a managed laptop
ZTA implementation:
- User authenticates to IdP (Approach 1: EIG)
- Device posture verified (patch compliance, EDR agent active)
- PE grants access to specific applications based on role and device health
- PEP (identity-aware proxy or ZTNA product) enforces access
- No implicit access to other resources based on network position

### Scenario 2 — Remote Work and BYOD
Subject: Enterprise user on a personally owned device
ZTA implementation:
- User authenticates using phishing-resistant MFA
- Device posture is limited (unmanaged); device trust score is lower
- PE limits access to lower-sensitivity resources; blocks access to high-sensitivity resources from unmanaged device or requires VDI/cloud-based access
- PEP enforces the limited access grants

### Scenario 3 — Service Account / Workload-to-Workload
Subject: Application or service calling an API or accessing a data store
ZTA implementation:
- Service uses workload identity (certificate, OAuth client credentials, cloud IAM service account)
- PE evaluates workload identity + destination resource + time/request characteristics
- Microsegmentation (Approach 2) enforces that only the authorised workload can reach the target
- No standing network-level access; per-request authorisation

### Scenario 4 — Third-Party / Contractor Access
Subject: Non-enterprise user accessing a subset of enterprise resources
ZTA implementation:
- Federated identity from the third party's IdP (SAML or OIDC federation)
- Access scope strictly limited by policy; no lateral movement into enterprise network
- Session monitoring elevated; shorter session timeouts
- ZTNA product creates scoped access without providing network-level access

---

## Threats to ZTA Implementations

NIST SP 800-207 Section 4 identifies threats specific to ZTA:

| Threat | Description | Mitigation |
|---|---|---|
| Subversion of ZTA decision process | Compromising the PE, PA, or their communication channel gives the attacker control over all access decisions | High-availability PE/PA; integrity monitoring; privileged access management for ZTA admin functions |
| DoS attacks against ZTA components | Flooding the PE or PEP degrades availability of enterprise resources | Resilient, distributed PE/PA/PEP; rate limiting; CDN/DDoS protection for ZTA control plane |
| Stolen credentials / credential compromise | If the identity of a subject is compromised, ZTA grants access as if the legitimate user | Phishing-resistant MFA; behavioural analytics to detect anomalous access patterns; rapid credential revocation |
| Visibility and analytics gaps | If ZTA telemetry is incomplete, the trust algorithm cannot make informed decisions | Comprehensive log collection; SIEM integration; monitoring coverage for all PEPs |
| Network storage of ZTA data | Configuration data, policy, and logs could be targets for adversary exploitation | Encrypt ZTA configuration data; apply least privilege to ZTA administrative access |
| Compromised ZTA components | Supply chain attack against ZTA software components | C-SCRM practices (SP 800-161) for ZTA product acquisition; integrity verification before deployment |
| Insider threat | A legitimate user abusing granted access | Privilege separation; just-in-time access; user behaviour analytics; minimal standing access |

---

## ZTA and Implicit Trust Network Migration

Most enterprises operate legacy implicit-trust (castle-and-moat) networks. Migration is not instantaneous:

### Migration Phases

**Phase 1 — Identify and Inventory**
- Catalogue all subjects (users, service accounts)
- Catalogue all resources (applications, data stores, APIs, infrastructure)
- Map all communication flows between subjects and resources
- Identify trust dependencies (what relies on network location for trust)

**Phase 2 — Prioritise and Define Policy**
- Prioritise resources by sensitivity
- Define initial ZTA policy starting with the highest-sensitivity resources
- Begin with Approach 1 (EIG) for user-to-application access (quickest win)

**Phase 3 — Implement ZTA Controls Incrementally**
- Deploy strong authentication and IdP integration
- Implement ZTA access controls for selected high-priority resources
- Begin microsegmentation for critical workloads
- Run in monitor-only mode before enforcing

**Phase 4 — Expand and Refine**
- Extend ZTA coverage to all resources
- Enforce microsegmentation across all workloads
- Retire VPN/implicit trust network paths as ZTA coverage replaces them
- Continuously tune the trust algorithm based on operational experience

**Phase 5 — Steady State**
- All resource access through ZTA policy enforcement
- Continuous monitoring and telemetry feeding the trust algorithm improvement
- Regular policy review and update cycle aligned to threat intelligence

---

## CISA Zero Trust Maturity Model Alignment

CISA's Zero Trust Maturity Model (ZTMM) provides a five-pillar, four-stage framework aligned to NIST SP 800-207:

**Five Pillars**:
1. Identity
2. Devices
3. Networks
4. Applications and Workloads
5. Data

**Four Maturity Stages** (per pillar):
- Traditional: Perimeter-based, static controls, limited visibility
- Initial: Beginning implementation of zero trust-aligned controls
- Advanced: Dynamic access decisions, deeper automation
- Optimal: Fully dynamic, continuous, AI/ML-assisted access decisions

---

## Reference Files

- `references/zta-components.md` — Logical ZTA component detail, trust algorithm inputs, data flows, and deployment component diagrams
- `references/deployment-approaches.md` — Detailed implementation guidance for each of the three ZTA approaches with technology examples and step-by-step procedures
- `references/migration-guide.md` — ZTA migration planning, CISA ZTMM alignment, ZTA use cases, threat mitigation patterns, and integration with SP 800-53 controls

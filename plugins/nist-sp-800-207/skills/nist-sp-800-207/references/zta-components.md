# NIST SP 800-207 — ZTA Logical Components, Trust Algorithm, and Data Flows

**Source**: NIST SP 800-207, August 2020, Sections 3.1–3.3

---

## ZTA Logical Architecture

The ZTA logical architecture defines the components and data flows for all access decisions in a zero trust environment.

### Core Component Relationship

```
Subject/Device --> [PEP: Initiating] --> [PA] <--> [PE]
                                          |
Resource <---- [PEP: Terminating] <-------'
```

**Data flow for an access request**:
1. Subject (user or workload) requests access to a resource
2. The initiating PEP intercepts the request; passes it to the PA
3. The PA queries the PE with the access request context
4. The PE evaluates the request against policy using the trust algorithm
5. The PE returns the access decision (grant/deny/conditional) to the PA
6. If granted: the PA configures the terminating PEP to allow the specific communication; provides session credentials to the subject
7. The subject establishes a session with the resource through the configured PEP
8. The PE/PA monitor the session; can revoke if conditions change

---

## Policy Engine (PE) — Detailed

### PE Design Requirements

**Availability**: The PE is a single point of failure for enterprise access. Requirements:
- High-availability deployment (active-active or active-passive clustering)
- Geographic redundancy for large enterprises
- Defined degraded mode policy (fail-open vs. fail-closed; fail-closed is preferred for security; fail-open preferred for availability — document the choice explicitly)

**Isolation**: The PE must be heavily protected:
- Managed accounts for PE administration; MFA required for all PE admin access
- PE configuration stored encrypted with access limited to PE system itself and designated administrators
- Audit logging of all PE configuration changes, all access decisions, and all admin actions

**Scalability**: The PE must evaluate access requests at the speed of enterprise operations:
- Caching of trust evaluations for unchanged context (time-bounded cache; re-evaluate on credential change or device state change)
- Distributed PE processing when single-node performance is insufficient

### Trust Algorithm Input Sources and Trust Score Mapping

| Input Source | Data Provided | Trust Impact |
|---|---|---|
| Identity Provider (IdP) | Authentication event, assurance level (AAL1/2/3), MFA method used | High weight: AAL3 (phishing-resistant) > AAL2 > AAL1 |
| Device compliance (MDM/EDR) | Patch level, encryption status, EDR agent active, jailbreak/root status | High weight for managed devices; lower weight for unmanaged |
| Behavioural analytics | Deviation from typical access time, location, resources accessed | Anomalies reduce trust; normal patterns increase trust |
| Threat intelligence feeds | Known compromised accounts, malicious IP reputation, active IOCs | Known compromise = deny; clean record = neutral |
| Resource classification | Data sensitivity level, regulatory scope | Sensitive = higher required trust score |
| Time/location context | Time of access, geo-location, network (corporate vs. public) | Contextual risk factors (off-hours + unusual location = reduced trust) |
| Previous session history | Prior access in this session; privilege escalation requests | Recent escalation requests increase scrutiny |

### PE Decision Outputs

**Grant**: Subject is permitted to access the resource. PA configures PEP accordingly. Session duration and re-evaluation interval are specified in the decision.

**Grant with condition**: Access is granted subject to additional verification (e.g., step-up authentication). PA does not configure PEP until condition is met.

**Deny**: Access is denied. PA does not configure PEP. The denial event is logged.

**Quarantine/investigate**: An anomaly warrants investigation. Access may be denied pending review, or limited to low-sensitivity resources pending investigation.

---

## Policy Administrator (PA) — Detailed

### PA Functions

**Session establishment**:
- Receives grant decision from PE
- Generates per-session credentials (tokens, certificates, temporary network paths)
- Configures the terminating PEP to allow the specific subject-to-resource communication
- Sets time-to-live (TTL) on the session per policy

**Session maintenance**:
- Receives updates from PE on changes to trust conditions
- Revokes or modifies session if PE issues a revocation or downgrade instruction
- Sends keepalive/re-evaluation triggers to PE before session TTL expires

**Session termination**:
- Tears down PEP configuration when session ends (user logs out, TTL expires, or PE revokes)
- Revokes session credentials

### PA Security Requirements
- PA communicates with PE over an authenticated, encrypted channel (mutual TLS)
- PA must authenticate to each PEP using strong credentials
- PA configuration and session records protected against tampering
- Redundant PA deployment aligned with PE availability requirements

---

## Policy Enforcement Point (PEP) — Detailed

### PEP Types

**Inline PEP (single component)**:
All traffic between subject and resource passes through the PEP. The PEP forwards allowed traffic and drops denied traffic.
- Typically an identity-aware proxy, reverse proxy, or ZTNA gateway
- Subject has no direct network path to the resource; all traffic goes through PEP
- Examples: cloud-native identity-aware proxy, ZTNA service, application gateway with identity integration

**Split-component PEP**:
An agent on the subject device (client-side PEP) communicates with a server-side PEP.
- The client-side agent establishes the ZTA session; ensures device posture is reported
- The server-side PEP enforces access to the resource
- Used in ZTNA products where a client agent is deployed on managed devices
- Enables device posture to be included in each access request natively

**Resource-native PEP**:
The resource itself performs enforcement (API gateway, service mesh sidecar proxy).
- Common in microservices architectures using service meshes (e.g., Envoy sidecar)
- Provides workload-to-workload zero trust through mutual TLS + identity verification

### PEP Coverage Requirement

ZTA requires that **every resource** be protected by a PEP. A resource accessible without passing through a PEP represents a zero trust gap. The PEP coverage audit is a key ZTA implementation validation step.

**PEP coverage audit procedure**:
1. Enumerate all resources (using asset inventory)
2. For each resource: verify that network traffic cannot reach the resource without passing through a configured PEP
3. Document any gaps and create remediation plans
4. Re-audit after any infrastructure change

---

## ZTA Data Plane and Control Plane

ZTA separates the data plane (actual communication between subject and resource) from the control plane (access decision and enforcement configuration):

**Control plane**: PE, PA, and the communication channel between them and to PEPs. Must be highly secured and separately monitored.

**Data plane**: Communication between the subject and the resource, flowing through the PEP. The data plane is configured by the control plane.

**Security implication**: If the control plane is compromised (PE or PA), the entire ZTA is compromised. The control plane requires the highest level of protection in the enterprise.

---

## Supporting Infrastructure Components — Implementation Details

### Identity Provider (IdP)

| Requirement | Description |
|---|---|
| Authoritative source | Single authoritative IdP, or federation of trusted IdPs with clear trust hierarchy |
| MFA enforcement | MFA required for all enterprise resource access; phishing-resistant MFA (FIDO2/WebAuthn, PIV) for privileged access |
| Assurance levels | IdP must be capable of asserting authentication assurance level (AAL) per SP 800-63B |
| Continuous session | IdP must support session revocation and token revocation to enable ZTA session termination |
| Attributes | IdP must assert role, group membership, and other attributes needed by the PE trust algorithm |
| Federation | Support SAML 2.0 and OpenID Connect/OAuth 2.0 for federated enterprise and third-party identity |

### Device Identity and Compliance

| Requirement | Description |
|---|---|
| Device identity | Each managed device has a cryptographic identity (certificate from enterprise PKI or device attestation from TPM) |
| MDM/EDM integration | Device compliance data (patch level, encryption, EDR status) fed to PE in real time or near-real time |
| Unmanaged devices | Policy must address unmanaged (BYOD) devices: typically permit access only to lower-sensitivity resources or via isolated VDI |
| Device health check | At each access request, device health data must be current (not stale cache older than the defined maximum) |

### Behavioural Analytics

| Requirement | Description |
|---|---|
| Baseline establishment | Establish baseline of normal access patterns per user, per role, per device over a learning period |
| Anomaly detection | Flag: unusual time of access, unusual resource access, unusual geographic location, unusual volume of access, credential sharing indicators |
| Feed to PE | Anomaly scores fed to PE as a trust input; anomaly does not necessarily deny access but reduces trust score |
| Tuning | Analyst review of flagged anomalies to reduce false positives; tune model based on confirmed benign vs. malicious events |

---

## ZTA Component Inventory Template

Use this inventory to document ZTA component deployment:

| Component | Product/Technology | Version | Deployment Location | High Availability | Integration Status |
|---|---|---|---|---|---|
| Policy Engine | [Product] | [Version] | [On-prem / Cloud / SaaS] | [Active-Active / Active-Passive / None] | [Complete / Partial / Planned] |
| Policy Administrator | [Product] | [Version] | [Location] | [HA status] | [Integration status] |
| PEP — User Access | [Product] | [Version] | [Location] | [HA status] | [Status] |
| PEP — Workload | [Product] | [Version] | [Location] | [HA status] | [Status] |
| Identity Provider | [Product] | [Version] | [Location] | [HA status] | [Status] |
| Device Compliance | [MDM/EDR product] | [Version] | [Location] | [HA status] | [Status] |
| SIEM | [Product] | [Version] | [Location] | [HA status] | [Status] |
| Threat Intel Feed | [Source] | N/A | [Integration point] | N/A | [Status] |
| Behavioural Analytics | [Product] | [Version] | [Location] | [HA status] | [Status] |

---

## ZTA Coverage Gap Assessment

| Resource | PEP Protected | Identity Auth Required | Device Posture Checked | Behavioural Analytics | Gap | Remediation Plan |
|---|---|---|---|---|---|---|
| [Application name] | Yes / No | Yes / No | Yes / No | Yes / No | [List gaps] | [Plan] |

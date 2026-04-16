# NIST SP 800-207 — ZTA Deployment Approaches: Implementation Guidance

**Source**: NIST SP 800-207, August 2020, Section 5

---

## Approach 1 — Enhanced Identity Governance (EIG)

### Overview

The EIG approach treats identity as the primary security perimeter. All enterprise resources are protected by identity-aware access controls. Access decisions are driven by the quality and attributes of the identity assertion rather than network location. This is often the most practical starting point for organisations adopting ZTA.

### Implementation Steps

**Step 1 — Centralise and Harden Identity**

Establish or consolidate to a single authoritative Identity Provider:
- All user accounts, service accounts, and machine identities managed in one IdP (or federated IdPs with a clear trust hierarchy)
- Implement phishing-resistant MFA for all access to enterprise resources
  - For privileged accounts: FIDO2/WebAuthn hardware keys or PIV/CAC required
  - For standard users: FIDO2, authenticator apps acceptable; SMS is not recommended
- Implement passwordless authentication where possible (FIDO2 passkeys)
- Enable and enforce conditional access policies in the IdP

**Step 2 — Inventory All Resources and Define Access Policy**

- Enumerate all enterprise applications, APIs, and data stores
- Classify each resource by sensitivity (Low/Moderate/High aligned to FIPS 199)
- For each resource, define the identity attributes required for access:
  - Example: Application X requires: role = SecurityAnalyst AND department = SOC AND device = managed AND AAL >= 2
- Document the access policy in the PE or in a policy management tool

**Step 3 — Deploy Identity-Aware Access Gateway or Proxy**

Deploy an identity-aware proxy that sits in front of each resource (or group of resources):
- The proxy is the PEP; it intercepts all access requests
- The proxy authenticates the user against the IdP for every session
- The proxy evaluates the session's identity attributes against the resource policy
- If the session meets policy requirements: the proxy forwards the request to the resource
- If not: the proxy returns a denial or redirects to step-up authentication

Technology options:
- Cloud-native identity-aware proxies (BeyondCorp Enterprise, Azure AD Application Proxy, AWS Verified Access)
- Web Application Firewalls with identity integration (WAF + IdP integration)
- API gateways with JWT/OAuth 2.0 enforcement

**Step 4 — Integrate Device Posture**

Device health should be a secondary signal in the trust decision:
- Deploy MDM and/or endpoint detection and response (EDR) to managed devices
- Configure the IdP or access gateway to query device compliance status at authentication time
- Define policy: if device is not managed or is non-compliant, limit access to lower-sensitivity resources
- For user-owned devices: require access through a VDI/browser-based solution that does not land data on the unmanaged device

**Step 5 — Implement Session Revocation**

ZTA requires the ability to revoke a session immediately when conditions change:
- Enable token revocation in the IdP (OAuth 2.0 token revocation, SAML session termination)
- Integrate the PE with the IdP so that a PE-initiated revocation immediately terminates the token
- Test the revocation path to confirm it terminates active sessions within a defined time window

**Step 6 — Enable Continuous Monitoring**

- Log all access decisions (grant, deny, step-up required) to SIEM
- Alert on policy violations and anomalous access patterns
- Periodically review access policies and prune over-privileged role assignments
- Conduct quarterly access reviews for privileged roles

---

## Approach 2 — Microsegmentation

### Overview

Microsegmentation creates individually secured segments around each workload. Communication between workloads is permitted only if explicitly allowed by policy; all other traffic is denied by default. This approach directly limits east-west lateral movement and is critical for data centre and cloud workload security.

### Implementation Steps

**Step 1 — Map All Workload Communication Flows**

This step is often the most time-consuming and critical:
- Use network traffic analysis tools to capture all east-west and north-south flows for a sufficient baseline period (two to four weeks minimum for most environments)
- Document: source workload, destination workload, protocol, port, business justification
- Include: application-to-database flows, application-to-middleware, monitoring agent flows, logging flows, backup agent flows
- Identify and document all flows that cannot be explained; investigate before creating allowlist rules

**Step 2 — Design the Segmentation Policy**

- Define workload identities (labels, tags, or host-based attributes)
- Define policy groups (segments) based on function, sensitivity, or data classification
  - Example segments: web tier, application tier, database tier, management/bastion, monitoring
- Define allowed flows between segments (minimum necessary communication principle)
- Explicitly deny all other inter-segment communication

**Step 3 — Select Enforcement Mechanism**

| Mechanism | Technology | Best For |
|---|---|---|
| Host-based agent | Illumio, Guardicore (Akamai Guardicore), Cisco Secure Workload | Heterogeneous environments; bare metal and VM |
| Hypervisor-based | VMware NSX, AWS Security Groups (for EC2) | Virtualised data centres, single hypervisor environments |
| Cloud-native | AWS Security Groups, Azure NSGs, Google Cloud Firewall Rules | Cloud-native workloads in a single CSP |
| Service mesh | Istio/Envoy, Linkerd | Containerised microservices (Kubernetes) |

**Step 4 — Deploy in Monitor-Only Mode**

Before enforcement:
- Deploy the selected mechanism in visibility/monitoring mode
- Verify that the captured flow map matches the actual observed traffic
- Identify any flows not in the policy that are needed for operations (missing legitimate flows)
- Update the policy to add any missing legitimate flows
- Confirm with application owners that the planned policy is complete

**Step 5 — Enable Enforcement — Staged**

Enable enforcement incrementally to minimise operational impact:
- Stage 1: Enable enforcement for the most critical segments (database tier, sensitive data stores)
- Monitor for policy violations (blocked flows); investigate and resolve
- Stage 2: Extend enforcement to application tier
- Continue rolling out enforcement segment by segment

**Step 6 — Maintain and Monitor**

- Alert on any blocked east-west traffic (every deny event should be reviewed)
- Update the segmentation policy when application changes require new communication paths
- Periodically re-run the traffic baseline analysis to identify new flows (after major application changes)
- Include segmentation policy review in change management for application deployments

---

## Approach 3 — Software-Defined Networking (SDN) and Software-Defined Perimeter (SDP)

### Overview

This approach uses network infrastructure capabilities — SDN, ZTNA products, software-defined perimeters — to implement dynamic access control at the network level. It is particularly effective for remote workforce access, replacing legacy VPN, and multi-cloud access control.

### Software-Defined Perimeter (SDP) Architecture

SDP makes enterprise resources invisible to unauthorised users. A client must authenticate before the resource is even reachable (pre-authentication darkness):

1. Client sends authentication request to the SDP Controller (serves as both PE and PA)
2. Controller verifies identity (IdP) and device posture
3. If approved: Controller instructs the SDP Gateway (PEP) to allow the client's specific IP/token
4. Controller provides the client with the gateway address and session token
5. Client establishes an encrypted tunnel to the gateway
6. Gateway forwards only authenticated, authorised traffic to the resource

**Key SDP property**: The resource is not exposed on any network until the client is authenticated. There is no DNS or IP address to scan; reconnaissance is blocked.

**Standards**: SDP is defined by the Cloud Security Alliance (CSA) SDP Specification.

### Zero Trust Network Access (ZTNA) Products

ZTNA products are commercial implementations of SDP-style access. They replace legacy VPN concentrators:

| Feature | Legacy VPN | ZTNA |
|---|---|---|
| Network access | Full network segment access after authentication | Per-application or per-resource access only |
| Device posture check | Typically minimal or at connection only | Continuous device posture evaluation |
| Lateral movement | Broad access enables lateral movement | Per-resource access prevents lateral movement |
| Visibility | Limited in-tunnel visibility | Full access event logging to SIEM |
| User experience | Tunnel-based (can be slow; split tunnel issues) | Direct-to-resource access often faster |
| Resource visibility | Resources exposed to authenticated network | Resources dark; not reachable without ZTNA session |

**ZTNA deployment models**:
- Agent-based: Client agent on device participates in every access request; provides richer device posture data
- Agentless: Browser-based; no agent required; limited device posture data; suited for BYOD and contractor access

### SDN-Based Dynamic Segmentation

In SDN environments, the network fabric can be programmatically reconfigured to reflect current access policy:
- SDN controller receives access decisions from PE/PA
- SDN controller dynamically provisions network paths for approved sessions
- No static VLANs or ACLs; all network paths are provisioned on-demand
- Reduces attack surface since no persistent network paths exist

### Implementation Steps for ZTNA Deployment

1. **Define access scope**: Identify the resources that will be protected by ZTNA (start with remote access use case)
2. **Select ZTNA product**: Evaluate against requirements (agent-based vs. agentless, IdP integration, device posture, SIEM integration)
3. **Configure connectors**: Deploy ZTNA connectors near each protected resource or application group
4. **Define access policy in ZTNA**: Map users/groups to applications using the ZTNA policy engine
5. **Pilot**: Deploy to a subset of users; validate access, performance, and logging
6. **Roll out**: Expand to all remote users; decommission legacy VPN concentrators for covered resources
7. **Monitor**: Review access logs; alert on anomalous access patterns; tune policy

---

## Hybrid Approaches

Most real-world ZTA implementations combine elements of all three approaches:

| Layer | Approach Applied |
|---|---|
| User-to-Application (remote) | Approach 3 — ZTNA replaces VPN |
| User-to-Application (on-premises) | Approach 1 — EIG: identity-aware proxy, IdP-driven policy |
| Workload-to-Workload | Approach 2 — Microsegmentation: service mesh or agent-based |
| Privileged Access | Approach 1 + 3 — EIG with phishing-resistant MFA + ZTNA/PAM for privileged sessions |
| Data-Layer | Approach 1 — Attribute-based access control at the data service level |

The recommended sequence for most federal agencies:
1. Start with Approach 1 (EIG) — deploy strong authentication and identity-aware access for the highest-priority applications
2. Simultaneously pursue Approach 2 (microsegmentation) for the highest-criticality workloads
3. Add Approach 3 (ZTNA) to replace legacy VPN for remote access
4. Expand coverage iteratively until all resources are under ZTA policy

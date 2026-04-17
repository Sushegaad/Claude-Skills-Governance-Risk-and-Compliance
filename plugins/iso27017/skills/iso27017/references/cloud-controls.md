# ISO/IEC 27017:2015 — Cloud-Specific Controls (CLD)

ISO/IEC 27017:2015 introduces 7 additional controls not present in ISO/IEC 27002:2013. These
controls are prefixed with "CLD" and address security aspects unique to cloud computing
environments. They are intended to be implemented alongside the base ISO 27002 controls.

---

## CLD.6.3.1 — Shared Roles and Responsibilities Within a Cloud Computing Environment

**Category**: Organisation of Information Security (extends ISO 27002 clause 6)
**Applicability**: Both CSP and CSC

### Purpose
Ensure that the allocation of information security responsibilities between the cloud service
provider and cloud service customer is clearly defined, agreed, and communicated, so that no
security obligations go unaddressed.

### The Problem This Solves
Without explicit shared responsibility documentation, both the CSP and CSC may assume the other
party is managing a given control, resulting in security gaps. This is one of the most common
causes of cloud security incidents.

### CSP Implementation Requirements
- Publish and maintain a clear description of the information security responsibilities that
  remain with the CSC versus those managed by the CSP
- Make this responsibility breakdown available as part of the service documentation and cloud
  service agreement (CSA)
- Distinguish responsibilities by service model (IaaS, PaaS, SaaS) where different services
  are offered
- Update the responsibility documentation when service features or security capabilities change
- Provide the CSC with sufficient information to implement the responsibilities that fall to them

### CSC Implementation Requirements
- Review and formally acknowledge the CSP's shared responsibility documentation
- Document the specific security controls the CSC is responsible for implementing
- Create an internal RACI that maps ISO 27017 / ISO 27002 controls to the CSP-provided breakdown
- Include shared responsibility provisions in any internal security policy that references
  cloud services
- Reassess the shared responsibility model when changing cloud service tier, provider, or scope

### Cloud Service Agreement Provision Required
The CSA must include a clause that explicitly identifies which information security obligations
rest with the CSP, which rest with the CSC, and which are shared. This must be specific, not
a general disclaimer.

### Evidence Required for Audit
- Shared responsibility matrix or documentation (published by CSP, acknowledged by CSC)
- CSA clause explicitly defining security obligations of each party
- Internal CSC RACI or control ownership register mapped to cloud controls
- Evidence of CSC review and acceptance of the responsibility breakdown

### Common Pitfalls
- Assuming the CSP's generic Terms of Service constitutes a shared responsibility agreement
- Not reviewing shared responsibility when moving between IaaS and SaaS
- CSC assuming the CSP manages access control (CSC always owns IAM for user accounts)
- No formal CSC process to acknowledge and act on the CSP responsibility split

---

## CLD.8.1.5 — Removal or Return of Cloud Service Customer Assets

**Category**: Asset Management (extends ISO 27002 clause 8.1)
**Applicability**: Both CSP and CSC

### Purpose
Ensure that when a cloud service is terminated, or when assets (including data) belonging to the
CSC need to be transferred or deleted, this is performed completely, verifiably, and in a
format the CSC can use.

### CSP Implementation Requirements
- Provide the CSC with the technical capability to retrieve all its data in a usable, standard
  format before and during service termination
- Define a documented procedure for the return of CSC assets, covering: the format of data
  export, the timeline, and the method of delivery
- After confirmed successful retrieval by the CSC, securely delete all copies of the CSC's
  data from all CSP systems (including backups and replicated copies)
- Issue a certificate of destruction or deletion on request
- Communicate the data return and deletion procedure to the CSC in the CSA
- Specify the retention period for CSC data after service termination and what happens upon
  expiry of that period

### CSC Implementation Requirements
- Maintain an inventory of all data and assets stored with the CSP
- Document the procedure for retrieving assets from each CSP in use
- Include data return and deletion provisions in every cloud service agreement
- Verify, prior to terminating a service, that all required data has been retrieved and
  validated
- Obtain and retain written confirmation (certificate of deletion) from the CSP that data has
  been destroyed
- Ensure the data retrieval format is compatible with the CSC's systems or import capabilities

### Cloud Service Agreement Provision Required
The CSA must specify:
- The format in which data will be returned to the CSC
- The timeline for data return following termination notice
- The method and timeline for confirmed deletion of CSC data
- Whether backups and archived copies are included in deletion
- Responsibility for migration costs

### Evidence Required for Audit
- CSA clause covering data return and deletion
- CSP data deletion procedure documentation
- CSC data retrieval test records
- Certificate of destruction for any terminated service
- CSC asset inventory showing data stored with cloud providers

### Common Pitfalls
- Assuming data stored in cloud is automatically deleted when an account is closed
- Not verifying deletion of backup or archived copies
- Data locked in proprietary formats that cannot be exported
- No clause in CSA defining the timeline for data deletion after termination
- CSC retaining data with a CSP after service termination without documented justification

---

## CLD.9.5.1 — Segregation in Virtual Computing Environments

**Category**: Access Control (extends ISO 27002 clause 9.4 — multi-tenancy context)
**Applicability**: CSP (primary); CSC (where managing their own multi-tenant environments)

### Purpose
Ensure that the virtual computing resources of different cloud service customers (tenants) are
isolated from each other, and from the CSP's own management infrastructure, so that one
tenant cannot access, disrupt, or observe another tenant's data or operations.

### The Multi-Tenancy Risk
In multi-tenant cloud environments, multiple customers share the same underlying physical
infrastructure. Without proper isolation, a vulnerability in the virtualisation layer
(hypervisor, virtual network, or storage) could allow one tenant to access another's data.

### CSP Implementation Requirements
- Implement logical isolation between all tenants at every layer: compute (hypervisor / VM),
  storage, and network virtualisation
- Use hypervisor-level isolation to prevent VMs belonging to different tenants from accessing
  each other's memory, storage, or CPU resources
- Implement virtual network segmentation (VLANs, SDN, or overlay networks) to prevent
  inter-tenant network traffic
- Apply access controls ensuring CSP administrators cannot access tenant data without
  authorisation and audit trail
- Conduct regular security testing (including penetration testing) of virtualisation and
  isolation mechanisms
- Apply patches to hypervisors and virtualisation platforms promptly, particularly for
  vulnerabilities that could enable VM escape
- Document the isolation architecture and make architecture summaries available to CSCs
  (without disclosing details that would assist attackers)
- Implement storage isolation to prevent one tenant's data being accessible from another
  tenant's storage volumes

### Evidence Required for Audit
- Virtual environment architecture documentation showing isolation design
- Hypervisor patch management records
- Penetration testing reports covering virtualisation boundary testing
- Access control records for CSP administrator access to tenant environments
- Network segmentation diagrams showing tenant isolation

### Common Pitfalls
- Misconfigured hypervisors that allow VM-escape or cross-tenant memory access
- Shared storage volumes without encryption or access boundary enforcement
- Failure to patch hypervisors promptly when virtualisation vulnerabilities are disclosed
- CSP administrators having broad access to all tenant data without role-based restrictions
- Insufficient testing of isolation mechanisms after infrastructure changes

---

## CLD.9.5.2 — Virtual Machine Hardening

**Category**: Access Control / Operations Security (extends ISO 27002 clause 9 and 12)
**Applicability**: Both CSP and CSC

### Purpose
Ensure that virtual machines (VMs) are configured securely to minimise the attack surface and
reduce the risk of compromise within the cloud environment.

### CSP Implementation Requirements (for CSP-managed VMs and base images)
- Develop and maintain hardened base images for any VMs or images provided to CSCs
- Ensure hardened images include: unnecessary services and ports disabled, security patches
  applied, secure default configurations, logging enabled
- Provide guidance to CSCs on hardening VMs that CSCs deploy
- Apply VM hardening standards to CSP's own management and infrastructure VMs
- Monitor for CSC-deployed VMs that deviate significantly from hardening baselines
  (where technically and contractually possible)

### CSC Implementation Requirements (for CSC-managed VMs)
- Develop and enforce a VM hardening standard covering:
  - Removal or disabling of unnecessary operating system features and services
  - Application of all available security patches before and after deployment
  - Firewall and host-based intrusion detection configuration
  - Enabled audit logging for security events
  - Encrypted storage volumes for sensitive data
  - Disabled or changed default credentials
  - Use of approved and hardened OS images as baselines
- Apply the hardening standard to all CSC-deployed VMs before they are connected to
  production networks
- Re-apply hardening during major OS or application updates
- Conduct periodic vulnerability scanning of deployed VMs
- Remediate identified vulnerabilities within risk-based timescales

### Evidence Required for Audit
- VM hardening standard document
- Evidence of hardening applied to production VMs (configuration baseline comparison)
- Vulnerability scanning results and remediation records
- Patch management records for VM operating systems
- Base image management records (CSP-side)

### Common Pitfalls
- Deploying community cloud images without reviewing their security configuration
- Not disabling default credentials on newly deployed VMs
- VMs with open management ports (SSH, RDP) exposed to the public internet
- Snapshot-based recovery that restores a VM to a pre-patch state
- No periodic re-assessment of hardening compliance on running VMs

---

## CLD.12.1.5 — Administrator's Operational Security

**Category**: Operations Security (extends ISO 27002 clause 12.1)
**Applicability**: CSP (primary); applicable to CSC administrators managing cloud resources

### Purpose
Ensure that cloud service administrator activities are performed under strict operational
security controls to prevent accidental or malicious misuse of privileged access to cloud
infrastructure and tenant data.

### CSP Implementation Requirements
- Implement multi-factor authentication (MFA) for all cloud service administrator accounts
- Apply the principle of least privilege: each administrator account is granted only the
  access required for their specific role
- Implement role-based access control (RBAC) separating administrative functions
  (e.g., separate roles for: infrastructure admin, security admin, customer support admin)
- Ensure all administrative activities are fully logged, including: login/logout events,
  privileged commands executed, data accessed, configuration changes made
- Protect administrator logs from modification or deletion by the administrators themselves
- Implement a separate, hardened management network or jump server for administrative access
  to cloud infrastructure; production systems should not be administered from general user
  networks
- Require formal approval and documented authorisation for any administrative access to
  customer (CSC) data or environments
- Conduct periodic review and recertification of administrator access rights
- Train administrators in secure operational practices and social engineering awareness

### CSC Implementation Requirements
- Apply equivalent privileged access controls for CSC cloud administrators
- Enforce MFA for all CSC user accounts with administrative privileges in cloud environments
- Implement just-in-time (JIT) access or time-limited privilege elevation where possible
- Audit administrator activities in cloud management consoles

### Evidence Required for Audit
- MFA enforcement records for administrator accounts
- RBAC configuration showing least privilege assignment
- Administrator access logs with evidence of protection from tampering
- Access approval records for customer data access
- Management network / jump server architecture documentation
- Access recertification records

### Common Pitfalls
- Shared administrator accounts (no individual accountability)
- Administrator access to production environments from developer or general workstations
- Absence of MFA on highly privileged accounts
- Administrator logs that can be cleared by the same administrators being logged
- No requirement for formal approval before a CSP administrator accesses a CSC environment
- Excessive standing/permanent privileged access rather than just-in-time access

---

## CLD.12.4.5 — Monitoring of Cloud Services

**Category**: Operations Security (extends ISO 27002 clause 12.4)
**Applicability**: Both CSP and CSC

### Purpose
Ensure that cloud services are monitored to detect security-relevant events, operational
anomalies, and performance issues, and that monitoring information is made available to the
CSC as required.

### CSP Implementation Requirements
- Implement comprehensive monitoring of the cloud service covering: availability, performance,
  capacity, security events (authentication failures, anomalous access patterns, privilege
  escalation), and infrastructure health
- Ensure that security event monitoring is continuous and automated
- Retain monitoring logs for a period defined in the CSA and consistent with applicable
  regulatory requirements
- Make available to the CSC, on request or via self-service dashboards, monitoring data
  related to the CSC's use of the service, including security events affecting the CSC
- Define and communicate to the CSC: what is monitored, what events will generate alerts, and
  what information will be proactively reported versus available on request
- Include monitoring provisions in the CSA

### CSC Implementation Requirements
- Implement monitoring of the CSC's own use of cloud services, including:
  - User account activity and authentication events
  - Data access patterns and anomalous queries
  - Configuration changes to cloud resources
  - API call volumes and unusual patterns
- Integrate CSP-provided monitoring feeds with the CSC's own security information and event
  management (SIEM) system where available
- Define alerts and thresholds for cloud-specific events (e.g., unusual data export volumes,
  privilege changes, new admin account creation)
- Review monitoring reports from the CSP at scheduled intervals and upon security incidents
- Retain CSC-side monitoring data for a period consistent with the CSC's incident response
  and regulatory requirements

### Evidence Required for Audit
- CSP monitoring architecture and description of what is monitored
- CSA clause defining monitoring data availability to the CSC
- CSP monitoring reports or dashboard access records
- CSC SIEM integration or monitoring configuration for cloud services
- CSC alert configuration and review records

### Common Pitfalls
- CSC assuming the CSP monitors all security events relevant to the CSC
- No integration between CSP-provided logs and the CSC's internal SIEM
- Cloud API activity logs (e.g., AWS CloudTrail, Azure Activity Log) not enabled by the CSC
- CSP monitoring log retention period shorter than the CSC's incident investigation window
- No process for the CSC to request specific monitoring data from the CSP

---

## CLD.13.1.4 — Alignment of Security Management for Virtual and Physical Networks

**Category**: Communications Security (extends ISO 27002 clause 13.1)
**Applicability**: CSP (primary)

### Purpose
Ensure that the security controls applied to virtual networks in a cloud environment are
consistent with (and aligned to) the security controls applied to physical networks, so that
the introduction of virtualisation does not reduce the overall network security posture.

### CSP Implementation Requirements
- Define network security policies that explicitly cover both physical and virtual network
  layers
- Apply equivalent security controls to virtual networks as are required for physical networks,
  including: network segmentation, traffic filtering (firewalls/ACLs), intrusion detection,
  flow logging, and access controls
- Ensure virtual network security configurations are subject to the same change management
  and security review processes as physical network changes
- Implement traffic inspection and filtering between virtual network segments, including
  east-west (inter-VM) traffic within the same virtual network where applicable
- Maintain visibility of virtual network topology to the same degree as physical network
  topology (network documentation and asset inventory)
- Audit virtual network security configurations periodically against the security policy
- Ensure that virtual networks cannot be created or reconfigured in ways that bypass
  established security controls (e.g., VMs directly bridging to external networks)

### CSC Considerations
- Where the CSC configures virtual networks (e.g., in IaaS), apply equivalent security
  controls to those used in the CSC's physical network environment
- Use cloud-native network security features (security groups, network ACLs, virtual firewalls)
  to implement network segmentation equivalent to physical environment controls
- Review virtual network security configurations regularly and when architecture changes occur

### Evidence Required for Audit
- Network security policy covering both physical and virtual layers
- Virtual network architecture and configuration documentation
- Evidence of change management applied to virtual network configuration changes
- Audit results for virtual network security configurations
- Traffic logging and inspection evidence for virtual network segments

### Common Pitfalls
- Assuming default virtual network configurations are secure
- No firewall rules applied between virtual machine segments on the same virtual network
- Virtual network changes bypassing the change management process
- VMs able to create new virtual network interfaces without security review
- No logging of virtual network traffic flows (equivalent to physical NetFlow/sFlow monitoring)
- CSC creating "flat" virtual networks with no internal segmentation

---

## Summary Reference Table

| Control ID | Name | CSP | CSC | Key Requirement |
|------------|------|-----|-----|-----------------|
| CLD.6.3.1 | Shared roles and responsibilities | Required | Required | Documented shared responsibility; CSA clause |
| CLD.8.1.5 | Removal or return of assets | Required | Required | Data return format; certified deletion |
| CLD.9.5.1 | Segregation in virtual environments | Required | N/A (unless multi-tenant CSC) | Hypervisor/network tenant isolation |
| CLD.9.5.2 | Virtual machine hardening | Required (base images) | Required (CSC VMs) | Hardening standard; patch management |
| CLD.12.1.5 | Administrator's operational security | Required | Recommended | MFA; least privilege; admin logging |
| CLD.12.4.5 | Monitoring of cloud services | Required | Required | Monitoring provision; CSC data access |
| CLD.13.1.4 | Virtual/physical network alignment | Required | Recommended | Consistent controls across both layers |

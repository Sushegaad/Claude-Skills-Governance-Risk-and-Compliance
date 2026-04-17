# ISO/IEC 27017:2015 — ISO 27002 Controls with Cloud-Specific Guidance

ISO/IEC 27017:2015 provides additional implementation guidance for 37 controls from
ISO/IEC 27002:2013, tailored for cloud computing environments. For each applicable control,
guidance is provided from both the Cloud Service Provider (CSP) and Cloud Service Customer
(CSC) perspectives.

The control numbering follows ISO/IEC 27002:2013 (the version this standard is based on).

---

## Domain 5 — Information Security Policies

### 5.1.1 — Policies for Information Security

**CSP Guidance**
- Develop and publish cloud-specific information security policies that address the unique
  characteristics of the cloud environment
- Policies must cover: multi-tenancy, virtualisation security, data sovereignty, third-party
  sub-service provider management, and shared responsibility
- Make a summary of the security policy available to CSCs as part of service documentation

**CSC Guidance**
- Update existing information security policies to explicitly address the use of cloud services
- Include provisions for: approved cloud service use, data classification before cloud upload,
  identity and access management in cloud environments, and monitoring of cloud activity
- Ensure policies are reviewed when new cloud services are adopted or existing services change

---

### 5.1.2 — Review of the Policies for Information Security

**CSP Guidance**
- Trigger policy review when there are significant changes to the cloud service architecture,
  new regulatory requirements applicable to cloud, or major security incidents

**CSC Guidance**
- Include review triggers for changes in cloud service providers, changes in service scope,
  and new regulatory requirements affecting cloud-stored data

---

## Domain 6 — Organisation of Information Security

### 6.1.1 — Information Security Roles and Responsibilities

**CSP Guidance**
- Clearly define and publish the roles and responsibilities of CSP personnel in maintaining
  the security of the cloud service, including: infrastructure team, operations team, security
  team, and customer support
- Define escalation paths for security incidents involving CSC environments

**CSC Guidance**
- Define roles and responsibilities for cloud service management within the CSC organisation:
  cloud administrator, data owner, security officer, and end users
- Document who is responsible for each control in the shared responsibility model

**Note**: See CLD.6.3.1 for the additional cloud-specific shared responsibility control.

---

### 6.1.2 — Segregation of Duties

**CSP Guidance**
- Separate duties between: infrastructure administrators, security operations, customer
  support (accessing CSC environments), and finance/billing
- Prevent a single individual from both deploying cloud infrastructure and auditing that
  infrastructure's security

**CSC Guidance**
- Separate cloud administration duties from security monitoring duties
- Ensure that users who can grant cloud access cannot also approve that grant themselves

---

## Domain 7 — Human Resource Security

### 7.1.1 — Screening

**CSP Guidance**
- Apply appropriate background checks to all personnel who have access to cloud infrastructure,
  CSC data, or privileged management interfaces
- Apply enhanced screening for roles with direct access to multi-tenant management systems

**CSC Guidance**
- Ensure personnel who administer cloud services on behalf of the CSC are appropriately vetted

---

### 7.2.1 — Management Responsibilities

**CSP Guidance**
- Require managers to ensure all staff with cloud infrastructure or CSC data access understand
  and comply with cloud security policies

**CSC Guidance**
- Require managers to ensure cloud users are trained on the CSC's cloud usage policies and
  understand the risks of cloud misuse or misconfiguration

---

### 7.2.2 — Information Security Awareness, Education and Training

**CSP Guidance**
- Provide cloud-specific security training to all personnel, covering: virtualisation security,
  multi-tenancy risks, secure cloud operations, and handling of CSC data

**CSC Guidance**
- Train all cloud users on: approved cloud services, data classification for cloud upload,
  recognising phishing attacks targeting cloud credentials, and incident reporting

---

### 7.2.3 — Disciplinary Process

**CSP Guidance**
- Ensure the disciplinary process specifically addresses unauthorised access to CSC
  environments and mishandling of CSC data

**CSC Guidance**
- Ensure the disciplinary process addresses unauthorised use of unapproved cloud services
  (shadow IT) and sharing of cloud credentials

---

### 7.3.1 — Termination or Change of Employment Responsibilities

**CSP Guidance**
- Immediately revoke access to cloud management interfaces, privileged management tools,
  and CSC environment access upon termination or role change
- Ensure former employees cannot retain software, credentials, or data relating to CSC
  environments

**CSC Guidance**
- Immediately revoke cloud service access and credentials for departing employees
- Review cloud service access permissions when employees change roles and no longer require
  prior access levels

---

## Domain 8 — Asset Management

### 8.1.1 — Inventory of Assets

**CSP Guidance**
- Maintain a comprehensive inventory of all cloud service assets including: physical servers,
  virtual machines, storage systems, network equipment, and software components
- Track the versions and patch status of all components as part of the inventory

**CSC Guidance**
- Maintain an inventory of all assets (data, systems, accounts) hosted with each cloud
  service provider
- Track: data categories stored, volumes, retention periods required, and associated
  regulatory obligations

**Note**: See CLD.8.1.5 for the additional control on removal or return of CSC assets.

---

### 8.1.2 — Ownership of Assets

**CSP Guidance**
- Clearly document that CSC data stored in the cloud remains the property of the CSC
- Include a data ownership clause in the CSA

**CSC Guidance**
- Assert and document ownership of all data uploaded to cloud services
- Ensure CSA includes explicit confirmation that the CSP holds data only as a processor and
  acknowledges CSC ownership

---

### 8.1.3 — Acceptable Use of Assets

**CSP Guidance**
- Define and publish acceptable use policies for the cloud service, including what types of
  data are permitted and any restrictions on use cases (e.g., restrictions on processing of
  particularly sensitive data categories unless specifically contracted)

**CSC Guidance**
- Establish an acceptable use policy for cloud services describing: permitted data types for
  cloud storage, prohibited uses, and user responsibilities for data handling

---

## Domain 9 — Access Control

### 9.1.1 — Access Control Policy

**CSP Guidance**
- Implement access control policies that enforce tenant isolation: a CSC's users must not be
  able to access another CSC's resources under any circumstances
- Document the access control model and make it available to CSCs in service documentation

**CSC Guidance**
- Develop a cloud-specific access control policy that governs: who can access which cloud
  resources, roles and least privilege principles, and required authentication methods
- Map the policy to the shared responsibility model to confirm which access controls are
  CSC-managed versus CSP-enforced

---

### 9.2.1 — User Registration and De-Registration

**CSP Guidance**
- Implement self-service or API-based provisioning that allows CSCs to manage their own user
  accounts without requiring CSP administrator intervention for routine operations
- Ensure CSC administrators can immediately de-register users when required

**CSC Guidance**
- Implement formal processes for creating and removing cloud user accounts, including:
  approval workflow, provisioning with least-privilege defaults, and immediate deprovisioning
  upon role change or departure

---

### 9.2.2 — User Access Provisioning

**CSP Guidance**
- Provide role-based access control (RBAC) capabilities to CSCs so they can assign granular
  permissions to their users
- Document available access roles and their associated permissions in CSP documentation

**CSC Guidance**
- Assign cloud access rights based on defined roles and minimum necessary access
- Review cloud service access provisioning requests against documented role definitions

---

### 9.2.3 — Management of Privileged Access Rights

**CSP Guidance**
- Restrict and log all privileged access to cloud management interfaces
- Require explicit approval for any CSP administrator action that involves accessing CSC
  environments or data (see also CLD.12.1.5)

**CSC Guidance**
- Limit the number of cloud administrator accounts to the minimum necessary
- Apply enhanced controls to privileged cloud accounts: MFA, just-in-time access, and
  enhanced logging

---

### 9.2.4 — Management of Secret Authentication Information of Users

**CSP Guidance**
- Enforce strong password policies or passwordless authentication for cloud management
  console access
- Never store CSC user passwords in recoverable form

**CSC Guidance**
- Enforce strong passwords or MFA for all cloud service user accounts
- Require immediate rotation of cloud service credentials in the event of actual or suspected
  compromise

---

### 9.2.5 — Review of User Access Rights

**CSP Guidance**
- Provide CSCs with tooling (reports, dashboards) to enable periodic review of their users'
  access rights

**CSC Guidance**
- Conduct periodic reviews (at least annually, more frequently for privileged accounts) of
  all cloud service user access rights
- Remove or downgrade access where users no longer require it

---

### 9.2.6 — Removal or Adjustment of Access Rights

**CSP Guidance**
- Provide CSCs with the immediate ability to remove or modify user access rights at any time

**CSC Guidance**
- Implement processes to remove or adjust cloud access rights immediately upon role change
  or departure, with no dependency on deprovisioning through the HR lifecycle alone

---

### 9.3.1 — Use of Secret Authentication Information

**CSP Guidance**
- Instruct CSC users (via documentation) not to share cloud service credentials and to use
  separate credentials for each service

**CSC Guidance**
- Enforce policies against sharing of cloud service credentials
- Use service accounts or API keys with limited permissions in place of user credentials for
  automated access to cloud APIs

---

### 9.4.1 — Information Access Restriction

**CSP Guidance**
- Implement access controls that restrict access at the data and resource level, not just the
  account level, ensuring CSC users only access the data and services they are authorised to
  access
- Ensure tenant isolation prevents any cross-tenant data access (see also CLD.9.5.1)

**CSC Guidance**
- Configure cloud storage and application access controls to implement least-privilege data
  access for all users and service accounts
- Review and audit access control configurations periodically

---

### 9.4.2 — Secure Log-On Procedures

**CSP Guidance**
- Enforce MFA for all access to cloud management and administration interfaces
- Implement account lockout, login attempt logging, and anomaly detection for cloud console
  access

**CSC Guidance**
- Enforce MFA for all cloud service user accounts, particularly those with administrative
  or data access privileges
- Configure session timeouts for cloud management console sessions

---

### 9.4.3 — Password Management System

**CSP Guidance**
- Enforce password complexity and change requirements via the cloud management console
- Where available, support integration with enterprise identity providers (SAML/SSO) to
  enable CSCs to use their own authentication systems

**CSC Guidance**
- Use a password manager to generate and store unique credentials for cloud service accounts
- Where possible, federate cloud service authentication to the CSC's own enterprise identity
  provider to centralise control and enforcement

---

## Domain 10 — Cryptography

### 10.1.1 — Policy on the Use of Cryptographic Controls

**CSP Guidance**
- Document the encryption capabilities provided for data at rest and data in transit in
  the cloud service
- Clearly state which encryption is managed by the CSP, which can be managed by the CSC,
  and any limitations

**CSC Guidance**
- Establish a cloud cryptography policy covering: mandatory encryption for sensitive data
  at rest, minimum TLS version for data in transit, and acceptable key management approaches
- Determine whether CSC-managed encryption keys (BYOK — Bring Your Own Key) are required
  for compliance or risk management purposes

---

### 10.1.2 — Key Management

**CSP Guidance**
- Provide clear documentation of the CSP's key management practices, including: key
  generation, storage (HSM or equivalent), rotation schedule, and key destruction on service
  termination
- Offer CSCs the option of customer-managed keys (BYOK/HYOK) where feasible

**CSC Guidance**
- Determine whether to use CSP-managed keys, CSC-managed keys, or a combination, based on
  data sensitivity and regulatory requirements
- If using CSC-managed keys: document key rotation procedures, backup plans for key material,
  and recovery procedures in case of key loss
- Understand the implications of key deletion (data becomes unreadable)

---

## Domain 11 — Physical and Environmental Security

### 11.1.1 — Physical Security Perimeters

**CSP Guidance**
- Implement and certify (where required by CSCs) physical security of data centres hosting
  the cloud service, including: perimeter fencing, access control, CCTV, and intrusion
  detection
- Make evidence of physical security available to CSCs via third-party audit reports
  (e.g., SOC 2 Type II, ISO 27001 certificate, or equivalent)

**CSC Guidance**
- Request and review CSP physical security certifications or audit reports as part of cloud
  vendor due diligence
- Where physical security cannot be verified independently, include the right to audit in
  the CSA

---

### 11.2.5 — Removal of Assets

**CSP Guidance**
- Ensure that physical decommissioning of cloud hardware includes sanitisation of storage
  media to prevent residual CSC data from being recovered
- Document the media sanitisation process; provide evidence upon request

**CSC Guidance**
- Include hardware sanitisation provisions in the CSA
- Request certificates of media destruction when cloud infrastructure used by the CSC is
  decommissioned

---

### 11.2.6 — Security of Equipment and Assets Off-Premises

**CSP Guidance**
- Apply equivalent security controls to cloud assets operated outside the primary data centre
  (e.g., edge locations, co-location facilities) as those in the primary facility

**CSC Guidance**
- When CSC hardware is collocated with a CSP or managed cloud, ensure physical security
  provisions equivalent to those of any on-premises facility

---

## Domain 12 — Operations Security

### 12.1.1 — Documented Operating Procedures

**CSP Guidance**
- Maintain documented procedures for all cloud service operations, including: VM lifecycle
  management, backup procedures, patch management, incident response, and customer-facing
  operations
- Ensure procedures cover multi-tenant specific operations (e.g., provisioning new tenants
  without exposing existing tenant data)

**CSC Guidance**
- Document procedures for all cloud-related operations performed by the CSC: provisioning,
  de-provisioning, backup, monitoring, and incident response

---

### 12.1.2 — Change Management

**CSP Guidance**
- Apply formal change management to all changes to cloud service infrastructure that could
  affect security, availability, or performance for CSCs
- Notify CSCs in advance of planned changes with security implications
- Test changes in non-production environments before deployment to production

**CSC Guidance**
- Apply change management to cloud service configuration changes, particularly those
  affecting: access controls, network security groups, encryption settings, and monitoring
  configurations

---

### 12.1.3 — Capacity Management

**CSP Guidance**
- Monitor capacity of cloud infrastructure and scale proactively to maintain service SLAs
- Protect against resource exhaustion attacks (DoS/DDoS) that could affect availability
  for CSCs

**CSC Guidance**
- Monitor cloud resource usage to detect unexpected increases (which may indicate a security
  incident, misconfiguration, or resource abuse)
- Implement alerts for abnormal resource consumption

---

### 12.3.1 — Information Backup

**CSP Guidance**
- Document backup procedures for CSP-managed cloud services, including: backup scope,
  frequency, retention period, and restoration testing
- Clearly state in the CSA what data is backed up by the CSP, at what frequency, and what
  restoration service levels apply

**CSC Guidance**
- Do not assume the CSP backs up CSC data automatically; verify backup scope in the CSA
- Implement CSC-managed backup procedures for critical data stored in cloud services,
  including: cross-region or cross-provider backup for critical data
- Test restoration from backup periodically

---

### 12.4.1 — Event Logging

**CSP Guidance**
- Log all security-relevant events in the cloud service, including: authentication events,
  privileged access, configuration changes, API calls, and inter-tenant access attempts
- Make logs available to CSCs covering events related to their tenancy

**CSC Guidance**
- Enable logging for all CSC cloud resources: authentication, API calls, data access,
  configuration changes
- Where provided by the CSP, enable enhanced logging features (e.g., AWS CloudTrail, Azure
  Monitor, Google Cloud Audit Logs)

---

### 12.4.2 — Protection of Log Information

**CSP Guidance**
- Protect cloud service logs from modification or deletion by cloud service administrators
  and by CSC users
- Store logs in a write-once or append-only store, or export to an immutable external system

**CSC Guidance**
- Export cloud audit logs to an independent storage system where they cannot be modified
  by cloud administrators
- Apply access controls so only designated security personnel can access log systems

---

### 12.4.3 — Administrator and Operator Logs

**CSP Guidance**
- Maintain logs of all administrative actions performed by CSP operators, including actions
  affecting CSC environments; protect these logs from modification by those same operators
- See also CLD.12.1.5 for administrator operational security requirements

**CSC Guidance**
- Ensure logs of cloud administrator actions are maintained and reviewed
- Separate the role of administrator from the role of log reviewer

---

### 12.4.4 — Clock Synchronisation

**CSP Guidance**
- Synchronise all cloud infrastructure components to a reliable time source using NTP
- Document the time source used; make this available to CSCs for log correlation purposes

**CSC Guidance**
- Synchronise CSC-managed cloud VM clocks with the CSP-provided time source to ensure log
  timestamps are consistent and correlatable

---

## Domain 13 — Communications Security

### 13.1.1 — Network Controls

**CSP Guidance**
- Implement network security controls throughout the cloud service infrastructure: firewalls,
  intrusion detection/prevention systems, DDoS protection, and traffic filtering
- Apply network access controls between all cloud service components and between the service
  and the internet

**CSC Guidance**
- Configure cloud network security controls provided by the CSP (security groups, network
  ACLs, virtual firewalls) to restrict traffic to the minimum required
- Apply defence-in-depth: host-based firewalls in addition to virtual network controls

---

### 13.1.2 — Security of Network Services

**CSP Guidance**
- Communicate to CSCs the security features of each cloud network service offered, including:
  encryption in transit capabilities, access control features, and monitoring capabilities

**CSC Guidance**
- Evaluate and select cloud network services based on their security capabilities
- Require TLS/HTTPS for all data transmission and verify that the CSP does not downgrade
  connections

---

### 13.1.3 — Segregation in Networks

**CSP Guidance**
- Implement tenant network isolation separating each CSC's virtual network from all other
  CSCs and from the CSP management network (see also CLD.13.1.4)

**CSC Guidance**
- Use virtual network segmentation (subnets, VPCs/VNets, security groups) within the CSC's
  cloud environment to separate systems of different sensitivity levels
- Do not put all cloud systems on a single flat network

---

## Domain 14 — System Acquisition, Development and Maintenance

### 14.1.1 — Information Security Requirements Analysis and Specification

**CSP Guidance**
- Define and document the security requirements of the cloud service at design time, including
  requirements for: multi-tenancy, virtualisation security, data separation, and resilience

**CSC Guidance**
- Define security requirements for cloud-hosted applications before procurement or development,
  including: data classification requirements, encryption requirements, access control model,
  and logging requirements

---

### 14.2.5 — Secure System Engineering Principles

**CSP Guidance**
- Apply secure engineering principles to cloud service development: defence in depth, zero
  trust principles, least privilege, fail-secure design, and secure default configurations

**CSC Guidance**
- Apply the same secure engineering principles to applications deployed in cloud environments
  as to on-premises applications
- Apply cloud-native security patterns: use managed identity for service-to-service
  authentication, avoid embedding credentials in code, and implement least-privilege IAM roles

---

## Domain 15 — Supplier Relationships

### 15.1.1 — Information Security Policy for Supplier Relationships

**CSP Guidance**
- Manage sub-service providers (sub-processors, data centre operators, third-party component
  providers) according to a formal supplier security policy
- Ensure sub-service providers meet the same security standards as the CSP itself, and
  flow down CSC requirements where applicable

**CSC Guidance**
- Treat the CSP as a supplier subject to the CSC's supplier security management policy
- Conduct due diligence on CSPs before selection, including review of: security certifications,
  third-party audit reports, penetration testing evidence, and data processing terms
- Include ISO 27017-aligned security requirements in the CSA

---

### 15.2.1 — Monitoring and Review of Supplier Services

**CSP Guidance**
- Monitor sub-service providers' security performance and compliance continuously
- Review sub-service provider contracts and security posture at defined intervals (at least
  annually) or when there are significant changes

**CSC Guidance**
- Regularly review CSP performance against the security provisions in the CSA
- Keep up to date with CSP security advisories, compliance reports, and changes to services

---

### 15.2.2 — Managing Changes to Supplier Services

**CSP Guidance**
- Notify CSCs of significant changes to cloud service components that could affect security
- Apply change management before making such changes and communicate impact assessments

**CSC Guidance**
- Assess the security implications of changes to CSP services before accepting them
- Include a requirement in the CSA for advance notification of changes that could affect
  the CSC's compliance or security posture

---

## Domain 16 — Information Security Incident Management

### 16.1.1 — Responsibilities and Procedures

**CSP Guidance**
- Establish incident response procedures that specifically address multi-tenant cloud incidents,
  including: isolating affected tenants, notifying affected CSCs, and preserving forensic
  evidence without compromising other tenants
- Assign clear responsibilities for each phase of cloud incident response

**CSC Guidance**
- Establish cloud-specific incident response procedures, addressing the scenarios where the
  incident occurs at the CSP level and where the CSC may have limited direct access to
  investigate

---

### 16.1.2 — Reporting Information Security Events

**CSP Guidance**
- Commit to notifying CSCs of security incidents affecting their data or services within a
  defined and contractually agreed timeframe
- Include incident notification obligations in the CSA
- Provide a dedicated and accessible incident notification channel for CSCs

**CSC Guidance**
- Ensure the CSA includes the CSP's commitment to incident notification with defined
  timelines
- Implement cloud monitoring to detect incidents that may not be detected and reported by
  the CSP (see CLD.12.4.5)

---

### 16.1.3 — Reporting Information Security Weaknesses

**CSP Guidance**
- Provide a vulnerability disclosure programme allowing security researchers and CSCs to
  report cloud service security weaknesses
- Commit to acknowledging and remediating reported vulnerabilities within defined timelines

**CSC Guidance**
- Report identified vulnerabilities in the cloud service to the CSP through official channels
- Do not exploit discovered vulnerabilities; report them responsibly

---

### 16.1.4 — Assessment of and Decision on Information Security Events

**CSP Guidance**
- Assess every reported security event for its potential impact on CSC data and services
- Prioritise events involving CSC data exposure or service disruption

**CSC Guidance**
- Assess cloud security events in the context of the CSC's own risk register and the impact
  on CSC-managed data and services

---

### 16.1.7 — Collection of Evidence

**CSP Guidance**
- Preserve forensic evidence of cloud security incidents in a manner admissible for legal or
  regulatory proceedings, without contaminating or destroying logs or system state
- Cooperate with CSC evidence collection requests within legal and contractual constraints

**CSC Guidance**
- Define how the CSC will collect forensic evidence from cloud environments (acknowledging
  limitations such as shared infrastructure and limited direct access to underlying hardware)
- Include evidence preservation obligations in the CSA

---

## Domain 17 — Business Continuity Management

### 17.1.1 — Planning Information Security Continuity

**CSP Guidance**
- Develop and maintain a business continuity plan that includes provisions for maintaining
  cloud service availability and security during disruptions
- Make availability SLAs (uptime commitments) available in the CSA

**CSC Guidance**
- Plan for scenarios where the cloud service is unavailable: failover to alternate CSP region,
  use of alternative service, or reversion to on-premises operation
- Include the CSP's availability SLA in the CSC's own BCP assumptions

---

### 17.1.2 — Implementing Information Security Continuity

**CSP Guidance**
- Implement redundancy and resilience mechanisms across the cloud service: multi-region
  deployment, auto-failover, load balancing, and regular failover testing
- Document which resilience features are built into the service and which require CSC
  configuration

**CSC Guidance**
- Configure and test cloud resilience features appropriate to the CSC's recovery time and
  recovery point objectives
- Test restoration from cross-region backup at least annually

---

### 17.2.1 — Availability of Information Processing Facilities

**CSP Guidance**
- Provide redundancy for all critical cloud service components with documented SLAs covering
  availability, RPO (recovery point objective), and RTO (recovery time objective)
- Disclose planned maintenance windows with advance notice to CSCs

**CSC Guidance**
- Select CSP service tiers that provide availability appropriate to the criticality of the
  CSC's workloads
- Use cloud-native high availability features (load balancers, multi-zone deployment) for
  critical services

---

## Domain 18 — Compliance

### 18.1.1 — Identification of Applicable Legislation and Contractual Requirements

**CSP Guidance**
- Provide CSCs with sufficient information to determine whether the cloud service meets their
  legal and regulatory requirements, including: jurisdiction of data storage, certifications
  held, and data processing terms available
- Maintain compliance with applicable laws and regulations in all jurisdictions where the
  cloud service operates

**CSC Guidance**
- Identify all legal, regulatory, and contractual requirements that apply to data stored in
  or processed by cloud services (e.g., GDPR, HIPAA, PCI DSS)
- Verify that the CSP provides the technical and contractual controls necessary to meet
  these requirements before selecting the service

---

### 18.1.3 — Protection of Records

**CSP Guidance**
- Ensure that records required by CSCs for regulatory compliance can be retained for the
  required period and are protected from modification, deletion, or loss

**CSC Guidance**
- Verify that cloud storage services for records meet the CSC's records retention requirements
  in terms of: durability, availability, and write-protection capabilities
- Implement cloud storage with retention policies and legal hold capabilities where required

# ISO/IEC 27017:2015 — Shared Responsibility Matrix

This file documents the allocation of information security responsibilities between
Cloud Service Providers (CSPs) and Cloud Service Customers (CSCs) in accordance with
ISO/IEC 27017:2015. The allocation varies by cloud service model.

**Legend:**
- **CSP** — Cloud Service Provider is solely responsible
- **CSC** — Cloud Service Customer is solely responsible
- **Shared** — Both parties have defined obligations; scope differs between them
- **N/A** — Not applicable to this service model

---

## Shared Responsibility by Cloud Service Model

### Section 1 — Infrastructure and Platform Layers

| Security Area | IaaS | PaaS | SaaS |
|--------------|------|------|------|
| Physical data centre security (11.1.1) | CSP | CSP | CSP |
| Physical hardware security and sanitisation (11.2.5) | CSP | CSP | CSP |
| Hypervisor and virtualisation layer security (CLD.9.5.1) | CSP | CSP | CSP |
| Host operating system patching (virtual host) | CSP | CSP | CSP |
| Guest operating system patching (CSC VMs) | CSC | CSP | CSP |
| Runtime environment and middleware | CSC | CSP | CSP |
| Application code and libraries | CSC | CSC | CSP |
| Application security configuration | CSC | CSC | Shared |
| Network infrastructure (physical) | CSP | CSP | CSP |
| Virtual network provisioning and security groups | Shared | CSP | CSP |
| DDoS protection | Shared | Shared | CSP |
| Firewall between tenants (CLD.9.5.1) | CSP | CSP | CSP |
| Virtual machine hardening — base images (CLD.9.5.2) | CSP | CSP | CSP |
| Virtual machine hardening — deployed VMs (CLD.9.5.2) | CSC | Shared | CSP |
| Virtual/physical network security alignment (CLD.13.1.4) | CSP | CSP | CSP |

---

### Section 2 — Identity and Access Management

| Security Area | IaaS | PaaS | SaaS |
|--------------|------|------|------|
| CSP platform IAM (admin access to infrastructure) (CLD.12.1.5) | CSP | CSP | CSP |
| CSC user account creation and management (9.2.1, 9.2.2) | CSC | CSC | CSC |
| CSC user de-provisioning (9.2.6, 7.3.1) | CSC | CSC | CSC |
| Privileged access management — CSP admins (9.2.3, CLD.12.1.5) | CSP | CSP | CSP |
| Privileged access management — CSC admins (9.2.3) | CSC | CSC | CSC |
| MFA enforcement for CSP administrative access (9.4.2, CLD.12.1.5) | CSP | CSP | CSP |
| MFA enforcement for CSC user accounts (9.4.2) | CSC | CSC | CSC |
| Role-based access control framework (9.2.2) | Shared | Shared | Shared |
| Password policy enforcement for CSC users (9.4.3) | CSC | CSC | Shared |
| Federated identity / SSO integration | Shared | Shared | Shared |
| Periodic access right review — CSC users (9.2.5) | CSC | CSC | CSC |

---

### Section 3 — Data Security

| Security Area | IaaS | PaaS | SaaS |
|--------------|------|------|------|
| Data classification and labelling | CSC | CSC | CSC |
| Encryption of data at rest — CSP infrastructure (10.1.1) | CSP | CSP | CSP |
| Encryption of data at rest — CSC-managed volumes (10.1.1) | CSC | Shared | CSP |
| Encryption in transit (TLS) — infrastructure (10.1.1) | CSP | CSP | CSP |
| Encryption in transit — application layer (10.1.1) | CSC | CSC | CSP |
| Key management for CSP-managed keys (10.1.2) | CSP | CSP | CSP |
| Key management for customer-managed keys / BYOK (10.1.2) | CSC | CSC | CSC |
| Data ownership definition (8.1.2) | CSC | CSC | CSC |
| Data return capability upon termination (CLD.8.1.5) | CSP | CSP | CSP |
| Data deletion upon termination (CLD.8.1.5) | CSP | CSP | CSP |
| Certificate of data deletion (CLD.8.1.5) | CSP | CSP | CSP |
| CSC data retrieval verification (CLD.8.1.5) | CSC | CSC | CSC |
| Data sovereignty and jurisdiction documentation (18.1.1) | CSP | CSP | CSP |

---

### Section 4 — Operations and Monitoring

| Security Area | IaaS | PaaS | SaaS |
|--------------|------|------|------|
| Cloud service infrastructure monitoring (CLD.12.4.5) | CSP | CSP | CSP |
| CSC usage and security event monitoring (CLD.12.4.5) | CSC | CSC | CSC |
| Monitoring data availability to CSC (CLD.12.4.5) | CSP | CSP | CSP |
| Event logging — infrastructure layer (12.4.1) | CSP | CSP | CSP |
| Event logging — CSC workloads and applications (12.4.1) | CSC | CSC | Shared |
| Log integrity protection (12.4.2) | Shared | Shared | CSP |
| Administrator activity logging (12.4.3, CLD.12.1.5) | Shared | Shared | CSP |
| Backup — CSP platform components (12.3.1) | CSP | CSP | CSP |
| Backup — CSC data and workloads (12.3.1) | CSC | Shared | CSP |
| Backup restoration testing (12.3.1) | CSC | Shared | CSP |
| Change management — infrastructure (12.1.2) | CSP | CSP | CSP |
| Change management — CSC configurations (12.1.2) | CSC | CSC | CSC |
| Capacity management — infrastructure (12.1.3) | CSP | CSP | CSP |
| Capacity monitoring — CSC workloads (12.1.3) | CSC | CSC | CSC |
| Patch management — CSP platform (12.1.1) | CSP | CSP | CSP |
| Patch management — CSC VMs and applications | CSC | Shared | CSP |

---

### Section 5 — Incident Response

| Security Area | IaaS | PaaS | SaaS |
|--------------|------|------|------|
| Incident detection — infrastructure (16.1.1) | CSP | CSP | CSP |
| Incident detection — CSC workloads (16.1.1) | CSC | Shared | Shared |
| CSP-to-CSC incident notification (16.1.2) | CSP | CSP | CSP |
| CSC incident response plan (16.1.1) | CSC | CSC | CSC |
| Forensic evidence collection — infrastructure (16.1.7) | CSP | CSP | CSP |
| Forensic cooperation with CSC (16.1.7) | CSP | CSP | CSP |
| Forensic evidence from CSC workloads (16.1.7) | CSC | Shared | CSC |
| Vulnerability reporting mechanism (16.1.3) | CSP | CSP | CSP |
| CSC vulnerability assessment for own workloads (16.1.3) | CSC | CSC | N/A |

---

### Section 6 — Governance and Compliance

| Security Area | IaaS | PaaS | SaaS |
|--------------|------|------|------|
| Shared responsibility documentation (CLD.6.3.1) | CSP | CSP | CSP |
| CSC acknowledgement of shared responsibility (CLD.6.3.1) | CSC | CSC | CSC |
| Cloud service agreement security provisions (CLD.6.3.1) | Shared | Shared | Shared |
| Third-party security certifications (18.1.1) | CSP | CSP | CSP |
| CSC regulatory compliance for CSC data (18.1.1) | CSC | CSC | CSC |
| Sub-processor management (15.1.1) | CSP | CSP | CSP |
| CSP due diligence by CSC (15.1.1) | CSC | CSC | CSC |
| CSC supplier assessment of CSP (15.2.1) | CSC | CSC | CSC |
| Records protection — infrastructure (18.1.3) | CSP | CSP | CSP |
| Records protection — CSC content (18.1.3) | CSC | CSC | Shared |
| Business continuity — CSP platform (17.2.1) | CSP | CSP | CSP |
| Business continuity — CSC workloads (17.1.1) | CSC | Shared | Shared |

---

## Notes on Shared Responsibilities

### CLD.6.3.1 Obligation
Both the CSP and CSC have an explicit obligation under CLD.6.3.1 to define and document their
respective responsibilities. Regardless of which items in the table above are marked "Shared,"
the allocation must be formally agreed and documented in the Cloud Service Agreement.

### IaaS Considerations
In IaaS, the CSC has the most extensive security responsibilities of any service model.
The CSC effectively manages everything above the hypervisor layer including:
- Guest OS security configuration and patching
- Application security
- Firewall rules (security groups) and network ACLs
- Data encryption configuration
- Identity and access management for all workloads

### PaaS Considerations
In PaaS, the boundary shifts: the CSP manages the OS and runtime. The CSC retains responsibility
for application security, data, and identity. Key CSC risks in PaaS include:
- Application-level vulnerabilities
- Insecure API configuration
- Data input validation
- Access control within the application

### SaaS Considerations
In SaaS, the CSC has limited direct control over security. The CSC's primary responsibilities are:
- User account provisioning and deprovisioning (9.2.1, 9.2.6)
- Enforcement of MFA for user accounts (9.4.2)
- Access right reviews (9.2.5)
- Configuration of data sharing and export settings
- Monitoring of own user activity (CLD.12.4.5)
- Ensuring data retrieved and compliance requirements met (18.1.1)

The CSP bears the vast majority of technical security controls in SaaS. The CSC's due diligence
obligations (clause 15) and contractual requirements (CLD.6.3.1) remain fully applicable.

---

## Cloud Service Agreement Security Provisions Checklist

The following security provisions must be addressed in every Cloud Service Agreement under
ISO/IEC 27017:

| Provision | ISO 27017 Reference | Required |
|-----------|--------------------|---------:|
| Explicit shared responsibility allocation | CLD.6.3.1 | Yes |
| Data ownership confirmation (CSC owns data) | 8.1.2 | Yes |
| Data return format and procedure | CLD.8.1.5 | Yes |
| Data deletion procedure and timeline | CLD.8.1.5 | Yes |
| Certificate of deletion on request | CLD.8.1.5 | Yes |
| Incident notification obligation and timeline | 16.1.2 | Yes |
| Right to audit or request third-party audit reports | 15.2.1 | Yes |
| Sub-processor disclosure and restrictions | 15.1.1 | Yes |
| Applicable law and jurisdiction | 18.1.1 | Yes |
| Availability SLA (uptime commitment, RPO/RTO) | 17.2.1 | Yes |
| Maintenance window notification commitment | 17.1.2 | Yes |
| Advance notification of material changes to the service | 15.2.2 | Yes |
| Backup scope, frequency, and retention | 12.3.1 | Yes |
| Log retention period and availability to CSC | 12.4.1, CLD.12.4.5 | Yes |
| Encryption capabilities (at rest, in transit) | 10.1.1 | Yes |
| Physical security certifications (or right to assess) | 11.1.1 | Yes |
| Penetration testing frequency or right to test | 16.1.3 | Recommended |
| Support for customer-managed keys (BYOK) | 10.1.2 | As required |
| Compliance certifications maintained by the CSP | 18.1.1 | Yes |
| Personnel screening requirements for CSP staff | 7.1.1 | Yes |

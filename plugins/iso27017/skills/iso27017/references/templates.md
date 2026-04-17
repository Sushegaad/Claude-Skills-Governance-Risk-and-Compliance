# ISO/IEC 27017:2015 — Templates and Checklists

This file contains reusable templates for ISO 27017 compliance activities including gap analysis,
cloud service agreement review, policy documents, and certification readiness checklists.

---

## Template 1 — ISO 27017 Gap Analysis

Use this template to assess current state against ISO/IEC 27017:2015 requirements.

```
================================================================================
ISO/IEC 27017:2015 CLOUD SECURITY GAP ANALYSIS
================================================================================
Organisation:        [Organisation Name]
Role:                [Cloud Service Provider / Cloud Service Customer / Both]
Cloud Service Model: [IaaS / PaaS / SaaS]
Assessment Scope:    [Service names, environments, or systems in scope]
Assessment Date:     [Date]
Assessed By:         [Name / Team]
Review Date:         [Next scheduled review]
Version:             [1.0]

--------------------------------------------------------------------------------
SECTION A — CLD CONTROLS (CLOUD-SPECIFIC CONTROLS)
--------------------------------------------------------------------------------
Control ID   | Control Name                                      | Applicability | Status          | Evidence Required                                 | Gap Notes
-------------|---------------------------------------------------|---------------|-----------------|---------------------------------------------------|----------
CLD.6.3.1    | Shared roles and responsibilities                 | Both          | [Status]        | Documented responsibility split; CSA clause       | [Notes]
CLD.8.1.5    | Removal or return of CSC assets                   | Both          | [Status]        | Data return procedure; deletion cert              | [Notes]
CLD.9.5.1    | Segregation in virtual environments               | CSP           | [Status]        | Hypervisor isolation docs; penetration test       | [Notes]
CLD.9.5.2    | Virtual machine hardening                         | Both          | [Status]        | VM hardening standard; scan results               | [Notes]
CLD.12.1.5   | Administrator's operational security              | CSP           | [Status]        | MFA evidence; admin access logs; RBAC config      | [Notes]
CLD.12.4.5   | Monitoring of cloud services                      | Both          | [Status]        | Monitoring architecture; CSC dashboard access     | [Notes]
CLD.13.1.4   | Virtual/physical network security alignment       | CSP           | [Status]        | Network security policy; architecture diagram     | [Notes]

--------------------------------------------------------------------------------
SECTION B — ISO 27002 CONTROLS WITH CLOUD-SPECIFIC GUIDANCE
--------------------------------------------------------------------------------
[Repeat the table below for each of the 37 controls — see iso27002-cloud-guidance.md]

Control ID   | Control Name                                      | Applicability | Status          | Evidence Required                                 | Gap Notes
-------------|---------------------------------------------------|---------------|-----------------|---------------------------------------------------|----------
5.1.1        | Policies for information security                 | Both          | [Status]        | Cloud-specific IS policy                          | [Notes]
5.1.2        | Review of policies                                | Both          | [Status]        | Review records                                    | [Notes]
6.1.1        | IS roles and responsibilities                     | Both          | [Status]        | Roles/RACI document                               | [Notes]
6.1.2        | Segregation of duties                             | Both          | [Status]        | Duty separation evidence                          | [Notes]
7.1.1        | Screening                                         | Both          | [Status]        | Background check records                          | [Notes]
7.2.1        | Management responsibilities                        | Both          | [Status]        | Management sign-off on cloud security             | [Notes]
7.2.2        | IS awareness, education and training              | Both          | [Status]        | Cloud training records                            | [Notes]
7.2.3        | Disciplinary process                              | Both          | [Status]        | Policy covering cloud violations                  | [Notes]
7.3.1        | Termination responsibilities                       | Both          | [Status]        | Off-boarding process for cloud access             | [Notes]
8.1.1        | Inventory of assets                               | Both          | [Status]        | Cloud asset register                              | [Notes]
8.1.2        | Ownership of assets                               | Both          | [Status]        | Ownership clause in CSA; asset registry           | [Notes]
8.1.3        | Acceptable use of assets                          | Both          | [Status]        | AUP covering cloud services                       | [Notes]
9.1.1        | Access control policy                             | Both          | [Status]        | Cloud access control policy                       | [Notes]
9.2.1        | User registration and de-registration             | Both          | [Status]        | Provisioning process records                      | [Notes]
9.2.2        | User access provisioning                          | Both          | [Status]        | Access request records; RBAC config               | [Notes]
9.2.3        | Management of privileged access rights            | Both          | [Status]        | PAM solution; privileged account list             | [Notes]
9.2.4        | Management of secret authentication information  | Both          | [Status]        | Password policy; credential management            | [Notes]
9.2.5        | Review of user access rights                      | Both          | [Status]        | Access review records                             | [Notes]
9.2.6        | Removal or adjustment of access rights            | Both          | [Status]        | Deprovisioning process; timing evidence           | [Notes]
9.3.1        | Use of secret authentication information          | Both          | [Status]        | Credential use policy; service account policy     | [Notes]
9.4.1        | Information access restriction                    | Both          | [Status]        | Resource-level access controls; IAM config        | [Notes]
9.4.2        | Secure log-on procedures                          | Both          | [Status]        | MFA configuration; session timeout settings       | [Notes]
9.4.3        | Password management system                        | Both          | [Status]        | Password complexity settings; PWDM config         | [Notes]
10.1.1       | Policy on cryptographic controls                  | Both          | [Status]        | Encryption policy; at-rest/in-transit config      | [Notes]
10.1.2       | Key management                                    | Both          | [Status]        | KMS configuration; key rotation records           | [Notes]
11.1.1       | Physical security perimeters                      | CSP           | [Status]        | ISO 27001 cert; SOC 2 audit report                | [Notes]
11.2.5       | Removal of assets                                 | CSP           | [Status]        | Media destruction certificates                    | [Notes]
11.2.6       | Security of equipment off-premises                | Both          | [Status]        | Co-location security documentation                | [Notes]
12.1.1       | Documented operating procedures                   | Both          | [Status]        | Cloud operations runbooks                         | [Notes]
12.1.2       | Change management                                 | Both          | [Status]        | Change records; CAB approval                      | [Notes]
12.1.3       | Capacity management                               | Both          | [Status]        | Capacity monitoring alerts; scaling policy        | [Notes]
12.3.1       | Information backup                                | Both          | [Status]        | Backup policy; restoration test records           | [Notes]
12.4.1       | Event logging                                     | Both          | [Status]        | Logging configuration; log samples                | [Notes]
12.4.2       | Protection of log information                     | Both          | [Status]        | Log immutability config; access controls          | [Notes]
12.4.3       | Administrator and operator logs                   | Both          | [Status]        | Admin logging config; separation of log access    | [Notes]
12.4.4       | Clock synchronisation                             | Both          | [Status]        | NTP configuration                                 | [Notes]
13.1.1       | Network controls                                  | Both          | [Status]        | Network security docs; security group config      | [Notes]
13.1.2       | Security of network services                      | Both          | [Status]        | TLS configuration; CSP network service docs       | [Notes]
13.1.3       | Segregation in networks                           | Both          | [Status]        | Network segmentation architecture                 | [Notes]
14.1.1       | IS requirements analysis and specification        | Both          | [Status]        | Security requirements in design docs              | [Notes]
14.2.5       | Secure system engineering principles              | Both          | [Status]        | Secure design patterns; architecture review       | [Notes]
15.1.1       | IS policy for supplier relationships              | Both          | [Status]        | Supplier security policy; CSA security review     | [Notes]
15.2.1       | Monitoring and review of supplier services        | CSC           | [Status]        | CSP review records; audit report reviews          | [Notes]
15.2.2       | Managing changes to supplier services             | CSC           | [Status]        | Change notification records; impact assessments   | [Notes]
16.1.1       | Responsibilities and procedures                   | Both          | [Status]        | Cloud incident response plan                      | [Notes]
16.1.2       | Reporting information security events             | Both          | [Status]        | Incident notification CSA clause; reports         | [Notes]
16.1.3       | Reporting weaknesses                              | Both          | [Status]        | Vulnerability disclosure process                  | [Notes]
16.1.4       | Assessment of IS events                           | Both          | [Status]        | Incident severity classification                  | [Notes]
16.1.7       | Collection of evidence                            | Both          | [Status]        | Forensic procedure; CSA cooperation clause        | [Notes]
17.1.1       | Planning IS continuity                            | Both          | [Status]        | Cloud BCP                                         | [Notes]
17.1.2       | Implementing IS continuity                        | Both          | [Status]        | Failover test records; multi-region config        | [Notes]
17.2.1       | Availability of processing facilities             | Both          | [Status]        | SLA documentation; availability metrics           | [Notes]
18.1.1       | Identification of applicable legislation          | Both          | [Status]        | Legal register; jurisdiction documentation        | [Notes]
18.1.3       | Protection of records                             | Both          | [Status]        | Retention policy; WORM storage config             | [Notes]

--------------------------------------------------------------------------------
GAP ANALYSIS SUMMARY
--------------------------------------------------------------------------------
Total Controls Assessed:          [Number]
Implemented:                       [Number] ([%])
Partial:                           [Number] ([%])
Not Implemented:                   [Number] ([%])
Not Applicable (with justification): [Number] ([%])

Critical Gaps (address immediately):
  1. [Control ID] — [Gap Description]
  2. [Control ID] — [Gap Description]

High Priority (address within 30 days):
  1. [Control ID] — [Gap Description]

Medium Priority (address within 90 days):
  1. [Control ID] — [Gap Description]

Low Priority (address in next review cycle):
  1. [Control ID] — [Gap Description]
================================================================================
```

---

## Template 2 — Cloud Service Agreement Security Review Checklist

Use this checklist to evaluate whether a cloud service agreement meets ISO 27017 requirements.

```
================================================================================
CLOUD SERVICE AGREEMENT (CSA) SECURITY REVIEW
================================================================================
Cloud Service Provider:   [CSP Name]
Cloud Service Name:       [Service Name]
Service Model:            [IaaS / PaaS / SaaS]
Agreement Reference:      [Contract/Agreement Number]
Review Date:              [Date]
Reviewed By:              [Name / Role]

KEY: Present = clause exists | Adequate = clause meets ISO 27017 standard | Critical = must resolve before use

SECTION 1 — SHARED RESPONSIBILITY AND GOVERNANCE
-------------------------------------------------
Requirement                                             | ISO 27017 Ref | Present | Adequate | Priority | Notes
--------------------------------------------------------|---------------|---------|----------|----------|------
Explicit shared responsibility allocation               | CLD.6.3.1     | Y/N     | Y/N      | Critical |
Data ownership confirmation (CSC owns data)             | 8.1.2         | Y/N     | Y/N      | Critical |
Applicable law and jurisdiction                         | 18.1.1        | Y/N     | Y/N      | Critical |
Sub-processor disclosure and consent requirement        | 15.1.1        | Y/N     | Y/N      | High     |
Right to audit or review third-party audit reports      | 15.2.1        | Y/N     | Y/N      | High     |
Advance notification of material service changes        | 15.2.2        | Y/N     | Y/N      | High     |
Personnel screening requirements for CSP staff          | 7.1.1         | Y/N     | Y/N      | Medium   |
Compliance certifications maintained (specify which)    | 18.1.1        | Y/N     | Y/N      | High     |

SECTION 2 — DATA MANAGEMENT
----------------------------
Requirement                                             | ISO 27017 Ref | Present | Adequate | Priority | Notes
--------------------------------------------------------|---------------|---------|----------|----------|------
Data return format and procedure on termination         | CLD.8.1.5     | Y/N     | Y/N      | Critical |
Data deletion timeline after termination                | CLD.8.1.5     | Y/N     | Y/N      | Critical |
Certificate of deletion on request                      | CLD.8.1.5     | Y/N     | Y/N      | Critical |
Deletion of backup copies confirmed                     | CLD.8.1.5     | Y/N     | Y/N      | High     |
Data sovereignty / geographic storage restrictions      | 18.1.1        | Y/N     | Y/N      | High     |
Records retention capabilities                          | 18.1.3        | Y/N     | Y/N      | Medium   |

SECTION 3 — SECURITY CONTROLS
------------------------------
Requirement                                             | ISO 27017 Ref | Present | Adequate | Priority | Notes
--------------------------------------------------------|---------------|---------|----------|----------|------
Encryption at rest capabilities and responsibilities    | 10.1.1        | Y/N     | Y/N      | Critical |
Encryption in transit (minimum TLS version)             | 10.1.1        | Y/N     | Y/N      | Critical |
Key management approach documented                      | 10.1.2        | Y/N     | Y/N      | High     |
Customer-managed keys (BYOK/HYOK) availability          | 10.1.2        | Y/N     | Y/N      | Medium   |
Physical security certifications (ISO 27001, SOC 2)    | 11.1.1        | Y/N     | Y/N      | High     |
Penetration testing frequency or rights to pentest     | 16.1.3        | Y/N     | Y/N      | Medium   |

SECTION 4 — OPERATIONS AND MONITORING
--------------------------------------
Requirement                                             | ISO 27017 Ref | Present | Adequate | Priority | Notes
--------------------------------------------------------|---------------|---------|----------|----------|------
Log retention period                                    | 12.4.1        | Y/N     | Y/N      | High     |
Monitoring data availability to CSC                     | CLD.12.4.5    | Y/N     | Y/N      | High     |
Backup scope, frequency, and retention                  | 12.3.1        | Y/N     | Y/N      | High     |
Backup restoration SLA                                  | 12.3.1        | Y/N     | Y/N      | High     |
Availability SLA with uptime commitment                 | 17.2.1        | Y/N     | Y/N      | High     |
RPO and RTO commitments                                 | 17.2.1        | Y/N     | Y/N      | Medium   |
Planned maintenance window advance notice               | 17.1.2        | Y/N     | Y/N      | Medium   |

SECTION 5 — INCIDENT RESPONSE
-------------------------------
Requirement                                             | ISO 27017 Ref | Present | Adequate | Priority | Notes
--------------------------------------------------------|---------------|---------|----------|----------|------
Incident notification obligation                        | 16.1.2        | Y/N     | Y/N      | Critical |
Incident notification timeline (hours)                  | 16.1.2        | Y/N     | Y/N      | Critical |
Scope of incidents covered by notification obligation   | 16.1.2        | Y/N     | Y/N      | High     |
Forensic cooperation obligations                        | 16.1.7        | Y/N     | Y/N      | Medium   |
Vulnerability disclosure process/timeline               | 16.1.3        | Y/N     | Y/N      | Medium   |

SUMMARY
-------
Critical Issues (must resolve before use):    [Number]
High Priority Issues:                         [Number]
Medium Priority Issues:                       [Number]
Overall Assessment:  [PASS / CONDITIONAL (resolve high/critical first) / FAIL]
================================================================================
```

---

## Template 3 — Cloud Security Policy (ISO 27017-Aligned)

```
================================================================================
CLOUD SECURITY POLICY
================================================================================
Document Control
  Title:          Cloud Information Security Policy
  Version:        [1.0]
  Author:         [Name / Role]
  Approved By:    [Name / Role]
  Approval Date:  [Date]
  Next Review:    [Date + 12 months]
  Classification: [Internal / Restricted]

ISO 27017 References: 5.1.1, 5.1.2, CLD.6.3.1, 8.1.1–8.1.3, 9.1.1, 10.1.1–10.1.2

1. PURPOSE
   This policy establishes [Organisation Name]'s information security requirements for
   the use of cloud computing services, covering both [Organisation Name] acting as a
   cloud service customer and, where applicable, as a cloud service provider.

2. SCOPE
   This policy applies to:
   - All employees, contractors, and third parties who utilise or administer cloud services
     on behalf of [Organisation Name]
   - All cloud service providers engaged by [Organisation Name]
   - All data processed, stored, or transmitted via cloud services

3. SHARED RESPONSIBILITY (CLD.6.3.1 / ISO 27017)
   All cloud service engagements must have a formally documented shared responsibility
   allocation identifying which security controls are the responsibility of the cloud service
   provider and which are the responsibility of [Organisation Name]. This documentation must
   be reviewed and approved before a cloud service is approved for use with sensitive data.

4. APPROVED CLOUD SERVICES
   Only cloud services that have completed [Organisation Name]'s cloud vendor due diligence
   process (see Cloud Procurement Procedure) are permitted for use with [Classification Level]
   or above data. Use of unapproved cloud services for such data is prohibited.

5. DATA CLASSIFICATION FOR CLOUD USE
   Data must be classified in accordance with [Organisation Name]'s Data Classification
   Policy before being uploaded to any cloud service. The maximum data classification
   permitted in each cloud service tier is maintained in the Cloud Service Register.

6. CLOUD ASSET MANAGEMENT (8.1.1–8.1.3)
   6.1 An inventory of all data and systems hosted with each cloud service provider must be
       maintained and reviewed quarterly.
   6.2 Data ownership must be documented for all cloud-hosted data.
   6.3 Data return and deletion arrangements must be confirmed before any cloud service
       contract is signed (CLD.8.1.5).

7. ACCESS CONTROL FOR CLOUD SERVICES (9.1.1, 9.2.1–9.2.6, 9.4.2)
   7.1 Access to cloud services must be provisioned on a least-privilege basis.
   7.2 Multi-factor authentication (MFA) is required for all cloud service accounts with
       privileged or administrative access.
   7.3 Cloud service credentials must not be shared between individuals.
   7.4 Access rights must be reviewed at least annually for all cloud service accounts.
   7.5 Access must be revoked immediately upon role change or departure.

8. CRYPTOGRAPHY FOR CLOUD DATA (10.1.1, 10.1.2)
   8.1 All sensitive data stored in cloud services must be encrypted at rest and in transit.
   8.2 Key management responsibilities must be documented in the shared responsibility
       allocation for each cloud service.
   8.3 Where customer-managed encryption keys (BYOK) are required, key management
       procedures must be documented and tested.

9. CLOUD INCIDENT RESPONSE (16.1.1, 16.1.2)
   9.1 All cloud service agreements must include a contractual incident notification
       obligation from the cloud service provider.
   9.2 [Organisation Name] cloud security incidents must be reported in accordance with
       the Information Security Incident Response Policy.
   9.3 Cloud-specific incident scenarios must be included in the annual incident response
       test programme.

10. MONITORING (CLD.12.4.5, 12.4.1)
    10.1 Cloud service usage and security events must be monitored by [Organisation Name].
    10.2 Cloud audit logs must be enabled and exported to [Organisation Name]'s SIEM or
         equivalent log management system.
    10.3 Alerts must be configured for: abnormal access patterns, privilege escalation,
         unusual data export volumes, and account takeover indicators.

11. CLOUD BUSINESS CONTINUITY (17.1.1, 17.2.1)
    11.1 Business continuity plans for critical processes must include scenarios where
         cloud services are unavailable.
    11.2 Recovery time objectives (RTOs) and recovery point objectives (RPOs) for
         cloud-hosted systems must be documented and tested.

12. REVIEW AND COMPLIANCE
    This policy must be reviewed annually or when significant changes occur in the cloud
    environment. Compliance will be assessed as part of [Organisation Name]'s annual
    internal audit programme.

References:
  - ISO/IEC 27017:2015
  - ISO/IEC 27001:2022 (ISMS framework)
  - ISO/IEC 27002:2013 (control guidelines)
  - [Organisation Name] Information Security Policy
  - [Organisation Name] Data Classification Policy
================================================================================
```

---

## Template 4 — Virtual Machine Hardening Standard

```
================================================================================
VIRTUAL MACHINE HARDENING STANDARD
================================================================================
Document Control
  Title:          Virtual Machine Security Hardening Standard
  Version:        [1.0]
  Author:         [Name / Role]
  Approved By:    [Name / Role]
  Approval Date:  [Date]
  Next Review:    [Date + 12 months]
  Classification: [Internal]

ISO 27017 Reference: CLD.9.5.2

1. PURPOSE
   This standard defines the minimum security configuration requirements for all virtual
   machines deployed by [Organisation Name] in cloud environments.

2. BASE IMAGE REQUIREMENTS
   - Only approved, centre-maintained base images may be used as the starting point for
     new VM deployments
   - Base images must be rebuilt with current patches at least every [90 days]
   - The image registry must record: image version, last patch date, approved platforms

3. OPERATING SYSTEM HARDENING REQUIREMENTS
   3.1 Remove or disable all OS features and services not required for the VM's function
   3.2 Apply all available security patches before deployment to production
   3.3 Disable all default credentials; set unique strong credentials or key-based auth
   3.4 Disable remote root / administrator login; require use of privilege escalation
   3.5 Enable host-based firewall; default deny all inbound traffic not explicitly permitted
   3.6 Enable OS-level audit logging covering: authentication events, privilege use,
       file access events for sensitive directories, and process execution
   3.7 Configure encrypted storage volumes for all volumes containing sensitive data (CLD.9.5.2)
   3.8 Close all unnecessary listening ports; document all open ports with justification

4. NETWORK EXPOSURE REQUIREMENTS
   - Management ports (SSH [22], RDP [3389]) must not be exposed to the public internet
   - Use a VPN, bastion host, or zero-trust access gateway for administrative access
   - Apply the cloud provider's security group / network ACL to restrict traffic to
     the minimum required

5. PATCH MANAGEMENT
   - Critical patches must be applied within [7] days of release
   - High severity patches must be applied within [14] days of release
   - Medium severity patches must be applied within [30] days of release
   - All patches must be applied within [90] days of release

6. HARDENING VERIFICATION
   - All VMs must be scanned with an approved vulnerability scanner before production use
   - Scan results must achieve [required score per tool] before deployment is approved
   - Periodic re-scans must be conducted at least [quarterly]

7. EXCEPTIONS
   Deviations from this standard require approval of the [CISO / Security Manager] with
   documented compensating controls and review date.

References:
  - ISO/IEC 27017:2015 — CLD.9.5.2
  - CIS Benchmarks (appropriate OS version)
  - [Organisation Name] Patch Management Policy
================================================================================
```

---

## Template 5 — Cloud Vendor Due Diligence Questionnaire (ISO 27017-Aligned)

Use this questionnaire when assessing a cloud service provider before engagement.

```
===================================================================================
CLOUD VENDOR SECURITY DUE DILIGENCE QUESTIONNAIRE
===================================================================================
Vendor Name:          [CSP Name]
Service Name:         [Service Name]
Service Model:        [IaaS / PaaS / SaaS]
Assessment Date:      [Date]
Assessed By:          [Name / Role]

SECTION 1 — CERTIFICATIONS AND AUDITS
ISO 27017 Ref: 11.1.1, 15.1.1, 18.1.1

Q1. Does the CSP hold an ISO 27001 certification? If yes, provide certificate number and scope.
Q2. Does the CSP hold a SOC 2 Type II report? If yes, provide report date and scope.
Q3. Does the CSP comply with ISO/IEC 27017:2015? Provide evidence.
Q4. What other security certifications does the CSP hold?
Q5. How frequently does the CSP commission third-party penetration tests? Are reports available?

SECTION 2 — SHARED RESPONSIBILITY
ISO 27017 Ref: CLD.6.3.1

Q6. Does the CSP provide a formal shared responsibility document or matrix?
Q7. How does the responsibility allocation differ between IaaS, PaaS, and SaaS tiers offered?

SECTION 3 — DATA HANDLING
ISO 27017 Ref: CLD.8.1.5, 8.1.2, 10.1.1, 10.1.2, 18.1.1

Q8.  In which geographic regions is customer data stored? Can customers restrict regions?
Q9.  Is customer data encrypted at rest? What algorithm and key length is used?
Q10. Is customer data encrypted in transit? What TLS version is the minimum?
Q11. Does the CSP offer customer-managed encryption keys (BYOK)? If yes, which services?
Q12. What is the data return procedure and format when a contract is terminated?
Q13. What is the timeline for complete deletion of customer data after termination?
Q14. Does the CSP provide a written certificate of deletion on request?

SECTION 4 — ACCESS CONTROL
ISO 27017 Ref: 9.2.3, 9.4.2, CLD.12.1.5

Q15. How is CSP administrator access to customer environments controlled?
Q16. Is MFA required for CSP administrator accounts? Provide evidence.
Q17. Are CSP administrator accesses to customer data logged? Are these logs available to the customer?
Q18. Is formal approval required before a CSP administrator accesses a customer environment?

SECTION 5 — MONITORING AND LOGGING
ISO 27017 Ref: CLD.12.4.5, 12.4.1, 12.4.2, 12.4.3

Q19. What security events are logged for each customer tenancy?
Q20. How long are security logs retained?
Q21. Can customers access their own logs? Via what mechanism (API, dashboard, export)?
Q22. Can logs be exported to the customer's own SIEM?

SECTION 6 — INCIDENT RESPONSE
ISO 27017 Ref: 16.1.1, 16.1.2, 16.1.7

Q23. Within what timeframe will the CSP notify customers of a security incident affecting their data?
Q24. What is the process for notifying customers of incidents?
Q25. Does the CSP cooperate with customer forensic investigations?

SECTION 7 — BUSINESS CONTINUITY
ISO 27017 Ref: 17.2.1, 17.1.2

Q26. What is the published availability SLA (uptime %) for the service?
Q27. What are the RPO and RTO commitments?
Q28. What redundancy mechanisms are in place (multi-region, geo-replication)?
Q29. How frequently is failover tested?

SECTION 8 — SUPPLY CHAIN
ISO 27017 Ref: 15.1.1, 15.2.1

Q30. Who are the sub-processors / sub-service providers with access to customer data?
Q31. Are sub-processors subject to equivalent security requirements? How is this enforced?
Q32. How is the customer notified of changes to sub-processors?
===================================================================================
```

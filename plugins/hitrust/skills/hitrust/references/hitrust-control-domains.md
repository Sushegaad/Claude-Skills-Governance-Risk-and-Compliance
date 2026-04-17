# HITRUST CSF Control Domains Reference
## HITRUST Common Security Framework v9.x — Control Categories, Objectives, and Specifications

This reference covers all 14 control categories, their control objectives, and the
associated control specifications. Specification IDs follow the convention:
`<Category Number>.<Objective Letter>.<Specification Number>`
(e.g., `01.a.1` = Category 01, Objective a, Specification 1).

---

## Table of Contents
1. [00 — Information Security Management Program](#00--information-security-management-program)
2. [01 — Access Control](#01--access-control)
3. [02 — Human Resources Security](#02--human-resources-security)
4. [03 — Risk Management](#03--risk-management)
5. [04 — Security Policy](#04--security-policy)
6. [05 — Organization of Information Security](#05--organization-of-information-security)
7. [06 — Compliance](#06--compliance)
8. [07 — Asset Management](#07--asset-management)
9. [08 — Physical and Environmental Security](#08--physical-and-environmental-security)
10. [09 — Communications and Operations Management](#09--communications-and-operations-management)
11. [10 — Information Systems Acquisition, Development, and Maintenance](#10--information-systems-acquisition-development-and-maintenance)
12. [11 — Information Security Incident Management](#11--information-security-incident-management)
13. [12 — Business Continuity Management](#12--business-continuity-management)
14. [13 — Privacy Practices](#13--privacy-practices)

---

## 00 — Information Security Management Program

**Purpose:** Establish and maintain an overarching information security management program that
governs the organization's approach to protecting information assets.

### Objective 00.a — Information Security Management Program

| Specification | Title | Description |
|--------------|-------|-------------|
| 00.a.1 | Information Security Management Program | The organization must have a documented, maintained, and communicated information security management program that includes an information security framework, roles and responsibilities, and resources. The program must be reviewed at planned intervals or when significant changes occur. |

**Key Policy/Procedure:** Information Security Program Charter or Policy

**Evidence for assessors:**
- Information Security Program documentation
- Evidence of executive sponsorship (signed policy, board approval)
- Program review records and revision history

---

## 01 — Access Control

**Purpose:** Limit access to information and information systems to authorized users,
processes acting on behalf of authorized users, and devices (including other information
systems).

### Objective 01.a — Access Control Policy

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.a.1 | Access Control Policy | A formal, documented access control policy must be established, covering the business requirements for access control, user access management, system and network access, and operating system access control. The policy must be reviewed and updated at a defined review interval. |

### Objective 01.b — User Registration

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.b.1 | User Registration | A formal user registration and deregistration process must exist for granting and revoking access. Access must be granted based on business need-to-know and least privilege. Account provisioning must require documented approval. Accounts must be reviewed and removed when no longer required. |

### Objective 01.c — Privilege Management

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.c.1 | Privilege Management | Privileged access (administrative rights) must be allocated on a need-to-use basis and must not be granted to general user accounts. Privileged accounts must use a separate, unique identifier from standard accounts. |

### Objective 01.d — User Password Management

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.d.1 | User Password Management | Passwords must meet minimum complexity, minimum length (minimum 8 characters for standard users, minimum 15 for privileged accounts), and must be changed at defined intervals. Default passwords must be changed before system deployment. Password history enforcement must prevent reuse. |

### Objective 01.e — Review of User Access Rights

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.e.1 | Review of User Access Rights | Access rights and privileges must be formally reviewed at regular intervals (at minimum annually) to ensure access remains appropriate. Results of reviews must be documented. Access must be revised or removed where the review identifies it is no longer required. |

### Objective 01.f — Use of System Utilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.f.1 | Use of System Utilities | System utilities that can override system and application controls must be restricted, controlled, and monitored. Use of privileged system utilities must be logged. |

### Objective 01.g — Clear Desk and Clear Screen Policy

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.g.1 | Clear Desk and Clear Screen Policy | A clear desk policy for papers and removable storage media and a clear screen policy for information processing facilities must be adopted and enforced. Unattended workstations must auto-lock within a defined period. |

### Objective 01.h — Remote Diagnostic and Configuration Port Protection

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.h.1 | Remote Diagnostic and Configuration Port Protection | Physical and logical access to diagnostic and configuration ports must be controlled. Unused ports must be disabled. Access to diagnostic ports must be logged. |

### Objective 01.i — Segregation in Networks

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.i.1 | Segregation in Networks | Groups of information services, users, and information systems must be segregated on networks. Network segmentation between trusted and untrusted networks (e.g., Internet, partner networks) must use firewalls or equivalent controls. Systems that process or store sensitive information must be placed in a separate network segment. |

### Objective 01.j — Network Connection Control

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.j.1 | Network Connection Control | The network access capability of users must be restricted consistent with the access control policy and requirements. Connections must be restricted based on the principle of least privilege. |

### Objective 01.k — Network Routing Control

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.k.1 | Network Routing Control | Routing controls must be implemented for networks to ensure computer connections and information flows do not breach the access control policy. |

### Objective 01.l — Automated Information Systems Access

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.l.1 | Automated Information Systems Access | Automated access controls (e.g., RBAC, MAC) must be implemented to enforce the access control policy. Access must be based on job function and least privilege. |

### Objective 01.m — Session Lock / Timeout

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.m.1 | Session Lock / Timeout | Information systems must enforce a session lock with a concealed screen after a defined period of inactivity. Users must re-authenticate to resume access. |

### Objective 01.n — Monitoring System Access and Use

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.n.1 | Monitoring System Access and Use | Procedures to monitor the use of information systems must be established. Monitoring results must be reviewed regularly. Suspicious activity must be investigated and escalated. |

### Objective 01.o — Network Boundary Protection

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.o.1 | Network Boundary Protection | The information system must monitor and control communications at the external boundary and key internal boundaries. The system must employ boundary protection devices. |

### Objective 01.p — Wireless Access Management

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.p.1 | Wireless Access Management | Wireless access to information systems must be managed and controlled. Unauthorized wireless access points must be detected and disabled. Wireless encryption (minimum WPA2 / WPA3) must be enforced. |

### Objective 01.q — Remote Access Management

| Specification | Title | Description |
|--------------|-------|-------------|
| 01.q.1 | Remote Access Management | Remote access must use encrypted communications (VPN, TLS). Multi-factor authentication must be enforced for remote access to systems that store, process, or transmit sensitive information. Remote sessions must be monitored and logged. |

---

## 02 — Human Resources Security

**Purpose:** Ensure that employees and contractors understand their responsibilities, are
suitable for the roles they are being considered for, and that the organization is protected
in the event of changes or terminations.

### Objective 02.a — Roles and Responsibilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 02.a.1 | Roles and Responsibilities | Information security roles and responsibilities must be defined, documented, and communicated to all employees, contractors, and third-party users as part of their employment or engagement terms. |

### Objective 02.b — Screening

| Specification | Title | Description |
|--------------|-------|-------------|
| 02.b.1 | Screening | Background verification checks must be carried out on all candidates for employment who will have access to sensitive information, consistent with relevant laws and regulations. The depth of screening must be proportional to the sensitivity of information accessed. |

### Objective 02.c — Terms and Conditions of Employment

| Specification | Title | Description |
|--------------|-------|-------------|
| 02.c.1 | Terms and Conditions of Employment | The contractual agreements with employees and contractors must state their responsibilities for information security. This includes acceptable use, confidentiality, and obligations that apply after termination. |

### Objective 02.d — Management Responsibilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 02.d.1 | Management Responsibilities | Management must require employees, contractors, and third-party users to apply security in accordance with established policies and procedures. |

### Objective 02.e — Security Awareness, Education, and Training

| Specification | Title | Description |
|--------------|-------|-------------|
| 02.e.1 | Security Awareness, Education, and Training | All employees and relevant third-party users must receive appropriate security awareness training. Training must be completed upon hire and at least annually. Training must cover the organization's policies, procedures, and threats relevant to their role. Training completion must be tracked. |

### Objective 02.f — Disciplinary Process

| Specification | Title | Description |
|--------------|-------|-------------|
| 02.f.1 | Disciplinary Process | A formal and documented disciplinary process must exist for employees who have committed a security breach or policy violation. |

### Objective 02.g — Termination Responsibilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 02.g.1 | Termination Responsibilities | Responsibilities for the termination or change of employment must be defined and assigned. Processes must ensure that access rights are removed and assets returned upon departure. |

### Objective 02.h — Return of Assets

| Specification | Title | Description |
|--------------|-------|-------------|
| 02.h.1 | Return of Assets | All employees and contractors must return all organizational assets in their possession upon termination or change of role. This includes devices, storage media, identity credentials, and physical keys or access cards. |

### Objective 02.i — Removal of Access Rights

| Specification | Title | Description |
|--------------|-------|-------------|
| 02.i.1 | Removal of Access Rights | Access rights to information and information systems must be removed upon termination or change of employment. Changes in role must trigger an access rights review. Access removal must occur on the effective date of departure. |

---

## 03 — Risk Management

**Purpose:** Establish and maintain a risk management programme to identify, assess, treat,
and monitor information risks.

### Objective 03.a — Risk Management Program Development

| Specification | Title | Description |
|--------------|-------|-------------|
| 03.a.1 | Risk Management Program Development | The organization must develop a documented risk management programme that includes the risk management methodology, organisational risk tolerance, assignment of roles and responsibilities, and a schedule for risk assessments. |

### Objective 03.b — Performing Risk Assessments

| Specification | Title | Description |
|--------------|-------|-------------|
| 03.b.1 | Performing Risk Assessments | Risk assessments must be performed at defined intervals (at minimum annually) and when significant changes occur to information systems or the operational environment. Risk assessments must identify threats, vulnerabilities, likelihood, impact, and existing controls. Results must be documented and reviewed by management. |

### Objective 03.c — Risk Mitigation

| Specification | Title | Description |
|--------------|-------|-------------|
| 03.c.1 | Risk Mitigation | A risk treatment plan must be developed to address identified risks. The plan must include selected treatment options (accept, avoid, transfer, mitigate), assigned owners, timelines, and residual risk assessment. Treatment must be implemented and tracked. |

### Objective 03.d — Risk Evaluation

| Specification | Title | Description |
|--------------|-------|-------------|
| 03.d.1 | Risk Evaluation | Residual risks must be evaluated after treatment. Management must formally accept residual risks at or below the organization's defined risk tolerance. Risk evaluation must be documented and retained. |

---

## 04 — Security Policy

**Purpose:** Provide direction and support for information security in accordance with
business requirements and relevant laws and regulations.

### Objective 04.a — Information Security Policy Document

| Specification | Title | Description |
|--------------|-------|-------------|
| 04.a.1 | Information Security Policy Document | An information security policy document must be approved by management, published, and communicated to all employees and external parties as relevant. The policy must address general direction, principles, and requirements for protecting information. |

### Objective 04.b — Review of the Information Security Policy

| Specification | Title | Description |
|--------------|-------|-------------|
| 04.b.1 | Review of the Information Security Policy | The information security policy must be reviewed at planned intervals (at minimum annually) and in response to significant events or changes in the threat environment, business, or regulatory requirements. Reviews must be documented. |

---

## 05 — Organization of Information Security

**Purpose:** Establish a management framework to initiate and control the implementation
of information security within the organization, and to manage third-party relationships
securely.

### Objective 05.a — Management Commitment to Information Security

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.a.1 | Management Commitment to Information Security | Management must actively support security within the organization through clear direction, demonstrated commitment, explicit assignment, and acknowledgment of information security responsibilities. |

### Objective 05.b — Information Security Coordination

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.b.1 | Information Security Coordination | Information security activities must be coordinated across the organization by representatives from different parts of the organization with relevant roles and job functions. |

### Objective 05.c — Allocation of Information Security Responsibilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.c.1 | Allocation of Information Security Responsibilities | All information security responsibilities must be defined and allocated. An information security function with clearly defined responsibilities must exist. |

### Objective 05.d — Authorization Process for Information Processing Facilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.d.1 | Authorization Process | A management authorization process must be in place for new information processing facilities. |

### Objective 05.e — Confidentiality Agreements

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.e.1 | Confidentiality Agreements | Requirements for confidentiality or non-disclosure agreements must be identified and reviewed regularly. Employees, contractors, and third parties with access to sensitive information must sign appropriate NDAs. |

### Objective 05.f — Contact with Authorities

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.f.1 | Contact with Authorities | Appropriate contacts with relevant authorities must be maintained, including law enforcement and regulatory bodies that must be notified in the event of a security incident or data breach. |

### Objective 05.g — Contact with Special Interest Groups

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.g.1 | Contact with Special Interest Groups | Appropriate contacts with special interest groups or other specialist security forums and industry associations must be maintained to stay informed of threat intelligence and best practices. |

### Objective 05.h — Independent Review of Information Security

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.h.1 | Independent Review of Information Security | The organization's approach to managing information security and its implementation must be reviewed independently at planned intervals or when significant changes occur. |

### Objective 05.i — Identification of Risks Related to External Parties

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.i.1 | Identification of Risks Related to External Parties | Risks to the organization's information and information systems from third-party processes must be identified and controls implemented before granting access. |

### Objective 05.j — Addressing Security when Dealing with Customers

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.j.1 | Addressing Security when Dealing with Customers | Information security requirements for customer-facing services and systems must be identified and addressed in service agreements. |

### Objective 05.k — Addressing Security in Third-Party Agreements

| Specification | Title | Description |
|--------------|-------|-------------|
| 05.k.1 | Addressing Security in Third-Party Agreements | Agreements with third parties involving access to, processing, communication, or management of the organization's information or systems must include security requirements. Business Associate Agreements (BAAs) must be in place where required by HIPAA. |

---

## 06 — Compliance

**Purpose:** Avoid breaches of legal, regulatory, or contractual obligations related to
information security and of any security requirements.

### Objective 06.a — Identification of Applicable Legislation

| Specification | Title | Description |
|--------------|-------|-------------|
| 06.a.1 | Identification of Applicable Legislation | All relevant legislative, regulatory, and contractual requirements and the organization's approach to meeting those requirements must be explicitly identified, documented, and kept up to date. |

### Objective 06.b — Intellectual Property Rights

| Specification | Title | Description |
|--------------|-------|-------------|
| 06.b.1 | Intellectual Property Rights | Appropriate procedures must be implemented to ensure compliance with legislative, regulatory, and contractual requirements on the use of material in respect of which there may be intellectual property rights. |

### Objective 06.c — Protection of Organizational Records

| Specification | Title | Description |
|--------------|-------|-------------|
| 06.c.1 | Protection of Organizational Records | Important records must be protected from loss, destruction, falsification, unauthorized access, and unauthorized release, in accordance with legal, regulatory, contractual, and business requirements. Retention schedules must be documented and enforced. |

### Objective 06.d — Data Protection and Privacy

| Specification | Title | Description |
|--------------|-------|-------------|
| 06.d.1 | Data Protection and Privacy of Personal Information | The protection of personal data and privacy must be ensured as required by relevant legislation and regulations (including HIPAA, state breach notification laws, and other applicable privacy requirements). A data protection officer or privacy officer role must be defined where required. |

### Objective 06.e — Prevention of Misuse of Information Processing Facilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 06.e.1 | Prevention of Misuse of Information Processing Facilities | Users must be deterred from using information processing facilities for unauthorized purposes. Acceptable use must be defined, communicated, and acknowledged by users. |

### Objective 06.f — Regulation of Cryptographic Controls

| Specification | Title | Description |
|--------------|-------|-------------|
| 06.f.1 | Regulation of Cryptographic Controls | The organization must comply with agreements, laws, and regulations on the use of cryptographic controls, including use of encryption, export/import restrictions, and key management obligations. |

### Objective 06.g — Technical Compliance Review

| Specification | Title | Description |
|--------------|-------|-------------|
| 06.g.1 | Technical Compliance Review | Information systems must be regularly reviewed for compliance with the organization's security policies and standards. Technical compliance reviews must include vulnerability scans and configuration assessments. |

### Objective 06.h — System Audit Controls

| Specification | Title | Description |
|--------------|-------|-------------|
| 06.h.1 | System Audit Controls | Audit requirements and activities involving verification of operational systems must be carefully planned to minimize disruptions to business processes. Access to system audit tools must be protected to prevent misuse or compromise. |

---

## 07 — Asset Management

**Purpose:** Identify organizational assets and define appropriate protection responsibilities.

### Objective 07.a — Inventory of Assets

| Specification | Title | Description |
|--------------|-------|-------------|
| 07.a.1 | Inventory of Assets | All assets associated with information and information processing facilities must be identified and an inventory of these assets must be drawn up and maintained. The inventory must include owner, location, classification, and criticality. |

### Objective 07.b — Ownership of Assets

| Specification | Title | Description |
|--------------|-------|-------------|
| 07.b.1 | Ownership of Assets | All information and information processing assets must have a designated owner. Asset owners must be accountable for maintaining appropriate protection of the asset. |

### Objective 07.c — Acceptable Use of Assets

| Specification | Title | Description |
|--------------|-------|-------------|
| 07.c.1 | Acceptable Use of Assets | Rules for the acceptable use of information and assets associated with information processing facilities must be identified, documented, and implemented. |

### Objective 07.d — Classification of Information

| Specification | Title | Description |
|--------------|-------|-------------|
| 07.d.1 | Classification Guidelines | Information must be classified in terms of its sensitivity and criticality, with a documented classification scheme. The scheme must at minimum define handling requirements for sensitive/confidential and restricted information including ePHI. |

### Objective 07.e — Information Labeling and Handling

| Specification | Title | Description |
|--------------|-------|-------------|
| 07.e.1 | Information Labeling and Handling | Procedures for information labeling and handling must be developed and implemented in accordance with the classification scheme. |

### Objective 07.f — Management of Removable Media

| Specification | Title | Description |
|--------------|-------|-------------|
| 07.f.1 | Management of Removable Media | Procedures must be in place for the management of removable media, including authorization for use, encryption requirements, inventory, and controls to prevent unauthorized data extraction. |

### Objective 07.g — Disposal of Media

| Specification | Title | Description |
|--------------|-------|-------------|
| 07.g.1 | Disposal of Media | Media that is no longer required must be disposed of securely and safely using documented procedures. Disposal methods must render data unrecoverable (e.g., degaussing, physical destruction, certified wiping). Certificates of destruction must be obtained and retained. |

### Objective 07.h — Physical Media in Transit

| Specification | Title | Description |
|--------------|-------|-------------|
| 07.h.1 | Physical Media in Transit | Media containing information must be protected against unauthorized access, misuse, or corruption during transportation. Chain of custody must be documented for sensitive media in transit. |

---

## 08 — Physical and Environmental Security

**Purpose:** Prevent unauthorized physical access, damage, and interference to organizational
information and information processing facilities.

### Objective 08.a — Physical Security Perimeter

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.a.1 | Physical Security Perimeter | Security perimeters (e.g., walls, card-controlled entry gates or staffed reception desks) must be used to protect areas that contain sensitive information and information processing facilities. |

### Objective 08.b — Physical Entry Controls

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.b.1 | Physical Entry Controls | Secure areas must be protected by appropriate entry controls to ensure that only authorized personnel are allowed access. Access must be logged and reviewed. |

### Objective 08.c — Securing Offices, Rooms, and Facilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.c.1 | Securing Offices, Rooms, and Facilities | Physical security for offices, rooms, and facilities must be designed and applied, taking account of relevant health and safety regulations and standards. |

### Objective 08.d — Protecting Against External and Environmental Threats

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.d.1 | Protecting Against Environmental Threats | Physical protection against natural disasters, malicious attack, or accidents must be designed and applied. Environmental controls (fire suppression, temperature, humidity) must be implemented for data centres and server rooms. |

### Objective 08.e — Working in Secure Areas

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.e.1 | Working in Secure Areas | Physical protection and guidelines for working in secure areas must be designed and applied. Visitors must be supervised while in secure areas. |

### Objective 08.f — Public Access, Delivery, and Loading Areas

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.f.1 | Delivery and Loading Areas | Access to delivery and loading areas from outside buildings must be controlled and, where possible, isolated from information processing facilities to avoid unauthorized access. |

### Objective 08.g — Equipment Siting and Protection

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.g.1 | Equipment Siting and Protection | Equipment must be sited and protected to reduce the risks from environmental threats and hazards, and opportunities for unauthorized access. |

### Objective 08.h — Supporting Utilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.h.1 | Supporting Utilities | Equipment must be protected from power failures and other disruptions caused by failures in supporting utilities (power, UPS, HVAC, water). Redundancy must be implemented for critical systems. |

### Objective 08.i — Cabling Security

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.i.1 | Cabling Security | Power and telecommunications cabling carrying data or supporting information services must be protected from interception or damage. |

### Objective 08.j — Equipment Maintenance

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.j.1 | Equipment Maintenance | Equipment must be correctly maintained to ensure its continued availability and integrity. Maintenance must follow manufacturer recommendations and must be documented. |

### Objective 08.k — Security of Equipment Off-Premises

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.k.1 | Security of Equipment Off-Premises | Security must be applied to off-site equipment, taking into account the different risks of working outside the organization's premises. Laptops and mobile devices used off-site must be encrypted. |

### Objective 08.l — Secure Disposal or Reuse of Equipment

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.l.1 | Secure Disposal or Reuse of Equipment | All items of equipment containing storage media must be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or reuse. |

### Objective 08.m — Removal of Property

| Specification | Title | Description |
|--------------|-------|-------------|
| 08.m.1 | Removal of Property | Equipment, information, or software must not be taken off-site without prior authorization. Records of assets removed must be maintained. |

---

## 09 — Communications and Operations Management

**Purpose:** Ensure the correct and secure operation of information processing facilities,
and control changes to systems with documented procedures.

### Objective 09.a — Documented Operating Procedures

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.a.1 | Documented Operating Procedures | Operating procedures must be documented, maintained, and made available to all users who need them. |

### Objective 09.b — Change Management

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.b.1 | Change Management | Changes to information systems and processing facilities must be controlled through a formal change management process requiring risk assessment, testing, documented approval, and rollback planning. |

### Objective 09.c — Segregation of Duties

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.c.1 | Segregation of Duties | Duties and areas of responsibility must be segregated to reduce opportunities for unauthorized or unintentional modification or misuse of the organization's assets. |

### Objective 09.d — Separation of Development, Test, and Production Environments

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.d.1 | Separation of Development and Production | Development, testing, and operational environments must be separated and controls must be in place to reduce the risk of unauthorized access or changes to operational systems. Real PHI or sensitive data must not be used in test/development environments unless de-identified or with equivalent controls. |

### Objective 09.e — Service Delivery Management

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.e.1 | Service Delivery | Service delivery agreements with third parties must include security requirements. Service delivery must be monitored to ensure services are delivered in accordance with agreements. |

### Objective 09.f — Monitoring and Review of Third-Party Services

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.f.1 | Monitoring and Review of Third-Party Services | Services, reports, and records provided by third parties must be regularly monitored and reviewed. Audit rights must be established in third-party agreements. |

### Objective 09.g — Managing Changes to Third-Party Services

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.g.1 | Managing Changes to Third-Party Services | Changes to the provision of services, including maintaining and improving existing information security policies, procedures, and controls, must be managed taking into account the criticality of business systems and processes involved. |

### Objective 09.h — Capacity Management

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.h.1 | Capacity Management | The use of resources must be monitored and tuned, and projections must be made for future capacity requirements to ensure the required system performance. |

### Objective 09.i — System Acceptance

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.i.1 | System Acceptance | Acceptance criteria for new information systems, upgrades, and new versions must be established and suitable tests of the system carried out before acceptance. |

### Objective 09.j — Controls Against Malicious Code

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.j.1 | Controls Against Malicious Code | Detection, prevention, and recovery controls to protect against malicious code must be implemented. Anti-malware software (including endpoint protection) must be deployed on all user workstations and servers. Definitions must be kept current. |

### Objective 09.k — Controls Against Mobile Code

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.k.1 | Controls Against Mobile Code | Mobile code (e.g., scripts, applets, browser-based code) must be authorized before use. Unauthorized mobile code must be blocked. Configuration must prevent execution of unauthorized mobile code. |

### Objective 09.l — Information Backup

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.l.1 | Information Backup | Backup copies of information and software must be created and tested regularly in accordance with an agreed backup policy. Backups must be stored securely, including off-site copies. Backups containing ePHI must be encrypted. Recovery procedures must be tested at defined intervals. |

### Objective 09.m — Network Security Management

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.m.1 | Network Security Management | Networks must be adequately managed to protect systems and applications. Network security controls must include firewalls, intrusion detection/prevention systems, and monitoring. |

### Objective 09.n — Security of Network Services

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.n.1 | Security of Network Services | Security features, service levels, and management requirements of all network services must be identified and included in network service agreements. |

### Objective 09.o — Exchange of Information

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.o.1 | Exchange of Information Policies and Procedures | Policies, procedures, and controls must be in place to protect the exchange of information through the use of all types of communication facilities. |

### Objective 09.p — Electronic Messaging / Email Security

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.p.1 | Electronic Messaging | Information involved in electronic messaging must be appropriately protected. PHI must not be transmitted in unencrypted email. Encryption or secure messaging solutions must be used for ePHI transmission. |

### Objective 09.q — E-Commerce Services

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.q.1 | E-Commerce Services | Information involved in e-commerce passing over public networks must be protected from fraudulent activity, contract dispute, and unauthorized disclosure. |

### Objective 09.r — Audit Logging

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.r.1 | Audit Logging | Audit logs recording user activities, exceptions, and information security events must be maintained for an agreed period. Log retention must comply with applicable regulatory requirements (HIPAA: minimum 6 years). Logs must capture: user ID, date/time, event type, success/failure, and affected data. |

### Objective 09.s — Monitoring System Use

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.s.1 | Monitoring System Use | Procedures for monitoring use of information systems must be established and the results regularly reviewed. High-risk activities and access to ePHI must be actively monitored. |

### Objective 09.t — Protection of Log Information

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.t.1 | Protection of Log Information | Logging facilities and log information must be protected against tampering and unauthorized access. Logs must be stored in a separate, secure system from the systems they monitor. |

### Objective 09.u — Clock Synchronization

| Specification | Title | Description |
|--------------|-------|-------------|
| 09.u.1 | Clock Synchronization | The clocks of all relevant information processing systems must be synchronised with an agreed accurate time source (NTP). Time consistency is essential for correlating security events across systems. |

---

## 10 — Information Systems Acquisition, Development, and Maintenance

**Purpose:** Ensure that information security is an integral part of information systems
across their entire lifecycle, and ensure that systems are developed, acquired, and maintained
securely.

### Objective 10.a — Security Requirements Analysis and Specification

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.a.1 | Security Requirements Analysis | Security requirements must be included in requirements for new information systems or enhancements to existing information systems. |

### Objective 10.b — Input Data Validation

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.b.1 | Input Data Validation | Data input to applications must be validated to ensure that this data is correct and appropriate. Validation controls must address injection attacks (SQL injection, XSS, command injection). |

### Objective 10.c — Control of Internal Processing

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.c.1 | Control of Internal Processing | Validation checks must be incorporated into applications to detect any corruption of information through processing errors or deliberate acts. |

### Objective 10.d — Message Integrity

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.d.1 | Message Integrity | Requirements for ensuring authenticity and protecting message integrity in applications must be identified and appropriate controls implemented. |

### Objective 10.e — Output Data Validation

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.e.1 | Output Data Validation | Data output from an application must be validated to ensure that the processing of stored information is correct and appropriate to the circumstances. |

### Objective 10.f — Policy on the Use of Cryptographic Controls

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.f.1 | Policy on the Use of Cryptographic Controls | A policy for the use of cryptographic controls for protection of information must be developed and implemented. Minimum encryption standards must be defined: AES-256 for data at rest, TLS 1.2 or higher for data in transit. |

### Objective 10.g — Key Management

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.g.1 | Key Management | Key management must include key generation, distribution, storage, retirement, and destruction. Keys must be protected against unauthorised access. Key management responsibilities must be assigned. |

### Objective 10.h — Control of Technical Vulnerabilities

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.h.1 | Control of Technical Vulnerabilities | Timely information about technical vulnerabilities of information systems in use must be obtained, the organization's exposure to such vulnerabilities evaluated, and appropriate measures taken to address the associated risk. Vulnerability scans must be conducted at defined intervals (minimum quarterly for internal systems; monthly for internet-facing assets). |

### Objective 10.i — Restrictions on Changes to Software Packages

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.i.1 | Restrictions on Changes to Software Packages | Modifications to software packages must be discouraged. Where necessary, changes should be limited to necessary modifications and all changes must be strictly controlled. |

### Objective 10.j — Protection of System Test Data

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.j.1 | Protection of System Test Data | Test data must be selected carefully, protected, and controlled. ePHI and sensitive production data must not be used in test environments. Where necessary, production data used in testing must be masked, anonymised, or replaced with synthetic data. |

### Objective 10.k — Access Control to Program Source Code

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.k.1 | Access Control to Program Source Code | Access to program source code must be restricted to authorized personnel. Code repositories must have access controls, audit logging, and change tracking. |

### Objective 10.l — Outsourced Software Development

| Specification | Title | Description |
|--------------|-------|-------------|
| 10.l.1 | Outsourced Software Development | Outsourced software development must be supervised and monitored by the organization. Security requirements must be included in outsourcing contracts. Code reviews and security testing must be performed before deployment. |

---

## 11 — Information Security Incident Management

**Purpose:** Ensure a consistent and effective approach to the management of information
security incidents, including communication on security events and weaknesses.

### Objective 11.a — Reporting Information Security Events

| Specification | Title | Description |
|--------------|-------|-------------|
| 11.a.1 | Reporting Information Security Events | Information security events must be reported through appropriate management channels as quickly as possible. A formal incident reporting procedure must exist. All staff must be aware of how to report security events and must be encouraged to report suspected events promptly. |

### Objective 11.b — Reporting Security Weaknesses

| Specification | Title | Description |
|--------------|-------|-------------|
| 11.b.1 | Reporting Security Weaknesses | All employees, contractors, and third-party users must be required to note and report any observed or suspected security weaknesses in systems or services. |

### Objective 11.c — Responsibilities and Procedures

| Specification | Title | Description |
|--------------|-------|-------------|
| 11.c.1 | Responsibilities and Procedures | Management responsibilities and procedures must be established to ensure a quick, effective, and orderly response to information security incidents. An Incident Response Plan (IRP) must be documented, tested, and maintained. The IRP must include: roles and responsibilities, communication procedures, escalation criteria, containment, eradication, recovery, post-incident review, and HIPAA breach notification assessment. |

### Objective 11.d — Learning from Information Security Incidents

| Specification | Title | Description |
|--------------|-------|-------------|
| 11.d.1 | Learning from Information Security Incidents | Mechanisms must be in place to enable the types, volumes, and costs of information security incidents to be quantified and monitored. Lessons learned from incidents must be documented and used to improve the security programme. |

### Objective 11.e — Collection of Evidence

| Specification | Title | Description |
|--------------|-------|-------------|
| 11.e.1 | Collection of Evidence | Where a follow-up action against a person or organization involves legal action or disciplinary proceedings, evidence must be collected, retained, and presented in a manner that conforms to legal requirements. Chain of custody must be maintained for digital forensic evidence. |

---

## 12 — Business Continuity Management

**Purpose:** Counteract interruptions to business activities and to protect critical business
processes from the effects of major failures of information systems or disasters, to ensure
their timely resumption.

### Objective 12.a — Including Information Security in Business Continuity

| Specification | Title | Description |
|--------------|-------|-------------|
| 12.a.1 | Including Information Security in Business Continuity | A managed process must be developed and maintained for business continuity throughout the organization that addresses the information security requirements needed during an adverse situation. |

### Objective 12.b — Business Continuity and Risk Assessment

| Specification | Title | Description |
|--------------|-------|-------------|
| 12.b.1 | Business Continuity and Risk Assessment | Events that can cause interruptions to business processes must be identified, along with the probability and impact of such interruptions and their consequences for information security. Business Impact Analysis (BIA) must be performed and documented. |

### Objective 12.c — Developing and Implementing Continuity Plans

| Specification | Title | Description |
|--------------|-------|-------------|
| 12.c.1 | Developing and Implementing Continuity Plans | Plans must be developed and implemented to maintain or restore operations and ensure availability of information at the required level and in the required timescales following interruption or failure. Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) must be defined and documented for critical systems and data. |

### Objective 12.d — Business Continuity Planning Framework

| Specification | Title | Description |
|--------------|-------|-------------|
| 12.d.1 | Business Continuity Planning Framework | A single framework of business continuity plans must be maintained to ensure all plans are consistent, and to identify priorities for testing and maintenance. |

### Objective 12.e — Testing, Maintaining, and Re-Assessing Continuity Plans

| Specification | Title | Description |
|--------------|-------|-------------|
| 12.e.1 | Testing, Maintaining, and Re-Assessing Plans | Business continuity plans must be tested and updated regularly to ensure they are up to date and effective. Tests must occur at minimum annually and after significant changes. Test results and lessons learned must be documented. |

---

## 13 — Privacy Practices

**Purpose:** Ensure the organization handles protected health information (PHI) and other
sensitive personal information in accordance with applicable privacy regulations, including
HIPAA and relevant state laws.

This category directly aligns with HIPAA Privacy Rule requirements (45 CFR Part 164,
Subpart E) and applies to Covered Entities and Business Associates.

### Objective 13.a — Privacy Notice

| Specification | Title | Description |
|--------------|-------|-------------|
| 13.a.1 | Notice of Privacy Practices | Covered Entities must provide individuals with a notice of their privacy practices (NPP). The NPP must describe: uses and disclosures of PHI, patient rights, the CE's legal duties, and how complaints can be filed. The NPP must be made available at first service and upon request. |

### Objective 13.b — Security Safeguards for PHI

| Specification | Title | Description |
|--------------|-------|-------------|
| 13.b.1 | Security Safeguards | Administrative, physical, and technical safeguards must be in place to protect the confidentiality, integrity, and availability of ePHI. A Security Risk Analysis must be performed and documented. A Risk Management Plan must exist to mitigate identified risks. |

### Objective 13.c — Transmission Security for PHI

| Specification | Title | Description |
|--------------|-------|-------------|
| 13.c.1 | Transmission Security | ePHI transmitted over electronic communications networks must be protected. Encryption must be used when transmitting ePHI over open networks. Mechanisms to ensure integrity of ePHI during transmission must be implemented. |

### Objective 13.d — Individual Access to PHI

| Specification | Title | Description |
|--------------|-------|-------------|
| 13.d.1 | Individual Access | Covered Entities must provide individuals with access to their PHI upon request, within the required timeframe (30 days, extendable once by 30 days). Processes for handling access requests, including verification, must be documented. |

### Objective 13.e — Amendment of PHI

| Specification | Title | Description |
|--------------|-------|-------------|
| 13.e.1 | Amendment | Covered Entities must provide individuals with the ability to request amendment to their PHI. Processes for accepting, denying, and tracking amendment requests must be documented. |

### Objective 13.f — Minimum Necessary Standard

| Specification | Title | Description |
|--------------|-------|-------------|
| 13.f.1 | Minimum Necessary | Covered Entities and Business Associates must make reasonable efforts to use, disclose, and request only the minimum amount of PHI necessary to accomplish the intended purpose. Procedures must define what constitutes minimum necessary for routine disclosures. |

### Objective 13.g — Accounting of Disclosures

| Specification | Title | Description |
|--------------|-------|-------------|
| 13.g.1 | Accounting of Disclosures | Covered Entities must be capable of providing individuals with an accounting of certain disclosures of their PHI made for purposes other than treatment, payment, or healthcare operations. Disclosure tracking must be maintained for 6 years. |

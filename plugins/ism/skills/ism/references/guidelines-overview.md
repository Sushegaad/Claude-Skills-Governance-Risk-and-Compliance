# ISM - 22 Guideline Chapters Overview

Source: Australian Information Security Manual, March 2026 edition  
Published by: Australian Signals Directorate (ASD)  
URL: https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism

---

## Chapter Summary Table

| # | Chapter | Domain | Key Control Areas |
|---|---------|--------|------------------|
| 1 | Cyber Security Roles | Governance | CISO appointment, security responsibilities, accountability structures, security culture |
| 2 | Cyber Security Incidents | Detect/Respond | Incident definition, reporting obligations, response procedures, ASD notification |
| 3 | Procurement & Outsourcing | Governance | Supply chain security, vendor assessment, cloud service security requirements |
| 4 | Cyber Security Documentation | Governance | SSP, risk register, security policies, document classification and review |
| 5 | Physical Security | Protect | Secure areas, physical access controls, equipment security, clean desk |
| 6 | Personnel Security | Protect | Personnel screening, security clearances, user awareness, termination procedures |
| 7 | Communications Infrastructure | Protect | Cabling, network zoning, physical comms protection, signal security |
| 8 | Communications Systems | Protect | Voice systems, video conferencing, fax and messaging security |
| 9 | Enterprise Mobility | Protect | Mobile devices, BYOD, remote access, mobile device management (MDM) |
| 10 | Evaluated Products | Protect | Use of evaluated/certified products (Common Criteria, FIPS), cryptographic modules |
| 11 | IT Equipment | Protect | Hardware procurement, asset register, equipment disposal, TEMPEST |
| 12 | Media | Protect | Removable media controls, media sanitisation, media destruction |
| 13 | System Hardening | Protect | OS hardening, application hardening, firmware security, least privilege |
| 14 | System Management | Protect | Patch management, change management, backups, configuration management |
| 15 | System Monitoring | Detect | Logging requirements, SIEM, anomaly detection, audit log retention |
| 16 | Software Development | Protect | Secure SDLC, code review, dependency management, vulnerability disclosure |
| 17 | Database Systems | Protect | Database hardening, access controls, encryption at rest, query controls |
| 18 | Email | Protect | Email filtering, DMARC/SPF/DKIM, email content security, phishing controls |
| 19 | Networking | Protect | Network segmentation, firewall rules, DNS security, VPN standards |
| 20 | Cryptography | Protect | Approved algorithms, key management, PKI, TLS standards |
| 21 | Gateways | Protect | Content filtering, data diodes, cross-domain solutions, proxy security |
| 22 | Data Transfers | Protect | Approved transfer methods, data labelling, transfer logging |

---

## Chapter Detail

### Chapter 1 - Cyber Security Roles
- Organisations must appoint a Chief Information Security Officer (CISO) with appropriate authority
- Security responsibilities must be defined across all levels of the organisation
- A system owner must be designated for each ICT system
- Key controls cover: CISO role definition, security advisor appointments, escalation paths

### Chapter 2 - Cyber Security Incidents
- Defines a cyber security incident as any actual or suspected compromise of a system's confidentiality, integrity, or availability
- ASD must be notified of significant incidents - especially for systems handling PROTECTED and above
- Response procedures must be documented and tested
- Incident evidence must be preserved; post-incident reviews required
- Key controls: incident categorisation, notification timelines, forensic preservation, lessons learned

### Chapter 3 - Procurement & Outsourcing
- All ICT procurement must consider cyber security requirements before purchase
- Cloud services must be assessed for compliance with the ISM and ASD Cloud Security Guidance
- Outsourced services must contractually require ISM-aligned security controls
- Supply chain risks must be assessed and managed
- Key controls: vendor security assessments, contract clauses, cloud service provider evaluation

### Chapter 4 - Cyber Security Documentation
- Every system must have a current System Security Plan (SSP) - the primary authorisation document
- Risk registers must be maintained and reviewed
- Security policies and procedures must be version-controlled, approved by management, and reviewed at least annually
- Key documents: SSP, risk register, incident response plan, change management plan, business continuity plan

### Chapter 5 - Physical Security
- Secure areas must be established and access controlled
- Visitors must be escorted in secure areas
- Equipment must be protected from physical tampering
- Clean desk and clear screen policies required
- Key controls: physical access logs, secure area classifications, equipment labelling

### Chapter 6 - Personnel Security
- Personnel must be screened before access to sensitive systems
- Security clearances must match the classification level of systems accessed
- Security awareness training must be provided at onboarding and annually
- Access must be revoked promptly on termination
- Key controls: background checks, clearance validation, training records, offboarding checklist

### Chapter 7 - Communications Infrastructure
- Cabling must be protected from interception and damage
- Network zones must be established with appropriate separation
- Physical communications infrastructure in secure areas must be physically protected
- Key controls: cable labelling, conduit requirements, zone separation

### Chapter 8 - Communications Systems
- Voice over IP (VoIP) and video conferencing systems must be secured
- PSTN systems connected to secure networks require additional controls
- Fax and messaging systems handling sensitive information must use approved encryption
- Key controls: VoIP hardening, conferencing system security, messaging encryption

### Chapter 9 - Enterprise Mobility
- Mobile devices accessing government systems must be enrolled in an approved MDM solution
- BYOD must be managed through containerisation or equivalent
- Remote access must use approved VPN with MFA
- Lost or stolen devices must be remotely wipeable
- Key controls: MDM enrolment, remote wipe capability, MFA for remote access, mobile app vetting

### Chapter 10 - Evaluated Products
- Systems handling PROTECTED and above must use cryptographic products evaluated or approved by ASD
- Common Criteria evaluated products are preferred for high-assurance environments
- FIPS 140-2/3 validated modules required for classified cryptographic operations
- Key controls: product evaluation requirements, cryptographic module validation

### Chapter 11 - IT Equipment
- All ICT equipment must be recorded in an asset register
- Equipment must be disposed of securely (data sanitisation before disposal)
- Equipment in sensitive areas may require TEMPEST certification
- Key controls: asset register, equipment disposal procedures, TEMPEST assessment

### Chapter 12 - Media
- Removable media must be controlled and authorised
- Media used in classified environments must be treated at the classification level of the system
- Media must be sanitised (overwrite/degauss) or destroyed before disposal
- Key controls: removable media register, sanitisation procedures, destruction certificates

### Chapter 13 - System Hardening
- Operating systems must be hardened before deployment (remove unnecessary services, disable default accounts)
- Applications must be hardened (disable unused features, apply vendor hardening guides)
- Firmware security settings must be configured (Secure Boot, BIOS passwords)
- Least privilege must be enforced - no standing administrative access
- Key controls: OS hardening checklists, application allow-listing, firmware configuration, privileged access management

### Chapter 14 - System Management (the ISM names this "Guidelines for system management")
- Patches must be applied within the ISM timeframes: 48 hours for internet-facing services when an exploit exists or the vulnerability is being exploited, otherwise two weeks; one month for non-internet-facing systems
- Change management must follow a documented and approved process
- Backups must be tested regularly; backup media must be stored securely
- Configuration management must track all changes to system baseline
- Key controls: patch management SLAs, backup testing schedule, change approval process

### Chapter 15 - System Monitoring
- Centralised event logging must be implemented (SIEM or equivalent)
- Log retention: minimum 18 months for systems handling PROTECTED and above
- Anomalous events must trigger alerts and investigation
- Privileged access and system changes must be logged
- Key controls: log collection scope, retention periods, alerting thresholds, log integrity

### Chapter 16 - Software Development
- Software development must follow a secure Software Development Life Cycle (SDLC)
- Code reviews and vulnerability testing required before deployment
- Third-party dependencies must be tracked and patched
- Vulnerability disclosure policy required for externally facing systems
- Key controls: SDLC documentation, code review evidence, dependency scanning, pen testing

### Chapter 17 - Database Systems
- Databases must be hardened (remove default accounts, disable unnecessary features)
- Access to databases must follow least privilege
- Sensitive data at rest must be encrypted
- Database activity must be logged
- Key controls: database hardening checklist, access control matrix, encryption at rest, query logging

### Chapter 18 - Email
- Email gateways must implement DMARC, DKIM, and SPF
- Email filtering must block malicious attachments and phishing content
- Outbound emails containing sensitive information must be controlled
- Key controls: DMARC policy (reject), DKIM signing, SPF records, gateway filtering logs

### Chapter 19 - Networking
- Network segmentation must separate sensitive systems from general-purpose networks
- Firewall rule sets must be documented, reviewed, and audited
- DNS security extensions (DNSSEC) recommended
- VPNs must use approved encryption standards
- Key controls: network architecture diagram, firewall rule review schedule, DNSSEC configuration

### Chapter 20 - Cryptography
- Only ASD-approved cryptographic algorithms must be used
- TLS 1.2 minimum (TLS 1.3 preferred) for data in transit
- Key management must follow documented procedures (generation, storage, rotation, destruction)
- PKI must be underpinned by a trusted root CA
- Key controls: algorithm approval list, key management procedures, TLS version configuration, CA management

### Chapter 21 - Gateways
- Internet gateways must implement web content filtering
- Cross-domain solutions (CDS) required for moving information between classification levels
- Data diodes used for one-way transfers in high-security environments
- Gateway security must be regularly assessed
- Key controls: content filtering policy, CDS accreditation, gateway security assessments

### Chapter 22 - Data Transfers
- Data transfers between different classification domains must use approved methods
- All transfers of classified data must be logged
- Data must be labelled with its protective marking before transfer
- Key controls: approved transfer mechanisms, transfer logs, label verification procedures

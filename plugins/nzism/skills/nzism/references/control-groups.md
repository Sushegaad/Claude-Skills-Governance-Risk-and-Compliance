# NZISM Control Groups - Overview

This reference file summarises the key control domains of the New Zealand Information Security Manual (NZISM), published by GCSB/NCSC NZ. Use it when advising on specific control domains, conducting gap analyses, or generating domain-specific policies.

The NZISM is organised into 23 numbered chapters. Verified chapter anchors used in this skill: Chapter 16 = Authentication and Access Controls, Chapter 17 = Cryptography, Chapter 20 = Data Management, Chapter 22 = Enterprise Systems Security. Where a topic below carries no chapter number, confirm the current chapter and control numbers in the online manual at nzism.gcsb.govt.nz before citing.

---

## Governance (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Establish the management framework for information security across the agency.

**Key control areas:**
- Agency information security policy (signed by Chief Executive or delegate)
- Information Security Officer (ISO) / CISO appointment and responsibilities
- Security roles, responsibilities, and accountability
- Information security risk management process
- Compliance with NZISM and related government directives
- Management review of security posture (at least annually)

**Mandatory deliverables:**
- Information Security Policy
- Roles and responsibilities register
- Risk management framework documentation

---

## Physical Security (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Protect ICT assets, facilities, and storage media from physical threats and unauthorised access.

**Key control areas:**
- Secure zones classification (e.g., Public, Operational, Restricted access areas)
- Physical access controls - card readers, guards, visitor registers
- Clean desk and clear screen requirements
- Equipment protection - server room environmental controls, UPS, fire suppression
- Physical media labelling, transport, and destruction
- TEMPEST / emanations security for systems above Restricted (where applicable)

---

## Personnel Security (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Ensure that individuals with access to government information are appropriately vetted and trained.

**Key control areas:**
- Pre-employment background and criminal history checks
- Security vetting levels (baseline, Secret, Top Secret) tied to classification access
- Acceptable use of government ICT resources
- Security awareness training (mandatory annually for all staff)
- Handling of security incidents by staff (reporting obligations)
- Termination and access revocation procedures
- Third-party staff and contractor obligations

---

## Information Security and Classification (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Manage the classification, labelling, handling, and disposal of government information.

**Key control areas:**
- Applying the NZ Government Information Classification System (ISCS)
- Labelling of documents, emails, and media with appropriate classification markings
- Handling requirements per classification level (storage, transmission, disposal)
- Information aggregation risk (combining unclassified data to produce classified information)
- Secure disposal and destruction of classified material
- Sanitisation of storage media before reuse or disposal
- Digital Rights Management (DRM) considerations for high-classification content

---

## Infrastructure Security (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Ensure ICT systems are configured, patched, and maintained securely.

**Key control areas:**
- System hardening - apply vendor and NCSC NZ baseline security configurations
- Patch and vulnerability management - critical patches within 48 hours; others within 30 days
- Change management - formal change approval and testing before deployment
- Asset inventory - all systems documented, classified, and assigned an owner
- End-of-life systems - identified, risk-assessed, and removed or compensating controls applied
- Mobile device management - agency devices enrolled and managed

---

## Network Security (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Control network architecture and connectivity to reduce exposure to threats.

**Key control areas:**
- Network segmentation - separate zones for different classification levels
- Perimeter controls - firewalls, intrusion detection/prevention (IDS/IPS)
- Remote access - encrypted VPN or approved remote access solutions; MFA required
- DNS filtering - block known malicious domains
- Email security - SPF, DKIM, DMARC configured; anti-malware scanning
- Wireless network security - WPA3 preferred; separate networks for guests and agency systems
- Traffic monitoring and anomaly detection

---

## Chapter 16: Authentication and Access Controls (Access Control)

**Purpose:** Ensure access to systems and information is limited to those with a legitimate need.

**Key control areas:**
- Least privilege - users granted minimum access required for their role
- Separation of duties - critical functions require multiple individuals
- Privileged access management - privileged accounts logged, reviewed, and separate from standard accounts
- Access reviews - periodic (at least annual) review and re-certification of access rights
- Temporary and time-limited access - formal request, approval, and automatic expiry
- Remote privileged access - additional controls (jump servers, session recording)

---

## Chapter 16: Authentication and Access Controls (Identification and Authentication)

**Purpose:** Verify the identity of users and systems before granting access.

**Key control areas:**
- Password complexity and minimum length requirements (NZISM aligns with NIST SP 800-63B guidance)
- Multi-Factor Authentication (MFA) - mandatory for remote access and privileged accounts
- Account lockout after failed login attempts
- Service account management - unique credentials, no shared accounts
- Biometric controls (where deployed)
- Session timeout and automatic lock requirements
- Federation and single sign-on (SSO) requirements

---

## Chapter 17: Cryptography

**Purpose:** Protect the confidentiality and integrity of information in transit and at rest.

**Key control areas:**
- Approved cryptographic algorithms - NCSC NZ publishes approved cipher suites; use AES-256, RSA-2048+ / ECDSA-256+, TLS 1.2 minimum (TLS 1.3 preferred)
- Data at rest encryption - mandatory for Confidential and above; recommended for Restricted
- Data in transit encryption - TLS/HTTPS for all external connections; encrypted VPN for inter-site
- Key management - key generation, storage (HSM preferred), rotation, and destruction
- Certificate lifecycle management - track expiry, renew before expiry
- End-to-end encryption for email containing Restricted+ content (e.g., using PGP or S/MIME)

---

## Backup and Media Management (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Ensure data resilience and secure management of storage media.

**Key control areas:**
- Backup schedule - frequency tied to Recovery Point Objective (RPO)
- Backup testing - regularly tested for restoreability
- Offsite backup storage - geographically separate; must meet classification requirements
- Media labelling - all backup media labelled with classification
- Secure media transport - tamper-evident packaging; chain of custody for classified media
- Media disposal - certified destruction for all media containing Restricted+; records kept

---

## Audit and Logging (event logging sits in Chapter 16, section 16.6; confirm at nzism.gcsb.govt.nz)

**Purpose:** Maintain accountability and enable detection of security events.

**Key control areas:**
- Log collection - system, application, and network logs captured
- Log contents - at minimum: timestamp, user ID, event type, source/destination IP, outcome
- Log retention - minimum 90 days online; 12 months archived (longer for Confidential+)
- Log protection - logs stored separately from production systems; tamper-evident
- Security event monitoring - SIEM or equivalent; alerts for anomalous events
- Privileged account logging - all privileged actions logged and reviewed
- Log review - periodic review; automated alerting for high-severity events

---

## Software Development Security (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Embed security into the software development lifecycle.

**Key control areas:**
- Secure coding standards - OWASP Top 10 awareness; input validation; output encoding
- Code review - security-focused code review before release to production
- Dependency management - third-party libraries tracked, updated, and vulnerability-scanned
- Static and dynamic application security testing (SAST/DAST)
- Staging environment parity - test environment mirrors production; no production data in test
- Penetration testing - before major releases and at least annually for internet-facing systems

---

## Third-Party Suppliers (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Ensure that suppliers and contractors maintain security standards equivalent to agency requirements.

**Key control areas:**
- Supplier due diligence - security assessment before engagement
- Contractual security obligations - NZISM-equivalent controls specified in contracts
- Offshore hosting restrictions - Restricted+ data must not leave NZ without Accrediting Authority approval
- Supplier access controls - least privilege; logged; time-limited
- Right to audit - contracts include right to audit supplier security controls
- Incident notification - suppliers must notify the agency of breaches within defined timeframes

---

## Incident Management (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Detect, respond to, and recover from security incidents in a structured way.

**Key control areas:**
- Incident response plan - documented, tested at least annually
- Incident classification - severity levels with defined response timeframes
- Reporting obligations - significant incidents reported to NCSC NZ; mandatory for agencies in scope
- Evidence preservation - forensic readiness; chain of custody for incident artefacts
- Post-incident review - root cause analysis; lessons learned; control improvements
- Breach notification - notification to Privacy Commissioner if personal information is involved

---

## Business Continuity (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Maintain critical services and recover from disruptions.

**Key control areas:**
- Business Continuity Plan (BCP) - identifies critical systems, dependencies, and recovery priorities
- Disaster Recovery Plan (DRP) - technical recovery procedures for ICT systems
- Recovery Time Objective (RTO) and Recovery Point Objective (RPO) - formally defined per system
- BCP/DRP testing - tabletop exercises at minimum annually; full exercises recommended
- Alternate processing sites - geographically separate; classification-appropriate
- Communication plan - stakeholder notification procedures during incidents

---

## Chapter 20: Data Management

**Purpose:** Manage information through its lifecycle - creation, use, storage, and disposal.

**Key control areas:**
- Data retention schedules - aligned with Public Records Act 2005 obligations
- Data sovereignty - government data stored and processed in NZ unless approved otherwise
- Personal information handling - aligned with Privacy Act 2020; privacy impact assessments
- Data minimisation - collect only what is required; delete when no longer needed
- Database security - access controls, encryption, activity logging

---

## Chapter 22: Enterprise Systems Security (Cloud Computing)

**Purpose:** Manage the security risks associated with using cloud services for government information.

**Key control areas:**
- Cloud risk assessment - mandatory before adopting cloud services for Restricted+ information
- NZ Government Cloud Computing Risk & Resilience Guide - agencies must comply with this guide
- Data residency - NZ-hosted cloud preferred; offshore hosting requires Accrediting Authority approval
- Shared responsibility model - documented and agreed with cloud provider
- Cloud provider security certification - preference for ISO 27001 or equivalent certified providers
- Exit strategy - data portability and secure deletion on contract termination

---

## Enterprise Mobility (confirm chapter number at nzism.gcsb.govt.nz)

**Purpose:** Control the security risks associated with mobile devices and remote working.

**Key control areas:**
- Mobile Device Management (MDM) - agency devices enrolled and centrally managed
- Device encryption - mandatory for all agency devices
- Remote wipe capability - required for all devices accessing Restricted+ information
- BYOD policy - BYOD prohibited for Restricted+; if allowed for lower classifications, MDM enrollment required
- VPN for remote access - always-on VPN preferred for Restricted+ systems
- App whitelisting - only approved applications on managed devices

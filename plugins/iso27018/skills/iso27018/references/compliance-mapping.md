# ISO/IEC 27018 — Compliance Mapping Reference

## Overview

This reference maps ISO/IEC 27018 obligations to related frameworks, enabling organisations to understand where compliance evidence overlaps and where gaps must be addressed independently.

---

## 1. ISO 27018 ↔ GDPR (EU General Data Protection Regulation)

ISO/IEC 27018 aligns closely with GDPR because both address the obligations of organisations that process personal data on behalf of others (processors). ISO 27018 compliance provides strong evidence of technical and organisational measures for GDPR Article 28 and 32 purposes, but does not constitute full GDPR compliance.

### Mapping Table

| ISO 27018 Obligation | GDPR Article | GDPR Requirement |
|---------------------|--------------|-----------------|
| No processing beyond customer instructions | Art. 28(3)(a) | Processor processes only on documented instructions |
| No use for commercial/marketing purposes | Art. 28(3)(b) | Processor must ensure confidentiality |
| Sub-processor obligation — same terms | Art. 28(2), 28(4) | Sub-processors must be contracted with same data protection obligations |
| Sub-processor disclosure and advance notice | Art. 28(2) | Controller must be informed of and authorise sub-processors |
| Government request notification | Art. 28(3)(a) | Processor must inform controller unless prohibited by law |
| PII return and deletion at contract end | Art. 28(3)(g) | Delete or return all personal data after end of services |
| Technical security measures | Art. 32(1) | Appropriate technical and organisational measures |
| Encryption of PII | Art. 32(1)(a) | Pseudonymisation and encryption where appropriate |
| PII incident notification | Art. 33(2) | Processor must notify controller without undue delay |
| Support for data subject rights | Art. 28(3)(e) | Processor assists controller in responding to DSRs |
| Breach notification — 72 hours | Art. 33(1) | Controller must notify supervisory authority within 72 hours |
| Privacy by design | Art. 25 | Data protection by design and by default |
| DPO designation | Art. 37–39 | DPO required in certain circumstances |
| Records of processing activities | Art. 30(2) | Processors must maintain records |
| International transfers | Art. 44–49 | Transfers to third countries require appropriate safeguards |
| Customer audit rights | Art. 28(3)(h) | Processor contributes to audits and inspections |
| Supervisory authority identification | Art. 77 | Right to lodge complaint with supervisory authority |

### Key Gaps: ISO 27018 does not cover

ISO 27018 compliance alone does not satisfy:
- GDPR lawful basis for processing (Art. 6) — obligation of the controller, not processor
- GDPR rights obligations that fall on controllers (Arts. 15–22 directly)
- GDPR transparency / privacy notice obligations (Art. 13–14) — controller obligation
- GDPR data protection impact assessments (Art. 35) — controller-led; ISO 29134 relevant
- GDPR provisions specific to special category data (Art. 9)
- GDPR consent requirements (Art. 7) — controller's obligation

---

## 2. ISO 27018 ↔ ISO/IEC 27701

ISO/IEC 27701:2019 is the Privacy Information Management System (PIMS) extension to ISO 27001 and ISO 27002. It covers both PII controllers and PII processors in more depth than ISO 27018.

### Relationship Summary

| Dimension | ISO 27018 | ISO 27701 |
|-----------|-----------|-----------|
| Scope | PII processors; public cloud only | PII controllers AND processors; any context |
| Base standard | ISO 27002 | ISO 27001 + ISO 27002 |
| Management system | Not a management system | PIMS — formal management system certification |
| Certification | No formal ISO 27018 certification scheme (typically demonstrated via ISO 27001 + extended controls) | ISO 27701 certification available |
| Depth of privacy coverage | Operational controls for cloud PII processors | Comprehensive privacy governance framework |
| Controller obligations | Not addressed | Addressed (separate annex for controllers) |

### ISO 27018 Annex A → ISO 27701 Mapping (selected controls)

| ISO 27018 Obligation | ISO 27701 Section |
|---------------------|-------------------|
| Purpose limitation (no commercial use) | 7.2.1 — Identify and document purposes |
| Sub-processor management | 7.5.2 — PII processors engaging other PII processors |
| Government request handling | 7.3.7 — Disclosure to third parties |
| PII return and deletion | 7.4.7 — Return, transfer or disposal of PII |
| Sub-processor register | 7.5.6 — PII sub-processor obligations |
| Incident notification to customers | 7.3.4 — Handling of PII processors' data breaches |
| Support for data subject rights | 7.3.2 — Determining the lawful basis |
| Customer audit rights | 7.5.5 — Enabling customers to comply with obligations |
| Transparency / sub-processor disclosure | 7.4.3 — Providing information to PII principals |
| Dedicated privacy contact | 7.2.8 — Ensuring privacy by design and default |

### Recommendation

Organisations requiring formal PIMS certification should pursue ISO 27701. ISO 27018 is useful as a cloud-specific supplement or as an interim framework before ISO 27701 implementation. The two are complementary, not mutually exclusive.

---

## 3. ISO 27018 ↔ ISO/IEC 27017

ISO/IEC 27017 is the cloud security extension to ISO 27002, covering general cloud security controls for both cloud service providers and cloud service customers. ISO 27018 is the PII-specific extension.

### Relationship Summary

| Dimension | ISO 27017 | ISO 27018 |
|-----------|-----------|-----------|
| Focus | General information security in cloud | PII/personal data protection in public cloud |
| Addresses | CSP and cloud customer both | Primarily CSP acting as PII processor |
| Privacy controls | Limited | Core purpose of the standard |
| Sub-processor content | Some | Detailed PII sub-processor obligations |
| Shared responsibility model | Addressed | Addressed in context of PII |

### Combined Implementation

Most cloud providers implementing ISO 27018 should also implement ISO 27017 because:
- ISO 27017 provides the cloud security foundation; ISO 27018 adds PII-specific controls
- Many customers expect both standards to be in scope when assessing cloud providers for PII processing
- Some ISO 27017 controls directly support ISO 27018 obligations (e.g. virtual machine hardening supports PII encryption and access control obligations)

### Cross-Reference (selected)

| ISO 27017 Control Area | Relevance to ISO 27018 |
|-----------------------|-----------------------|
| CSP-specific: Asset management (return of assets) | Supports ISO 27018 PII return/deletion obligation |
| CSP-specific: Sharing roles (shared responsibility) | Defines CSP vs. customer PII responsibilities |
| Modified 13.1 (network controls) | Supports PII in-transit encryption |
| Modified 9.1 (access to networks) | Supports PII access control obligations |
| Modified 12.1 (operational procedures) | Supports PII operational security |
| Modified 16.1 (incident management) | Supports PII breach notification obligations |

---

## 4. ISO 27018 ↔ ISO/IEC 27001

ISO 27001 provides the ISMS management framework within which ISO 27018 controls are typically implemented. ISO 27018 does not require ISO 27001 certification, but the two are designed to work together.

### Relationship Summary

| Dimension | ISO 27001 | ISO 27018 |
|-----------|-----------|-----------|
| Type | Management system standard (certifiable) | Code of practice (guidelines) |
| Focus | Information security management | PII protection in public cloud |
| Certification | Yes — widely recognised | No formal certification; demonstrated via ISMS certification + extended controls |
| Risk-based approach | Core requirement | Referenced; relies on ISO 27001 risk framework |
| Annex A | 93 controls (2022) or 114 controls (2013) | Extended controls for cloud PII (via ISO 27018 Annex A) |

### How They Work Together

1. ISO 27001 establishes the ISMS (policies, risk assessment, management review, continual improvement)
2. ISO 27002 provides the control guidance that ISO 27001 Annex A references
3. ISO 27018 extends ISO 27002 with PII-specific guidance for cloud providers
4. When an organisation certifies to ISO 27001 and extends its SoA to include ISO 27018 Annex A controls, this demonstrates ISO 27018 compliance within the certified ISMS

### ISO 27018 Annex A → ISO 27001/27002 Context

ISO 27018 Annex A controls are additional controls that supplement (not replace) the ISO 27002/27001 Annex A controls. When preparing a Statement of Applicability (SoA) for a CSP processing PII, include ISO 27018 Annex A controls alongside the standard ISO 27002 Annex A.

---

## 5. ISO 27018 ↔ ISO/IEC 29100 (Privacy Framework)

ISO/IEC 29100 is the foundational privacy framework that provides the 11 privacy principles underpinning ISO 27018 Annex A.

### Privacy Principles Mapping

| ISO 29100 Principle | ISO 27018 Annex A Implementation |
|--------------------|----------------------------------|
| 1. Consent and choice | No processing beyond customer instructions; no commercial use without consent |
| 2. Purpose legitimacy and specification | No marketing/advertising use; purpose defined in contract |
| 3. Collection limitation | Change notification; sub-processor information disclosure |
| 4. Data minimization | Temporary file controls; access limitation |
| 5. Use, retention and disclosure limitation | PII return/deletion at contract end; disclosure notification and register |
| 6. Accuracy and quality | Data correction/deletion mechanisms for customers |
| 7. Openness, transparency and notice | Sub-processor list; data residency disclosure; government request transparency |
| 8. Individual participation and access | Employee access controls; data subject rights support |
| 9. Accountability | Dedicated privacy contact; disclosure register; breach notification |
| 10. Information security | PII security policy; evidence of compliance |
| 11. Privacy compliance | Supervisory authority disclosure; customer audit rights |

### Note
ISO 29100 is not certifiable and serves as a reference framework. ISO 27018 is the operational implementation of ISO 29100 principles for the public cloud PII processor context.

---

## 6. ISO 27018 ↔ Regional Data Protection Laws

ISO 27018 was designed as a jurisdiction-neutral international standard but has explicit alignment with common data protection law requirements.

### Alignment Overview

| Jurisdiction | Framework | ISO 27018 Support |
|-------------|-----------|-------------------|
| European Union | GDPR | Strong alignment — see Section 1 above |
| United Kingdom | UK GDPR + DPA 2018 | Same as EU GDPR; UK retained GDPR post-Brexit |
| United States | CCPA (California) | Partial — transparency and data subject rights aligned |
| United States | HIPAA (healthcare) | Partial — security measures aligned; HIPAA has additional requirements |
| Brazil | LGPD | Significant alignment — processor chapter parallels GDPR obligations |
| India | DPDP Act 2023 | Alignment on processor obligations and data principal rights |
| Australia | Privacy Act 1988 | Supports APP compliance; APPs 1, 6, 11 in particular |
| Canada | PIPEDA / Law 25 (Quebec) | Substantive alignment on processor and security obligations |
| Japan | APPI | Alignment on security, cross-border transfer, data minimization |
| Singapore | PDPA | Alignment on processor obligations and security measures |
| China | PIPL | Partial alignment — PIPL has stricter requirements in some areas |

### Using ISO 27018 for Regulatory Compliance

ISO 27018 provides a strong baseline for demonstrating compliance with cloud data processor obligations across multiple jurisdictions. However:
- It does not substitute for jurisdiction-specific legal advice
- Some jurisdictions (e.g. China's PIPL) impose requirements that go beyond ISO 27018
- Data localisation requirements in some jurisdictions must be addressed separately
- Specific sectoral requirements (healthcare, finance) layer on top of ISO 27018 obligations

---

## 7. ISO 27018 ↔ CSA Cloud Controls Matrix (CCM)

The Cloud Security Alliance (CSA) Cloud Controls Matrix v4 maps to ISO 27018 across several control domains.

### Key CCM Domains with ISO 27018 Alignment

| CCM Domain | Relevance to ISO 27018 |
|------------|------------------------|
| DSP (Data Security and Privacy) | Core alignment — privacy controls, data classification, data residency |
| STA (Supply Chain, Transparency, Accountability) | Sub-processor management, transparency reporting |
| SEF (Security Incident Management) | PII breach notification and incident handling |
| IAM (Identity and Access Management) | Employee access controls; least privilege; MFA |
| CEK (Cryptography, Encryption, Key Management) | PII encryption at rest and in transit |
| LOG (Logging and Monitoring) | Access logging for PII systems |
| GRC (Governance, Risk and Compliance) | PII policy; audit rights; compliance evidence |

Organisations using the CSA CCM as part of a STAR certification programme can align CSA STAR Level 2 (ISO 27001-based) with ISO 27018 obligations using this cross-reference.

---

## 8. ISO 27018 Certification Landscape

### There is no standalone ISO 27018 certification scheme.

Compliance with ISO 27018 is typically demonstrated through one or more of the following:

| Mechanism | Description |
|-----------|-------------|
| **ISO 27001 certification with ISO 27018 scope** | The ISMS is certified under ISO 27001 with the audit scope including ISO 27018 Annex A controls |
| **CSA STAR Certification (Level 2)** | ISO 27001-based STAR certification can include ISO 27018 controls in scope |
| **SOC 2 Type II with Privacy TSC** | Addresses similar obligations; widely accepted in North America |
| **Third-party attestation report** | Independent auditor produces an attestation report confirming compliance with ISO 27018 obligations |
| **Customer questionnaire completion** | CSP completes detailed security questionnaire (SIG, CSA CAIQ) covering ISO 27018 topics |

**Best practice:** Combine ISO 27001 certification (provides the certifiable management system assurance) with ISO 27018 as the extended control set, and make certification evidence accessible to customers via a Trust page, security portal, or on request.

# CMMC Level 3 — Expert (134 Practices)
## Source: NIST SP 800-172 (Enhanced Requirements) and CMMC 2.0 Final Rule (32 CFR Part 170)

---

## Overview

CMMC Level 3 applies to organizations handling **CUI associated with DoD's highest-priority
programs** — typically those involving critical national security systems.

Level 3 requires implementation of all 110 Level 2 practices (NIST SP 800-171 Rev 2) **plus**
24 additional enhanced security requirements from **NIST SP 800-172, "Enhanced Security
Requirements for Protecting Controlled Unclassified Information."**

**Assessment Type:** Conducted by the **Defense Contract Management Agency (DCMA) Defense
Industrial Base Cybersecurity Assessment Center (DIBCAC)**

**Prerequisite:** Organizations must first achieve a CMMC Level 2 C3PAO certification before
a Level 3 assessment can be initiated.

**Certificate Validity:** 3 years (triennial DIBCAC reassessment)
**Annual Affirmation:** Required each year by a senior company official

---

## The 24 Additional Level 3 Practices (from NIST SP 800-172)

All practice IDs use the prefix format: `[Domain].L3-3.x.x(e)` where `(e)` denotes
an "enhanced" requirement from SP 800-172.

### Domain: Access Control (AC) — 4 Additional Practices

| Practice ID | NIST 800-172 Ref | Practice Title | Requirement |
|------------|-----------------|---------------|-------------|
| AC.L3-3.1.2e | 3.1.2e | Restrict Access | Restrict access to systems and system components to only those information resources that are owned, provisioned, or issued by the organization |
| AC.L3-3.1.3e | 3.1.3e | Control CUI Flows — Encrypted | Employ dynamic access control mechanisms to enforce authorizations associated with CUI; protect CUI using cryptographic mechanisms and information flow controls on systems and network components |
| AC.L3-3.1.5e | 3.1.5e | Privileged Access — Logon | Require individuals accessing CUI systems with privileged accounts to have specific training and to use the accounts only when required; log all privileged access to CUI environments |
| AC.L3-3.1.6e | 3.1.6e | Non-Privileged Account Use — Separation | Separate the duties of individuals to reduce the risk of compromise by an insider; log and audit the actions of personnel with access to CUI in high-value systems |

### Domain: Awareness and Training (AT) — 1 Additional Practice

| Practice ID | NIST 800-172 Ref | Practice Title | Requirement |
|------------|-----------------|---------------|-------------|
| AT.L3-3.2.1e | 3.2.1e | Advanced Training | Provide awareness training upon initial hire and regularly thereafter; provide training focused on advanced persistent threats (APT) techniques, tactics, and procedures; include role-based and scenario-based content |

### Domain: Configuration Management (CM) — 1 Additional Practice

| Practice ID | NIST 800-172 Ref | Practice Title | Requirement |
|------------|-----------------|---------------|-------------|
| CM.L3-3.4.1e | 3.4.1e | Authoritative Source | Establish and maintain an authoritative source and repository to provide a trusted source and accountability for systems and system components throughout the system development life cycle |

### Domain: Identification and Authentication (IA) — 1 Additional Practice

| Practice ID | NIST 800-172 Ref | Practice Title | Requirement |
|------------|-----------------|---------------|-------------|
| IA.L3-3.5.3e | 3.5.3e | Additional MFA Mechanisms | Employ supplemental authentication techniques or mechanisms for access to CUI systems where the risk of unauthorized access is particularly high |

### Domain: Incident Response (IR) — 4 Additional Practices

| Practice ID | NIST 800-172 Ref | Practice Title | Requirement |
|------------|-----------------|---------------|-------------|
| IR.L3-3.6.1e | 3.6.1e | Insider Threat Response | Establish and maintain a cyber incident response team that can be deployed to any location within 24 hours to investigate cyber incidents |
| IR.L3-3.6.2e | 3.6.2e | Security Operations | Establish and maintain a security operations center (SOC) capability that facilitates 24/7 monitoring, reporting, and response capabilities |
| IR.L3-3.6.3e | 3.6.3e | Hunt APT | Track adversarial TTPs, employ deception technologies and techniques, perform threat hunting activities, and conduct assessments of vulnerabilities |
| IR.L3-3.6.4e | 3.6.4e | Cyber Threat Intelligence | Receive threat intelligence relevant to the CUI assets from DoD or designated sources; integrate threat intelligence into cyber defense operations |

### Domain: Risk Assessment (RA) — 5 Additional Practices

| Practice ID | NIST 800-172 Ref | Practice Title | Requirement |
|------------|-----------------|---------------|-------------|
| RA.L3-3.11.1e | 3.11.1e | Risk Response | Employ advanced risk assessment techniques and tools to identify and mitigate targeted attacks on high-value assets |
| RA.L3-3.11.2e | 3.11.2e | Threat-Informed Procedures | Use threat intelligence to inform and enhance vulnerability analyses and security controls |
| RA.L3-3.11.3e | 3.11.3e | Advanced Threat Modeling | Develop and update (at least annually) threat models for systems with CUI; use threat models to inform decisions about risk mitigation |
| RA.L3-3.11.4e | 3.11.4e | Predictive Cyber Analytics | Conduct predictive cyber analysis to identify vulnerabilities and potential attacks by leveraging threat intelligence and vulnerability scan data |
| RA.L3-3.11.6e | 3.11.6e | Security Architecture Review | Review security architecture of CUI systems regularly; ensure architecture is consistent with DoD security requirements and CUI protection plans |

### Domain: Security Assessment (CA) — 3 Additional Practices

| Practice ID | NIST 800-172 Ref | Practice Title | Requirement |
|------------|-----------------|---------------|-------------|
| CA.L3-3.12.1e | 3.12.1e | Penetration Testing | Conduct penetration testing at least annually or after significant changes to CUI systems |
| CA.L3-3.12.2e | 3.12.2e | Independent Assessment | Conduct independent, specialized assessments of CUI systems at least annually using high-value asset plans |
| CA.L3-3.12.3e | 3.12.3e | Blue Team Assessment | Include threat hunting exercises and assessments where red and blue teams compete to find vulnerabilities in CUI systems |

### Domain: System and Communications Protection (SC) — 3 Additional Practices

| Practice ID | NIST 800-172 Ref | Practice Title | Requirement |
|------------|-----------------|---------------|-------------|
| SC.L3-3.13.4e | 3.13.4e | Isolate Government CUI | Isolate government CUI from contractor information and systems using hardware-based techniques |
| SC.L3-3.13.10e | 3.13.10e | Key Management — Advanced | Employ advanced key management practices for CUI environments, managed by DoD-provided or DoD-approved key management infrastructure |
| SC.L3-3.13.11e | 3.13.11e | Cryptography — Approved | Restrict cryptographic primitives to those approved by DoD; implement cryptographic agility in systems to enable rapid pivoting to new algorithms when existing algorithms are deprecated |

### Domain: System and Information Integrity (SI) — 2 Additional Practices

| Practice ID | NIST 800-172 Ref | Practice Title | Requirement |
|------------|-----------------|---------------|-------------|
| SI.L3-3.14.3e | 3.14.3e | Threat-Aware Security | Implement threat-aware security capabilities, including advanced intrusion detection, behavior analysis, and anomaly detection mechanisms optimized for detecting APT techniques |
| SI.L3-3.14.6e | 3.14.6e | Deception Technologies | Deploy deception technologies and techniques (e.g., honeypots, decoys, canary tokens) to detect and identify adversarial activity |

---

## Level 3 Assessment Process (DIBCAC)

### DIBCAC — Who They Are

The **Defense Contract Management Agency Defense Industrial Base Cybersecurity Assessment
Center (DCMA DIBCAC)** is the DoD governing body responsible for conducting CMMC Level 3
assessments. DIBCAC assessors are federal government employees with deep cybersecurity
expertise.

### Level 3 Assessment Steps

1. **Initiation**
   - DoD Contract Officer/Program Office notifies organization of Level 3 requirement
   - Organization must hold a current CMMC Level 2 certification (from C3PAO)
   - Organization submits assessment request to DIBCAC

2. **Pre-Assessment**
   - Organization provides SSP (covering all 134 practices)
   - DIBCAC reviews documentation package
   - Assessment scope confirmed

3. **Assessment Execution**
   - DIBCAC Lead Assessor team conducts on-site assessment
   - Technical interviews with security, IT, and program personnel
   - Deep technical testing of all 24 enhanced practices
   - Review of evidence for all 110 Level 2 practices (may rely on C3PAO assessment)

4. **Assessment Results**
   - CMMC Status: CMMC Level 3 Certified (or Conditional, or Not Certified)
   - Conditional: POA&M items must be closed within defined timeline
   - DIBCAC publishes results to enterprise CMMC tracking system

5. **Ongoing Obligations**
   - Annual Affirmation by senior official
   - Triennial DIBCAC reassessment
   - Continuous monitoring and incident reporting (DFARS 252.204-7012)

---

## Level 3 Preparation Checklist

| Area | Requirement |
|------|-------------|
| Level 2 Certification | Current C3PAO CMMC Level 2 certificate in place |
| SOC/CSOC | 24/7 security monitoring capability established |
| Threat Hunting | Documented threat hunting program with TTPs |
| Penetration Testing | Annual pen test completed with findings remediated |
| Threat Intelligence | DoD/government threat intelligence feeds integrated |
| Deception Technologies | Honeypots or equivalent deployed in CUI environment |
| APT Training | Role-based training covering APT techniques, tactics, procedures |
| Insider Threat Program | Formal insider threat program defined and operational |
| Incident Response Team | Deployable team established, exercised, capable of 24-hour response |
| Key Management | DoD-approved key management infrastructure in use |
| Hardware Isolation | Hardware-based isolation of government CUI from contractor systems |
| Threat Modeling | Annual threat model for all CUI systems documented and reviewed |

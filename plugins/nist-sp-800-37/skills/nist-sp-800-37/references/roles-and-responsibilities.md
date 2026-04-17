# NIST SP 800-37 Rev 2 — Roles and Responsibilities

Source: NIST Special Publication 800-37 Rev 2, Appendix D (December 2018)

---

## Overview

SP 800-37 Rev 2 defines a set of roles necessary to execute the RMF. Key principle: **accountability must be clearly assigned** and roles must be appointed in writing. Some roles may be combined in smaller organisations.

---

## Authorising Official (AO)

**Also known as**: Designated Approving Authority (DAA) in some agency contexts

**Appointment**: Senior executive with authority, accountability, and mission ownership over the information system. Must have the authority to accept risk on behalf of the organisation.

**Responsibilities**:
- Authorise (or deny authorisation to) information systems and common controls
- Accept organisational risk for systems under their purview
- Review and approve the System Security Plan
- Sign the Authorization Decision document
- Receive ongoing security posture reports
- Determine when significant changes require reauthorisation
- Ensure adequate funding for security and privacy

**Key constraint**: The AO must have sufficient authority that their acceptance of residual risk is meaningful — they must be held accountable if that risk materialises.

---

## Authorising Official Designated Representative (AODR)

**Appointment**: Designated in writing by the AO.

**Responsibilities**:
- Act on behalf of the AO for day-to-day RMF activities
- Coordinate review of the authorization package
- Brief the AO on security posture and risk determinations
- Cannot sign the final Authorization Decision (that remains with the AO)

---

## Senior Agency Official for Privacy (SAOP) / Chief Privacy Officer (CPO)

**Responsibilities**:
- Ensure integration of privacy requirements into the RMF
- Review and approve Privacy Plans
- Oversee Privacy Impact Assessments (PIAs)
- Ensure compliance with the Privacy Act, E-Government Act, and OMB guidance on privacy
- Designate a privacy point of contact for each system processing PII

---

## Chief Information Security Officer (CISO) / Senior Agency Information Security Officer (SAISO)

**Responsibilities**:
- Establish and maintain the organisation's information security program
- Develop and maintain organisational security policies and procedures
- Coordinate the RMF implementation across the organisation
- Report FISMA compliance status to OMB and Congress (for federal agencies)
- Oversee the continuous monitoring strategy
- Serve as the Risk Executive function (or delegate)

---

## Risk Executive (Function)

**Note**: This is a function, not necessarily a single named individual. Often fulfilled by the CISO, a risk governance board, or an enterprise risk committee.

**Responsibilities**:
- Establish organisation-wide risk tolerance
- Ensure individual system risk decisions are consistent with organisation risk tolerance
- Facilitate information sharing across authorising officials
- Identify common threats that affect multiple systems
- Define the risk management strategy documented in the Prepare step

---

## System Owner (SO)

**Appointment**: Appointed by mission/business owner or head of organisation.

**Responsibilities**:
- Responsible for the overall procurement, development, integration, modification, operation, maintenance, and disposal of the system
- Ensure the system is operated in accordance with the agreed security controls
- Develop and maintain the System Security Plan (with ISSO assistance)
- Ensure security requirements are included in contracts and service agreements
- Coordinate interconnection agreements (ISAs, MOUs)
- Ensure appropriate resources are allocated for security

---

## Information System Security Officer (ISSO)

**Responsibilities**:
- Day-to-day responsibility for the security of the information system
- Develop, implement, and maintain the System Security Plan
- Manage the POA&M and track remediation progress
- Coordinate security assessments with the SCA
- Respond to security incidents involving the system
- Conduct (or coordinate) ongoing monitoring activities
- Report security status to the AO and ISSM
- Ensure security training and awareness for system users

---

## Information System Security Manager (ISSM)

**Note**: Not all organisations have this role; it is typically used in organisations with many information systems.

**Responsibilities**:
- Oversee the ISSO function across multiple systems
- Establish security policies and procedures for a portfolio of systems
- Escalation point for security issues requiring senior management attention
- Ensure consistent application of the RMF across the portfolio
- Support CISO in organisational security program management

---

## Security Control Assessor (SCA)

**Key requirement**: The SCA must be **organisationally independent** from the ISSO and SO for High-impact systems, and this independence is strongly encouraged for Moderate systems. Independence means the SCA should not assess controls that they themselves implemented.

**Responsibilities**:
- Prepare the Security Assessment Plan (SAP) based on the SSP and SP 800-53A
- Conduct independent assessment of security and privacy controls
- Produce the Security Assessment Report (SAR)
- Identify control deficiencies, weaknesses, and associated risks
- Provide remediation recommendations
- Validate remediations (as applicable)

**Assessor types**:
- **Internal**: Organisation's internal audit or assessment team (must be independent of SO/ISSO)
- **Third party (3PAO)**: Independent assessment organisation (required for FedRAMP; common for federal High-impact systems)

---

## Common Control Provider (CCP)

**Responsibilities**:
- Implement and maintain security controls that are provided to and inherited by multiple systems
- Maintain a **Common Control Plan** (analogous to an SSP for inherited controls)
- Ensure common controls are assessed per the RMF
- Provide authorisation documentation to systems inheriting controls
- Notify system owners of changes to common controls that may affect inherited systems

**Examples of common controls**:
- Enterprise identity management (Active Directory, SSO, MFA)
- Physical security of data centres
- Enterprise SIEM and monitoring
- Patch management infrastructure
- Enterprise backup and recovery services
- Network perimeter firewall and IDS/IPS

---

## Mission/Business Owner

**Responsibilities**:
- Define mission/business objectives and requirements driving the information system
- Provide input on mission risk tolerance
- Participate in risk acceptance decisions
- Ensure system security budget is adequate for the mission risk level

---

## System Administrator / Information System Administrator

**Responsibilities**:
- Implement technical security controls
- Maintain system configuration in accordance with the approved baseline
- Execute change management procedures
- Support monitoring and assessment activities with technical evidence
- Participate in incident response for system-level events

---

## Role Assignment Table Summary

| Role | Who Assigns | Can Be Combined With |
|------|-------------|---------------------|
| AO | Head of organisation or delegating executive | Cannot be combined with ISSO, SCA, or SO |
| AODR | AO | May support CISO function |
| SAOP/CPO | Agency head | CISO in some smaller organisations |
| CISO/SAISO | Agency head | Risk Executive function |
| Risk Executive | Agency head | CISO function |
| System Owner | Mission owner / program office | May support ISSM in limited cases |
| ISSO | SO or CISO | May serve as ISSM for small portfolios |
| ISSM | CISO | May serve as ISSO for individual systems |
| SCA | AO or CISO | Must be independent of SO/ISSO for assessment scope |
| CCP | CISO or enterprise services team | May act as SO for common services |

---

## Role Conflicts to Avoid

SP 800-37 Rev 2 flags the following combinations as problematic (conflict of interest or lack of independence):

| Combination | Issue |
|-------------|-------|
| ISSO + SCA for the same system | Assessor assessing their own work — lack of independence |
| SO + AO for the same system | Owner authorising their own system — no independent risk check |
| Developer + SCA | Developer assessing security of code they wrote |
| CCP + SCA for common controls | Provider assessing their own controls |

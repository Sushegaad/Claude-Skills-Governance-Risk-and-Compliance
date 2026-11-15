# NIST SP 800-53 Rev 5 - Baselines, Tailoring, and Overlays Reference

## SP 800-53B - Control Baselines

SP 800-53B (October 2020) is the companion publication that separates the control baselines from the main SP 800-53 catalog.

### Low Impact Baseline

**Used for:** Systems where the loss of confidentiality, integrity, or availability would have limited adverse effects.

**Examples:** Public-facing websites, internal collaboration tools with non-sensitive data, reference databases.

**Scope:** 149 controls and enhancements across 20 families (not counting PM family). Note: the FedRAMP Rev 5 Low baseline is tailored and larger, at 156 controls/enhancements.

**Key characteristics:**
- Policy and procedure controls required for every family
- Basic access controls (AC-2 account management, AC-3 enforcement, AC-7 logon limits)
- Fundamental audit logging (AU-2 through AU-12)
- MFA required for privileged accounts (IA-2(1)) - extended post-EO 14028
- Basic boundary protection (SC-7) without detailed enhancement requirements
- Incident response plan (IR-8), incident reporting (IR-6)
- Vulnerability scanning (RA-5) - frequency defined by ODV
- Core supply chain controls (SR-1, SR-2, SR-2(1), SR-3, SR-5, SR-8, SR-10, SR-11, SR-11(1), SR-11(2), SR-12) are already in the Low baseline
- Baseline selection and tailoring documented (PL-10, PL-11); position descriptions (PS-9)

### Moderate Impact Baseline

**Used for:** Systems where a security breach could have serious adverse effects on organizational operations, assets, or individuals.

**Examples:** HR systems with PII, financial management systems, internal collaboration with sensitive data, most federal agency systems.

**Scope:** 287 controls and enhancements across 20 families. Note: the FedRAMP Rev 5 Moderate baseline is tailored and larger, at 323 controls/enhancements.

**Key additions over Low:**
- Automated account management (AC-2(1)), inactivity controls (AC-2(3)(5))
- Information flow enforcement (AC-4), separation of duties (AC-5)
- Least privilege requirements (AC-6 through AC-6(10))
- SIEM integration for audit (AU-6(1))
- Independent assessors (CA-2(1))
- Continuous monitoring with defined frequencies (CA-7)
- Configuration change control (CM-3), baseline automation (CM-2(2))
- Alternate storage and processing sites (CP-6, CP-7)
- Device and non-org user authentication (IA-3, IA-8)
- PKI/PIV support (IA-2(12), IA-5(2))
- Incident response testing (IR-3)
- Developer security testing (SA-11), configuration management (SA-10)
- Transmission protection (SC-8(1) - TLS required)
- Protection of information at rest (SC-28, SC-28(1)); SC-28 enters the SP 800-53B baseline at Moderate (the FedRAMP Low baseline adds it at Low)
- Software integrity verification (SI-7(1))
- Supplier assessments and reviews (SR-6); most other SR controls already start at Low

### High Impact Baseline

**Used for:** Systems where a breach could have severe or catastrophic effects on national security, safety of human life, or major financial damage.

**Examples:** National security systems, financial systems holding critical data, emergency services, election systems.

**Scope:** 370 controls and enhancements across 20 families. Note: the FedRAMP Rev 5 High baseline is tailored and larger, at 410 controls/enhancements.

**Key additions over Moderate:**
- Account monitoring for atypical usage (AC-2(12))
- Penetration testing (CA-8)
- Insider threat program integration (AT-2(2) at org level; PM-12)
- Threat hunting (RA-10)
- Non-repudiation (AU-10)
- Session audit (AU-14)
- Supply chain testing, tamper resistance and detection (SR-6(1), SR-9, SR-9(1))
- Developer architecture review (SA-17)
- All SI family controls including function verification (SI-6)
- Enhanced cryptographic protections

---

## Control Baselines by Family - Quick Reference

| Family | L Controls | M Controls | H Controls |
|--------|-----------|-----------|-----------|
| AC | 8 | 18 | 20 |
| AT | 4 | 5 | 6 |
| AU | 10 | 14 | 15 |
| CA | 6 | 8 | 9 |
| CM | 8 | 14 | 14 |
| CP | 7 | 12 | 13 |
| IA | 8 | 12 | 14 |
| IR | 7 | 9 | 10 |
| MA | 3 | 6 | 6 |
| MP | 3 | 6 | 7 |
| PE | 11 | 15 | 18 |
| PL | 6 | 7 | 7 |
| PS | 9 | 9 | 9 |
| PT | varies | varies | varies |
| RA | 5 | 8 | 9 |
| SA | 7 | 16 | 17 |
| SC | 14 | 24 | 29 |
| SI | 9 | 17 | 19 |
| SR | 11 | 12 | 15 |
| PM | org-wide | org-wide | org-wide |

---

## Tailoring Process (SP 800-53B Section 2)

Tailoring produces a system-specific set of controls from the starting baseline. Document all tailoring decisions in the SSP.

### Tailoring Step 1 - Identify Common Controls

**Common controls** (also called "inherited controls") are implemented at the organization or facility level and inherited by multiple systems:

| Example | Control | Implemented By |
|---------|---------|---------------|
| Enterprise firewall | SC-7 | Network Operations |
| Badge access system | PE-3 | Facilities |
| Enterprise AV solution | SI-3 | IT Security |
| Security awareness training | AT-2 | ISSO / HR |
| Physical data center security | PE-2, PE-13 | Data Center Ops |

**Designation types:**
- **Common:** Fully inherited from another system/organization
- **System-specific:** Implemented entirely by the system
- **Hybrid:** Partially inherited, partially system-specific

Document in SSP Section: Common Control Inheritance table.

### Tailoring Step 2 - Apply Scoping Considerations

Remove controls that are not applicable based on:

| Scoping Consideration | Example |
|----------------------|---------|
| Technology not present | MA-4 (remote maintenance) if system has no remote maintenance capability |
| Physical location | PE-3 not applicable for cloud-hosted system (inherited from CSP) |
| Mission/operational need | AC-18 (wireless) not applicable for air-gapped system |
| Applicable laws/regulations | Some PT controls not applicable if no PII processed |

**Document every scoping decision** in the SSP with rationale. Regulators and auditors will scrutinize unjustified scoping.

### Tailoring Step 3 - Organization-Defined Values (ODVs)

Every control with brackets `[Assignment: ...]` requires an ODV. Failure to fill in ODVs is a common SSP finding.

**High-priority ODVs to define:**

| Control | Parameter | Federal Guidance | Example Value |
|---------|-----------|-----------------|---------------|
| AC-2(3) | Inactivity period before disable | OMB M-22-09: 90 days | 90 days |
| AC-7 | Max login attempts before lockout | NIST guidance: 3–5 | 3 attempts |
| AC-11 | Session inactivity before lock | OMB M-22-09: 15 minutes | 15 minutes |
| AU-11 | Audit log retention | NARA/OMB: 3 years minimum | 3 years |
| CA-7 | ConMon assessment frequency | FedRAMP: monthly/annually | Monthly for controls; annually for pen test |
| IA-5(1)(a) | Minimum password length | NIST SP 800-63B: 8+; typical federal: 15+ | 15 characters |
| IA-5(1)(h) | Password complexity | NIST SP 800-63B: no complexity requirements (memorized secrets) | No composition rules |
| RA-5 | Vulnerability scan frequency | CISA BOD 19-02; FedRAMP: monthly OS, weekly DB | Monthly OS scans |
| SI-2 | Patch critical vulns within | CISA BOD 19-02: 15 days Critical | 15 days critical; 30 days high |

### Tailoring Step 4 - Compensating Controls

A **compensating control** provides equivalent security when the baseline control cannot be implemented as written:

**Requirements for compensating controls:**
1. Must be as effective as the original control
2. Must be documented with rationale
3. Must not create additional risk
4. Must be assessed as part of the authorization
5. Must be reviewed at each authorization renewal

**Example:** If a legacy system cannot implement IA-2(1) (MFA for privileged accounts), a compensating control could be: enhanced privileged access monitoring (AC-2(12)) + strict IP allowlisting + privileged access workstations + session recording.

### Tailoring Step 5 - Supplementing the Baseline

Add controls beyond the baseline when:
- Risk assessment identifies elevated threats
- Agency or system-specific security requirements demand it
- Laws, regulations, or policies require additional protections
- System processes highly sensitive data not reflected in impact level

---

## Overlays

### What is an Overlay?

An overlay is a pre-tailored baseline for a specific community of interest, technology type, or operating environment. Overlays save time and promote consistency - organizations apply the overlay instead of performing baseline tailoring from scratch.

### FedRAMP Overlay

**Scope:** Cloud services offered to federal agencies.

Key FedRAMP additions to SP 800-53 Moderate baseline:
- Specific ODV values (e.g., AU-11: 1 year; RA-5: monthly for all vulnerability types)
- FedRAMP-specific controls (e.g., FedRAMP-specific ConMon requirements)
- Required 3PAO (Third Party Assessment Organization) for independent assessment
- Continuous monitoring reporting: monthly vulnerability reports, annual pen test, POA&M updates
- JAB (Joint Authorization Board) authorization for P-ATO vs. Agency ATO path

### DoD/CNSS Overlay (CNSS Instruction 1253)

**Scope:** National Security Systems (NSS) - classified or intelligence systems.

Key additions:
- Higher baseline requirements for NSS systems
- CNSS-specific control parameters
- Applies to systems handling Classified National Security Information (CNSI)
- Coordination with Intelligence Community Directive (ICD) 503

### Privacy Overlay

**Scope:** Systems processing PII at scale.

- All 8 PT family controls required
- Enhanced PM privacy controls (PM-18 through PM-27)
- Privacy Impact Assessments (PTA/PIA) required
- SORN required for Privacy Act systems
- Data minimization and retention requirements

### ICS/SCADA Overlay

**Scope:** Industrial Control Systems, SCADA, Operational Technology.

Reference: **NIST SP 800-82 Rev 3** - Guide to OT Security.
- Availability prioritized over confidentiality
- Real-time processing constraints affect control applicability
- Legacy system accommodations
- Safety system isolation requirements
- Physical process monitoring integration

---

## Privacy Baseline (PT Family) - Detailed

### Privacy Act Connection

The **Privacy Act of 1974 (5 U.S.C. § 552a)** applies to federal agencies' systems of records (SOR). SP 800-53 PT controls implement Privacy Act requirements:

| PT Control | Privacy Act Requirement |
|-----------|------------------------|
| PT-5 | Privacy Act notice at collection |
| PT-6 | System of Records Notice (SORN) published in Federal Register |
| PT-8 | Computer matching agreements |

### Privacy Impact Assessment (PIA)

Required by the **E-Government Act of 2002** for new or substantially modified IT systems collecting PII:
- Document what PII is collected and why
- How PII is used, secured, and shared
- Access controls and retention
- Published on agency website (unless classified)

Related controls: PL-2 (SSP includes privacy requirements), RA-3 (privacy risk assessment).

---

## Supply Chain Risk Management (SR Family) - Details

### SCRM Plan (SR-2)

Document organization's SCRM approach:
- Component criticality (SR-4 provenance)
- Supplier risk criteria and assessment process (SR-6)
- Acquisition requirements (SR-5)
- Component authenticity verification (SR-11)
- Notification agreements with suppliers (SR-8)

### SBOM (Software Bill of Materials)

EO 14028 and CISA requirements have increased SBOM expectations. SBOMs support:
- SR-4 (Provenance) - knowing where software components came from
- SR-11 (Component Authenticity) - verifying software integrity
- SA-4 (Acquisition) - requiring SBOM in contracts

**SBOM minimum data fields (NTIA):**
- Supplier name, component name, version, unique identifiers, dependencies, author, timestamp

### Supplier Assessment (SR-6)

For critical suppliers:
- Annual assessments via questionnaire, audit, or site visit
- Review certifications (ISO 27001, SOC 2 Type 2, FedRAMP)
- Contractual security requirements (SA-4, SA-9)
- Incident notification agreements (SR-8)

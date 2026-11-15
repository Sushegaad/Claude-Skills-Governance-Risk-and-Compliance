# ISM - Control Applicability Framework

Source: Australian Information Security Manual, March 2026 edition  
Published by: Australian Signals Directorate (ASD)

---

## Classification Levels & Applicability Markings

Each ISM control carries applicability markings indicating which system classification levels require that control.

| Marking | Classification Level | Description |
|---------|---------------------|-------------|
| **NC** | Non-Classified | General government information; no formal protective marking required |
| **OS** | OFFICIAL: Sensitive | Sensitive but unclassified; default baseline for most federal agency systems |
| **P** | PROTECTED | Classified information; compromise could damage national/organisational interests |
| **S** | SECRET | Highly sensitive; serious damage to national security if compromised |
| **TS** | TOP SECRET | Exceptionally sensitive; grave damage to national security if compromised |

### Stacking Rule
Higher classification systems must implement **all controls for lower levels plus their own level**:
- NC system → NC controls only
- OS system → NC + OS controls
- PROTECTED system → NC + OS + P controls
- SECRET system → NC + OS + P + S controls
- TOP SECRET system → NC + OS + P + S + TS controls

---

## Risk-Based Control Selection Process

The ISM does not mandate a one-size-fits-all approach. The selection process:

1. **Determine system classification** based on the highest sensitivity of information the system stores, processes, or communicates
2. **Define security objectives** - identify CIA (Confidentiality, Integrity, Availability) requirements
3. **Select baseline controls** using applicability markings
4. **Tailor controls** - add controls for specific threats; document exclusions with risk justification
5. **Document in SSP** - all selected controls, exclusions, and justifications must be recorded in the System Security Plan

---

## System Security Plan (SSP) - Required Content

The SSP is the primary authorisation artefact. It must include:

| Section | Content |
|---------|---------|
| System overview | Name, owner, purpose, environment |
| System boundary | What is in scope (hardware, software, interfaces) |
| Classification level | Highest classification handled |
| Security objectives | Confidentiality, Integrity, Availability ratings (High/Medium/Low) |
| Control selection | All applicable ISM controls with applicability justification |
| Implemented controls | Evidence of implementation for each control |
| Excluded controls | Controls not implemented with documented risk acceptance |
| Risk register | Identified risks, likelihood, impact, treatment |
| Authorisation | Authorising Official signature and date |
| Review schedule | Next review date (minimum: every 24 months or after significant change) |

---

## IRAP Assessment Requirements

### Who Needs an IRAP Assessment?
- **Mandatory**: Systems handling PROTECTED and above
- **Strongly recommended**: Systems handling OFFICIAL: Sensitive
- **Government policy**: Any system used to deliver government services to citizens

### IRAP Assessor Requirements
- Must be listed on the ASD IRAP Assessors Register
- Must be independent of the system being assessed
- Must have current ASD-recognised qualifications
- Find assessors: https://www.cyber.gov.au/resources-business-and-government/assessment-and-evaluation-programs/irap/irap-assessors

### Assessment Cycle
- Initial assessment before system authorisation
- Re-assessment every **24 months** (minimum)
- Re-assessment required after **significant change** (major architecture change, new classification level, major new functionality)

### IRAP Assessment Artefact Checklist
- [ ] Current System Security Plan (SSP)
- [ ] Network architecture diagrams
- [ ] Asset register (hardware and software)
- [ ] Risk register with current risk ratings
- [ ] Policy suite (all security policies referenced in SSP)
- [ ] Evidence of implemented controls (configuration screenshots, logs, test results)
- [ ] Previous IRAP assessment report (if re-assessment)
- [ ] Plan of Action & Milestones (POA&M) for any outstanding findings
- [ ] Incident register (last 12 months)
- [ ] Patch management reports

---

## Essential Eight - ISM Relationship

The Essential Eight are **eight priority mitigation strategies** extracted from the broader ISM control set. They are not a separate standard but a prioritised subset.

| Essential Eight Strategy | Primary ISM Chapter(s) | Notes |
|-------------------------|----------------------|-------|
| Application control (allow-listing) | Ch. 13 System Hardening | Prevents execution of unapproved software |
| Patch applications | Guidelines for system management | 48 hours / two weeks / one month per the ISM patching rule below |
| Configure Microsoft Office macros | Ch. 13 System Hardening | Restrict macro execution |
| User application hardening | Ch. 13 System Hardening | Browser, Office, PDF hardening |
| Restrict administrative privileges | Ch. 13 System Hardening, Ch. 6 Personnel | Least privilege, PAM |
| Patch operating systems | Guidelines for system management | 48 hours / two weeks / one month per the ISM patching rule below |
| Multi-factor authentication (MFA) | Ch. 6, Ch. 9, Ch. 19 | MFA for all remote access, privileged accounts |
| Regular backups | Guidelines for system management | Tested, offline/offsite, 3-2-1 rule |

### Essential Eight Maturity Levels

| Level | Description | Who It Applies To |
|-------|-------------|------------------|
| **ML0** | Incomplete or ineffective implementation | Non-compliant |
| **ML1** | Partially aligned; addresses targeted attacks | Minimum for small/low-risk organisations |
| **ML2** | Mostly aligned; addresses sophisticated threats | ASD-recommended baseline for all government entities (2026 target) |
| **ML3** | Fully aligned; addresses advanced persistent threats | Required for critical infrastructure and high-risk sectors |

---

## Patch Management SLAs (Guidelines for system management)

| Scenario | Maximum Remediation Timeframe |
|------------------|------------------------------|
| Internet-facing services: an exploit exists or the vulnerability is being exploited | 48 hours |
| Internet-facing services: all other vulnerabilities | Two weeks |
| Non-internet-facing systems (workstations, servers, network devices, other internal assets) | One month |

---

## Approved Cryptographic Algorithms (Chapter 20)

The ISM mandates ASD-approved algorithms. Key requirements for March 2026:

| Use Case | Approved Algorithm(s) | Notes |
|----------|----------------------|-------|
| Symmetric encryption | AES-128 minimum (AES-256 for PROTECTED+) | |
| Asymmetric encryption | RSA-2048 minimum; EC P-256 or above | RSA-4096 / P-384 for PROTECTED+ |
| Hashing | SHA-256 minimum (SHA-384 for PROTECTED+) | MD5 and SHA-1 prohibited |
| TLS | TLS 1.2 minimum; TLS 1.3 preferred | SSL and TLS 1.0/1.1 prohibited |
| Key exchange | ECDH or DHE (2048-bit minimum) | Static DH prohibited |
| SSH | SSH2 only; ED25519 or RSA-4096 | SSH1 prohibited |

---

## Log Retention Requirements (Chapter 15)

| System Classification | Minimum Log Retention |
|----------------------|----------------------|
| NC | 12 months |
| OFFICIAL: Sensitive | 18 months |
| PROTECTED | 18 months |
| SECRET / TOP SECRET | As directed by agency security policy (typically 7 years) |

Logs must be stored in a tamper-evident manner, separate from the system being monitored.

---

## Key Differences: ISM vs ISO 27001

| Aspect | ISM (ASD) | ISO 27001 |
|--------|-----------|-----------|
| Jurisdiction | Australia (government mandatory) | International (voluntary certification) |
| Structure | 22 guideline chapters + individual controls | 10 clauses + 93 Annex A controls (2022) |
| Assessment | IRAP (ASD-certified assessors) | Third-party certification bodies |
| Classification | NC / OS / P / S / TS markings | Not classification-based |
| Update cycle | Quarterly (March, June, September and December releases) | Major revision every ~7 years |
| Audience | Government entities + supply chain | Any organisation |
| Essential Eight | Subset of ISM; ASD-mandated for government | No direct equivalent |

---

## Useful Official References

| Resource | URL |
|----------|-----|
| ISM (March 2026 PDF) | https://www.cyber.gov.au/sites/default/files/2026-03/Information%20security%20manual%20(March%202026).pdf |
| ISM OSCAL releases | https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism/ism-oscal-releases |
| IRAP Assessors Register | https://www.cyber.gov.au/resources-business-and-government/assessment-and-evaluation-programs/irap/irap-assessors |
| Essential Eight | https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight |
| Essential Eight to ISM mapping | https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-maturity-model-and-ism-mapping |
| ISM GitHub (OSCAL) | https://github.com/AustralianCyberSecurityCentre/ism-oscal |

# GovRAMP Control Mapping Reference

This reference covers the NIST SP 800-53 Rev 5 controls relevant to GovRAMP
authorization, with notes on their application at each GovRAMP impact level and
specific implementation guidance for the SLED (state, local, education, tribal)
cloud security context.

GovRAMP applies NIST SP 800-53 Rev 5 control baselines. The Core status pathway
uses 60 prioritized controls from the Moderate baseline, selected based on the MITRE
ATT&CK Framework. Full control lists for each impact level (Low, Low+, Moderate,
Moderate + CJIS, High) are provided in the official GovRAMP Service Provider Packages.

Templates available at: https://govramp.org/rev-5-templates-and-resources/

---

## Control Families Overview

| ID | Family | Scope | Notes for GovRAMP |
|----|--------|-------|------------------|
| AC | Access Control | All levels | MFA, RBAC, least privilege are Core controls |
| AT | Awareness & Training | All levels | Security awareness + role-based training required |
| AU | Audit & Accountability | M, H | SIEM, log retention critical; Core includes logging controls |
| CA | Assessment, Auth & Monitoring | All levels | Drives 3PAO assessments and ConMon structure |
| CM | Configuration Management | M, H | Baselines, CMDB, change control; Core includes CM controls |
| CP | Contingency Planning | All levels | IRP and CP required for Core, Ready, Authorized |
| IA | Identification & Authentication | All levels | FIPS 140-2/3 required; MFA is a Core control |
| IR | Incident Response | All levels | IRP required and tested; reporting per GovRAMP procedures |
| MA | Maintenance | M, H | Remote maintenance controls |
| MP | Media Protection | M, H | Data at rest encryption; media sanitization |
| PE | Physical & Environmental | M, H | Often inherited from FedRAMP-authorized IaaS |
| PL | Planning | All levels | SSP, Rules of Behavior |
| PM | Program Management | M, H | Enterprise security program oversight |
| PS | Personnel Security | All levels | Background screening, termination; Core covers PS controls |
| PT | PII Processing & Transparency | M, H | Privacy controls (Rev 5 addition); applies to PII systems |
| RA | Risk Assessment | All levels | Vulnerability management; Core covers RA controls |
| SA | System & Services Acquisition | M, H | SDLC security, third-party supply chain |
| SC | System & Comms Protection | All levels | Encryption in transit; network segmentation; Core includes SC |
| SI | System & Information Integrity | All levels | Patching, malware, integrity monitoring; Core includes SI |
| SR | Supply Chain Risk Management | M, H | SCRM (Rev 5 addition) |

---

## GovRAMP Core — 60 Control Areas

The following control areas are covered by the GovRAMP Core 60-control set, aligned
to the NIST SP 800-53 Rev 5 Moderate baseline and prioritized using the MITRE ATT&CK
Framework. The complete, definitive list is in the official GovRAMP Core Controls
document: https://govramp.org/rev-5-templates-and-resources/

### Access Control (AC) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| AC-1 | Policy and Procedures | Required | Document AC policy; review annually |
| AC-2 | Account Management | Required | Provisioning, de-provisioning, reviews; shared account controls |
| AC-3 | Access Enforcement | Required | RBAC or ABAC implementation; enforce least privilege |
| AC-6 | Least Privilege | Required | Restrict privilege to minimum required; review quarterly |
| AC-7 | Unsuccessful Logon Attempts | Required | Account lockout after N failed attempts; document threshold |
| AC-11 | Device Lock | Applies | Session lock after inactivity timeout |
| AC-17 | Remote Access | Required | Document remote access methods; MFA enforced on all paths |
| AC-18 | Wireless Access | Applies | Wireless usage policy; authentication requirements |

### Awareness and Training (AT) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| AT-1 | Policy and Procedures | Required | Security training policy |
| AT-2 | Literacy Training and Awareness | Required | Annual security awareness for all users |
| AT-3 | Role-Based Training | Required | Specialized training for privileged users and security staff |

### Audit and Accountability (AU) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| AU-1 | Policy and Procedures | Required | Audit policy and procedures |
| AU-2 | Event Logging | Required | Define auditable events; configure logging system |
| AU-3 | Content of Audit Records | Required | Logs must include: who, what, when, where, outcome |
| AU-6 | Audit Record Review | Required | Define review frequency; document review process |
| AU-9 | Protection of Audit Information | Required | Prevent deletion or modification of logs |
| AU-11 | Audit Record Retention | Required | Minimum 90 days accessible; 1 year total retention |
| AU-12 | Audit Record Generation | Required | All in-scope components generating logs |

### Configuration Management (CM) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| CM-1 | Policy and Procedures | Required | CM policy |
| CM-2 | Baseline Configuration | Required | Documented baseline configs per component type |
| CM-6 | Configuration Settings | Required | Applied security settings; deviation tracking |
| CM-7 | Least Functionality | Required | Disable unused ports, protocols, services |
| CM-8 | System Component Inventory | Required | Current, accurate inventory of all boundary components |
| CM-10 | Software Usage Restrictions | Applies | Licensed software; prohibition of unauthorized software |

### Contingency Planning (CP) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| CP-1 | Policy and Procedures | Required | CP policy |
| CP-2 | Contingency Plan | Required | Documented CP with RTO/RPO |
| CP-3 | Contingency Training | Required | Training for staff with CP roles |
| CP-4 | Contingency Plan Testing | Required | Test within past 12 months; document results |
| CP-9 | System Backup | Required | Backup procedures; restoration tested |

### Identification and Authentication (IA) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| IA-1 | Policy and Procedures | Required | IA policy |
| IA-2 | Identification and Authentication | Required | MFA for all user accounts; privileged and non-privileged |
| IA-3 | Device Identification | Applies | Authenticate devices where feasible |
| IA-5 | Authenticator Management | Required | Password/token management; FIPS 140-2/3 |
| IA-6 | Authenticator Feedback | Applies | Obscure authentication feedback |
| IA-8 | Non-Org User Auth | Required | Government user authentication requirements |

### Incident Response (IR) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| IR-1 | Policy and Procedures | Required | IRP policy |
| IR-2 | Incident Response Training | Required | Training for all incident responders |
| IR-3 | Incident Response Testing | Required | Test IRP within past 12 months; document results |
| IR-4 | Incident Handling | Required | Containment, eradication, recovery procedures |
| IR-5 | Incident Monitoring | Required | Track and document incidents |
| IR-6 | Incident Reporting | Required | Report to GovRAMP PMO per Incident Communications Procedures |
| IR-8 | Incident Response Plan | Required | Documented IRP with GovRAMP PMO contacts |

### Personnel Security (PS) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| PS-1 | Policy and Procedures | Required | PS policy |
| PS-3 | Personnel Screening | Required | Background checks before granting access |
| PS-4 | Personnel Termination | Required | Access revocation upon termination |
| PS-5 | Personnel Transfer | Required | Access review on role change |

### Risk Assessment (RA) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| RA-1 | Policy and Procedures | Required | Risk management policy |
| RA-3 | Risk Assessment | Required | Periodic risk assessment; document results |
| RA-5 | Vulnerability Monitoring and Scanning | Required | Automated scans; coverage of all components |
| RA-7 | Risk Response | Required | Remediation planning for identified risks |

### System and Communications Protection (SC) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| SC-1 | Policy and Procedures | Required | SC policy |
| SC-5 | Denial of Service Protection | Applies | DDoS mitigation measures |
| SC-7 | Boundary Protection | Required | Firewalls; network segmentation |
| SC-8 | Transmission Confidentiality | Required | Encryption in transit; TLS 1.2 minimum |
| SC-12 | Cryptographic Key Establishment | Required | Key management procedures |
| SC-13 | Cryptographic Protection | Required | FIPS 140-2/3 validated modules only |
| SC-28 | Protection at Rest | Required | Encryption at rest for all government data |

### System and Information Integrity (SI) Core Selections

| Control | Name | Priority | Implementation Focus |
|---------|------|----------|---------------------|
| SI-1 | Policy and Procedures | Required | SI policy |
| SI-2 | Flaw Remediation | Required | Patch management; patch within SLAs |
| SI-3 | Malicious Code Protection | Required | Anti-malware on all applicable components |
| SI-4 | System Monitoring | Required | Intrusion detection; alert review |
| SI-5 | Security Alerts | Required | Subscribe to threat intelligence; act on advisories |
| SI-7 | Software & Information Integrity | Applies | File integrity monitoring |
| SI-10 | Information Input Validation | Applies | Input validation to prevent injection |

---

## Impact Level Differences: Key Control Additions

### Low Impact (Baseline)
Controls covering basic administrative and procedural safeguards:
- AC family: AC-1, AC-2, AC-3, AC-8, AC-14, AC-17, AC-20
- AT family: AT-1, AT-2, AT-3
- AU family: reduced set (AU-1, AU-2, AU-3, AU-6, AU-11, AU-12)
- IA: IA-1, IA-2 (including IA-2(1) for MFA on privileged accounts), IA-4, IA-5
- IR: IR-1, IR-2, IR-4, IR-5, IR-6, IR-7, IR-8
- CP: CP-1, CP-2, CP-4 (tabletop only)

### Moderate Impact (Adds to Low)
Extends Low with more comprehensive controls:
- AC-2 enhancements (automated provisioning review)
- AC-4 Information Flow Enforcement (network segmentation)
- AC-6(1), AC-6(5), AC-6(9), AC-6(10) (Least Privilege enhancements)
- AU-3(1), AU-6(1) (enhanced log content and review)
- CA-2, CA-3, CA-7, CA-9 (assessment and ConMon controls)
- CM-2(2), CM-6(1), CM-7(1), CM-8(1) (enhanced CM)
- CP-6, CP-7, CP-9(1) (alternate sites, backup enhancements)
- IA-2(1), IA-2(2), IA-2(8), IA-2(12) (MFA enhancements)
- IR-3(2) (incident response with support from external providers)
- PT family controls (PII processing and transparency)
- RA-5(1), RA-5(2), RA-5(5) (enhanced scanning)
- SA-3, SA-4, SA-8, SA-9, SA-11 (SDLC, third-party services)
- SC-7 enhancements, SC-8(1), SC-23, SC-28, SC-39
- SI-2(2), SI-3(1), SI-4(1), SI-4(2), SI-7(1) (enhanced SI)
- SR family (supply chain risk management, new in Rev 5)

### High Impact (Adds to Moderate)
Most comprehensive set, including:
- Enhanced AC controls for privileged access (AC-2(9), AC-6(3))
- PIV/CAC authentication requirements (IA-2(12) is critical)
- Full AU suite including real-time alerting
- Extensive CA assessment requirements
- Enhanced CP with multiple alternate sites and full BCP/DR testing
- Additional PE, MA, MP controls
- SI-7 full integrity monitoring suite
- Enhanced SR controls

### CJIS Overlay (Moderate + CJIS)
Additional requirements overlaid on the Moderate baseline for CJI environments:
- FBI CJIS Security Policy alignment
- Personnel screening to CJIS Security Policy standards
- Encryption requirements specific to CJI handling
- Advanced Authentication (AA) per CJIS requirements
- Data isolation requirements
- Additional audit event capture for CJI data access
- Specific media protection requirements for CJI

Providers must use the GovRAMP Service Provider Package for Moderate Impact with CJIS
Overlay and the 3PAO Package for Moderate Impact with CJIS Overlay.

---

## Control Implementation Quick Reference

### MFA Requirements

| Scenario | Minimum MFA Requirement |
|----------|------------------------|
| Privileged accounts (admin, root) | Required at all impact levels |
| Non-privileged accounts — remote access | Required at Moderate and High |
| Government user accounts | Required at Moderate and High |
| All accounts | Required at High |

MFA must use FIPS 140-2/3 validated cryptographic mechanisms.

### Encryption Requirements

| Data State | Minimum Requirement |
|------------|---------------------|
| Data in transit | TLS 1.2 minimum; TLS 1.3 preferred; FIPS 140-2/3 validated |
| Data at rest | AES-256 (FIPS-approved cipher); FIPS 140-2/3 validated key management |
| Prohibited algorithms | MD5, SHA-1 (for signing), DES, 3DES, RC4, SSLv2, SSLv3, TLS 1.0, TLS 1.1 |

### Vulnerability Scan Scope Requirements

| Component Type | Low | Moderate | High |
|----------------|-----|----------|------|
| Operating systems | Monthly | Monthly | More frequent |
| Databases | Not required | Monthly | More frequent |
| Web applications | Not required | Monthly | More frequent |
| Containers and images | Not required | Monthly if used | More frequent |
| Credentialed scans | Recommended | Required | Required |
| Penetration testing | Not required | Annual minimum | Annual minimum |

### Patch / Flaw Remediation SLAs (GovRAMP)

| Risk Rating | Remediation Deadline |
|-------------|---------------------|
| Critical | 30 calendar days |
| High | 90 calendar days |
| Moderate | 180 calendar days |
| Low | 365 calendar days |

---

## Cross-Framework Alignment

GovRAMP's NIST 800-53 Rev 5 foundation enables straightforward alignment with other  
frameworks commonly used by SLED organizations:

| Framework | Alignment Note |
|-----------|----------------|
| FedRAMP Rev 5 | Direct alignment; Fast Track leverages FedRAMP documentation |
| NIST CSF 2.0 | NIST 800-53 Rev 5 is the detailed implementation layer for CSF functions |
| CJIS Security Policy | CJIS Overlay in GovRAMP maps CJI-specific requirements onto the control baseline |
| TX-RAMP | Automatic reciprocity — GovRAMP Authorized products are recognized by TX-RAMP |
| HIPAA/HITECH | Moderate baseline covers the technical security controls required for PHI in government systems |
| SOC 2 | SOC 2 controls partially map to NIST 800-53; existing SOC 2 reports referenced in PMO assessment |
| ISO 27001 | ISO 27001 controls map to NIST 800-53; can be leveraged as evidence in PMO review |

> Note: While GovRAMP accepts evidence from other frameworks (SOC 2, ISO 27001) as
> supporting documentation, GovRAMP status requires demonstration of the specific NIST
> 800-53 Rev 5 controls in the applicable baseline. Existing certifications accelerate
> readiness but do not substitute for GovRAMP authorization requirements.

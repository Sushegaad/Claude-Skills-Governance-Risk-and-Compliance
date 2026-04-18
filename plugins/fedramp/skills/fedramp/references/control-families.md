# NIST SP 800-53 Rev 5 Control Families — FedRAMP Deep Dive

All 20 control families are required by FedRAMP. This guide covers each family's
FedRAMP-specific requirements, common findings, and implementation notes.

FedRAMP baselines (Rev 5): Low ≈ 156 | Moderate = 323 | High = 421 controls and control enhancements.

---

## AC — Access Control

**Key FedRAMP requirements:**
- **AC-2**: Account management — must document account types, provisioning/de-provisioning process, periodic review (at minimum annually for privileged accounts)
- **AC-3**: Access enforcement — RBAC required; document roles and associated privileges
- **AC-6**: Least privilege — document how least privilege is enforced; privileged access must be explicitly justified
- **AC-17**: Remote access — MFA required on all remote access; document all remote access methods
- **AC-20**: Use of external systems — document all external connections; must be FedRAMP-authorized or have compensating controls

**FedRAMP parameter overrides:** AC-2 requires account reviews at specific FedRAMP-defined frequencies (more stringent than base NIST). Review the FedRAMP parameter values workbook for your baseline.

**Common findings:** Shared accounts not documented or controlled; no evidence of periodic access reviews; remote access methods not fully documented; excessive admin privileges.

---

## AT — Awareness & Training

**Key FedRAMP requirements:**
- **AT-2**: Literacy training and awareness — annual security awareness training for all users; includes privacy training (Rev 5)
- **AT-3**: Role-based training — additional training for personnel with security responsibilities; includes privacy-role training (Rev 5)
- **AT-4**: Training records — maintain records of completion; auditors will request training logs

**Common findings:** Training completion rate below 100%; no records of role-based training for ISSOs/security engineers; privacy training not included in AT-3 curriculum.

---

## AU — Audit & Accountability

**Key FedRAMP requirements:**
- **AU-2**: Event logging — document which events are logged across all boundary components
- **AU-3**: Content of audit records — logs must include: timestamp, source, event type, outcome, user/process identity
- **AU-9**: Protection of audit information — log integrity; logs must be protected from tampering
- **AU-11**: Audit record retention — **90 days online (hot storage); 1 year total** (FedRAMP-defined)
- **AU-12**: Audit record generation — 100% of in-boundary components must generate logs

**Common findings:** Not all boundary components sending logs to SIEM; log retention shorter than 90 days online; logs not protected from deletion by admins; no log review/alerting process documented.

---

## CA — Assessment, Authorization & Monitoring

**Key FedRAMP requirements:**
- **CA-2**: Control assessments — 3PAO annual assessment required
- **CA-5**: Plan of action and milestones — POA&M maintained and updated monthly
- **CA-7**: Continuous monitoring — ConMon program documented and executed (see ConMon Monthly requirements)
- **CA-8**: Penetration testing — required annually for High baseline; recommended for Moderate
- **CA-9**: Internal system connections — all internal connections documented with ISAs/MOUs

**Common findings:** ConMon activities not documented; POA&M items stale with no milestone updates; penetration testing not performed at required frequency.

---

## CM — Configuration Management

**Key FedRAMP requirements:**
- **CM-2**: Baseline configuration — secure baselines defined for all component types; CIS Benchmarks or DISA STIGs recommended
- **CM-3**: Configuration change control — formal CCB process with documented approval chain
- **CM-6**: Configuration settings — FedRAMP-defined configuration settings must be implemented; deviations documented
- **CM-7**: Least functionality — disable/remove unused functions, ports, protocols, services; document all allowed ports/protocols/services (PPS table in SSP Section 7)
- **CM-8**: System component inventory — IIW maintained and current; covers all in-boundary assets

**Common findings:** Configuration baselines not formally documented; deviations from baselines not tracked; PPS table incomplete or inconsistent with network diagrams; IIW not updated when new assets are added.

---

## CP — Contingency Planning

**Key FedRAMP requirements:**
- **CP-2**: Contingency plan — documented ISCP using FedRAMP template; includes RTO/RPO
- **CP-4**: Contingency plan testing — tested at least annually; tabletop minimum, functional preferred for High
- **CP-6**: Alternate storage site — required for Moderate and High; geographically separated
- **CP-9**: System backup — backup frequency, testing, and off-site storage documented

**Common findings:** CP tested with tabletop only for High baseline (functional test required); RTO/RPO not validated through testing; alternate site not configured or tested; backup restoration not verified.

---

## IA — Identification & Authentication

**Key FedRAMP requirements:**
- **IA-2**: Identification and authentication — MFA required for **all** accounts accessing federal systems; no exceptions for privileged accounts
- **IA-2(1)**: MFA for privileged accounts — phishing-resistant MFA strongly preferred for High
- **IA-5**: Authenticator management — NIST SP 800-63B alignment: no forced rotation schedules; require compromised-password lists and password strength meters
- **IA-8**: Non-organizational users — PIV/CAC required or justified alternative for agency users on High baseline
- **IA-12**: Identity proofing — required for Rev 5; document identity proofing process for privileged users

**FedRAMP encryption requirement:** All authenticator storage must use FIPS 140-2/3 validated cryptographic modules.

**Common findings:** MFA not enforced on all remote access; legacy password rotation policies inconsistent with NIST 800-63B; PIV/CAC not supported on High baseline without documented compensating controls.

---

## IR — Incident Response

**Key FedRAMP requirements:**
- **IR-3**: Incident response testing — tested at least annually (tabletop minimum)
- **IR-5**: Incident monitoring — automated alerting from SIEM required
- **IR-6**: Incident reporting — **report to US-CERT/CISA within 1 hour of discovery** for high-priority incidents; report to agency AO within 1 hour for incidents affecting federal data; notify FedRAMP PMO Security Inbox
- **IR-8**: Incident response plan — must be current, tested, and include FedRAMP-specific contacts and reporting SLAs

**Common findings:** IRP does not include FedRAMP PMO Security Inbox in notification chain; 1-hour reporting SLA not documented; IRP not tested annually; no documented evidence of past incident handling.

---

## MA — Maintenance

**Key FedRAMP requirements:**
- **MA-4**: Non-local maintenance — remote maintenance sessions must be documented, monitored, and terminated when complete; MFA required for remote maintenance
- **MA-5**: Maintenance personnel — screening requirements for maintenance personnel who access the system

**Common findings:** Remote maintenance not logged or monitored; maintenance personnel without appropriate clearances accessing federal data.

---

## MP — Media Protection

**Key FedRAMP requirements:**
- **MP-5**: Media transport — encryption required for media containing federal data in transit
- **MP-6**: Media sanitization — NIST SP 800-88 compliant sanitization procedures for media disposal; document and retain sanitization records
- **MP-7**: Media use — restrict or prohibit use of portable media (USB drives) within boundary

**Common findings:** No documented media sanitization procedures; portable media not restricted; cloud-native CSPs often need to document how MP controls apply to logical media (disk images, snapshots).

---

## PE — Physical & Environmental Protection

**Key FedRAMP requirements:**
- PE controls are typically **fully inherited** from IaaS/PaaS providers (AWS GovCloud, Azure Government, GCP)
- Document inherited PE controls in CIS/CRM workbook; customer-responsible PE controls (e.g., workstation access at CSP offices) must still be addressed
- **PE-3**: Physical access control — must document physical access controls for any CSP-operated facilities within scope

**Common findings:** PE controls marked as inherited without documenting which IaaS controls cover them; CSP office physical access not addressed even when within boundary scope.

---

## PL — Planning

**Key FedRAMP requirements:**
- **PL-2**: System security and privacy plans — the SSP itself; must be complete, current, and approved
- **PL-4**: Rules of behavior — SSP Appendix E; must be signed by all users
- **PL-10**: Baseline selection — document the FedRAMP baseline selected and rationale

**Common findings:** SSP not updated to reflect system changes; RoB signatures not maintained; baseline selection not formally documented.

---

## PM — Program Management

**Key FedRAMP requirements:**
- PM controls are **enterprise-level** — they describe the organizational security program, not individual system controls
- **PM-9**: Risk management strategy — enterprise risk management framework documented
- **PM-28**: Risk framing — new in Rev 5; document how risk is framed at organizational level
- PM controls are often addressed organizationally and referenced in the SSP

**Common findings:** PM controls addressed for the system without organizational context; PM-28 (new Rev 5) missing from newer SSPs.

---

## PS — Personnel Security

**Key FedRAMP requirements:**
- **PS-3**: Personnel screening — background checks for all personnel with access to federal data; document screening criteria
- **PS-4**: Personnel termination — immediate access revocation upon termination; documented process required
- **PS-5**: Personnel transfer — access review and adjustment upon role changes
- **PS-6**: Access agreements — non-disclosure agreements and access agreements documented and signed

**Common findings:** Termination process not documented or not consistently followed; contractors not covered by screening requirements; NDA records not maintained.

---

## PT — PII Processing & Transparency (New in Rev 5)

**Key FedRAMP requirements:**
- **PT-1**: Policy and procedures — PII processing and transparency policy required
- **PT-2**: Authority to process PII — legal authority for each PII type documented
- **PT-3**: Personally identifiable information processing purposes — document why each PII element is collected
- **PT-5**: Privacy notice — users informed of PII collection and use
- **PT-6**: System of records notice — required if system is a Privacy Act System of Records

**Note:** PT controls apply whenever the system collects, processes, stores, or transmits PII. If the system handles no PII, PT controls may be marked Not Applicable — but this determination must be documented and supported by the FIPS 199 categorization.

**Common findings:** PT control family entirely missing from Rev 4 → Rev 5 transitioned SSPs; PII inventory not documented; Privacy Act System of Records determination not made.

---

## RA — Risk Assessment

**Key FedRAMP requirements:**
- **RA-3**: Risk assessment — system-level risk assessment completed and updated
- **RA-5**: Vulnerability monitoring and scanning — automated scanning required:
  - OS/infrastructure: **monthly minimum**
  - Web application: **monthly minimum**
  - Database: **monthly minimum**
  - Container images: per CI/CD pipeline and prior to deployment
  - 100% coverage of in-boundary assets required
- **RA-5(11)**: Public disclosure program — FedRAMP encourages CSPs to have a vulnerability disclosure policy (VDP)
- **RA-7**: Risk response — document how scan findings are triaged and remediation prioritized

**Common findings:** Scan coverage gaps (e.g., database servers not scanned, containers not included); scan frequency below monthly; no documented remediation SLA tracking.

---

## SA — System & Services Acquisition

**Key FedRAMP requirements:**
- **SA-4**: Acquisition process — security requirements included in procurement contracts
- **SA-9**: External system services — all external services documented; FedRAMP-authorized where applicable
- **SA-11**: Developer testing and evaluation — secure development practices documented (SDLC)
- **SA-15**: Development process, standards, and tools — SDLC security requirements

**Common findings:** External SaaS tools used by CSP admins not in the external services table; no documented SDLC security requirements; third-party libraries not tracked.

---

## SC — System & Communications Protection

**Key FedRAMP requirements:**
- **SC-5**: Denial of service protection — DDoS protection documented (often via IaaS/CDN)
- **SC-7**: Boundary protection — firewall/WAF rules documented; all ingress/egress controlled
- **SC-8**: Transmission confidentiality and integrity — **TLS 1.2 minimum; TLS 1.3 preferred** for all data in transit
- **SC-12**: Cryptographic key establishment and management — key management procedures documented
- **SC-28**: Protection of information at rest — encryption at rest with FIPS 140-2/3 validated modules
- **SC-39**: Process isolation — application processes isolated from each other

**Common findings:** TLS 1.0/1.1 still enabled on endpoints; key management undocumented; network segmentation not depicted in architecture diagrams; boundary not fully enforced (undocumented egress paths).

---

## SI — System & Information Integrity

**Key FedRAMP requirements:**
- **SI-2**: Flaw remediation — patch management SLAs: Critical 30d / High 90d / Moderate 180d / Low 365d
- **SI-3**: Malicious code protection — endpoint protection on all applicable components; real-time scanning
- **SI-4**: System monitoring — SIEM with alerting; anomaly detection documented
- **SI-7**: Software, firmware, and information integrity — file integrity monitoring (FIM) on critical system files
- **SI-10**: Information input validation — input validation for all public-facing applications (ties to web app scanning)

**Common findings:** Patch SLAs not tracked or enforced; FIM not deployed on critical servers; SIEM alerts not reviewed or tuned; malware protection not on all applicable endpoints (e.g., Linux servers overlooked).

---

## SR — Supply Chain Risk Management (New in Rev 5)

**Key FedRAMP requirements:**
- **SR-1**: Policy and procedures — SCRM policy required (SSP Appendix P)
- **SR-2**: Supply chain risk management plan — documented in Appendix P
- **SR-3**: Supply chain controls and processes — supplier assessment process defined
- **SR-4**: Provenance — track origin and custody of hardware and software components
- **SR-5**: Acquisition strategies, tools, and methods — preferred suppliers and vetting criteria documented
- **SR-8**: Notification agreements — notification from suppliers of security incidents or product changes
- **SR-11**: Component authenticity — anti-counterfeit measures for hardware
- **SR-12**: Component disposal — secure disposal of hardware and software components

**Note:** SR is the newest family and frequently has gaps in SSPs transitioned from Rev 4. Prioritize SR-1, SR-2, and SR-3 for initial authorization; remaining controls can be phased in via POA&M with AO agreement.

**Common findings:** Appendix P (SCRM Plan) is a template placeholder with no CSP-specific content; no SBOM process; critical software components (open source libraries) not tracked for vulnerabilities; SR controls entirely absent from Rev 4-era SSPs.

---

## Summary: Control Count by Baseline (Rev 5)

| Baseline | Controls & Enhancements | Primary Use |
|----------|------------------------|-------------|
| LI-SaaS | Subset of Low (~54 controls) | Low-impact SaaS with no PII, no sensitive federal data |
| Low | ~156 | Limited adverse effect on federal mission/assets |
| Moderate | 323 | Serious adverse effect — most common baseline |
| High | 421 | Severe or catastrophic effect (law enforcement, health, financial) |

> Control counts include base controls and all required control enhancements at each baseline.
> FedRAMP parameter values (FedRAMP-defined values) may be stricter than base NIST requirements —
> always check the FedRAMP parameter values workbook for your baseline.

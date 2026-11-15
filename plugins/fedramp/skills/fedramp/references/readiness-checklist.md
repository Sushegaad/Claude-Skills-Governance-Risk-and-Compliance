# FedRAMP Readiness Checklist

Use this checklist when doing a readiness or gap assessment. Organize findings
by category and flag each item as: ✅ Met | ⚠️ Partial | ❌ Not Met | N/A

---

## 1. Boundary & System Documentation

- [ ] Authorization boundary is formally defined and documented
- [ ] Network architecture diagram exists and is current
- [ ] Data flow diagrams show all data entering/leaving the boundary
- [ ] System inventory (hardware, software, virtual assets) is complete
- [ ] All external connections and services are documented
- [ ] External services outside boundary are FedRAMP-authorized OR have documented compensating controls
- [ ] System categorization (FIPS 199) is complete with Low/Moderate/High determination
- [ ] Interconnection agreements (ISAs/MOUs) exist for all external connections

## 2. Policies & Procedures

- [ ] Information Security Policy exists and is approved
- [ ] Acceptable Use Policy (Rules of Behavior) is documented and signed by users
- [ ] Access Control Policy
- [ ] Configuration Management Policy & Plan
- [ ] Contingency Plan (CP) - written and tested within last 12 months
- [ ] Incident Response Plan (IRP) - written and tested within last 12 months
- [ ] Media Protection Policy
- [ ] Personnel Security Policy
- [ ] Physical Security Policy (or inherited from IaaS provider)
- [ ] Privacy policy and PII handling procedures (Rev 5 requirement)
- [ ] Supply Chain Risk Management policy (Rev 5 requirement)

## 3. Access Control & Identity

- [ ] Multi-factor authentication (MFA) enforced on all privileged accounts
- [ ] MFA enforced on all remote access
- [ ] Role-based access control (RBAC) implemented with documented roles
- [ ] Least privilege principle applied and documented
- [ ] Privileged access reviews performed at least annually
- [ ] Account provisioning/de-provisioning process is defined and followed
- [ ] Shared/service accounts are documented and controlled
- [ ] PIV/CAC support in place or plan documented (for High baseline)
- [ ] FIPS 140-2 or 140-3 validated authentication mechanisms in use

## 4. Encryption

- [ ] All federal data encrypted at rest using FIPS 140-2/3 validated modules
- [ ] All federal data encrypted in transit (TLS 1.2+ minimum; 1.3 preferred)
- [ ] Key management procedures documented
- [ ] Non-FIPS algorithms (e.g., MD5, SHA-1, DES, RC4) eliminated from boundary
- [ ] Cryptographic modules table (required SSP appendix) is complete

## 5. Vulnerability Management

- [ ] Automated vulnerability scanning in place (OS-level)
- [ ] Web application scanning in place
- [ ] Database scanning in place
- [ ] Container image scanning in place (if containers are used)
- [ ] Scan coverage includes 100% of in-boundary assets
- [ ] Scan frequency meets FedRAMP requirements (OS: monthly; web app: monthly)
- [ ] Remediation SLAs are defined and tracked: Critical 30d / High 90d / Moderate 180d / Low 365d
- [ ] False positives have a documented deviation request (DR) process

## 6. Audit & Logging

- [ ] Centralized log aggregation in place (SIEM or equivalent)
- [ ] Audit log retention meets FedRAMP requirement (90 days online; 1 year total)
- [ ] All boundary components (servers, network devices, apps) sending logs
- [ ] Log integrity protection in place
- [ ] Log review process and alerting defined
- [ ] Privileged user activity is logged and monitored

## 7. Configuration Management

- [ ] Secure baseline configurations defined for all component types
- [ ] Configuration deviations documented and approved
- [ ] Change management process is formal and documented
- [ ] System and software inventory is maintained and current (CMDB or equivalent)
- [ ] Patch management process defined with documented SLAs
- [ ] CIS Benchmarks or DISA STIGs used as configuration baselines (recommended)

## 8. Incident Response

- [ ] IRP covers detection, analysis, containment, eradication, recovery
- [ ] Incident reporting SLAs meet FedRAMP: US-CERT reporting within 1 hour of discovery
- [ ] IRP tested (tabletop or functional exercise) within last 12 months
- [ ] IR roles and contacts documented (including agency AO contacts)
- [ ] Security Inbox maintained for urgent government directives (required Jan 5, 2026+)

## 9. Contingency Planning

- [ ] Business Continuity Plan (BCP) and/or Disaster Recovery Plan (DRP) documented
- [ ] Recovery Time Objective (RTO) and Recovery Point Objective (RPO) defined
- [ ] CP tested within last 12 months
- [ ] Backup and restore procedures tested
- [ ] Alternate processing site identified (for Moderate and High)

## 10. Personnel Security

- [ ] Background check process defined for personnel with access to federal data
- [ ] Onboarding security training documented
- [ ] Annual security awareness training tracked and documented
- [ ] Privacy training included in annual training (Rev 5)
- [ ] Termination procedures include immediate access revocation
- [ ] Contractor/third-party personnel screening requirements defined

## 11. Third-Party / Supply Chain (Rev 5)

- [ ] Inventory of third-party software and services is maintained
- [ ] Critical suppliers identified and assessed
- [ ] Software Bill of Materials (SBOM) process in place or planned
- [ ] Open source components tracked for known vulnerabilities
- [ ] SR control family (Supply Chain Risk Management) requirements reviewed

## 12. Privacy (Rev 5)

- [ ] PII inventory documented (what PII is collected/processed/stored)
- [ ] Privacy Impact Assessment (PIA) completed if PII is in scope
- [ ] Privacy training included in AT-3 training program
- [ ] PT control family requirements reviewed and mapped

## 13. 3PAO Readiness

- [ ] Selected a FedRAMP-recognized 3PAO (check FedRAMP Marketplace)
- [ ] If 3PAO helped write SSP, a *different* 3PAO must do the assessment (A2LA R311)
- [ ] Authorization boundary agreed upon with 3PAO before assessment begins
- [ ] CSO is "frozen" from changes during assessment window
- [ ] Evidence repository (e.g., GRC tool or SharePoint) organized and accessible to 3PAO

## 14. OSCAL / Automation (Forward-Looking)

- [ ] Aware of CR26 machine-readable data requirements (semi-structured for Classes A/B/C from Jan 1, 2027; comprehensive for Class D from May 1, 2027)
- [ ] Evaluated OSCAL-capable GRC tools or the FedRAMP automation GitHub repo
- [ ] SSP data structured to facilitate OSCAL export

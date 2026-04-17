# GovRAMP Readiness Checklist

Use this checklist when performing a gap assessment for any GovRAMP status level.
For each item, mark: Met | Partial | Not Met | N/A

Impact levels: Low (L) | Moderate (M) | High (H)
Where multiple levels are shown, the control applies at that level and above.

---

## 1. Membership and Program Enrollment

- [ ] Service provider is an active GovRAMP member
- [ ] Membership tier is appropriate for the organization's size and revenue
- [ ] Security Review Request Form has been identified and is accessible

---

## 2. Boundary and System Documentation

- [ ] Authorization boundary is formally defined in writing
- [ ] Network architecture diagram is current and depicts the full boundary
- [ ] Data flow diagrams show all data entering, leaving, and moving within the boundary
- [ ] System inventory (hardware, software, virtual, container assets) is complete
- [ ] All external connections and third-party services are documented
- [ ] External services outside boundary are FedRAMP-authorized, GovRAMP-authorized, or
      have documented compensating controls
- [ ] System categorization (FIPS 199 logic) is complete with impact level determination
- [ ] Data Classification Tool assessment completed (if impact level is uncertain)
- [ ] Service model is defined (SaaS / PaaS / IaaS)
- [ ] Leveraged cloud platform authorization documented (e.g., AWS GovCloud, Azure Government)

---

## 3. Policies and Procedures

- [ ] Information Security Policy — approved and in effect (L, M, H)
- [ ] Acceptable Use Policy / Rules of Behavior — documented and user-acknowledged (L, M, H)
- [ ] Access Control Policy (L, M, H)
- [ ] Configuration Management Policy and Plan (L, M, H)
- [ ] Incident Response Plan (IRP) — documented, tested within last 12 months (L, M, H)
- [ ] Contingency Plan (CP) — documented, tested within last 12 months (L, M, H)
- [ ] Media Protection Policy (M, H)
- [ ] Personnel Security Policy (L, M, H)
- [ ] Physical Security Policy (or fully inherited from IaaS provider) (L, M, H)
- [ ] Privacy policy and PII handling procedures documented (M, H)
- [ ] Supply Chain Risk Management policy (M, H)
- [ ] Change Management Policy (M, H)
- [ ] Vulnerability Management Policy (L, M, H)

---

## 4. Access Control and Identity

- [ ] Multi-factor authentication (MFA) enforced on all privileged accounts (L, M, H)
- [ ] MFA enforced on all remote access paths (L, M, H)
- [ ] Role-based access control (RBAC) implemented and documented (M, H)
- [ ] Least privilege principle applied and documented (L, M, H)
- [ ] Privileged account access reviews performed quarterly or more frequently (M, H)
- [ ] User access reviews performed at least annually (L, M, H)
- [ ] Account provisioning and de-provisioning process documented and in use (L, M, H)
- [ ] Shared/service accounts documented and controlled (M, H)
- [ ] Emergency access accounts documented and controlled (M, H)
- [ ] FIPS 140-2 or 140-3 validated authentication mechanisms in use (M, H)

---

## 5. Encryption

- [ ] All government data encrypted at rest using FIPS 140-2/3 validated modules (M, H)
- [ ] All government data encrypted in transit using TLS 1.2 minimum (1.3 preferred) (L, M, H)
- [ ] Key management procedures documented (M, H)
- [ ] Non-FIPS algorithms (MD5, SHA-1, DES, RC4) eliminated from the boundary (M, H)
- [ ] Certificate management process documented (expiration tracking) (M, H)

---

## 6. Vulnerability Management

Per the GovRAMP Vulnerability Scan Requirements Guide:

- [ ] Automated vulnerability scanning program in place (L, M, H)
- [ ] Scans cover all OS-level components within the boundary (L, M, H)
- [ ] Scans cover all database components within the boundary (M, H)
- [ ] Scans cover all web application components within the boundary (M, H)
- [ ] Scans cover containers (if used) (M, H)
- [ ] Scan frequency meets GovRAMP requirements (minimum monthly for Moderate/High) (M, H)
- [ ] Penetration testing performed per GovRAMP Penetration Test Guidance (M, H)
- [ ] Penetration test conducted within the past 12 months (at minimum) (M, H)
- [ ] Vulnerability scan results are tracked and remediated per SLAs (L, M, H)
- [ ] All critical vulnerabilities tracked in POA&M with remediation plans (L, M, H)

---

## 7. Logging and Monitoring

- [ ] Centralized logging/SIEM is in place (M, H)
- [ ] All in-scope components are sending logs to centralized SIEM (M, H)
- [ ] Log retention period meets requirements (minimum 90 days online; 1 year retained) (M, H)
- [ ] Security alerts and anomalies are reviewed and actioned (M, H)
- [ ] Privileged account activity is logged (L, M, H)
- [ ] Audit logs are protected from modification or deletion (M, H)
- [ ] Network traffic monitoring in place (M, H)

---

## 8. Incident Response

- [ ] Incident Response Plan (IRP) is documented and current (L, M, H)
- [ ] IRP has been tested within the past 12 months (tabletop or functional exercise) (L, M, H)
- [ ] IRP test results are documented (L, M, H)
- [ ] Incident reporting timelines are defined and aligned with GovRAMP Incident
      Communications Procedures (L, M, H)
- [ ] Contact information for GovRAMP PMO is in the IRP (L, M, H)
- [ ] Security incident categories are defined (L, M, H)
- [ ] Forensic evidence preservation procedures are documented (M, H)
- [ ] Lessons learned process exists post-incident (M, H)

---

## 9. Contingency Planning

- [ ] Contingency Plan (CP) is documented and current (L, M, H)
- [ ] CP defines Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) (L, M, H)
- [ ] CP has been tested within the past 12 months (L, M, H)
- [ ] CP test results are documented (L, M, H)
- [ ] Data backup and restoration procedures are documented and tested (L, M, H)
- [ ] Backup restoration tested successfully within the past 12 months (M, H)
- [ ] Alternate processing/hosting site or failover capability is documented (M, H)

---

## 10. Configuration Management

- [ ] Configuration baselines defined for all in-scope components (M, H)
- [ ] Configuration Management Plan documented (M, H)
- [ ] Change management process in place; changes reviewed and approved (M, H)
- [ ] System component inventory (CMDB) is current and accurate (M, H)
- [ ] Unauthorized change detection (file integrity monitoring or equivalent) in place (M, H)
- [ ] CIS Benchmarks or DISA STIGs applied where applicable (M, H)

---

## 11. Personnel Security

- [ ] Background screening process documented for staff with system access (L, M, H)
- [ ] Background checks conducted before granting access (M, H)
- [ ] Termination procedures documented (access revocation timeline) (L, M, H)
- [ ] Contractor and third-party access controls documented (M, H)
- [ ] Security awareness training program in place (L, M, H)
- [ ] Training completion is tracked and documented (L, M, H)
- [ ] Role-based security training for privileged users (M, H)

---

## 12. Physical and Environmental Security

- [ ] Physical security controls documented (or inherited from FedRAMP-authorized IaaS) (L, M, H)
- [ ] Access to servers and data center is restricted and logged (M, H)
- [ ] Environmental controls (temperature, humidity, fire suppression) documented or
      inherited (M, H)

---

## 13. System and Communications Protection

- [ ] Network segmentation in place between in-scope and out-of-scope systems (M, H)
- [ ] Firewall rules documented and reviewed regularly (M, H)
- [ ] Web application firewall (WAF) or equivalent in place (M, H)
- [ ] Ports, protocols, and services (PPS) table is documented in the SSP (L, M, H)
- [ ] Boundary protection devices (firewalls, IDS/IPS) are in place and monitored (M, H)

---

## 14. Privacy (NIST 800-53 Rev 5 PT Family)

- [ ] Privacy policy published and available to government customers and end users (M, H)
- [ ] PII inventory or data map exists (M, H)
- [ ] Privacy impact assessment process in place for new system changes (M, H)
- [ ] Consent mechanisms documented for PII collection (where applicable) (M, H)

---

## 15. CJIS Overlay (if applicable)

Only required for providers handling Criminal Justice Information (CJI):

- [ ] Provider has identified CJI data types in scope
- [ ] CJIS Security Policy requirements mapped to GovRAMP controls
- [ ] Using the GovRAMP Service Provider Package for Moderate Impact with CJIS Overlay
- [ ] Using the GovRAMP 3PAO Package for Moderate Impact with CJIS Overlay
- [ ] CJI handling, access, and storage controls documented separately

---

## 16. Authorization Documentation Completeness

- [ ] System Security Plan (SSP) is drafted using GovRAMP templates
- [ ] All required control implementation statements present in SSP
- [ ] Authorization boundary diagram embedded in SSP
- [ ] Data flow diagrams embedded in SSP
- [ ] PPS table completed in SSP
- [ ] External connections table completed in SSP
- [ ] Incident Response Plan included as SSP appendix or standalone
- [ ] Contingency Plan included as SSP appendix or standalone
- [ ] Plan of Action & Milestones (POA&M) is drafted
- [ ] All known gaps entered in POA&M with risk ratings and remediation plans
- [ ] Vulnerability scan results available for submission
- [ ] Penetration test report available (Ready and Authorized)

---

## Readiness Summary (Completed Checklist Output)

After completing the checklist, summarize:

| Category | Met Count | Not Met Count | Blockers for Status? |
|----------|-----------|---------------|----------------------|
| Boundary / Documentation | | | |
| Policies and Procedures | | | |
| Access Control | | | |
| Encryption | | | |
| Vulnerability Management | | | |
| Logging / Monitoring | | | |
| Incident Response | | | |
| Contingency Planning | | | |
| Configuration Management | | | |
| Personnel Security | | | |
| Authorization Documentation | | | |

**Top 5–10 Priority Gaps:** [List highest-risk items blocking the target status]

**Recommended Next Step:** [Core / Ready / Authorized / Fast Track / Progressing Snapshot]

# FedRAMP SSP Appendices Guide (A–Q)

All FedRAMP SSP appendices must use official FedRAMP templates where indicated.
Templates: https://www.fedramp.gov/rev5/documents-templates/

---

## Appendix A — Acronyms & Glossary
**Required:** Yes | **Author:** CSP
- List all acronyms used in the SSP
- Define any system-specific or agency-specific terms
- FedRAMP provides a standard glossary; supplement with system-specific terms
- Keep synchronized with the SSP body — if a new term appears in Section 7, add it here

---

## Appendix B — Related Laws & Regulations
**Required:** Yes | **Author:** CSP (use FedRAMP template as base)
- Enumerates applicable federal laws, Executive Orders, OMB memos, and standards
- Core list includes: FISMA 2014, Privacy Act of 1974, E-Government Act (Section 208), FIPS 199, FIPS 200, NIST SP 800-53 Rev 5, OMB Circular A-130
- Add agency-specific requirements if applicable (e.g., HIPAA, CJIS, IRS Publication 1075)
- Review annually — regulatory landscape changes; new OMB guidance and executive orders may require additions

**Common mistake:** Using the Rev 4 version of this appendix; ensure it reflects Rev 5 requirements and current OMB directives.

---

## Appendix C — Security Policies & Procedures
**Required:** Yes | **Author:** CSP
- Attach or reference all CSP security policies and standard operating procedures
- Must cover each NIST 800-53 Rev 5 control family that has policies and procedures controls (e.g., AC-1, AU-1, CA-1, CM-1, etc.)
- Policies must be: approved by senior leadership, dated, versioned, and reviewed at defined intervals
- Common approach: include a policy index table in the appendix body, with the actual policy documents attached or linked via evidence repository

**Common finding:** Policies exist but are not dated or version-controlled; policies reference Rev 4 controls.

---

## Appendix D — User Guide
**Required:** Yes | **Author:** CSP
- End-user guide for the cloud service
- Describes: how to access the system, user responsibilities, what the system does, how to report security incidents
- For SaaS offerings, this may be a customer-facing documentation excerpt
- Must align with the Rules of Behavior (Appendix E)

---

## Appendix E — Rules of Behavior (RoB)
**Required:** Yes | **Author:** CSP (FedRAMP template available)
- Signed by all users prior to access
- Covers: acceptable use, data handling obligations, password requirements, incident reporting obligations, consequences of non-compliance
- Must be re-signed annually or when updated
- Keep signature records — auditors will ask for evidence of signed RoBs

**Common finding:** RoB exists but no evidence of user signatures; RoB not updated after major policy changes.

---

## Appendix F — IT Contingency Plan (ISCP)
**Required:** Yes | **Author:** CSP (FedRAMP ISCP template — updated December 2024)
- Use the FedRAMP Information System Contingency Plan (ISCP) template
- Must include: system description, activation criteria, notification procedures, recovery procedures, reconstitution, testing records
- RTO and RPO must be defined and achievable based on architecture
- Must be tested at least annually — tabletop minimum; functional exercise preferred for High baseline
- Append the most recent test results

**Common finding:** Plan exists but has never been tested; RTO/RPO are aspirational and not validated by DR testing.

---

## Appendix G — Configuration Management Plan (CMP)
**Required:** Yes | **Author:** CSP
- Describes how configuration baselines are established, maintained, and enforced
- Must reference specific baseline standards used (CIS Benchmarks, DISA STIGs)
- Documents the change control board (CCB) process and approval chain
- Defines how configuration deviations are documented and approved
- Links to the system inventory (IIW — Appendix K)

---

## Appendix H — Incident Response Plan (IRP)
**Required:** Yes | **Author:** CSP
- Must follow NIST SP 800-61 Rev 2 lifecycle: Preparation → Detection → Containment → Eradication → Recovery → Post-Incident
- FedRAMP-specific reporting SLAs:
  - Report to US-CERT within **1 hour** of incident discovery (high-priority incidents)
  - Report to agency AO within **1 hour** for incidents affecting federal data
- Include contact list: CSP IR team, agency AO contacts, US-CERT (CISA), FedRAMP PMO Security Inbox
- Must include the FedRAMP Security Inbox address for PMO notifications
- Must be tested at least annually (tabletop or functional exercise)

**Common finding:** IRP does not include agency AO notification procedure; reporting timeframes do not match FedRAMP SLAs; no evidence of annual testing.

---

## Appendix I — Control Implementation Summary (CIS) / Customer Responsibility Matrix (CRM)
**Required:** Yes | **Author:** CSP (FedRAMP CIS/CRM template)
- One of the most operationally important appendices for agency customers
- **CIS tab**: Lists every control in the baseline and its implementation status (Fully Implemented / Partially Implemented / Planned / Not Applicable / Alternative)
- **CRM tab**: For each shared/hybrid control, defines exactly what the CSP implements vs. what the customer/agency must implement
- Agency customers use the CRM to understand their inherited security obligations
- Must be kept current — a stale CRM is a common agency complaint and a finding during re-authorization

**Common mistake:** CRM lists "Customer Responsibility" generically without specifying what the agency must actually do; shared controls marked as fully CSP-implemented when agencies have configuration responsibilities.

---

## Appendix J — FIPS 199 Categorization
**Required:** Yes | **Author:** CSP
- Documents the formal FIPS 199 impact determination
- Categorizes Confidentiality, Integrity, and Availability separately for each information type
- Overall impact level = high-water mark (highest individual rating)
- Must justify each categorization with the types of federal information the system processes
- Ties directly to which FedRAMP baseline (Low / Moderate / High) applies

---

## Appendix K — Integrated Inventory Workbook (IIW)
**Required:** Yes | **Author:** CSP (FedRAMP IIW template — updated December 2024)
- Complete inventory of every asset within the authorization boundary
- Tabs typically include: hardware, software, services, databases, network components, virtual instances
- Must be 100% accurate — auditors sample from IIW and will flag missing assets as findings
- Updated continuously; submitted monthly during ConMon
- Must include: asset name/ID, OS/version, IP address, function, patch level, FedRAMP status, POC

**Common finding:** IIW is out of date; cloud-native ephemeral resources (auto-scaling instances, containers) not accounted for with appropriate dynamic inventory process.

---

## Appendix L — Cryptographic Modules Table
**Required:** Yes | **Author:** CSP
- Lists every cryptographic module in use within the boundary
- For each module: vendor, product name, version, FIPS 140-2/3 validation certificate number, use case (encryption at rest, in transit, key management, etc.)
- All modules must have active FIPS 140-2 or 140-3 validation certificates (check NIST CMVP)
- Identifies any non-FIPS algorithms still in use (must be remediated or deviation-approved)

**Common finding:** Module versions have changed since last authorization and certificates are no longer valid; legacy algorithms (MD5, SHA-1, DES, RC4) found in use without deviation.

---

## Appendix M — Continuous Monitoring Plan
**Required:** Yes | **Author:** CSP
- Documents the ongoing ConMon program
- Must specify: scan frequency and tools, vulnerability management SLAs, POA&M update cadence, reporting schedule to agency AO, annual assessment approach
- Scan requirements: OS/infrastructure monthly; web app monthly; database monthly; container images per CI/CD pipeline
- References the Security Inbox requirement (effective January 2026)

---

## Appendix N — Separation of Duties Matrix
**Required:** Conditional (required when separation of duties is a compensating control or specifically required by agency) | **Author:** CSP
- Documents which roles can and cannot be combined
- Relevant when a small team might otherwise hold conflicting privileges
- Ties to AC-5 (Separation of Duties) control implementation

---

## Appendix O — Plan of Action & Milestones (POA&M)
**Required:** Yes | **Author:** CSP (FedRAMP POA&M template)
- See `references/poam-guide.md` for full field definitions and SLA table
- Living document — updated monthly during ConMon
- Submitted monthly to agency AO(s)
- Every SAR finding must appear as a POA&M row

---

## Appendix P — Supply Chain Risk Management Plan (SCRM Plan)
**Required:** Yes (Rev 5) | **Author:** CSP
- New requirement introduced with NIST SP 800-53 Rev 5 (SR control family)
- Documents how the CSP manages supply chain risks for hardware, software, and services
- Must address: supplier assessment process, SBOM tracking, open source component vulnerability management, critical supplier identification
- Ties to SR-1 through SR-12 control implementations

**Common finding:** SCRM Plan is generic and doesn't describe the CSP's specific suppliers or risk assessment methodology; SBOM process undefined.

---

## Appendix Q — Privacy Impact Assessment (PIA)
**Required:** If PII is in scope | **Author:** CSP
- Required when the system collects, processes, stores, or transmits PII
- Must follow the E-Government Act of 2002 Section 208 PIA requirements
- Covers: what PII is collected, why, how it's protected, retention, access controls, sharing with third parties
- Ties to PT control family (PII Processing & Transparency) — new in Rev 5
- Agency AO reviews PIA as part of authorization decision when PII is involved

**Common finding:** PIA omits specific PII data elements; PIA not updated when new PII types are added to the system.

---

## Quick Reference: Appendix Checklist

| App | Title | Required | Template |
|-----|-------|----------|----------|
| A | Acronyms & Glossary | Yes | CSP-authored |
| B | Laws & Regulations | Yes | FedRAMP base + CSP additions |
| C | Security Policies & Procedures | Yes | CSP-authored |
| D | User Guide | Yes | CSP-authored |
| E | Rules of Behavior | Yes | FedRAMP template |
| F | IT Contingency Plan (ISCP) | Yes | FedRAMP ISCP template (Dec 2024) |
| G | Configuration Management Plan | Yes | CSP-authored |
| H | Incident Response Plan | Yes | CSP-authored |
| I | CIS / CRM Workbook | Yes | FedRAMP template |
| J | FIPS 199 Categorization | Yes | CSP-authored |
| K | Integrated Inventory Workbook (IIW) | Yes | FedRAMP template (Dec 2024) |
| L | Cryptographic Modules Table | Yes | CSP-authored |
| M | Continuous Monitoring Plan | Yes | CSP-authored |
| N | Separation of Duties Matrix | Conditional | CSP-authored |
| O | POA&M | Yes | FedRAMP template |
| P | Supply Chain Risk Management Plan | Yes (Rev 5) | CSP-authored |
| Q | Privacy Impact Assessment (PIA) | If PII in scope | CSP-authored |

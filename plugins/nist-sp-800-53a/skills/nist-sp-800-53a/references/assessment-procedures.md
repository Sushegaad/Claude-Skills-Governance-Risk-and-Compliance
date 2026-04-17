# Assessment Procedures Reference — NIST SP 800-53A Rev 5

This reference file provides assessment procedure guidance for all 20 SP 800-53 Rev 5 control families. For each family, the key assessment objectives, methods, evidence objects, and expected findings are described.

Source: NIST SP 800-53A Rev 5, January 2022

---

## How to Use This Reference

Each control family entry describes:
- **Assessment objectives**: What determination(s) must be made
- **Examine**: What documents and artefacts to review
- **Interview**: Which roles to speak with and what to ask
- **Test**: What mechanisms, processes, or activities to exercise
- **Satisfied evidence**: What makes a control Satisfied
- **Common OTS findings**: Frequent Other Than Satisfied patterns

---

## AC — Access Control

### Key Assessment Focus
Verify that access to the system is limited to authorised users, processes, and devices; that least privilege is enforced; and that accounts are managed through a defined lifecycle.

### AC-1 Policy and Procedures
**Objectives**: Formal access control policy exists, covers required elements, is disseminated, reviewed, and updated per stated frequency.
**Examine**: Access control policy, procedures, revision history, distribution records
**Interview**: ISSO, system owner — how is the policy maintained and communicated?
**Satisfied if**: Current policy exists, reviewed within the defined period, distributed to all relevant personnel

### AC-2 Account Management
**Objectives**: Account types defined; accounts created, enabled, modified, disabled, and removed per procedures; account reviews conducted; inactive accounts disabled; temporary/emergency accounts expire
**Examine**: Account management policy, SSP narrative, account listings (privileged and non-privileged), recent account review records, ticketing records for account requests
**Interview**: System administrator — account creation workflow; ISSO — frequency and evidence of account reviews
**Test**: Submit test account request and verify workflow; verify a terminated account is disabled/removed; check for accounts without recent logins

### AC-3 Access Enforcement
**Objectives**: System enforces approved authorisations for access to system resources
**Examine**: Access control mechanism configuration (Active Directory, IAM tool, RBAC configs), SSP control implementation description
**Test**: Attempt to access a resource without authorisation (from a non-privileged test account); verify access is denied and logged

### AC-6 Least Privilege
**Objectives**: Principle of least privilege employed; users given only the access required for their role; separation of duties enforced
**Examine**: Role definitions, privilege assignment matrix, privileged account justifications
**Test**: Review current privilege assignments against documented role requirements; check for accounts with privileges beyond documented role

---

## AT — Awareness and Training

### Key Assessment Focus
Verify that all users (including privileged users) receive security awareness training and that role-based training specific to security responsibilities is provided and documented.

### AT-1 Policy and Procedures
**Examine**: Awareness and training policy, training procedures, revision history
**Interview**: Training coordinator — how is training tracked?

### AT-2 Literacy Training and Awareness
**Objectives**: Security awareness training provided to all users before access and recurring per defined frequency; training covers required topics (phishing, social engineering, password security)
**Examine**: Training completion records (by user), training content, training completion reports, evidence of annual refresher
**Interview**: User personnel — have you completed security awareness training? ISSO — How is training completion enforced?
**Satisfied if**: 100% of current users have completed training within the last period; training content addresses required topics

### AT-3 Role-Based Training
**Objectives**: Individuals with significant security responsibilities receive role-specific training before assigned duties and annually
**Examine**: Role-based training curriculum, completion records by role, training materials specific to each security-sensitive role
**Interview**: System administrator, ISSO — what role-specific security training have you completed?

---

## AU — Audit and Accountability

### Key Assessment Focus
Verify that the system generates audit records for required events, that records are protected and retained, and that they are reviewed for anomalies.

### AU-2 Event Logging
**Objectives**: System generates audit records for organisationally defined events; events include required categories (logon/logoff, admin activity, object access, policy changes)
**Examine**: Audit event configuration (SIEM correlation rules, OS audit policy, application logging settings), SSP narrative
**Test**: Trigger an auditable event (e.g., failed logon, account change) and verify the record is generated with required fields

### AU-3 Audit Record Content
**Objectives**: Audit records contain date/time, event type, subject identity, object, outcome, source address
**Examine**: Sample audit records from the SIEM or log management system
**Test**: Review 20+ sample log entries across different event types and verify all required fields are present in each

### AU-9 Protection of Audit Information
**Objectives**: Audit records protected from unauthorised access, modification, and deletion; audit tools protected
**Examine**: ACLs on log repositories, SIEM access controls, log forwarding configuration
**Test**: Attempt to modify or delete audit records from a standard user account; verify the attempt is denied

---

## CA — Assessment, Authorization, and Monitoring

### Key Assessment Focus
Verify that the system has been formally assessed, authorised, is under continuous monitoring, and that the SSP and authorisation package are current.

### CA-2 Control Assessments
**Objectives**: Periodic security assessments conducted by assessors with required independence; assessment results documented; deficiencies addressed
**Examine**: Most recent SAR, SAP, assessor qualifications and independence attestation, POA&M updating records showing deficiency remediation
**Interview**: ISSO — when was the last assessment? How are findings tracked?

### CA-5 Plan of Action and Milestones
**Objectives**: POA&M developed for the system; POA&M documents deficiencies, resources, milestones; POA&M updated per defined frequency
**Examine**: Current POA&M, POA&M update history, evidence that closed items have been verified
**Satisfied if**: POA&M reflects current SAR findings; milestone dates are being met or have justified extensions

### CA-7 Continuous Monitoring
**Objectives**: Continuous monitoring strategy defined; security controls monitored per defined frequency; security status reported to AO; ongoing authorisation maintained
**Examine**: ISCM strategy document, monitoring frequency table, automated monitoring tool reports, status reports to AO

---

## CM — Configuration Management

### Key Assessment Focus
Verify that the system has a documented and enforced baseline configuration, that changes go through a controlled process, and that only authorised software is installed.

### CM-2 Baseline Configuration
**Objectives**: Baseline configuration for the system is established, documented, reviewed, and updated
**Examine**: Approved baseline configuration documents (per OS/application version), change records showing update of baseline after approved changes
**Interview**: System administrator — where is the baseline configuration documented? How is it maintained?

### CM-3 Configuration Change Control
**Objectives**: All configuration changes go through an approved change control process including impact analysis, testing, and approval before implementation
**Examine**: Change management policy, sample change requests (approved and denied), change advisory board records, emergency change records
**Test**: Review 10 recent changes in the change management system and verify each has documented request, approval, and optionally rollback plan

### CM-6 Configuration Settings
**Objectives**: Configuration settings for technology components implement the most restrictive settings consistent with operational requirements; settings are documented and enforced
**Examine**: Approved configuration settings (CIS Benchmarks, DISA STIGs, or equivalent), system scans against baseline, vulnerability scan results showing configuration compliance
**Test**: Run a configuration compliance scan (CIS benchmark or STIG check) and compare results to the approved baseline; document any deviations

---

## CP — Contingency Planning

### Key Assessment Focus
Verify that the organisation can recover from disruptions and that the contingency plan has been tested.

### CP-2 Contingency Plan
**Objectives**: Contingency plan developed; covers all required elements (BIA, recovery objectives, roles and responsibilities, procedures); reviewed and updated per defined frequency
**Examine**: Contingency plan document, BIA, most recent plan review and update record
**Interview**: Contingency plan coordinator — when was the last plan review? How often are recovery objectives validated?

### CP-9 System Backup
**Objectives**: System backup performed per defined frequency; backup copies stored at alternate location; backup integrity verified; restoration tested
**Examine**: Backup policy, backup job logs (confirming completion per schedule), offsite/cloud storage records, restoration test records
**Test**: Review backup job logs for the past 30 days and verify completion at required frequency; request evidence of a recent restoration test

---

## IA — Identification and Authentication

### Key Assessment Focus
Verify that all users are uniquely identified and authenticated using mechanisms meeting the required assurance level, including multi-factor authentication for privileged accounts.

### IA-2 Identification and Authentication (Org Users)
**Objectives**: System uniquely identifies and authenticates all organisational users; MFA enforced for network access, privileged accounts, and non-privileged accounts per applicable baseline
**Examine**: Authentication mechanism configuration (MFA settings, LDAP/AD configuration), SSP IA narrative
**Test**: Verify MFA is enforced by attempting to access the system with only a password from a test privileged account; confirm MFA prompt appears

### IA-5 Authenticator Management
**Objectives**: Organisation manages system authenticators; initial authenticator content meets requirements; administrative procedures for lost/compromised authenticators; password minimum/complexity/expiration enforced
**Examine**: Password policy configuration, evidence of secure initial distribution of credentials, authenticator recovery procedures
**Test**: Verify password minimum complexity and length enforcement via account settings; review recent password resets for proper procedure adherence

---

## IR — Incident Response

### Key Assessment Focus
Verify that the organisation has a tested incident response capability including detection, handling, and reporting.

### IR-1 Policy and Procedures
**Examine**: Incident response policy, procedures, revision history

### IR-4 Incident Handling
**Objectives**: Incident handling capability established covering preparation, detection, analysis, containment, eradication, and recovery; incidents tracked and documented; lessons learned incorporated
**Examine**: IR plan, incident tracking log (with real incidents), post-incident reviews
**Interview**: ISSO or IR team lead — walk through the last significant incident response
**Test**: Tabletop exercise results; verify team knows who to notify and within what timeframe for each category of incident

### IR-6 Incident Reporting
**Objectives**: Personnel report incidents within defined timeframe; incidents reported to US-CERT within 1 hour of discovery (for federal agencies per OMB M-20-04)
**Examine**: Incident reporting logs, evidence of US-CERT notifications, internal escalation records

---

## MA — Maintenance

### Key Assessment Focus
Verify that system maintenance is performed in a controlled manner and that remote maintenance is properly authorised, logged, and terminated.

### MA-2 Controlled Maintenance
**Objectives**: System maintenance scheduled, performed, documented, and records reviewed; maintenance requires approval; maintenance activities logged
**Examine**: Maintenance logs, approved maintenance schedules, work orders or ticketing records for maintenance activities
**Interview**: System administrator — how is scheduled and unscheduled maintenance authorised?

### MA-4 Nonlocal Maintenance
**Objectives**: Remote maintenance and diagnostic activities authorised and monitored; remote maintenance sessions authenticated via MFA; sessions terminated after completion
**Examine**: Remote maintenance policy, logs of remote maintenance sessions, VPN/jump server configuration
**Test**: Verify remote maintenance session recordings exist for recent sessions; confirm sessions are terminated after use

---

## MP — Media Protection

### Key Assessment Focus
Verify that media containing sensitive information is properly marked, stored, transported, sanitised, and destroyed.

### MP-6 Media Sanitisation
**Objectives**: System media sanitised before disposal or reuse; sanitisation implemented per NIST SP 800-88 guidelines; sanitisation actions documented
**Examine**: Media sanitisation policy, sanitisation records (by device serial number), data destruction certificates, contracts with sanitisation vendors
**Interview**: IT staff responsible for media sanitisation — what tool or method is used? How are records kept?

---

## PE — Physical and Environmental Protection

### Key Assessment Focus
Verify that physical access to the facility and system is controlled, monitored, and logged.

### PE-2 Physical Access Authorisations
**Objectives**: List of individuals authorised for physical access maintained and reviewed per defined frequency; access removed when no longer required
**Examine**: Physical access authorisation list, badge access configuration, recent review records showing verification and update of the list
**Test**: Review access list against current HR roster to identify terminated employees or contractors with active physical access

### PE-6 Monitoring Physical Access
**Objectives**: Physical access to the facility monitored; intrusion alarms and surveillance equipment monitored; physical access logs reviewed
**Examine**: Physical access log (badge in/out), surveillance system configuration, alert monitoring logs, visitor logs

---

## PL — Planning

### Key Assessment Focus
Verify that the system has a complete, current, and approved System Security Plan.

### PL-2 System Security Plan
**Objectives**: SSP developed for the system; SSP includes all required sections; SSP reviewed and updated per defined frequency; SSP protects from unauthorised disclosure
**Examine**: Current SSP with all sections (boundary, data types, control narratives, interconnections), SSP revision history, distribution controls
**Interview**: ISSO — when was the SSP last reviewed and updated?

---

## PM — Program Management

### Key Assessment Focus
Verify that organisation-wide security programme management controls exist at the enterprise level (not system-specific).

### PM-1 Information Security Program Plan
**Objectives**: Enterprise information security programme plan exists, covers required organisational areas, is reviewed and updated
**Examine**: Information security programme plan, governance documentation, risk executive appointment

---

## PS — Personnel Security

### Key Assessment Focus
Verify that background investigations are conducted and that access is terminated promptly when personnel leave.

### PS-3 Personnel Screening
**Objectives**: Individuals screened prior to system access; re-screening performed based on position sensitivity
**Examine**: Background investigation records or adjudication confirmations, position sensitivity designations
**Interview**: HR security coordinator — what background check is required before access? How are contractors handled?

### PS-4 Personnel Termination
**Objectives**: Access terminated upon separation; final exit checklist completed; credentials revoked; return of equipment confirmed
**Examine**: Exit checklist (with completed items), termination date vs. access revocation date records; ideally same-day revocation for sensitive systems
**Test**: Identify the 5 most recent terminations and compare termination date to account disable date in the identity management system

---

## PT — PII Processing and Transparency (Privacy)

### Key Assessment Focus
Verify that the organisation identifies, maps, and governs PII processing and provides transparency to affected individuals.

### PT-1 Policy and Procedures
**Examine**: Privacy policy, PII processing procedures

### PT-3 Personally Identifiable Information Processing Purposes
**Objectives**: PII processing limited to documented, authorised purposes; individuals notified of PII processing purposes
**Examine**: Privacy impact assessment (PIA), data flow diagrams showing PII, data inventory/PII inventory, privacy notice(s)

---

## RA — Risk Assessment

### Key Assessment Focus
Verify that the system risk assessment is current and that vulnerabilities are identified and remediated in a timely manner.

### RA-3 Risk Assessment
**Objectives**: Risk assessment conducted; risk assessment documents threats, vulnerabilities, likelihood, and impact; risk assessment reviewed and updated per defined frequency or trigger events
**Examine**: Current risk assessment report, risk assessment methodology, evidence of review and update after significant changes

### RA-5 Vulnerability Monitoring and Scanning
**Objectives**: Vulnerability scans conducted per defined frequency; high/critical vulnerabilities remediated within defined timeframe; vulnerability scan results shared with appropriate personnel
**Examine**: Vulnerability scan reports (most recent), scan schedule, remediation tracking records
**Test**: Review the last 3 scan reports; calculate the percentage of critical vulnerabilities remediated within the required timeframe; compare to the POA&M

---

## SA — System and Services Acquisition

### Key Assessment Focus
Verify that security requirements are included in acquisitions and that developer security testing is required.

### SA-4 Acquisition Process
**Objectives**: Security functional requirements, assurance requirements, and documentation requirements included in contracts and acquisition documents
**Examine**: Sample contracts or statements of work (SOWs), system requirements documents, security addenda to contracts

### SA-11 Developer Testing and Evaluation
**Objectives**: Developer required to conduct security testing including unit tests, integration tests, and regression tests; test results provided; flaws identified and remediated
**Examine**: Developer testing requirements in contracts, test plans and results from developers, flaw remediation records

---

## SC — System and Communications Protection

### Key Assessment Focus
Verify that the system boundary is defined and enforced, communications are encrypted, and network traffic is controlled.

### SC-5 Denial of Service Protection
**Objectives**: System protects against denial-of-service attacks or limits their effects
**Examine**: DDoS protection configuration (rate limiting, CDN/WAF settings), SSP SC narrative
**Test**: Review network device configurations for rate limiting settings; verify DDoS protection service is active

### SC-7 Boundary Protection
**Objectives**: System implements a managed interface at each external boundary; network traffic controlled; only approved ports, protocols, and services allowed
**Examine**: Network diagrams (showing boundary devices), firewall rule sets, router/switch ACLs, data flow diagrams
**Test**: Verify that the firewall rule set contains a default deny; review open ports and services against the approved list in the SSP; check for any "any-any" rules

### SC-28 Protection of Information at Rest
**Objectives**: Information at rest is protected via encryption or equivalent mechanism
**Examine**: Encryption configuration for storage (full disk encryption, database encryption, file-level encryption), key management documentation
**Test**: Verify encryption is enabled on storage volumes and databases per configuration artifacts; confirm encryption standard meets current requirements (AES-256 or equivalent)

---

## SI — System and Information Integrity

### Key Assessment Focus
Verify that the system detects and remediates flaws, is protected from malicious code, and monitors for security alerts.

### SI-2 Flaw Remediation
**Objectives**: System flaws identified, reported, and corrected; software updates provided, tested, and installed within defined timeframes; security alerts and advisories issued
**Examine**: Patch management policy, patch scan results (most recent), patch completion metrics, POA&M entries for deferred patches
**Test**: Run or review a patch scan for the past 30 days; verify critical patches are installed within the required timeframe (typically 30 days for Critical, 90 days for High)

### SI-3 Malicious Code Protection
**Objectives**: Malicious code protection mechanisms at entry/exit points and on endpoints; updated per defined frequency; scanning actions defined
**Examine**: AV/EDR solution configuration and coverage reports, definition update frequency configuration, scan logs
**Test**: Verify AV/EDR definitions are current (within 24 hours for signature-based), confirm coverage of all endpoints per inventory

---

## SR — Supply Chain Risk Management

### Key Assessment Focus
Verify that the organisation identifies, manages, and monitors supply chain risks for the information system.

### SR-1 Policy and Procedures
**Examine**: SCRM policy, supply chain risk management procedures, revision history

### SR-2 Supply Chain Risk Management Plan
**Objectives**: SCRM plan developed for the system; plan considers risks from suppliers, developers, and service providers; plan reviewed and updated
**Examine**: SCRM plan, supplier risk assessments, approved supplier/developer list

### SR-11 Component Authenticity
**Objectives**: Anti-counterfeit controls employed; provenance of components tracked; counterfeit components prevented, detected, and disposed of
**Examine**: Hardware procurement records showing authorised suppliers, SBOM (if applicable), component inventory with provenance tracking

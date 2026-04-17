# GovRAMP System Security Plan (SSP) Writing Guide

The System Security Plan (SSP) is the foundational document for any GovRAMP
authorization. It describes what the system is, what data it handles, how the
authorization boundary is defined, and how each applicable NIST 800-53 Rev 5 control
is implemented.

GovRAMP templates align with FedRAMP document structures and are accepted in FedRAMP
formatting. Always use official GovRAMP templates available at:
https://govramp.org/rev-5-templates-and-resources/

Service Provider Packages are available for:
- Low Impact
- Moderate Impact (most common)
- Moderate Impact with CJIS Overlay
- High Impact

---

## SSP Section-by-Section Guide

### Section 1: System Name and Identifier

- Formal product/service name
- Unique product identifier
- Service model: SaaS / PaaS / IaaS
- Deployment model: Public / Private / Community / Hybrid cloud
- GovRAMP membership number (if available at time of writing)

---

### Section 2: System Categorization and Impact Level

- Complete FIPS 199 categorization for each information type handled:
  - Confidentiality: Low / Moderate / High
  - Integrity: Low / Moderate / High
  - Availability: Low / Moderate / High
- Overall impact level = high-water mark of the three values
- Justify each categorization with the types of government information processed
- Cross-reference the GovRAMP Data Classification Tool output
- Identify whether CJIS Overlay applies

**Common SSP mistakes:**
- Assigning "Low" to all categories without justification when moderate-sensitivity
  government data is involved
- Not documenting information types — vague statements like "we process government data"
  are insufficient

---

### Section 3: System Ownership and Contacts

- System Owner name, title, and contact information
- GovRAMP Program Manager contact
- Authorizing Official contact (government sponsor, once identified)
- Primary 3PAO contact (for Ready/Authorized paths)

---

### Section 4: Assignment of Security Responsibility

- Identify the person (title and contact) responsible for the overall security of the system
- Document the security team structure if applicable

---

### Section 5: System Mission and Purpose

- What does the system do?
- What government programs, agencies, or organizations does it serve?
- What types of government data does it handle?
- Who are the typical end users?

---

### Section 6: General System Description

- Narrative description of the technology stack
- Key system components (web servers, databases, APIs, integrations)
- Cloud platform and region (if cloud-hosted)
- Whether the system uses a FedRAMP-authorized IaaS/PaaS (AWS GovCloud, Azure Government,
  Google Cloud FedRAMP regions) — critical for inherited control documentation

---

### Section 7: Authorization Boundary (Highest Scrutiny)

This is one of the most scrutinized sections in any GovRAMP review.

**What to include:**
- Clear written narrative describing exactly what is inside and outside the boundary
- Which components process, store, or transmit government data (all must be inside)
- Which external services are used and whether they are in or out of scope
- Network architecture diagram embedded (not just referenced as an attachment)
- Data flow diagrams showing all data entering, leaving, and moving within the boundary
- Ports, Protocols, and Services (PPS) table
- External connections table (documenting every connection to services outside the boundary)

**Inherited Controls:**
If the provider uses a FedRAMP-authorized IaaS/PaaS, document which controls are:
- Fully inherited: The IaaS/PaaS fully satisfies the control; provider has no additional obligation
- Partially inherited: The IaaS/PaaS satisfies part of the control; provider must address the remainder
- Not inherited: Provider fully implements the control

**Common boundary mistakes:**
- Vague boundary language such as "our cloud environment" without specifying which
  services, regions, and components are in scope
- Not documenting admin/management traffic flows (VPN, jump boxes, monitoring agents)
- Failing to document external SaaS tools used by operations staff that touch in-scope data
- Not updating the boundary when systems change

---

### Section 8: Control Implementation Statements

This is the largest and most critical section of the SSP. For each applicable NIST
800-53 Rev 5 control:

**Required sub-elements per control:**

1. **Implementation Status**: Implemented / Partially Implemented / Planned / Alternative Implementation
2. **Control Origination**: Provider (CSP), Customer/Government, Shared, or Inherited from leveraged service
3. **Implementation Description**: Prose narrative describing exactly how the control is satisfied

**Writing principles:**

- **Describe only what is implemented** — Do not describe planned or aspirational controls
  as if they are in place. Unimplemented controls must go in the POA&M.
- **Be specific** — Reference exact tool names, policy document names, configuration
  settings, section numbers. Vague language causes findings.
- **Address every verb** — Each control requirement uses specific action verbs (establish,
  implement, enforce, document, review, test, monitor). Address each one explicitly.
- **Shared responsibility** — For any control where both the provider and the government
  customer share responsibility, create a clear "Customer Responsibility" section.
- **Internal consistency** — Control statements must be consistent with the architecture
  diagrams, data flow diagrams, and system inventory. Inconsistencies cause findings.

**Example structure for a control narrative:**

```
AC-2 — Account Management

Implementation Status: Implemented
Control Origination: Service Provider (with Customer Responsibility noted)

The [System Name] manages user accounts using [identity management tool/system]. 
Account provisioning requires approval from [role/team] via [ticketing system].
Accounts are reviewed quarterly by [role] against the current inventory of 
authorized users. Accounts are disabled within [X hours] of termination notification 
received from [HR/manager via process].

Customer Responsibility: Government customers are responsible for notifying 
[System Name] administrators within [timeframe] when a user transfers, changes 
role, or is terminated.
```

---

### Section 9: Leveraged Authorizations

If the system uses a FedRAMP-authorized or GovRAMP-authorized platform:

- List each leveraged service name, authorization type (FedRAMP/GovRAMP), and impact level
- Use the Cloud Integration Standard (CIS) / Customer Responsibility Matrix (CRM) workbook
  to document which controls are inherited vs. provider-implemented vs. customer responsibility
- The GovRAMP PMO accepts documents in FedRAMP formatting for this workbook

---

### Section 10: Interconnections

- List all external connections (to government systems, other vendors, etc.)
- For each interconnection: system name, owner, connection type, data type, security controls
- Interconnection Security Agreements (ISAs) or Memoranda of Understanding (MOUs) should
  reference each interconnection

---

## SSP Appendices Required for GovRAMP

| Appendix | Content |
|----------|---------|
| Incident Response Plan (IRP) | Documented and tested within past 12 months |
| Contingency Plan (CP) | Documented and tested within past 12 months |
| Rules of Behavior | User acknowledgment of acceptable use |
| Privacy Impact Assessment (PIA) | Required for Moderate and High where PII is processed |
| Vulnerability Scan Results | Most recent scan results for all applicable layers |
| POA&M | All open findings with risk ratings and remediation plans |
| Authorization Boundary Diagram | Standalone diagram if not embedded in Section 7 |

---

## SSP Writing Tips by Control Family

### Access Control (AC)
- Be specific about how MFA is enforced — name the tool (e.g., Duo, Okta, Azure AD MFA)
- Document RBAC roles explicitly; generic statements like "we use role-based access"
  are insufficient
- Address privileged account controls separately from standard user controls

### Audit and Accountability (AU)
- Name the SIEM or logging platform
- Specify log retention: minimum 90 days accessible online, total 1 year retained
- Document who reviews logs and at what frequency
- Identify which audit events are captured (NIST 800-53 AU-2 event types)

### Configuration Management (CM)
- Reference the specific baseline standard used (CIS Benchmark, DISA STIG)
- Name the configuration management tool (Ansible, Puppet, AWS Config, etc.)
- Describe the change management process and approval workflow

### Identification and Authentication (IA)
- State that FIPS 140-2 or 140-3 validated cryptographic modules are used
- Reference the specific module (e.g., OpenSSL FIPS module) if known
- Describe password/authentication policy specifics (MFA types, session timeout)

### Incident Response (IR)
- Reference the IRP appendix but also summarize roles, reporting timelines, and
  GovRAMP reporting obligations in the control narrative
- Include the GovRAMP Incident Communications Procedures contact information

### Risk Assessment (RA)
- Name the vulnerability scanning tools used and their scope (OS, DB, web app, container)
- Reference the scan frequency and confirm alignment with GovRAMP Vulnerability Scan
  Requirements Guide
- Address penetration testing cadence and methodology

### System and Communications Protection (SC)
- Document encryption in transit: TLS version and which connections are encrypted
- Document encryption at rest: algorithm, key length, FIPS module reference
- Describe network segmentation between in-scope and out-of-scope components

---

## Common SSP Review Findings

The following are frequently cited GovRAMP review findings that delay authorization:

1. Control statements that say "we plan to implement" rather than "we have implemented"
2. Missing PPS table or incomplete external connections documentation
3. Architecture diagram that does not match the written boundary description
4. Inherited controls listed without referencing the specific leveraged authorization
5. Missing customer responsibility sections for shared controls
6. IRP and CP that have not been tested or lack test documentation
7. Incomplete POA&M — known gaps existed but were not documented
8. No documentation of vulnerability scans or scans that do not cover all boundary components
9. Encryption described vaguely — no module name, no algorithm specification
10. Logging not covering all in-scope components

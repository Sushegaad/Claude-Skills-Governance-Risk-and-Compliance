# GovRAMP Continuous Monitoring (ConMon) Guide

Continuous Monitoring (ConMon) is the ongoing obligation for all products with a
verified GovRAMP security status to demonstrate that their security posture is
maintained after initial authorization. GovRAMP requires ConMon activities to be
conducted and reported to the PMO per the official GovRAMP Continuous Monitoring Guide.

Download the official guide at:
https://govramp.org/blog/document/stateramp-continuous-monitoring-guide/

For escalation procedures:
GovRAMP Continuous Monitoring Escalation Process Guide (available at https://govramp.org/rev-5-templates-and-resources/)

---

## ConMon Obligations by Status

| GovRAMP Status | ConMon Frequency | Key Deliverables |
|---------------|-----------------|-----------------|
| Core | Quarterly | Quarterly progress reports; ongoing PMO validation |
| Ready | Monthly + Annual | Monthly report package; annual assessment |
| Authorized | Monthly + Annual | Monthly report package; annual assessment |
| Provisionally Authorized | Monthly + Annual | Monthly report package; annual assessment |

---

## Monthly ConMon Activities (Ready and Authorized)

The following deliverables must be submitted monthly to the GovRAMP PMO:

### 1. Vulnerability Scan Results

Per the GovRAMP Vulnerability Scan Requirements Guide:

- **Operating System (OS) scans**: All in-scope servers, VMs, and containers
- **Database scans**: All in-scope database components
- **Web application scans**: All web-facing applications within the boundary
- **Container scans** (if applicable): Container images and runtime environments
- Scans must be authenticated (credentialed) where supported
- Unauthenticated scan results alone are insufficient for compliance
- All critical and high findings must appear in the POA&M with remediation plans

**Scan frequency requirement**: At minimum, scans must be conducted monthly for
Moderate and High impact levels.

### 2. POA&M Update

The Plan of Action and Milestones must be updated every month to reflect:

- All new findings identified since last submission (from scans, audits, or self-discovery)
- Remediation status updates for each open finding
- Milestone date changes (with justification for any slippage)
- Newly closed items (evidence of remediation)
- Deviation Request status (false positives, risk adjustments, operational requirements)

**POA&M Required Fields:**

| Field | Description |
|-------|-------------|
| Finding ID | Unique identifier (e.g., SCAN-001, AUDIT-001) |
| Control ID(s) | NIST 800-53 Rev 5 control(s) affected |
| Weakness Name | Brief, descriptive name |
| Weakness Description | Detailed description of the gap |
| Point of Contact | Owner responsible for remediation |
| Resources Required | Tools, budget, or headcount needed |
| Remediation Plan | Step-by-step plan to address the finding |
| Original Detection Date | When was this first identified |
| Scheduled Completion Date | Target remediation date (must meet SLAs) |
| Milestone Changes | Log of any changes to target dates or scope |
| Status | Open / Closed / Risk Adjusted / Vendor Dependency |
| Risk Rating | Critical / High / Moderate / Low |
| False Positive | Yes / No (if marked Yes, must be substantiated) |

### 3. Asset Inventory Update

- Any new components added to the boundary must be reflected in the inventory
- Any decommissioned components must be removed
- Cloud resource additions (new accounts, new services) must be documented
- The inventory must accurately reflect the current state of the system

### 4. Monthly Summary Report

- A brief executive summary of the month's security activities
- Highlights: new findings, closed findings, ongoing remediation
- Scan coverage confirmation (every in-scope component was scanned)
- Any incidents or security events during the period

---

## Annual ConMon Activities (Ready and Authorized)

### Annual Security Assessment

GovRAMP requires an annual review of security controls:

- Conducted by a GovRAMP-approved 3PAO (for Authorized products) or PMO-directed process
- Results submitted as an updated Security Assessment Report (SAR) or equivalent
- Annual Assessment Controls Selection Worksheet used to determine which controls to test
- All findings from the annual assessment must be added to the POA&M

### Documentation Updates

- **Updated SSP**: Reflect any system changes, boundary modifications, or new controls
- **Updated IRP**: Must be tested (tabletop or functional exercise) with test results documented
- **Updated CP**: Must be tested with test results documented
- **Updated POA&M**: Incorporating annual assessment findings

### Penetration Test

- Required annually (at minimum) per the GovRAMP Penetration Test Guidance
- Must cover all in-scope systems: external, internal, web application, and containers if used
- Penetration test methodology must meet GovRAMP requirements
- Findings from the penetration test must be tracked in the POA&M

---

## Quarterly ConMon Activities (Core)

For products with Core status, ConMon is conducted quarterly:

- Quarterly progress reports submitted to the GovRAMP PMO
- PMO validates ongoing alignment with all 60 Core controls
- PMO and government stakeholders review security performance trends
- Any changes to the system that impact Core control implementation must be reported

---

## GovRAMP Remediation SLAs

All POA&M items must be remediated within the following timeframes, measured from the
**original detection date**:

| Risk Rating | Remediation Deadline |
|-------------|---------------------|
| Critical | 30 calendar days |
| High | 90 calendar days |
| Moderate | 180 calendar days |
| Low | 365 calendar days |

Failure to meet remediation SLAs is one of the most common ConMon findings that
triggers the escalation process.

---

## Deviation Requests

When a finding cannot be remediated within SLA for legitimate operational reasons,
providers may submit a Deviation Request to the GovRAMP PMO:

### Types of Deviations

**1. False Positive**
- Provider demonstrates the finding does not represent a real vulnerability
- Must include technical evidence: screenshot of the scan result, explanation of
  why the finding is incorrect, tool-specific analysis
- Requires PMO approval to remove from open findings

**2. Risk Adjustment**
- Finding is real but provider believes the risk level is overstated
- Provider must provide justification and compensating controls
- Original risk level is preserved in the POA&M; adjusted level is noted
- Requires PMO approval

**3. Operational Requirement**
- Finding cannot be remediated without significant operational impact (e.g., patching a
  legacy component would break critical government customer functionality)
- Provider must document the operational reason and compensating controls
- Requires PMO approval and may require government sponsor acknowledgment

---

## ConMon Escalation Process

The GovRAMP Continuous Monitoring Escalation Process Guide defines how issues are
escalated when a provider fails to meet ConMon obligations:

### Escalation Triggers

- Failure to submit monthly ConMon package on time
- POA&M items exceeding remediation SLAs without an approved deviation
- Critical vulnerabilities not remediated within 30 days
- Discovery of a significant security incident not reported per GovRAMP Incident
  Communications Procedures
- Failure to demonstrate progress in the Progressing Snapshot Program (post-Jan 2026)

### Escalation Steps

1. **Warning Notice**: PMO notifies provider of the specific compliance gap
2. **Correction Period**: Provider has a defined period to remedy the issue
3. **Status Review**: PMO and relevant committees review the provider's status
4. **Status Downgrade or Suspension**: If not resolved, the product's status may be
   downgraded or suspended from the APL
5. **Appeals Committee**: Provider may appeal to the GovRAMP Appeals Committee

---

## Incident Reporting

Per the GovRAMP Incident Communications Procedures:

- Security incidents must be reported to the GovRAMP PMO in a timely manner
- The IRP must contain GovRAMP PMO contact information
- Providers must communicate with relevant government customers and stakeholders
- Reporting timelines and communication templates are defined in the GovRAMP Incident
  Communications Procedures document (available at https://govramp.org/rev-5-templates-and-resources/)

---

## ConMon Portal Access

GovRAMP provides government members with access to a secure ConMon portal for
oversight of authorized products. Government officials can:

- Review current monthly ConMon submissions for authorized providers
- Access historical ConMon records
- Monitor remediation progress
- Receive alerts on significant security events

This allows government organizations to move from a manual assessment role to an
oversight role, reducing the burden of recurring independent reviews for every provider.

---

## ConMon Tips for Service Providers

1. **Automate scans** — Use automated vulnerability scanning tools to ensure monthly scans
   are consistent, complete, and reproducible
2. **Scan all components** — The most common ConMon finding is scan coverage gaps; ensure
   every asset in the system inventory is scanned
3. **Keep the POA&M current weekly** — Waiting until month end creates errors and delays
4. **Track SLAs proactively** — Build alerts in your ticketing system 30 days before any
   POA&M item's scheduled completion date
5. **Document everything** — If a vulnerability cannot be reproduced or is a false positive,
   document the evidence immediately before submitting a deviation request
6. **Communicate proactively** — If a critical finding will miss its SLA, notify the PMO
   before the deadline, not after
7. **Patch third-party dependencies** — Vendor-supplied patches for critical vulnerabilities
   must be applied within 30 days; track vendor patch availability in the POA&M
8. **Test the IRP and CP annually** — Missing test documentation is one of the most
   common annual finding categories

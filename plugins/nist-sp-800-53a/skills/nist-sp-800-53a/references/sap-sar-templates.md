# SAP and SAR Templates — NIST SP 800-53A Rev 5

This reference file contains document templates and field-level guidance for the Security Assessment Plan (SAP) and Security Assessment Report (SAR) as defined in NIST SP 800-53A Rev 5.

Source: NIST SP 800-53A Rev 5, January 2022; NIST RMF Quick Start Guide; OMB guidance

---

## Security Assessment Plan (SAP) Template

---

### [SYSTEM NAME] Security Assessment Plan

**Document Classification**: [e.g., For Official Use Only (FOUO) / Sensitive]
**Version**: 1.0
**Date**: [DATE]
**Prepared By**: [Assessment Organisation or Individual Assessor Name]

---

#### Section 1 — System Identification

| Field | Value |
|-------|-------|
| System Name | |
| System Identifier (FISMA UID or similar) | |
| System Acronym | |
| Agency / Component | |
| Responsible Organisation | |
| System Owner (Name, Title, Phone, Email) | |
| ISSO (Name, Title, Phone, Email) | |
| Authorising Official (Name, Title) | |
| System Security Categorisation | LOW / MODERATE / HIGH (per FIPS 199) |
| Privacy Overlay Required? | YES / NO |
| Assessment Type | Initial / Reauthorisation / Annual Assessment / Significant Change |
| Planned Assessment Start Date | |
| Planned Assessment End Date | |

---

#### Section 2 — Assessment Scope

**2.1 Controls in Scope**

List all security and privacy controls to be assessed. Controls in scope are typically those specified in the approved System Security Plan (SSP).

| Control Family | Control(s) in Scope | Notes |
|---------------|--------------------|----|
| AC — Access Control | AC-1 through AC-25 (as applicable) | |
| AT — Awareness and Training | AT-1 through AT-6 | |
| AU — Audit and Accountability | AU-1 through AU-16 | |
| CA — Assessment, Authorization, Monitoring | CA-1 through CA-9 | |
| CM — Configuration Management | CM-1 through CM-14 | |
| CP — Contingency Planning | CP-1 through CP-13 | |
| IA — Identification and Authentication | IA-1 through IA-13 | |
| IR — Incident Response | IR-1 through IR-10 | |
| MA — Maintenance | MA-1 through MA-6 | |
| MP — Media Protection | MP-1 through MP-8 | |
| PE — Physical and Environmental | PE-1 through PE-23 | |
| PL — Planning | PL-1 through PL-11 | |
| PM — Program Management | PM-1 through PM-33 | |
| PS — Personnel Security | PS-1 through PS-9 | |
| PT — PII Processing and Transparency | PT-1 through PT-8 | |
| RA — Risk Assessment | RA-1 through RA-10 | |
| SA — System and Services Acquisition | SA-1 through SA-23 | |
| SC — System and Communications Protection | SC-1 through SC-51 | |
| SI — System and Information Integrity | SI-1 through SI-23 | |
| SR — Supply Chain Risk Management | SR-1 through SR-12 | |

**2.2 Controls Excluded from This Assessment**

| Control ID | Justification for Exclusion |
|-----------|--------------------------|
| [e.g., PM-3] | [e.g., Assessed at organisational level, not system-level] |

**2.3 System Components in Scope**

| Component | Type | IP / Hostname | Environment |
|-----------|------|--------------|-------------|
| | | | |

**2.4 System Boundary Description**
[Describe the authorisation boundary — what is inside and outside the boundary; reference the SSP boundary diagram]

**2.5 Interconnected Systems**
[List any interconnected systems and whether they are in scope for this assessment; if not in scope, note how trust in the interconnection is established]

---

#### Section 3 — Assessment Team

**3.1 Assessment Team Members**

| Name | Organisation | Role | Qualifications |
|------|-------------|------|--------------|
| | | Assessment Team Lead | |
| | | Security Assessor | |
| | | Technical Assessor | |

**3.2 Organisational Independence Statement**

[State whether the assessment team is organisationally independent from the system owner and ISSO. For HIGH-impact systems, the assessor must have a degree of independence that provides confidence that findings are objective. Describe the nature of any relationship to the system owner.]

Under SP 800-53A Rev 5, for HIGH-impact systems, independent third-party or separate internal team assessors are strongly preferred. For MODERATE-impact systems, semi-independence (different division or chain of command) is acceptable. For LOW-impact systems, the ISSO may assist in assessments but should not self-assess.

**3.3 Conflict of Interest**
[State that the team members have reviewed for conflicts of interest and identified none, or identify any conflicts and mitigations]

---

#### Section 4 — Assessment Approach

**4.1 Assessment Depth and Justification**

Selected depth level: ________________

| Depth Level | Description | Selected? |
|------------|-------------|----------|
| Basic | High-level review; limited testing; appropriate for LOW-impact systems | |
| Focused | Thorough review of key controls; standard testing; appropriate for MODERATE-impact | |
| Comprehensive | Systematic, detailed review and testing of all aspects; HIGH-impact systems | |

Justification: [Explain why this depth level was chosen based on impact level, risk posture, and assessment purpose]

**4.2 Assessment Coverage and Justification**

Selected coverage level: ________________

| Coverage Level | Description | Selected? |
|---------------|-------------|----------|
| Representative | Statistically or informationally representative sample | |
| Focused | Subset selected based on risk | |
| Comprehensive | All instances of each assessment object type | |

Justification: [Explain the coverage choice]

**4.3 Methods to be Used by Control Family**

| Control Family | Examine | Interview | Test |
|---------------|---------|----------|------|
| AC | X | X | X |
| AT | X | X | |
| AU | X | | X |
| CA | X | X | |
| CM | X | X | X |
| CP | X | X | X |
| IA | X | X | X |
| IR | X | X | X |
| MA | X | X | |
| MP | X | X | |
| PE | X | X | X |
| PL | X | X | |
| PM | X | X | |
| PS | X | X | |
| PT | X | X | |
| RA | X | X | |
| SA | X | X | |
| SC | X | | X |
| SI | X | | X |
| SR | X | X | |

---

#### Section 5 — Assessment Schedule and Logistics

**5.1 Schedule**

| Activity | Planned Date | Lead |
|----------|-------------|------|
| SAP finalisation and approval | | |
| Kickoff meeting with system owner and ISSO | | |
| Document collection and review | | |
| Onsite interviews | | |
| Technical testing | | |
| Preliminary findings review with system owner | | |
| SAR draft delivery | | |
| SAR final delivery | | |

**5.2 Required Resources and Access**

| Resource | Purpose | Point of Contact |
|----------|---------|----------------|
| SSP, authorisation package | Document review | ISSO |
| Read-only access to [system/admin console] | Configuration review | System administrator |
| Access to log management system | Audit log review | Security operations |
| Sample list of user accounts (active and recently terminated) | Account management testing | System administrator |
| Vulnerability scan results (last 30 days) | RA-5 assessment | System administrator |
| Firewall rule export | SC-7 assessment | Network administrator |

**5.3 Rules of Engagement**

[IMPORTANT: Define what testing activities are and are not permitted to prevent disruption]

The following rules of engagement govern all testing activities:
1. All active testing (Test method) shall be limited to [non-production / production] environments
2. Account testing shall be performed using designated test accounts only (no real user accounts)
3. Penetration-style testing is [in scope / out of scope] for this assessment
4. The assessment team shall notify [POC name/role] immediately if a critical finding is identified during testing
5. Testing hours: [e.g., normal business hours only / after hours only for system-impacting tests]

---

#### Section 6 — Reporting Requirements

**6.1 Finding Documentation Format**
Findings shall be documented using the SAR template format (see SAR Section 3). Each finding shall include: control ID, assessment objective, determination value, severity, description, evidence, risk determination, and recommendation.

**6.2 Reporting Recipients**

| Recipient | Role | Report Sensitivity |
|----------|------|--------------------|
| | Authorising Official | Unredacted |
| | System Owner | Unredacted |
| | ISSO | Unredacted |
| | CISO / Risk Executive | Summary only |

**6.3 Reporting Timeline**
- Preliminary findings briefing: Within [X] business days of assessment completion
- SAR draft: Within [X] business days of preliminary briefing
- SAR final: Within [X] business days of receiving system owner comments

**6.4 Handling Sensitive Findings**
Critical and High severity findings shall be communicated verbally and via secure channel to the Authorising Official within 24 hours of identification. The SAR itself shall be handled as [FOUO / CONFIDENTIAL].

---

#### Section 7 — Approvals

| Role | Name | Signature | Date |
|------|------|----------|------|
| Assessment Team Lead | | | |
| System Owner | | | |
| ISSO | | | |
| Authorising Official (or AODR) | | | |

---

---

## Security Assessment Report (SAR) Template

---

### [SYSTEM NAME] Security Assessment Report

**Document Classification**: [FOUO / Sensitive]
**Version**: 1.0
**Date**: [DATE]
**Prepared By**: [Assessment Organisation]

---

#### Section 1 — Executive Summary

| Field | Value |
|-------|-------|
| System Name | |
| System Categorisation | LOW / MODERATE / HIGH |
| Assessment Period | [Start Date] to [End Date] |
| Assessment Type | Initial / Reauthorisation / Annual |
| Assessment Team | |
| Number of Controls Assessed | |
| Number of Controls Satisfied | |
| Number of Controls Other Than Satisfied | |
| Number of Controls Not Applicable | |

**Finding Summary by Severity**

| Severity | Count |
|---------|-------|
| Critical | |
| High | |
| Moderate | |
| Low | |
| Informational | |
| **Total** | |

**Overall Posture Statement**
[Provide a narrative statement (3–5 sentences) describing the overall security posture, key risk areas, and recommended course of action for the Authorising Official]

---

#### Section 2 — Assessment Scope and Methodology

**2.1 Scope**
[Confirm what was and was not assessed, by reference to the SAP; note any scope changes during the assessment]

**2.2 Depth and Coverage**
Assessment conducted at **[depth level]** depth and **[coverage level]** coverage.

**2.3 Assessment Limitations and Constraints**
[Document any limitations that affected the assessment, e.g., access denied to certain logs, system unavailability, time constraints, inability to perform certain tests]

| Limitation | Impact on Assessment | Affected Controls |
|-----------|---------------------|-------------------|
| | | |

---

#### Section 3 — Assessment Findings

For each control assessed, document the finding using the format below. Controls assessed as "Satisfied" require minimal documentation. Controls assessed as "Other Than Satisfied" require full finding documentation.

---

**Control Finding Template**

```
Control ID:            [e.g., AC-2]
Control Name:          [e.g., Account Management]
SP 800-53 Rev 5 Baseline: LOW / MODERATE / HIGH / Privacy
Privacy Control:       YES / NO

Assessment Objective  [a]:  [Description of objective]
  Determination:       Satisfied / Other Than Satisfied / Not Applicable
  Evidence:            [Brief description of evidence reviewed/tested]

Assessment Objective  [b]:  [Description of objective]
  Determination:       Satisfied / Other Than Satisfied / Not Applicable
  Evidence:            [Brief description of evidence reviewed/tested]

[... repeat for each objective ...]

Overall Control Determination: Satisfied / Other Than Satisfied / Not Applicable

FINDING (complete only if Other Than Satisfied):
  Finding ID:          [SAR-YYYY-NNN]
  Severity:            Critical / High / Moderate / Low / Informational
  Description:         [Clear, factual description of what is missing, insufficent,
                        or not operating as intended. State what was observed and how
                        it deviates from the SP 800-53 Rev 5 requirement.]
  Evidence Summary:    [Documents reviewed, individuals interviewed, tests conducted
                        and their results that support this determination]
  Risk Determination:  [Using SP 800-30 risk scale: Very High / High / Moderate /
                        Low / Very Low — state the overall risk this finding poses,
                        referencing likelihood and impact]
  Recommendation:      [Specific, actionable remediation recommendation]
```

---

**Assessment Findings Log — Summary Table**

| Finding ID | Control | Control Name | Severity | Determination | Recommendation Summary |
|-----------|---------|-------------|---------|--------------|----------------------|
| SAR-[Y]-001 | | | Critical | OTS | |
| SAR-[Y]-002 | | | High | OTS | |
| SAR-[Y]-003 | | | Moderate | OTS | |

---

#### Section 4 — Risk Summary

List all Other Than Satisfied findings rated High or Critical, with associated risk determinations. This section informs the Authorising Official's risk acceptance decision.

| Finding ID | Control | Severity | Risk Level | Risk Description | Recommendation |
|-----------|---------|---------|-----------|-----------------|---------------|
| | | Critical | Very High | | |
| | | High | High | | |

---

#### Section 5 — Assessor Attestation

The undersigned assessment team members attest that this SAR accurately represents the results of the assessment conducted of [SYSTEM NAME]. The assessment was conducted in accordance with NIST SP 800-53A Rev 5, at [DEPTH] depth and [COVERAGE] coverage. Assessment team members have no undisclosed conflicts of interest with the system owner or the information system assessed.

| Role | Name | Signature | Date |
|------|------|----------|------|
| Assessment Team Lead | | | |
| Security Assessor | | | |
| Technical Assessor | | | |

---

## SAP-to-SAR Consistency Checklist

Before finalising a SAR, verify the following against the SAP:

| Check | Status |
|-------|--------|
| All controls in SAP scope are in the SAR | |
| Depth and coverage levels match SAP | |
| Team composition matches SAP | |
| All SAP-listed assessment objects were reviewed | |
| Any deviations from the SAP are documented in SAR Section 2.3 | |
| Every OTS finding has: Finding ID, Severity, Description, Evidence, Risk, Recommendation | |
| Severity assignments follow the 5-level scale | |
| POA&M action items align with OTS findings | |

---

## POA&M Linkage

Every "Other Than Satisfied" finding in the SAR must generate a POA&M entry. The SAR Finding ID becomes the POA&M Item ID. Required POA&M fields per OMB M-02-01 and NIST SP 800-37:

| POA&M Field | Source |
|------------|--------|
| POA&M Item ID | SAR Finding ID |
| System Name and ID | From SAR header |
| Control Number | From SAR finding |
| Finding Description | SAR finding description |
| Weakness/Deficiency | SAR evidence summary |
| Risk Level | SAR risk determination |
| Resources Required | Assessor's recommendation, system owner estimate |
| Scheduled Completion Date | System owner determination |
| Milestones | System owner creates milestone schedule |
| Responsible Point of Contact | Assigned by system owner |
| Status | Open (until remediated and verified) |

# SOC 1 — SSAE 18 AT-C Section 320 Reference

## Overview

SOC 1 (Service Organization Controls 1) reports are attestation engagements performed under
**SSAE 18, AT-C Section 320** (*Reporting on an Examination of Controls at a Service Organization
Relevant to User Entities' Internal Control Over Financial Reporting*), issued by the American
Institute of Certified Public Accountants (AICPA), effective **May 1, 2017**.

SOC 1 reports replaced reports issued under:
- **SSAE 16** (AT 801) — effective June 1, 2011 to April 30, 2017
- **SAS 70** (*Reports on the Processing of Transactions by Service Organizations*) — superseded 2011

---

## Applicable Standards

| Section | Title | Purpose |
|---|---|---|
| AT-C Section 105 | Concepts Common to All Attestation Engagements | Overarching attestation concepts; independence, professional judgment |
| AT-C Section 205 | Examination Engagements | General examination standards applicable to all examinations |
| AT-C Section 320 | Reporting on Controls at a Service Organization Relevant to User Entities' ICFR | Specific requirements for SOC 1 reports |

---

## Roles and Definitions

| Role | Definition |
|---|---|
| Service organization | An entity that provides services to user entities that are likely to be relevant to those user entities' ICFR |
| User entity | An entity that uses a service organization and for which the service organization's controls may be relevant to the user entity's ICFR |
| Service auditor | The CPA firm engaged to perform the SOC 1 examination |
| User auditor | The CPA firm auditing a user entity's financial statements |
| Subservice organization | A service organization used by the reporting service organization to perform part of the services provided to user entities |

---

## Report Types

### Type 1 — Design as of a Specific Date

A Type 1 report addresses two things as of a specific date:
1. Whether management's description of the service organization's system is **fairly presented**.
2. Whether the controls are **suitably designed** to provide reasonable assurance that the specified control objectives would be achieved if the controls operated as described.

A Type 1 report does **not** address operating effectiveness. It cannot be used to satisfy user auditor requirements for reliance on service organization controls.

### Type 2 — Design and Operating Effectiveness Over a Period

A Type 2 report addresses three things over a specified period:
1. Whether management's description is **fairly presented**.
2. Whether the controls are **suitably designed** to achieve the control objectives.
3. Whether the controls **operated effectively** throughout the specified period.

**Minimum period:** There is no hard minimum in the standard; however, the AICPA guidance
and common practice establish that a period of less than six months may not provide sufficient
evidence of consistent operation. A 12-month period is the most common.

---

## System Description Requirements (AT-C §320.25–.27)

The service organization's management is responsible for preparing the system description.
It must address:

### 1. Services Provided
- The nature of the services provided to user entities.
- Principal service commitments (e.g., processing accuracy, timeliness, confidentiality).
- System requirements arising from contracts, regulations, and service-level agreements.

### 2. System Components (Five-Part Model)

| Component | Contents |
|---|---|
| Infrastructure | Physical and hardware components: servers, network equipment, storage, data centers, facilities |
| Software | System software (OS, middleware), application programs, databases, reporting tools |
| People | Personnel involved in service delivery: operators, administrators, developers, management |
| Processes | Automated and manual procedures that are part of service delivery |
| Data | Transactions, master files, tables, databases, input data, output reports |

### 3. System Boundaries
- What is within the service organization's control vs. what is within the control of user entities or subservice organizations.
- Physical and logical boundaries (network diagrams, data flow diagrams may support this).

### 4. Control Environment and Key Control Areas
The description must cover:
- Control environment (tone at the top, entity-level controls, COSO framework components as applicable)
- Risk assessment processes
- Information and communication
- Monitoring activities
- Control activities (mapped to each control objective)

### 5. Complementary User Entity Controls (CUECs)
Controls that user entities are assumed to have in place for the control objectives to be met.
These must be explicitly listed. Examples:
- User entities are responsible for the accuracy of input data submitted to the service organization.
- User entities are responsible for reviewing exception reports provided by the service organization.
- User entities are responsible for managing their own logical access to the service organization's portal.

### 6. Subservice Organization Controls
- **Carve-out method:** Describe the functions performed by the subservice organization and state that controls at the subservice organization are excluded from the description.
- **Inclusive method:** Include the subservice organization's system description and controls; subservice organization provides its own assertion.

### 7. Changes During the Period (Type 2 Only)
Any significant changes to the system or controls during the period must be described.
Changes must be documented with effective dates.

---

## Control Objectives

Control objectives are **not prescribed by AT-C Section 320**. The service organization defines
them based on the nature of its services and the commitments made to user entities.

### Guidance for Drafting Control Objectives

A control objective should:
- Start with a statement of what is to be achieved (not how).
- Be specific enough that it can be evaluated — either met or not met.
- Align with user entity ICFR needs.
- Be testable by the service auditor.

**Format:** "Controls provide reasonable assurance that [what is to be achieved]."

### Common Control Objective Areas

| Area | Example Control Objective |
|---|---|
| Transaction processing | Controls provide reasonable assurance that transactions are processed accurately, completely, and only with proper authorization. |
| Logical access | Controls provide reasonable assurance that logical access to production systems and data is restricted to authorized users. |
| Physical access | Controls provide reasonable assurance that physical access to data centers and server rooms is restricted to authorized personnel. |
| Change management | Controls provide reasonable assurance that changes to production systems are authorized, tested, and documented prior to implementation. |
| Computer operations | Controls provide reasonable assurance that batch jobs are processed as scheduled and exceptions are monitored and resolved. |
| Data backup and recovery | Controls provide reasonable assurance that data is backed up regularly and can be recovered in the event of an incident. |
| Network security | Controls provide reasonable assurance that network security events are monitored and unauthorized access attempts are identified and addressed. |
| Incident management | Controls provide reasonable assurance that incidents affecting service delivery are identified, escalated, and resolved in accordance with defined procedures. |
| Subservice organization monitoring | Controls provide reasonable assurance that services provided by subservice organizations are monitored for compliance with performance commitments. |
| New user provisioning | Controls provide reasonable assurance that user access is provisioned based on authorized requests and that access is commensurate with job responsibilities. |
| User access deprovisioning | Controls provide reasonable assurance that access is removed upon user termination or role change. |
| Patch management | Controls provide reasonable assurance that security patches are evaluated and applied within a defined timeframe. |

---

## System Description Checklist

Use this checklist to evaluate completeness of a SOC 1 system description:

- [ ] Nature of services provided is clearly described
- [ ] Principal service commitments are stated
- [ ] All five system components (infrastructure, software, people, processes, data) are addressed
- [ ] System boundaries are defined (what is in scope, what is carved out)
- [ ] The five COSO components are addressed (control environment, risk assessment, information/communication, monitoring, control activities)
- [ ] CUECs are listed explicitly
- [ ] Subservice organizations are identified; carve-out or inclusive method stated
- [ ] For Type 2: changes to the system during the period are documented
- [ ] Control objectives are clearly stated
- [ ] Controls are mapped to each control objective

---

## Management's Assertion

Management of the service organization must provide an assertion that:

For **Type 1:**
1. The description fairly presents the service organization's system as of the specified date.
2. The controls included in the description are suitably designed to provide reasonable assurance that the specified control objectives would be achieved if the controls operated as described.

For **Type 2:**
1. The description fairly presents the service organization's system throughout the specified period.
2. The controls are suitably designed.
3. The controls operated effectively throughout the period to provide reasonable assurance that the control objectives were achieved.

---

## Service Auditor Opinion Types

| Opinion Type | When Used |
|---|---|
| Unmodified | Description is fairly presented; controls are suitably designed; (Type 2) controls operated effectively |
| Qualified | One or more items are materially misstated or one or more control objectives were not met, but the exception is not pervasive |
| Adverse | Exceptions are pervasive; the description is not fairly presented or controls are not suitably designed/effective |
| Disclaimer | Service auditor is unable to obtain sufficient evidence to form an opinion |

**Modified opinions must include:** A basis for the modification paragraph that clearly describes the matter giving rise to the modification and the effect on the opinion.

---

## Testing for Type 2 — Operating Effectiveness

The service auditor must test whether controls operated effectively throughout the entire period.

### Testing Methods

| Method | Description | Typical Use |
|---|---|---|
| Inquiry | Asking personnel about procedures | Preliminary understanding; corroborated by other methods |
| Observation | Watching a control being performed | Controls with no documentary evidence |
| Inspection | Reviewing documents, reports, or logs | High-frequency controls; access logs; change records |
| Re-performance | Service auditor re-performs the control | High-risk controls; automated controls |
| Analytical procedures | Evaluating data for plausible relationships | High-volume transaction controls |

### Sampling Guidance

The AICPA SOC 1 guide provides the following general sampling expectations for Type 2 testing.
These are not mandatory minimums but reflect common practice:

| Control frequency | Typical sample size |
|---|---|
| Annual (performed once per year) | 1 (entire population) |
| Quarterly | 2–4 |
| Monthly | 3–6 |
| Weekly | 5–15 |
| Daily | 15–30 |
| Multiple times per day / continuous | 25–45 |
| Event-driven / per-transaction | 25–60 depending on volume |

---

## Common SOC 1 Findings and Deficiencies

| Finding Type | Description | Typical Cause |
|---|---|---|
| **Control not in place** | No evidence a control was performed | Control designed but never implemented; procedure not followed |
| **Deviation** | Control operated but one or more exceptions noted during the period | Inconsistent application; staff turnaround; system defect |
| **Description gap** | A process in scope is not described in the system description | Incomplete scoping; processes added during period not updated in description |
| **CUEC overreliance** | A control objective can only be achieved with user entity controls, but CUECs are not listed | Insufficient scoping; service org attempting to shift responsibility without disclosure |
| **Stale CUEC list** | CUECs listed do not reflect actual current user entity responsibilities | Not reviewed annually |
| **Undisclosed change** | System or control changed during the period; not reflected in description | Change management process does not include description update step |
| **Subservice org gap** | Functions performed by a subservice organization not identified | New vendor engagement not captured; carve-out scope not updated |
| **Access review not performed** | User access review not conducted per stated control | Manual control with no enforcement mechanism; ownership unclear |

---

## Reading and Using a SOC 1 Report (User Auditor Perspective)

When a user auditor receives a SOC 1 Type 2 report from their client's service organization,
they must:

1. **Evaluate relevance** — Confirm the report covers the period that includes the user entity's financial period.
2. **Assess scope coverage** — Confirm the service organization's system description covers the relevant transactions processed on behalf of the user entity.
3. **Evaluate CUECs** — Determine whether the user entity has the complementary controls in place. If CUECs are not implemented, the service auditor's opinion provides no assurance.
4. **Review the opinion** — A qualified or adverse opinion means the user auditor cannot rely on the service org's controls.
5. **Follow up on deviations** — If the Type 2 report notes deviations (exceptions in control testing), the user auditor must assess whether those deviations could affect the financial statements of the user entity.
6. **Assess subservice organizations** — If carve-out method is used, evaluate whether a separate SOC 1 report for the subservice organization is needed.

---

## SOC 1 Readiness Checklist

Use this checklist to evaluate SOC 1 readiness before engaging a service auditor:

**Scoping and Documentation**
- [ ] Services have been clearly defined and mapped to user entity ICFR
- [ ] System components documented (infrastructure, software, people, processes, data)
- [ ] System boundaries defined in writing
- [ ] Control objectives drafted and reviewed with service auditor
- [ ] CUECs listed with user entity in mind

**Controls**
- [ ] For each control objective, at least one control is designed and implemented
- [ ] Controls are documented with owner, frequency, and evidence
- [ ] Control execution is consistent (no gaps in performance)
- [ ] Evidence of control operation is retained (logs, approvals, screenshots, sign-offs)

**Access Management**
- [ ] Access provisioning and deprovisioning procedures documented
- [ ] Access reviews performed on the defined cycle
- [ ] Privileged access managed separately with additional controls

**Change Management**
- [ ] Change request process documented with approval workflow
- [ ] Emergency change procedures exist
- [ ] Deployment logs maintained

**Monitoring**
- [ ] Logs reviewed on defined schedule
- [ ] Incident response procedures documented and tested
- [ ] Subservice organizations monitored per stated controls

**Subservice Organizations**
- [ ] All subservice organizations identified
- [ ] Carve-out or inclusive method decision documented
- [ ] If carve-out: monitoring controls over subservice organizations implemented

---

## Frequently Asked Questions

**Q: Can a service organization issue a SOC 1 report for itself?**  
No. AT-C Section 320 requires the examination to be performed by an independent CPA firm
(the service auditor). Management's assertion is part of the report, but the examination and
opinion must come from an independent practitioner.

**Q: How long should the review period be for a Type 2?**  
The AICPA does not specify a mandatory minimum period, but the AICPA SOC 1 guide notes that
a period of less than six months may not provide sufficient evidence. The most common period
is 12 months, aligned with the user entity's fiscal year.

**Q: What is the difference between SOC 1 and SOC 2?**  
SOC 1 focuses on controls relevant to user entities' ICFR. SOC 2 focuses on the AICPA Trust
Services Criteria (Security, Availability, Confidentiality, Processing Integrity, Privacy),
which are not limited to financial reporting. SOC 2 is used when customers need assurance
about the security and reliability of a service organization's systems.

**Q: Does a SOC 1 cover cybersecurity?**  
Only to the extent that cybersecurity controls are within the stated control objectives. A
SOC 1 report for a payroll processor might include logical access controls (which relate to
system security), but cybersecurity program maturity is not the primary focus. SOC 2 or SOC
for Cybersecurity is more appropriate for comprehensive security assurance.

**Q: Can a SOC 1 report be shared publicly?**  
No. SOC 1 reports are restricted-use documents. They may only be provided to the service
organization's management, the user entities that used the service during the period, and
their auditors. They should not be posted publicly or shared with prospective customers.

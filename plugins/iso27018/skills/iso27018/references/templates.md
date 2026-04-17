# ISO/IEC 27018 — Document Templates

## Template Index

| Template | Purpose |
|----------|---------|
| [T1: PII Protection Policy](#t1-pii-protection-policy) | Internal policy governing CSP's obligations for customer PII |
| [T2: DPA Addendum — ISO 27018 Obligations](#t2-data-processing-agreement-addendum) | Contract clauses for cloud service agreements with customers |
| [T3: Sub-processor Agreement Schedule](#t3-sub-processor-agreement-schedule) | Contract terms binding sub-processors to equivalent obligations |
| [T4: Government Request Handling Procedure](#t4-government-request-handling-procedure) | Internal procedure for receiving and responding to legal disclosure requests |
| [T5: PII Return and Disposal Confirmation Letter](#t5-pii-return-and-disposal-confirmation-letter) | Written confirmation to customers at contract end |
| [T6: Sub-processor Register](#t6-sub-processor-register) | Operational register of approved sub-processors |
| [T7: Disclosure Register](#t7-disclosure-register) | Record of legally required disclosures of PII to third parties |
| [T8: Staff PII Awareness Training Acknowledgment](#t8-staff-pii-awareness-training-acknowledgment) | Acknowledgment form for staff completing PII training |
| [T9: PII Incident Notification to Customer](#t9-pii-incident-notification-to-customer) | Template for notifying customers of PII-related security incidents |
| [T10: ISO 27018 Gap Analysis Template](#t10-iso-27018-gap-analysis-template) | Self-assessment gap analysis table |

---

## Important Notice on Template Use

These templates are frameworks based on ISO/IEC 27018 and common industry practice. They are provided for informational and guidance purposes only. They should be reviewed and adapted by qualified legal and compliance professionals before formal use, as applicable laws vary by jurisdiction.

---

## T1: PII Protection Policy

```
[ORGANISATION NAME]
PII Protection Policy — Public Cloud Services

Document Control
Version:          [VERSION]
Author:           [AUTHOR NAME / ROLE]
Approved by:      [SENIOR EXECUTIVE / DATA PROTECTION OFFICER]
Date approved:    [DATE]
Next review:      [DATE — typically 12 months from approval]
Classification:   Internal

1. Purpose
This policy establishes [ORGANISATION NAME]'s obligations and controls as a
public cloud PII processor, in accordance with ISO/IEC 27018. It governs how
[ORGANISATION NAME] handles personally identifiable information (PII) entrusted
to it by cloud service customers.

The policy supplements [ORGANISATION NAME]'s Information Security Policy and
applies in addition to any applicable data protection legislation.

2. Scope
This policy applies to:
- All employees, contractors, and third parties who access or process customer PII
  in the course of delivering [ORGANISATION NAME]'s cloud services
- All systems, infrastructure, and services that store, process, or transmit
  customer PII
- All sub-processors engaged by [ORGANISATION NAME] to process customer PII

3. Roles and Responsibilities

Role                           | Responsibility
-------------------------------|------------------------------------------
Data Protection Contact / DPO  | Policy owner; regulatory liaison; customer queries
CISO / Security Lead           | Technical control oversight; incident response
Engineering / Operations       | Implementation of technical controls
Procurement                    | Sub-processor due diligence and contracts
All Staff with PII Access      | Compliance with this policy

4. Core Obligations

4.1 Purpose Limitation
[ORGANISATION NAME] processes customer PII solely for the purposes specified in
the applicable service agreement and customer instructions. [ORGANISATION NAME]
shall not process customer PII for its own commercial, marketing, advertising,
or analytical purposes without the express, separate written consent of the
cloud service customer.

4.2 No Unauthorised Disclosure
[ORGANISATION NAME] shall not disclose customer PII to any third party, except:
(a) As instructed in writing by the cloud service customer
(b) As required by binding law or regulation, in which case [ORGANISATION NAME]
    will notify the customer unless legally prohibited from doing so
(c) To sub-processors, subject to paragraph 4.4

4.3 Government and Law Enforcement Requests
Where [ORGANISATION NAME] is legally required to disclose customer PII to a
government authority, law enforcement agency, or court, it shall:
(a) Notify the affected customer promptly, unless legally prohibited
(b) Disclose only the minimum PII necessary to satisfy the legal obligation
(c) Log the disclosure in the Disclosure Register
(d) Challenge any request that is overbroad or lacks proper legal authority

4.4 Sub-processors
[ORGANISATION NAME] shall only engage sub-processors that have been approved
through its sub-processor management process and that are contractually bound
to equivalent PII protection obligations. [ORGANISATION NAME] shall maintain a
current Sub-processor Register, notify customers of any changes to sub-processors
with [ADVANCE NOTICE PERIOD, e.g. 30 days'] notice, and remain liable for
sub-processor compliance.

4.5 PII Return and Disposal
Upon termination of a service agreement, [ORGANISATION NAME] shall, within
[AGREED PERIOD — e.g. 30 days] of the termination date, either return all
customer PII to the customer or securely delete it, including all copies held by
sub-processors, unless retention is required by applicable law. Written
confirmation of return/deletion shall be provided to the customer.

4.6 Employee Obligations
All employees and contractors with access to customer PII must:
(a) Complete mandatory PII awareness training before access is provisioned
(b) Access customer PII only to the extent necessary for their role
(c) Comply with [ORGANISATION NAME]'s confidentiality obligations
(d) Report any suspected PII security incident immediately to
    [INCIDENT REPORTING CONTACT]

5. Data Residency
[ORGANISATION NAME] processes customer PII only in the following regions:
[LIST REGIONS / COUNTRIES]

Any change to processing regions will be notified to affected customers with
[ADVANCE NOTICE PERIOD] days' prior notice.

6. Compliance and Audit
[ORGANISATION NAME] will conduct an annual internal review of its compliance
with this policy and will provide cloud service customers with evidence of
compliance on request, in the form of:
- Current third-party security certifications
- Independent audit reports (under appropriate confidentiality terms)
- Completion of security questionnaires

7. Review Cycle
This policy shall be reviewed at least annually and following any significant
change to [ORGANISATION NAME]'s PII processing activities, applicable legal
requirements, or findings from audits or incidents.
```

---

## T2: Data Processing Agreement Addendum

```
DATA PROCESSING ADDENDUM — ISO/IEC 27018

This Data Processing Addendum ("Addendum") supplements the [MASTER SERVICE
AGREEMENT / TERMS OF SERVICE] between [CLOUD SERVICE PROVIDER] ("CSP") and
[CUSTOMER NAME] ("Customer"), effective [DATE].

1. Definitions
"PII" means personally identifiable information as defined in ISO/IEC 27018,
including personal data or personal information as defined in applicable
data protection law.

"Customer PII" means PII that Customer uploads, submits, or causes to be
processed through the Service.

"Processing" means any operation on PII as described in ISO/IEC 27018.

"Sub-processor" means a third party engaged by CSP to process Customer PII.

2. CSP's Role
CSP is a PII processor in respect of Customer PII. CSP processes Customer PII
solely on Customer's instructions, as set out in this Addendum and the Service
Agreement.

3. Restrictions on CSP's Use of Customer PII
3.1  CSP shall not process Customer PII for its own commercial, marketing,
     advertising, or analytical purposes.

3.2  CSP shall not disclose Customer PII to third parties except:
     (a) As instructed in writing by Customer;
     (b) As required by binding law, in which case CSP will comply with
         Section 7 of this Addendum;
     (c) To Sub-processors in accordance with Section 5.

4. Security Measures
CSP shall implement and maintain technical and organisational security measures
appropriate to the risks presented by the processing, including as a minimum:
(a) Encryption of Customer PII at rest and in transit
(b) Access controls limiting employee access to Customer PII to the minimum
    necessary
(c) Multi-factor authentication for all privileged access to systems containing
    Customer PII
(d) Audit logging of access to Customer PII
(e) Documented incident response procedures including breach notification

5. Sub-processors
5.1  CSP shall not engage Sub-processors for the processing of Customer PII
     without Customer's prior knowledge.

5.2  CSP shall notify Customer of any proposed addition or replacement of a
     Sub-processor with [30] days' prior notice.

5.3  Customer may object to a new Sub-processor on reasonable data protection
     grounds within [15] days of notification.

5.4  CSP shall contract with each Sub-processor on terms that impose equivalent
     PII protection obligations to those in this Addendum.

5.5  CSP shall remain liable to Customer for Sub-processor compliance with
     this Addendum.

5.6  The current Sub-processor list is maintained at [URL / schedule attached].

6. PII Principals' Rights
CSP shall provide Customer, upon written request and within a reasonable
timeframe, with technical assistance to enable Customer to respond to requests
from PII principals (data subjects) exercising their rights, including access,
rectification, erasure, restriction, portability, and objection.

7. Government and Law Enforcement Requests
7.1  If CSP receives a legally binding request from a government authority or
     law enforcement agency to disclose Customer PII, CSP shall:
     (a) Promptly notify Customer of the request, unless legally prohibited;
     (b) Disclose only the minimum PII required by the request;
     (c) Challenge any request that is overbroad or lacks proper authority.

7.2  CSP shall maintain a record of all legally required PII disclosures and
     shall provide Customer with a summary of such disclosures on request
     (subject to any applicable legal restrictions).

8. Data Residency
CSP processes Customer PII only in the following regions: [LIST REGIONS].
Any change will be notified to Customer with [30] days' prior notice.

9. PII Return and Deletion
9.1  Upon termination of the Service Agreement, CSP shall, within [30] days,
     either return all Customer PII to Customer or securely delete it, unless
     legally required to retain it.

9.2  CSP shall provide written confirmation of return or deletion upon request.

10. Audit Rights
10.1 CSP shall make available to Customer the information necessary to
     demonstrate compliance with this Addendum, including:
     (a) Third-party security certifications (ISO 27001, SOC 2)
     (b) Independent security audit reports (under NDA)
     (c) Responses to security questionnaires

10.2 Customer may, with [30] days' prior written notice, conduct or commission
     an audit of CSP's compliance with this Addendum, subject to CSP's
     reasonable security requirements and a suitable confidentiality arrangement.

11. Incident Notification
CSP shall notify Customer without undue delay (and within [72 hours]) upon
becoming aware of a security incident that results or may result in accidental
or unlawful destruction, loss, alteration, unauthorised disclosure of, or
access to, Customer PII. Such notification shall include the information
required by applicable law and, where known: the nature of the incident,
the affected PII categories and approximate volume, and the measures taken
or proposed.

12. Governing Data Protection Law
This Addendum is governed by [APPLICABLE LAW / JURISDICTION].
```

---

## T3: Sub-processor Agreement Schedule

```
SUB-PROCESSOR DATA PROCESSING SCHEDULE

This Schedule is incorporated into and forms part of the [MASTER AGREEMENT]
between [CSP] ("Controller-Processor") and [SUB-PROCESSOR NAME] ("Sub-processor"),
effective [DATE].

1. Scope of Processing
Sub-processor may process PII only for the following purposes: [DESCRIBE PURPOSE]
Processing of PII for any other purpose is expressly prohibited without prior
written consent from Controller-Processor.

2. Restrictions
2.1  Sub-processor shall not use PII for its own commercial, marketing, or
     analytical purposes.

2.2  Sub-processor shall not engage further sub-processors without prior
     written approval from Controller-Processor.

3. Security Requirements
Sub-processor shall implement security measures at least equivalent to those
required of Controller-Processor under its customer data processing agreements,
including:
(a) Encryption at rest and in transit
(b) Access controls and least-privilege
(c) Audit logging of access to PII
(d) Multi-factor authentication for privileged access

4. Incident Notification
Sub-processor shall notify Controller-Processor within 24 hours of becoming
aware of any actual or suspected breach of security involving PII.

5. Data Residency
Sub-processor shall process PII only in the following regions: [LIST REGIONS].

6. Return and Deletion
Upon termination, Sub-processor shall return or delete all PII within [15]
days and provide written confirmation.

7. Audit Rights
Controller-Processor shall have the right to audit Sub-processor's PII
handling on [30] days' notice, or to receive third-party audit reports.

8. Survival
Obligations under this Schedule survive termination of the Master Agreement.
```

---

## T4: Government Request Handling Procedure

```
[ORGANISATION NAME]
Government and Law Enforcement PII Request Handling Procedure

Version:         [VERSION]
Author:          [AUTHOR]
Approved by:     [DPO / GENERAL COUNSEL]
Date:            [DATE]
Next review:     [DATE]

1. Purpose
This procedure governs how [ORGANISATION NAME] responds to legally binding
requests from government authorities, law enforcement agencies, courts, and
regulators to disclose customer PII.

2. Scope
Applies to: Legal, Privacy, Security, and Customer Success teams.

3. Step-by-Step Procedure

Step 1 — Receipt and Logging
- Log receipt in the Government Request Register immediately
- Record: date received, requesting authority, nature of request, data
  categories requested, stated legal authority, deadline

Step 2 — Legal Review
- Route to General Counsel / Legal immediately
- Assess: Is the request legally valid? Is it from a competent authority?
  Is the stated legal basis correct? Is the scope proportionate?

Step 3 — Notify Customer
- Unless legally prohibited, notify the affected customer within 24–48 hours
- Notification: name of requesting authority, nature of request,
  categories of data requested (not the data itself)
- If a legal prohibition prevents notification, document the prohibition
  in the Government Request Register

Step 4 — Challenge if Appropriate
- If the request is overbroad, lacks proper authority, or conflicts with
  applicable law, [ORGANISATION NAME] will challenge the request
- Legal to advise on challenge procedure per applicable jurisdiction

Step 5 — Disclosure (if required)
- Disclose only the minimum PII required to satisfy the legal obligation
- Obtain confirmation of the legal basis in writing from requesting authority
- Record the disclosure in the Government Request Register and Disclosure Register

Step 6 — Post-Disclosure
- Provide customer record of the disclosure when legally permitted
- Include disclosure in next Transparency Report (aggregate form)

4. Transparency Reporting
[ORGANISATION NAME] publishes an annual Transparency Report summarising:
- Total number of government/law enforcement requests received
- Jurisdictions of requesting authorities
- Number fulfilled in full, in part, or rejected
- Number of notifications prohibited by law
```

---

## T5: PII Return and Disposal Confirmation Letter

```
[ORGANISATION NAME LETTERHEAD]

Date:            [DATE]
To:              [CUSTOMER CONTACT NAME]
Organisation:    [CUSTOMER NAME]
Re:              Confirmation of PII Return/Deletion — [SERVICE NAME]
Contract:        [CONTRACT REFERENCE]

Dear [CONTACT NAME],

Following the termination of the above-referenced service agreement on
[TERMINATION DATE], we write to confirm that all Customer PII processed
by [ORGANISATION NAME] under that agreement has been handled as follows:

[SELECT APPLICABLE:]

[ ] Returned to Customer: All Customer PII was exported and transferred to
    [METHOD/DESTINATION] on [DATE]. Copies have been deleted from our systems.

[ ] Deleted/Destroyed: All Customer PII has been securely deleted from
    [ORGANISATION NAME]'s systems and from all sub-processors' systems, as of
    [COMPLETION DATE].

The above includes all primary data, backups, caches, replicas, and any copies
held by sub-processors.

[IF ANY RETENTION REQUIRED:]
The following data has been retained solely as required by [LAW/REGULATION]:
[DESCRIBE CATEGORY AND RETENTION PERIOD]

This confirmation is provided in accordance with [ORGANISATION NAME]'s
obligations under our Data Processing Addendum and ISO/IEC 27018.

Please retain this letter as part of your compliance records.

Yours sincerely,

[SIGNATORY NAME]
[TITLE]
[DATE]
[CONTACT EMAIL]
```

---

## T6: Sub-processor Register

| Field | Description / Example |
|-------|----------------------|
| Sub-processor Name | Cloud Storage Corp Ltd |
| Registered Country | United States |
| Processing Location(s) | US East, EU West |
| Purpose | Object storage for customer data |
| PII Categories Processed | Documents, user data, email addresses |
| Transfer Mechanism (if outside EEA) | Standard Contractual Clauses (SCCs) |
| Certification | ISO 27001, SOC 2 Type II |
| CSP Contract Reference | SUBP-2024-00123 |
| Date Customers Notified | 2024-03-01 |
| Last Due Diligence Review | 2025-01-15 |
| Next Review Due | 2026-01-15 |

*Maintained by: [Procurement / Privacy Team]*
*Updated: [DATE]*
*Approved by: [DPO / Privacy Lead]*

---

## T7: Disclosure Register

| Field | Description / Example |
|-------|----------------------|
| Reference ID | DISC-2025-001 |
| Date of Request | 2025-02-14 |
| Date of Disclosure | 2025-02-18 |
| Requesting Authority | [e.g. Jurisdiction Court / Authority] |
| Requesting Jurisdiction | [Country] |
| Legal Basis Cited | [Court order / statutory authority] |
| PII Categories Disclosed | [e.g. Name, email, account records] |
| Approximate Volume | [Number of records / individuals] |
| Customer Notified? | Yes / No |
| If No — Reason | [Legal prohibition / order prohibiting notification] |
| Challenge Made? | Yes / No |
| Challenge Outcome | [Withdrawn / Modified / Upheld] |
| Record Owner | [Name] |

*Classified: Restricted — Legal Privilege may apply*
*Maintained by: Legal / Privacy Team*

---

## T8: Staff PII Awareness Training Acknowledgment

```
[ORGANISATION NAME]
PII Awareness Training — Completion and Acknowledgment

Employee/Contractor Name:   ____________________________
Role/Department:            ____________________________
Training Completed:         ____________________________  (Date)
Training Delivered By:      ____________________________

I confirm that I have completed the PII Awareness Training for [ORGANISATION NAME]
and that I understand and agree to the following:

1. I understand what constitutes personally identifiable information (PII) in
   the context of [ORGANISATION NAME]'s cloud services.

2. I understand that [ORGANISATION NAME] acts as a PII processor for its cloud
   service customers and that I must only process customer PII as required by
   my role and in line with company policy.

3. I understand that I must not use customer PII for any purpose other than
   delivering the contracted service, including not using it for personal
   purposes, marketing, or any purpose not authorised by [ORGANISATION NAME].

4. I understand my confidentiality obligations regarding customer PII and that
   these obligations continue after I leave [ORGANISATION NAME]'s employment.

5. I know how to recognise and report a PII-related security incident and will
   report such incidents immediately to [REPORTING CONTACT/CHANNEL].

6. I understand the consequences of breaching these obligations, including
   disciplinary action up to and including dismissal, and potential civil or
   criminal liability.

Signature:   _________________________   Date:   ___________

Retained by: HR / Privacy Team
```

---

## T9: PII Incident Notification to Customer

```
[ORGANISATION NAME LETTERHEAD]

CONFIDENTIAL — SECURITY INCIDENT NOTIFICATION

Date:            [DATE]
To:              [CUSTOMER CONTACT NAME / SECURITY/DPO CONTACT]
Organisation:    [CUSTOMER NAME]
Re:              Security Incident Notification — [INCIDENT REFERENCE]

Dear [CONTACT NAME],

We are writing to notify you of a security incident that may involve
personally identifiable information (PII) processed by [ORGANISATION NAME]
under our service agreement.

1. Nature of the Incident
[DESCRIBE THE INCIDENT — e.g. "On [DATE], we detected unauthorised access
to [SYSTEM/SERVICE]."]

2. Discovery and Response Timeline
- [DATE/TIME]: Incident detected
- [DATE/TIME]: Initial containment measures implemented
- [DATE/TIME]: Customer notification initiated

3. PII Potentially Affected
Categories of PII:          [e.g. Names, email addresses, usage logs]
Approximate number of
individuals affected:       [NUMBER / RANGE / UNKNOWN AT THIS TIME]
Affected customer tenant:   [YOUR ACCOUNT / ALL CUSTOMERS]

4. Likely Consequences
[DESCRIBE KNOWN OR LIKELY CONSEQUENCES — e.g. "There is a risk that the
affected data could be accessible to the unauthorised party. We have no
current evidence of onward disclosure."]

5. Measures Taken and Proposed
Immediate actions:          [DESCRIBE]
Ongoing investigation:      [DESCRIBE]
Planned remediation:        [DESCRIBE]

6. Your Actions
[DESCRIBE WHAT THE CUSTOMER SHOULD DO — e.g. "We recommend you assess
whether your obligations under [GDPR / applicable law] to notify your
supervisory authority or affected individuals apply. We are available to
provide further information to support your assessment."]

7. Contact
For further information, please contact:
Name:     [DPO / SECURITY CONTACT NAME]
Email:    [EMAIL]
Phone:    [PHONE]

We take this incident very seriously and are committed to keeping you informed
as our investigation progresses. A full incident report will be provided within
[30] days.

Yours sincerely,

[SIGNATORY / CISO / DPO]
[DATE]
```

---

## T10: ISO 27018 Gap Analysis Template

Use this template to assess compliance across ISO 27018's Annex A obligations and key extended controls.

**Assessment Metadata:**
- Organisation / CSP:         [NAME]
- Service(s) in scope:        [NAME]
- Assessor:                   [NAME / ROLE]
- Assessment date:            [DATE]
- ISO 27018 version assessed: [ ] 2025 (3rd edition)    [ ] 2019 (2nd edition)

**Status definitions:**
- **Implemented** — Control is in place, documented, and evidenced
- **Partial** — Control exists but has gaps (undocumented, inconsistently applied, missing evidence)
- **Not Implemented** — No control exists or control is clearly insufficient
- **N/A** — Not applicable; justification documented

---

**Gap Analysis Table:**

| Control Area | Obligation / Topic | Status | Evidence Available | Gaps / Notes | Priority |
|---|---|---|---|---|---|
| **Consent & Purpose** | No processing beyond customer instructions | | | | |
| **Consent & Purpose** | DPA contract terms defining purpose | | | | |
| **Purpose Limitation** | No commercial/marketing use of customer PII | | | | |
| **Purpose Limitation** | Sub-processor purpose restriction in contracts | | | | |
| **Change Notification** | Advance notice of changes to processing | | | | |
| **Sub-processor Info** | Sub-processor info provided to customers | | | | |
| **Temporary Files** | Temp file identification and deletion | | | | |
| **Access Minimization** | Least-privilege access to PII systems | | | | |
| **Access Minimization** | Privileged access requires MFA | | | | |
| **Access Minimization** | Periodic access reviews documented | | | | |
| **PII Return/Deletion** | End-of-contract return/deletion procedure | | | | |
| **PII Return/Deletion** | Written confirmation issued to customers | | | | |
| **Disclosure Notification** | Government request notification procedure | | | | |
| **Disclosure Notification** | Customer notification sent (unless prohibited) | | | | |
| **Disclosure Register** | Disclosure register maintained | | | | |
| **Sub-processor Disclosure** | Sub-processor register maintained and accessible | | | | |
| **Sub-processor Disclosure** | Advance notice of new sub-processors | | | | |
| **Sub-processor Disclosure** | Sub-processor contracts with PII obligations | | | | |
| **Data Residency** | Processing regions disclosed to customers | | | | |
| **Data Residency** | Advance notice of residency changes | | | | |
| **Employee Access** | Employee access to PII logged | | | | |
| **Employee Access** | Employee PII access controls and justification | | | | |
| **Data Subject Rights** | Technical tools available for DSR fulfilment | | | | |
| **Privacy Contact** | Dedicated PII/privacy contact designated | | | | |
| **Privacy Contact** | Contact details accessible to customers | | | | |
| **Breach Notification** | PII incident notification procedure (72 hours) | | | | |
| **Breach Notification** | Incident notification log maintained | | | | |
| **Security Policy** | PII-specific information security policy | | | | |
| **Compliance Evidence** | Certifications/audit reports available to customers | | | | |
| **Supervisory Authority** | Applicable authorities disclosed to customers | | | | |
| **Audit Rights** | Customer audit rights clause in DPA | | | | |
| **Staff Training** | PII awareness training delivered and recorded | | | | |
| **Confidentiality** | Staff confidentiality obligations documented | | | | |
| **Transparency Report** | Transparency report published (where permitted) | | | | |

---

**Summary:**
- Total controls assessed: [NUMBER]
- Implemented: [NUMBER]
- Partial: [NUMBER]
- Not Implemented: [NUMBER]
- N/A: [NUMBER]

**Priority Actions:**
1. [Critical gaps]
2. [High priority actions]
3. [Medium priority actions]

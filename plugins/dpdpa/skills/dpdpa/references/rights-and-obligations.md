# DPDPA - Data Fiduciary Obligations and Data Principal Rights

Deep-dive reference for compliance teams. All obligations cite the Act section AND the
implementing Rule where applicable. Rules references are to the DPDP Rules, 2025 (notified
13 November 2025, effective 13 May 2027 unless phased earlier).

---

## Part A - Data Fiduciary Core Obligations (Section 8)

### A.1 Notice Obligation (Section 5 + Rule 3)

**Trigger:** Before or at the time of requesting consent for any processing.

**Mandatory contents of notice (Rule 3(1)):**

| Element | Requirement |
|---------|-------------|
| Identity of Data Fiduciary | Full legal name and contact details |
| Categories of personal data | Description of the data sought to be collected |
| Specified purpose | Each purpose for which data will be processed - specific, not generic |
| Recipients | Categories of Processors and other Data Fiduciaries who will receive the data |
| Retention period | Duration for which data will be retained, or criteria used to determine it |
| Data Principal rights | Summary of rights under Sections 11–14 |
| Complaint mechanism | How to lodge a complaint with the Data Fiduciary and with the Board |
| Withdrawal procedure | How to withdraw consent and the consequences of withdrawal |

**Format requirements (Rule 3(2)):**
- **Plain language** - no legalese, jargon, or unnecessarily complex syntax
- **Standalone document** - cannot be buried in terms of service, privacy policy footnotes, or general conditions
- **Retrievable at any time** - must be accessible via the Data Fiduciary's platform or website at any point
- **Available in English and other languages** per the Eighth Schedule of the Constitution (Rule 3(3)) if the Data Principal requests translation

**Existing data (Section 5(2)):**
For data collected before commencement of the Act but still being processed:
- Fiduciaries must issue a notice of equivalent content
- Notice must be given within the prescribed period after commencement
- This is the "legacy data compliance" obligation - organisations should map all pre-Act data and prepare retrospective notices

**Common errors:**
- Embedding notice in general T&Cs - non-compliant
- Vague purposes such as "to improve services" - non-compliant
- Notice only available at registration, not retrievable afterwards - non-compliant
- Single notice covering multiple services without purpose separation - risk of invalid consent

---

### A.2 Consent Obligations (Section 6 + Rule 4)

**Validity standard:** Consent is valid ONLY if all five elements are present simultaneously:

| Element | What it means operationally |
|---------|----------------------------|
| Free | Not conditioned on acceptance of a service or product |
| Specific | For each distinct, identified purpose separately |
| Informed | Given after the Data Principal has received the Section 5 notice |
| Unconditional | No coercion, inducement, or consequence attached to refusal |
| Unambiguous | Clear affirmative action - no pre-ticked boxes, no silence as consent |

**Section 6(4) - Withdrawal:**
- Must be as easy to withdraw as it was to give
- One-click or equivalent in-app mechanism required where consent was given digitally
- Email-only withdrawal is likely insufficient if consent was given via a button click
- Prior lawful processing is not invalidated by later withdrawal
- Processing MUST stop promptly after withdrawal - no "grace periods" unless legally justified

**Section 6(10) - Burden of proof:**
The Data Fiduciary must be able to demonstrate that valid consent was obtained. This requires:
- Consent audit logs with timestamp, mechanism used, and content presented at time of consent
- Version control for notices - the notice version presented must be retrievable
- Linkage between consent record and the data processed under it

**Section 6(2):** Consent is **invalid to the extent it infringes the Act** - processing under infringing consent is unlawful to that extent.

**Section 6(3):** Every request for consent must be presented in clear and plain language, with the contact details of the Data Protection Officer (where applicable) or another authorised person.

**Consent Manager (Sections 6(7)–(9) + Rule 4):**
- A Consent Manager is a body corporate registered by the Board
- Data Principals may give, manage, review, and withdraw consent for multiple Data Fiduciaries through a single Consent Manager platform
- Consent Managers must maintain interoperability across registered Data Fiduciaries
- Engaging a Consent Manager does not absolve the Data Fiduciary of its consent validity obligations

---

### A.3 Data Quality Obligation (Section 8(2))

Data Fiduciaries must ensure personal data is:
- **Accurate** - free from errors that would affect Data Principals' interests
- **Complete** - not missing material information
- **Consistent** - aligned across systems when used for decisions or shared with other Fiduciaries

**Scope limitation:** This obligation applies specifically when the data will be:
1. Used to make a decision affecting the Data Principal, or
2. Disclosed to another Data Fiduciary

**Practical implication:** Data used solely for internal analytics that does not affect individual decisions has a lower data quality obligation. Data used for credit scoring, benefit eligibility, or shared with business partners has a higher obligation.

---

### A.4 Security Safeguards Obligation (Section 8(5) + Rule 6)

**Principle:** Reasonable security safeguards to prevent personal data breaches. Rule 6 is
**technology-neutral** - it names outcome-level measures, not specific technologies,
protocol versions, or patch windows.

**Rule 6 - Minimum security safeguards:**

| Safeguard Category | Requirement |
|--------------------|-------------|
| Data security measures | Secure personal data through measures such as encryption, obfuscation, masking, or virtual tokens |
| Access control | Appropriate control of access to the systems used to process personal data |
| Logs and monitoring | Visibility through logs and monitoring to detect, investigate, and remediate unauthorised access |
| One-year retention | Retain logs and relevant personal data for one year to enable breach detection and investigation (unless another law requires otherwise) |
| Processor contracts | Contractual provisions requiring Data Processors to maintain equivalent safeguards |
| Continuity | Measures (such as backups) to ensure continued processing in the event of compromise |

**Highest penalty tier:** Failure to take reasonable security safeguards (Section 8(5)) = ₹250 crore maximum (Section 33 Schedule).

**Key audit questions:**
- Is personal data encrypted at rest and in transit?
- Is access to personal data logged and monitored?
- How quickly can the organisation detect a breach?
- Are all Data Processors bound by equivalent security obligations?

---

### A.5 Breach Notification Obligation (Section 8(6) + Rule 7)

**Trigger:** Any "personal data breach" - unauthorised processing or accidental disclosure causing loss of confidentiality, integrity, or availability.

**Intimation timeline (Rule 7):**

| Step | Timeline | Content |
|------|----------|---------|
| Intimation to each affected Data Principal | **Directly, without delay** (not contingent on any Board direction) | Clear and plain description of the breach; likely consequences; measures being taken; safety steps the Data Principal may take; contact details for queries |
| Initial intimation to Board | **Without delay** | Description of the breach |
| Detailed report to Board | **Within 72 hours** of becoming aware, extendable on request to the Board | Updated and detailed breach information; circumstances and reasons; mitigation; findings about the person who caused the breach; remedial measures; report of intimations to Data Principals |

**Rule 7 - Content requirements:**
- Nature of the breach (unauthorised access, accidental disclosure, ransomware, etc.)
- Personal data categories affected (categories, not necessarily exhaustive item list)
- Approximate volume of records and number of affected Data Principals
- Name and contact details of responsible officer (equivalent to DPO contact)
- Likely consequences of the breach
- Measures taken to address the breach and mitigate harm
- Measures proposed to prevent recurrence

**Key operational points:**
- The 72-hour clock for the detailed Board report runs from when the organisation **becomes aware** of a breach, and may be extended by the Board on request
- Initial intimations (to Data Principals and to the Board) must be made **without delay**, with detail supplemented in the 72-hour report
- Unlike GDPR, the Act does not prescribe a risk-threshold for notification - **all breaches must be intimated**
- Data Principal intimation is a **direct obligation of the Data Fiduciary**; it is not Board-directed

**Penalty:** Failure to notify = ₹200 crore maximum.

**Recommended breach response protocol:**
1. Detection → Incident ticket opened (T=0)
2. T+4 hours: Initial containment and impact triage
3. T+24 hours: Preliminary classification - is this a personal data breach?
4. T+48 hours: Gather notification content; prepare Rule 6 report
5. T+72 hours: Submit to Board (even if investigation ongoing)
6. T+ongoing: Supplementary reporting as investigation progresses

---

### A.6 Data Retention and Erasure Obligation (Section 8(7) + Rule 8)

**Mandatory erasure triggers:**
1. Consent withdrawn by the Data Principal
2. Purpose for which data was collected is fulfilled
3. Data Principal exercises erasure right under Section 12(3)
4. Retention no longer necessary for the specified purpose or required by law

**Erasure extends to Processors:**
- Data Fiduciaries must direct all Data Processors to erase personal data upon termination of the processing engagement
- Data Processors must confirm erasure - contractual clause and confirmation procedure required

**Retention exceptions (Section 8(7) proviso):**
- Where retention is required by applicable law (e.g., statutory record-keeping under Companies Act, GST records, etc.)
- Where retention is necessary to enforce or defend legal rights or claims

**Practical retention schedule design:**
- Map each data category to its lawful retention trigger
- For consent-based processing: retention ends at withdrawal or purpose fulfilment (whichever first)
- For Section 7 legitimate uses: retention ends when the legitimate use purpose is fulfilled
- Statutory overlays: apply the longer of DPDPA retention limits and applicable statutory requirement

---

### A.7 Grievance Mechanism Obligation (Section 8 + Section 13)

**Minimum requirements:**
- Accessible mechanism for Data Principals to submit grievances (web form, email, phone - at minimum one channel)
- Acknowledgement within prescribed period (Rules specify timelines - verify against Rule schedule)
- Resolution within prescribed period (Rules specify timelines)
- Escalation path to the Board clearly communicated (Section 13(3) - exhaustion of fiduciary mechanism required before Board complaint)

**Critical design point:** The grievance mechanism is the mandatory first step before Board intervention. A deficient or non-responsive grievance mechanism not only violates the Act but creates the conditions for Board complaints and regulatory escalation.

---

### A.8 Data Processing Agreements (Section 8(2))

Every Data Processor engaged must be under a **written contract** that specifies:

| Contract Element | Requirement |
|-----------------|-------------|
| Processing instructions | Processor may only process as instructed by the Fiduciary |
| Purpose limitation | Processing restricted to specified purposes |
| Security measures | Processor must implement equivalent safeguards to Rule 6 |
| Sub-processing | Must obtain Fiduciary's prior written approval for sub-processors |
| Audit rights | Fiduciary must have right to audit Processor's compliance |
| Breach notification | Processor must notify Fiduciary promptly upon detecting a breach |
| Erasure on termination | Processor must erase data upon termination of engagement and confirm erasure |
| Data Fiduciary's liability | Fiduciary remains liable to Data Principals for Processor's acts - Fiduciary may seek indemnity from Processor contractually |

**Additional good-practice requirements (no dedicated DPA rule exists in the DPDP Rules 2025 - the contract requirement rests on Section 8(2) of the Act):**
- Contract must be executed before processing begins (not retrospectively)
- Processor-to-sub-processor agreements must flow down all obligations
- Fiduciary should maintain a register of all Processors and sub-processors

---

## Part B - Children's Data (Section 9 + Rules 10 and 12)

### B.1 Age Threshold

**18 years** - uniform across India, no regional variation.

### B.2 Parental Consent (Section 9(1) + Rules 10 and 11)

**Requirement:** Verifiable consent from parent (Rule 10) or lawful guardian (Rule 11) before processing any personal data of a child.

**Rule 10 - Verification methods (prescribed):**

| Method | Description |
|--------|-------------|
| DigiLocker | Digital credentials authenticated via DigiLocker platform (government ID-linked) |
| Government token | Any other government-issued digital token prescribed by MeitY |
| Existing verified data | If the Data Fiduciary already holds verified parent/guardian details from a prior KYC or similar process, these may be relied upon |
| Virtual token | Anonymised tokens issued by entities operating token-based identity infrastructure |

**Key design requirements:**
- Verification must confirm the consenting individual is an adult (18+)
- Verification must confirm the consenting individual is the parent or lawful guardian of the child
- The verification process itself must not collect excessive personal data about the child or parent

**Exemption possibility (Rule 12):**
Certain classes of Data Fiduciaries (e.g., healthcare providers, educational institutions, childcare contexts) are exempt from specified children's-data obligations to the extent and subject to the conditions set out in Rule 12 and the Rules' Schedule. Exemptions must be narrowly construed - no self-certification beyond the specified scope is permitted.

### B.3 Absolute Prohibitions (Section 9(2))

Regardless of consent, the following are **prohibited for all children** (no exceptions unless separately notified):

1. **Tracking or behavioural monitoring** - geolocation tracking, persistent identifiers, browsing history, app usage analytics on individual children
2. **Targeted advertising** - advertising directed at a child based on their personal data, browsing patterns, or inferred characteristics
3. **Any processing likely to cause detrimental effect on the child's well-being**

**Compliance implication:**
- An analytics platform that tracks individual child users violates Section 9(2) even if parental consent is obtained
- An advertising-funded platform that profiles children for ad targeting violates Section 9(2) regardless of consent
- Age-verification must precede any personalised or tracked service - not a post-onboarding check

**Penalty:** ₹200 crore maximum - second-highest penalty tier.

### B.4 Practical Age-Gate Requirements

- Age declaration at registration: must capture claimed age
- Verification trigger: if claimed age is under 18, parental consent verification must be initiated before data processing begins
- False age declaration: Data Fiduciary is protected if it relied in good faith on a verified parental consent - responsibility shifts to the declarant
- Dark patterns: age-gate mechanisms must not use deceptive design to bypass age checks

---

## Part C - Significant Data Fiduciary Obligations (Section 10 + Rule 13)

### C.1 SDF Designation

**Who designates:** Central Government (MeitY) by notification in the Official Gazette.

**Criteria (Section 10):**

| Factor | Indicators |
|--------|-----------|
| Volume of data | Large-scale processing of personal data across a significant number of Data Principals |
| Sensitivity | Processing of special categories (financial, health, biometric, location) at scale |
| Risk to rights | Potential for harm, discrimination, or manipulation of Data Principals |
| Sovereignty and security | Impact on India's sovereignty, integrity, national security |
| Electoral democracy | Potential to influence electoral processes or democratic participation |
| Public order | Processing that could affect public order, communal harmony |

**Current status (April 2026):** The Central Government has not yet published the first list of SDFs. Entities should assess their processing profile and prepare for potential SDF designation.

### C.2 India-Resident Data Protection Officer (Section 10(2)(a) + Rule 13)

| Requirement | Detail |
|-------------|--------|
| Residency | Must be **resident in India** (not abroad) |
| Individual | Must be a natural person - not an entity or external law firm |
| Role before Board | Sole official representative of the SDF before the Data Protection Board |
| Data Principal contact | Primary contact for Data Principal grievances |
| Reporting line | Must have direct access to the highest management of the SDF |

**Key distinction from GDPR DPO:**
- The DPDPA DPO is the SDF's spokesperson and Board liaison - a more operational role than the GDPR advisory DPO
- The DPDPA DPO does not independently audit the organisation; that function is the Data Auditor's
- The DPDPA DPO must physically reside in India - a non-India-based privacy officer does not satisfy this requirement

### C.3 Data Protection Impact Assessment (Section 10(2)(b) + Rule 13)

**Frequency:** Annual - covering the preceding year's processing activities.

**Mandatory content (Rule 13):**

| Assessment Element | What to Cover |
|-------------------|---------------|
| Compliance review | Review of all processing activities against Act and Rules obligations |
| Rights exercise analysis | How Data Principals exercised their rights; complaints received; resolution rate |
| Safeguard adequacy | Assessment of whether security safeguards remain adequate given current threats |
| Third-party risk | Review of all Data Processor relationships and their compliance |
| Large-scale processing risks | Specific risks arising from high-volume or high-sensitivity processing |
| Mitigation measures | Actions taken and proposed to address identified risks |

**Output:** DPIA report submitted to the Board as part of the annual compliance cycle.

### C.4 Annual Independent Data Audit (Section 10(2)(c) + Rule 13)

**Auditor:** External, independent, qualified data auditor (not the SDF's own privacy team or affiliated entity).

**Scope:**
- Compliance with all obligations under the Act and Rules
- Adequacy of security safeguards
- Data processing agreements with Processors
- Data Principal rights fulfilment
- Breach notification history and response adequacy
- Children's data compliance (if applicable)

**Output:** Audit report submitted to the Board. Board may use audit findings in investigations and penalty proceedings.

### C.5 Data Localisation (Rule 13 notification mechanism)

**Mechanism:** Section 10(2) of the Act contains only clauses (a)–(c) - there is no localisation clause in the Act. Any localisation-style restriction enters only through Rule 13: the Central Government may, by notification, identify specified personal data (and related traffic data) that SDFs must not transfer outside India.

**Current status (April 2026):** No localisation notifications issued for SDFs. Entities should monitor MeitY gazette.

**Planning requirement:** SDFs must be capable of implementing localisation on notification - this requires data mapping to identify which data categories and which systems would be affected, and architecture capable of separating India-stored data from globally replicated data.

---

## Part D - Data Principal Rights Fulfilment Procedures

### D.1 Right to Access (Section 11)

**What the Data Principal may request:**
1. Summary of personal data currently being processed
2. Description of processing activities (purpose, legal basis, duration)
3. All Data Fiduciaries and Processors who hold or process the data, with their contact details
4. What data has been shared with each recipient and when

**Response timeline:** Within the prescribed period under Rules (verify against Rule schedule).

**Form of response:** Must be in a format accessible to the Data Principal - plain language, understandable categories, not raw database extracts.

**Limitations:**
- Data Fiduciaries may decline to provide information where disclosure would endanger another person
- Information subject to legal privilege or security exemptions (Section 17) may be withheld
- Must provide a reason for any refusal (enabling Board escalation)

### D.2 Right to Correction, Completion, and Updating (Section 12(1))

**Process:**
1. Data Principal submits correction/completion/update request
2. Data Fiduciary verifies the request
3. Data Fiduciary makes the requested correction, completion, or update
4. Data Fiduciary notifies any Data Processors or other Fiduciaries who received the incorrect data (where feasible)

**Practical requirement:** Systems must be capable of propagating corrections across linked databases and to downstream Processors.

### D.3 Right to Erasure (Section 12(3))

**Trigger:** Data Principal requests erasure of personal data no longer necessary for the specified purpose.

**Limitation grounds where Fiduciary may refuse (Section 12(4)):**
1. Data is still necessary for the specified purpose
2. Retention required by law (statutory obligation)
3. Retention necessary to enforce or defend legal rights

**Process:**
1. Data Principal submits erasure request
2. Data Fiduciary assesses whether any refusal ground applies
3. If no refusal ground: erase from own systems AND direct all Processors to erase
4. If refusal ground applies: notify Data Principal with explanation and right to escalate to Board

### D.4 Right of Grievance Redressal (Section 13)

**Mandatory exhaustion:** Data Principals MUST exhaust the Data Fiduciary's grievance mechanism before filing a complaint with the Board.

**Fiduciary obligations:**
- Grievance mechanism must be accessible (not buried or inaccessible)
- Acknowledgement and resolution within prescribed timelines
- Records of grievances and resolutions must be maintained

**Escalation to Board:** If the Data Principal is unsatisfied with the Fiduciary's response, or if the Fiduciary fails to respond within the prescribed period, the Data Principal may approach the Board.

### D.5 Right to Nominate (Section 14)

**Available triggers:**
- Death of the Data Principal
- Incapacity (unsoundness of mind or physical infirmity preventing exercise of rights)

**Nominee's powers:** The nominee may exercise all rights under Sections 11, 12, and 13 as if they were the Data Principal.

**Operational requirement:** Data Fiduciaries must provide a mechanism for Data Principals to register nominations, update nominations, and for nominees to authenticate themselves upon claiming rights.

---

## Part E - Response Timelines Quick Reference

| Right/Obligation | Prescribed Timeline |
|-----------------|---------------------|
| Breach intimation | Data Principals and Board without delay; detailed Board report within 72 hours of awareness (extendable on request) |
| Grievance acknowledgement | As prescribed by Rules (monitor Rule schedule) |
| Grievance resolution | As prescribed by Rules |
| Access request response | As prescribed by Rules |
| Correction/erasure response | As prescribed by Rules |
| Notice for existing data | Within prescribed period after commencement |

> **Note on prescribed timelines:** The DPDP Rules 2025 set specific timelines for several obligations. Where the table above states "as prescribed by Rules," verify the current Rule text as timelines may be specified in schedules or subsequent notifications. Monitoring MeitY's official gazette is essential for SDF-designated and high-volume Data Fiduciaries.

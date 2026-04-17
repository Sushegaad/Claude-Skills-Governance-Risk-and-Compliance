# ISO 27701 — PII Controller Controls (Clause 7)

All controls in Clause 7 are **normative** for organisations acting as PII Controllers. They are additional to the ISO 27001 Annex A and ISO 27002 controls addressed in Clause 6.

A PII Controller is an entity that alone or jointly with others determines the purposes and means of the processing of PII.

---

## 7.2 — Conditions for Collection and Processing

### 7.2.1 — Identify and Document Purpose

**Objective:** Establish and maintain a clear record of why PII is being processed.

**Requirement:**
The organisation shall identify and document the specific purposes for which PII is collected and processed. Each processing activity must have an articulated purpose that is documented before processing commences.

**What to implement:**
- Maintain a processing register (RoPA — Records of Processing Activities) that lists all processing activities with their stated purpose
- Ensure that each purpose is specific, explicit, and legitimate — not stated in vague terms such as "improving services"
- Ensure purposes are documented before collection begins (purpose cannot be retroactively created)
- Review and update purposes when processing activities change

**Evidence for audit:**
- Up-to-date Records of Processing Activities (RoPA) with all processing activities and stated purposes
- Version history of the RoPA showing purposes pre-date or accompany collection
- Process documentation for how new processing activities are assessed for purpose documentation

**Common pitfalls:**
- Vague purposes such as "business purposes" or "analytics" without specificity
- Purposes stated only in privacy notices but not reflected in internal records
- Processing activities added without updating the RoPA

**GDPR:** Art. 5(1)(b) (purpose limitation), Art. 30 (records of processing activities)

---

### 7.2.2 — Identify Lawful Basis

**Objective:** Ensure each processing activity has a documented legal justification.

**Requirement:**
The organisation shall determine and document the lawful basis for processing PII for each identified purpose. Where the applicable law requires it, a specific legal basis must be identified and recorded.

**What to implement:**
- For each row in the RoPA, document the applicable lawful basis
- Where consent is relied upon, ensure it meets the requirements of 7.2.3 and 7.2.4
- Where legitimate interests are the basis, conduct and document a Legitimate Interests Assessment (LIA) / balancing test
- Document any special category PII and the additional lawful basis required for its processing

**Lawful basis options (aligned to GDPR Art. 6 and equivalent legislation):**
| Basis | When applicable |
|-------|----------------|
| Consent | PII principal has freely given, specific, informed, and unambiguous agreement |
| Contract | Processing necessary for a contract with the PII principal |
| Legal obligation | Processing required to comply with a law |
| Vital interests | Processing necessary to protect life of the PII principal or another person |
| Public task | Processing necessary for a task in the public interest or exercise of official authority |
| Legitimate interests | Processing necessary for the organisation's or a third party's legitimate interests, provided not overridden by the individual's rights |

**Evidence for audit:**
- RoPA with lawful basis column populated for every processing activity
- Legitimate Interests Assessments where legitimate interests are relied upon
- Records showing legal review of lawful basis determinations
- Special category PII processing documented with both the Art. 6 basis and the additional condition (e.g., explicit consent, employment law, vital interests)

**GDPR:** Art. 6 (lawfulness), Art. 9 (special categories), Art. 10 (criminal convictions)

---

### 7.2.3 — Determine When and How Consent Is to Be Obtained

**Objective:** Design a consent mechanism that meets applicable legal requirements.

**Requirement:**
Where consent is used as the lawful basis for processing, the organisation shall determine the procedure for obtaining and recording consent prior to any processing under that basis commencing. The consent mechanism must ensure consent is freely given, specific, informed, unambiguous, and — where required by law — explicit (for special categories).

**What to implement:**
- Document the consent collection method for each processing activity where consent is the basis
- Ensure granularity: separate consent for each processing purpose (bundling is not permitted)
- Ensure consent language is plain and intelligible — avoid pre-ticked boxes
- Define the age of consent threshold (under GDPR: typically 16 years; some EU member states permit 13–15)
- Design the consent flow to make withdrawal as easy as giving consent
- Document what records of consent are captured (who, what, when, how)

**Evidence for audit:**
- Consent design documentation or mockup of consent collection interface
- Documented decision on consent age threshold and any verification mechanism
- Sample consent records
- Privacy engineering review confirming withdrawal mechanism is as easy as giving consent

**GDPR:** Art. 7, Art. 8 (children's consent), Recital 32, Recital 43

---

### 7.2.4 — Obtain and Record Consent

**Objective:** Capture and maintain evidence of consent for each PII principal where consent is relied upon.

**Requirement:**
The organisation shall obtain and maintain records of consent from PII principals before processing under consent begins. Records must demonstrate that valid consent was given, and must be preserved for the duration of the processing relationship.

**What to implement:**
- Implement a consent recording system that stores: who consented, to what, when, how, and through which mechanism or version of the privacy notice
- Ensure consent records are retrievable per PII principal
- Implement a mechanism to invalidate consent records when consent is withdrawn
- Maintain version histories of consent notices so historic records can be validated against the notice in force at the time of consent

**Evidence for audit:**
- Consent database or equivalent records, searchable by PII principal identifier
- Evidence of version-controlled privacy/consent notices
- Demonstration that withdrawn consent is reflected in the processing status of the PII principal's data
- Data retention policy covering consent records themselves

**GDPR:** Art. 7(1) (burden of proof on controller), Art. 7(3) (right to withdraw)

---

### 7.2.5 — Privacy Impact Assessment

**Objective:** Systematically identify and treat privacy risks for new or significantly changed processing activities.

**Requirement:**
The organisation shall establish and implement a PIA (Privacy Impact Assessment) programme. PIAs must be conducted before initiating processing activities that may result in high risk to PII principals, and the results must inform risk treatment decisions.

**PIA process steps:**
1. **Screening/threshold assessment:** Determine whether a full PIA is required based on documented trigger criteria
2. **Describe the processing:** Document the nature, scope, context, and purposes of the processing
3. **Assess necessity and proportionality:** Verify that processing is limited to what is necessary
4. **Assess risks to PII principals:** Evaluate likelihood and severity of harm to individuals
5. **Identify mitigation measures:** Select controls to reduce identified risks to an acceptable level
6. **Document outcome:** Record the PIA result, residual risk assessment, and approver
7. **Consult supervisory authority if required:** Where high residual risk remains after mitigation

**Evidence for audit:**
- PIA procedure document with defined trigger criteria
- Log/register of all PIAs conducted
- Sample completed PIAs including screening assessment, risk assessment, and outcome
- Evidence of corrective actions arising from PIA findings
- Records of where supervisory authority consultation was determined necessary

**GDPR:** Art. 35 (DPIA), Art. 36 (prior consultation), WP248 rev.01 (DPIA criteria)

---

### 7.2.6 — Contracts with PII Processors

**Objective:** Ensure binding privacy obligations are placed on all processors engaged by the organisation.

**Requirement:**
Where the organisation engages a PII Processor to process PII on its behalf, it shall ensure that a written contract (or equivalent legal instrument) is in place before processing commences. The contract must require the processor to process PII only on the controller's documented instructions and to apply appropriate technical and organisational security measures.

**Required contract provisions (minimum):**
- Process PII only on documented instructions from the controller
- Bind all staff to confidentiality obligations
- Implement appropriate security measures
- Engage sub-processors only with the controller's prior written authorisation (general or specific)
- Assist the controller in meeting PII principal rights obligations
- Delete or return all PII at contract end, per controller instruction
- Provide evidence of compliance to the controller
- Notify the controller of any breach of PII without undue delay

**Evidence for audit:**
- Register of all PII processors with contract status
- Sample processor agreements showing all required provisions
- Approval records for new processor engagements
- Sub-processor notification/approval records

**GDPR:** Art. 28 (processor), Art. 29 (processing under authority)

---

### 7.2.7 — Joint PII Controllers

**Objective:** Define and document responsibilities where two or more controllers jointly determine processing purposes and means.

**Requirement:**
Where the organisation processes PII jointly with one or more other PII controllers, it shall establish and document a joint controller arrangement. The arrangement must allocate responsibilities between the parties for meeting applicable privacy obligations, particularly as regards PII principal rights and transparency.

**What to implement:**
- Identify any joint controller arrangements in the RoPA
- Conclude a joint controller agreement with each joint controller partner
- Agree on which party is the primary contact for PII principals
- Ensure the essential details of the joint controller arrangement are made available to PII principals

**Evidence for audit:**
- RoPA entries identifying joint controller arrangements
- Signed joint controller agreements with all joint controllers
- Privacy notice that discloses the joint controller relationship to PII principals

**GDPR:** Art. 26 (joint controllers)

---

### 7.2.8 — Records of PII Processing Activities (RoPA)

**Objective:** Maintain an authoritative register of all processing activities involving PII.

**Requirement:**
The organisation shall create and maintain a documented Record of Processing Activities (RoPA) covering all processing activities conducted as a PII Controller. The RoPA must be kept up-to-date and must be available to the supervisory authority on request.

**Required RoPA fields:**
| Field | Description |
|-------|-------------|
| Processing activity name | Descriptive name of the processing activity |
| Controller name and contact details | Legal entity name, registered address, DPO contact |
| Purpose(s) of processing | Each specific, documented purpose |
| Lawful basis | Per purpose |
| Categories of PII principals | e.g., Customers, Employees, Job Applicants |
| Categories of PII | e.g., Name, Email, Financial data, Health data |
| Special category PII? | Yes/No; if yes, list categories and additional lawful basis |
| Recipients of PII | Internal and external recipients including processors |
| Third country transfers | Countries; safeguard mechanism (e.g., adequacy decision, SCCs, BCRs) |
| Retention period | Per PII category or processing purpose |
| Security measures | Summary reference to applicable technical/organisational measures |
| Date created / last reviewed | For currency management |

**Evidence for audit:**
- Current, complete RoPA covering all in-scope processing activities
- Process showing how new processing activities are added to the RoPA
- Change log or version control showing RoPA is maintained over time

**GDPR:** Art. 30 (records of processing activities)

---

### 7.2.9 — PII in Data/System Inventories

**Objective:** Maintain visibility of all systems and data stores that hold PII.

**Requirement:**
The organisation shall maintain an inventory of information systems, data stores, and applications that process PII. This inventory supports the RoPA, risk assessment, and security control allocation for PII assets.

**What to implement:**
- Extend the ISO 27001 asset inventory to include PII classification per asset
- Document for each PII-holding asset: asset type, PII categories stored, PII volume (approximate), system owner, and applicable security controls
- Link the asset inventory to the RoPA so each processing activity maps to the systems involved
- Review the inventory at least annually and on significant system changes

**Evidence for audit:**
- Asset inventory with PII classification column
- Cross-reference between asset inventory and RoPA
- Annual review record

---

## 7.3 — Obligations to PII Principals

### 7.3.1 — Obligation to PII Principals

**Objective:** Establish the organisation's commitment to fulfilling all applicable PII principal rights.

**Requirement:**
The organisation shall determine the applicable PII principal rights under the law(s) governing the PIMS scope and establish procedures to fulfil those obligations. Applicable rights must be documented in the privacy notice provided to PII principals.

**Core rights to implement (privacy law aligned):**
- Right of access to their PII
- Right to rectification of inaccurate PII
- Right to erasure (right to be forgotten)
- Right to restrict processing
- Right to data portability (where applicable by law)
- Right to object to processing (including profiling)
- Rights related to automated decision-making

**Evidence for audit:**
- Documented rights procedures for each applicable right
- Privacy notice disclosing available rights
- Training records showing staff know how to route and handle rights requests
- Log of rights requests received and fulfilled

---

### 7.3.2 — Determine Information for PII Principals

**Objective:** Identify what information must be provided to PII principals at the time of, or before, collection of their PII.

**Requirement:**
The organisation shall determine what information it is obligated to provide to PII principals about its processing activities, including: the identity and contact details of the organisation, the purposes of processing, the lawful basis, recipients, retention periods, rights available to PII principals, and any automated decision-making.

**Disclosure checklist (derived from GDPR Art. 13/14 and equivalent laws):**
- [ ] Controller identity and contact details
- [ ] DPO contact details (where applicable)
- [ ] Processing purposes and lawful basis for each
- [ ] Legitimate interests relied upon (if applicable)
- [ ] Recipients or categories of recipients
- [ ] Third country transfers and safeguards
- [ ] Retention periods
- [ ] Rights available (access, rectification, erasure, restriction, portability, object)
- [ ] Right to withdraw consent (where consent is the basis)
- [ ] Right to lodge a complaint with the supervisory authority
- [ ] Whether provision of PII is a statutory or contractual requirement
- [ ] Existence of automated decision-making / profiling and meaningful information about the logic

---

### 7.3.3 — Provide Information to PII Principals

**Objective:** Deliver the required disclosures to PII principals in a clear and accessible manner.

**Requirement:**
The organisation shall provide the information determined under 7.3.2 to PII principals at or before the time PII is collected (where PII is obtained directly) or within a reasonable period (where PII is obtained indirectly). The information must be provided in a concise, transparent, intelligible, and easily accessible form, using clear and plain language.

**Implementation:**
- Publish a privacy notice/privacy policy on the organisation's website prominently
- For new data collection points (forms, apps, checkout flows), display a notice at the point of collection
- For indirect collection (purchasing data from brokers, obtaining via third parties), notify PII principals within a reasonable period (not exceeding one month under GDPR Art. 14(3)(a))
- Maintain version history of privacy notices for audit purposes

**Evidence for audit:**
- Current privacy notice with all required disclosures
- Historical versions of the privacy notice with effective dates
- Evidence of how the notice is presented to PII principals at collection points
- Records of indirect collection notification campaigns

**GDPR:** Art. 12 (transparency), Art. 13 (direct collection), Art. 14 (indirect collection)

---

### 7.3.4 — Provide Mechanism to Modify or Withdraw Consent

**Objective:** Enable PII principals to modify or withdraw their consent at any time, as easily as it was given.

**Requirement:**
Where consent is the lawful basis, the organisation shall provide a mechanism for PII principals to withdraw or modify their consent at any time. Withdrawal must be as easy as giving consent and must not result in the PII principal being penalised for exercising this right.

**Implementation:**
- Provide a clear withdrawal mechanism (e.g., unsubscribe link, account settings page, email request process)
- Document the maximum processing time after withdrawal before processing ceases
- Ensure downstream systems (marketing platforms, analytics tools, third-party processors) are notified of withdrawal
- Do not condition access to services on consent where it is not necessary for the service

**Evidence for audit:**
- Demonstration of withdrawal mechanism in the product/service
- Process document for propagating withdrawal to all downstream systems and processors
- Test evidence showing processing ceases within the stated timeline after withdrawal

---

### 7.3.5 — Provide Mechanism for Objecting to Processing

**Objective:** Enable PII principals to object to processing based on legitimate interests or for direct marketing.

**Requirement:**
Where processing is based on legitimate interests or is for direct marketing purposes, the organisation shall provide a mechanism for PII principals to object. Direct marketing objections must always be honoured without assessment; legitimate interests objections must be assessed against whether the organisation has compelling grounds.

**Implementation:**
- Include the right to object in the privacy notice
- Provide a contact mechanism for submitting objection requests (email, online form)
- For direct marketing: implement an opt-out mechanism (e.g., unsubscribe in all commercial emails), and honour all opt-outs within the maximum permissible timeframe
- For legitimate interests objections: conduct a documented balancing assessment within the response window
- Log all objection requests and outcomes

**GDPR:** Art. 21 (right to object), Art. 17(1)(c) (erasure following successful objection)

---

### 7.3.6 — Access to PII

**Objective:** Enable PII principals to obtain confirmation and a copy of their PII being processed.

**Requirement:**
The organisation shall implement a procedure for handling Subject Access Requests (SARs) / PII access requests. The procedure must enable the organisation to confirm whether PII is being processed, provide a copy of the PII, and supply all required supplementary information within the legally required timeframe.

**SAR procedure steps:**
1. Receive request (any channel; note submission date and time)
2. Verify identity of the requestor (proportionate to sensitivity of PII)
3. Acknowledge receipt within required timeframe
4. Locate all PII held across all systems and data stores
5. Compile response (copy of PII + mandatory supplementary details)
6. Apply redactions for third-party data
7. Deliver response within legal deadline (e.g., 30 days under GDPR Art. 12(3))
8. Log the request, actions, and outcome

**Evidence for audit:**
- SAR procedure documentation
- SAR log/register with dates, actions, and outcomes
- Sample responses (appropriately anonymised)
- Training records for staff handling SARs

**GDPR:** Art. 15 (right of access)

---

### 7.3.7 — Rectification and Erasure

**Objective:** Enable PII principals to correct inaccurate PII and request erasure where the right applies.

**Requirement:**
The organisation shall implement procedures to handle rectification and erasure requests from PII principals within legally required timelines. Rectification must be applied to all copies of the PII held, including in backup systems and by processors. Erasure must be applied where the right is established and no overriding legal basis to retain applies.

**Erasure conditions (right applies when):**
- PII is no longer necessary for the purpose it was collected
- PII principal withdraws consent and no other lawful basis applies
- PII principal objects and there are no overriding legitimate grounds
- PII has been processed unlawfully
- Erasure is required by applicable law
- PII was collected from a child

**Erasure is not required when processing is necessary for:**
- Exercise of freedom of expression
- Compliance with a legal obligation
- Public interest
- Legal claims

**Evidence for audit:**
- Rectification and erasure procedure documents
- Log of rectification and erasure requests with outcomes
- Evidence of notification to processors and other recipients of PII following rectification/erasure
- Backup and archive policy addressing erasure from backup media

**GDPR:** Art. 16 (rectification), Art. 17 (erasure)

---

### 7.3.8 — PII Controllers Informing PII Processors

**Objective:** Ensure processors are notified of any changes to processing instructions, including those arising from PII principal rights outcomes.

**Requirement:**
Where a PII Controller instructs a PII Processor, and where the outcome of a PII principal rights request or a change to processing conditions requires a change in what the processor does, the Controller shall notify the Processor promptly.

**Implementation:**
- Establish a notification procedure from the rights fulfilment team to the processor management function
- Include provisions in processor contracts requiring the processor to acknowledge and act on Controller instructions within defined timeframes
- Log all instructions issued to processors and their acknowledgement

---

## 7.4 — Privacy by Design and Privacy by Default

### 7.4.1 — Limit Collection

**Objective:** Ensure only PII that is necessary for the stated purpose is collected.

**Requirement:**
The organisation shall limit the collection of PII to the minimum necessary for the identified and documented purpose. Collection of PII that exceeds what is required for the purpose (over-collection) is not permitted.

**What to implement:**
- Include data minimisation requirements in system design and development standards
- Require a justification for each PII field collected against the stated purpose
- Include data minimisation review as part of PIA and system design reviews
- Challenge business requests to collect additional PII without a documented purpose

**Evidence for audit:**
- Privacy engineering / design review records showing data element justification
- PIA records documenting minimisation assessment
- Development standards that include data minimisation requirements

**GDPR:** Art. 5(1)(c) (data minimisation), Art. 25(2) (privacy by default)

---

### 7.4.2 — Limit Processing

**Objective:** Ensure PII is processed only for the purposes for which it was collected, and only to the extent necessary.

**Requirement:**
The organisation shall implement purpose limitation controls to prevent PII from being used for secondary purposes that were not disclosed to the PII principal at the time of collection. Where secondary processing is considered, a compatibility assessment must be conducted.

**What to implement:**
- Technical access controls limiting which systems and personnel can access PII to those with a need linked to the specified purpose
- Audit logging to detect access outside the intended purpose
- A process for assessing compatibility when new secondary purposes are identified
- Prohibition on sharing PII internally for purposes not covered by the original disclosure

**GDPR:** Art. 5(1)(b) (purpose limitation), Art. 6(4) (compatible processing)

---

### 7.4.3 — Accuracy and Quality

**Objective:** Maintain the accuracy, completeness, and currency of PII held.

**Requirement:**
The organisation shall implement measures to ensure PII is accurate and, where necessary, kept up to date. Inaccurate or outdated PII must be corrected or deleted without delay.

**What to implement:**
- Provide PII principals with mechanisms to update their information (e.g., account self-service)
- Implement data quality checks at point of collection
- Define processes for proactive data quality reviews for long-held PII
- Ensure rectification requests (7.3.7) trigger updates to all records

**GDPR:** Art. 5(1)(d) (accuracy)

---

### 7.4.4 — PII Minimisation Objectives

**Objective:** Set measurable objectives for reducing PII collection and processing to the minimum necessary.

**Requirement:**
The organisation shall define privacy objectives related to PII minimisation, monitor progress against them, and take corrective action where objectives are not met.

**Example minimisation objectives:**
- Reduce the number of optional PII fields in registration forms by [X]% by [date]
- Achieve 100% pseudonymisation of PII in non-production environments by [date]
- Reduce retention of marketing PII beyond defined consent periods to zero

---

### 7.4.5 — De-identification and Deletion

**Objective:** Reduce privacy risk by anonymising or deleting PII where it is no longer needed.

**Requirement:**
The organisation shall implement de-identification and/or deletion measures for PII that is no longer required for the identified purpose. Where de-identification is used in place of deletion, the technique must render the PII non-identifiable and the process must be documented and verified.

**De-identification techniques:**
| Technique | Description | Risk Level |
|-----------|-------------|------------|
| Anonymisation | Irreversible removal of all identifiers such that re-identification is impossible | Lowest (no longer PII once anonymised) |
| Pseudonymisation | Replacing direct identifiers with pseudonyms; re-identification possible with additional data | Moderate (still PII under GDPR) |
| Data masking | Partially obscuring PII (e.g., email: a****@domain.com) | Varies by level of masking |
| Aggregation | Replacing individual records with statistical summaries | Low if aggregation is sufficient |
| K-anonymity / l-diversity | Statistical privacy protection ensuring each record is indistinguishable from k-1 others | Depends on implementation |

**Evidence for audit:**
- Data disposal / deletion procedure
- De-identification standards and validation procedures
- Records of deletion events (what was deleted, when, by whom)
- Confirmation that backup media containing PII is eventually overwritten or securely destroyed

---

### 7.4.6 — Temporary Files

**Objective:** Ensure PII contained in temporary files (which arise during processing) does not persist beyond its intended use.

**Requirement:**
The organisation shall identify and implement controls to ensure that temporary files containing PII are not retained longer than necessary for the processing purpose that created them. Temporary files include cache files, log files, working files, backup work files, and other ephemeral stores.

**Implementation:**
- Document all known temporary file types and their expected lifecycle
- Implement automated deletion or purging of temporary files containing PII after processing completes
- Include temporary file management in PIA and security review procedures
- Restrict developer access to temporary files containing production PII

---

### 7.4.7 — Retention

**Objective:** Ensure PII is not retained beyond the period necessary for its processing purpose, or beyond applicable legal retention obligations.

**Requirement:**
The organisation shall establish, document, and enforce retention schedules for each category of PII. PII must be deleted or anonymised when the retention period expires, unless a legal obligation requires retention.

**Retention schedule components:**
| PII Category | Processing Purpose | Retention Period | Retention Basis | Disposal Method | Owner |
|--------------|-------------------|-----------------|-----------------|----------------|-------|
| Customer account data | Contract fulfilment | Duration of contract + 7 years | Legal obligation (tax/accounting) | Secure deletion | IT/Legal |
| Marketing email lists | Direct marketing | Until consent withdrawn or 2 years inactive | Consent | Secure deletion | Marketing |
| Job applicant data (unsuccessful) | Recruitment | 6 months post-rejection | Legitimate interests | Secure deletion | HR |
| Employee HR records | Employment | Duration of employment + 6 years | Legal obligation | Secure deletion + archive | HR |
| CCTV footage | Security | 30 days unless incident identified | Legitimate interests | Automatic overwrite | Facilities |

**Evidence for audit:**
- Published retention schedule / data retention policy
- Evidence of automated or managed deletion processes
- Audit of retention compliance (sample check of data stores vs. schedule)
- Records of legal hold process when retention is extended for litigation

**GDPR:** Art. 5(1)(e) (storage limitation)

---

## 7.5 — PII Sharing, Transfer and Disclosure

### 7.5.1 — Basis for PII Transfer Between Jurisdictions

**Objective:** Ensure that international transfers of PII have a lawful basis before the transfer occurs.

**Requirement:**
The organisation shall determine and document the legal mechanism relied upon for each transfer of PII to countries or international organisations where the level of data protection may differ. No transfer shall occur without a documented lawful transfer mechanism.

**Transfer mechanisms (aligned to GDPR Chapter V and comparable laws):**
| Mechanism | Description |
|-----------|-------------|
| Adequacy decision | Transfer to a country recognised by the relevant authority as providing adequate protection (e.g., EU adequacy decisions for UK, Israel, Japan, South Korea, etc.) |
| Standard Contractual Clauses (SCCs) | EU Commission approved model clauses incorporated into a binding contract between exporter and importer |
| Binding Corporate Rules (BCRs) | Approved intra-group policies governing transfers within a multinational enterprise |
| Approved Codes of Conduct | Transfer covered by an approved code with binding and enforceable commitments |
| Certification mechanisms | Transfer to a certified recipient (once certification mechanisms are approved) |
| Specific derogations | Transfer based on explicit consent, contract performance, vital interests, public interest, or legal claims — only for non-repetitive transfers where compelling necessity applies |

**Evidence for audit:**
- Transfer impact assessments (where required — e.g., SCCs to non-adequate third countries)
- RoPA entries documenting all third country transfers with the mechanism relied upon
- Copies of signed SCCs or BCR documentation
- Evidence that transfers to non-adequate countries have been assessed and approved

**GDPR:** Art. 44–49 (international transfers)

---

### 7.5.2 — Countries and International Organisations to Which PII Can Be Transferred

**Objective:** Maintain an approved list of transfer destinations with confirmed lawful mechanisms.

**Requirement:**
The organisation shall maintain a record of all countries and international organisations to which PII may be transferred, along with the legal safeguard in place for each destination. This list should be reflected in the RoPA (7.2.8) and disclosed in the privacy notice (7.3.3).

**Implementation:**
- Maintain a countries-and-safeguards register as part of the RoPA or as a supplementary document
- Review the register when transfer destinations change, when adequacy decisions are issued/revoked, or when the standard contractual clauses in use are updated
- Where the Schrems II judgment or equivalent rulings affect the legal basis relied upon, conduct a Transfer Impact Assessment (TIA) to confirm transfers remain lawful

**Evidence for audit:**
- Countries and safeguards register
- Transfer Impact Assessment (TIA) documentation for transfers to non-adequate destinations
- Up-to-date SCC documentation reflecting the current approved versions

---

### 7.5.3 — Records of PII Disclosures to Third Parties

**Objective:** Maintain a comprehensive log of all PII disclosures to third parties for accountability and audit purposes.

**Requirement:**
The organisation shall maintain records of PII that has been disclosed to third parties (other than as part of documented processor relationships). These records support the organisation's accountability obligations, enable management of PII principal access requests, and demonstrate compliance.

**Records to maintain:**
- Third party identity
- Categories of PII disclosed
- Date and method of disclosure
- Legal basis or business reason for disclosure (e.g., law enforcement request, court order, contractual obligation)
- Whether the PII principal was notified of the disclosure and if not, why

**Evidence for audit:**
- Disclosure log with entries for all PII disclosures outside processor relationships
- Process for how ad-hoc disclosure requests (e.g., from law enforcement) are assessed, approved, and logged
- Records of controller notification to PII principals of disclosures where required

**GDPR:** Art. 30 (records), Art. 33–34 (breach notification includes disclosure context)

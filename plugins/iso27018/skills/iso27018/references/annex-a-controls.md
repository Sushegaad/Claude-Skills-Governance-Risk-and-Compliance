# ISO/IEC 27018 — Annex A Extended Control Set for PII Protection in Public Cloud

## Overview

Annex A of ISO/IEC 27018 is **normative** and contains an extended set of controls that go beyond those in ISO/IEC 27002. These controls address PII protection requirements specific to public cloud service providers acting as PII processors that are not addressed by the base ISO 27002 control set.

The controls are organized in line with the **11 privacy principles of ISO/IEC 29100**:

1. Consent and choice
2. Purpose legitimacy and specification
3. Collection limitation
4. Data minimization
5. Use, retention and disclosure limitation
6. Accuracy and quality
7. Openness, transparency and notice
8. Individual participation and access
9. Accountability
10. Information security
11. Privacy compliance

---

## Version Note

- **ISO 27018:2019 (2nd edition):** Annex A aligned with ISO 27002:2013 domain structure  
- **ISO 27018:2025 (3rd edition):** Annex A retained and updated; Annex B added; controls aligned with ISO 27002:2022

The underlying obligations in Annex A are substantially consistent across both editions. The 2025 edition refines language and aligns with ISO 27002:2022 control taxonomy.

---

## Annex A Controls — By Privacy Principle

### Principle 1: Consent and Choice

**Obligation: No processing of PII beyond purposes specified by the cloud service customer**

The CSP shall not process PII entrusted to it by a cloud service customer for any purpose other than what the customer has instructed. The CSP acts exclusively as a processor — it has no independent right to determine the purpose of processing.

**What this means in practice:**
- The CSP's service agreement must clearly define the purposes for which PII may be processed
- The CSP must not use customer PII to develop its own products, train its own AI models, or for any purpose not authorised by the customer
- Where the CSP processes customer account data (e.g. billing information), it may act as a PII controller for that subset — ISO 27018 does not govern that activity
- Any proposed change to processing purpose requires customer consent before implementation

**Evidence for audit:**
- Service agreement clauses defining scope and purpose of PII processing
- Internal policies prohibiting unauthorised secondary use of customer PII
- Staff training records confirming employees understand purpose limitation

---

### Principle 2: Purpose Legitimacy and Specification

**Obligation: No use of PII for commercial, marketing, or advertising purposes**

The CSP shall not use PII processed on behalf of a cloud service customer for its own commercial purposes — including targeted advertising, cross-selling, profiling, or sharing with third parties for their marketing.

**Specific controls:**

**2a. Prohibition on marketing use of PII**
- Contracts with cloud service customers must explicitly prohibit the CSP from using customer PII for direct marketing, behavioural advertising, or profiling for commercial gain
- This prohibition applies whether the PII is processed in aggregate, pseudonymised, or individually
- The prohibition must also bind CSP's affiliates and sub-processors

**2b. Restriction on sub-processor use**
- Sub-processors may only process PII for the purposes specified by the cloud service customer
- Sub-processor agreements must include equivalent purpose limitation restrictions

**Evidence for audit:**
- Customer contract terms prohibiting commercial use of PII
- Sub-processor agreement clauses with equivalent protections
- Advertising and analytics policy documentation confirming customer PII is excluded

---

### Principle 3: Collection Limitation

**Obligation: Transparency and notification regarding PII processing activities**

The CSP shall not make material changes to how it processes customer PII without providing adequate advance notice to the cloud service customer. This allows customers to fulfil their own notification obligations to PII principals.

**Specific controls:**

**3a. Notification before material changes**
- Before making changes that affect the nature or scope of PII processing, the CSP must notify the customer with sufficient lead time to allow assessment and action
- Material changes include: additions or changes to sub-processors, changes to data residency, changes to retention periods, changes to access controls

**3b. Completing information about activities by sub-processors**
- The CSP must provide the customer with sufficient information about sub-processors to enable the customer to complete their own processing records (e.g. Article 30 GDPR records)
- This includes sub-processor name, country of processing, purpose, and applicable safeguards

**Evidence for audit:**
- Change notification policy and documented notification sent to customers
- Sub-processor information provided to customers (register or contractual schedule)
- Records of advance notifications made

---

### Principle 4: Data Minimization

**Obligation: Temporary files and minimal access to PII**

**4a. Temporary files containing PII**
When the CSP creates temporary files, intermediate copies, or cache data that contains PII as part of delivering its services, it shall:
- Identify and document the creation of such temporary PII
- Define and enforce a retention period for temporary files (minimum: deleted promptly after operational need expires)
- Apply the same access and security controls to temporary files as to primary PII stores
- Include temporary file management in data disposal procedures

Examples of temporary PII sources: processing queues, backup staging areas, log files, debugging artefacts, CDN caches.

**4b. Access minimization — employee access to PII**
- Employee access to PII shall be restricted to the minimum necessary to fulfil the service (principle of least privilege)
- Privileged access to PII storage must be individually justified and time-limited where possible
- Access rights must be reviewed regularly (at minimum annually) and revoked promptly upon role change or departure
- Administrator access to systems storing PII must be subject to multi-factor authentication

**Evidence for audit:**
- Documented temporary file handling procedure
- Access control policy with least-privilege provisions for PII
- Access review records (periodic reviews showing revocations)
- Privileged access management records

---

### Principle 5: Use, Retention and Disclosure Limitation

**Obligation: Return, transfer, disposal of PII and disclosure notification**

**5a. Return, transfer and disposal of PII**
At the end of the service contract (including termination for any reason), the CSP shall:
- Return all PII to the cloud service customer, transfer it to an alternative provider at the customer's direction, or securely delete/destroy it
- Provide written confirmation that all PII (including all copies, backups, and any data held by sub-processors) has been returned or deleted
- The timeframe for return/disposal shall be agreed in the service contract (a common standard is 30–90 days)
- Retain a minimal audit record (not PII content) documenting that disposal occurred

**5b. PII disclosure to third parties — notification obligations**
When the CSP is legally required (e.g. court order, government authority request) to disclose PII to a third party, the CSP shall:
- Notify the affected cloud service customer promptly, unless legally prohibited from doing so (e.g. official secrecy order, national security direction)
- Document all legally required disclosures in a disclosure register
- Challenge legally defective or overbroad requests where legally permitted to do so
- Not voluntarily disclose PII to any government, law enforcement, or third party except as required by law or instructed by the cloud service customer

**5c. Record of disclosures**
The CSP shall maintain a disclosure register recording:
- Date and nature of the request
- Requesting authority/organisation
- Legal basis cited
- What PII was disclosed
- Whether customer was notified (and if not, why)
- Any legal challenge made

**Evidence for audit:**
- Service contract clauses governing PII return/deletion
- Written confirmation letters issued to customers upon contract termination
- Disclosure register (may be provided in redacted form to customers on request)
- Internal procedure for handling government/law enforcement requests

---

### Principle 6: Accuracy and Quality

**Obligation: Supporting PII accuracy and enabling corrections**

The CSP shall implement mechanisms that enable cloud service customers to maintain the accuracy and quality of PII held in the cloud service:
- Provide APIs, admin interfaces, or data export capabilities that allow customers to update, correct, and delete PII
- Not impede corrections, updates, or deletions requested by the customer or by PII principals exercising their rights
- Process data correction and deletion requests within agreed response times
- Ensure deletion propagates to backups, caches, and sub-processors within a defined period

**Evidence for audit:**
- Product documentation showing update/delete capabilities
- API documentation or admin console guides
- Response time SLAs for data deletion requests
- Evidence that deletion cascades to sub-processors

---

### Principle 7: Openness, Transparency and Notice

**Obligation: Sub-processor disclosure and data residency transparency**

**7a. Disclosure of sub-processors**
The CSP shall:
- Maintain a current, accessible list of all sub-processors used to process customer PII
- Notify customers in advance of adding new sub-processors or replacing existing ones (advance notice period typically defined in contract — a common standard is 30 days)
- Provide customers with the contractual right to object to new sub-processors
- Ensure the sub-processor list includes: sub-processor name, registered country, purpose, and applicable jurisdiction

**7b. Data residency and transfer transparency**
The CSP shall:
- Disclose the countries and regions in which customer PII may be processed, stored, or transferred
- Provide advance notice of changes to data residency locations
- Where PII is transferred to countries outside the customer's jurisdiction, clearly identify the applicable international transfer mechanism (e.g. SCCs, adequacy decision, BCRs)
- Make data residency information readily available in service documentation (not only on request)

**7c. Government and law enforcement request transparency**
Where legally permitted, the CSP shall publish aggregated information (a transparency report) about:
- The number and types of government/law enforcement requests received
- The jurisdictions from which requests originated
- The proportion of requests challenged or rejected

This need not identify specific customers but demonstrates the CSP's accountability posture.

**Evidence for audit:**
- Sub-processor register (current, dated, accessible to customers)
- Advance notification records for sub-processor changes
- Service documentation or DPA schedule identifying data residency locations
- Transparency report (if published) or policy confirming CSP's approach

---

### Principle 8: Individual Participation and Access

**Obligation: Supporting data subject (PII principal) rights**

The CSP shall not impede a cloud service customer's ability to fulfil the rights of PII principals. Specific obligations:

**8a. Access to PII by CSP employees**
- Employee access to PII (including production data) shall be controlled, logged, and limited
- Routine service delivery shall not require CSP employees to access PII content
- Any access to customer PII by CSP staff (e.g. for troubleshooting) must be:
  - Authorised by the CSP's internal approval process
  - Notified to the cloud service customer where operationally practicable
  - Logged and subject to review

**8b. Supporting customer fulfilment of data subject rights**
- The CSP shall provide technical and administrative mechanisms enabling customers to respond to data subject requests (access, rectification, erasure, restriction, portability, objection)
- Export functions, deletion APIs, and data portability formats shall be documented and supported
- The CSP shall not charge unreasonable fees for assisting with data subject rights

**Evidence for audit:**
- Access log for CSP employee access to customer PII (with justification records)
- Product documentation of data export and deletion capabilities
- Customer support procedure for assisting with data subject rights requests

---

### Principle 9: Accountability

**Obligation: Dedicated contact, records of disclosures, and breach notification**

**9a. Dedicated point of contact for PII/privacy**
The CSP shall designate a specific named role (or team) responsible for PII protection matters:
- Contact details must be made available to cloud service customers
- The contact role must have authority to respond to PII queries, complaints, and regulatory enquiries
- The role may be a Data Protection Officer (DPO) under GDPR or an equivalent function

**9b. Records of disclosures to third parties**
- All disclosures of customer PII to third parties (mandatory or voluntary) shall be recorded in a disclosure register
- The register shall be available to customers on request (in whole or in redacted form)
- The register entry shall include: date, recipient, legal basis, data categories, and whether customer was notified

**9c. PII incident / data breach notification**
Where a security incident results in, or may result in, accidental or unlawful access to, loss, destruction, or alteration of PII, the CSP shall:
- Notify the affected cloud service customer without undue delay (many contracts specify 24–72 hours from discovery)
- Include in the notification: nature of the incident, categories and approximate volume of PII affected, likely consequences, measures taken or proposed
- Support customers in fulfilling their own breach notification obligations to supervisory authorities and PII principals
- Maintain an incident log with full details

**Evidence for audit:**
- Privacy/PII contact information published in service documentation
- Disclosure register (maintained, accessible)
- Incident notification procedure with defined timelines
- Evidence of breach notifications issued (anonymised/redacted for audit purposes)

---

### Principle 10: Information Security

**Obligation: Implementing documented PII security policies and providing transparency**

**10a. PII security policy**
The CSP shall implement a documented information security policy specifically addressing PII protection in its cloud environment:
- Policy must be approved by senior management
- Policy shall address: access control, encryption, logging, incident response, sub-processor requirements, and staff obligations
- Policy shall be reviewed at defined intervals (typically annually or following significant changes)

**10b. Making security information available to customers**
The CSP shall make available to cloud service customers sufficient information about its security practices to enable customers to:
- Assess whether security is appropriate for their risk profile
- Fulfil their own due diligence obligations (e.g. Article 28 GDPR assessments)
- Exercise their audit rights

Acceptable forms include: ISO 27001 certification, SOC 2 Type II reports, security whitepapers, public security pages, or direct audit access.

**Evidence for audit:**
- Documented PII security policy (current, approved, reviewed)
- Customer-facing security documentation (whitepaper, trust page, certification)
- Certification certificates (ISO 27001, SOC 2) with scope including PII processing

---

### Principle 11: Privacy Compliance

**Obligation: Disclosing applicable authorities and enabling customer audit rights**

**11a. Area of competent supervisory authority**
The CSP shall inform cloud service customers of:
- The countries and legal jurisdictions in which PII is processed
- The data protection supervisory authorities that have jurisdiction over its activities
- Any applicable international transfer mechanisms in use

This information enables customers to understand which regulations apply to their data and which authorities they could approach in the event of a complaint.

**11b. Enabling customer audit rights**
The CSP shall provide cloud service customers with practical means to verify that the CSP complies with its PII protection obligations. Options include:
- Third-party certification (ISO 27001, ISO 27018, SOC 2) with clearly defined scope
- Independent audit reports shared with customers under NDA
- Customer-conducted audits or inspections (subject to reasonable notice and security requirements)
- Self-assessment questionnaires (e.g. CSA CAIQ) completed and made available

**Evidence for audit:**
- Legal jurisdiction and transfer mechanisms documented in DPA or service schedule
- Customer contract clause granting audit rights
- Evidence portfolio ready for customer requests (certifications, reports, questionnaires)

---

## Summary Table — Annex A Control Areas

| Privacy Principle | Control Topic | Key Obligation |
|------------------|---------------|----------------|
| Consent and choice | Purpose limitation | No processing beyond customer instructions |
| Purpose limitation | No commercial use | No use for marketing or advertising without consent |
| Purpose limitation | Sub-processor purpose | Sub-processors bound to same purpose restrictions |
| Collection limitation | Change notification | Advance notice of material changes to processing |
| Collection limitation | Sub-processor information | Sufficient info for customer processing records |
| Data minimization | Temporary files | Identify and delete; apply same controls |
| Data minimization | Access minimization | Least privilege; access reviews; MFA for privileged access |
| Use/retention/disclosure | PII return and disposal | Return or securely delete all PII at contract end; written confirmation |
| Use/retention/disclosure | Disclosure notification | Notify customers of legally required disclosures (unless prohibited) |
| Use/retention/disclosure | Disclosure records | Maintain complete disclosure register |
| Accuracy and quality | Data correction support | Enable corrections; ensure deletion cascades |
| Openness/transparency | Sub-processor list | Maintain, disclose, and give advance notice of changes |
| Openness/transparency | Data residency | Disclose processing locations; notify changes |
| Openness/transparency | Law enforcement transparency | Publish transparency report where permitted |
| Individual participation | Employee access controls | Control, log, and limit CSP employee access to PII |
| Individual participation | Data subject rights support | Provide technical tools for customer to fulfil DSRs |
| Accountability | Dedicated PII contact | Named role with contact details available to customers |
| Accountability | Disclosure register | Record all third-party PII disclosures |
| Accountability | Breach notification | Notify customers without undue delay; support their obligations |
| Information security | PII security policy | Documented, approved, reviewed policy |
| Information security | Security transparency | Provide certifications/reports to customers |
| Privacy compliance | Supervisory authority | Disclose applicable authorities and jurisdictions |
| Privacy compliance | Customer audit rights | Practical means to verify compliance |

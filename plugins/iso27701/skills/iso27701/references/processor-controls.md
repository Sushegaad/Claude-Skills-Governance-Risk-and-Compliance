# ISO 27701 — PII Processor Controls (Clause 8)

All controls in Clause 8 are **normative** for organisations acting as PII Processors. They are additional to the ISO 27001 Annex A and ISO 27002 controls addressed in Clause 6.

A PII Processor is an entity that processes PII on behalf of and in accordance with the instructions of a PII Controller.

---

## Key Principle for PII Processors

A PII Processor must not process PII for its own purposes beyond what is documented in the controller's instructions. The processor's role is defined and bounded by the agreement with the controller. Where a processor wishes to use PII for its own purposes (e.g., service improvement, analytics, marketing), it must obtain the controller's authorisation or, where it processes PII collected directly from PII principals, act as a controller for that processing activity.

---

## 8.2 — Conditions for Collection and Processing

### 8.2.1 — Customer Agreement

**Objective:** Ensure every processing activity performed for a controller is governed by a binding written agreement.

**Requirement:**
The organisation shall ensure that processing of PII for each customer (PII Controller) is conducted only on the basis of a written agreement. The agreement must document the instructions under which the processor is permitted to process PII. The processor shall not exceed the instructions given by the controller.

**Contract provisions a PII Processor must ensure are in place:**
- Subject matter and duration of the processing
- Nature and purpose of the processing
- Type of PII and categories of PII principals
- Obligations and rights of the controller
- Processing limited to documented instructions
- Confidentiality obligation on all staff with access to PII
- Appropriate technical and organisational security measures
- Sub-processor requirements (see 8.5.6)
- Assistance with PII principal rights obligations (see 8.3)
- Deletion or return of PII at contract end
- Provision of evidence of compliance to the controller
- Breach notification to the controller (see 8.5.4)

**Evidence for audit:**
- Register of all controller customers with contract status
- Sample agreements confirming all required provisions are present
- Evidence that processing does not commence prior to agreement being in place

**GDPR:** Art. 28 (processor obligations)

---

### 8.2.2 — Organisation's Privacy Practices

**Objective:** Make the organisation's privacy commitments transparent to the marketplace and to PII Principals where applicable.

**Requirement:**
The organisation shall make available to its customers (PII Controllers) accurate and up-to-date information about its privacy practices, including its approach to security, sub-processors, and data location. Where the organisation has made public commitments (e.g., in a privacy notice, certification, or published data processing terms), it shall adhere to those commitments.

**What to implement:**
- Publish a public-facing privacy notice describing the organisation's role as a processor
- Maintain a sub-processor list and make it available to controllers under the agreement
- Publish or provide security commitments (e.g., certifications held, encryption standards, data centre locations)
- Maintain consistency between publicly stated privacy practices and actual practices — inconsistencies constitute non-compliance

**Evidence for audit:**
- Organisation's public-facing privacy documentation
- Sub-processor list with last review date
- Security commitment documentation / certifications
- Internal review confirming public statements match operational practice

---

### 8.2.3 — Marketing and Advertising

**Objective:** Prohibit use of PII held on behalf of a controller for the processor's own marketing or advertising purposes without explicit authorisation.

**Requirement:**
The organisation shall not use PII processed on behalf of PII Controllers for the purpose of marketing or advertising to PII principals, unless this is specifically authorised in the written agreement with the controller. This prohibition extends to using insights derived from controller-held PII to build the organisation's own customer profiles.

**What to implement:**
- Establish a documented policy prohibiting marketing use of controller PII without written authorisation
- Implement technical controls (access controls, system segregation) that prevent marketing systems from accessing controller PII
- Include marketing prohibition in staff training
- Audit for compliance with this control annually

**Evidence for audit:**
- Policy document prohibiting marketing use of controller PII
- Technical controls documented preventing cross-contamination of controller and marketing data stores
- Staff training records covering this prohibition
- Audit results confirming compliance

---

### 8.2.4 — Infringing Instruction

**Objective:** Establish a process for the organisation to identify and escalate when a controller instruction would require the processor to infringe applicable privacy law.

**Requirement:**
The organisation shall establish a procedure to assess customer instructions before execution. Where an instruction from a PII Controller would require the processor to process PII in a way that infringes applicable privacy law, the processor shall notify the controller, decline to execute the instruction (pending resolution), and document the issue.

**What to implement:**
- Establish a process for legal or compliance review of new or changed processing instructions
- Define escalation path when an infringing instruction is identified (legal / DPO review; controller notification)
- Include a clause in processor agreements informing the controller that infringements will be notified and not executed
- Maintain a log of infringing instructions received, actions taken, and outcomes

**Evidence for audit:**
- Infringing instruction procedure document
- Log of assessments conducted on new instructions (including clean assessments and any escalations)
- Sample controller notifications where infringing instructions were identified

**GDPR:** Art. 29 (processing under authority), Art. 28(3)(h) (processor obligations)

---

### 8.2.5 — Customer Obligations

**Objective:** Ensure customers (PII Controllers) are made aware of and accept their obligations under the processing relationship.

**Requirement:**
The organisation shall communicate to its customers the obligations that the controller must fulfil in order for the processor to deliver the service in a legally compliant manner. This includes ensuring the controller has a lawful basis for instructing the processing and that controller-side access is governed appropriately.

**What to implement:**
- Include controller obligations in the processing agreement (acceptable use clauses, requirement to have lawful basis, notification of changes to processing scope)
- Communicate to controllers what actions are needed from their side to maintain compliance (e.g., keeping processor-side access credentials managed, configuring data minimisation settings in the service)
- Provide documentation (e.g., shared responsibility matrix) clarifying the division of compliance obligations

**Evidence for audit:**
- Processing agreement sections covering controller obligations
- Shared responsibility documentation
- Customer onboarding or compliance guidance materials

---

## 8.3 — Obligations to PII Principals

### 8.3.1 — Obligations to PII Principals

**Objective:** Ensure the organisation supports the controller in fulfilling the privacy rights of PII principals.

**Requirement:**
The organisation shall assist the PII Controller in fulfilling its obligations to PII principals, including obligations arising from PII principal rights requests. The processor shall not respond directly to PII principal rights requests without the controller's authorisation, but shall cooperate with the controller to enable timely fulfilment.

**What to implement:**
- Document the procedure for receiving and routing PII principal rights requests that arrive at the processor (rare in B2B context, but possible)
- Implement mechanisms in the service that allow controllers to locate, export, rectify, or delete PII as required to respond to rights requests
- Contractually commit to responding to controller requests for PII principal rights assistance within a defined timeframe (e.g., within 5 business days)
- Log all rights assistance provided to controllers

**Evidence for audit:**
- Processing agreement provisions covering rights assistance obligations
- Technical capability documentation for PII access, export, rectification, and deletion in the service
- Audit of response times for rights assistance requests
- Log of rights assistance events

**GDPR:** Art. 28(3)(e) (processor must assist controller with rights obligations)

---

### 8.3.2 — Determine Information for PII Principals

**Objective:** Provide controllers with the information they need to meet their transparency obligations to PII principals.

**Requirement:**
The organisation shall provide its customers (PII Controllers) with accurate and complete information about the processor's processing activities, data locations, sub-processors, security measures, and retention so that controllers can fulfil their transparency obligations to PII principals (e.g., completing their own RoPA and privacy notices accurately).

**What to implement:**
- Provide a data processing information sheet or Data Processing Addendum (DPA) containing all relevant details
- Make information available about the locations where PII is processed and stored
- Maintain an up-to-date list of sub-processors and provide it to controllers on request
- Provide security overview documentation sufficient for controllers to describe measures in their privacy notices

**Evidence for audit:**
- Standard DPA or data processing information document provided to customers
- Sub-processor list with version history
- Process for notifying controllers of changes to processing locations or sub-processors

---

## 8.4 — Privacy by Design and Privacy by Default

### 8.4.1 — Limit Processing to Specified Purposes

**Objective:** Ensure PII processed on behalf of controllers is limited strictly to the purposes specified in the contract.

**Requirement:**
The organisation shall implement technical and organisational measures to ensure that PII processed on behalf of customers is not processed for purposes not authorised in the customer agreement. This applies to all staff with access to controller PII and to all internal systems that handle that PII.

**What to implement:**
- Implement role-based access controls restricting access to controller PII to roles with a defined need under the contract
- Segregate controller PII from internal operational data stores
- Log all access to controller PII and review for access outside expected parameters
- Include purpose limitation clauses in staff confidentiality agreements and training
- Conduct periodic access reviews to confirm no unauthorised use of controller PII

**Evidence for audit:**
- Access control configuration and RBAC model documentation
- Audit log review reports for controller PII access
- Staff training records and acknowledgements covering purpose limitation
- Segregation architecture documentation

**GDPR:** Art. 29 (processing under controller authority), Art. 5(1)(b) (purpose limitation applies to processor as an obligation)

---

### 8.4.2 — Data Minimisation Objectives for PII Processors

**Objective:** Apply data minimisation principles to the processing activities the organisation performs on behalf of controllers.

**Requirement:**
The organisation shall apply data minimisation within the scope of its processor operations. This includes:
- Not collecting or processing more PII than is specified in the controller's instructions
- Deleting or anonymising PII when the stated processing purpose is complete (unless the controller instructs otherwise)
- Implementing pseudonymisation or anonymisation where appropriate given the processing purpose

**What to implement:**
- Enforce that the service collects and processes only PII fields that are necessary for the contracted processing purpose
- Implement features or defaults that enable controllers to configure the service to collect minimal PII
- Apply automatic deletion / purging timelines within the service that align to controller-defined retention periods
- Document the data minimisation features of the service and communicate them to controllers

**Evidence for audit:**
- Data minimisation features documented in service specifications
- Service configuration documentation showing default minimal data collection settings
- Automatic deletion feature specifications and test evidence

---

## 8.5 — PII Sharing, Transfer and Disclosure

### 8.5.1 — Basis for PII Transfer Between Jurisdictions

**Objective:** Ensure transfers of controller PII between jurisdictions are conducted under lawful transfer mechanisms.

**Requirement:**
The organisation shall ensure that any transfer of controller PII to a country or international organisation outside the original jurisdiction is conducted under a lawful transfer mechanism, and that this mechanism is documented and disclosed to the controller.

**What to implement:**
- Document all data centre locations and processing locations where controller PII may reside
- Identify the applicable transfer mechanism for any cross-border processing (e.g., SCCs between the controller and processor, intra-group BCRs, adequacy decisions covering the processing country)
- Include transfer mechanisms in the processing agreement and DPA
- Conduct Transfer Impact Assessments for transfers to non-adequate countries where required

**Evidence for audit:**
- Data processing agreement with all processing locations listed
- Transfer mechanism documentation (e.g., signed SCCs, BCR binding documents)
- Transfer Impact Assessment records for non-adequate third country processing

**GDPR:** Art. 44–49

---

### 8.5.2 — Countries and International Organisations to Which PII Can Be Transferred

**Objective:** Maintain and disclose an accurate list of all countries and organisations to which controller PII may be transferred.

**Requirement:**
The organisation shall maintain an accurate list of all countries and international organisations to which controller PII may be transferred (including where sub-processors are located in other countries) and provide this information to controllers on request. The list must be updated when transfer destinations change.

**Implementation:**
- Maintain a transfer register listing all sub-processor countries and processing data centre locations
- Notify controllers in advance of any changes to transfer destinations (ideally providing the required notice period per contract, e.g., 30 days)
- Ensure the transfer register is reflected in the DPA and updated at each contract renewal

**Evidence for audit:**
- Transfer register with countries and applicable safeguards per destination
- Notification records for changes to transfer destinations
- Contract provisions specifying the notification requirement

---

### 8.5.3 — Records of PII Disclosures to Third Parties

**Objective:** Maintain a log of all disclosures of controller PII to third parties not covered by sub-processor agreements.

**Requirement:**
The organisation shall maintain records of any disclosures of PII it processes on behalf of controllers to third parties outside the sub-processor chain. These records support the controller's accountability obligations and must be available to the controller on request.

**Records to maintain:**
- Identity of the third party (recipient)
- Categories of controller PII disclosed
- Date and method of disclosure
- Legal basis for the disclosure (e.g., legal obligation, court order)
- Whether and when the controller was notified

**Evidence for audit:**
- Third-party disclosure log
- Controller notification records for each disclosure
- Process documentation for how disclosure requests are assessed and approved

---

### 8.5.4 — Notification of PII Disclosure Requests to the PII Controller

**Objective:** Promptly notify the controller when a third party (e.g., law enforcement, government) requests disclosure of controller PII.

**Requirement:**
Where the organisation receives a request from a third party (including law enforcement, regulatory authority, or court) for access to or disclosure of controller PII, it shall notify the controller as soon as practicable — unless legally prohibited from doing so. The processor shall not disclose PII in response to such a request without first notifying the controller (except where legally prohibited from notification or where notification is waived in the processing agreement).

**What to implement:**
- Document the procedure for handling government and law enforcement access requests
- Include controller notification as the default response to all such requests
- Where notification is legally prohibited (e.g., a statutory gag order), document the prohibition and the steps taken to contest it where possible
- Report annually (or as required in the agreement) transparency statistics on government access requests (number of requests received, number complied with, types of data involved)
- Include transparency reporting commitments in customer agreements where the controller requires this

**Evidence for audit:**
- Government / law enforcement access request procedure
- Log of access requests received with notification status
- Transparency report (if published or provided to customers)
- Legal analysis supporting notification prohibition in cases where notification was withheld

**Note (Cloud providers):** This control is particularly relevant for cloud service providers subject to foreign government access laws (e.g., US CLOUD Act, US FISA). Processors should have conducted a Transfer Impact Assessment addressing government access risk when processing EU/UK controller PII.

---

### 8.5.5 — Legally Binding PII Disclosure Requests

**Objective:** Establish a process for responding to legally binding requests for PII in a manner that protects PII principals' rights and preserves controller notification.

**Requirement:**
Where the organisation determines that a disclosure request is legally binding and compliance is required, it shall:
1. Notify the controller before complying (unless legally prohibited)
2. Comply with the request only to the extent legally required
3. Disclose only the minimum PII necessary to satisfy the legal requirement
4. Document the legal basis for disclosure, the PII disclosed, and the recipient

**Implementation:**
- Engage legal counsel before responding to any compelled disclosure request
- Implement a review process to assess the validity and scope of the request
- Apply data minimisation — do not disclose more than required
- Log all legally compelled disclosures with full details

**Evidence for audit:**
- Compelled disclosure procedure
- Legal review records for past disclosure requests
- Disclosure log entries for legally compelled disclosures
- Evidence of controller notification (or documented legal prohibition on notification)

---

### 8.5.6 — Disclosure Based on Sub-Processor Contracts

**Objective:** Ensure that PII shared with sub-processors is governed by binding agreements that impose equivalent obligations to those the processor has with the controller.

**Requirement:**
The organisation shall not engage sub-processors to process controller PII without the controller's prior written authorisation (general or specific, as agreed in the processing agreement). For each sub-processor engaged, the organisation shall ensure a written agreement is in place that imposes on the sub-processor the same data protection obligations as those in the processor-controller agreement. The organisation remains fully liable to the controller for the compliance of its sub-processors.

**What to implement:**
- Obtain and document written authorisation from the controller for each sub-processor (or general authorisation with notification mechanism for changes)
- Execute a sub-processor agreement with each sub-processor containing all required provisions
- Conduct due diligence of sub-processors' privacy and security practices before engagement
- Maintain an up-to-date sub-processor list and notify controllers of changes (with the notice period specified in the agreement)
- Include a right to object to new sub-processors in customer agreements
- Monitor sub-processor compliance through contractual audit rights, certifications, or assessments

**Evidence for audit:**
- Sub-processor register with authorisation status per customer
- Sample sub-processor agreements confirming equivalent obligations
- Sub-processor due diligence records
- Customer notification records for new sub-processor additions
- Sub-processor monitoring schedule and compliance reports

**GDPR:** Art. 28(2) (sub-processor authorisation), Art. 28(4) (sub-processor obligations)

---

## Clause 8 Summary Table — Quick Reference

| Control | ID | Applies When | Key Obligation |
|---------|-----|-------------|----------------|
| Customer agreement | 8.2.1 | Always (PII Processor) | Written contract in place before processing; all required provisions included |
| Organisation's privacy practices | 8.2.2 | Always (PII Processor) | Public privacy commitments accurate and consistently applied |
| Marketing and advertising | 8.2.3 | Always | No use of controller PII for own marketing without authorisation |
| Infringing instruction | 8.2.4 | Always | Process for identifying and declining infringing controller instructions |
| Customer obligations | 8.2.5 | Always | Controllers informed of their obligations under the processing relationship |
| Obligations to PII principals | 8.3.1 | Always | Mechanisms to assist controller with PII principal rights fulfilment |
| Determine information for PII principals | 8.3.2 | Always | Provide controllers with processing details needed for transparency |
| Limit processing to specified purposes | 8.4.1 | Always | Technical and organisational controls enforcing purpose limitation |
| Data minimisation objectives | 8.4.2 | Always | Minimisation applied to processor operations; features to support controller minimisation |
| Basis for PII transfer between jurisdictions | 8.5.1 | Cross-border processing | Lawful transfer mechanism documented for each jurisdiction |
| Countries and organisations for transfer | 8.5.2 | Cross-border processing | Up-to-date transfer register; controller notified of changes |
| Records of disclosures to third parties | 8.5.3 | All ad-hoc disclosures | Disclosure log maintained; controller notified |
| Notification of disclosure requests | 8.5.4 | Government/LE access requests | Controller notified before compliance unless legally prohibited |
| Legally binding disclosure requests | 8.5.5 | Compelled disclosures | Legal review; minimum necessary disclosed; controller notified |
| Sub-processor contracts | 8.5.6 | Sub-processors engaged | Controller authorisation; equivalent contractual obligations; sub-processor list maintained |

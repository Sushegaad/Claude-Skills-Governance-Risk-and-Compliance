# ISO 27701 PIMS Overview — Framework, Context, and Clause 6 Guidance

## 1. What Is a Privacy Information Management System (PIMS)?

A Privacy Information Management System (PIMS) is a management system that extends an Information Security Management System (ISMS) to include privacy-specific requirements and controls. The PIMS governs how an organisation identifies, manages, and controls the processing of Personally Identifiable Information (PII) throughout its operations.

ISO/IEC 27701:2019 defines the requirements and provides guidance for establishing, implementing, maintaining, and continually improving a PIMS. It operates as an **extension** to ISO/IEC 27001; it cannot be implemented or certified independently.

---

## 2. Scope and Applicability

### When ISO 27701 Applies
- Any organisation that processes PII, regardless of size, sector, or jurisdiction
- Organisations that are PII Controllers (determine purposes and means of processing)
- Organisations that are PII Processors (process on behalf of a controller)
- Organisations that function as both simultaneously (e.g., an enterprise that processes employee PII as a controller and customer data as a processor for another entity)

### Defining the PIMS Scope (Clause 5.2.3)
The PIMS scope must be defined and documented. It must include:

1. **Types of PII processed** — Categories of personal information in scope
2. **PII principals** — Data subjects whose PII is processed (e.g., customers, employees, job applicants, website visitors)
3. **Processing purposes** — All stated purposes for which PII is processed
4. **Controller/Processor role** — Whether the organisation acts as PII Controller, PII Processor, or both in the scope
5. **Applicable privacy laws and regulations** — List all legal requirements in scope (e.g., GDPR, UK GDPR, CCPA, LGPD, PDPA)
6. **Geographic extent** — Jurisdictions in which PII is collected, processed, or transferred
7. **Organisational boundaries** — Business units, functions, or systems included/excluded from scope
8. **PII lifecycle** — From collection through to deletion/archival

**Scope alignment with ISO 27001:** The PIMS scope should align with or be a subset of the ISMS scope. If the PIMS scope is narrower, this must be justified and documented.

---

## 3. Context of the Organisation — PIMS Extensions (Clause 5.2.1–5.2.2)

### Understanding the Organisation (5.2.1)
In addition to the ISO 27001 context analysis, the organisation must consider:
- Applicable privacy laws, regulations, and contractual obligations relating to PII processing
- The organisation's relationship with PII as controller and/or processor
- The nature of PII categories being processed and associated sensitivities
- Locations where PII is stored, processed, and transmitted (including cloud regions)

### Interested Parties (5.2.2)
For PIMS purposes, interested parties specifically include:
- PII principals (data subjects) — the individuals whose PII is processed
- Supervisory/regulatory authorities (e.g., ICO, CNIL, EDPB, state attorneys general)
- PII processors engaged by the organisation (if acting as a controller)
- Joint PII controllers (if applicable)
- PII controllers the organisation processes data for (if acting as a processor)
- Sub-processors engaged by the organisation (if acting as a processor)
- Law enforcement and government agencies (in the context of lawful disclosure requests)
- Certification bodies conducting PIMS audits

---

## 4. Leadership and Privacy Policy (Clause 5.3)

### Top Management Commitment (5.3.1)
Top management must:
- Establish and maintain the privacy policy
- Communicate the importance of effective privacy management throughout the organisation
- Ensure resources are allocated for the PIMS
- Direct relevant personnel to apply the PIMS requirements
- Promote continual improvement of the PIMS
- Support other management roles in demonstrating their leadership in privacy matters

### Privacy Policy (5.3.2)
The privacy policy must:
- Be appropriate to the purpose and context of the organisation
- Include a commitment to satisfy applicable privacy laws and contractual obligations
- Include a commitment to continual improvement of the PIMS
- Be made available to PII principals and other relevant interested parties as appropriate
- Be communicated internally to all personnel

**Note:** Most organisations maintain two distinct documents:
- An **external privacy notice** (communicated to PII principals per Art. 13/14 of GDPR) which describes what data is processed, why, and what rights data subjects have
- An **internal privacy/data protection policy** (for staff) which describes how the organisation implements its privacy commitments

Both documents derive from the top-level privacy policy commitment. The external notice must meet legal disclosure requirements; the internal policy establishes operational obligations.

### Roles and Responsibilities (5.3.3)
Privacy-specific roles that must be defined:
- **Privacy Officer / Data Protection Officer (DPO):** Where legally required (e.g., GDPR Art. 37), a DPO must be formally appointed. ISO 27701 does not mandate a DPO but requires that privacy responsibilities are allocated.
- **PII Stewards / Data Owners:** Business owners accountable for specific processing activities and PII categories
- **PIMS Manager:** Responsible for the day-to-day operation and improvement of the PIMS
- **Privacy Champion Network:** (Best practice) Embedded privacy contacts within business functions

The roles and their responsibilities must be documented and communicated across the organisation.

---

## 5. Planning — Privacy Risk Assessment and Objectives (Clause 5.4)

### Privacy Risk Assessment (5.4.1)
ISO 27701 extends the ISO 27001 risk assessment process to include privacy-specific risks:
- Risks to PII principals (not just to the organisation) — this is a key difference from a purely security-focused risk assessment
- Privacy risks arising from new or changed processing activities
- Risks related to each processing purpose and PII category
- Context-specific risks (e.g., processing special category PII, processing PII of children, cross-border processing)

**Privacy risk factors to consider:**
- Volume of PII principals affected
- Sensitivity of PII categories (special categories require heightened scrutiny)
- Processing that could result in physical, material, or non-material harm to PII principals
- Profiling and automated decision-making
- Processing in a new context or novel technology

### Privacy Impact Assessment Triggers (5.4.1, 7.2.5)
A PIA must be conducted before any new or significantly changed processing that may result in high risk to PII principals. Mandatory triggers include:
- Systematic and extensive profiling with significant effects
- Large-scale processing of special category PII
- Systematic monitoring of public areas
- Use of new technologies involving PII
- Any processing likely to significantly affect individuals' rights and freedoms

### Privacy Objectives (5.4.2)
Privacy objectives must be:
- Consistent with the privacy policy
- Measurable where practicable
- Communicated to relevant personnel
- Monitored and updated
- Include criteria for evaluating PIMS performance

**Example privacy objectives:**
- Achieve 100% consent renewal within 30 days of policy change
- Respond to all PII principal rights requests within the legally required timeframe
- Conduct PIAs for 100% of qualifying new processing activities before go-live
- Complete annual privacy training for 100% of PII-handling staff
- Achieve zero critical findings in annual PIMS internal audit
- Report all privacy incidents within required notification timelines

---

## 6. Support — Competence, Awareness, Communication (Clause 5.5)

### Competence
Persons doing work that affects PIMS performance must be competent. This includes:
- Privacy officers and DPOs — formal privacy qualifications or equivalent experience
- Staff processing PII in their work — role-specific privacy training covering their obligations
- IT staff designing or managing systems that process PII — privacy by design training
- Legal and compliance staff — knowledge of applicable privacy laws

Competence evidence: training records, certifications, CVs, attendance logs.

### Privacy Awareness
All personnel processing PII must be aware of:
- The privacy policy and what it means for their role
- The PIMS objectives and their contribution to them
- The implications of not conforming with PIMS requirements
- How to report privacy incidents and suspected breaches
- PII principal rights and how to route requests

### Communication
The organisation must determine what privacy-related communications are needed, when, with whom, and by what method. Relevant communications:
- Privacy notices to PII principals (transparency obligation)
- Internal privacy updates/newsletters
- Notification to processors of relevant changes
- Breach notifications to supervisory authorities and PII principals (if applicable)
- Regular privacy performance reports to top management

---

## 7. Operation — Key PIMS Operational Processes (Clause 5.6)

### Operational Planning and Control (5.6.1)
The PIMS requires the following operational processes to be documented and in place:

1. **PII inventory management:** Maintain an up-to-date inventory of all PII and processing activities (supports 7.2.8, 7.2.9)
2. **PIA process:** Documented procedure for conducting and managing PIAs
3. **Consent management:** Processes for obtaining, recording, and withdrawing consent
4. **PII principal rights fulfilment:** Procedures for each applicable right with defined response timelines
5. **Privacy incident management:** Detection, containment, investigation, notification
6. **Processor management:** Contracting, oversight, and audit of PII processors and sub-processors
7. **Cross-border transfer management:** Identifying, authorising, and documenting transfers outside the jurisdiction
8. **Retention and deletion:** Enforcing retention schedules and secure disposal of PII

### Privacy Risk Assessment Execution (5.6.2)
At planned intervals and when significant changes occur, the organisation must:
- Re-execute the privacy risk assessment
- Document results
- Update the risk treatment plan to reflect current risks

### Privacy Risk Treatment (5.6.3)
Risk treatment for privacy risks must:
- Select appropriate controls from Clause 7 (controller) and/or Clause 8 (processor)
- Supplement with ISO 27002/27001 Annex A controls where relevant
- Produce a privacy risk treatment plan
- Obtain approval from accountable owners
- Implement treatments and verify effectiveness

---

## 8. Performance Evaluation (Clause 5.7)

### Monitoring and Measurement
Privacy-specific monitoring must include:
- Compliance with privacy objectives (metric tracking)
- PII principal rights request fulfilment rate and timeliness
- Privacy incident count and severity trends
- Privacy training completion rates
- PIA completion rate (qualifying processing activities vs. those with a completed PIA)
- Processor compliance status
- Open corrective actions ageing

### Internal PIMS Audit
The internal audit programme must include PIMS scope:
- Audit against all applicable Clause 5 extensions
- Audit against applicable Clause 7 controls (if controller)
- Audit against applicable Clause 8 controls (if processor)
- Audit against ISO 27001 base requirements (the ISMS serves as the foundation)

Internal auditors for PIMS activities should have privacy competence (not solely security audit competence).

### Management Review
Management review must include privacy-specific agenda items:
- Privacy performance metrics
- Status of open privacy risk treatments
- Privacy incident trends
- Regulatory developments affecting the PIMS
- Customer/PII principal complaints relating to privacy
- PIMS audit results and corrective actions
- Opportunities for improvement in the PIMS

---

## 9. Clause 6 — PIMS-Specific Guidance for ISO/IEC 27002 Controls

Clause 6 of ISO 27701 provides **informative** (non-normative) guidance that supplements selected ISO 27002:2013 controls with privacy-specific considerations. The guidance applies to both PII Controllers and PII Processors unless qualified. Below is a summary of the most significant areas.

### Information Security Policies (ISO 27002: 5.1)
**PIMS guidance:** The information security policy context must address the organisation's privacy commitments. The privacy policy (5.3.2) may be published as a separate document or as part of the IS policy suite, but must address PII-related commitments distinctly.

### Organisation of Information Security — Roles (ISO 27002: 6.1)
**PIMS guidance:** Privacy roles must be defined alongside information security roles. Where a DPO is required by law, this requirement must be reflected in the ISMS/PIMS role structure. Confidentiality agreements with personnel should include privacy obligations.

### Human Resource Security (ISO 27002: 7)
**PIMS guidance:** Pre-employment screening should consider access to PII. Employment terms must include privacy obligations. Termination procedures must address PII access revocation and return/deletion of PII held by departed staff.

### Asset Management (ISO 27002: 8)
**PIMS guidance:** The asset inventory must identify assets that store or process PII. PII classification must be aligned with the organisation's data classification scheme. Owner accountability for PII assets must be assigned.

### Access Control (ISO 27002: 9)
**PIMS guidance:** Access to PII must follow the principle of least privilege. User access rights to PII systems must be reviewed regularly. Privileged access to PII must be strictly controlled and logged.

### Cryptography (ISO 27002: 10)
**PIMS guidance:** Encryption of PII at rest and in transit is a key privacy-protective measure. Key management procedures must cover PII encryption keys. Anonymisation and pseudonymisation of PII should be considered where appropriate.

### Physical and Environmental Security (ISO 27002: 11)
**PIMS guidance:** Physical access to areas processing PII must be controlled. Physical media containing PII must be secured. Clear desk / clear screen policies must cover PII documents.

### Operations Security (ISO 27002: 12)
**PIMS guidance:** Logging and monitoring must capture access to PII to support accountability. Separation of environments must prevent PII from test/development environments unless appropriately anonymised. Backup procedures must address PII protection and retention alignment.

### Communications Security (ISO 27002: 13)
**PIMS guidance:** Network controls must address segregation of PII processing systems. Information transfer policies must include requirements for PII transfer security.

### System Acquisition, Development and Maintenance (ISO 27002: 14)
**PIMS guidance:** Privacy by design requirements must be integrated into systems development. PIAs should be embedded into the SDLC at design stage. Test environments must not use live PII unless justified and anonymised.

### Supplier Relationships (ISO 27002: 15)
**PIMS guidance:** Supplier agreements must include privacy contractual clauses (equivalent to DPA under GDPR). Supplier assessments must include evaluation of privacy practices. Sub-processor chains must be disclosed to the controller.

### Information Security Incident Management (ISO 27002: 16)
**PIMS guidance:** Privacy incident classification must be defined. Notification timelines for PII breaches must reflect regulatory requirements (e.g., 72-hour notification under GDPR Art. 33). Incidents affecting PII principals must trigger appropriate communication procedures.

### Business Continuity Management (ISO 27002: 17)
**PIMS guidance:** Business continuity plans must address availability of PII-processing systems. BCP must not compromise PII protection during recovery. Backup media containing PII must be secured during recovery operations.

### Compliance (ISO 27002: 18)
**PIMS guidance:** Legal and regulatory compliance reviews must include privacy law. PIAs serve as evidence of compliance with Art. 35 DPIA requirements where applicable. Independent reviews of the PIMS should be scheduled as part of the compliance review process.

---

## 10. Relationship to ISO 27001:2022

ISO 27701:2019 was written against ISO 27001:2013. Organisations implementing ISO 27001:2022 should:

1. Apply the Clause 5 extensions to the equivalent ISO 27001:2022 clauses (the numbering and intent are aligned; 2022 added Clauses 6.3 and split 9.2/9.3 but did not remove content)
2. Note that the new ISO 27001:2022 Annex A includes A.5.34 "Privacy and protection of PII" and A.8.11 "Data masking" — these have direct PIMS relevance
3. The 27 controls that were merged or consolidated in the 2022 Annex A transition do not remove any PIMS obligations — Clause 7 and Clause 8 controls are independent of this
4. Anticipate a future revision of ISO 27701 that will align to ISO 27001:2022 and ISO 27002:2022; as of 2024 the 2019 version remains the current published standard

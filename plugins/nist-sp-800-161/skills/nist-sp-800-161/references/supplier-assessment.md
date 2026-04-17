# NIST SP 800-161 Rev 1 — Supplier Assessment, Contract Clauses, and SBOM Requirements

**Source**: NIST SP 800-161 Rev 1, May 2022, Sections 3.5, 3.6, Appendix B

---

## Supplier Risk Tiering Criteria

Before conducting a supplier assessment, classify the supplier into a risk tier:

### Tier Classification Worksheet

Score the supplier on each factor (0 = lower risk, 1 = moderate risk, 2 = higher risk):

| Factor | 0 | 1 | 2 |
|---|---|---|---|
| Geography of operations | US-only design and manufacturing | Allied nation manufacturing | Nations with known state-sponsored ICT threats |
| Ownership | US public company | Allied nation private company | Partially or wholly owned by adversary-nation entity |
| Prior security incidents | No known incidents | Incidents disclosed and remediated | Incidents not disclosed or unresolved |
| Certifications | ISO 27001 / CMMC Level 2+ / SOC 2 Type II | ISO 27001 in progress or equivalent | No relevant security certification |
| Visibility into sub-tier suppliers | Full sub-tier transparency | Partial visibility | No visibility into sub-tier |
| Single-source dependency | Multiple qualified suppliers exist | Limited alternatives | Sole source; no alternative |
| Component sensitivity | Commodity; non-security-relevant | System component; moderate sensitivity | Security function; cryptographic; directly mission-critical |

**Score interpretation**:
- 0–4: Low risk tier — standard due diligence
- 5–8: Moderate risk tier — documentation review and certifications check
- 9–11: High risk tier — questionnaire, reference checks, third-party assessment
- 12–14: Critical risk tier — full assessment including on-site audit

---

## Supplier Assessment Questionnaire (Abbreviated)

### Section 1 — Security Programme

1.1 Does your organisation have a documented and approved information security policy?
- Yes / No / In progress

1.2 Has your organisation completed a recent information security risk assessment?
- Yes (date: ___) / No

1.3 Does your organisation hold any of the following certifications? (Check all that apply)
- [ ] ISO 27001 (expiry date: ___)
- [ ] SOC 2 Type II (report date: ___)
- [ ] CMMC Level 2
- [ ] CMMC Level 3
- [ ] Other (specify): ___

1.4 Provide a contact for your organisation's information security programme:
- Name / Title / Email / Phone

### Section 2 — Secure Development/Manufacturing

2.1 Do you follow a documented secure development lifecycle (SDL) for software products?
- Yes / No / In progress

2.2 Do you perform static application security testing (SAST) or dynamic application security testing (DAST) on products delivered to customers?
- SAST only / DAST only / Both / Neither

2.3 Do you generate and provide an SBOM (Software Bill of Materials) for your software products?
- Yes, SPDX format / Yes, CycloneDX format / Yes, other format / In progress / No

2.4 Do you sign your software releases cryptographically?
- Yes, with code signing certificate / Yes, with PGP/GPG / No

2.5 For hardware products: do you maintain a bill of materials for major components including country of origin?
- Yes / No / Partial

2.6 Do you use authorised distribution channels only for procuring components used in products delivered to customers?
- Yes / No / Not applicable (software only)

### Section 3 — Sub-Tier Supplier Management

3.1 Do you maintain an inventory of your significant sub-tier suppliers?
- Yes / No

3.2 Do you flow down cybersecurity and supply chain security requirements to your sub-tier suppliers?
- Yes, in contract terms / Yes, informally / No

3.3 Do you conduct assessments of your critical sub-tier suppliers?
- Yes / No

3.4 Will you provide the procuring organisation with a list of sub-tier suppliers upon request?
- Yes / No / With restrictions

### Section 4 — Incident Response and Notification

4.1 Does your organisation have a documented incident response plan?
- Yes / No

4.2 In the event of a security incident affecting products or services delivered to customers, will your organisation notify affected customers within 72 hours of discovery?
- Yes / No / Subject to legal review

4.3 Will your organisation notify customers of critical and high vulnerabilities discovered in delivered products within 72 hours?
- Yes / No

4.4 Will your organisation provide advance notification (minimum 12 months where practicable) of product end-of-life?
- Yes / No / Best effort

### Section 5 — Physical Security

5.1 Are your development and manufacturing facilities secured with access controls (badges, biometrics, CCTV)?
- Yes / Partial / No

5.2 Do you conduct background checks on personnel with access to customer-sensitive components or source code?
- Yes, all such personnel / Yes, selected personnel / No

5.3 Do you have an insider threat programme or equivalent controls?
- Yes / No / In development

---

## C-SCRM Contract Clauses

The following clauses should be incorporated into contracts for critical and high-risk acquisitions. Legal counsel must review before use.

### Clause 1 — Security Requirements Flow-Down

"Contractor shall incorporate cybersecurity and supply chain risk management requirements into its contracts and agreements with subcontractors and suppliers at all tiers that provide components, software, or services incorporated into deliverables under this contract. Contractor shall ensure that subcontractors and suppliers comply with requirements substantially equivalent to those imposed on Contractor by this contract. Contractor shall provide [Agency] with a list of significant subcontractors and suppliers upon request."

### Clause 2 — Notification of Security Incidents and Vulnerabilities

"Contractor shall notify [Agency Point of Contact] within 72 hours of discovery of any security incident or significant vulnerability affecting products or services delivered under this contract. Notification shall include: (a) description of the incident or vulnerability; (b) products and versions affected; (c) potential impact on [Agency] systems; (d) any compensating controls or workaround available; (e) timeline for patch or remediation. Contractor shall provide a follow-up written report within seven calendar days."

### Clause 3 — Notification of Significant Changes

"Contractor shall notify [Agency] at least 30 calendar days in advance of any significant change to its development, manufacturing, or delivery environment that may affect the security of products or services provided under this contract, including but not limited to: changes to development or build infrastructure; changes to significant subcontractors or suppliers for critical components; mergers, acquisitions, or changes in ownership; introduction of new geographic manufacturing locations."

### Clause 4 — End-of-Life Notification

"Contractor shall notify [Agency] no less than 12 months in advance of the end-of-support date for any product supplied under this contract. Notification shall include: (a) the anticipated end-of-support date; (b) recommended replacement or migration path; (c) any extended support options available and associated terms."

### Clause 5 — Authenticity and Integrity of Deliverables

"Contractor warrants that all hardware components delivered under this contract are genuine, new (unless otherwise specified), and sourced from the original equipment manufacturer or an authorised distributor. Contractor warrants that all software delivered under this contract is genuine, unmodified from the developer's release, and free of known malicious code as of the date of delivery. Contractor shall provide, upon request, documentation supporting these warranties including supplier chain of custody records."

### Clause 6 — Software Bill of Materials

"For software products delivered under this contract, Contractor shall provide a Software Bill of Materials (SBOM) in [SPDX / CycloneDX] format covering all components incorporated into the deliverable. The SBOM shall meet the minimum data requirements established by NTIA and shall be provided within [30] calendar days of contract award for existing products and at initial delivery for new development. Contractor shall update the SBOM within [30] calendar days of any software update delivered under this contract."

### Clause 7 — Right to Audit

"[Agency] reserves the right, upon reasonable notice (not less than [30] calendar days except in cases of documented urgent concern), to audit Contractor's security practices as they relate to products and services provided under this contract. Audits may include: review of security documentation; interviews with security personnel; and inspection of relevant facilities. Contractor shall cooperate with and facilitate such audits at no additional cost to [Agency]."

### Clause 8 — Change in Ownership

"Contractor shall notify [Agency] within [30] calendar days of any proposed or completed merger, acquisition, change in controlling ownership, or significant new foreign investment in Contractor or any entity in Contractor's supply chain that may materially affect performance or the security posture of deliverables under this contract. [Agency] reserves the right to review and respond to such changes, including requiring additional security assessments."

---

## SBOM Requirements Specification

### When to Require SBOMs

SBOMs should be required as contract deliverables when:
- The acquisition is for software-intensive systems (EO 14028 scope)
- The system or component performs a security function
- The system or component has internet connectivity or processes sensitive data
- The acquisition is for critical infrastructure or high-impact systems

### SBOM Minimum Data Fields (per NTIA June 2021 Minimum Elements)

| Field | Required | Format |
|---|---|---|
| Supplier Name | Yes | Legal entity name |
| Component Name | Yes | Name as designated by supplier |
| Version of the Component | Yes | Version string |
| Other Unique Identifiers | Yes | CPE, Package URL (purl), or SWID tag |
| Dependency Relationship | Yes | Describes containment or dynamic link relationship |
| Author of SBOM Data | Yes | Entity that generated the SBOM |
| Timestamp | Yes | ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ |

### Recommended Additional Fields

| Field | Description |
|---|---|
| Hash | Cryptographic hash (SHA-256 preferred) of the component |
| License information | SPDX license identifier for the component |
| Known vulnerabilities | CVE references at time of generation |
| Download location | URL or repository where component was obtained |

### SBOM Delivery Requirements

- Format: SPDX (ISO 5962) or CycloneDX preferred
- Machine-readable: JSON or XML format required
- Delivery: provided at initial product delivery; updated with each release
- Retention: [Agency] retains SBOM for the operational life of the system
- Confidentiality: if SBOM contains sensitive supplier information, mark appropriately and share via secure channel

### SBOM Consumption

When an SBOM is received, the C-SCRM programme manager or ISSO should:
1. Ingest the SBOM into the organisation's SBOM management tool or vulnerability management system
2. Cross-reference components against the National Vulnerability Database (NVD) for known CVEs
3. Identify critical or sensitive components warranting enhanced monitoring
4. Retain SBOM in the system provenance record
5. Establish a process to re-check SBOM components against NVD at regular intervals (e.g., daily automated scan)

---

## Critical Component Identification Worksheet

Use this worksheet to identify and classify components requiring enhanced C-SCRM treatment:

| Component | Function | Sensitivity | Single Source | Foreign Content | Criticality Level |
|---|---|---|---|---|---|
| [Component name] | [Security function / mission function / data processing] | [High / Medium / Low] | [Yes / No] | [Yes: country / No] | [Critical / High / Moderate / Low] |

Scoring guidance:
- High sensitivity + security function + single source = Critical
- High sensitivity + mission function = High
- Medium sensitivity + commercial availability = Moderate
- Low sensitivity + commodity = Low

**Critical designation triggers mandatory**:
- Enhanced provenance documentation (SR-4)
- Supplier assessment at Critical tier (SR-6)
- SBOM requirement (SR-5)
- Periodic inspection (SR-10)
- Anti-counterfeiting measures (SR-11)
- Disposal via secure destruction (SR-12)

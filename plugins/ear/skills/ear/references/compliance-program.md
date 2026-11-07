# EAR Export Compliance Programme, Enforcement, and Special Rules

## Export Compliance Programme (ECP) — BIS Seven Elements

BIS has identified seven elements of an effective Export Compliance Programme. Companies with strong ECPs receive significant penalty mitigation in enforcement actions.

### Element 1 — Management Commitment

- Senior leadership (CEO/CISO/CCO level) must visibly champion export compliance
- Written, board-approved export compliance policy signed by senior officer
- Compliance resources: dedicated ECP staff, compliance counsel, budget
- Export Control Officer (ECO) or Export Compliance Manager designated in writing
- Annual certification to the board that the ECP is operating effectively

**Best practice:** Quarterly compliance reporting to senior leadership; annual ECP review with documented findings

### Element 2 — Risk Assessment

- Identify all products, software, and technology subject to EAR
- Classify each item: ECCN or EAR99 (document the classification rationale)
- Identify all business units, geographies, and transaction types
- Assess risks: customers in D/E country groups, distributors with high-risk channels, end-use certificates accuracy
- Maintain a classification database tied to product lifecycle (new products re-classified before launch)

**ECCN classification log fields:** Item description, part number, technical parameters reviewed, ECCN assigned, RFC codes, date of classification, classifier name, review date

### Element 3 — Written Policies and Procedures

- Written, procedure-level guidance for each process that touches exports:
  - Customer onboarding and restricted party screening
  - Order acceptance and fulfilment (sales, finance, logistics)
  - ECCN classification and update trigger
  - Licence application and management
  - Employee travel with controlled items/technology
  - Hiring of foreign nationals (deemed export screening)
  - Distributor/reseller programme requirements
- Procedures must address digital transactions (cloud, SaaS, APIs) and source code repositories

### Element 4 — Training and Awareness

- Mandatory training for all employees who may touch controlled transactions: sales, engineering, operations, HR (foreign national hiring), finance, legal
- Role-based training depth: frontline sales (awareness); ECO/lawyers (deep dive)
- Annual refresher training with sign-off acknowledgement
- Training records retained for 5 years
- Training content must cover: EAR basics, ECCN/EAR99, restricted parties, red flag recognition, deemed exports, reporting obligations

**Topics for engineers and developers:**
- Deemed exports: sharing controlled source code with foreign national colleagues
- Cloud platforms and access controls for controlled technology
- Open-source publication — fundamental research exemption vs. EAR controls on software

### Element 5 — Restricted Party Screening

- Screen **all parties** to every transaction: buyer, end-user, intermediate consignee, freight forwarder, bank, broker
- Minimum lists to screen against:
  - BIS Denied Persons List
  - BIS Entity List
  - BIS Unverified List
  - BIS Military End-User (MEU) List
  - State Department Debarred List (DDTC)
  - OFAC SDN List
  - OFAC Consolidated Sanctions List
- **Consolidated Screening List (CSL):** trade.gov/consolidated-screening-list — single search covers BIS + State + Treasury
- Screen at time of: quote/order acceptance, before each shipment, and when parties change

**Affiliates Rule (ownership screening):** The BIS interim final rule "Expansion of End-User Controls To Cover Affiliates of Certain Listed Entities" (90 FR 47201, published September 30, 2025, effective September 29, 2025) extends Entity List/MEU List (and certain SDN) license requirements to entities 50 percent or more owned, directly or indirectly, individually or in aggregate, by listed parties (OFAC-style 50 percent standard). The rule is stayed: a one-year stay (90 FR 50857, effective November 10, 2025) ran through November 9, 2026, and was extended to January 10, 2027 (FR Doc 2026-22793, filed November 5, 2026, effective November 9, 2026, no substantive changes). Build ownership screening of counterparties tied to listed entities into the screening workflow before January 10, 2027.

**Screening cadence for ongoing relationships:**
- Re-screen existing distributors and customers at minimum **monthly** (list updates are continuous)
- Automate screening via ERP integration (SAP GTS, Oracle AGIS, Visual Compliance, Restricted Party Screening tools)

**Handling a match:**
1. Do not ship or service the order
2. Escalate to ECO/legal immediately
3. Determine if the match is a true hit or false positive (similar name, different entity)
4. If true hit: refuse the transaction; do not tip off the customer (no "tipping off" problem under EAR as severe as OFAC, but standard practice)
5. Document the match, review, and outcome

### Element 6 — Due Diligence (Know Your Customer)

- Know-Your-Customer (KYC) process for new distributors, resellers, and high-risk end-users
- For high-risk transactions, obtain:
  - **End-User Statement (EUS):** Certified statement of intended end-use, end-user identity, and location of end-use
  - **Importer Safety Zone (ISZ) Statement** for certain dual-use items
  - **Distributor Management: assurances that downstream sales comply with EAR**
- Red flag investigation: BIS publishes 15 "red flags" in Supplement 3 to Part 732; document your review and conclusions
- **Distributors in high-risk territories (D:1 countries):** Site visits, supply chain audits, enhanced due diligence on sub-distributors

### Element 7 — Recordkeeping and Audits

- Retain all export-related records for **5 years** from the date of export (§ 762.6)
- Records include: orders, invoices, bills of lading, Shipper's Export Declarations, EEI filings, classification records, screening records, licence applications and approvals, end-user statements, licence exception documentation
- Records accessible to BIS within a **reasonable time** (generally within 5 business days of OEE request)
- Annual internal ECP audit or review
- Periodic third-party ECP assessment recommended for high-volume or high-risk exporters

---

## Enforcement Regime

### Office of Export Enforcement (OEE)

BIS's enforcement arm investigates violations through:
- **Special Agents** conducting criminal investigations
- **End-Use Checks (EUC):** Pre-licence checks (PLC) and post-shipment verifications (PSV) conducted by US Commercial Service officers and BIS agents overseas
- **Administrative investigations** by the Office of Chief Counsel (OCC)

### Civil Penalties (§ 764.3, Part 766)

| Violation Type | Maximum Penalty |
|---------------|----------------|
| Per civil violation | Greater of $374,474 per violation (adjusted annually for inflation) OR **2× the value of the transaction** |
| Egregious violations | Higher penalties; may approach statutory maximum |
| Denial of export privileges | Temporary or permanent denial of all export privileges |

**Penalty determination factors (Part 766, Supplement 1):**
- Willfulness (did the violator know it was a violation?)
- Nature of the item (weapons-relevant, dual-use, EAR99)
- Harm to US national security or foreign policy interests
- Compliance programme quality (strong ECP = significant mitigation)
- Remedial action taken
- Cooperation with OEE

**Base penalty matrix** (post-September 2024 rule change):
- BIS removed caps that previously limited penalties below statutory maximums
- Penalties now more directly reflect transaction value, particularly for egregious cases
- Multiple violations per shipment (wrong ECCN, wrong destination, wrong exception = 3 violations from 1 shipment)

### Criminal Penalties (§ 764.2)

Willful violations of the EAR may be referred to the Department of Justice for criminal prosecution:
- **Individuals:** Up to **20 years** imprisonment + fines up to $1 million per violation
- **Corporations:** Fines up to $1 million per violation (per count)
- Criminal cases are reserved for deliberate, knowing, or willful violations — particularly those involving proliferation, sanctions evasion, or schemes to evade Entity List restrictions

### Export Denial Orders (EDOs)

BIS issues Export Denial Orders (EDOs) against individuals and companies found to have violated the EAR:
- EDOs are published in the Federal Register and placed on the Denied Persons List
- Third parties are prohibited from participating in any transaction involving a denied person
- Scope: US persons everywhere in the world; any person regarding items subject to EAR

---

## Voluntary Self-Disclosure (VSD) Process (§ 764.5)

### What is a VSD?

A Voluntary Self-Disclosure (VSD) is a self-initiated notification to OEE of an **apparent violation** of the EAR, license conditions, or orders. BIS strongly encourages VSDs.

### When to File

File a VSD when you discover:
- Items shipped without a required licence
- Items shipped to an Entity List, Denied Persons List, or Unverified List party
- Incorrect ECCN used that resulted in an unlicensed shipment
- SNAP-R licence conditions violated
- Prohibited end-use found post-shipment

### VSD Process

1. **Preliminary Inquiry (PI):** Review the facts; if a likely violation is found, stop any ongoing transactions
2. **Initial Notification:** File a brief initial notification to OEE (letter or email) — as soon as a likely violation is discovered; preserves the VSD date
3. **Full VSD Submission (within 180 days of initial notification):** Complete written VSD including:
   - Detailed narrative of the facts
   - All transactions identified (shipper, consignee, item, ECCN, value, date, exception claimed)
   - Root cause analysis
   - Remedial actions already taken
   - Proposed corrective actions
4. **OEE Review:** May request additional information; may conduct End-Use Checks
5. **Resolution:** Warning Letter, No-Action Letter, or administrative penalty with significant reduction for VSD

### VSD Penalty Mitigation

- VSD is considered a **strong mitigating factor** under the 2024 revised penalty guidelines
- Deliberate decision **not to disclose** significant apparent violations is an **aggravating factor**
- Combined with robust ECP, remediation, and full cooperation → may result in warning letter only for non-egregious cases

---

## Foreign Direct Product Rule (FDPR) — Deep Dive

### General FDPR (§ 736.2(b)(3))

Foreign-made items are subject to EAR if they are the **direct product** of US-origin technology or software that is controlled for NS or CB reasons AND the foreign item is to be shipped to a Country Group D:1 or E:1/E:2 country.

**Test:** Two-prong test:
1. **Technology/software prong:** Was the item produced using US-origin technology or software controlled for NS or CB reasons under the CCL?
2. **Destination prong:** Is the item destined for a D:1 or E:1/E:2 country?

### Entity List FDPR (2020 — Huawei Rule)

Extended the FDPR to capture foreign-made items when:
1. The foreign item is produced using equipment or technology that is the direct product of **specific US technology/software** (tooling, wafer fab equipment under 3B001/3B002)
2. AND the item is destined for a party on the Entity List

Designed to prevent circumvention of Entity List restrictions through foreign-chip supply chains.

### Advanced Computing FDPR (October 2022 / October 2023)

Captures items produced with US wafer fabrication equipment destined for:
- China or Macau for use in advanced computing applications above threshold
- Any Entity List party

### Russia/Belarus FDPR (March 2022)

Captures virtually all items produced anywhere with **any** US technology, software, or equipment, destined for Russia or Belarus — with extremely limited exceptions.

---

## Deemed Export Rules — Compliance Programme Implications

### What Constitutes a Deemed Export

Under § 734.13, the **release** of controlled technology or software to a **foreign national** in the US is a deemed export to their home country. "Release" includes:
- Visual inspection of controlled hardware
- Providing access to controlled equipment
- Oral, written, or electronic transmission of controlled technical data
- Demonstration of controlled software

### Nationality Rule

BIS applies the **"most restrictive" nationality rule** for dual nationals or persons with multiple citizenships:
- Apply the nationality that requires the most restrictive licensing treatment
- Example: A Chinese/Canadian dual national in the US is treated as a Chinese national for deemed export licensing purposes

### Practical Compliance Steps

1. **HR Screening:** When hiring foreign nationals for roles touching controlled technology, conduct pre-employment deemed export screening
2. **Classification Review:** Determine which technologies the employee will access; classify each
3. **Access Controls:** Limit access to controlled technology to employees with appropriate authorizations
4. **Deemed Export Licence Applications:** For employees who need access to NS-controlled technology from D:1 countries, apply for a deemed export licence via SNAP-R
5. **Source Code Repositories:** Restrict access to controlled source code on GitHub/GitLab/Bitbucket using role-based access; foreign nationals from D:1 countries require deemed export licences or exception applicability review
6. **Cloud and SaaS Environments:** Access to controlled technology via cloud platforms can constitute a deemed export; apply IP controls, authentication, and access auditing

---

## SNAP-R — Licensing Portal Guidance

**URL:** snap-r.bis.doc.gov (requires free BIS account)

**Forms filed through SNAP-R:**
- BIS-748P: Multipurpose Application Form (export licence, CCATS, Advisory Opinion)
- BIS-748P-A: Supplement for encryption review notifications (ENC exception)
- BIS-748P-B: Supplement for end-user statement attachments
- BIS-711: Statement by Ultimate Consignee and Purchaser

**SNAP-R Best Practices:**
- Submit complete applications — missing technical data is the #1 cause of delay
- Include end-use statements and supporting technical documentation proactively
- Track licence expiration dates and re-apply at least 60 days before expiry
- For time-sensitive transactions: contact the relevant BIS division directly after submission
- Use the "Licensing at a Glance" tool on bis.gov to estimate processing times by category

---

## EAR Recordkeeping Quick Reference

| Document Type | Retention Period | Format |
|---------------|-----------------|--------|
| Commercial invoices, purchase orders | 5 years from export date | Any readable format |
| Bills of lading, air waybills | 5 years | Any |
| EEI/AES filings | 5 years | Any |
| Licence applications and approvals | 5 years from expiry/completion | Any |
| Licence exception documentation | 5 years from export | Any |
| Restricted party screening records | 5 years | Recommended: dated screenshots |
| End-user statements and certifications | 5 years | Any |
| ECCN classification records | 5 years from last export of item | Any |
| VSD submissions and correspondence | Permanently | Any |

---

## Compliance Programme Maturity Assessment

| Level | Characteristics |
|-------|----------------|
| **Basic** | Written policy exists; some screening; training ad hoc; no formal audit |
| **Developing** | Formal ECCN classification; screening tool in place; annual training; no automated integration |
| **Proficient** | ERP-integrated screening; annual audits; full classification database; documented due diligence |
| **Advanced** | Real-time automated screening; ECCN lifecycle management; pre-shipment compliance review; regular third-party assessments; VSD process documented |

BIS rewards **Advanced** programmes with maximum penalty mitigation; **Basic** programmes may receive minimal credit even for VSDs.

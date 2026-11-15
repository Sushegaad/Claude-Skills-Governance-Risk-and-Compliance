# CCPA/CPRA vs. GDPR - Side-by-Side Comparison

For organisations subject to both laws (e.g., a US company with EU customers, or an EU company with California customers), understanding the differences and overlaps is essential to building an efficient dual-compliance programme.

---

## Scope & Applicability

| Dimension | CCPA/CPRA | GDPR |
|---|---|---|
| **Jurisdictional trigger** | Doing business in California | Processing EU/EEA/UK residents' personal data |
| **Who is covered** | For-profit businesses meeting threshold criteria | Any controller or processor, regardless of size or location |
| **Size/revenue thresholds** | Yes - $25M revenue OR 100K+ consumers OR 50%+ revenue from PI sale/sharing | No - applies to any organisation processing EU personal data |
| **Non-profits** | Generally exempt | Covered |
| **Government entities** | Exempt | Covered (public authorities have specific rules) |
| **B2B data** | Generally excluded (employee data limited exemption extended by CPRA) | Covered |

---

## Key Definitions

| Concept | CCPA/CPRA | GDPR |
|---|---|---|
| **Personal data/PI** | Broadly defined; includes household data | Broadly defined; personal to identified/identifiable individual only |
| **Special/sensitive categories** | CPRA SPI: SSN, precise geolocation, biometric, health, racial/ethnic, religious, union, sexual orientation, genetic, credentials, comms content | Special categories: racial/ethnic, political opinion, religious, union, genetic, biometric, health, sex life, sexual orientation |
| **Controller equivalent** | "Business" | "Controller" |
| **Processor equivalent** | "Service Provider" + "Contractor" (CPRA) | "Processor" |
| **Third party** | Entity that receives PI that is not a service provider/contractor | Not separately defined in same way |
| **Sale of data** | Broad: monetary or other valuable consideration | No equivalent concept; disclosure to third party = separate processing activity |
| **Sharing (cross-context behavioral advertising)** | CPRA-specific concept | No direct equivalent; covered under legitimate interests or consent for tracking |

---

## Lawful Basis

| Aspect | CCPA/CPRA | GDPR |
|---|---|---|
| **Basis for processing** | No lawful basis requirement - businesses can collect PI without consent (for most purposes) | Requires one of six lawful bases (consent, contract, legal obligation, vital interests, public task, legitimate interests) |
| **Consent for sensitive data** | Right to limit SPI use (opt-out model for most businesses) | Explicit consent required for special category data (with narrow exceptions) |
| **Opt-in vs. opt-out** | Primarily opt-out model (consumers must affirmatively request opt-out) | Primarily opt-in model (consent must be freely given, specific, informed, unambiguous) |
| **Minors (under 16)** | Opt-in required for sale/sharing of PI of consumers 13–16; parental consent under 13 | GDPR age of consent varies by Member State (13–16); parental consent for under-16 processing based on consent |

---

## Consumer / Data Subject Rights

| Right | CCPA/CPRA | GDPR |
|---|---|---|
| **Right to access** | Yes - specific pieces + categories (12-month scope pre-CPRA, no limit post-Jan 2022) | Yes - all personal data, no 12-month limitation |
| **Right to delete** | Yes - with numerous exceptions | Yes (right to erasure) - with exceptions |
| **Right to correct** | Yes (CPRA addition) | Yes (right to rectification) |
| **Right to portability** | Yes - portable format in access request | Yes - explicitly structured, commonly used, machine-readable format |
| **Right to opt-out of sale** | Yes - "Do Not Sell or Share My Personal Information" | No direct equivalent; may be covered by withdrawal of consent or objection to legitimate interests |
| **Right to restrict processing** | Limited - SPI limitation right (CPRA) | Yes - broader right to restrict processing |
| **Right to object** | Limited - opt-out of sale/sharing | Yes - right to object to processing based on legitimate interests or direct marketing |
| **Automated decision-making** | Yes: ADMT regulations are final and effective January 1, 2026, with compliance for significant decisions required from January 1, 2027 (opt-out, pre-use notice, access/human review) | Yes (Art. 22) - right not to be subject to solely automated decisions with significant effects |
| **Non-discrimination** | Yes (§1798.125) | No direct equivalent |
| **Response deadline** | 45 days + 45-day extension; SPI limit: 15 business days | 1 month + 2-month extension |

---

## Privacy Notices

| Requirement | CCPA/CPRA | GDPR |
|---|---|---|
| **At-collection notice** | Yes - categories, purposes, whether PI is sold/shared, link to privacy policy | Yes - Art. 13/14 privacy notice at collection |
| **Privacy policy** | Yes - comprehensive; updated annually | Yes - privacy notice must be accessible |
| **Retention periods** | Yes (CPRA addition) | Yes (must be specified or criteria stated) |
| **Lawful basis disclosure** | No - not applicable | Yes - must identify lawful basis for each processing purpose |
| **GPC signal** | Must honor as valid opt-out | No equivalent; but ePrivacy Directive may cover browser signals |

---

## Vendor / Third-Party Management

| Aspect | CCPA/CPRA | GDPR |
|---|---|---|
| **Processor agreements** | Required with service providers and contractors | Required Data Processing Agreements (Art. 28) |
| **Contract requirements** | Purpose limitation, prohibition on resale, deletion, audit rights | Detailed Art. 28 requirements: processing only on instructions, security, subprocessor rules, return/deletion |
| **Sub-processor** | Contractor / downstream service provider must also comply | Subprocessors require DPA + controller notification/approval |
| **International transfers** | No transfer restriction mechanism (CCPA does not restrict cross-border transfers) | Restricted to adequate countries or requires transfer mechanism (SCCs, BCRs, adequacy decision) |

---

## Enforcement & Penalties

| Aspect | CCPA/CPRA | GDPR |
|---|---|---|
| **Enforcement body** | California Privacy Protection Agency (CPPA) + California AG | Data Protection Authorities (DPAs) in each EU/EEA Member State |
| **Civil penalties** | $2,500 per unintentional / $7,500 per intentional violation | Up to €10M or 2% (lower tier) / €20M or 4% (higher tier) of global annual turnover |
| **Private right of action** | Yes - but limited to data breaches: $100–$750 per consumer per incident | Limited; EU Member States vary; class actions being developed |
| **Criminal penalties** | No direct CCPA criminal liability | Some Member States have criminal provisions |
| **Cure period** | No mandatory cure period for AG/CPPA enforcement since January 1, 2023; cure consideration is discretionary (§1798.199.45). Only the §1798.150(b) private data-breach action keeps a mandatory 30-day notice-and-cure, and curing blocks statutory damages only | No formal cure period |

---

## Practical Dual-Compliance Guidance

For organisations subject to both frameworks, the GDPR is generally the more demanding law. A GDPR-compliant programme will cover most CCPA/CPRA obligations with targeted additions:

**What GDPR already covers:**
- Privacy notices (at collection and policy)
- Consumer/data subject rights processes (access, delete, correct, portability)
- Processor agreements
- Data minimization and purpose limitation
- Retention schedules
- Security measures

**CCPA/CPRA-specific additions needed:**
1. Add **"Do Not Sell or Share My Personal Information"** link and opt-out workflow
2. Honor **Global Privacy Control (GPC)** signals
3. Add **"Limit the Use of My Sensitive Personal Information"** link and 15-day response workflow
4. Review vendor classification: are all "processors" actually **service providers** under CCPA (contracts may need updating)?
5. Implement **minors' opt-in** consent for sale/sharing (under 16)
6. Add **financial incentive / loyalty programme** disclosures if applicable
7. Confirm business threshold compliance annually - revenues and data volume thresholds
8. Implement **ADMT obligations** (regulations effective January 1, 2026; significant-decision compliance from January 1, 2027) plus cybersecurity audit and risk assessment requirements

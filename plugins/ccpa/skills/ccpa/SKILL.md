---
name: ccpa
description: >
  California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA)
  compliance advisor — business threshold analysis, consumer rights fulfillment
  (access, delete, correct, opt-out of sale/sharing, limit SPI, ADMT opt-out),
  privacy notice drafting, service provider vs. contractor vs. third-party
  classification, sensitive personal information (SPI) handling, data minimization,
  opt-out mechanisms (including GPC), cybersecurity audits and risk assessments
  (live since Jan 1, 2026), ADMT obligations (effective 2026, deadline Jan 1, 2027),
  CPPA enforcement (Disney $2.75M, PlayOn $1.1M, Ford $375K), penalty exposure,
  GDPR comparison, and gap assessments for businesses operating in or targeting
  California residents.
---

# CCPA/CPRA Compliance Advisor

> **Last verified:** 2026-10-03

You are an expert on California's comprehensive privacy laws:
- **CCPA**: California Consumer Privacy Act (Cal. Civ. Code §1798.100 et seq.), effective January 1, 2020
- **CPRA**: California Privacy Rights Act (Proposition 24), effective January 1, 2023 — significantly amends and expands CCPA, creates the California Privacy Protection Agency (CPPA)

## Applicability Workflow

Work through these steps in order for any organization asking "does CCPA/CPRA apply to us?"

1. **Confirm entity type.** Must be a **for-profit business** doing business in California. Non-profits and government entities are generally not covered, though some CPRA provisions may apply indirectly through service provider/contractor obligations flowing down from a covered business.
2. **Test the three thresholds** — the business is covered if it meets **at least one**:

| # | Threshold | Exact Figure |
|---|---|---|
| 1 | Annual gross revenue | Exceeds **$25 million** in the preceding calendar year |
| 2 | Data volume | Annually buys, sells, receives, or shares the personal information of **100,000 or more** consumers or households |
| 3 | Revenue from data monetization | Derives **50% or more** of annual revenue from selling or sharing consumers' personal information |

3. **Classify each downstream data recipient.** Applicability findings are incomplete without classifying who the business shares PI with:

| Classification | Definition | Sale? |
|---|---|---|
| **Service Provider** | Processes PI on behalf of the business under a written contract that prohibits further use beyond the specified business purpose | Not a sale |
| **Contractor** *(CPRA addition)* | Receives PI under a contract that prohibits use for any purpose other than specified; must certify compliance | Not a sale |
| **Third Party** | Receives PI but is not a service provider or contractor | May constitute a sale or sharing |

4. **Document the determination** — revenue and data-volume thresholds must be reassessed annually; vendor classifications should be reassessed whenever a contract is renewed or a new data recipient is onboarded.

## Key Definitions

- **Personal Information (PI)**: Information that identifies, relates to, describes, or could reasonably be linked to a consumer or household. Includes name, email, IP address, browsing history, purchase history, biometric data, geolocation.
- **Sensitive Personal Information (SPI)** *(CPRA addition)*: PI that reveals SSN/government ID, account credentials, precise geolocation, racial/ethnic origin, religious beliefs, union membership, genetic/biometric data, health/medical data, sexual orientation, or contents of consumer communications. See the full SPI category table and right-to-limit workflow below.
- **Sale**: Disclosing PI to a third party for monetary **or other valuable consideration** (broad definition — includes data brokering).
- **Sharing** *(CPRA addition)*: Disclosing PI to a third party for **cross-context behavioral advertising**, even without monetary consideration.
- **Service Provider**: Processes PI on behalf of a business under a written contract that prohibits further use; not considered a sale.
- **Contractor** *(CPRA addition)*: Entity receiving PI under a contract that prohibits use for any other purpose; must certify compliance.
- **Third Party**: Entity that receives PI from a business but is not a service provider or contractor.

## Consumer Rights

| Right | Description | Response Deadline |
|---|---|---|
| **Right to Know** (§1798.110 / §1798.115) | Access specific PI collected, categories, sources, purposes, third parties | 45 days (+ 45-day extension) |
| **Right to Delete** (§1798.105) | Delete PI collected from the consumer; exceptions apply | 45 days (+ 45-day extension) |
| **Right to Correct** (§1798.106) | Correct inaccurate PI *(CPRA addition)* | 45 days (+ 45-day extension) |
| **Right to Opt-Out of Sale/Sharing** (§1798.120) | Stop sale or sharing of PI to third parties | Immediate upon request; propagate within 15 business days |
| **Right to Limit SPI Use** (§1798.121) | Limit use/disclosure of SPI to what's necessary *(CPRA addition)* | 15 business days |
| **Right to Non-Discrimination** (§1798.125) | Cannot deny goods/services or charge different prices for exercising rights | N/A |
| **Right to Data Portability** | Receive PI in portable, usable format | Included in right to know |
| **Right to Opt-In (minors)** | Opt-in required for sale/sharing of minors' PI (under 16); parental consent under 13 | N/A |
| **Automated Decision-Making (ADMT)** (§1798.185(a)(16)) | Right to opt-out of ADMT; right to access logic; right to human review. **Regulations finalized and effective January 1, 2026. Compliance deadline for ADMT opt-out mechanism: January 1, 2027.** | Per CPPA regulations |

### General Request-Handling Principles

- **Response timeline (state it in every request-handling answer):** confirm receipt within **10 business days** with a description of the verification process (Regs §7021(a)); substantive response within **45 calendar days**, extendable once by a further **45 days** with notice to the consumer (§1798.130(a)(2)); opt-out and limit requests must be effectuated within **15 business days**.
- **Intake channels (§1798.130)**: Provide at least two methods for submitting requests, including (where applicable) a toll-free phone number and a web form or email. Online-only businesses may provide an email address as one method.
- **Identity verification — tiered standards (Regs §§7060–7062):**
  - **Reasonable degree of certainty** (e.g., categories-of-PI requests, deletion of non-sensitive data): match at least **2 data points** the business already holds
  - **Reasonably high degree of certainty** (specific pieces of PI; deletion of sensitive data): match at least **3 data points** PLUS a **signed declaration under penalty of perjury** that the requestor is the consumer
  - **Verification failure handling**: a request to know specific pieces that cannot be verified is answered with categories instead; a **deletion request that cannot be verified is denied as deletion but must be treated as an opt-out of sale/sharing** where applicable (Regs §7022(f)); opt-out requests themselves require no identity verification (only fraud screening)
  - Authorized-agent requests: require written permission from the consumer plus verification of the agent's identity; may also require direct verification with the consumer (except opt-out requests where the agent has power of attorney)
- **Free of charge**: Fulfill requests free of charge, **twice per 12-month period**. A reasonable fee may be charged for additional requests within 12 months if manifestly unfounded or excessive.
- **Record-keeping**: Businesses handling PI of **10 million or more** consumers/households must maintain records of consumer requests and responses, disclosures, and CCPA/CPRA training for **24 months**.

### Right to Know — Workflow (§1798.110 / §1798.115)

**Must disclose**: specific pieces of PI collected; categories of PI; categories of sources; business/commercial purpose for collecting, selling, or sharing; categories of third parties PI was disclosed to; categories of PI sold or shared and to whom.

**Scope**: default lookback is the 12 months prior to the request; for PI collected on or after January 1, 2022, the consumer may request information beyond 12 months and the business must provide it unless doing so proves impossible or would involve disproportionate effort (§1798.130(a)(2)(B)).

**Exceptions**: disclosure would reveal third-party trade secrets; would conflict with federal/state law; PI was collected for a single one-time transaction and not retained; PI is used solely for internal operations consistent with context of collection; PI is used solely to complete the transaction for which it was collected.

| Step | Action |
|---|---|
| 1 | Receive and log request with timestamp |
| 2 | Verify consumer identity (2-point match for standard requests) |
| 3 | Search PI systems using identifying data |
| 4 | Compile responsive PI across all systems (CRM, analytics, ad tech, etc.) |
| 5 | Apply exceptions — remove third-party trade secrets, conflicting legal holds |
| 6 | Deliver response in portable, readily usable format within 45 days |
| 7 | Provide extension notice if needed (within the original 45-day window) |

### Right to Delete — Workflow (§1798.105)

Business must delete the consumer's PI from its records **and** direct service providers and contractors to delete it.

**Exceptions** (business may retain PI if necessary to): (1) complete a transaction or perform a contract; (2) detect security incidents or protect against malicious, deceptive, fraudulent, or illegal activity; (3) fix errors that impair intended functionality; (4) exercise free speech or ensure another consumer's right to free speech; (5) comply with a legal obligation (§1798.145(a)); (6) use PI solely for internal purposes compatible with the context of collection (limited CPRA exception); (7) research, journalism, or statistical purposes in the public interest.

**Two-step deletion confirmation workflow:**

| Step | Action |
|---|---|
| 1 | Receive and log deletion request |
| 2 | Verify consumer identity |
| 3 | Check whether any exception applies; document reasoning if invoking one |
| 4 | **Step one — execute**: if proceeding, identify all PI records and propagate deletion instructions to service providers and contractors |
| 5 | **Step two — confirm**: confirm deletion to the consumer (or explain the exception invoked) within 45 days |
| 6 | Retain deletion-request records as proof of compliance (retaining the request record itself is not a contradiction of the deletion) |

### Right to Correct — Workflow (§1798.106, CPRA addition)

Business must take commercially reasonable steps to correct inaccurate PI and instruct service providers and contractors to correct it. Consumer must provide documentation if the business contests the claimed inaccuracy. Business may decline if correction would require revealing another individual's PI, or if it disagrees the PI is inaccurate and documents its decision.

| Step | Action |
|---|---|
| 1 | Receive correction request with claimed correction details |
| 2 | Verify consumer identity |
| 3 | Evaluate accuracy of the claimed correction (may request supporting documentation) |
| 4 | If agreeing to correct: update all relevant systems; instruct service providers and contractors |
| 5 | Notify consumer of outcome within 45 days |

### Right to Opt-Out of Sale/Sharing — Workflow (§1798.120)

**Scope**: "Sale" = disclosure of PI to a third party for monetary or other valuable consideration. "Sharing" (CPRA) = disclosure of PI to a third party for **cross-context behavioral advertising**.

**Sale vs. sharing analysis for ad tech**: any pipeline that passes PI (cookie IDs, device fingerprints, hashed emails, IP addresses) to ad exchanges, DMPs, or ad tech partners for cross-context behavioral advertising is "sharing" even absent monetary payment, and must be covered by the opt-out mechanism. First-party analytics tools that do not disclose PI to third parties are typically unaffected. Once a consumer opts out, the business must wait **12 months** before asking them to re-consent.

**The service-provider workaround does not exist for CCBA (Regs §7050(c))**: a person who contracts with a business to provide **cross-context behavioral advertising is a third party, not a service provider or contractor**, with respect to those services — restricted-use contract terms cannot convert CCBA disclosures into service-provider activity. Service providers may still provide **contextual** advertising and non-CCBA marketing services, but must not combine opted-out consumers' PI with PI from other sources. State this rule explicitly in any ad-tech classification answer.

**GPC / opt-out preference signal handling**: the business must honor the **Global Privacy Control (GPC)** signal as a valid opt-out — the CPPA has confirmed GPC compliance is required. GPC signals must be treated equivalently to a manual click on the "Do Not Sell or Share" link; no separate identity verification is required to act on an opt-out (only reasonable verification that the requester is the consumer).

| Step | Action |
|---|---|
| 1 | Consumer submits opt-out via link, form, or GPC signal |
| 2 | No identity verification required for opt-out beyond reasonable confirmation the requester is the consumer |
| 3 | Update consent/preference management platform within 15 business days |
| 4 | Propagate opt-out to service providers and contractors engaged in sale/sharing |
| 5 | Do not contact the consumer for 12 months to ask them to reconsider |

### Right to Limit Use of Sensitive Personal Information — Workflow (§1798.121, CPRA addition)

**SPI categories** (applicability trigger for the right to limit):
- Social Security number, driver's license, passport, or other government ID
- Financial account credentials (login + security code)
- Precise geolocation (locating a consumer within a radius of 1,850 feet — §1798.140(w))
- Racial/ethnic origin, religious/philosophical beliefs, union membership
- Contents of consumer mail, email, or text messages (unless the business is the intended recipient)
- Genetic data
- Biometric data used to uniquely identify a person
- Health/medical information
- Sexual orientation or sex life

**The right to limit does NOT apply** when SPI is used only for these permitted purposes:
- Performing services or providing goods reasonably expected by the consumer
- Safety, security, and integrity of services
- Short-term, transient use (e.g., a contextual ad based on the current session)
- Services performed on behalf of the business (service provider context)
- Verifying or maintaining quality of services
- Activities for which the SPI was specifically provided

| Step | Action |
|---|---|
| 1 | Provide "Limit the Use of My Sensitive Personal Information" link on the homepage (alongside or combined with the "Do Not Sell or Share" link) |
| 2 | Consumer exercises the right — no identity verification required beyond confirming consumer identity |
| 3 | Process within **15 business days** |
| 4 | Restrict SPI use to only the permitted purposes listed above |
| 5 | Propagate the limitation instruction to service providers and contractors |

### Right to Non-Discrimination (§1798.125)

Businesses **cannot**, because a consumer exercised a CCPA/CPRA right: deny goods or services; charge a different price (except where directly related to the value of the data); provide a different level or quality of goods/services; or suggest that any of the above will occur.

**Financial incentive exception**: businesses may offer financial incentives (loyalty programs, discounts) in exchange for PI, provided the incentive is reasonably related to the value of the consumer's PI, the consumer gives opt-in consent with a clear description of material terms, and the consumer can withdraw at any time.

### Authorized Agent Requests

Consumers may designate an authorized agent to submit requests on their behalf. The business must require written permission from the consumer (signed authorization), verify the agent's identity, and may require direct verification with the consumer as well — except for opt-out requests where the agent holds power of attorney.

## Key Obligations

### Privacy Notice at Collection
Inform consumers at or before PI collection: categories collected, purposes, whether PI is sold or shared, retention periods (CPRA requirement), and link to privacy policy.

### Privacy Policy
Must include: categories of PI collected in last 12 months, purposes of use, categories of third parties PI disclosed to, consumer rights and how to exercise them, contact info for requests, and "Do Not Sell or Share My Personal Information" link (or opt-out of SPI limitation where applicable). Update the privacy policy annually.

### Opt-Out Mechanisms
- **"Do Not Sell or Share My Personal Information"** link on homepage
- Accept opt-out signals including **Global Privacy Control (GPC)** — must be honored as a valid opt-out
- **"Limit the Use of My Sensitive Personal Information"** link (if SPI used beyond necessary purposes)
- **ADMT opt-out** — Must be implemented by **January 1, 2027**; applies to automated decisions producing legal or similarly significant effects

### Data Minimization & Purpose Limitation *(CPRA additions)*
PI collected must be adequate, relevant, and limited to what is necessary for the disclosed purpose. Cannot use PI for undisclosed purposes.

### Retention Limits *(CPRA addition)*
Disclose retention periods or criteria for each category. Cannot retain PI longer than reasonably necessary.

### Service Provider, Contractor, and Third-Party Contracts
Contracts with service providers and contractors must include: purpose limitations, prohibition on further sale/sharing, obligation to comply with consumer requests, rights to audit, and data deletion obligations. Confirm vendors are properly classified as service providers/contractors (not a sale) versus third parties (may constitute a sale or sharing) — a mismatch between contractual classification and actual data flow is a common gap-assessment finding.

### Cybersecurity Audits *(CPRA — Effective January 1, 2026)*
Businesses that process PI that presents **significant risk** to consumers' security must conduct **annual cybersecurity audits**. Regulations (finalized 2025, effective January 1, 2026) define scope and audit requirements. Non-compliance is an enforcement risk — the Disney $2.75M enforcement (2026) involved, in part, failure to implement adequate security practices.

### Risk Assessments *(CPRA — Effective January 1, 2026)*
Businesses must conduct and document **risk assessments** before processing PI that presents significant risk to consumers. Assessments must be submitted to the CPPA upon request. Regulations are live (effective January 1, 2026).

### Automated Decision-Making Technology (ADMT) *(Effective January 1, 2026 / Deadline January 1, 2027)*
- CPPA finalized ADMT regulations in 2025; **effective January 1, 2026**
- Consumers have the right to: opt out of ADMT producing significant decisions; know about automated processing; request human review
- Businesses must implement opt-out mechanisms **by January 1, 2027**
- ADMT covers decisions with legal or significant effects (employment, credit, housing, insurance, education)

## Penalties & Enforcement

**CPPA**: Independent enforcement agency (created by CPRA). Issues regulations, investigates complaints, brings administrative actions. The **California Attorney General (AG)** retains concurrent enforcement authority.

**Civil penalties (§1798.155)**:
- Unintentional violations: up to **$2,500 per violation**
- Intentional violations: up to **$7,500 per violation**
- Violations involving minors' PI: up to **$7,500 per violation** (always treated as intentional)

**Cure provisions**: a **30-day cure period** applies to AG actions (CPPA administrative actions may differ and are not subject to the same formal cure notice process).

**Private right of action (§1798.150)** — data breach only:
- Applies when PI is subject to unauthorized access due to failure to implement reasonable security measures
- Statutory damages: **$100–$750 per consumer per incident** (or actual damages, whichever is greater)
- Class action eligible; 30-day cure period (for non-CPRA actions)

### 2026 Enforcement Precedents

These cases define the current enforcement posture and penalty expectations:

| Company | Fine | Key Violations |
|---|---|---|
| **The Walt Disney Company** | **$2.75M** *(largest CCPA enforcement ever)* | Children's data handling failures; opt-out mechanism deficiencies; third-party ad tech data sharing |
| **PlayOn Sports** | **$1.1M** | Unauthorized sharing of consumer PI with third parties; inadequate consumer rights processes |
| **Ford Motor Company** | **$375K** | Failure to process consumer data deletion and access requests within required timeframes |

These cases signal that the CPPA is actively pursuing large enterprises for systematic violations, not just technical non-compliance. The Ford case in particular underscores that **missing the 45-day response deadline** for access/deletion requests is, on its own, an actionable enforcement basis — not merely a procedural lapse.

## CCPA/CPRA vs. GDPR — Quick Reference

GDPR is generally the more demanding law. A GDPR-compliant program covers most CCPA/CPRA obligations (privacy notices, rights processes, processor agreements, minimization, retention, security), but these CCPA/CPRA-specific items still need to be added: (1) "Do Not Sell or Share My Personal Information" link and opt-out workflow; (2) honor **GPC** signals; (3) "Limit the Use of My Sensitive Personal Information" link and 15-business-day workflow; (4) confirm vendor classification maps to **service provider**/**contractor** vs. third party, with contracts meeting the **§1798.100(d)** required terms; (5) a compliant **notice at collection** (§1798.100(a)-(b)) — a distinct artifact from a GDPR Art. 13 notice, delivered at or before collection, listing PI/SPI categories, purposes, retention periods per category, and sale/sharing status with the opt-out link; (6) minors' opt-in for sale/sharing (under 16; parental consent under 13); (7) financial incentive/loyalty disclosures, if applicable; (8) annual reconfirmation of the three business thresholds; (9) cybersecurity audit and risk assessment obligations (effective January 1, 2026) and ADMT opt-out (deadline January 1, 2027). **Name notice-at-collection explicitly in every GDPR-to-CCPA gap answer** — it is the most commonly missed delta because GDPR programmes assume their existing privacy notice covers it.

**Structural differences to state in every GDPR-comparison answer:**
- **Consent model**: CCPA is opt-out (sale/sharing); GDPR requires an opt-in lawful basis — CCPA has no lawful-basis requirement at all
- **Scope**: CCPA protects consumers **and households**; only businesses meeting the revenue/volume **applicability thresholds** are covered (GDPR has no thresholds); CCPA's "sale" concept (any disclosure for valuable consideration) is broader than anything in GDPR
- **Rights deltas**: the **right to correct was only added by CPRA**; CCPA has **no GDPR-style objection right and no full portability regime** (portable format applies to right-to-know responses); GDPR's DPO/DPIA regime maps only loosely to CPRA risk assessments
- **Remedies**: CCPA's **private right of action is limited to data breaches** (statutory damages **$100–$750 per consumer per incident**, §1798.150) — there is no general private action for privacy violations, unlike GDPR Art. 79/82

Key enforcement contrast: GDPR penalties run up to €10M/2% or €20M/4% of global annual turnover with no formal cure period in most cases, versus CCPA/CPRA's per-violation civil penalties of $2,500 (unintentional) / $7,500 (intentional) with a 30-day AG cure period.

## 2026 Legislation & Enforcement Update (state where relevant)

**September 2026 signings (effective January 1, 2027 unless noted):**
- **SB 923 (Expanding Privacy Rights Act)** — the right to delete now reaches PI collected **"from or about"** the consumer, including data acquired from third parties and data brokers (not just first-party collection); businesses may run suppression lists to keep deleted consumers deleted; exclusively-online businesses must offer an online request-submission method. Complements (does not replace) the Delete Act/DROP.
- **Children's package (signed Sept 10)**: AB 2246 replaces the Age-Appropriate Design Code with a reasonable-steps framework (default ban on profiling minors, dark-pattern bans); AB 1709 bans addictive features (personalized feeds, autoplay, push) for under-16s with penalties to $50,000 per minor; AB 1856 fixes the Digital Age Assurance Act's OS age-signal scope; SB 1119 adds companion-chatbot child-safety duties (core obligations July 1, 2027); SB 867 bans companion-chatbot toys (sunset 2031).
- Also: **AB 883** (data-broker DSR deadline cut 45→30 days + DROP notices), **AB 2561** (no silent reversion of privacy settings after updates), **AB 1609** (chatbot disclosure for >$500M businesses).
- **Vetoed: AB 1542** — the categorical ban on selling/sharing sensitive PI ("a step too far"; the statutory limit-the-use right remains the mechanism). Note: SB 435 was NOT vetoed — it died in Assembly Appropriations in August.

**Enforcement posture (CPPA):** data-broker registration blitz — **SalesIntel Research fined $36,400** (Sept 1) for failing to register; **Enforcement Advisory 2026-01** (Sept 3) targets registration accuracy with **$200/day** exposure; DROP deletion processing live since August 1, 2026. Earlier 2026: GM $12.75M (connected cars), PlayOn Sports $1.1M, Ford $375K (opt-out friction).

**ADMT countdown (include in any automation/profiling answer):** compliance for significant decisions begins **January 1, 2027** (pre-use notice, opt-out, access); risk assessments for processing ongoing as of Jan 1, 2026 are due **December 31, 2027** with first CPPA submissions by **April 1, 2028**; cybersecurity-audit certifications phase in April 2028/2029/2030 by revenue tier.

## Reference Files

- `references/consumer-rights-workflows.md` — step-by-step workflows for honoring each consumer right, verification requirements, exception handling
- `references/ccpa-gdpr-comparison.md` — side-by-side comparison of CCPA/CPRA vs. GDPR for global compliance teams

## How to Help

1. **Business applicability** — determine if a business is subject to CCPA/CPRA based on revenue, data volume, and monetization thresholds; classify downstream recipients as service providers, contractors, or third parties
2. **Consumer rights fulfillment** — guide the design of request intake, identity verification, response workflows, and exception handling for each right (know, delete, correct, opt-out, limit SPI)
3. **Privacy notices** — draft at-collection notices and privacy policies with all required disclosures
4. **Vendor classification** — classify data recipients as service providers, contractors, or third parties; review contract requirements
5. **SPI handling** — identify SPI categories, advise on limiting use/disclosure, draft SPI limitation notices
6. **Opt-out mechanisms** — design "Do Not Sell or Share" links, GPC signal handling, ADMT opt-out, consent management for minors
7. **Ad tech / sale-sharing analysis** — evaluate whether specific data flows (pixels, SDKs, cookie syncing, ad exchange bidding) constitute a "sale" or "sharing" under §1798.120 and require opt-out coverage
8. **GDPR alignment** — map CCPA/CPRA obligations to existing GDPR controls; identify US-specific gaps
9. **Gap assessment** — audit current practices against CCPA/CPRA requirements; prioritise remediation by penalty exposure and upcoming deadlines (ADMT deadline Jan 1, 2027)
10. **Enforcement & penalties** — assess penalty exposure in light of 2026 enforcement actions; advise on CPPA investigation response and cure-period strategy

---

> *This skill provides general compliance information, not legal advice. Verify current requirements against official sources; consult qualified counsel or an accredited assessor for decisions.*

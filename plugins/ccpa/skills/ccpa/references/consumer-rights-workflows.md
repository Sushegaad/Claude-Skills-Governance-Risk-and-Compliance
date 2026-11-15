# CCPA/CPRA Consumer Rights - Fulfillment Workflows

## General Request Handling Principles

**Intake channels (§1798.130):** Businesses must provide at least two methods for submitting requests, including (where applicable) a toll-free phone number and a web form or email. Online-only businesses may provide an email address as one method.

**Identity verification:** Must verify consumer identity before disclosing or deleting PI. Verification requirements scale with sensitivity:
- For non-sensitive requests: match 2 data points the business already holds
- For sensitive PI / financial data: match 3 data points + signed declaration under penalty of perjury
- For requests submitted through an authorized agent: require written permission + verification of agent identity

**Response timelines:** 45 calendar days from receipt (extendable once by another 45 days with notice). For SPI limitation requests: 15 business days.

**Free of charge:** Requests must be fulfilled free of charge, twice per 12-month period. Businesses may charge a reasonable fee for additional requests within 12 months if manifestly unfounded or excessive.

---

## Right to Know (§1798.110 / §1798.115)

**What must be disclosed:**
- Specific pieces of PI collected about the consumer
- Categories of PI collected
- Categories of sources from which PI was collected
- Business or commercial purpose for collecting, selling, or sharing PI
- Categories of third parties to whom PI was disclosed
- Categories of PI sold or shared and the categories of third parties to whom it was sold/shared

**Scope:** Covers PI collected in the 12 months prior to request (and ongoing from January 1, 2022 under CPRA, with no 12-month limit for data collected after that date).

**Exceptions where disclosure can be refused:**
- Would require disclosing third-party trade secrets
- Would conflict with federal/state law
- PI collected for single one-time transaction and not retained
- PI solely for internal operations consistent with context of collection
- Solely used to complete the transaction for which collected

**Workflow:**
1. Receive and log request with timestamp
2. Verify consumer identity (2-point match for standard requests)
3. Search PI systems using identifying data
4. Compile responsive PI across all systems (CRM, analytics, ad tech, etc.)
5. Apply exceptions - remove third-party trade secrets, conflicting legal holds
6. Deliver response in portable, readily usable format within 45 days
7. Provide notice if extension is needed (within original 45-day window)

---

## Right to Delete (§1798.105)

**Business must:**
- Delete the consumer's PI from its records
- Direct service providers and contractors to delete the PI

**Exceptions (business may retain PI if necessary to):**
1. Complete a transaction or perform a contract
2. Detect security incidents; protect against malicious, deceptive, fraudulent, or illegal activity
3. Fix errors that impair intended functionality
4. Exercise free speech or ensure another consumer's right to free speech
5. Comply with a legal obligation (CCPA §1798.145(a))
6. Use PI solely for internal purposes in a manner compatible with the context of collection (limited CPRA exception)
7. Research, journalism, or statistical purposes in the public interest

**Workflow:**
1. Receive and log deletion request
2. Verify consumer identity
3. Check if any exceptions apply; document reasoning if invoking an exception
4. If proceeding with deletion: identify all PI records, propagate deletion to service providers and contractors
5. Confirm deletion to consumer (or explain exception invoked) within 45 days
6. Retain deletion request records (for proof of compliance) - note: retaining the request itself is not a contradiction

---

## Right to Correct (§1798.106) - CPRA Addition

**What the business must do:**
- Take commercially reasonable steps to correct inaccurate PI
- Instruct service providers and contractors to correct the PI
- Consumer must provide documentation if business contests the claimed inaccuracy

**Business may decline if:**
- Correction would require revealing another individual's PI
- Business disagrees the PI is inaccurate and documents its decision

**Workflow:**
1. Receive correction request with claimed correction details
2. Verify consumer identity
3. Evaluate accuracy of the claimed correction (may request supporting documentation)
4. If agreeing to correct: update all relevant systems; instruct service providers and contractors
5. Notify consumer of outcome within 45 days

---

## Right to Opt-Out of Sale / Sharing (§1798.120)

**Scope:** Applies to:
- **Sale**: disclosure of PI to a third party for monetary or other valuable consideration
- **Sharing** (CPRA): disclosure of PI to a third party for cross-context behavioral advertising

**Mechanics:**
- "Do Not Sell or Share My Personal Information" link must be prominently placed on homepage and in privacy policy
- Must honor the **Global Privacy Control (GPC)** signal as a valid opt-out - the CPPA has confirmed GPC compliance is required
- Once opted out, the business must wait **12 months** before asking the consumer to re-consent

**Impact on advertising:**
- Opt-out means the business cannot pass PI (including cookie IDs, device fingerprints) to ad tech partners, ad exchanges, or DMPs for targeting
- Analytics via first-party tools that do not involve PI disclosure to third parties are typically not affected

**Workflow:**
1. Consumer submits opt-out via link, form, or GPC signal
2. No identity verification required for opt-out (only reasonable verification to confirm they are the consumer)
3. Update consent/preference management platform within 15 business days
4. Propagate opt-out to service providers and contractors engaged in sale/sharing
5. Do not contact consumer for 12 months to ask them to reconsider

---

## Right to Limit Use of Sensitive Personal Information (§1798.121) - CPRA Addition

**Sensitive Personal Information (SPI) categories:**
- Social Security numbers, driver's license, passport, other government IDs
- Financial account credentials (login + security code)
- Precise geolocation (within 1/4 mile)
- Racial/ethnic origin, religious/philosophical beliefs, union membership
- Contents of consumer mail, email, or text messages (unless business is the intended recipient)
- Genetic data
- Biometric data for uniquely identifying a person
- Health/medical information
- Sexual orientation or sex life

**Permitted uses without limitation right:**
Business may use SPI without offering limitation if the purpose is:
- Performing services or providing goods reasonably expected by a consumer
- Safety, security, and integrity of services
- Short-term, transient use (e.g., contextual ad based on current session)
- Services on behalf of the business (service provider context)
- Verifying or maintaining quality of services
- Activities for which SPI was provided

**Workflow:**
1. Provide "Limit the Use of My Sensitive Personal Information" link on homepage (alongside or combined with "Do Not Sell or Share" link)
2. Consumer exercises right - no identity verification required beyond confirming consumer identity
3. Process within **15 business days**
4. Restrict use of SPI to only the permitted purposes listed above
5. Propagate limitation to service providers and contractors

---

## Right to Non-Discrimination (§1798.125)

Businesses **cannot**, because a consumer exercised a CCPA/CPRA right:
- Deny goods or services
- Charge a different price (except where directly related to value of data)
- Provide a different level or quality of goods/services
- Suggest any of the above will occur

**Exception:** Businesses may offer financial incentives (loyalty programs, discounts) in exchange for PI, provided:
- The financial incentive is reasonably related to the value of the consumer's PI
- Consumer provides opt-in consent with a clear description of material terms
- Consumer can withdraw at any time

---

## Authorized Agent Requests

Consumers may designate an authorized agent to submit requests on their behalf. Business must:
- Require written permission from the consumer (signed authorization)
- Verify the agent's identity
- May require direct verification with the consumer as well (except for opt-out requests where agent has power of attorney)

---

## Record-Keeping

**All businesses** must maintain records of consumer requests and how they responded for at least **24 months** (11 CCR 7101). Records may include the request date, nature of the request, response date, nature of the response, and basis for any denial.

**Businesses that handle PI of 10,000,000 or more consumers in a calendar year** (11 CCR 7102) have one additional duty: compile annual metrics on requests received, complied with, and denied (plus median/mean response times) and disclose them in the privacy policy (or a linked page) by **July 1** each year.

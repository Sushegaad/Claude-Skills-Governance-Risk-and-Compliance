# Vietnam PDPL - Decree 356/2025/ND-CP: Implementation Details

Decree of the Government of Vietnam dated 31 December 2025, elaborating on certain articles of Law No. 91/2025/QH15 on Personal Data Protection. Effective 1 January 2026.

## Table of Contents
1. [Article 3 - Basic Personal Data (Non-Exhaustive List)](#article-3--basic-personal-data)
2. [Article 4 - Sensitive Personal Data (Open-Ended List)](#article-4--sensitive-personal-data)
3. [Article 5 - Response Timeframes for Data Subject Requests](#article-5--response-timeframes)
4. [Article 6 - Valid Consent Methods](#article-6--valid-consent-methods)
5. [Article 8 - Finance and Banking Sector](#article-8--finance-and-banking-sector)
6. [Article 9 - Big Data Processing](#article-9--big-data-processing)
7. [Article 10 - AI Systems and Metaverse](#article-10--ai-systems-and-metaverse)
8. [Article 11 - Blockchain and Distributed Ledger Technology](#article-11--blockchain)
9. [Article 12 - Cloud Computing Services](#article-12--cloud-computing)
10. [Article 13 - Personal Data Protection Personnel (DPO Qualifications)](#article-13--personal-data-protection-personnel)
11. [Practical Guidance by Sector](#practical-guidance-by-sector)

---

## Article 3 - Basic Personal Data

The Law itself (Article 2) defines basic personal data only abstractly and delegates the enumeration to the Government. Decree 356 Article 3 enumerates **10 basic personal data categories plus a catch-all item 11**, so the list is **non-exhaustive**:

1. Full name
2. Date of birth; date of death or going missing
3. Gender
4. Place of birth; place of registration of permanent residence; current place of residence; hometown; contact address
5. Nationality
6. Personal image
7. Phone number
8. National identity card/citizen identity card number; passport number; vehicle registration number; driver's licence number
9. Marital status
10. Information on family relationships (spouse, children, parents, siblings)
11. **Catch-all item:** other personal data attached to a specific individual that is not classified as sensitive - this item makes the basic-data list non-exhaustive

**Note:** Basic personal data still requires lawful basis and appropriate protection, but consent requirements are less stringent than for sensitive data. Because of item 11, do not treat the enumeration as a closed list.

---

## Article 4 - Sensitive Personal Data

The Law itself (Article 2) defines sensitive personal data only abstractly and delegates the enumeration to the Government. Decree 356 Article 4 enumerates **12 sensitive personal data categories plus a catch-all item (m)**, so the list is **open-ended**. Each category requires **explicit, separate consent**:

1. Political views, political party membership
2. Religious or philosophical views, religious organisation membership
3. Health status and private medical life; medical treatment history (except as required by law)
4. Racial or ethnic origin
5. Information about sexual life or sexual orientation
6. Data about criminal offences and criminal convictions
7. Financial information including bank accounts, credit cards, personal income, and credit history
8. Location data and data on movement of individuals
9. Biometric data - physiological or behavioural characteristics used to identify individuals: facial recognition data, fingerprints, iris scans, voice recognition, etc.
10. Genetic data - unique personal biological characteristics inherited or acquired
11. Social media behaviour tracking data - click-through rates, viewing history, behavioural patterns across platforms
12. Information about private life, personal secrets, family secrets
13. **Catch-all item (m):** other personal data specified by law as sensitive or requiring special protection - this item makes the sensitive-data list open-ended

---

## Article 5 - Response Timeframes for Data Subject Requests

Controllers and processors must respond to data subject rights requests as follows:

| Request Type | Acknowledgement | Fulfilment |
|---|---|---|
| Any data subject request | **2 working days** | (see below) |
| Access to personal data | - | **10 working days** |
| Correction of personal data | - | **10 working days** |
| Deletion of personal data | - | **20 working days** |
| Withdrawal of consent / restriction of processing | - | **15 working days** |
| Objection to processing | - | **15 working days** |

**Extension:** One extension is allowed per request. The data subject must be notified of the extension and the reason within the original deadline period.

**Exemptions:** A controller may refuse a request if:
- The request is manifestly unfounded or excessive
- Processing is required for national security or law enforcement purposes
- Processing is required to protect the vital interests of the data subject or another person
- Other cases prescribed by law

**Documentation:** All requests and responses must be logged for audit purposes.

---

## Article 6 - Valid Consent Methods

Consent must be expressly given using one of the following verifiable methods:

1. **Written consent** - signed paper document or electronic document with digital signature
2. **Recorded telephone call** - audio recording of verbal consent, with timestamp and call metadata
3. **SMS/text message** - specific consent syntax sent from the data subject's registered mobile number
4. **Email** - consent expressed through email sent from the data subject's registered address
5. **Website/application/platform form** - checkboxes or confirmation flows on digital platforms (but NOT pre-ticked boxes)
6. **Other electronic or verifiable format** - any other format that allows identification of the data subject and the specific consent given

**Invalid consent forms:**
- Silence or failure to respond
- Pre-ticked boxes
- Continued use of a service (unless the use itself constitutes the purpose and is made clear at the time of collection)
- Bundled consent where one consent covers unrelated purposes
- Consent obtained through deception, coercion, or undue influence

---

## Article 8 - Finance and Banking Sector

Special obligations for personal data processing in the **banking, credit, and financial services sector:**

**Annual compliance assessment:**
- Conduct and document an annual personal data protection compliance assessment
- Assessment must cover all personal data processing activities, legal bases, and security controls

**Audit logs:**
- Maintain detailed periodic audit logs of access to personal data systems
- Audit logs must record: who accessed data, when, what data was accessed, and the purpose

**Breach notification:**
- 72-hour notification to the personal data protection authority (same as general rule)
- ADDITIONALLY: notify the affected **data subjects** within 72 hours (for finance sector, data subject notification is mandatory simultaneously with authority notification)

**Data retention:**
- Financial transaction data must be retained for the period prescribed by financial sector regulations
- Personal data no longer needed for the processing purpose must be deleted or de-identified

**Third-party processors:**
- Written data processing agreements required with all outsourced processors
- Annual security assessments of critical third-party processors recommended

---

## Article 9 - Big Data Processing

Organisations processing personal data at **large scale or using big data analytics:**

**Security controls:**
- Implement **strong authentication** (multi-factor authentication) for all access to big data environments
- Apply **encryption or anonymisation** techniques appropriate to the sensitivity of the data
- Implement **continuous monitoring** for anomalous access patterns and potential breaches
- Conduct periodic penetration testing and vulnerability assessments

**Data minimisation:**
- Big data collection must still comply with purpose limitation - collect only what is demonstrably necessary
- Regularly purge data that is no longer required for the specified purpose

**Transparency:**
- Publish clear notices on big data collection practices
- Provide opt-out mechanisms for data subjects where feasible

---

## Article 10 - AI Systems and Metaverse

For personal data processing using **artificial intelligence, machine learning, or automated decision-making:**

**Right to opt out:**
- Data subjects must be informed when their data is used in automated processing
- Data subjects have the right to **opt out of automated processing** that produces decisions significantly affecting them
- Opt-out mechanisms must be simple and accessible

**Periodic assessment:**
- Organisations must conduct **periodic assessments** of AI/automated systems processing personal data
- Assessments must evaluate: accuracy, bias, impact on data subject rights, and security
- Assessment results must be documented and acted upon

**Transparency:**
- Inform data subjects when an AI system processes their data, what type of processing is involved, and the likely outcomes
- Do not use AI processing in ways that could be considered deceptive or manipulative

**High-risk AI:**
- Where AI is used for profiling, credit scoring, employment decisions, or other high-stakes decisions, enhanced transparency and data subject rights apply

---

## Article 11 - Blockchain and Distributed Ledger Technology

Special rules for personal data in **blockchain and DLT systems:**

**Core prohibition:** Personal data must **NOT be stored directly on a public or permissioned blockchain** where deletion or modification is technically infeasible.

**Permitted approaches:**
- Store **only de-identified data or cryptographic hash values** on-chain
- Maintain personal data in off-chain storage with only hashes or references on-chain
- Use private/permissioned chains with strict access controls if direct storage is unavoidable for the use case

**Data subject rights:**
- Controllers using blockchain must have a technical mechanism to fulfil deletion, correction, and access requests off-chain
- Where on-chain data cannot be deleted, document the technical impossibility and implement compensating controls

**Security:**
- Apply cryptographic controls appropriate to the sensitivity of the data
- Conduct regular security assessments of smart contracts and consensus mechanisms

---

## Article 12 - Cloud Computing Services

Special rules for personal data processed in **cloud environments:**

**Encryption requirements:**
- Encrypt personal data **at rest** and **in transit**
- Use encryption keys managed by the controller (or with appropriate key management controls)
- Apply encryption standards appropriate to the sensitivity of the data

**Access control:**
- Implement **access delegation controls** - cloud provider access to personal data should be limited to what is technically necessary for service delivery
- Document cloud provider access rights and review regularly

**Data residency:**
- For cloud storage of employee HR data, Article 20 cross-border transfer exemption may apply if data is used solely for HR administration purposes
- Confirm with legal counsel whether the specific cloud use case qualifies for the exemption

**Due diligence:**
- Conduct security assessments of cloud service providers before onboarding
- Include VN-PDPL compliance obligations in cloud service agreements
- Verify data centre locations and applicable security certifications (ISO 27001, SOC 2, etc.)

**Incident response:**
- Cloud providers must notify controllers immediately on becoming aware of a breach affecting personal data
- Controllers remain responsible for the 72-hour notification to the authority

---

## Article 13 - Personal Data Protection Personnel (DPO Qualifications)

**When a DPO is required:** The law requires appointment of a DPO for organisations processing personal data at large scale or processing sensitive personal data. Check with Ministry of Public Security guidelines for specific thresholds.

**Minimum qualifications:**
- College degree or higher (bachelor's degree preferred)
- Minimum **2 years of relevant experience** in one or more of: information technology, law, cybersecurity, risk management, compliance, or human resources
- Demonstrated knowledge of VN-PDPL and implementing regulations

**DPO responsibilities:**
- Advise the organisation on VN-PDPL compliance
- Monitor compliance with the law and internal data protection policies
- Act as point of contact for data subjects exercising their rights
- Act as point of contact with the Ministry of Public Security
- Conduct or oversee impact assessments
- Maintain the organisation's data processing records

**DPO independence:**
- The DPO must not receive instructions on how to perform their tasks
- Must not be penalised for performing their duties
- Must report directly to senior management

**DPO contact details:**
- Must be published (on website and/or in privacy notice) so data subjects can contact the DPO

**External DPO:** A DPO may be an external service provider (outsourced) provided they meet the qualification requirements and there is a written service agreement.

---

## Practical Guidance by Sector

### E-commerce and Retail
- Consent must be collected at point of registration and separately for marketing communications
- Cookie consent banners must comply with consent validity requirements (no pre-ticked boxes)
- Loyalty programme data requires separate consent from transactional data

### Healthcare
- Health data is sensitive - requires explicit consent for every distinct processing purpose
- Sharing with third-party providers (insurers, pharmacies) requires separate consent
- Medical records retention periods are governed by health sector regulations

### Human Resources
- Employee personal data processing requires a lawful basis (typically contract performance for employment-related processing)
- Consent is appropriate for voluntary benefits, wellness programmes, optional monitoring
- Cross-border transfer of employee HR data to cloud HR systems may qualify for the Article 20 exemption

### Technology and SaaS
- Software vendors processing Vietnamese user data are subject to VN-PDPL if their service is directed at Vietnamese users
- Data processing agreements with Vietnamese enterprise customers must include VN-PDPL compliance obligations
- Automated profiling features require opt-out mechanisms per Decree 356 Article 10

### Financial Services
- Annual compliance assessments mandatory (Decree 356 Article 8)
- Dual 72-hour notification (authority + data subjects) for breaches
- Credit scoring and financial profiling are high-risk AI uses requiring enhanced transparency

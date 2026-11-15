# HIPAA Breach Notification Rule Reference
## 45 CFR Part 164, Subpart D (HITECH / 2009)

---

## Table of Contents
1. [What is a Breach?](#1-what-is-a-breach)
2. [Breach Risk Assessment (4-Factor Test)](#2-breach-risk-assessment-4-factor-test)
3. [Notification to Individuals](#3-notification-to-individuals)
4. [Notification to HHS](#4-notification-to-hhs)
5. [Notification to Media](#5-notification-to-media)
6. [Business Associate Obligations](#6-business-associate-obligations)
7. [Documentation Requirements](#7-documentation-requirements)
8. [Penalties & Enforcement](#8-penalties--enforcement)
9. [Breach Response Workflow](#9-breach-response-workflow)
10. [Common Breach Scenarios](#10-common-breach-scenarios)

---

## 1. What is a Breach?

### Definition (§164.402):
A **breach** is the acquisition, access, use, or disclosure of PHI in a manner not permitted under the Privacy Rule that compromises the security or privacy of the PHI.

### Three Exceptions - These Are NOT Breaches:
1. **Unintentional access** by workforce member acting in good faith within scope of authority - if no further use/disclosure
2. **Inadvertent disclosure** between authorized persons at the CE/BA - if no further use/disclosure
3. **Good faith belief** that unauthorized person who received PHI could not have retained it (e.g., misdirected fax that was immediately returned/destroyed)

### Presumption:
**Assume it's a breach unless the CE/BA demonstrates low probability that PHI has been compromised** using the 4-Factor Risk Assessment.

---

## 2. Breach Risk Assessment (4-Factor Test)
### §164.402(2)

To rebut the presumption of a breach, document a risk assessment considering:

### Factor 1: Nature and Extent of PHI Involved
- What types of identifiers were included?
- Was financial information involved (SSN, credit card, bank account)?
- Was clinical information included (diagnosis, treatment, medication)?
- Higher sensitivity = higher likelihood of compromise

### Factor 2: Who Unauthorized Person Was
- Was it another CE or BA (who would understand privacy obligations)?
- Was it a member of the public?
- Was it a malicious actor vs. inadvertent recipient?
- Known or unknown recipient?

### Factor 3: Whether PHI Was Actually Acquired or Viewed
- Did the unauthorized person actually access the information?
- Was the email read? Was the USB drive opened?
- Technical evidence (email delivery receipts, server logs)?
- Attestation from recipient that they did not view/retain?

### Factor 4: Extent to Which Risk Has Been Mitigated
- Was the PHI retrieved/destroyed?
- Did recipient sign a confidentiality agreement?
- Did recipient provide credible assurance of destruction?

### Assessment Outcome:
- **Low probability of compromise** → Not a reportable breach (document your reasoning thoroughly)
- **Cannot demonstrate low probability** → Treat as reportable breach

> **Important**: HHS scrutinizes risk assessments. Document contemporaneously, thoroughly, and honestly. A weak or post-hoc justification is worse than treating the incident as a breach.

### Safe Harbor - Encryption:
If PHI was **encrypted** using NIST-approved methods AND the encryption key was not also compromised → **Not a reportable breach**, because the Breach Notification Rule applies only to "unsecured PHI" (as defined at §164.402 per the HHS encryption/destruction guidance); §164.402(2) is the breach presumption and 4-factor test, not the safe harbor.
- Acceptable: AES-128+, NIST FIPS 140-2 validated
- Must maintain documentation of encryption

---

## 3. Notification to Individuals
### §164.404

### Timeline:
**Without unreasonable delay AND within 60 calendar days** of discovery of the breach.

Discovery = when CE/BA knew or should have known of the breach (not when investigation concludes).

### Method:
- **First choice**: Written notice by **first-class mail** to last known address
- **If email on file and individual agreed to electronic notice**: Email acceptable
- **If contact info insufficient or out-of-date** (10+ individuals): Substitute notice:
  - Prominent posting on website homepage for 90 days + toll-free number, OR
  - Major print/broadcast media in affected area
- **Urgent situations** (imminent misuse risk): Phone or other means in addition to written notice

### Required Content of Individual Notice (§164.404(c)):
1. Brief description of what happened (date of breach, date of discovery if known)
2. Description of types of PHI involved
3. Steps individuals should take to protect themselves
4. Brief description of what CE is doing to investigate, mitigate, and prevent recurrence
5. Contact info (toll-free number, email, website, or postal address)

---

## 4. Notification to HHS
### §164.408

### Timeline Depends on Breach Size:

| Affected Individuals | HHS Notification Deadline |
|---------------------|--------------------------|
| **500 or more** in a state/jurisdiction | **Simultaneously with individual notice** (within 60 days of discovery) |
| **Fewer than 500** | **Annual log** - submit within 60 days after end of calendar year |

### How to Submit:
- HHS Breach Reporting Portal: www.hhs.gov/hipaa/for-professionals/breach-notification/
- Breaches of 500+ are posted on HHS "Wall of Shame" (public)

### Required Information for HHS Report:
- Name of CE
- Contact information
- Type of breach (theft, loss, unauthorized access/disclosure, hacking, improper disposal, other)
- Location of breached information (laptop, paper, EHR, email, other)
- Number of individuals affected
- Date of breach
- Date of discovery
- Description of PHI types involved
- Description of safeguards in place
- Actions taken in response

---

## 5. Notification to Media
### §164.406

### Required When:
Breach affects **500 or more residents** of a **state or jurisdiction**.

### Timeline:
Without unreasonable delay and within **60 calendar days** of discovery.

### Method:
Notify prominent media outlets serving the affected state/jurisdiction (e.g., major newspaper, TV station).

### Content:
Same as individual notification content.

> Note: Media notification is IN ADDITION to individual and HHS notification - not a substitute.

---

## 6. Business Associate Obligations
### §164.410

### BA Must Notify CE:
- **Without unreasonable delay** and within **60 calendar days** of discovery
- BA discovery = when any employee, officer, or agent of BA knows (or should know)

### What BA Must Provide to CE:
- Identity of each individual affected (if known)
- All information needed for CE to provide required notifications

### CE Remains Responsible:
- The CE must send notifications to individuals, HHS, and media
- CE's 60-day clock runs from CE's discovery OR BA's notification (whichever is earlier)
- CE and BA should establish clear breach notification obligations in BAA

### BA-to-Subcontractor:
- Subcontractors of BAs must notify the BA (same timeline)
- Chain of notification flows up: Subcontractor → BA → CE

---

## 7. Documentation Requirements
### §164.414

### Must Maintain Documentation of:
- Risk assessments for incidents (justifying breach vs. non-breach determination)
- All notifications sent (copies)
- Dates notifications were sent
- Substitute notice postings
- HHS reports submitted
- Media notifications

### Retention: 6 years from creation or last effective date

### Best Practice - Incident Log:
Maintain a running log of all security incidents (whether or not they rise to reportable breach level). Useful for:
- Demonstrating Security Rule compliance (§164.308(a)(6))
- Pattern identification
- HHS investigations
- Annual HHS small breach reporting

---

## 8. Penalties & Enforcement
### HITECH / §160.404

### Civil Money Penalties (CMPs):

| Violation Category | Per Violation | Calendar Year Cap |
|-------------------|--------------|-------------------|
| Did not know (reasonable diligence) | $137 – $68,928 | $2,067,813 |
| Reasonable cause (not willful neglect) | $1,379 – $68,928 | $2,067,813 |
| Willful neglect - corrected | $13,785 – $68,928 | $2,067,813 |
| Willful neglect - not corrected | $68,928 – $2,067,813 | $2,067,813 |

> Note: Penalty amounts are adjusted annually for inflation (figures above are approximate 2024 levels).

### Criminal Penalties (§1320d-6):
- Knowingly obtaining/disclosing PHI: Up to $50,000 + 1 year imprisonment
- Under false pretenses: Up to $100,000 + 5 years
- With intent to sell/transfer/use for commercial advantage: Up to $250,000 + 10 years

### State Attorneys General:
- May bring civil actions for HIPAA violations on behalf of state residents
- May obtain $100/violation, up to $25,000/year per violation category (pre-inflation)

### HHS Enforcement Priorities (Historical):
- Risk analysis failures (most common)
- Access control deficiencies
- Insufficient encryption (not implementing addressable standard)
- Business Associate Agreement failures
- Insufficient audit logging
- Failure to timely notify of breaches

---

## 9. Breach Response Workflow

```
INCIDENT DETECTED
      │
      ▼
STEP 1: CONTAINMENT (Immediate)
- Isolate affected systems
- Preserve evidence (logs, screenshots)
- Prevent further unauthorized access
- Assign incident response team
      │
      ▼
STEP 2: INVESTIGATION (Days 1-14)
- What PHI was involved? (types, quantity)
- When did breach occur? When discovered?
- Who was affected (individuals)?
- How did breach occur?
- Was encryption in place?
      │
      ▼
STEP 3: RISK ASSESSMENT (Days 1-30)
- Apply 4-Factor Test (see Section 2)
- Document analysis contemporaneously
- Determine: Reportable Breach or Not?
      │
      ├─ NOT A BREACH ──→ Document findings; close incident; review safeguards
      │
      ▼
STEP 4: IF REPORTABLE BREACH
      │
      ├─ Notify INDIVIDUALS within 60 days of discovery
      ├─ Notify HHS:
      │    ├─ 500+ affected: Within 60 days of discovery
      │    └─ <500 affected: Add to annual log; report by Mar 1 of following year
      └─ Notify MEDIA if 500+ residents in a state/jurisdiction
      │
      ▼
STEP 5: REMEDIATION
- Address root cause
- Enhance safeguards
- Update policies/procedures
- Retrain workforce
- Update Risk Analysis
      │
      ▼
STEP 6: DOCUMENTATION
- Incident report with all details
- Risk assessment documentation
- Copies of all notifications sent
- Remediation steps taken
```

---

## 10. Common Breach Scenarios

| Scenario | Breach? | Key Considerations |
|----------|---------|-------------------|
| Laptop with unencrypted PHI stolen | **Yes** (unless risk assessment rebuts) | Encryption safe harbor doesn't apply; document risk assessment |
| Encrypted laptop stolen | **Likely not** | Confirm encryption was FIPS 140-2 compliant; document |
| Email with PHI sent to wrong patient | **Risk assess** | Did recipient view it? Can they be contacted to confirm deletion? |
| PHI mailed to wrong address | **Risk assess** | Was it returned unopened? Could recipient have retained it? |
| Employee snoops on celebrity patient records | **Yes** | Workforce members are authorized users but this is impermissible access |
| Ransomware encrypts ePHI | **Likely yes** | Access/acquisition occurred; must conduct risk assessment; difficult to rebut |
| Vendor (BA) has breach | **Yes** | BA must notify CE; CE must notify individuals within 60 days |
| PHI posted on social media by employee | **Yes** | Impermissible disclosure; high severity |
| Paper PHI left in unsecured area briefly | **Risk assess** | Was it accessed? By whom? Mitigated? |
| Verbal disclosure of PHI to wrong party | **Privacy Rule** (not Security Rule) | Breach Notification applies to PHI broadly, not just ePHI |

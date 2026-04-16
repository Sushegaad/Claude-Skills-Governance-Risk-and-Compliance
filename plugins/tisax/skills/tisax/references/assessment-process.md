# TISAX Assessment Process Reference
## From Registration to Label Issuance via ENX Portal

---

## Overview

TISAX assessments are managed through the **ENX Association portal** at https://enx.com.
The entire lifecycle — registration, assessment, result publication, and sharing — takes
place within this portal. Results are **not publicly disclosed**; they are shared privately
between companies on a need-to-know basis.

Assessment lifecycle:
```
Register on ENX → Create Assessment Scope → Receive TISAX-ID (TAI) →
Engage Audit Provider → Conduct Assessment → Results on ENX Portal →
Share results with OEM/customer
```

---

## Step 1 — ENX Portal Registration

### Who Registers?

Any company that must demonstrate TISAX compliance to an automotive customer must
register themselves as a **TISAX Participant** on the ENX portal.

### Registration Steps

1. Go to https://enx.com/en-US/TISAX/
2. Click "Register" and create a company account
3. Provide accurate company details:
   - Legal company name (must match trade register)
   - Registered address
   - Industry sector
   - Primary contact and data protection contact
4. Accept the ENX TISAX Participation Agreement
5. Pay the annual participation fee (fee schedule on ENX website)
6. Receive ENX Participant ID (TISAX company identifier)

### Important

- A company may only have **one ENX participant account**
- Subsidiaries and separate legal entities require separate registration
- Fees are payable annually; non-payment suspends access to results

---

## Step 2 — Create Assessment Scope

### What is an Assessment Scope?

An Assessment Scope defines what organizational units, locations, and activities
are included in the TISAX assessment. A company may have multiple assessment
scopes (e.g., one per site, or per type of information handled).

### Scope Definition Steps

1. Log into ENX portal and navigate to "Assessment Scopes"
2. Click "Create New Scope"
3. Define:
   - **Scope name** — descriptive name; may be seen by customers
   - **Scope description** — what systems, locations, processes are covered
   - **Assessment objectives** — select which labels are sought (IS, IS High, Prototype, Strict Prototype, Data)
   - **Locations** — list all sites/locations in scope (address, country, number of staff)
4. Submit scope for review
5. ENX validates the scope and issues a **TISAX Assessment ID (TAI)** — a unique identifier for this scope

### TISAX Assessment ID (TAI)

- Format: TAI-XXXXXXXX (alphanumeric)
- Often called "TISAX-ID" in casual usage
- Share this ID with your Audit Provider and, later, with customers
- It links your assessment to the ENX portal result

---

## Step 3 — Determine Required Assessment Level

The required Assessment Level (AL) is determined by the **protection need** of the
information/assets covered and the OEM's requirements.

| Assessment Level | Method | Typical Trigger |
|-----------------|--------|-----------------|
| AL 1 | Self-assessment (plausibility check) | Rare; not accepted by most OEMs |
| AL 2 | On-site audit by licensed Audit Provider | Standard IS label; Prototype label; most OEMs |
| AL 3 | On-site audit with deeper scrutiny | Info High, Strict Prototype; high-risk suppliers |

**Critical note:** Most major OEM contract requirements specify AL 2 or AL 3. AL 1 is
rarely accepted as sufficient proof of conformance. Always confirm the required level
with your customer before booking an assessment.

---

## Step 4 — Engage a Licensed TISAX Audit Provider

### Finding an Audit Provider

Only ENX-licensed **TISAX Audit Providers** (formerly called Audit Service Providers) may
conduct TISAX assessments. A current list is published on the ENX portal.

Licensed providers include (non-exhaustive, as of 2024):
- TÜV Rheinland
- TÜV SÜD
- TÜV NORD
- Bureau Veritas
- SGS
- Deutsche Telekom (for German operations)
- Many national IT security / certification firms licensed per country

### Engagement Steps

1. Download the list of licensed providers from ENX portal
2. Request quotes from 2–3 providers (specify objectives, locations, timeline)
3. Sign engagement contract with chosen Audit Provider
4. Provide the Audit Provider with your:
   - TAI (TISAX Assessment ID)
   - Scope description document
   - Preliminary self-assessment against VDA ISA (if completed)
5. Agree on assessment timeline and pre-audit activities

---

## Step 5 — Pre-Assessment Preparation

### Self-Assessment Against VDA ISA

Before the formal audit, conduct an internal gap analysis against VDA ISA 6.0:

1. Download VDA ISA 6.0 from https://www.vda.de (registration may be required)
2. Work through all applicable chapters:
   - Chapters 1–14: Mandatory for all assessments
   - Chapter 15: Only if Prototype or Strict Prototype label required
   - Chapter 16: Only if Data label required
3. Rate each control/question against the 0–5 maturity scale:
   - 0 = Incomplete/no process
   - 1 = Performed (informal)
   - 2 = Managed (planned and tracked)
   - 3 = Established (defined and consistent processes)
   - 4 = Predictable (quantitatively measured)
   - 5 = Optimizing (continuous improvement)
4. Identify all "must" criteria rated below 3 — these are mandatory non-conformances
5. Develop a remediation plan for all gaps before the formal assessment

### Document Preparation

Prepare an evidence package for the Audit Provider:
- ISMS documentation (policies, procedures, controls)
- Recent internal audit reports
- Completed self-assessment against VDA ISA
- Network and architecture diagrams
- Asset and risk registers
- Evidence of implemented controls (screenshots, configurations, records)

---

## Step 6 — Conducting the Assessment

### AL 2 Assessment Process

| Phase | Activities |
|-------|-----------|
| Document review (remote or on-site) | Audit Provider reviews IS documentation; requests clarifications |
| On-site audit day(s) | Physical inspection of facilities; interviews with key personnel; technical checks |
| Observation of controls | Verifying implemented controls match documented procedures |
| Non-conformance identification | All failures against must criteria and standard criteria documented |
| Preliminary findings | Audit Provider presents preliminary findings; organization has limited time to respond |
| Final assessment report | Formal report submitted to ENX portal; result published to participant's portal account |

### AL 3 Assessment Process

AL 3 follows the same phases as AL 2 but with:
- Extended document review (more detailed scrutiny)
- Additional investigative days on-site
- Deeper technical testing (e.g., network scans, penetration testing consideration)
- Stricter minimum requirements for certification

### Non-Conformances

| Category | Description | TISAX Impact |
|---------|-------------|-------------|
| Major non-conformance | Failure to meet a "must" criterion; fundamental control absent | Label not issued until resolved |
| Minor non-conformance | Weakness in a standard requirement; control partially effective | Label may be issued with conditions |
| Observation | Improvement recommendation; control is present but not optimal | No impact on label issuance |

**Correction period:**
- Major non-conformances must be corrected and verified before the label can be issued
- The Audit Provider will perform a **re-assessment** or **targeted follow-up** to verify corrections
- Companies typically have up to 3 months to address major non-conformances

---

## Step 7 — Results on ENX Portal

### Label Issuance

Once all non-conformances are resolved:
1. Audit Provider uploads the assessment report to the ENX portal
2. ENX validates the report
3. Assessment result becomes visible in the participant's portal account
4. TISAX Labels are formally recorded against the Assessment Scope (TAI)

### Label Validity

| Attribute | Details |
|-----------|---------|
| Validity period | **3 years** from the date of assessment |
| Reassessment trigger | Expiry of 3-year period; significant changes to scope |
| Continuous monitoring | Not required, but significant changes (new sites, new systems) may require scope update |
| Interim checks | Some OEMs may request evidence that controls remain effective between assessments |

### Portal Result Record

The ENX portal record for each assessment shows:
- Company name and ENX Participant ID
- Assessment Scope description
- TAI (Assessment ID)
- Labels achieved
- Audit Provider name and date of assessment
- Validity period end date

---

## Step 8 — Sharing Results with Customers

TISAX results are **private by default**. They must be explicitly shared with each customer
or partner that requires them.

### Sharing Process

1. Log into ENX portal
2. Navigate to your Assessment Scope / TAI
3. Click "Share Results"
4. Enter the ENX Participant ID of the company you are sharing with (your customer/OEM)
5. Confirm the sharing scope (full or partial)
6. The receiving company receives a notification and can view the result in their portal

### Sharing Considerations

- Sharing is granular — you can share specific scopes with specific customers
- Sharing does not hand over the full audit report; it grants view access to the ENX result record
- Full audit reports are not routinely shared; they remain with the Audit Provider and the assessed company
- If a customer requests the full report, this is negotiated directly; ENX results are sufficient for most OEM requirements

### Receiving Results as an OEM or Customer

OEMs and customers must also be registered ENX participants to receive shared results.
When a supplier shares results:
1. OEM receives notification in their ENX portal
2. OEM views the result record (label type, scope, validity, Audit Provider)
3. OEM stores the result reference (TAI and validity date) in their supplier management system

---

## Step 9 — Renewal and Re-assessment

### 3-Year Cycle

As the label expiry date approaches (typically 6–12 months before expiry):
1. Create a new Assessment Scope or update the existing one if scope has changed
2. Engage an Audit Provider for re-assessment
3. Re-assessment follows the same process as the initial assessment
4. New labels issued upon completion

### Scope Changes

If significant changes occur within the 3-year period:
- Addition of new sites/locations
- Major system changes affecting IS posture
- Organizational restructuring

Recommended: Inform your Audit Provider; they will advise whether a scope update
or interim review is required.

---

## Assessment Timeline Reference

| Activity | Typical Duration |
|----------|-----------------|
| ENX registration + Scope creation | 1–2 weeks |
| Audit Provider selection and contracting | 2–4 weeks |
| Internal gap analysis and remediation | 4–12 weeks (depends on maturity) |
| Document review phase (Audit Provider) | 1–2 weeks |
| On-site audit (AL 2) | 1–3 days |
| On-site audit (AL 3) | 2–5 days |
| Non-conformance resolution (if needed) | 4–12 weeks |
| Report finalization and ENX publication | 2–4 weeks |
| **Total end-to-end (first assessment)** | **3–9 months** |

---

## Common Assessment Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|-----------|
| Scope too broad — includes systems not relevant to CBI | Higher cost and effort | Define scope tightly around where CBI is actually processed |
| Scope too narrow — excludes critical supporting infrastructure | Assessment finding; may invalidate label | Ensure all systems supporting CBI processing are included |
| Evidence not prepared in advance | Assessment delays; additional audit days | Prepare the evidence package 4–6 weeks before audit days |
| Must criteria below maturity 3 discovered on audit day | Major non-conformance; delays label | Conduct thorough pre-assessment self-assessment |
| AL 1 delivered when OEM requires AL 2 | Customer rejects result | Always confirm AL requirement with customer before engaging Audit Provider |
| Assessment scope changed significantly after TAI issued | Scope invalid; may need new TAI | Discuss all planned changes with Audit Provider before implementation |

---

## Key Contacts and Resources

| Resource | URL / Method |
|----------|-------------|
| ENX Association TISAX portal | https://enx.com/en-US/TISAX/ |
| ENX portal registration | https://enx.com (registration button) |
| VDA ISA download | https://www.vda.de/en/education-and-training/isa |
| Licensed Audit Provider list | Listed in ENX portal after registration |
| ENX helpdesk | Contact form on enx.com |

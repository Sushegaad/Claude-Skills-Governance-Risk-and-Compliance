# SOC 3 — General Use Report Reference

## Overview

SOC 3 reports are general use attestation reports based on the same AICPA Trust Services
Criteria (TSC) as SOC 2. They are designed to communicate to the public that an organization
received a clean opinion from an independent CPA firm, without disclosing the detailed control
descriptions, testing procedures, or test results included in a SOC 2 report.

**Governing standard:** SSAE 18, AT-C Section 205 (*Examination Engagements*)  
**Criteria applied:** AICPA Trust Services Criteria (2017, with 2022 Revised Points of Focus)  
**Distribution:** Unrestricted — may be posted publicly, shared freely with customers, prospects, and partners

---

## SOC 3 vs SOC 2 — Side-by-Side Comparison

| Attribute | SOC 2 | SOC 3 |
|---|---|---|
| Governing standard | SSAE 18 AT-C §205 + TSC | SSAE 18 AT-C §205 + TSC |
| Distribution | Restricted (specific parties under NDA) | Unrestricted (general public) |
| System description | Full, detailed description of the system | Brief, high-level description only |
| Controls documented | Yes — all in-scope controls described | No — controls not described in report |
| Tests of controls | Yes — testing procedures and results included | No — no test details in report |
| Results of tests | Yes — deviations and exceptions reported | No — only the overall opinion |
| AICPA seal permitted | No | Yes |
| Suitable for posting on website | No | Yes |
| Suitable for user auditor reliance | Yes | No |
| Suitable for security questionnaire response | Yes (restricted sharing) | Yes (openly shareable) |
| Can be issued simultaneously with SOC 2? | N/A | Yes — same examination period |

---

## Trust Services Criteria Categories

A SOC 3 report covers one or more of the five Trust Services Criteria categories, identical to SOC 2:

| Category | Code | Always Required? |
|---|---|---|
| Security (Common Criteria) | CC | Yes — must be included |
| Availability | A | Optional |
| Confidentiality | C | Optional |
| Processing Integrity | PI | Optional |
| Privacy | P | Optional |

The same scope principles as SOC 2 apply. Security (CC) is not optional. Additional categories
are included based on service commitments to customers.

---

## SOC 3 Report Structure

A SOC 3 report contains three components:

### 1. Management's Assertion
Management asserts that:
- The description of the system is fairly presented.
- Controls operated effectively throughout the period with respect to the TSC categories covered.

### 2. Practitioner's Short-Form Report
The CPA firm issues a short-form opinion that states:
- The examination was conducted in accordance with SSAE 18 AT-C Section 205.
- In the practitioner's opinion, the entity maintained effective controls over the TSC categories covered throughout the period.

The short-form report does **not** include:
- A description of each test procedure.
- Results of individual tests.
- A list of deviations or exceptions.

### 3. Brief System Description
A high-level description of the services and system. This is deliberately less detailed than
the SOC 2 system description. It typically covers:
- The services provided.
- The geographic locations if relevant.
- The major categories of data processed.
- The TSC categories covered.

---

## Relationship Between SOC 2 and SOC 3

An organization typically obtains a SOC 3 based on the **same examination** as a SOC 2 Type 2.
The same CPA firm performs the same testing against the same TSC for the same period. From
that single examination, it issues:

- The full SOC 2 Type 2 report — distributed only to specified parties.
- The SOC 3 report — distributed publicly or used for the AICPA seal.

**A standalone SOC 3 without an underlying SOC 2 examination is possible** but uncommon. The
AICPA guidance permits a practitioner to issue a SOC 3 from an examination conducted solely
for that purpose. In practice, most organizations obtain SOC 2 as the primary deliverable and
add SOC 3 for public use.

---

## AICPA SOC Service Organization Seal

Organizations that receive an unmodified (clean) SOC 3 practitioner's report may display the
**AICPA SOC Service Organization seal**. The seal communicates to stakeholders that an
independent CPA firm has examined the organization's controls and found them effective.

### Seal Requirements

- The report must be an unmodified opinion (no qualifications).
- The seal must include text specifying the TSC categories covered.
- The seal must include the period covered.
- Only licensed AICPA member CPA firms may award the seal.
- The AICPA licenses the use of the seal; the organization must comply with AICPA's seal usage policies.

### Seal Use Restrictions

- The seal may not be altered, modified, or used in a misleading context.
- The seal may not imply AICPA endorsement of any particular product or service.
- If a subsequent examination results in a modified opinion, the previous seal reference must be updated.

---

## When to Recommend SOC 3

Recommend SOC 3 in these situations:

| Scenario | Reason |
|---|---|
| Organization wants a publicly shareable security certification | SOC 3 is freely distributable; SOC 2 is not |
| Marketing or sales team needs evidence to share with prospects | SOC 3 can be placed on the website or included in sales materials |
| Customer RFPs ask for "SOC report" without specifying SOC 2 | SOC 3 satisfies general requests where detail is not required |
| Organization already has SOC 2 and wants incremental value | SOC 3 adds public credibility at minimal additional cost |
| Small organization wants public assurance without disclosing test detail | SOC 3 provides global assurance without revealing control specifics |

**When SOC 3 is NOT sufficient:**
- User auditors require SOC 2 Type 2 to rely on service organization controls for ICFR purposes.
- A sophisticated customer or partner requires a full SOC 2 report with test procedures and results.
- The organization's vendor risk management program requires signed NDA and full SOC 2.

---

## SOC 3 Procurement Guidance (Customer Perspective)

When evaluating a vendor's SOC 3 report:

1. **Confirm the report is current** — SOC 3 reports should cover a period ending within the last 12 months. An older report may not reflect current controls.
2. **Check TSC scope** — A SOC 3 covering Security only may not address Availability or Privacy. If these are important, ask for SOC 2 or a separate assessment.
3. **Identify the CPA firm** — The report must be issued by a licensed CPA firm. Confirm the firm is reputable and experienced in SOC engagements.
4. **Understand the limitation** — SOC 3 tells you the controls were effective; it does not tell you what the controls were, how they were tested, or whether there were any exceptions. For deeper assurance, request the full SOC 2 report under NDA.
5. **Ask about the underlying SOC 2** — Confirm there is a full SOC 2 Type 2 report available under NDA if needed for your own audit or regulatory requirements.

---

## Common Questions

**Q: Can an organization claim SOC 3 compliance?**  
"Compliance" is not the correct term for SOC 3. SOC 3 is an attestation — a CPA firm examined
the organization's controls and issued an opinion. The correct phrasing is "we received an
unmodified SOC 3 report" or "our controls were examined under SOC 3."

**Q: Does SOC 3 replace SOC 2?**  
No. SOC 3 does not replace SOC 2. They serve different purposes and audiences. SOC 3 is for
public audiences; SOC 2 is for specific parties (user entities, user auditors) that need
detailed control information.

**Q: Is a SOC 3 the same as ISO 27001 certification?**  
No. ISO 27001 is a certification against an information security management system standard,
issued by an accredited certification body. A SOC 3 is an attestation by a CPA firm that the
organization's controls met the AICPA Trust Services Criteria during the examination period.
Both provide assurance about information security controls, but they use different frameworks,
are issued by different types of bodies, and convey different types of assurance.

**Q: How often should a SOC 3 be renewed?**  
The AICPA does not mandate a renewal period, but the seal displays the period covered by the
examination. In practice, annual examinations are the norm to maintain a current report.

**Q: Can SOC 3 cover multiple TSC categories?**  
Yes. A SOC 3 can cover Security, Availability, Confidentiality, Processing Integrity, and
Privacy — the same categories as SOC 2. Most SOC 3 reports cover Security (CC) as a minimum.
Additional categories are included when the organization has contractual or regulatory
commitments related to those categories.

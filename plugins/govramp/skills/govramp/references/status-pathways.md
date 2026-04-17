# GovRAMP Status Pathways — Decision Guide

Use this reference when helping a provider or government entity determine the most
appropriate GovRAMP status pathway based on their situation, goals, resources, and
existing authorizations.

---

## Status Pathway Overview

| Status | 3PAO Required | Gov Sponsor | ConMon Frequency | Key Requirement | Listed on APL |
|--------|--------------|-------------|-----------------|-----------------|---------------|
| Progressing Snapshot | No | No | N/A (not verified) | Membership; quarterly engagement | No (Progressing List) |
| Core | No (PMO review) | No | Quarterly | 60 controls evidenced; templates | Yes |
| Ready | Yes (RAR) | No | Monthly + Annual | Min. mandatory req's; 50% docs | Yes |
| Authorized | Yes (SAR) | Yes | Monthly + Annual | All controls; 100% docs | Yes |
| Provisionally Authorized | Yes (SAR) | Pending/Committee | Monthly + Annual | All controls; sponsor in process | Yes |

---

## Decision Tree: Which Pathway Is Right?

### Step 1: Do you already hold FedRAMP authorization?

**YES** → **Fast Track** is available. You can submit existing federal security documentation
(FedRAMP SSP, SAR, 90 days of ConMon data) to the GovRAMP PMO. GovRAMP accepts
documents in FedRAMP formatting. Fast Track applies to Ready or Authorized status.
Proceed to Step 5 for Fast Track specifics.

**NO** → Proceed to Step 2.

---

### Step 2: What is your primary goal?

**A. Build initial credibility and visibility with less upfront investment**
→ Consider **Progressing Snapshot** first, then progress to Core or Ready.

**B. Achieve a formal verified status without a full 3PAO audit**
→ Target **GovRAMP Core** (launched May 2025; 60 controls; PMO-reviewed).

**C. Achieve full verified status demonstrating minimum mandatory requirements**
→ Target **GovRAMP Ready** (3PAO Readiness Assessment Report required).

**D. Achieve the highest level of assurance to compete for major government contracts**
→ Target **GovRAMP Authorized / Provisionally Authorized** (3PAO SAR + government sponsor).

---

### Step 3: What impact level do you need?

Use the GovRAMP Data Classification Tool to determine your level:
https://govramp.org/blog/document/data-classification-tool/

| Government Data Type | Likely Impact Level |
|---------------------|---------------------|
| Public records, administrative tools, non-PII systems | Low |
| General PII, non-law-enforcement public records | Low+ or Moderate |
| Healthcare data (PHI), financial data, voter records | Moderate |
| Criminal Justice Information (CJI) | Moderate + CJIS Overlay |
| Emergency services, critical infrastructure, classified-adjacent data | High |

Core status is aligned to the **Moderate** baseline regardless of the provider's
ultimate target level. It provides a foundation before pursuing full Moderate or High
authorization.

---

### Step 4: What is your readiness?

| Readiness State | Recommended Path |
|----------------|-----------------|
| Early stage; significant gaps; first time building a security program | Progressing Snapshot → Core |
| Documentation partially complete; controls partially implemented | Core (if no 3PAO budget) or Ready (if 3PAO budget available) |
| Documentation near-complete; controls mostly implemented | Ready → Authorized |
| Documentation fully complete; controls fully implemented | Authorized directly |
| FedRAMP-authorized or in active pursuit | Fast Track |

---

### Step 5: Fast Track Decision

**Prerequisites:**
- Active GovRAMP membership
- Existing FedRAMP authorization OR active FedRAMP pursuit with documentation available
- 90 days of continuous monitoring data
- Completed federal-approved security package

**Fast Track Process:**
1. Submit a Security Review Request Form to the GovRAMP PMO
2. Work with 3PAO to gather and authenticate: federal security package, 90 days of
   ConMon data, any required GovRAMP-specific template adjustments
3. PMO reviews package and conducts a review call with provider and 3PAO
4. Provider achieves Ready or Authorized status (PMO determination)
5. Begin GovRAMP Continuous Monitoring

**Texas Note:** TX-RAMP recognizes GovRAMP with automatic reciprocity. GovRAMP provides
a weekly sync — GovRAMP-authorized products automatically appear on the TX-RAMP list.

---

## Pathway Comparison — Effort and Cost

### GovRAMP Core

| Dimension | Detail |
|-----------|--------|
| Controls assessed | 60 (NIST 800-53 Rev 5 Moderate-aligned, MITRE ATT&CK prioritized) |
| Assessment method | PMO review of submitted documentation and evidence |
| 3PAO required | No |
| Policies required | Yes (for all 60 control areas) |
| Templates required | SSP, IRP, CP, Scan documentation (Moderate Impact package) |
| ConMon | Quarterly |
| Typical timeline | Shorter than Ready/Authorized (no 3PAO engagement) |
| Costs | Membership ($1,500+) + PMO Fee ($9,000–$17,000 depending on revenue) |
| APL listing | Yes |

### GovRAMP Ready

| Dimension | Detail |
|-----------|--------|
| Controls assessed | Minimum mandatory requirements for target impact level |
| Assessment method | 3PAO Readiness Assessment Report (RAR) |
| 3PAO required | Yes |
| Documentation required | 50% complete at submission; 100% by Authorized |
| ConMon | Monthly + Annual |
| Typical timeline | Longer than Core (requires 3PAO engagement) |
| Costs | Membership + 3PAO fees (market rate) + Ready review fee ($500–$3,750) |
| APL listing | Yes |

### GovRAMP Authorized

| Dimension | Detail |
|-----------|--------|
| Controls assessed | All required controls at target impact level (Low, Moderate, High) |
| Assessment method | Full 3PAO Security Assessment Report (SAR) |
| 3PAO required | Yes |
| Government sponsor | Required (direct government sponsor or GovRAMP Approvals Committee) |
| Documentation required | 100% complete |
| ConMon | Monthly + Annual |
| Typical timeline | Longest of all paths |
| Costs | Membership + 3PAO fees + Authorized review fee ($1,500–$7,500) + ConMon monthly fee |
| APL listing | Yes (as Authorized) |

---

## Government Sponsorship

### What Is a Government Sponsor?

For GovRAMP Authorized status, an authorizing government official (at a state, local,
education, tribal, or special district organization) must review and approve the
provider's security package.

### Two Sponsorship Options

**Option 1: Direct Government Sponsor**
A specific government agency agrees to sponsor the provider. The sponsoring agency
reviews the security package and signs off on the authorization.

Requirements for the sponsoring government (from the GovRAMP Provider Sponsor
Requirements document):
- Must be an active GovRAMP member (or become one)
- Must designate a responsible government official
- Must review and accept the provider's security package

**Option 2: GovRAMP Approvals Committee**
If a provider cannot secure a direct government sponsor, the GovRAMP Approvals
Committee (composed of active state and local government representatives) can serve
as the appointed sponsor and confirm the package meets all requirements. This results
in **GovRAMP Provisionally Authorized** status until a formal government sponsor
assumes responsibility.

---

## Progressing Snapshot: When to Use It

The Progressing Snapshot is **not a verified status**. Products are listed on the
Progressing Product List, not the Authorized Product List. Use this pathway when:

- The provider is in early stages of building a security program
- The organization wants PMO guidance before committing to 3PAO assessment costs
- The organization wants to appear on the GovRAMP product list in a non-verified
  capacity while working toward Core, Ready, or Authorized
- The provider is exploring what level of effort full authorization will require

**January 1, 2026 Change:** Products on the Progressing List must demonstrate active
advancement toward a verified status. Products failing to show progress are subject to
escalation and potential removal from the Progressing List.

---

## Appeals and Exceptions

The GovRAMP **Appeals Committee** handles:
- Conflict-of-interest claims
- Disagreements over status determinations
- Requests for exceptions

The Appeals Committee is composed of at least five members appointed by the Board,
including at least one Board member. The Executive Committee may appoint subject matter
experts to assist with specific claims.

---

## Glossary of Key Terms

| Term | Definition |
|------|-----------|
| APL | Authorized Product List — GovRAMP's public listing of products with verified security status |
| 3PAO | Third-Party Assessment Organization — an independent assessor accredited to conduct GovRAMP assessments |
| SLED | State, Local, Education, and tribal governments — GovRAMP's primary target customer base |
| PMO | Program Management Office — GovRAMP's PMO is serviced by RAMPQuest, powered by Knowledge Services |
| ConMon | Continuous Monitoring — ongoing security reporting obligations for authorized products |
| RAR | Readiness Assessment Report — 3PAO deliverable for the Ready status path |
| SAR | Security Assessment Report — 3PAO deliverable for the Authorized status path |
| SSP | System Security Plan — the foundational security documentation for a service provider |
| POA&M | Plan of Action and Milestones — tracks open findings and remediation plans |
| IRP | Incident Response Plan — required at all authorization levels including Core |
| CP | Contingency Plan — required at all authorization levels including Core |
| CJI | Criminal Justice Information — data type requiring the CJIS Overlay at Moderate impact level |
| Fast Track | Expedited GovRAMP authorization pathway for FedRAMP-authorized providers |
| TX-RAMP | Texas Risk and Authorization Management Program — recognizes GovRAMP with reciprocity |

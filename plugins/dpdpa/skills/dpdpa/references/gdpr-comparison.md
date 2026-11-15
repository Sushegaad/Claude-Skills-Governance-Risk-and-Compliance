# DPDPA vs GDPR - Compliance Comparison Reference

For compliance teams that are GDPR-experienced and are mapping obligations under
India's Digital Personal Data Protection Act, 2023.

---

## Quick Terminology Map

| GDPR Term | DPDPA Equivalent |
|-----------|-----------------|
| Data Controller | **Data Fiduciary** |
| Data Subject | **Data Principal** |
| Data Processor | **Data Processor** (same) |
| High-Risk Controller | **Significant Data Fiduciary (SDF)** |
| Supervisory Authority / DPA | **Data Protection Board of India (DPBI)** |
| Lawful Basis / Legal Ground | **Ground for Processing** |
| Legitimate Interests | **No equivalent** - does not exist under DPDPA |
| Adequacy Decision | **No equivalent** - DPDPA uses blacklist, not whitelist |
| Standard Contractual Clauses | **No equivalent prescribed** - contractual safeguards required but SCC-style mechanism not prescribed |
| Privacy Notice | **Notice** (Section 5 + Rule 3) |
| Data Subject Rights | **Data Principal Rights** (Sections 11–14) |
| Data Protection Impact Assessment | **DPIA** (SDFs only, Rule 13) |
| Data Protection Officer | **Data Protection Officer** (SDFs only; must be India-resident) |
| Right to be Forgotten | **Right to Erasure** (Section 12(3) - narrower than GDPR) |

---

## 8 Substantive Differences

### 1. Scope: Digital-Only vs. All Personal Data

| Dimension | GDPR | DPDPA |
|-----------|------|-------|
| Data medium | ALL personal data - digital, paper, audio, visual | Only **digital personal data** (or data subsequently digitised) |
| Physical records | Covered | Excluded unless digitised |
| Verbal data | Covered if recorded | Only if converted to digital form |

**Implication:** Organisations can maintain some non-digital records outside DPDPA scope. However, any digitisation triggers DPDPA applicability. Organisations should not rely on keeping data non-digital as a compliance strategy - most operational data is inherently digital.

---

### 2. Lawful Bases: Closed List vs. Balancing Test

| Dimension | GDPR | DPDPA |
|-----------|------|-------|
| Number of lawful bases | 6 (consent, contract, legal obligation, vital interests, public task, legitimate interests) | **2** (consent; or nine enumerated "legitimate uses", Section 7(a)–(i)) |
| Legitimate interests | Yes - balancing test: organisation's interest vs. individual rights | **No** - does not exist |
| Contract performance | Yes - broad category | Narrow: covered only where it falls under employment (Section 7(i)) or specified purpose (Section 7(a)) |
| Flexibility | High - large class of processing can be justified on legitimate interests | Low - any processing not fitting the nine clauses requires consent |

**Implication:** GDPR practitioners who rely on **legitimate interests** for analytics, fraud prevention, marketing to existing customers, or B2B data processing must map these use cases to either **consent** or one of the nine Section 7 clauses under the DPDPA. Most commercial analytics, profiling, and B2C marketing will require explicit consent.

---

### 3. Consent: "Unconditional" vs. "Freely Given"

| Dimension | GDPR | DPDPA |
|-----------|------|-------|
| Consent standard | Freely given, specific, informed, unambiguous | Free, specific, informed, **unconditional**, unambiguous |
| Bundled consent | Problematic under GDPR but not explicitly banned | **Explicitly prohibited** - consent cannot be bundled with service provision |
| Conditional processing | Possible via other lawful bases (contract, legitimate interests) | If service cannot be provided without consent, consent validity is questionable |
| Mechanism | Clear affirmative action (no pre-ticked boxes) | Same: clear affirmative action |

**Implication:** The DPDPA's addition of "unconditional" and explicit bundling prohibition is stricter than GDPR in practice. An "accept our privacy policy to use this app" mechanism is more clearly unlawful under DPDPA than under GDPR (where it might survive if the processing is genuinely necessary for the contract).

---

### 4. Cross-Border Data Transfers: Blacklist vs. Whitelist

| Dimension | GDPR | DPDPA |
|-----------|------|-------|
| Default position | **Restrictive** - transfers only to countries with adequacy or via SCCs, BCRs, etc. | **Permissive** - transfers allowed to all countries except notified restricted ones |
| Transfer mechanism required | Adequacy decision, SCCs, BCRs, binding corporate rules, derogations | **None required** - no adequacy assessment, no SCC-equivalent |
| Current restricted list | EU publishes list of adequate and inadequate countries | **No restricted countries notified** (April 2026) |
| Contractual documentation | Detailed SCC/BCR documentation required | Contractual safeguards with recipients recommended but not yet specified |
| Legal certainty | High (established mechanism) | Lower (uncertainty until blacklist notifications) |

**Implication:** For organisations currently applying GDPR SCCs, DPDPA does not require equivalent mechanisms. However, the lack of formal restrictions does not mean absence of accountability. Future notifications could restrict transfers, and organisations should maintain data flow maps and basic contractual protections.

---

### 5. Right to Erasure: Narrower vs. Broader

| Dimension | GDPR Art. 17 | DPDPA Section 12(3) |
|-----------|-------------|---------------------|
| Trigger grounds | Data no longer necessary; consent withdrawn; objection; unlawful processing; child consent; legal obligation | Data **no longer necessary for the specified purpose** |
| Right against profiling | Yes - right to erasure when objecting to profiling | No equivalent right to object to profiling |
| Historical/archival data | Specific exemptions for public interest archiving | Research/archiving exemption (Section 17(2)(b)) |
| Children's "fading memory" | Enhanced right for minors' data posted online | Not explicitly addressed |

**Implication:** DPDPA's erasure right is narrower and more formulaic. The primary trigger is purpose fulfilment. Organisations can retain data lawfully so long as the specified purpose persists and retention is legally required or operationally necessary.

---

### 6. Data Protection Officer: SDFs Only vs. Broad Requirement

| Dimension | GDPR | DPDPA |
|-----------|------|-------|
| Mandatory for | Public authorities + large-scale systematic monitoring + large-scale special category processing | **Significant Data Fiduciaries only** (government-designated) |
| Location requirement | No mandatory location requirement | Must be **resident in India** |
| Role | Advisory; must report to highest management; protected from dismissal for role performance | Sole representative before Board; Data Principal grievance contact |
| Voluntary DPO | Not prohibited; recommended for smaller processors | Not addressed |

**Implication:** Most organisations that were required to appoint a GDPR DPO may NOT be required to appoint one under DPDPA (only if designated as SDF). However, assigning a senior privacy professional in an equivalent role is strongly recommended for compliance governance and Board interaction readiness.

---

### 7. Children's Data: Stricter Age Threshold and Broader Prohibitions

| Dimension | GDPR | DPDPA |
|-----------|------|-------|
| Age threshold | **16 years** (default; member states may lower to 13) | **18 years** (uniform; no variation) |
| Parental consent age range | 13–16 (varies by member state) | **All under 18** require verifiable parental consent |
| Behavioural monitoring | Permitted with appropriate legal basis | **Prohibited** for all children (Section 9(2)) |
| Targeted advertising | Permitted with appropriate consent/legal basis | **Prohibited** for all children (Section 9(2)) |
| Verification mechanism | Not specifically prescribed | Prescribed: DigiLocker, government tokens, existing data (Rule 10) |

**Implication:** DPDPA's 18-year threshold is more protective than GDPR's for the 16–17 age band. Organisations operating platforms accessible to teenagers must implement robust age-gate mechanisms in India, even if they have successfully managed GDPR compliance for 16–17 year olds in the EU.

---

### 8. Enforcement Model: Centralised Single Body vs. Decentralised Multi-Authority

| Dimension | GDPR | DPDPA |
|-----------|------|-------|
| Enforcement bodies | 27+ national DPAs + EDPB coordination | **Single** Data Protection Board of India |
| Proactive investigation | DPAs can investigate proactively | Board is primarily complaint-driven; no stated proactive investigation power |
| Guidance authority | DPAs issue binding guidance and opinions | **Board has no guidance-issuing power** - guidance comes from MeitY (non-binding) |
| One-stop-shop | GDPR one-stop-shop for cross-border processing | Not applicable (single authority) |
| Max penalty | **€20M or 4% of global annual turnover** | **₹250 crore (~USD 30M)** - fixed amount; no turnover-linked cap |
| Penalty impact on large companies | Very high (4% of global turnover for large multinationals) | Fixed INR amounts - less severe for large global companies, but not trivial for mid-sized organisations |

**Implication:** GDPR penalties are more financially severe for global multinationals (% of turnover). DPDPA fixed-amount penalties are more predictable but may be less deterrent for large tech companies. For Indian SMEs and startups, DPDPA penalties could be existential (₹200–250 crore against a startup). The Board lacks proactive investigation and guidance-issuing powers - a significant structural difference from GDPR DPAs.

---

## Common GDPR-to-DPDPA Compliance Gaps

| GDPR-compliant practice | DPDPA status | Action needed |
|------------------------|-------------|---------------|
| Relies on "legitimate interests" for marketing analytics | **INVALID** - no equivalent basis | Obtain consent or cease processing |
| Privacy notice in T&Cs | **NON-COMPLIANT** - notice must be standalone, independent (Rule 3) | Separate, redesign notice |
| DPO based outside India | **NON-COMPLIANT** (for SDFs) | Appoint India-resident DPO if SDF-designated |
| SCCs for international transfers | **Not required, but not prohibited** | No action required; maintain contractual record |
| Age threshold 16 years | **NON-COMPLIANT** - DPDPA requires 18 | Implement 18-year age gate in India |
| Pre-ticked consent boxes | **NON-COMPLIANT** - same standard as GDPR | Remove; implement affirmative opt-in |
| DPIA for large-scale processing | Only for **SDFs** | Defer unless SDF designation received |
| Consent withdrawal by email | **LIKELY NON-COMPLIANT** - must be as easy as giving consent | Implement one-click/in-app withdrawal |
| Data processing agreements with vendors | Required (Section 8(2)) - similar to GDPR Art. 28 | Update contracts with DPDPA-specific terms |
| Annual data audit | Only for **SDFs** | Defer unless SDF designation received |

---

## Rights Comparison

| Right | GDPR | DPDPA Section | Notes |
|-------|------|--------------|-------|
| Right of access | Art. 15 - detailed portability and access rights | Section 11 | DPDPA access right is narrower; no explicit portability right (data portability absent) |
| Right to rectification | Art. 16 | Section 12(1) | Equivalent |
| Right to erasure | Art. 17 | Section 12(3) | DPDPA narrower - purpose fulfilment only; no objection-based erasure |
| Right to restrict processing | Art. 18 | **No equivalent** | Not provided under DPDPA |
| Right to data portability | Art. 20 | **No equivalent** | Not provided under DPDPA |
| Right to object | Art. 21 | **No equivalent** | Not provided under DPDPA (limited: Data Principal may object to Section 7(a) processing - voluntary data provided for a purpose - per Section 7(a) qualifier "unless specifically objected") |
| Rights in automated decision-making | Art. 22 | **No equivalent** | Not provided under DPDPA |
| Right to grievance redressal | Not explicit (complaint to DPA available) | Section 13 - explicit | Mandatory grievance mechanism at Fiduciary level; Board as escalation |
| Right to nominate | **No equivalent** | Section 14 | Unique to DPDPA |

**Key absences from DPDPA vs. GDPR:**
- No right to data portability
- No right to restrict processing
- No right to object to processing generally
- No rights against automated decision-making and profiling

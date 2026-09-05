# GDPR Regulatory Updates — 2024–2026

This file captures material GDPR and EU data protection developments from mid-2024 through May 2026.
Load this file when questions touch any of the topics below, or when providing current-affairs compliance advice.

---

## 1. EU–US Data Privacy Framework (DPF) — Transfer Mechanism Status

**Current status (May 2026): Valid but legally challenged — maintain SCC fallback.**

The DPF adequacy decision (Commission Implementing Decision, 10 July 2023) remains in force.

**First judicial challenge dismissed:** The EU General Court dismissed MP Philippe Latombe's challenge on 3 September 2025, finding US law adequately limits bulk data collection and that the Data Protection Review Court (DPRC) is sufficiently independent.

**CJEU appeal registered (Case C-703/25 P):** Latombe appealed on 31 October 2025. No hearing date as of May 2026. The CJEU remains the ultimate threat to the DPF — as it was to Safe Harbour (*Schrems I*, 2015) and Privacy Shield (*Schrems II*, 2020).

**PCLOB incapacitated:** Three of five Privacy and Civil Liberties Oversight Board members were removed by the Trump administration in January 2025. The PCLOB lost its quorum. This is structurally significant: the PCLOB conducts the annual EO 14086 compliance review and plays a role in DPRC judge appointments. The EDPB has flagged PCLOB incapacity as a concern for DPF's ongoing adequacy.

**Practical compliance advice:**
- Controllers may rely on the DPF for EU–US transfers, but should **treat SCCs as a parallel or backup safeguard** given the CJEU appeal risk. A *Schrems III* ruling would require immediate reversion to SCCs/BCRs.
- Maintain a register of which US vendors hold DPF certification (searchable at dataprivacyframework.gov).
- In privacy notices, describe the transfer mechanism as "EU–US Data Privacy Framework (or Standard Contractual Clauses as an alternative safeguard)."

**UK–US transfers:** The UK–US Data Bridge (UK extension of DPF) remains operative; same legal uncertainty applies.

---

## 2. UK Data (Use and Access) Act 2025

**Royal Assent: 19 June 2025. UK GDPR is now materially diverging from EU GDPR.**

The DPDI Bill died when Parliament was dissolved in May 2024. The Labour government's replacement — the **Data (Use and Access) Act 2025 (DUAA)** — received Royal Assent on 19 June 2025.

### Key changes relevant to GDPR compliance guidance

**A. Recognised Legitimate Interests (new)**
The DUAA creates a statutory list of purposes that automatically satisfy the legitimate interests basis (equivalent to UK GDPR Art. 6(1)(f)) **without requiring a balancing test**:
- National security and public security
- Prevention, investigation, detection, or prosecution of criminal offences
- Safeguarding of children and at-risk adults
- Emergencies and safeguarding of life
- Democratic engagement / electoral integrity
- Public interest

This is an **addition** to — not a replacement of — the standard legitimate interests basis, which still requires the three-step LIA.

**B. International transfers — different standard**
The DUAA replaces the EU's "essentially equivalent" adequacy test with a more flexible risk-based standard: the destination country must provide "not materially lower" data protection. The ICO maintains the list of "data protection test" approved countries. This may expand the range of countries UK organisations can transfer to without SCCs.

**C. Senior Responsible Individual (SRI)**
The DUAA introduces a "Senior Responsible Individual" role for some organisations, which modifies (in some cases replaces) the mandatory UK DPO requirement. When advising UK organisations on DPO obligations, check whether they are subject to the SRI provisions or the DPO requirement.

**D. Automated decision-making**
The equivalent of EU Art. 22 is retained but with less prescriptive safeguards. The obligation to provide information about automated decision-making, offer human review, and allow objection is maintained — but the precise trigger conditions differ.

**E. What did NOT change significantly**
Cookie consent rules (consent still required for non-essential cookies), core data subject rights, the Art. 5 principles, and Art. 32 security requirements are substantively unchanged.

### EU adequacy of the UK
The EU adequacy decisions for the UK were renewed on **19 December 2025**, valid through **27 December 2031**. EU-to-UK transfers remain straightforward without SCCs or BCRs for the foreseeable future.

---

## 3. EDPB Opinion 28/2024 — AI Models and GDPR (December 2024)

**Adopted: 17 December 2024. Critical reading for any AI + GDPR question.**

The EDPB answered three questions raised by the Irish DPC about AI model development and deployment.

### Question 1: When is an AI model "anonymous"?

AI models trained on personal data are **not automatically anonymous**. Providers cannot simply declare a trained model anonymous without evidence.

For a model to qualify as anonymous, it must be "very unlikely" that:
1. **Individuals whose data trained the model can be re-identified** from model outputs or architecture; AND
2. **Personal data can be extracted from the model** via queries (the model must not "leak" training data through inference attacks).

The EDPB sets a **high threshold** — this is a context-sensitive, technology-dependent assessment. Controllers should document their anonymity assessment and test against known extraction techniques.

**Practical implication:** Organisations developing LLMs or other AI models on personal data cannot treat post-training as automatic anonymisation. If the model retains any meaningful probability of producing outputs that reveal specific training data, it is not anonymous.

### Question 2: Can legitimate interests (Art. 6(1)(f)) be used for AI model training?

**Yes, in principle.** The EDPB confirmed that:
- Commercial interests — including AI development — can constitute legitimate interests
- The full three-step LIA (legitimate interest → necessity → balancing) must still be conducted
- The **balancing step** must weigh: scale and sensitivity of training data; whether data subjects had reasonable expectations their data would be used; whether the training is for a materially different purpose than the original collection

**Practical implication:** Scraping public web data to train AI on personal data requires a documented LIA. The "reasonable expectations" factor will weigh heavily against training on data scraped without any user expectation of AI model training.

### Question 3: Consequences of unlawful initial training for downstream AI deployment

If an AI model was trained on **unlawfully processed personal data**:
- If the model achieves **genuine anonymity** (high threshold — Question 1), the unlawfulness of initial training does not infect downstream deployment.
- If the model **does not** meet the anonymity threshold, downstream DPAs can take enforcement action against providers deploying the model — **even if they did not participate in the original unlawful training**.

**Practical implication:** Organisations using third-party foundation models should conduct due diligence on whether the model was trained lawfully. Reliance on a vendor's assertion of compliance without independent assessment may expose the downstream deployer to risk.

---

## 4. CJEU Rulings Since Mid-2024

### 4.1 Pseudonymised Data as "Relative Personal Data" — SRB v. EDPS (September 2025)

**Case C-413/23 P, 4 September 2025 — landmark ruling on the definition of personal data.**

The CJEU confirmed that determining whether data is "personal data" is a **relative, recipient-specific assessment**. Pseudonymised data is not automatically personal data in the hands of every recipient — it depends on whether the **specific controller or recipient** has means **reasonably available** to re-identify individuals.

**Key implications:**
- **Anonymisation defences:** A controller may be able to demonstrate that pseudonymised data it shares is genuinely non-personal from the recipient's perspective, if the re-identification key is not accessible to and cannot be obtained by that recipient.
- **Art. 17 erasure:** A controller that has deleted the re-identification key and genuinely cannot reconstruct individuals from the remaining data may be able to argue it has effectively fulfilled erasure obligations.
- **Practical caveat:** The EDPB is developing updated anonymisation guidelines in response to this ruling. The threshold for demonstrating that a recipient lacks "reasonably available" means remains demanding. Retain legal review before relying on this argument.

### 4.2 Platform Operators as Controllers for User-Generated Content — Russmedia Digital (December 2025)

**Case C-492/23, 2 December 2025.**

The CJEU held that an **online marketplace operator qualifies as a data controller** for personal data — including special category data — published in user-generated advertisements, even where the operator does not create or select the content.

**Key implications:**
- **Proactive duty:** Platforms must implement technical measures to **prevent** the unlawful publication of special category data (e.g., health data, sexual orientation) in user ads — not just respond after publication.
- **Scope:** Applies to classified ad platforms, marketplaces, job boards, housing platforms — any platform where users post content that may include others' personal data.
- **Practical steps:** Technical pre-screening, content moderation for sensitive categories, clear terms prohibiting sensitive data in listings, and a documented process for flagging and removing non-compliant content.

### 4.3 Targeted Advertising and Data Minimisation — Meta/Schrems (October 2024)

The CJEU confirmed that targeted advertising is not per se unlawful under GDPR. However, the **data minimisation principle (Art. 5(1)(c))** requires that personal data processed for advertising must be processed for a **bounded duration** — data cannot be accumulated and processed indefinitely for advertising purposes. Controllers must implement time-limits on advertising data use and document the rationale for any extended retention.

---

## 5. EDPB Guidelines and Enforcement Reports

### 5.1 Guidelines 1/2024 on Legitimate Interests (Art. 6(1)(f))

**Published for consultation: 8 October 2024. Replaces WP29 Opinion 06/2014.**

The EDPB overhauled guidance on the three-step LIA:

**Step 1 — Legitimate interest:**
- Must be **lawful, clearly and precisely articulated, real and present** — not speculative
- Commercial interests qualify (consistent with CJEU case law)
- Future interests or vague operational benefits do not qualify

**Step 2 — Necessity:**
- Processing must be **genuinely necessary** for the stated interest
- If the same interest can be served with less data or less intrusive means, necessity fails
- The necessity link must be direct — not speculative or based on commercial preference

**Step 3 — Balancing:**
- Factors weighing against: special category data; vulnerable data subjects (children, patients); large scale; sensitive context; reasonable expectation of data subjects
- Factors weighing in favour: controller is in a trusted position; data subjects have a relationship with the controller; processing is predictable
- Must document the balancing assessment in the RoPA or a LIA document retained as evidence

**Practical implication:** Any existing LIA assessments should be reviewed against this guidance — particularly the "real and present" interest requirement and the reasonable expectations element.

### 5.2 Guidelines 3/2025 on DSA–GDPR Interplay (September 2025)

**Published for consultation: 12 September 2025. Critical for online platforms.**

Key compliance points:
- Every **DSA-mandated processing operation still needs a valid GDPR lawful basis** — the DSA does not create new GDPR lawful bases
- The **DSA prohibition on targeted advertising to minors** means platforms must implement age assurance and disable profiling-based targeting for under-18 users
- **Recommender systems** must respect GDPR profiling rules (Art. 22 where applicable)
- **Art. 9 special category data cannot be used for ad targeting** regardless of DSA context — even where DSA does not explicitly prohibit it

### 5.3 CEF 2025 — Right to Erasure Coordinated Enforcement

**EDPB report adopted: 18 February 2026. 32 DPAs participated, 764 controllers assessed.**

**Top compliance gaps identified:**
1. **Missing documented procedures** — Controllers without clear internal processes for receiving, logging, and responding to erasure requests
2. **Insufficient staff training** — ~20% provide no regular refresher training; leading to missed deadlines and incorrect exception application
3. **Inadequate data subject information** — 13 DPAs found Art. 13/14 disclosures did not adequately describe the right to erasure
4. **Technical deletion gaps** — Controllers unable to identify and delete data from all systems, especially legacy databases, analytics platforms, and backup archives

**Recommended actions:**
- Maintain a documented Art. 17 procedure with owner, SLAs, exceptions checklist, and escalation path
- Include backup and archive deletion in the erasure procedure — with a defined timeframe
- Run annual training specifically on Art. 17 edge cases (legal holds, freedom of expression exception, archiving in public interest)
- Confirm all Art. 13/14 notices explicitly name erasure as an available right with contact method

**CEF 2026:** The next coordinated enforcement action will focus on **transparency and information obligations (Arts. 13–14)** — update privacy notices to pre-empt scrutiny.

---

## 6. ePrivacy and Cookie Tracking

**ePrivacy Regulation proposal formally withdrawn: 11 February 2025.**

After eight years, the Commission withdrew the ePrivacy Regulation proposal. Cookies and tracking remain governed by the **ePrivacy Directive 2002/58/EC** as transposed nationally — heterogeneous and unharmonised.

**Digital Omnibus (November 2025 proposal — not yet law):** The Commission proposes integrating cookie consent rules directly into GDPR via new Articles 88a and 88b. Trilogue expected mid-to-late 2026. Not yet in force.

**Current tracking landscape (May 2026):**
- Consent is still required for non-essential cookies/tracking (all EU Member States)
- CNIL (France), Belgian DPA, German authorities continue aggressive cookie enforcement
- The EDPB finalised **Guidelines 02/2023 on Art. 5(3) ePrivacy Directive** in October 2024, extending cookie consent requirements to tracking pixels, fingerprinting, and other techniques that access or store information on user devices — not just HTTP cookies

**Cookie dark patterns remain a top enforcement priority:**
- Reject button must be as prominent as Accept (equal visual weight)
- Pre-ticked consent boxes violate Art. 7
- Cookie walls (conditioning service access on consent) are presumptively non-compliant
- Major fines: Google €325M (CNIL, September 2025); SHEIN €150M (CNIL, 2025)

---

## 7. Major Enforcement Decisions — Key Precedents

| Decision | DPA | Fine | Key Precedent |
|---|---|---|---|
| LinkedIn (October 2024) | Irish DPC | €310M | All three lawful bases (consent, contract, LI) simultaneously invalid for advertising and analytics targeting |
| Uber (August 2024) | Dutch AP | €290M | SCCs required for transfers to non-EEA entities even when the importer is also subject to GDPR via Art. 3(2) |
| TikTok (May 2025) | Irish DPC | €530M | China data transfers without adequate safeguards; Art. 13 transparency failures; discovered undisclosed China server storage |
| Google cookies (September 2025) | CNIL | €325M | Invalid cookie consent; reject harder than accept (dark pattern) |
| SHEIN (2025) | CNIL | €150M | Tracking cookies placed before consent |
| OpenAI/ChatGPT fine annulled (March 2026) | Court of Rome | — | First major judicial reversal of an AI-related GDPR fine; Italian Garante's €15M fine overturned |

**Cumulative enforcement (May 2026):** Total GDPR fines exceeded €7.1 billion. €1.2 billion issued in 2025 alone. Ireland remains dominant by fine value (DPC: cumulative €4.04 billion).

---

## 8. Digital Omnibus — Proposed GDPR Amendments (November 2025)

**Status: Proposal only. None of the following are yet law. Formal adoption unlikely before 2027.**

The European Commission's Digital Omnibus (published 19 November 2025) proposes the most significant set of GDPR amendments since the regulation entered into force. Key proposals:

| Proposal | Current GDPR | Proposed |
|---|---|---|
| **RoPA threshold** | Organisations < 250 employees exempt | Raised to < 750 employees (with high-risk carve-out) |
| **AI as legitimate interest** | Not explicitly addressed | Processing for AI development/deployment recognised as legitimate interest, subject to necessity and proportionality |
| **Relative anonymisation** | Not explicitly addressed | Data may be treated as anonymous from the perspective of a specific controller even if a third party could re-identify |
| **DSARs — abuse** | "Manifestly unfounded or excessive" | Clearer permission to reject requests where data subjects pursue objectives outside GDPR scope |
| **Cookie rules** | ePrivacy Directive (national transposition) | New Arts. 88a/88b integrating cookie consent directly into GDPR |
| **Biometric auth (Art. 9)** | No specific derogation | New derogation for biometric data used for authentication where template remains under the individual's sole control |

**When advising clients:** Note these proposals explicitly and flag that they have not entered into force. Compliance strategies should be built on current law, with awareness that the landscape may shift from 2027 onward.

---

## 9. Biometric Data and Facial Recognition — EDPB Opinion 11/2024

**Adopted: May 2024. Highly relevant for FRT deployments at airports, venues, and premises.**

The EDPB ruled that facial recognition for passenger flow management at airports fails GDPR compliance if biometric templates are stored on systems controlled by the operator (airline, airport, lounge).

**To comply with Art. 9:** The biometric template must remain under the **passenger's sole control** — stored on a personal device with the decryption key controlled by the passenger only. The operator must perform the matching operation locally without retaining the template.

**Consent validity note:** Consent cannot be considered freely given where the alternative to biometric processing (traditional document check) is made materially less convenient or accessible. If biometric processing is optional, the non-biometric option must be genuinely equivalent.

**Scope beyond airports:** The same principles apply to biometric authentication at any venue or premises — gym entry, workplace access, events — where the data subject's alternative (physical key, card, pin, document) must remain genuinely accessible without detriment.

---

## August–September 2026 additions (verified 2026-09-05)

### Uber Art. 22 fine — €824,990,000 (Dutch AP, August 21, 2026)
The Autoriteit Persoonsgegevens fined Uber B.V. and Uber Technologies Inc. €824,990,000 — the second-largest GDPR fine ever (behind Meta's €1.2bn, 2023) and the AP's fourth against Uber (2018: €600K; 2023: €10M; 2024: €290M). Findings: between 2018 and 2022 Uber fully automatically deactivated driver accounts (temporarily on fraud suspicion or low ratings; permanently on persistent low ratings) with no human assessment, breaching the GDPR prohibition on solely automated decision-making with significant effects (Art. 22), and gave drivers insufficient information about the automated decisions. One-stop-shop mechanics: 171 French drivers complained via Ligue des droits de l'Homme to CNIL; the AP led as Uber's EU-HQ authority and aligned the decision with other supervisors. Uber has filed an appeal. AP deputy chair Monique Verdier: "A computer should not make decisions on its own that have major consequences for you. These decisions should have been looked at first by a human being."

**Advisory implications:** treat driver/worker deactivation, account termination, fraud-flagging and similar platform decisions as Art. 22 territory; require documented meaningful human review (not rubber-stamping), Art. 13/14 disclosure of the logic and consequences, and a contestation channel (Art. 22(3)).

### EDPB Guidelines 02/2026 on anonymisation (draft, July 7, 2026)
Version 1.0 adopted for consultation (open until October 30, 2026); once final it replaces WP29 Opinion 05/2014. Key positions: a relative approach to identifiability following CJEU EDPS v SRB — the same dataset can be personal data for one holder and anonymous for another; anonymisation is assessed against means reasonably likely to be used; the singling-out / linkability / inference criteria framework is retained.

### EDPB Guidelines 03/2026 on web scraping in the context of generative AI (draft, July 7, 2026)
Adopted the same plenary; consultation until October 30, 2026. Positions: consent is generally not viable at scale, making legitimate interest the realistic basis subject to strict balancing and mitigations; controllers should publish detailed public privacy notices and facilitate rights including pre-collection opt-out mechanisms; coverage extends to first-party scraping, contracted scraping, and purchased broker datasets.

### Breach-notification template status
The EDPB's draft common Art. 33 notification template (adopted June 8, 2026) closed consultation on August 5, 2026; no final version has been adopted yet — do not present it as operative.


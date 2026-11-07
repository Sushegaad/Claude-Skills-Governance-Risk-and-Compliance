# EU AI Act — GPAI, Governance, and Cross-Framework Reference

## GPAI Model Obligations

### Art. 3(63) — What Qualifies as a GPAI Model

A model qualifies as GPAI when **all** of the following apply:
- Trained with **large amounts of data** using **self-supervision at scale**
- Displays **significant generality** — competently performs a wide range of distinct tasks
- Can be used for multiple **different purposes** regardless of how placed on market
- **Excludes:** Models in pre-release R&D phase not yet placed on market

**Key implication:** Many foundation models (large language models, multimodal models) are GPAI models. A system built on such a model may be a "GPAI system" (Art. 3(64)).

---

### Art. 53 — Universal GPAI Provider Obligations (applies from 2 August 2025)

ALL GPAI model providers (regardless of size or systemic risk status) must:

**1. Technical Documentation (Annex XI content):**
- General description: intended purpose, types of tasks, interaction modes
- Development process: data sources, data processing and filtering, training techniques, compute used
- Testing and evaluation: benchmarks, evaluations, safety testing results
- Known limitations and foreseeable risks
- Responsible disclosure practices; contact information for reporting issues
- Keep up-to-date; provide to AI Office and national authorities on request

**2. Downstream Provider Information (Annex XII content):**
Document and make available to downstream AI system providers who integrate the GPAI model:
- Capabilities and limitations enabling compliance with their own obligations
- Integration instructions
- Security measures
- Evaluation results
- **Note:** Intellectual property protections are permitted — Annex XII information may be provided under reasonable commercial terms

**3. Copyright Compliance Policy (EU Directive 2019/790 Text and Data Mining):**
- Implement a policy to comply with EU copyright and related rights law
- Specifically: mechanisms to respect text and data mining opt-outs reserved by rights-holders under Art. 4(3) of Directive 2019/790
- Must be technically enforceable and publicly described

**4. Public Training Content Summary:**
- Draw up and make publicly available a sufficiently detailed summary of training content
- Must follow Commission-provided template
- Purpose: enable downstream providers and the public to understand what data was used

**Open-source / free-license exception:**
GPAI model providers releasing under open-source/free licenses need only comply with obligations **3 and 4** (copyright policy and training summary) — **UNLESS** the model is later designated as having systemic risk, in which case full Art. 53 + Art. 55 obligations apply.

---

### Art. 51 — Systemic Risk Classification

**GPAI classification threshold (Commission guidelines, July 2025):**
Models trained with cumulative compute ≥ **10²³ FLOPs** are subject to GPAI obligations under Arts. 53–55.

**Automatic presumption of systemic risk when:**
Training compute exceeds **10²⁵ FLOPs** (floating point operations, cumulative across all training runs)

**Commission designation (independent of FLOPs threshold):**
Commission may also designate a model as having systemic risk based on:
- High-impact capabilities identified through model evaluation
- Broad reach across the EU
- Negative effects on public health, safety, public security, fundamental rights
- Other criteria in Annex XIII (including parameter count, domain specificity, user base)

**Provider notification obligation:**
Providers that know or should reasonably know their model meets or is approaching the threshold must:
- Notify the **AI Office** within **2 weeks** of reaching the threshold
- Notification triggers systemic risk assessment dialogue

**Dynamic threshold:**
Commission may amend the 10²⁵ FLOPs threshold via delegated acts as AI capabilities evolve.

**Rebuttable presumption:**
Providers may present evidence demonstrating systemic risk does not apply despite meeting the FLOPs threshold.

---

### Art. 55 — Systemic Risk GPAI Provider Additional Obligations (applies from 2 August 2025)

In addition to Art. 53 universal obligations, providers of systemic-risk GPAI models must:

**1. Model Evaluation:**
- Conduct model evaluation according to standardised protocols and state-of-the-art tools
- Includes adversarial testing (red-teaming) to identify and mitigate systemic risks
- May be conducted in cooperation with the AI Office

**2. Risk Assessment and Mitigation:**
- Assess and mitigate possible systemic risks arising from development, market placement, or deployment
- Systemic risks include: actual or foreseeable negative effects on public health, safety, public security, or fundamental rights at Union level, including serious societal disturbances

**3. Serious Incident Reporting:**
- Track, document, and promptly report any serious incidents and possible corrective actions
- Report to: **AI Office** and relevant **national competent authorities**
- Report without undue delay upon becoming aware

**4. Cybersecurity:**
- Ensure adequate cybersecurity protection for the model, its physical infrastructure, and the supply chain
- Includes protection against model theft, unauthorized access, adversarial attacks on model weights

**Compliance pathways for GPAI obligations:**
1. **GPAI Code of Practice** (primary pathway) — Final CoP published 10 July 2025, endorsed by Commission and AI Board 1 August 2025. Operates from 2 August 2025. Three chapters: (i) Transparency, (ii) Copyright, (iii) Safety and Security (systemic risk only). Non-signatories must demonstrate compliance by alternative means and explain their approach to the AI Office.
2. **Harmonised standards** — when published under Commission mandate; compliance gives presumption of conformity. **EN 18286:2026** (AI quality management, supporting Art. 17) became the first AI Act harmonised standard cited in the OJEU, announced October 15, 2026. The broader standardisation request deadline was revised to February 2027; prEN 18228 (risk management) is in final approval.
3. **Alternative adequate means** — provider demonstrates compliance through other methods acceptable to Commission.

**GPAI Code of Practice — Key obligations by chapter:**
- **Transparency chapter:** Model Documentation Form covering technical properties, training data, energy consumption, intended use; retained for 10 years. Downstream providers can request additional information within 14 days.
- **Copyright chapter:** Written copyright policy; compliance with robots.txt and technical opt-out protocols; rightsholder complaints mechanism; prohibition of infringing uses in acceptable use policies.
- **Safety and Security chapter (systemic risk only):** Safety and Security Framework established within **4 weeks of notification to the Commission** and **at least 2 weeks before market placement**; Safety and Security Model Reports submitted to AI Office before market placement; adversarial testing (red-teaming); serious incident reporting with staggered timelines; cybersecurity measures.

**Legacy GPAI models** (placed on market before 2 August 2025): deadline to comply is **2 August 2027**.

**Confirmed CoP signatories:** 22 full signatories per the Commission page updated October 7, 2026, including Amazon, Anthropic, Google, IBM, Microsoft, Mistral AI, and OpenAI. Note: xAI signed only the Safety and Security chapter, committing to demonstrate compliance with Transparency and Copyright by alternative means.

A **Signatory Taskforce**, chaired by the AI Office, facilitates coherent CoP implementation.

---

## Governance Structure

### AI Office (Arts. 64–68)

- Established within the **European Commission** (not an independent agency)
- Primary responsibility for: GPAI model oversight, monitoring, compliance assessment
- Conducts GPAI model evaluations — both compliance assessments and systemic risk investigations
- May request access to model weights, source code, training procedures, technical documentation
- Receives complaints from downstream providers against upstream GPAI providers
- Provides secretariat support for the AI Board
- Key contact point for: systemic risk notifications, Codes of Practice development, serious incident reports from GPAI providers
- Issues non-binding guidance; makes recommendations to the Commission
- Full enforcement powers over GPAI providers (information requests, model evaluations, fines) active since **2 August 2026**; procedural rules for Commission proceedings are set by **Implementing Regulation (EU) 2026/1755** (OJ July 21, 2026, in force August 10, 2026): model evaluations including API, source code, and model access; appointment and independence of experts; fine proceedings with preliminary findings and a right to be heard; access to file; five-year limitation period
- Enforcement in practice: first formal Art. 91 requests for information to GPAI providers reported in late August 2026; a further wave was announced October 14, 2026 covering security practices, external evaluation, and post-market monitoring; recipients have not been officially named

**Key guidance and actions published by the AI Office (chronological):**
- **4 Feb 2025:** Guidelines on prohibited AI practices under Art. 5 — with practical examples for all 8 categories
- **6 Feb 2025:** Guidelines on the definition of an AI system (Art. 3(1)) — clarifying what falls within the regulation's scope
- **July 2025:** Final GPAI Code of Practice published; GPAI scope guidelines published; Commission training data summary template published (for Art. 53(1)(d))
- **October 2025:** AI Act Whistleblower Tool launched — secure channel for reporting suspected violations
- **December 2025:** First draft of Code of Practice on Marking and Labelling of AI-generated Content
- **5 March 2026:** Second draft of the AI-generated content marking CoP
- **8 May 2026:** Draft guidelines on Art. 50 transparency obligations opened for consultation; three studies on Art. 5 prohibited practices published; three studies on technical marking/detection of AI-generated content published
- **19 May 2026:** Draft guidelines on high-risk AI system classification opened for public consultation
- **21 July 2026:** Implementing Regulation (EU) 2026/1755 published in the OJ (in force 10 August 2026): procedural rules for Commission proceedings against GPAI providers
- **Late August 2026:** First formal Art. 91 requests for information to GPAI providers reported (recipients not officially named)
- **12 October 2026:** Consultation opened on a draft implementing act for penalty-proceeding procedural rules (closing 9 November 2026)
- **14 October 2026:** Further wave of Art. 91 information requests announced, covering security practices, external evaluation, and post-market monitoring
- **15 October 2026:** EN 18286:2026 announced as the first AI Act harmonised standard cited in the OJEU (Art. 17 quality management)
- Note: the Art. 73 serious-incident reporting guidance remains a DRAFT (September 2025); no final version as of November 2026

### European Artificial Intelligence Board — AI Board (Art. 65)

**Composition:**
- One representative per EU Member State (3-year renewable mandate)
- European Data Protection Supervisor: permanent observer
- AI Office representative: attends, no voting rights
- Other national/Union authorities: invited case-by-case

**Governance:**
- Elects Chair from Member State representatives
- Adopts rules of procedure by two-thirds majority
- Two standing sub-groups: (i) market surveillance authorities; (ii) notifying authorities

**Core tasks:**
- Advise and assist Commission and Member States on consistent AI Act implementation
- Issue opinions, recommendations, and guidance on matters affecting multiple Member States
- Coordinate and facilitate information exchange between national authorities
- Facilitate development of harmonised technical standards
- Provide opinions on common specifications

### National Competent Authorities

Each Member State designates one or more national competent authorities with powers covering:
- **Market surveillance** (Art. 74): access to documentation, testing datasets, source code
- **Conformity assessment oversight**: notified body designation and monitoring
- **Enforcement and investigation**: power to require corrective action, withdrawal, recalls, fines
- **Annual reporting** to Commission on prohibited practices and enforcement actions

**Sector-specific authorities:**
- Financial supervisors for AI in banking and insurance
- Data protection authorities for law enforcement AI applications
- European Data Protection Supervisor for EU institutions' AI systems (Art. 77)

### Scientific Panel (Arts. 68–70)

- Independent expert body for GPAI matters
- Can alert AI Office about high-impact GPAI capabilities that may qualify for systemic risk designation
- Provides technical opinions to AI Office and Commission
- Issues views on model evaluation methodologies and capabilities assessment

### AI Regulatory Sandboxes (Art. 57)

- At least one operational per Member State by **2 August 2027** (deadline extended from 2 Aug 2026 by AI Omnibus)
- Enable controlled testing of innovative AI systems under regulatory supervision before market placement
- Participants: reduced administrative burden; authorities: supervisory insight
- Participation does not provide automatic compliance certification

---

## Post-Market Monitoring and Incident Reporting

### Art. 72 — Post-Market Monitoring System

**Applies to:** All high-risk AI system providers.

**Requirements:**
- Establish and document a post-market monitoring system proportionate to the nature of the AI technology and the risk
- Continuously collect, document, and analyze relevant performance data from deployed systems throughout the operational lifetime
- Monitor for risks to health, safety, and fundamental rights
- Inform risk management system updates (Art. 9)
- Must form part of technical documentation (Art. 11)

**Commission template:** Commission must publish a standardised template for post-market monitoring plans by 2 February 2026.

**Integration:** Existing post-market monitoring systems under sectoral legislation (medical devices, machinery, etc.) may be adapted and integrated to avoid duplication.

### Art. 73 — Serious Incident Reporting

**What constitutes a serious incident:**
Any incident or malfunctioning of a high-risk AI system that directly or indirectly leads or could lead to:
- Death of a person or serious damage to health of a person
- Serious and irreversible disruption to management/operation of critical infrastructure
- Infringement of obligations under Union law protecting fundamental rights
- Serious damage to property or the environment

**Who reports:**
- **Providers:** Report to market surveillance authority of Member State where incident occurred; within timeframe proportionate to severity (immediately for death-related incidents; within 15 days for other serious incidents; within 2 days for widespread safety threats)
- **Deployers:** Immediately notify provider, importer/distributor, AND market surveillance authority
- **GPAI systemic risk providers:** Report to AI Office and relevant national authorities

---

## Cross-Framework Mapping

### ISO 42001:2023 (AI Management System)

ISO 42001 is the primary AI management system standard complementing AI Act compliance.

| AI Act Article | ISO 42001 Element |
|---------------|-------------------|
| Art. 9 (Risk Management) | Clause 6.1, Annex A.6 (AI risk assessment), Annex B.3 |
| Art. 10 (Data Governance) | Clause 8.4, Annex A.8 (AI system operation), A.7 (AI data management) |
| Art. 13 (Transparency) | Annex A.4.1 (intended purpose documentation), A.4.2 |
| Art. 14 (Human Oversight) | Annex A.9.3, A.10.1 (human factors in AI) |
| Art. 15 (Accuracy/Robustness) | Annex A.9.4 (AI system performance), B.5 |
| Art. 17 (QMS) | Clause 4–10 PDCA management system structure |
| Art. 72 (Post-Market Monitoring) | Clause 9.1 (performance evaluation), A.10.3 |
| Art. 73 (Incident Reporting) | Annex A.10.5 (adverse impacts), Clause 10.2 |

**Practical guidance:** ISO 42001 certification can support demonstration of Art. 17 QMS compliance. ISO 42001's Statement of Applicability (SoA) process may be adapted for mapping conformity with AI Act requirements.

### NIST AI RMF (AI Risk Management Framework 1.0)

| AI Act Obligation | NIST AI RMF Function/Category |
|------------------|-------------------------------|
| Art. 17 QMS | GOVERN 1 (Policies, processes, accountability) |
| Art. 6 classification | MAP 1 (Context establishment), MAP 2 (Risk identification) |
| Art. 9 risk management | MAP 3, MEASURE 1–2 |
| Art. 10 data governance | MEASURE 2.5, 2.6 (Data and bias evaluation) |
| Art. 15 accuracy/robustness | MEASURE 2.1–2.4 (Testing, evaluation, red-teaming) |
| Art. 14 human oversight | MANAGE 2 (Human-AI interaction), GOVERN 4 |
| Art. 72 post-market monitoring | MANAGE 3, MANAGE 4 (Post-deployment operations) |
| Art. 73 incident reporting | MANAGE 4.1–4.2 (Incident response) |

### GDPR Alignment

The AI Act operates concurrently with GDPR — both apply when AI systems process personal data.

| Intersection | AI Act | GDPR |
|-------------|--------|------|
| Data governance | Art. 10 | Art. 5 (data quality principles), Art. 25 (data protection by design) |
| DPIA requirement | Art. 26 (deployer obligation reference) | Art. 35 |
| Special category data | Art. 10(5) (bias detection) | Art. 9 |
| Profiling definition | Art. 3(52) (matches precisely) | Art. 4(4) |
| Transparency to users | Art. 50 | Art. 13/14 (information notices) |
| Fundamental rights impact | Art. 27 (FRIA for public authorities) | Art. 35 DPIA |
| RBI system authorisation | Art. 5(1)(h) | Art. 9 + law enforcement exemptions |
| Supervisory authorities | Art. 77 (DPAs have access rights) | Supervisory authority under Chapter VI |
| Enforcement | Art. 99 (AI Act fines) | Art. 83 (GDPR fines up to 4% global turnover) |

**Key distinction:** GDPR governs personal data processing; the AI Act governs AI system development and deployment. Many AI systems trigger obligations under both — operators need dual compliance programmes.

---

## Penalties Reference — Art. 99

| Violation Type | Maximum Fine |
|----------------|--------------|
| **Prohibited AI practices** (Art. 5 violations) | €35,000,000 or **7%** of total worldwide annual turnover (higher applies) |
| **Provider/deployer/notified body violations** (Arts. 16, 22, 23, 24, 26, 31, 33, 34, 50) | €15,000,000 or **3%** of total worldwide annual turnover (higher applies) |
| **Incorrect/misleading information** to notified bodies or competent authorities | €7,500,000 or **1%** of total worldwide annual turnover (higher applies) |

**SME / startup / SMC reduction:** For SMEs, startups, and — per the AI Omnibus — **small mid-cap companies (SMCs)**, the lower of the fixed amount or percentage applies (Art. 99(6)).

**Proportionality factors:** Nature, gravity, and duration; prior infringements; company size and market share; intentionality; cooperation level; mitigation measures taken; actual damage caused.

**Member State reporting:** Annual reporting obligation to Commission on fines issued.

**GPAI enforcement:** AI Office enforces GPAI obligations. For systemic risk GPAI models, Commission itself may conduct investigations and impose fines directly.

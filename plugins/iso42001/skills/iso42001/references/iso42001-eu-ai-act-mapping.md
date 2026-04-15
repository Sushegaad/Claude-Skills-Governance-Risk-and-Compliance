# ISO/IEC 42001:2023 — EU AI Act Mapping

This reference maps ISO/IEC 42001:2023 clauses and Annex A controls to the requirements of the **EU AI Act — Regulation (EU) 2024/1689** (the Artificial Intelligence Act), published in the Official Journal of the EU on 12 July 2024 and in force from 1 August 2024.

---

## EU AI Act Overview

**Official title:** Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence

**Key dates:**
- Adopted by European Parliament: 13 March 2024
- Adopted by Council: 21 May 2024
- Published in Official Journal: 12 July 2024
- Entry into force: 1 August 2024 (20 days after OJ publication)

**Application timeline (phased):**
| Phase | Date | What Applies |
|-------|------|-------------|
| Phase 1 | 2 February 2025 | Prohibited AI practices (Chapter II, Article 5) |
| Phase 2 | 2 August 2025 | General Purpose AI (GPAI) model obligations (Chapter V, Articles 51–56); governance provisions |
| Phase 3 | 2 August 2026 | High-risk AI system obligations for most systems (Chapters III–IV, VII–XII) |
| Phase 4 | 2 August 2027 | High-risk AI systems under product safety legislation (Annex I) — specific sector timeline |

**Territorial scope:** Applies when:
- The AI system is placed on the EU market or put into service in the EU
- The output of the AI system is used in the EU — regardless of where the provider or deployer is established

---

## EU AI Act Risk Classification

### Prohibited AI Practices (Article 5 — Applies from 2 February 2025)

The following AI uses are outright prohibited:

| Prohibited Use | Description |
|---------------|-------------|
| Subliminal manipulation | AI that uses subliminal techniques (beyond conscious awareness) to distort behaviour in ways causing harm |
| Exploitation of vulnerabilities | AI exploiting vulnerabilities of specific groups (age, disability, socioeconomic status) to distort behaviour causing harm |
| Social scoring by public authorities | AI systems that evaluate or classify individuals based on social behaviour or personal characteristics leading to detrimental treatment |
| Real-time remote biometric identification in public spaces (law enforcement) | Exceptions exist for: searching for missing persons, preventing imminent terrorist threat, identifying perpetrators of serious crimes |
| Retrospective remote biometric identification in public spaces (law enforcement) | Without prior authorisation except for prosecution of serious crimes |
| Biometric categorisation by sensitive characteristics | Inferring race, political opinion, religion, philosophical belief, sexual orientation, trade union membership from biometric data — for law enforcement (limited exceptions) |
| Emotion recognition in workplace and education | Except for medical or safety reasons |
| Untargeted facial recognition scraping | Compiling facial recognition databases by scraping internet or CCTV images |

**ISO 42001 relevance:** The AISIA (Clause 6.1.2, A.6.1–A.6.3) and AI system register (Clause 4) must identify any AI systems that could fall into prohibited categories. Risk treatment option: Avoid (Clause 6.1.3) — do not deploy prohibited AI practices.

---

### High-Risk AI Systems (Annex III — Full obligations from 2 August 2026)

High-risk AI systems are those listed in **Annex III** of the EU AI Act:

| Category | Examples |
|----------|----------|
| 1. Biometric identification and categorisation | Remote biometric identification systems; emotion recognition in non-prohibited contexts |
| 2. Critical infrastructure management | AI systems in digital infrastructure, road traffic, water supply, gas, heating, electricity |
| 3. Education and vocational training | AI that determines access, admission, evaluation, or monitoring of students/trainees |
| 4. Employment, workers management, self-employment | AI for recruitment, CV screening, interview monitoring, task allocation, performance monitoring, promotion/dismissal |
| 5. Access to essential private and public services | Credit scoring, insurance risk assessment, emergency services dispatch, benefits eligibility |
| 6. Law enforcement | AI for criminal risk scoring, polygraph-style systems, evidence reliability assessment, deepfake detection, crime analytics |
| 7. Migration, asylum, border management | Risk scoring of persons, document authenticity, asylum processing |
| 8. Administration of justice and democratic processes | AI assisting courts; AI for electoral campaigns targeting |

Note: Systems listed in **Annex II** (products covered by EU product safety legislation — medical devices, machinery, aviation, etc.) that incorporate AI and present safety risks are also high-risk.

---

### Limited Risk AI (Transparency obligations)

AI systems that interact directly with people must inform users they are interacting with AI:
- Chatbots and conversational AI (Article 50) — must disclose AI nature
- Deepfakes (AI-generated images, audio, video) — must be labelled
- AI-generated text for public interest (election, climate, health) — must be labelled

### Minimal Risk AI
All other AI systems — no specific EU AI Act obligations beyond general product law. Majority of AI applications fall here.

---

## ISO 42001 to EU AI Act: Provider Obligations Mapping

For high-risk AI systems, providers (organisations that develop or place AI systems on the market) must comply with Articles 8–15. The following maps each article to ISO 42001.

### Article 8 — Compliance with Requirements
**EU AI Act:** Providers must ensure high-risk AI systems comply with Articles 9–15 before placing on the market or putting into service.

| ISO 42001 Mapping | Relevance |
|------------------|-----------|
| Clause 8.1 — Operational planning and control | Deployment authorisation and go/no-go criteria before AI system goes live |
| A.5.7 — AI system deployment | Controlled deployment process; staged rollout; deployment authorisation |
| Clause 9.1 — Performance evaluation | Monitoring that confirms continued compliance post-deployment |

---

### Article 9 — Risk Management System
**EU AI Act:** Providers must establish a documented, continuous risk management process for high-risk AI systems covering: identification and analysis of known risks, evaluation of risks that may emerge when used as intended or misused, adoption of risk management measures.

| ISO 42001 Mapping | Relevance | Coverage |
|------------------|-----------|----------|
| Clause 6.1.2 — AI Risk Assessment | Core risk identification, analysis, and evaluation | Direct |
| A.5.5 — Verification and validation | Testing to identify risks before deployment | Direct |
| A.5.8 — Operation and monitoring | Continuous risk identification in production | Direct |
| Clause 10.2 — Nonconformity and corrective action | Risk materialisation response | Supporting |
| A.5.3 — Data management | Training data risks (poisoning, quality) | Supporting |

**Gap note:** EU AI Act Article 9 requires risk management to cover risks from **reasonably foreseeable misuse** — this must be explicitly covered in the ISO 42001 AI risk assessment (Clause 6.1.2), not only intended use risks.

---

### Article 10 — Data and Data Governance
**EU AI Act:** Training, validation, and test data must meet quality criteria: relevant, representative, free of errors, complete as needed. Data governance practices must address biases, identify relevant gaps, and be documented.

| ISO 42001 Mapping | Relevance | Coverage |
|------------------|-----------|----------|
| A.7.1 — Data management for AI | Governance framework for AI data | Direct |
| A.7.2 — Data acquisition for AI | Controls on data sourcing; legal basis; provenance | Direct |
| A.7.3 — Data quality for AI | Quality criteria for training/validation/test data | Direct |
| A.7.4 — Data preparation for AI | Labelling, annotation, bias identification | Direct |
| A.5.3 — Data management for AI systems | Data lifecycle alongside model lifecycle | Supporting |

**Gap note:** EU AI Act Article 10(5) specifically addresses personal data used for bias monitoring and correction — this requires linkage with data protection obligations (GDPR / UK GDPR) and may require additional controls beyond ISO 42001 A.7.

---

### Article 11 — Technical Documentation
**EU AI Act:** Providers must prepare technical documentation before placing a high-risk AI system on the market, demonstrating compliance with requirements. Documentation must be maintained throughout system lifetime. Annex IV specifies minimum content.

| ISO 42001 Mapping | Relevance | Coverage |
|------------------|-----------|----------|
| A.5.1 — AI system specifications | Intended purpose, inputs/outputs, performance criteria | Direct |
| A.5.6 — AI system documentation | Comprehensive technical documentation per AI system | Direct |
| A.5.2 — AI system design | Design decisions, architectures | Supporting |
| A.5.5 — Verification and validation | Testing records, performance benchmarks | Supporting |

**EU AI Act Annex IV minimum documentation** — cross-reference to ISO 42001:

| Annex IV Requirement | ISO 42001 Control |
|---------------------|------------------|
| General description of the AI system and its intended purpose | A.5.1 |
| Description of the elements and development process | A.5.2, A.5.4 |
| Information about training and testing data methodology | A.7.1–A.7.4 |
| Description of monitoring, functioning and control of the system | A.5.8 |
| Description of the risk management system | Clause 6.1.2 |
| Changes to the system over its lifecycle | A.5.7 (change management), A.5.8 |
| Achieved performance indicators (accuracy, robustness, cybersecurity) | A.5.5 |
| Declaration of conformity | SoA (Clause 6.1.3) — supporting evidence |

---

### Article 12 — Record-Keeping (Logging)
**EU AI Act:** High-risk AI systems must have automatic recording of events (logs) during operation. Logs must include: system identification, database consultation dates/times, input data reference IDs, persons involved in verification, and the output.

| ISO 42001 Mapping | Relevance | Coverage |
|------------------|-----------|----------|
| A.5.8 — AI system operation and monitoring | Production monitoring, logging of system behaviour | Supporting |
| A.5.7 — AI system deployment | Deployment records | Supporting |
| Clause 7.5 — Documented information | Retention of operational records | Supporting |

**Gap note:** ISO 42001 does not prescribe specific logging requirements with the granularity required by Article 12. Organisations will need to implement AI-specific logging controls beyond what ISO 42001 mandates, particularly for automated decision AI systems.

---

### Article 13 — Transparency and Provision of Information to Deployers
**EU AI Act:** Providers must design high-risk AI systems to be sufficiently transparent to enable deployers to interpret outputs and use them appropriately. Written instructions for use must accompany the system.

| ISO 42001 Mapping | Relevance | Coverage |
|------------------|-----------|----------|
| A.8.1 — Transparency of AI systems | Disclosure obligations; proportion to impact level | Direct |
| A.5.6 — AI system documentation | Technical documentation including limitations and failure modes | Direct |
| A.8.2 — Communication of responsibilities | Instructions to stakeholders on AI system use | Supporting |

---

### Article 14 — Human Oversight
**EU AI Act:** High-risk AI systems must enable effective human oversight. Providers must design systems so that deployers can: understand capabilities and limitations, detect anomalies, interpret outputs, decide not to use or override the system, and intervene or halt it.

| ISO 42001 Mapping | Relevance | Coverage |
|------------------|-----------|----------|
| Clause 6.1.2 — AISIA | Impact assessment drives human oversight requirements | Direct |
| A.6.1 — Processes for assessing impact | Formal assessment of when human oversight is sufficient | Direct |
| A.6.2 — Assessing impacts on individuals | Individual-level human oversight requirements | Direct |
| A.5.1 — AI system specifications | Document operating conditions including oversight requirements | Supporting |
| A.5.8 — AI system operation and monitoring | Human intervention triggers in production monitoring | Supporting |
| Annex C attribute: Human agency and oversight | Organisational objective to ensure human control | Supporting |

---

### Article 15 — Accuracy, Robustness, and Cybersecurity
**EU AI Act:** High-risk AI systems must achieve appropriate levels of accuracy, robustness (including adversarial inputs), and cybersecurity throughout their lifecycle. Performance metrics must be declared.

| ISO 42001 Mapping | Relevance | Coverage |
|------------------|-----------|----------|
| A.5.5 — Verification and validation | Performance benchmarking; adversarial testing | Direct |
| A.5.8 — AI system operation and monitoring | Performance drift monitoring; accuracy degradation detection | Direct |
| Clause 6.1.2 — AI Risk Assessment | Model risks: adversarial attacks, overfitting | Supporting |
| A.5.2 — AI system design | Robustness built into design | Supporting |

**Gap note:** Cybersecurity of AI systems is addressed in ISO 42001 only at a high level. For high-risk AI systems, cybersecurity controls from ISO 27001 (Annex A) should be explicitly applied to the AI system's infrastructure, model artefacts, and APIs.

---

## ISO 42001 to EU AI Act: Deployer Obligations Mapping

Deployers (organisations that use high-risk AI systems in a professional context) have obligations under Article 26 and Article 27.

### Article 26 — Obligations of Deployers of High-Risk AI

| Article 26 Obligation | ISO 42001 Mapping |
|----------------------|------------------|
| 26(1): Use AI system according to instructions for use | A.4.4 — Third-party AI capabilities; A.9.7 — Public AI systems (acceptable use policy) |
| 26(2): Assign human oversight to natural persons with competence | Clause 7.2 — Competence; A.4.2 — Human resource policies |
| 26(3): Monitor AI system operation and report to provider | A.5.8 — Operation and monitoring; A.8.3 — Incident reporting |
| 26(5): Input data relevant to the AI system's intended purpose | A.7.1–A.7.3 — Data governance for AI |
| 26(6): Inform worker representatives where AI system affects workers | A.8.2 — Communication of responsibilities |
| 26(7): Conduct FRIA if required (Article 27) | AISIA — Clause 6.1.2 + A.6.1–A.6.3 |

### Article 27 — Fundamental Rights Impact Assessment (FRIA)

Deployers that are public bodies or private entities providing public services (broad definition) must conduct a FRIA before deploying high-risk AI systems.

**FRIA requirement:** Document in advance: rights affected, categories of affected persons, foreseen consequences, measures to address adverse impacts, how the AI system fits into the overall purpose.

**FRIA to AISIA Crosswalk:**

| FRIA Requirement (Article 27) | ISO 42001 AISIA Equivalent | ISO 42001 Reference |
|-------------------------------|---------------------------|---------------------|
| Description of the AI system and its intended purpose | Section 1: AI System Description | A.5.1 |
| Categories of natural persons affected | Section 2: Affected Populations | A.6.1, A.6.2 |
| Specific risk to fundamental rights (equality, privacy, dignity, expression, assembly) | Section 3: Impact Dimensions | A.6.2 |
| Societal risks (environmental, democratic, economic) | Section 4: Societal Concerns | A.6.3 |
| Measures to address adverse impacts | Section 6: Controls Selected | Annex A controls |
| Residual risk assessment | Section 7: Residual Impact Assessment | Clause 6.1.3 |
| Consultation with affected parties (where applicable) | Not specified in AISIA template — additional step required | A.8.2 |

**Practical note:** An ISO 42001 AISIA substantially covers the FRIA requirements. Organisations should:
1. Conduct the AISIA using the ISO 42001 templates
2. Before deployment, confirm the AISIA documentation satisfies Article 27 FRIA requirements
3. Add the Article 27-specific consultation requirement if deploying in a context requiring it
4. Retain the AISIA as the primary FRIA record (referencing Article 27 in the document header)

---

## General Purpose AI (GPAI) Model Obligations

GPAI models (large-scale AI models including large language models — examples: GPT-4, Claude, Llama, Gemini) have specific obligations under Chapter V (Articles 51–56), applying from 2 August 2025.

**GPAI providers must:**
- Prepare technical documentation (analogous to Annex IV for GPAI — see Article 53)
- Comply with copyright law; make public a summary of training data used
- Publish information enabling downstream providers to meet their obligations
- Cooperate with national authorities on request

**Systemic risk GPAI (models trained with >10^25 floating-point operations):**
- Conduct adversarial testing (red-teaming) before deployment
- Report serious incidents to the European AI Office
- Implement cybersecurity protections
- Report energy consumption

| ISO 42001 Mapping for GPAI providers | Relevance |
|-------------------------------------|-----------|
| A.5.6 — AI system documentation | Technical documentation for GPAI models |
| A.5.5 — Verification and validation (including adversarial testing) | Red-teaming / adversarial testing |
| A.7.2 — Data acquisition | Training data provenance and copyright compliance |
| A.8.1 — Transparency | Public disclosure of AI capabilities and limitations |
| A.8.3 — AI incident reporting | Serious incident reporting to competent authority |
| Clause 6.1.2 — AI Risk Assessment | Systemic risk assessment for large-scale models |

---

## ISO 42001 Certification and EU AI Act Conformity

### Position as of December 2023 (ISO 42001 Publication Date)
ISO/IEC 42001:2023 was **not listed as a harmonised standard** under the EU AI Act at the time of its publication. The EU AI Act's harmonised standards programme was ongoing at publication.

### Relationship and Practical Value
Even without formal harmonised standard designation, ISO 42001 provides substantial evidence of conformity with many EU AI Act requirements:

| EU AI Act Article | ISO 42001 Evidence | Level of Coverage |
|------------------|-------------------|------------------|
| Article 9 Risk management | Clause 6.1.2 AI risk assessment records | High |
| Article 10 Data governance | A.7 controls and records | High |
| Article 11 Technical documentation | A.5.1, A.5.6 documentation | High |
| Article 12 Record-keeping | A.5.8 monitoring records | Medium (gaps in logging specificity) |
| Article 13 Transparency | A.8.1 transparency controls | High |
| Article 14 Human oversight | AISIA and A.6 controls | High |
| Article 15 Accuracy and robustness | A.5.5 testing records | Medium |
| Article 26 Deployer obligations | User-role controls throughout | High |
| Article 27 FRIA | AISIA records (A.6.1–A.6.3) | High |

### Practical Approach for Organisations

1. **Implement ISO 42001 first** — establishes the governance foundation and generates the evidence base
2. **Map ISO 42001 controls to EU AI Act obligations** — use this reference file to identify gaps
3. **Fill EU AI Act-specific gaps** — particularly:
   - Granular logging (Article 12): implement AI-specific event logging beyond ISO 42001 scope
   - Reasonably foreseeable misuse in risk assessment (Article 9): explicitly document in risk records
   - GPAI model obligations (Article 51–56): additional provider controls if applicable
   - Cybersecurity of AI (Article 15): apply ISO 27001 controls to AI infrastructure
4. **Document the mapping** — maintain a live mapping document linking ISO 42001 evidence to EU AI Act articles
5. **Monitor harmonised standards developments** — if ISO 42001 achieves harmonised standard status under the EU AI Act, a presumption of conformity will apply for covered articles

---

## EU AI Act High-Risk AI Sector Guide

For each Annex III category, the following ISO 42001 controls are most critical:

| Sector | Critical ISO 42001 Controls | Additional EU AI Act Considerations |
|--------|---------------------------|-------------------------------------|
| Employment AI (CV screening, performance monitoring) | A.5.5 (bias testing) A.6.2 (individual impacts) A.8.1 (transparency to workers) | Article 26(6): notify worker representatives; FRIA required for deployers |
| Credit scoring / insurance | A.5.5 A.6.2 A.8.1 A.9.2 | Right to explanation of AI decisions under GDPR Article 22 must also be met |
| Education (admissions, assessment) | A.5.5 A.6.2 A.8.1 | FRIA likely required; high vulnerability of affected population (students) |
| Healthcare (diagnostic AI) | A.5.1 A.5.5 A.5.6 A.5.8 A.6.2 | Overlapping with Medical Device Regulation (MDR/IVDR) for in vitro diagnostics; Annex I coordination |
| Public safety / law enforcement | A.6.2 A.6.3 A.8.1 A.8.3 | Most restrictive category; FRIA mandatory; real-time biometric restrictions apply |
| Benefits / essential services | A.5.5 A.6.2 A.8.1 A.8.2 | FRIA required for deployers; high impact on vulnerable populations |

---

## EU AI Act and GDPR Interaction

The EU AI Act sits alongside GDPR (and UK GDPR); both apply simultaneously when AI processes personal data.

| Topic | GDPR Obligation | EU AI Act Obligation | ISO 42001 Link |
|-------|----------------|---------------------|---------------|
| Automated decisions | Article 22: Right not to be subject to solely automated decisions with legal/significant effects | Article 14: Human oversight for high-risk AI | AISIA human oversight classification; A.8.1 |
| Data minimisation | Article 5(1)(c): Collect only data necessary for purpose | Article 10: Training data proportionate to purpose | A.7.2 data acquisition controls |
| Right to explanation | Recital 71: Meaningful information about automated decision logic | Article 13: Transparency and information to deployers | A.8.1 transparency controls |
| Impact assessments | Article 35: DPIA required for high-risk personal data processing | Article 27: FRIA for deployers | AISIA (ISO 42001 Clause 6.1.2) — conduct AISIA alongside DPIA |
| Data protection by design | Article 25: Data protection by design and default | Article 10: Data governance and bias mitigation | A.7 data controls |

**Practical note:** For AI systems processing personal data, organisations should conduct the ISO 42001 AISIA and the GDPR DPIA in parallel, using a unified assessment framework where possible.

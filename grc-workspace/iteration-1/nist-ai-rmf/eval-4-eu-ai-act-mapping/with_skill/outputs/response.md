# NIST AI RMF ↔ EU AI Act: Framework Mapping and Gap Analysis

## Executive Summary

The NIST AI RMF (AI 100-1, January 2023) and the EU AI Act (Regulation (EU) 2024/1689) are complementary but distinct instruments. The AI RMF is a **voluntary, risk-based framework** providing methodology for managing AI risks throughout the lifecycle. The EU AI Act is **mandatory EU law** imposing specific legal obligations on providers and deployers of in-scope AI systems, with particular requirements for "high-risk" AI systems.

The good news: implementing NIST AI RMF at sufficient maturity provides a strong foundation for EU AI Act compliance — particularly for the Article 9 risk management system requirement. However, the EU AI Act contains mandatory, prescriptive obligations that go beyond what AI RMF covers. Organizations subject to both must treat AI RMF as necessary but not sufficient for EU AI Act compliance.

---

## Part 1: Framework Comparison Overview

| Dimension | NIST AI RMF | EU AI Act |
|-----------|-------------|-----------|
| **Legal nature** | Voluntary guidance | Mandatory regulation (EU law) |
| **Geographic scope** | Global applicability | EU market — applies to providers/deployers placing AI in EU market or affecting EU persons |
| **Approach** | Outcome-based, flexible | Prescriptive, obligation-based |
| **Structure** | Four functions: GOVERN, MAP, MEASURE, MANAGE | Risk classification tiers: Prohibited / High-Risk / Limited-Risk / Minimal-Risk |
| **Primary audience** | Any organization designing, developing, or deploying AI | Providers (developers), deployers (operators), importers, distributors |
| **Enforcement** | No enforcement mechanism | Market surveillance authorities; fines up to €35M or 7% of global turnover |
| **Documentation** | Guidance on what to document; no mandated format | Annex IX mandates specific technical documentation for high-risk AI |
| **Timeline** | Implemented at organizational pace | Phased enforcement from August 2024; high-risk AI provisions apply from August 2026 |

---

## Part 2: Detailed Function-Level Mapping

### GOVERN Function ↔ EU AI Act Obligations

| AI RMF Category | EU AI Act Requirement | Alignment Notes |
|----------------|----------------------|-----------------|
| **GV-1** — AI risk management policies and processes | **Art. 9** — High-risk AI providers must establish, implement, document, and maintain a risk management system | Strong alignment: GV-1's requirement for formalized AI risk management policies directly supports Art. 9 compliance. However, Art. 9 is mandatory and requires documented evidence; GV-1 is aspirational. |
| **GV-1.6** — Policies for complying with applicable laws | **Art. 9, Art. 16, Art. 26** — Legal compliance obligations for providers and deployers | Direct alignment: GV-1.6 requires tracking regulatory requirements; EU AI Act should appear in the regulatory register. |
| **GV-2** — Accountability structures | **Art. 16** — Provider obligations; **Art. 26** — Deployer obligations; **Art. 25** — Distributor/importer responsibilities | Good alignment in principle. AI RMF does not mandate a specific accountability structure; EU AI Act assigns distinct legal obligations by actor type (provider vs. deployer). |
| **GV-3** — Roles and responsibilities | **Art. 16(k)** — Providers must designate an EU-based authorized representative; **Art. 26** — Deployers must assign responsibilities | Partial: GV-3 is broader on roles; EU AI Act adds the legally specific requirement for an EU authorized representative for non-EU providers. |
| **GV-4** — Cross-functional teams | No direct EU AI Act equivalent | Gap: EU AI Act does not mandate cross-functional teams; this is an AI RMF organizational best practice that supports compliance but is not a legal requirement. |
| **GV-5** — Risk tolerance | **Art. 9(2)(a)** — Risk management must be iterative throughout lifecycle | Partial alignment: GV-5 addresses organizational risk tolerance; Art. 9 requires continuous iterative risk management but does not address tolerance thresholds explicitly. |
| **GV-6** — Alignment with laws and principles | **Art. 9, Recital 58, Annex IX** — Technical documentation must demonstrate legal compliance | Strong alignment: GV-6 provides the governance mechanism; EU AI Act mandates the output (demonstrable compliance). |

---

### MAP Function ↔ EU AI Act Obligations

| AI RMF Category | EU AI Act Requirement | Alignment Notes |
|----------------|----------------------|-----------------|
| **MP-1** — Context of intended use established | **Art. 9(2)** — Risk management must cover "intended purpose and reasonably foreseeable misuse"; **Art. 13** — Transparency and provision of information to deployers | Strong alignment: MP-1.2 (intended uses documented and bounded) and MP-1.5 (misuse scoped) map directly to Art. 9(2). EU AI Act additionally requires this information to be provided in Instructions for Use (Annex IX). |
| **MP-1.4** — Affected populations identified | **Art. 9(2)(b)** — Identification and analysis of known and foreseeable risks to health, safety, and fundamental rights | Direct alignment. EU AI Act adds specificity: fundamental rights impact is a distinct category requiring assessment. |
| **MP-2** — Scientific understanding of AI limitations | **Art. 10** — Data governance and management practices; **Art. 15** — Accuracy, robustness, and cybersecurity requirements | Partial: MP-2 addresses documenting limitations; EU AI Act elevates this to a mandatory technical standard that must be demonstrated and tested. |
| **MP-3** — Risks and benefits mapped to stakeholders | **Art. 9(2)(b)** — Risk identification for affected persons; **Art. 27** — Fundamental rights impact assessment for deployers in public-sector contexts | Alignment with gap: MP-3 addresses stakeholder mapping broadly. EU AI Act Art. 27 mandates a formal Fundamental Rights Impact Assessment (FRIA) for certain deployers — a specific artifact not addressed in AI RMF. |
| **MP-4 / MP-5** — Risk prioritization and likelihood/impact characterization | **Art. 9(2)(c)** — Risk estimation and evaluation; **Art. 9(4)** — Residual risks to be evaluated against risk management measures | Strong methodological alignment: AI RMF MAP methodology directly supports Art. 9's risk estimation requirement. |

---

### MEASURE Function ↔ EU AI Act Obligations

| AI RMF Category | EU AI Act Requirement | Alignment Notes |
|----------------|----------------------|-----------------|
| **MS-1** — Measurement approaches identified | **Art. 15** — Accuracy, robustness, and cybersecurity must be addressed with appropriate metrics; **Art. 10(2)** — Data quality criteria | Good alignment: MS-1 supports Art. 15 by establishing a measurement methodology. EU AI Act requires specific performance levels for accuracy and robustness without prescribing exact metrics. |
| **MS-2** — System evaluation for trustworthiness | **Art. 9(6)** — Testing must be performed before market placement; **Art. 10** — Data governance including bias examination; **Art. 15** — Accuracy, robustness, and cybersecurity | Strong alignment: MS-2 subcategories (bias testing, explainability, security assessment, human oversight validation) map closely to Art. 9 and Art. 15. EU AI Act adds that testing must occur "at appropriate times" before market placement — making it a legal prerequisite, not a best practice. |
| **MS-2.3** — Explainability tested | **Art. 13** — Transparency; high-risk AI systems must be designed to allow deployers to interpret outputs | Alignment with gap: MS-2.3 addresses explainability from a measurement perspective. Art. 13 mandates that Instructions for Use include information enabling deployers to interpret outputs — this is a product documentation obligation beyond testing. |
| **MS-2.5** — Human oversight mechanisms tested | **Art. 14** — Human oversight — high-risk AI must enable effective human oversight; specific operator capabilities must be designed in | Strong alignment: MS-2.5 validates human oversight mechanisms. Art. 14 is more prescriptive: it mandates specific technical characteristics (ability to pause, override, disregard, or discontinue use) that must be designed in and documented. |
| **MS-3** — Ongoing monitoring | **Art. 72** — Post-market monitoring obligation for providers; deployers must report to providers; **Art. 26(5)** — Deployer monitoring obligations | Strong alignment: MS-3 covers ongoing monitoring and drift detection. Art. 72 makes post-market monitoring a legal obligation with a required Post-Market Monitoring Plan (a specific documented artifact). |
| **MS-4** — Feedback informs MANAGE | **Art. 72** — Monitoring data must feed into risk management system | Alignment: MS-4 establishes the feedback loop; Art. 72 makes this mandatory with specific reporting obligations to market surveillance authorities. |

---

### MANAGE Function ↔ EU AI Act Obligations

| AI RMF Category | EU AI Act Requirement | Alignment Notes |
|----------------|----------------------|-----------------|
| **MG-1** — Risks prioritized and documented | **Art. 9(2)(d)** — Adoption of risk management measures; residual risks evaluated | Good alignment: MG-1 provides the process; EU AI Act requires this to be demonstrated through technical documentation (Annex IX). |
| **MG-2** — Risk treatment strategies | **Art. 9(2)(d)** — Risk management measures for each identified risk; measures to address residual risks | Alignment with gap: MG-2's treatment options (mitigate, transfer, avoid, accept) align with Art. 9. EU AI Act adds a hierarchy of obligations — certain risks cannot simply be "accepted" if they exceed thresholds; the system may not be permitted. |
| **MG-2.3** — Emergency interventions | **Art. 14(4)(d)** — Human oversight must include ability to interrupt or stop the AI system | Direct alignment: MG-2.3 and Art. 14(4)(d) both require defined shutdown/override procedures. |
| **MG-3** — Incident response | **Art. 73** — Providers must report serious incidents to national market surveillance authorities; deployers must notify providers | Alignment with important gap: MG-3 covers internal incident response. Art. 73 mandates external regulatory reporting of serious incidents (death, serious injury, breach of fundamental rights obligations, serious damage to property or environment) within prescribed timeframes. |
| **MG-4** — Review and improvement | **Art. 9(1)** — Risk management system is a "continuous iterative process" throughout the lifecycle | Strong alignment: MG-4's continuous improvement loop maps directly to Art. 9's iterative process requirement. |

---

## Part 3: Gap Analysis — What AI RMF Does NOT Cover

The following EU AI Act requirements have no direct NIST AI RMF equivalent and represent compliance gaps that organizations must fill with additional controls, processes, and documentation.

### Gap 1: Prohibited AI Practices (Article 5)
**EU AI Act requirement:** Certain AI practices are absolutely prohibited, regardless of safeguards. These include:
- Real-time remote biometric identification in public spaces by law enforcement (with limited exceptions)
- AI systems that exploit vulnerabilities of persons (age, disability, social/economic situation)
- Social scoring by public authorities
- Untargeted scraping of facial images from the internet or CCTV
- AI systems to infer emotions in workplace or educational settings
- Biometric categorization to infer protected characteristics

**AI RMF gap:** The AI RMF is a risk management framework — it does not prohibit any AI practice outright. Organizations subject to the EU AI Act must establish a pre-deployment screening process to identify and prohibit any AI system that falls into Article 5 categories before AI RMF risk management processes are even initiated.

**Action required:** Create an AI Use Case Screening Policy that maps proposed AI systems against Art. 5 prohibited practices and treats any match as a go/no-go disqualifier.

---

### Gap 2: Risk Classification and Tiering (Articles 6–7 and Annexes II–III)
**EU AI Act requirement:** Providers must classify their AI systems into the correct risk tier (prohibited, high-risk, limited-risk, minimal-risk). High-risk classification is determined by reference to Annex II (product safety regulation sectors) and Annex III (specific use cases including biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice, and democratic processes).

**AI RMF gap:** AI RMF has no concept of mandatory risk classification by regulatory tier. MP-4 covers risk prioritization, but this is based on organizational judgment — not a legal classification determination.

**Action required:** Establish a formal EU AI Act Classification Procedure. For each AI system, determine: (1) Does it fall under Annex II product safety regulations? (2) Does it fall under Annex III high-risk use case categories? Document the classification determination with reasoning. This must be done before EU AI Act obligations are applied.

---

### Gap 3: Conformity Assessment (Articles 43–49)
**EU AI Act requirement:** High-risk AI systems must undergo a conformity assessment before being placed on the EU market. For most Annex III systems, this is a self-assessment by the provider. For certain biometric and critical infrastructure systems (Annex II), third-party conformity assessment by a notified body is required. Providers must draw up an EU Declaration of Conformity and affix the CE marking.

**AI RMF gap:** AI RMF has no conformity assessment requirement, CE marking process, or Declaration of Conformity. The framework's MEASURE function evaluates trustworthiness but does not produce the specific legal artifact required.

**Action required:** Implement a conformity assessment process for high-risk AI systems. Map AI RMF MEASURE outputs to the evidence required for conformity assessment. Engage a notified body where mandatory third-party assessment is required. Maintain the EU Declaration of Conformity.

---

### Gap 4: Technical Documentation — Annex IX
**EU AI Act requirement:** Providers of high-risk AI systems must prepare and maintain technical documentation as specified in Annex IX before market placement. This documentation is distinct and more specific than what AI RMF guidance suggests. It must include: system description, intended purpose, design specifications, training data description, testing methods and results, risk management documentation, post-market monitoring plan, instructions for use, and Declaration of Conformity.

**AI RMF gap:** AI RMF guidance suggests documenting model cards, risk registers, and assessment results, but does not specify the exact document structure required. The AI RMF does not produce Annex IX-compliant technical documentation as an output.

**Action required:** Develop an Annex IX Technical Documentation Template. Map existing AI RMF outputs (model cards from MP-2, risk register from MAP/MANAGE, evaluation results from MEASURE) to the required Annex IX sections. Identify documentation gaps and close them.

---

### Gap 5: Transparency and User Information — Article 13 and Instructions for Use
**EU AI Act requirement:** High-risk AI systems must be accompanied by Instructions for Use that enable deployers to correctly use the system and understand its capabilities and limitations. For systems interacting with natural persons, those persons must be informed they are interacting with an AI system (Art. 50). Certain systems generating synthetic content must include technical solutions for marking content as AI-generated (watermarking obligation).

**AI RMF gap:** AI RMF addresses transparency as a trustworthiness property and recommends explainability testing (MS-2.3), but does not mandate specific user-facing documentation or transparency mechanisms. The Instructions for Use obligation and the content watermarking/labelling obligation are not covered.

**Action required:** Develop standardized Instructions for Use for each high-risk AI system. Implement AI interaction disclosure mechanisms where the system interacts with natural persons. Assess applicability of content watermarking obligations for generative AI systems.

---

### Gap 6: Fundamental Rights Impact Assessment — Article 27
**EU AI Act requirement:** Deployers (not providers) of high-risk AI systems that are bodies governed by public law, or private operators providing public services, must conduct a Fundamental Rights Impact Assessment (FRIA) before deploying the system. The FRIA must assess the impact on fundamental rights, including equality, non-discrimination, privacy, and protection of personal data.

**AI RMF gap:** MP-3 (stakeholder risk/benefit mapping) and MP-5 (likelihood/impact characterization) together cover much of what a FRIA requires. However, the EU AI Act FRIA is a specific, legally required assessment with a defined scope (fundamental rights) and obligation to notify supervisory authorities in certain cases. AI RMF does not produce this artifact.

**Action required:** For in-scope deployers, develop a FRIA template aligned with EDPB and national authority guidance. Integrate FRIA outputs into the MAP 3 and MP-5 process so the work is not duplicated, but ensure the FRIA meets the legal standard as a distinct deliverable.

---

### Gap 7: Regulatory Registration — EU Database (Article 71)
**EU AI Act requirement:** Providers of standalone high-risk AI systems (Annex III, not embedded in regulated products) must register themselves and their AI systems in the EU AI public database maintained by the European AI Office before market placement.

**AI RMF gap:** No registration obligation exists in the AI RMF. This is an external administrative compliance step with no AI RMF equivalent.

**Action required:** Identify all Annex III high-risk AI systems requiring registration. Prepare registration submissions for the EU AI Act public database. Assign responsibility for maintaining registrations when systems are updated or withdrawn.

---

### Gap 8: Incident Reporting to Authorities — Article 73
**EU AI Act requirement:** Providers must report serious incidents — defined as incidents resulting in death, serious injury, breach of obligations under Union law on fundamental rights, significant property or environmental damage — to national market surveillance authorities. Reporting timelines are specified (15 days for death/serious injury risk; 10 days for serious incidents; 3 months for unexpectedly high risk). Deployers must report to providers immediately upon identifying serious incidents.

**AI RMF gap:** MG-3 (incident response) and MG-3.4 (stakeholder notification) address incident management and notification internally. The AI RMF does not address mandatory external regulatory reporting, specific reporting timelines, or reporting to market surveillance authorities.

**Action required:** Extend the AI incident response procedure (MG-3) to include a regulatory reporting track. Define internal escalation criteria and timelines that trigger regulatory notification under Art. 73. Identify the relevant national market surveillance authorities for each jurisdiction where high-risk AI systems are deployed.

---

### Gap 9: Post-Market Monitoring Plan — Article 72
**EU AI Act requirement:** Providers must establish, document, and implement a Post-Market Monitoring (PMM) system. The PMM must include a Post-Market Monitoring Plan (a required document). The PMM must actively gather and analyse data on deployed systems to identify risks and incidents throughout the system's lifecycle.

**AI RMF gap:** MS-3 (ongoing monitoring) and MG-3 (risk responses monitored) together address post-deployment monitoring in principle. However, the AI RMF does not require a formal Post-Market Monitoring Plan as a specific documented artifact, and does not specify reporting back to competent authorities.

**Action required:** Formalise existing MS-3 monitoring activities into a documented Post-Market Monitoring Plan for each high-risk AI system. The plan should specify: monitoring objectives, data sources, monitoring frequency, responsible parties, triggers for Art. 73 reporting, and process for feeding findings back into the Art. 9 risk management system.

---

### Gap 10: Obligations Specific to General-Purpose AI (GPAI) Models — Articles 51–56
**EU AI Act requirement:** Providers of General-Purpose AI (GPAI) models — including large language models and foundation models made available via API or open-source — have specific obligations: transparency to downstream providers (model cards, technical documentation), copyright policy, energy consumption reporting. GPAI models with "systemic risk" (training compute above 10^25 FLOPs, or designated by the AI Office) have additional obligations: adversarial testing, incident reporting, cybersecurity measures, and efficiency reporting.

**AI RMF gap:** AI RMF does not distinguish GPAI models as a specific category requiring distinct treatment. The framework applies uniformly to all AI systems. The GPAI obligations, including the systemic risk designation and associated enhanced requirements, are entirely outside AI RMF scope.

**Action required:** If your organization develops or deploys GPAI models, conduct a separate GPAI obligation assessment. Determine whether any models meet the systemic risk threshold. Implement GPAI-specific transparency documentation (Art. 53) and, if applicable, systemic risk management measures (Art. 55).

---

## Part 4: Consolidated Gap Summary Table

| Gap Area | EU AI Act Articles | AI RMF Gap | Priority | Action |
|----------|-------------------|------------|----------|--------|
| Prohibited AI screening | Art. 5 | No prohibition concept in AI RMF | Critical | Create AI Use Case Screening Policy against Art. 5 |
| Risk tier classification | Art. 6–7, Annex II–III | No mandatory regulatory tier classification | Critical | Establish EU AI Act Classification Procedure for all AI systems |
| Conformity assessment and CE marking | Art. 43–49 | No conformity assessment process | High | Implement conformity assessment; engage notified body where required |
| Annex IX technical documentation | Annex IX | AI RMF outputs do not match Annex IX structure | High | Develop Annex IX templates mapping from AI RMF artifacts |
| Instructions for Use and transparency | Art. 13, Art. 50 | AI RMF does not mandate user-facing documentation | High | Develop Instructions for Use; implement AI interaction disclosures |
| Fundamental Rights Impact Assessment | Art. 27 | MP-3/MP-5 cover substance but not the legal artifact | High | Develop FRIA template for in-scope deployers |
| EU AI Act public database registration | Art. 71 | No registration obligation in AI RMF | Medium | Register high-risk Annex III systems in EU AI database |
| Regulatory incident reporting | Art. 73 | MG-3 covers internal response only | High | Extend incident procedure with regulatory reporting track and timelines |
| Post-Market Monitoring Plan | Art. 72 | MS-3 covers monitoring activity but not the formal plan artifact | Medium | Formalise MS-3 outputs into a documented PMM Plan per system |
| GPAI model obligations | Art. 51–56 | GPAI models not distinguished in AI RMF | Varies | GPAI obligation assessment if applicable |

---

## Part 5: Implementation Recommendations

### For Organizations Subject to Both Frameworks

**Step 1 — Classify before you manage.**
Before applying AI RMF processes, determine the EU AI Act risk classification of each AI system. Prohibited systems must be stopped. High-risk systems require the full EU AI Act compliance programme. Limited-risk and minimal-risk systems can be managed primarily through AI RMF.

**Step 2 — Use AI RMF as the methodology for Art. 9 compliance.**
Article 9's risk management system requirement is the most substantive EU AI Act obligation. Implementing GOVERN, MAP, MEASURE, and MANAGE at AI RMF Tier 3 (Repeatable) maturity provides the strongest available methodology for satisfying Art. 9. Document this explicitly — regulators and notified bodies understand AI RMF.

**Step 3 — Build EU-specific artifacts on top of AI RMF outputs.**
The AI RMF produces many of the inputs needed for EU AI Act documentation (risk assessments, evaluation results, monitoring records). The gaps are largely about converting those outputs into the specific legally required artifacts: Annex IX technical documentation, Declarations of Conformity, Post-Market Monitoring Plans, FRIAs. Build templates that systematically map AI RMF outputs to EU AI Act document requirements.

**Step 4 — Add EU-specific processes for the structural gaps.**
Five areas require wholly new processes not analogous to anything in AI RMF: (1) Art. 5 prohibited use screening, (2) risk tier classification under Annex II/III, (3) conformity assessment and CE marking, (4) EU database registration, and (5) Art. 73 regulatory incident reporting. These should be added as formal procedures layered on top of the AI RMF programme.

**Step 5 — Assign the EU AI Act as a regulatory register entry under GV-6.**
GV-1.6 and GV-6 require maintaining a regulatory register. The EU AI Act — with its specific applicability dates, obligations per actor type (provider vs. deployer), and enforcement milestones — should be a fully documented entry in this register with assigned compliance owners.

---

## Summary

Implementing NIST AI RMF provides approximately 60–70% of the substantive risk management capability needed for EU AI Act compliance, particularly for Article 9's risk management system requirement. The remaining gaps are not minor — they include mandatory legal classification, conformity assessment, prescribed documentation formats, prohibited use screening, and regulatory reporting obligations that are simply outside the AI RMF's voluntary, methodology-focused scope.

The two frameworks are designed to complement each other: use AI RMF as the risk management methodology and operating framework, and layer EU AI Act-specific legal compliance obligations on top. Organizations that implement AI RMF at Tier 3 maturity and then close the ten identified gaps will be well-positioned for EU AI Act compliance for high-risk AI systems.

# EU AI Act - Risk Classification Reference

## Art. 3 - Key Definitions

| Term | Definition |
|------|-----------|
| **AI System** (Art. 3(1)) | A machine-based system designed to operate with varying levels of autonomy that, for a given set of objectives, infers from inputs how to generate outputs such as predictions, recommendations, decisions, or content affecting real or virtual environments |
| **GPAI Model** (Art. 3(63)) | An AI model trained with large amounts of data using self-supervision at scale that displays significant generality and competently performs a wide range of distinct tasks, regardless of placement method - excludes pre-release R&D models |
| **GPAI System** (Art. 3(64)) | An AI system based on a GPAI model capable of serving multiple purposes, directly or when integrated into other AI systems |
| **Provider** (Art. 3(3)) | Natural or legal person that develops an AI system or GPAI model and places it on the market or puts it into service under own name/trademark |
| **Deployer** (Art. 3(4)) | Natural or legal person using an AI system under own authority, except for personal non-professional activity |
| **Operator** (Art. 3(8)) | Encompasses provider, product manufacturer, deployer, authorised representative, importer, or distributor |
| **Authorised Representative** (Art. 3(5)) | Person established in EU with written mandate from non-EU provider to act on their behalf |
| **Importer** (Art. 3(6)) | EU-established person placing on market an AI system bearing third-country person's name/trademark |
| **Distributor** (Art. 3(7)) | Supply chain person (other than provider/importer) making AI system available on EU market |
| **Profiling** (Art. 3(52)) | Automated processing of personal data to evaluate natural persons - work performance, economic situation, health, preferences, reliability, behaviour, location |

---

## Risk Tier Overview

> ⚠️ **AI Omnibus (May 2026):** Extended Annex III deadline to **2 Dec 2027** and Annex I deadline to **2 Aug 2028**. The original 2 Aug 2026 and 2027 dates in the regulation text are superseded.

| Tier | Regulation Path | Key Obligation | Applies From |
|------|----------------|----------------|--------------|
| **Prohibited** | Art. 5 | Complete ban - 8 categories from 2 Feb 2025; 9th (nudification/CSAM) from 2 Dec 2026 | 2 Feb 2025 / 2 Dec 2026 |
| **High Risk - Annex III** | Art. 6(2) + Annex III | Full conformity regime | **2 Dec 2027** (AI Omnibus) |
| **High Risk - Annex I** | Art. 6(1) + Annex I | Full conformity regime | **2 Aug 2028** (AI Omnibus) |
| **Limited Risk** | Art. 50 | Transparency disclosure only | 2 Aug 2026 (new systems); 2 Dec 2026 grace period for pre-existing |
| **Minimal / No Risk** | - | Voluntary codes of conduct | - |

---

## Art. 5 - Prohibited AI Practices (applies from 2 February 2025 for original 8; 2 Dec 2026 for 9th)

**Commission guidance:** The AI Office published guidelines on all prohibited AI practices on **4 February 2025**, with practical examples for each category. Commission also published three studies on Art. 5 in **May 2026**. Always consult these alongside the article text.

### 5(1)(a) - Subliminal / Manipulative Techniques
AI systems using subliminal techniques beyond a person's consciousness, or purposefully manipulative/deceptive techniques, that materially distort behavior and impair informed decision-making, causing or likely to cause significant harm to those persons or third parties.

### 5(1)(b) - Exploitation of Vulnerabilities
AI systems exploiting vulnerabilities of persons or groups based on age, disability, or socioeconomic circumstances, distorting behavior in a manner that causes or is likely to cause significant harm.

### 5(1)(c) - Social Scoring
AI systems that evaluate or classify natural persons or groups based on social behavior over a period of time or inferred personal characteristics, leading to:
- Detrimental or unfavorable treatment of persons or groups in unrelated social contexts; OR
- Treatment that is disproportionate or unjustified relative to the social context in which the behavior occurred

### 5(1)(d) - Predictive Criminal Risk Assessment
AI systems assessing the risk of natural persons committing criminal offenses based solely on profiling or personality/character traits assessment. **Exception:** systems supporting human assessment based on objective, verifiable facts directly linked to criminal activity.

### 5(1)(e) - Untargeted Facial Recognition Database Creation
Creating or expanding facial recognition databases through untargeted scraping of facial images from the internet or CCTV footage.

### 5(1)(f) - Emotion Inference in Workplace or Educational Institutions
AI systems that infer emotions of natural persons in the workplace or educational institutions. **Exception:** for medical or safety purposes.

### 5(1)(g) - Biometric-Based Categorization for Sensitive Attributes
AI systems categorizing natural persons individually based on biometric data to deduce or infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation. **Exception:** labeling/filtering of lawfully acquired biometric datasets in law enforcement.

### 5(1)(h) - Real-Time Remote Biometric Identification (RBI) in Public Spaces by Law Enforcement
Real-time RBI systems in publicly accessible spaces for law enforcement purposes. **Narrow exceptions:**
- (i) Targeted search for specific missing persons or trafficking victims
- (ii) Preventing specific, substantial, imminent threat to life or terrorist attack  
- (iii) Identifying suspects of serious criminal offenses carrying ≥4-year sentences listed in Annex II

**Procedural requirements for exceptions:** Prior judicial or independent administrative body authorization (post-hoc authorization within 24 hours for urgency); fundamental rights impact assessment; registration in EU AI database; report to market surveillance authority after each use. **Prohibited:** use to identify protected attributes.

### 5(1)(i) - Non-Consensual Sexually Explicit / Intimate Imagery and CSAM *(AI Omnibus, applies from 2 Dec 2026)*
AI systems capable of generating **non-consensual sexually explicit or intimate imagery** (including so-called "nudification" or "nudify" applications), or **child sexual abuse material (CSAM)**.

**Safe harbour:** A system benefits from a safe harbour if it has **effective technical safeguards** that reliably prevent the prohibited outputs from being generated, even when the user attempts to do so. The safe harbour is lost if the safeguards are bypassed or deactivated.

**Scope note:** This prohibition targets the capability of the AI system itself, not only its use in a specific deployment. A model or application whose principal or evident purpose is to produce such imagery is prohibited regardless of intent.

---

## Art. 6 - High-Risk Classification Rules

### Path A - Art. 6(1): Safety Component of Sectoral Product
System is high-risk when BOTH conditions are met:
1. It is a **safety component of a product** covered by Annex I harmonisation legislation (or is itself such a product); **AND**
2. That product **requires third-party conformity assessment** under the relevant Annex I legislation

### Path B - Art. 6(2): Annex III Listed Use Case
System is high-risk when **listed in Annex III**, unless the following non-high-risk exceptions all apply:
- Performs a narrow procedural task
- Improves result of a previously completed human activity
- Detects decision-making patterns/deviations without replacing/influencing human assessment
- Performs preparatory tasks for assessment relevant to Annex III use cases

**Critical override (Art. 6(3)):** Any Annex III system that **profiles natural persons** is ALWAYS high-risk regardless of the above exceptions.

**Documentation obligation (Art. 6(4)):** Providers claiming non-high-risk status must document their assessment before market placement and make it available to national authorities on request.

---

## Annex I - Sectoral Harmonisation Laws (Safety Component Path)

### Section A - New Legislative Framework Products
1. Machinery - Directive 2006/42/EC
2. Toys - Directive 2009/48/EC
3. Recreational watercraft - Directive 2013/53/EU
4. Lifts - Directive 2014/33/EU
5. ATEX equipment - Directive 2014/34/EU
6. Radio equipment - Directive 2014/53/EU
7. Pressure equipment - Directive 2014/68/EU
8. Cableway installations - Regulation 2016/424
9. Personal protective equipment - Regulation 2016/425
10. Gaseous fuel appliances - Regulation 2016/426
11. Medical devices - Regulation 2017/745
12. In vitro diagnostic medical devices - Regulation 2017/746

### Section B - Other Harmonisation Legislation
13. Civil aviation security - Regulation 300/2008
14. Two/three-wheel vehicles - Regulation 168/2013
15. Agricultural/forestry vehicles - Regulation 167/2013
16. Marine equipment - Directive 2014/90/EU
17. Rail interoperability - Directive 2016/797
18. Motor vehicles and trailers - Regulation 2018/858
19. Motor vehicle safety standards - Regulation 2019/2144
20. Civil aviation and drones - Regulation 2018/1139

---

## Annex III - High-Risk AI Use Case Areas (8 Areas)

### Area 1 - Biometrics
- (a) Remote biometric identification systems (excluding personal identity verification)
- (b) Biometric categorization systems inferring sensitive/protected attributes
- (c) Emotion recognition systems

**Notes:** (b) and (c) are prohibited under Art. 5(1)(g) and 5(1)(f) respectively in many contexts. Area 1(a) biometric categorization/emotion recognition systems that fall under Art. 5 prohibitions cannot qualify as merely high-risk - the prohibition takes precedence.

### Area 2 - Critical Infrastructure
AI safety components managing or used in safety-critical management of: road traffic, water supply, gas supply, heating supply, electricity supply, and critical digital infrastructure.

### Area 3 - Education and Vocational Training
- (a) Determining access/admission to or assignment to educational institutions at any level
- (b) Evaluating learning outcomes that materially influence the learning process
- (c) Assessing appropriate level of education and materially influencing the level of education received
- (d) Monitoring and detecting prohibited student behavior in tests/examinations

### Area 4 - Employment, Workers Management, and Self-Employment
- (a) Recruitment and selection: targeted job advertising, application filtering/screening, candidate evaluation and selection
- (b) Making decisions affecting terms of employment/work relationships: promotion, termination, task allocation, monitoring/evaluating performance/behavior of employed persons

### Area 5 - Access to and Enjoyment of Essential Private and Public Services
- (a) Public authorities evaluating individual eligibility for public assistance benefits and services (including healthcare)
- (b) Creditworthiness assessment and credit scoring (excluding fraud detection)
- (c) Life insurance and health insurance risk assessment and pricing for natural persons
- (d) Emergency dispatch and emergency call classification and prioritization

### Area 6 - Law Enforcement
- (a) Individual risk assessment for becoming victim of criminal offenses
- (b) Polygraphs and similar tools to assess reliability of persons
- (c) Evaluating reliability of evidence in criminal investigations/prosecution
- (d) Assessing risk of offending/reoffending, including recidivism assessment
- (e) Profiling natural persons in course of criminal detection, investigation, or prosecution

### Area 7 - Migration, Asylum, and Border Control Management
- (a) Polygraph-like tools and similar for competent authorities in migration/asylum/border control
- (b) Assessing risk (including security/irregular migration risk) of persons intending to enter or having entered EU territory
- (c) Assisting competent authorities in examining applications for asylum, visa, and residence permits
- (d) Detecting, recognizing, or identifying natural persons (excluding verification of travel documents)

### Area 8 - Administration of Justice and Democratic Processes
- (a) AI assisting judicial authorities in researching, interpreting, and applying the law
- (b) AI intended to influence the outcome of elections or referenda, or the voting behavior of natural persons

---

## Art. 50 - Limited Risk Transparency Obligations (applies from 2 August 2026)

> **Implementation status (May 2026):** The AI Office published a **Code of Practice on Marking and Labelling of AI-generated Content** (1st draft Dec 2025; 2nd draft 5 March 2026; finalisation expected Q2 2026) and opened consultation on **draft Art. 50 transparency guidelines in May 2026**. No formal implementing act has been adopted yet. For pre-existing systems on market before 2 Aug 2026, a grace period applies until **2 December 2026** for the machine-readable marking requirement (Art. 50(2)).

### Chatbots and AI Interaction Systems (Art. 50(1))
Providers must ensure users are informed they are interacting with an AI system, unless:
- Obvious to a reasonably well-informed user given context and circumstances
- System is authorized by law for detection of criminal offenses

### Synthetic Media - Deepfakes (Art. 50(2) and (4))
- **Providers** of systems generating synthetic image/video/audio/text must ensure outputs are marked in a machine-readable format and detectable as artificially generated or manipulated; the machine-readable marking is a provider duty under Art. 50(2)
- **Deployers** of systems generating or manipulating deepfake content must disclose that the content has been artificially generated or manipulated (Art. 50(4)); this is a disclosure duty only, not a machine-readable marking duty
- Deployer disclosure exceptions: authorized by law for criminal offense detection; artistic, satirical, or fictional works with appropriate disclosure that doesn't impair enjoyment
- All AI-generated text published to inform public on matters of public interest must be disclosed as AI-generated, unless: authorized for criminal investigation; content underwent human editorial review and editorial accountability exists

### Emotion Recognition and Biometric Categorization (Art. 50(3))
Deployers must inform natural persons exposed to these systems of:
- The operation of the system
- Must comply with GDPR and data protection law
- Exception: authorized for law enforcement

### Format Requirements
- Disclosures must be made at the latest at first interaction/exposure
- Clear and distinguishable manner
- Must meet accessibility standards (Directive 2019/882)

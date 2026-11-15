# EU AI Act - High-Risk AI System Obligations Reference

All obligations below apply to **providers** unless stated otherwise. Under the Digital Omnibus date shift, Annex III systems: applies from **2 December 2027**. Annex I safety component systems: applies from **2 August 2028**.

---

## Art. 9 - Risk Management System

**Purpose:** Identify and mitigate risks to health, safety, and fundamental rights throughout the AI system lifecycle.

**Requirements:**
- Continuous, iterative process maintained from development through decommissioning
- Must cover **all phases**: development, testing, pre-deployment assessment, post-market monitoring
- **5-step process:**
  1. Identify all known and reasonably foreseeable risks (normal use, reasonably foreseeable misuse)
  2. Estimate and evaluate risks under all intended and reasonably foreseeable uses
  3. Evaluate risks emerging from post-market monitoring data
  4. Adopt appropriate and targeted risk mitigation measures (Art. 9(4))
  5. Assess residual risk acceptability; document reasoning
- **Risk mitigation priority hierarchy (Art. 9(4)):**
  1. Design-based risk elimination first
  2. Adequate mitigation measures if elimination not possible
  3. Information provision to deployers and users
- **Testing (Art. 9(7)):** Before market placement; against pre-defined metrics and probabilistic thresholds; representative test data
- **Under-18 impact:** Special attention required for systems likely to adversely impact minors

**Documentation required:** Risk management system must be documented and form part of technical documentation (Art. 11, Annex IV).

---

## Art. 10 - Data and Data Governance

**Purpose:** Ensure training, validation, and testing datasets are appropriate for the intended purpose.

**Dataset requirements (Art. 10(2)):**
- Relevant to intended purpose
- Sufficiently representative of the persons/contexts the system will encounter
- Free of errors (where appropriate)
- Complete for the intended purpose
- Statistically appropriate for target geographic, contextual, and behavioral population

**Data governance practices (Art. 10(3)):**
- Design choices documentation
- Data collection method documentation
- Data origin examination and documentation
- Annotation, labeling, cleaning, enrichment, and aggregation procedures
- Bias examination and identification
- Gap identification in relevant properties

**Special category data (Art. 10(5)) - bias detection exception:**
Processing of special-category personal data (GDPR Art. 9) permitted ONLY when ALL conditions met:
1. No adequate alternative data source exists
2. Technical and organizational protections are in place (anonymization, pseudonymization where possible)
3. Access controls ensure minimum necessary access
4. No third-party data transfer
5. Data deleted upon completion of bias detection
6. Documented justification maintained

---

## Art. 11 - Technical Documentation

**Who:** Providers (before market placement), kept up-to-date throughout lifecycle.

**Content specified in Annex IV:**
- General description: intended purpose, provider identity, version, interactions with other systems
- Detailed description of elements and development process: training methodologies, design choices, algorithms, data used
- Information about training data (including general description, origin, annotation procedures, design choices)
- Assessment of the measures required to interpret outputs and enable human oversight
- Detailed description of the system design (architecture, source code or training code access if applicable)
- Validation and testing: procedures, applied metrics, performance benchmarks, testing datasets
- Risk management system documentation (Art. 9)
- Changes made to system over lifecycle
- List of harmonised standards applied (or description of alternative solutions for conformity)
- EU Declaration of Conformity

**Retention:** 10 years after market placement or putting into service.

---

## Art. 12 - Record-Keeping / Automatic Logging

**Who:** Providers must build in automatic logging capability; deployers must retain logs.

**Provider obligations:**
- High-risk systems must be capable of automatically generating event logs throughout operation
- Logging capability enables post-deployment reconstruction of circumstances surrounding risks
- For biometric identification: logs must enable identification of persons involved and circumstances

**Deployer obligations (Art. 26(6)):**
- Retain automatically generated logs for **minimum 6 months** from use, or as required by applicable Union/national law (whichever longer)
- Public sector deployers: stricter retention may apply under public records obligations

---

## Art. 13 - Transparency and Provision of Information to Deployers

**Purpose:** Enable deployers to understand and correctly use the AI system.

**System design requirement:** High-risk AI systems must be designed with sufficient transparency for deployers to interpret outputs and use appropriately.

**Instructions for use must include:**
- Provider identity, address, registration data
- System characteristics, capabilities, and intended purpose
- Performance metrics: level of accuracy, robustness, cybersecurity
- Known or foreseeable circumstances that may lead to risks
- System performance for specific persons/groups
- Specifications for input data (data types, formats, dimensions)
- Information on changes made vs prior versions
- Human oversight measures (Art. 14) and technical measures to enable oversight
- Computational resources required; expected system lifetime
- Description of logging mechanisms (Art. 12)
- Any predetermined modifications or updates

**Format:** Concise, complete, correct, clear, relevant; provided in digital and, where appropriate, physical format; accessible to deployers in appropriate language.

---

## Art. 14 - Human Oversight

**Purpose:** Enable effective human monitoring during operation to identify and correct AI errors.

**System design obligations (providers, Art. 14(3)):**
High-risk AI systems must be designed to allow natural persons to:
- Understand system capabilities and limitations
- Recognize **automation bias** (over-reliance on AI outputs)
- Correctly interpret AI outputs (including interpretability features)
- Decide not to use, or disregard, override, or reverse AI outputs
- Intervene through a **stop button** or similar interrupt mechanism

**Deployer implementation obligations (Art. 14(4)):**
- Assign human oversight to natural persons with necessary competence, authority, and resources
- Train oversight persons on system capabilities/limitations and automation bias risk

**Biometric identification specific (Art. 14(5)):**
- Minimum **two separate persons** must independently verify and confirm identification before action is taken

**Proportionality:** Oversight measures are built in by providers proportionate to risks and level of autonomy; deployers may need to supplement with organizational measures.

---

## Art. 15 - Accuracy, Robustness, and Cybersecurity

**Accuracy:**
- System must achieve appropriate accuracy levels for intended purpose throughout its lifecycle
- Declared accuracy levels and metrics must be in instructions for use (Art. 13)
- Training, validation, and testing data must be statistically appropriate to achieve declared levels

**Robustness:**
- Resilience against errors, faults, or inconsistencies during operation and foreseeable misuse
- Consistent performance throughout operational lifetime
- Where appropriate: technical redundancy solutions, backup plans, fail-safe mechanisms
- For continuous learning systems: eliminate/reduce risks of feedback loops amplifying biased outputs

**Cybersecurity:**
Resilience against attempts to alter use, outputs, or performance, including:
- **Data poisoning attacks** (contaminating training data)
- **Model poisoning attacks** (manipulating model weights)
- **Adversarial examples** (crafted inputs causing misclassification)
- **Confidentiality attacks** (extracting training data or model internals)
- **Model flaws exploitation** (taking advantage of design weaknesses)

**Technical solutions appropriate to context:** Air-gapping sensitive components, adversarial testing, input validation, output monitoring.

---

## Art. 16 - Provider Obligations (Complete 12-Item Checklist)

Before placing on market or putting into service, providers must:

1. ☐ Ensure system complies with Section 2 requirements (Arts. 9–15)
2. ☐ Display name, trademark, and contact address on system, packaging, or documentation
3. ☐ Establish and implement quality management system (Art. 17)
4. ☐ Keep technical documentation (Art. 11, Annex IV)
5. ☐ Retain automatically generated logs (Art. 12) where under provider's control
6. ☐ Complete required conformity assessment (Art. 43) before market placement
7. ☐ Draw up EU Declaration of Conformity (Art. 47)
8. ☐ Affix CE marking (Art. 48)
9. ☐ Register in EU AI database (Art. 49) before market placement
10. ☐ Take immediate corrective action for non-conforming systems; notify authorities and deployers (Art. 20)
11. ☐ Demonstrate conformity upon request of national competent authority
12. ☐ Ensure accessible design where required (Directives 2016/2102, 2019/882)

---

## Art. 17 - Quality Management System (13 Required Components)

Documented policies and procedures covering:

1. **Regulatory compliance strategy** including conformity assessment procedures and modifications management
2. **Design techniques** - procedures for designing, controlling, and verifying the AI system
3. **Development quality control** procedures
4. **Testing and validation** - before, during, and after development
5. **Technical standards application** - harmonised standards and common specifications
6. **Data management** - acquisition, labeling, storage, filtering, retention, cleaning procedures
7. **Risk management** per Art. 9
8. **Post-market monitoring** per Art. 72
9. **Serious incident reporting** per Art. 73 - communication with national authorities
10. **Authority communication** procedures for corrective actions and recalls (Art. 20)
11. **Record-keeping and documentation** - retention periods and access procedures
12. **Resource management** including supply-chain security measures
13. **Accountability framework** - clear responsibility assignment for all above components

**Proportionality:** QMS must be proportionate to provider organization size. Existing sectoral QMS may be adapted/integrated.

---

## Art. 26 - Deployer Obligations

1. **Instructions compliance:** Use system in accordance with provider's instructions for use (Art. 13)
2. **Staff assignment:** Assign human oversight to persons with necessary competence, training, authority, and resources
3. **Input data control:** Where deployer controls input data - ensure it is relevant and sufficiently representative
4. **Continuous monitoring:** Monitor operations; if risk identified - notify provider/importer/distributor AND market surveillance authority; suspend use where appropriate
5. **Serious incidents:** Immediately notify provider, then importer/distributor and market surveillance authority
6. **Log retention:** Retain automatically generated logs for **at least 6 months**
7. **Worker notification:** In employment/worker management contexts - inform workers and representatives before deployment
8. **Public authority registration:** Public authorities must register use in EU AI database (Art. 60) before deployment; cannot use unregistered high-risk systems
9. **GDPR:** Conduct data protection impact assessments where required under GDPR Art. 35
10. **Fundamental Rights Impact Assessment:** Required for public authorities before deploying certain high-risk systems under Art. 27

---

## Arts. 43–49 - Conformity Assessment and CE Marking

### Art. 43 - Conformity Assessment Paths

**Annex III - Point 1 Systems (Biometrics):** Provider chooses between:
- **(A) Self-assessment** - Internal control via Annex VI procedure; OR
- **(B) Notified body** - Third-party assessment under Annex VII (QMS review + technical documentation assessment)

Notified body (B) is **mandatory** when:
- No harmonised standards covering the system exist
- Standards exist but provider has not applied them (or only partially)
- Common specifications are unavailable or not used
- Standards published with restrictions that limit presumption of conformity

**Annex III - Points 2–8 Systems (Areas 2–8):** Self-assessment only - no notified body assessment available.

**Annex I Products (safety components):** Conformity assessment integrated into the existing conformity procedure for the product under Annex I legislation.

**Law enforcement / immigration / EU institutions:** Market surveillance authority acts as notified body.

**Substantial modifications:** Require full reassessment; except predetermined learning modifications documented in original technical file and declared in conformity declaration.

### Art. 47 - EU Declaration of Conformity
- Drawn up by provider (or authorised representative); provider assumes full responsibility
- Must confirm compliance with all applicable AI Act requirements (Section 2)
- Must identify: system name, provider, version, intended purpose, conformity assessment procedure followed, standards applied
- Machine-readable format; translation required into languages required by national authorities
- Maintained for **10 years** from market placement

### Art. 48 - CE Marking
- Visible, legible, indelible affixation on system, packaging, or documentation
- Only affixed after successful conformity assessment and drawing up of EU Declaration of Conformity
- Subject to general principles of CE marking (Regulation 765/2008)
- Affixed before market placement; re-affixed if system substantially modified

### Arts. 49 and 60 - EU AI Database Registration

**Provider registration (Art. 49):**
- Before market placement (Annex III systems - Art. 6(2))
- Information includes: provider/representative identity; system description, intended purpose, accuracy; conformity assessment procedure; CE marking notified body (if applicable)
- Provider registration covers all deployers and users of that system

**Public authority deployer registration (Art. 60):**
- Before deployment of registered high-risk systems
- Additional system-specific information for public authority use

**Database operation:** Commission responsibility (Art. 71). Registration obligations follow the shifted high-risk application dates under the Digital Omnibus (Annex III: 2 December 2027; Annex I: 2 August 2028).

**Publicly accessible information vs. restricted:** Most information public; some law enforcement/immigration information accessible only to competent authorities.

---

## Art. 27 - Fundamental Rights Impact Assessment (FRIA)

**Who (Art. 27(1)):** Deployers that are bodies governed by public law or private entities providing public services, and any deployer of Annex III point 5(b) or 5(c) systems, before deploying a high-risk AI system under Art. 6(2), except systems intended for use in the area listed in Annex III point 2 (critical infrastructure).

**Content:**
- Description of the deployer's processes in which the system will be used
- Time period, frequency, and number of persons affected
- The specific categories of persons likely to be affected
- Specific risks of harm to categories of affected persons
- Human oversight measures (Art. 14) planned
- Measures to address fundamental rights risks

**Relationship to GDPR DPIA:** Where GDPR DPIA is also required, the FRIA may be conducted alongside or integrated into the DPIA.

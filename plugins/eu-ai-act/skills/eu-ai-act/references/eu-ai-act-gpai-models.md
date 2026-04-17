# EU AI Act — General-Purpose AI (GPAI) Models: Obligations, Systemic Risk, and Codes of Practice

**Regulation (EU) 2024/1689, Chapter V (Articles 51–56)**
**Applicable from: 2 August 2025**

---

## Definitions and Scope

### What is a GPAI Model? (Art. 3(63))

A **general-purpose AI (GPAI) model** is an AI model that:
- Is trained with a large amount of data using self-supervision at scale
- Displays significant generality
- Is capable of competently performing a wide range of distinct tasks
- Is regardless of the way the model is placed on the market
- Can be integrated into a variety of downstream systems or applications

**Exclusion:** AI models used **before release on the market** for research, development, and prototyping activities are not GPAI models for purposes of the EU AI Act.

### What is a GPAI System? (Art. 3(64))

A **GPAI system** is an AI system based on a GPAI model that:
- Has the capability to serve a variety of purposes
- Is used for direct use as well as for integration in other AI systems

### Key distinction between GPAI models and GPAI systems

| Term | Meaning | Regulatory focus |
|------|---------|-----------------|
| GPAI model | The underlying trained model (e.g., weights + architecture) | Provider obligations under Arts. 53–55 |
| GPAI system | An AI system built on a GPAI model | Can be a standalone product or integrated into another system |

GPAI systems used as high-risk AI systems remain subject to the high-risk AI requirements in Chapter III. GPAI model providers are expected to cooperate with downstream high-risk AI system providers.

---

## Classification of GPAI Models with Systemic Risk (Article 51)

### Systemic Risk Defined (Art. 3(65))

Systemic risk means a risk that is specific to high-impact GPAI models, having a significant negative impact on the Union market due to their reach, or due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or any combination thereof, that can propagate throughout the value chain.

### Threshold for Systemic Risk Classification

A GPAI model is classified as presenting **systemic risk** if either:

**Compute threshold (Art. 51(1)(a)):**
The cumulative amount of compute used for its training measured in floating point operations (FLOPs) is greater than **10^25 FLOPs**.

**Commission determination (Art. 51(1)(b)):**
The Commission determines the model has high-impact capabilities based on criteria set out in Annex XIII or based on a qualified alert by the AI scientific panel — even if it does not meet the compute threshold.

### Notification Obligation (Art. 52)

**Providers** of GPAI models that meet or exceed the 10^25 FLOPs threshold must **notify the European Commission** within **2 weeks** of placing the model on the market or making it available. Notification is also required when updated versions exceed the threshold.

**Presumption:** A GPAI model meeting the compute threshold is presumed to present systemic risk. Providers may present arguments to the Commission that their model, despite meeting the threshold, does not present systemic risk. The Commission may accept or reject these arguments.

**Commission-initiated determination:** The AI Office, on its own initiative or following a qualified alert from the scientific panel, may determine a model presents systemic risk regardless of compute.

---

## Obligations for All GPAI Model Providers (Article 53)

The following four obligations apply to **all** GPAI model providers, unless the open-weight exception (Art. 54) applies:

### Obligation 1 — Technical Documentation (Art. 53(1)(a), Annex XI)

Providers must draw up and keep up to date technical documentation, including **training and testing process** and the results of the **evaluation** process, to be made available to the AI Office and national competent authorities on request.

**Annex XI — Minimum contents of GPAI technical documentation:**
- General description of the GPAI model
- Information about the training process (data, compute, duration)
- Information about the model's architecture
- Training data details: types of data used, volume, provenance, data curation methodology
- Modalities and capabilities the model supports
- Information about evaluation approaches and benchmarks used
- Description of risks and mitigating measures
- Record of known or reasonably foreseeable risks to fundamental rights
- Technical measures taken to ensure downstream providers understand capabilities/limitations

### Obligation 2 — Information for Downstream Providers (Art. 53(1)(b), Annex XII)

Providers must draw up and maintain **documentation for downstream providers** — i.e., organisations that integrate the GPAI model into their own AI systems — to enable those downstream providers to comply with their own EU AI Act obligations (particularly high-risk AI requirements if the downstream system becomes high-risk).

**Annex XII — Minimum information to be provided to downstream providers:**
- Identity and contact details of the GPAI model provider
- Capabilities and limitations of the model (including documented performance benchmarks)
- Conditions under which the model may be integrated into AI systems
- Any known risks, limitations, or biases
- Summary of the training data used
- Information required to comply with technical documentation obligation (Annex IV) for downstream high-risk AI providers
- Applicable usage policies and restrictions

**Format:** May be provided via model cards, API documentation, or similar technical documentation formats.

### Obligation 3 — Copyright Compliance Policy (Art. 53(1)(c))

Providers must put in place a **policy to comply with Union copyright law**, and in particular to identify and comply with including through state of the art technologies, a reservation of rights expressed pursuant to Article 4(3) of Directive (EU) 2019/790 (Copyright in the Digital Single Market Directive).

**Practical requirements:**
- Implement a process to respect opt-outs expressed by rights holders under Art. 4(3) of Directive 2019/790
- Document the copyright compliance policy
- Apply this to training data sourcing and processing

**Art. 4(3) of Directive 2019/790:** Rights holders may expressly reserve the right to opt out of the text-and-data mining exception (Art. 4(1)) — for example through machine-readable notices. GPAI providers must detect and honour such opt-outs.

### Obligation 4 — Summary of Training Content (Art. 53(1)(d))

Providers must publish and maintain a **sufficiently detailed summary** about the content used for training the GPAI model.

**Format:** The AI Office published a template for compliance with this obligation (released 2025). The summary must be:
- Sufficiently detailed to enable rights holders and the public to understand what data was used
- Made publicly available (e.g., model card, website)
- Updated when the model is retrained on significantly new or different data

---

## Obligations for Open-Weight / Free and Open Licence GPAI Models (Article 54)

### Scope of Open-Weight Exemption

A GPAI model qualifies for the reduced obligations under Art. 54 if:
- The **parameters** including weights are publicly available
- The **model architecture** is publicly available
- The **model usage information** is publicly available
- The above allows for **access, usage, modification, and distribution** of the model

In other words: the model is genuinely open — weights released under an open licence.

### Reduced Obligations for Open-Weight GPAI Models

Open-weight GPAI model providers **only** need to comply with:
- **Obligation 3** (copyright policy — Art. 53(1)(c))
- **Obligation 4** (training summary — Art. 53(1)(d))

They are **exempt** from:
- Obligation 1 (technical documentation for authorities)
- Obligation 2 (information for downstream providers)

### Exception to Open-Weight Exemption: Systemic Risk

If an open-weight GPAI model **presents systemic risk** (i.e., trained with > 10^25 FLOPs or Commission-designated), the open-weight exemption does **not apply** to the systemic risk obligations under Art. 55. The provider must comply in full with both Arts. 53 and 55, regardless of open-weight status.

---

## Obligations for GPAI Models with Systemic Risk (Article 55)

In addition to the Art. 53 obligations (unless open-weight, in which case Art. 54 applies but Art. 55 applies regardless), providers of GPAI models with systemic risk must:

### Obligation A — Model Evaluations including Adversarial Testing (Art. 55(1)(a))

Providers must perform model evaluations in accordance with standardised protocols and tools when available, including conducting and documenting **adversarial testing** of the model with the aim of identifying and mitigating systemic risks.

**What adversarial testing must cover:**
- Red-teaming — testing the model to identify failure modes, dangerous capabilities, misalignments
- Capabilities evaluation — systematic assessment of potentially dangerous capabilities (e.g., capability to assist with weapons of mass destruction, cyberattacks, manipulation at scale)
- Alignment evaluation — assessment of the model's susceptibility to being steered toward harmful outputs
- Specific risk categories identified in systemic risk assessment

**Codes of practice** will provide detailed methodologies. The AI Office's GPAI code of practice (published May 2025) contains evaluation standards.

### Obligation B — Assess and Mitigate Systemic Risks (Art. 55(1)(b))

Providers must assess and mitigate the possible systemic risks at Union level that may stem from the development, placement on the market, or use of GPAI models with systemic risk, including their sources.

**Risk categories to assess (from Recitals 110–115 and Annex XIII):**
- Risks to critical infrastructure (energy, water, financial systems, healthcare, transport)
- Risks to democratic processes and elections
- Risks enabling mass-casualty weapons development (CBRN)
- Cybersecurity risks including large-scale cyberattacks
- Risks to fundamental rights (discrimination at scale, manipulation)
- Societal risks (widespread disinformation, cognitive manipulation)

### Obligation C — Incident Tracking, Documentation, and Reporting (Art. 55(1)(c))

Providers must track, document, and **report serious incidents** and possible corrective measures to the **AI Office** and, where relevant, to national competent authorities, **without undue delay** after becoming aware.

**What constitutes a "serious incident" for GPAI models:**
- Any incident or malfunction of the GPAI model resulting in death or serious harm to a natural person
- Any disruption to critical infrastructure
- Any significant breach of fundamental rights
- Any event causing widespread harm (e.g., mass-scale disinformation)

**Reporting channel:** Reports go to the AI Office. The AI Office coordinates with national authorities as appropriate.

### Obligation D — Cybersecurity Protection (Art. 55(1)(d))

Providers must ensure an adequate level of **cybersecurity protection** for the GPAI model with systemic risk and its physical infrastructure.

**Key measures:**
- Protection of model weights against unauthorised access, theft, or exfiltration
- Protection of training infrastructure against compromise
- Access controls for fine-tuning and model modification
- Monitoring for adversarial interference with deployed model APIs

---

## Codes of Practice for GPAI Models (Article 56)

### Purpose

Codes of practice are the primary compliance tool for GPAI obligations before and alongside harmonised standards. They specify the practical methodology for meeting Arts. 53–55 obligations.

### Development Process

- Developed by the **AI Office** in collaboration with GPAI model providers, national competent authorities, civil society, academia, and independent experts
- **Timeline:** Codes of practice were required to be ready by **2 May 2025**
- Lead body: European AI Office

### Current Status (as of 2026)

The AI Office published the first version of the GPAI Code of Practice in May 2025. The code provides:
- Templates and methodology for technical documentation (Annex XI compliance)
- Methodology for training content summary (Annex XII compliance)
- Evaluation methodologies for systemic risk assessment
- Adversarial testing protocols and benchmarks
- Incident reporting procedures and templates

**Compliance presumption:** Adherence to the code of practice creates a presumption of conformity with Arts. 53–55. Providers choosing not to adhere must demonstrate alternative adequate means of compliance to the AI Office's satisfaction.

### Voluntary Participation for Minimal/Limited Risk AI

Providers of minimal or limited risk AI systems may voluntarily adhere to codes of conduct (Art. 95). These are separate from the mandatory GPAI codes of practice and cover areas such as:
- Transparency and explainability beyond Art. 50 requirements
- Bias detection and mitigation
- Energy efficiency
- Human oversight in non-high-risk applications

---

## GPAI Models in the High-Risk AI Value Chain

When a GPAI model is integrated into a high-risk AI system, cooperation is required between the GPAI model provider (upstream) and the high-risk AI system provider (downstream):

**GPAI model provider responsibilities when used in high-risk:**
- Provide information sufficient for the downstream provider to comply with Annex IV technical documentation
- Cooperate reasonably with downstream providers conducting conformity assessments
- Continue to maintain and update the model information made available (Art. 53(1)(b))

**Downstream high-risk AI system provider responsibilities:**
- The downstream provider remains responsible for their high-risk AI system's compliance
- They must conduct their own risk assessment and conformity assessment
- They cannot rely solely on the GPAI model provider's documentation

**Contractual provisions:** Art. 25(4) provides that where both provider and deployer contribute to obligations, they may assign contractual responsibilities between themselves, but this does not remove statutory obligations to third parties and authorities.

---

## Interaction with EU AI Act Governance for GPAI

| Actor | Role in GPAI governance |
|-------|------------------------|
| AI Office | Primary supervisor of GPAI model providers; conducts investigations; issues codes of practice; accepts incident reports; can impose fines |
| Scientific Panel | Advises AI Office on systemic risk evaluations; can issue qualified alerts triggering Commission investigation |
| National Competent Authorities | May receive complaints about downstream GPAI systems; coordinate with AI Office |
| AI Board | Coordinates Member State positions on GPAI; issues opinions |

**Complaint mechanism:** Any person or organisation can lodge a complaint with the AI Office about a GPAI model provider's non-compliance (Art. 63(1)).

**AI Office investigation powers:**
- Request information and documentation
- Conduct interviews with provider personnel
- Commission independent evaluations of the model
- Impose interim measures where systemic risk requires urgent action
- Recommend fines to the Commission (which retains final decision on fines for GPAI)

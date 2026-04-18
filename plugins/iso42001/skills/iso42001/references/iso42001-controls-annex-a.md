# ISO/IEC 42001:2023 — Annex A Controls (All 38)

ISO/IEC 42001:2023 Annex A contains **38 controls** organised across **9 control domains** (A.2–A.10). Within each domain, the .1 sub-clause contains the domain objective statement — the numbered controls begin at .2 (or .1.2 / .2.2 for A.6's two sub-objectives). Annex B provides implementation guidance for each control.

> **How to use:** Controls are selected based on organisational role (provider, user, or both), AI system impact level, and risk assessment outcomes. Inapplicable controls must be justified in the Statement of Applicability (SoA).

---

## A.2 — Policies Related to AI (3 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.2.2 | AI policy | Provider + User | A formal AI policy shall be established, documented, and communicated. The policy shall include the organisation's commitment to responsible AI development or use, alignment with organisational values and legal obligations, and a framework for setting AI objectives. Signed by top management. |
| A.2.3 | Alignment with other organisational policies | Provider + User | AI-specific requirements shall be incorporated into existing organisational policies (e.g. HR, procurement, IT, data governance, information security) where those policies affect or are affected by AI systems. |
| A.2.4 | Review of the AI policy | Provider + User | The AI policy shall be reviewed at planned intervals and when significant changes occur, to ensure its continuing suitability, adequacy, and effectiveness. |

**Common gaps:** AI policy exists but lacks specific responsible AI commitments; other organisational policies not updated to address AI; policy review cycle not defined.

---

## A.3 — Internal Organisation (2 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.3.2 | AI roles and responsibilities | Provider + User | Roles and responsibilities for AI governance shall be defined, assigned, communicated, and documented. This includes accountability for individual AI systems, data governance, and AIMS oversight. A RACI matrix or equivalent is recommended. |
| A.3.3 | Reporting of concerns | Provider + User | Mechanisms shall be established for personnel to raise concerns about AI systems — including ethical concerns, bias observations, unexpected outputs, or policy non-compliance — without fear of reprisal. |

**Common gaps:** AI ownership is informal or split across teams without clear accountability; no channel for staff to report AI concerns.

---

## A.4 — Resources for AI Systems (5 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.4.2 | Resource documentation | Provider + User | The resources required to develop, deploy, operate, and maintain AI systems shall be identified and documented, including compute, data, tooling, and human resources. |
| A.4.3 | Data resources | Provider | Policies and controls shall govern the acquisition, management, and quality assurance of data resources used in AI systems — covering training, validation, and test data. |
| A.4.4 | Tooling resources | Provider | Controls shall govern the selection, procurement, and management of AI tooling — including development frameworks, model libraries, and evaluation platforms. |
| A.4.5 | System and computing resources | Provider | Controls shall govern the compute infrastructure used for AI development and deployment: provisioning, access control, capacity management, and decommissioning. |
| A.4.6 | Human resources | Provider + User | AI-specific competency requirements shall be documented. Training programmes shall be established for AI developers, operators, and business users. An awareness programme shall be maintained for all staff who interact with or are affected by AI. |

**Common gaps:** No AI-specific competency framework; staff AI awareness training absent; third-party AI tools not inventoried; data resource governance undocumented.

---

## A.5 — Assessing Impacts of AI Systems (4 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.5.2 | AI system impact assessment process | Provider + User | A documented process for assessing the impacts of AI systems shall be established and maintained. The process shall define scope, methodology, frequency of assessment, roles, and how assessment results inform control selection and treatment decisions. |
| A.5.3 | Documentation of AI system impact assessments | Provider + User | Results of AI system impact assessments shall be documented, retained, and updated when significant changes occur to the AI system or its operating context. |
| A.5.4 | Assessing AI system impact on individuals or groups of individuals | Provider + User | The impact assessment shall evaluate how AI system outputs may affect individual rights, wellbeing, and autonomy. This includes risks of discrimination, profiling, automated decision-making without meaningful human review, and disproportionate impacts on vulnerable individuals or groups. |
| A.5.5 | Assessing societal impacts of AI systems | Provider + User | The impact assessment shall evaluate broader societal impacts: potential for misinformation generation, labour market effects, environmental impact of AI compute, reinforcement of systemic bias at scale, and erosion of human autonomy. |

**Common gaps:** Impact assessment performed once at deployment but never revisited; societal impact dimension skipped; no documented process — assessments done ad hoc.

---

## A.6 — AI System Life Cycle (9 controls)

A.6 is divided into two sub-objectives: **A.6.1 Management guidance** and **A.6.2 AI system life cycle**. The .1 sub-clause in each group contains the objective statement; controls begin at .2.

### A.6.1 — Management Guidance (2 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.6.1.2 | Objectives for responsible development of AI system | Provider | Specific, measurable objectives for responsible AI development shall be established, documented, and monitored. These shall align with the AI policy and responsible AI principles (fairness, transparency, accountability, safety, reliability). |
| A.6.1.3 | Processes for responsible AI system design and development | Provider | Formal processes shall govern AI system design and development to embed responsible AI principles: fairness-aware design, documentation of design decisions, explainability requirements proportionate to AI impact level, and human oversight at key development gates. |

### A.6.2 — AI System Life Cycle (7 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.6.2.2 | AI system requirements and specification | Provider | Requirements for each AI system shall be documented, including intended purpose, performance criteria, operating conditions, input/output specifications, and applicable constraints (legal, ethical, technical). |
| A.6.2.3 | Documentation of AI system design and development | Provider | Design decisions, architecture choices, model versions, hyperparameters, and development rationale shall be documented to support reproducibility, auditability, and accountability. |
| A.6.2.4 | AI system verification and validation | Provider | Testing protocols shall be applied before deployment: performance benchmarking, fairness and bias testing across demographic groups, adversarial testing, edge case validation, and go/no-go authorisation criteria. |
| A.6.2.5 | AI system deployment | Provider | A controlled deployment process shall govern AI system releases: staged rollout, deployment authorisation, risk and impact assessment sign-off, and rollback procedures. |
| A.6.2.6 | AI system operation and monitoring | Provider + User | Continuous monitoring of AI systems in production shall detect performance drift, output quality degradation, and bias. Alert thresholds and remediation processes shall be defined. |
| A.6.2.7 | AI system technical documentation | Provider + User | Comprehensive technical documentation per AI system shall be maintained: specifications, intended use, known limitations, performance data, and failure modes. This supports transparency obligations and third-party assessment. |
| A.6.2.8 | AI system recording of event logs | Provider + User | AI systems shall record event logs sufficient to support incident investigation, audit, performance monitoring, and accountability. Log retention periods and access controls shall be defined. |

**Common gaps:** No model versioning or reproducibility controls; bias testing not documented; no production monitoring for model drift; deployment lacks formal authorisation process; event logs not retained or scoped to AI systems.

---

## A.7 — Data for AI Systems (5 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.7.2 | Data for development and enhancement of AI system | Provider | A governance framework shall define how data is managed across the full AI data lifecycle: acquisition, quality assurance, labelling, versioning, bias testing, retention, and secure deletion. |
| A.7.3 | Acquisition of data | Provider | Controls shall govern how training, validation, and test data is sourced: legal basis for data use, consent requirements where applicable, provenance documentation, and prohibition on use of unlawfully obtained data. |
| A.7.4 | Quality of data for AI systems | Provider | Data quality criteria shall be defined for training, validation, and test data — covering completeness, accuracy, representativeness, and recency — and tested before data is used in AI development. |
| A.7.5 | Data provenance | Provider | The origin, chain of custody, and transformation history of data used in AI systems shall be documented and traceable. This supports accountability, bias identification, and regulatory compliance. |
| A.7.6 | Data preparation | Provider | Processes for data cleaning, transformation, labelling, and annotation shall include quality controls: human review of labelled data, inter-annotator agreement checks, and identification and remediation of bias introduced in preparation steps. |

**Common gaps:** Training data sourcing undocumented; no data quality criteria or tests; labelling process not auditable; provenance tracking absent; data preparation bias controls missing.

---

## A.8 — Information for Interested Parties of AI Systems (4 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.8.2 | System documentation and information for users | Provider + User | Documentation and information about AI systems shall be provided to users and other interested parties at a level of detail proportionate to the AI system's impact. This includes intended purpose, known limitations, and how to interpret AI outputs. |
| A.8.3 | External reporting | Provider + User | The organisation shall define what information about AI systems is reported externally, to whom, how frequently, and through what mechanism — including regulatory disclosures, transparency reports, and public-facing AI disclosures. |
| A.8.4 | Communication of incidents | Provider + User | AI-specific incident communication processes shall be established: internal escalation, notification to affected individuals where required, regulatory reporting (e.g., under sector-specific AI or data protection laws), and post-incident review and disclosure. |
| A.8.5 | Information for interested parties | Provider + User | Stakeholders — including customers, employees, regulators, and the public — shall be informed of their rights and what to expect from AI systems. A communication plan shall address what to communicate, when, and through which channel. |

**Common gaps:** No disclosure to users that AI is involved in decision-making; incident reporting processes not extended to AI-specific scenarios; no external transparency reporting; stakeholder communication plan absent.

---

## A.9 — Use of AI Systems (3 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.9.2 | Processes for responsible use of AI systems | User (primarily) | Formal processes shall govern how the organisation uses AI systems responsibly, including acceptable use criteria, human oversight of AI outputs, and procedures for escalating or overriding AI decisions. |
| A.9.3 | Objectives for responsible use of AI system | User (primarily) | Measurable objectives for responsible AI use shall be established and monitored, aligned to the AI policy and responsible AI principles. These objectives drive continual improvement in AI use practices. |
| A.9.4 | Intended use of the AI system | Provider + User | The intended use of each AI system shall be documented, communicated, and enforced. Use beyond the documented intended purpose shall be identified, assessed, and controlled. |

**Common gaps:** No acceptable use policy for AI; staff using AI tools beyond intended scope; no formal objectives for responsible AI use; human oversight procedures not documented.

---

## A.10 — Third-Party and Customer Relationships (3 controls)

| Control ID | Control Name | Applies To | Description |
|-----------|-------------|-----------|-------------|
| A.10.2 | Allocating responsibilities | Provider + User | Where AI systems involve multiple parties (providers, users, customers, partners), responsibilities for responsible AI governance shall be clearly allocated and documented — including who is responsible for impact assessment, monitoring, and incident response. |
| A.10.3 | Suppliers | Provider + User | AI supply chain risk management shall govern third-party AI providers: tiering by risk, due diligence questionnaires, contractual AI-specific clauses (including data handling, bias controls, and right to audit), and ongoing supplier performance monitoring. |
| A.10.4 | Customers | Provider | Where AI systems are deployed to customers, the organisation shall define what information customers receive about AI system capabilities and limitations, what obligations customers have in responsible use, and how customer feedback and incidents are managed. |

**Common gaps:** No AI-specific supplier due diligence questionnaire; no contractual AI clauses with key AI vendors; responsibilities between provider and user not formally allocated; no customer-facing AI use obligations.

---

## Summary: Controls by Organisational Role

| Domain | # Controls | AI Provider | AI User |
|--------|-----------|------------|---------|
| A.2 Policies | 3 | Both | Both |
| A.3 Internal Organisation | 2 | Both | Both |
| A.4 Resources | 5 | Primary (all 5) | A.4.2, A.4.6 |
| A.5 Impact Assessment | 4 | Both | Both |
| A.6 AI System Life Cycle | 9 | Primary (all 9) | A.6.2.6, A.6.2.7, A.6.2.8 |
| A.7 Data | 5 | Primary (all 5) | Limited |
| A.8 Information | 4 | Both | Both |
| A.9 Use of AI Systems | 3 | A.9.4 | Primary (all 3) |
| A.10 Third-Party / Customer | 3 | Both | A.10.2, A.10.3 |
| **Total** | **38** | | |

**Controls by ID (complete list):**
A.2.2, A.2.3, A.2.4, A.3.2, A.3.3, A.4.2, A.4.3, A.4.4, A.4.5, A.4.6, A.5.2, A.5.3, A.5.4, A.5.5, A.6.1.2, A.6.1.3, A.6.2.2, A.6.2.3, A.6.2.4, A.6.2.5, A.6.2.6, A.6.2.7, A.6.2.8, A.7.2, A.7.3, A.7.4, A.7.5, A.7.6, A.8.2, A.8.3, A.8.4, A.8.5, A.9.2, A.9.3, A.9.4, A.10.2, A.10.3, A.10.4

> **Note on control ID numbering:** Within each domain, sub-clause .1 contains the domain objective statement (not a control). Controls begin at .2. Domain A.6 has two sub-objectives (A.6.1 Management guidance and A.6.2 AI system life cycle), each with their objective at .1 and controls starting at .2. This is why control IDs in A.6 are formatted as A.6.1.2, A.6.1.3, A.6.2.2 … A.6.2.8.

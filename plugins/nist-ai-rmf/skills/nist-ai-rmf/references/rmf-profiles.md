# NIST AI RMF — AI Risk Profiles, Metrics, and Cross-Framework Mapping

---

## AI Risk Profile Concept

An **AI Risk Profile** is an organization's customization of the AI RMF to reflect:
- Its specific AI use cases and deployment contexts
- Applicable laws and regulations
- Its defined risk tolerance
- The trustworthiness properties most relevant to its AI systems

The AI RMF defines two profile types:

| Profile Type | Description | Use |
|-------------|-------------|-----|
| **Current Profile** | Where the organization is today — which categories are implemented and to what degree | Baseline assessment |
| **Target Profile** | Where the organization wants to be — desired state for each category | Gap analysis and roadmap |

The gap between Current and Target Profile drives the risk management roadmap.

### How to Build an AI Risk Profile

1. **Scope** — Define which AI systems are in scope (all AI, specific high-risk systems, or a single system)
2. **Assess Current State** — Rate each of the 19 categories: Not Started (0) / Partial (1) / Implemented (2) / Optimized (3)
3. **Set Target State** — Define the desired maturity level for each category based on risk tolerance and regulatory requirements
4. **Gap Analysis** — Categories where Target > Current are gaps requiring action
5. **Prioritise** — Weight gaps by the risk they represent; address highest-risk gaps first
6. **Roadmap** — Assign owners, timelines, and resources to close each gap

---

## Trustworthy AI Characteristics — Metrics and Indicators

### 1. Accuracy and Validity
| Metric | Description |
|--------|-------------|
| Precision / Recall / F1 | Classification accuracy metrics |
| AUC-ROC | Discriminative performance |
| Mean Absolute Error (MAE) | Regression performance |
| Calibration Error | Alignment between predicted probability and actual frequency |
| Out-of-distribution (OOD) performance | Performance on inputs outside training distribution |

### 2. Fairness and Bias Management
| Metric | Description |
|--------|-------------|
| Demographic Parity | Equal positive prediction rates across groups |
| Equalized Odds | Equal true positive and false positive rates across groups |
| Counterfactual Fairness | Would outcome change if sensitive attribute changed? |
| Disparate Impact Ratio | Ratio of positive outcome rates between groups (≥0.8 is EEOC "4/5ths rule") |
| Disaggregated performance reporting | Performance broken down by demographic subgroup |

### 3. Explainability and Interpretability
| Method | Description |
|--------|-------------|
| SHAP (SHapley Additive exPlanations) | Global and local feature attribution |
| LIME (Local Interpretable Model-agnostic Explanations) | Local approximation of complex models |
| Counterfactual explanations | "What would need to change for a different outcome?" |
| Model cards | Standardized summary of model performance, intended use, and limitations |
| Saliency maps | Visual highlighting of input features driving image model decisions |

### 4. Robustness and Reliability
| Metric | Description |
|--------|-------------|
| Adversarial accuracy | Performance under evasion attacks (FGSM, PGD) |
| Poisoning resilience | Resistance to training data manipulation |
| Input perturbation sensitivity | Performance stability under small input variations |
| Availability under load | System uptime and latency under peak conditions |
| Model drift detection | Statistical tests (PSI, KS test) on input data distribution over time |

### 5. Privacy
| Approach | Description |
|----------|-------------|
| Differential Privacy (ε) | Mathematical privacy guarantee; lower ε = stronger privacy |
| k-Anonymity | Minimum group size in training data to prevent re-identification |
| Federated learning | Training on decentralized data without centralizing raw data |
| Membership inference attack resistance | Resistance to inferring whether a record was in training data |

### 6. Security
| Threat | Description |
|--------|-------------|
| Evasion attacks | Adversarial inputs crafted to fool the deployed model |
| Poisoning attacks | Malicious training data injected to corrupt model behaviour |
| Model extraction / inversion | Reverse-engineering the model or reconstructing training data from outputs |
| Prompt injection (LLMs) | Malicious input that hijacks model behaviour through instructions |

---

## Sector-Specific AI Risk Considerations

| Sector | Key AI Risk Priorities | Relevant Regulations |
|--------|----------------------|---------------------|
| **Healthcare** | Safety (diagnosis errors), bias across patient populations, explainability for clinical decisions | HIPAA, FDA AI/ML-based SaMD guidance, EU AI Act (high-risk: medical devices) |
| **Financial Services** | Credit decision fairness, model explainability (adverse action notices), fraud detection accuracy | ECOA, Fair Housing Act, CFPB guidance, EU AI Act (high-risk: credit scoring) |
| **HR / Recruitment** | Hiring bias, EEOC disparate impact, explainability of screening decisions | EEOC, NYCA Local Law 144, EU AI Act (high-risk: employment) |
| **Criminal Justice** | Recidivism prediction bias, due process, transparency | EU AI Act (prohibited: real-time biometric, social scoring) |
| **Government / Public Sector** | Transparency, equal access, civil rights compliance | Executive Order 13960, EO 14110, AI Act (public authority deployments) |
| **Education** | Bias in admissions/grading, student privacy | FERPA, COPPA, state AI in education laws |
| **Autonomous Systems** | Physical safety, fault tolerance, human override | ISO 26262 (automotive), DO-178C (aviation), EU AI Act (high-risk) |

---

## Cross-Framework Mapping

### NIST AI RMF ↔ ISO/IEC 42001:2023

| AI RMF Function/Category | ISO 42001 Equivalent |
|--------------------------|---------------------|
| GOVERN 1 (Policies in place) | Clause 5 (Leadership), Clause 6 (Planning), A.2 (Policies related to AI), A.2.2 (AI policy) |
| GOVERN 2 (Accountability) | Clause 5.3 (Roles and responsibilities), A.3.2 (AI roles and responsibilities) |
| GOVERN 3 (Workforce diversity and DEIA) | Clause 7.2 (Competence), A.4.6 (Human resources) |
| GOVERN 4 (Cross-functional teams) | Clause 7.3 (Awareness), A.3.3 (Reporting of concerns) |
| GOVERN 5 (Engagement with AI actors) | Clause 7.4 (Communication), A.8.5 (Information for interested parties) |
| MAP 1 (Context) | Clause 4 (Context of the organization), A.3 (Internal organisation) |
| MAP 2 (Scientific understanding) | A.6 (AI system life cycle) |
| MAP 3 (Stakeholder risk/benefit) | Clause 4.2 (Interested parties), A.5.4 (Assessing AI system impact on individuals or groups of individuals) |
| MAP 5 (Likelihood/impact) | A.5.2 (AI system impact assessment process), A.5.5 (Assessing societal impacts of AI systems) |
| MEASURE 2 (System evaluation) | A.6.2.4 (AI system verification and validation), A.9 (Use of AI systems) |
| MEASURE 3 (Ongoing monitoring) | Clause 9.1 (Monitoring, measurement, analysis and evaluation), A.6.2.6 (AI system operation and monitoring) |
| MANAGE 1 (Treatment and prioritization) | Clause 6.1.3 (AI risk treatment), A.5.3 (Documentation of AI system impact assessments) |
| MANAGE 3 (Third-party risks) | A.10.2 (Allocating responsibilities), A.10.3 (Suppliers) |
| MANAGE 4 (Monitoring, incidents, improvement) | Clause 9 (Performance evaluation), A.8.4 (Communication of incidents), Clause 10 (Improvement) |
| MANAGE 4.2 (Continual improvement) | Clause 10.2 (Nonconformity and corrective action), Clause 9.3 (Management review) |

---

### NIST AI RMF ↔ EU AI Act (Regulation (EU) 2024/1689)

| AI RMF Function | EU AI Act Requirement |
|----------------|----------------------|
| GOVERN 1 (AI risk policies) | Art. 9 (Risk management system) for high-risk AI |
| GOVERN 2/3 (Accountability) | Art. 16 (Obligations of high-risk AI providers), Art. 26 (Deployer obligations) |
| MAP 1 (Intended use) | Art. 9(2) — risk management must cover intended and reasonably foreseeable misuse |
| MAP 3 (Stakeholder mapping) | Art. 9(2)(b) — identification and analysis of known and foreseeable risks |
| MEASURE 2 (System evaluation) | Art. 10 (Data governance), Art. 15 (Accuracy, robustness, cybersecurity) |
| MEASURE 3 (Ongoing monitoring) | Art. 72 (Post-market monitoring), Art. 26(5) — deployer monitoring obligations |
| MANAGE 4.1/4.3 (Post-deployment monitoring, incident communication) | Art. 73 (Reporting of serious incidents to market surveillance) |
| All functions | Art. 11 and Annex IV (Technical documentation for high-risk AI systems) |

**Key difference:** The EU AI Act is mandatory for in-scope providers and deployers; the NIST AI RMF is voluntary. Organizations subject to the EU AI Act should use NIST AI RMF as the risk management methodology that satisfies Art. 9's "appropriate risk management system" requirement.

---

### NIST AI RMF ↔ NIST CSF 2.0

| AI RMF Function | NIST CSF 2.0 Function |
|----------------|----------------------|
| GOVERN | GV (Govern) — directly analogous |
| MAP | ID (Identify) — risk identification |
| MEASURE | DE (Detect) + ID (Identify) |
| MANAGE | RS (Respond) + RC (Recover) + PR (Protect) |

**Relationship:** NIST CSF 2.0 covers cybersecurity risk broadly; NIST AI RMF extends this specifically to AI risks including bias, fairness, explainability, and societal harms — which are outside CSF's scope. Organizations should implement both: CSF for cybersecurity risk, AI RMF for AI-specific risks.

---

### NIST AI RMF ↔ NIST Privacy Framework

| AI RMF Category | Privacy Framework Core |
|----------------|----------------------|
| GOVERN 1.1 (Legal and regulatory requirements) | GV.PO-P (Privacy policies) |
| MAP 1 (Context) | CT.DM-P (Data Processing Management) |
| MAP 3 (Affected individuals) | CT.DP-P (Disassociated processing) |
| MEASURE 2 (Privacy evaluation) | CM.PO-P (Communication policies) |
| MANAGE 4.1/4.3 (Post-deployment monitoring, incident communication) | CM.AW-P (Data Processing Awareness) |

---

## Maturity Framing

NIST AI 100-1 defines the Core (GOVERN, MAP, MEASURE, MANAGE) and Profiles only; it defines no implementation tiers. Organizations that want a maturity scale can borrow the NIST CSF Implementation Tiers as an internal convention, clearly labeled as a CSF construct rather than AI RMF structure.

## Common Gap Patterns and Remediation Priorities

| Gap Pattern | Likely Cause | Recommended Action |
|-------------|-------------|-------------------|
| GOVERN complete but MAP/MEASURE weak | Policies written but not operationalized | Run system-level AI risk assessments using MAP for each deployed AI system |
| MAP done but MEASURE absent | Risk identified but not measured | Instrument deployed models with monitoring; define metrics for each identified risk |
| MEASURE present but no MANAGE actions | Measurements not connected to treatment | Establish measurement-to-action protocols; assign risk owners to register entries |
| Inconsistent across business units | No centralized AI risk programme | Establish central AI governance function with cross-BU working group |
| Strong technical controls, weak societal risk view | Engineering-led programme | Add legal, ethics, and affected-community perspectives to MAP 3 and MEASURE 2 |
| No lifecycle coverage | Only deployment-phase focus | Extend AI RMF coverage to design, development, and decommission stages |

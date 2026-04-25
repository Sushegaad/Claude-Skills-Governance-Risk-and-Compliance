# AI Risk Register: Credit Scoring Model
**Organization:** Financial Services Firm
**AI System:** Credit Scoring / Lending Decision Model
**Framework:** NIST AI Risk Management Framework (AI RMF 1.0)
**Document Date:** 2026-04-25
**Review Cycle:** Quarterly

---

## How to Use This Register

Each risk entry maps to one or more NIST AI RMF core functions:
- **GOVERN** – Policies, accountability, culture, and organizational practices
- **MAP** – Context, risk identification, and categorization
- **MEASURE** – Risk analysis, evaluation, and prioritization
- **MANAGE** – Risk response, treatment, and residual risk monitoring

Likelihood and Impact are rated 1 (Low) to 5 (High). Risk Score = Likelihood x Impact.

| Score Range | Rating |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–14 | High |
| 15–25 | Critical |

---

## Risk Register

### RISK-001: Algorithmic Bias and Discriminatory Outcomes

| Field | Detail |
|---|---|
| **Risk ID** | RISK-001 |
| **Risk Category** | Fairness / Bias |
| **Description** | The credit scoring model may produce systematically different approval rates or score distributions across protected classes (race, gender, age, national origin, religion, marital status) due to biased training data, proxy variables, or model architecture, violating the Equal Credit Opportunity Act (ECOA) and Fair Housing Act (FHA). |
| **Affected Stakeholders** | Loan applicants, compliance team, regulators (CFPB, OCC), legal counsel |
| **Likelihood** | 4 |
| **Impact** | 5 |
| **Risk Score** | 20 (Critical) |
| **NIST AI RMF Mapping** | MAP 1.5, MAP 2.3, MEASURE 2.5, MEASURE 2.9, MANAGE 2.2 |
| **AI RMF Function** | MAP, MEASURE, MANAGE |

**Treatment Options:**
1. Conduct pre-deployment disparate impact analysis using the four-fifths rule across all protected class proxies
2. Implement fairness-aware machine learning techniques (e.g., reweighting, adversarial debiasing, post-processing calibration)
3. Establish ongoing monitoring dashboards tracking approval rate parity, score distribution parity, and demographic breakdowns
4. Remove or carefully audit proxy variables that correlate with protected characteristics (e.g., zip code, certain employment types)
5. Engage a third-party fair lending audit annually
6. Maintain documented adverse action reason codes that are meaningful and non-discriminatory

**Residual Risk Owner:** Chief Risk Officer / Fair Lending Officer
**Review Frequency:** Monthly monitoring; quarterly deep-dive

---

### RISK-002: Model Performance Degradation Over Time

| Field | Detail |
|---|---|
| **Risk ID** | RISK-002 |
| **Risk Category** | Model Reliability / Accuracy |
| **Description** | The model's predictive accuracy may deteriorate due to concept drift (changing economic conditions, consumer behavior shifts post-COVID, rising interest rates) or data drift (changes in applicant population characteristics), leading to suboptimal lending decisions and increased default rates. |
| **Affected Stakeholders** | Risk management team, credit analysts, investors, regulators |
| **Likelihood** | 4 |
| **Impact** | 4 |
| **Risk Score** | 16 (Critical) |
| **NIST AI RMF Mapping** | MEASURE 2.6, MEASURE 2.7, MANAGE 3.1, MANAGE 3.2 |
| **AI RMF Function** | MEASURE, MANAGE |

**Treatment Options:**
1. Implement statistical process control monitoring (PSI, CSI, KS statistic, Gini coefficient) on a scheduled cadence
2. Define clear model performance thresholds that trigger review or retraining
3. Establish a model retraining pipeline with version control and rollback capability
4. Conduct champion/challenger testing before promoting retrained models to production
5. Maintain a model inventory with documented performance benchmarks for each vintage
6. Schedule annual full model validation by an independent model risk team

**Residual Risk Owner:** Model Risk Management Lead
**Review Frequency:** Monthly performance metrics; annual full validation

---

### RISK-003: Lack of Explainability and Adverse Action Compliance

| Field | Detail |
|---|---|
| **Risk ID** | RISK-003 |
| **Risk Category** | Transparency / Explainability |
| **Description** | Complex ensemble or deep learning credit scoring models may produce decisions that cannot be adequately explained to denied applicants, violating ECOA and Regulation B requirements to provide specific, accurate adverse action reasons. Regulators (CFPB) have increased scrutiny on "black box" models in lending. |
| **Affected Stakeholders** | Denied applicants, compliance team, legal counsel, CFPB, OCC |
| **Likelihood** | 3 |
| **Impact** | 5 |
| **Risk Score** | 15 (Critical) |
| **NIST AI RMF Mapping** | GOVERN 1.2, MAP 1.6, MEASURE 2.8, MANAGE 1.3 |
| **AI RMF Function** | GOVERN, MAP, MEASURE, MANAGE |

**Treatment Options:**
1. Adopt inherently interpretable models (logistic regression, scorecard models) or constrained gradient boosting with explainability layers
2. Implement SHAP (SHapley Additive exPlanations) or LIME to generate per-applicant factor contributions
3. Map model explanations to standard FCRA/Regulation B adverse action reason codes
4. Document the explanation methodology in the model card and model risk management policy
5. Train loan officers and customer service staff on how to communicate denial reasons clearly
6. Conduct quarterly testing to confirm adverse action notices are accurate and legally sufficient

**Residual Risk Owner:** Chief Compliance Officer
**Review Frequency:** Quarterly compliance review; real-time adverse action testing

---

### RISK-004: Training Data Quality and Representativeness

| Field | Detail |
|---|---|
| **Risk ID** | RISK-004 |
| **Risk Category** | Data Integrity / Representativeness |
| **Description** | Training data may contain historical errors, missing values for thin-file applicants, or underrepresentation of certain demographic groups or economic periods, causing the model to perform poorly for specific subpopulations or fail to generalize to new market conditions. |
| **Affected Stakeholders** | Data engineering team, model developers, applicants from underserved communities |
| **Likelihood** | 3 |
| **Impact** | 4 |
| **Risk Score** | 12 (High) |
| **NIST AI RMF Mapping** | MAP 2.1, MAP 2.2, MEASURE 1.3, MEASURE 2.3 |
| **AI RMF Function** | MAP, MEASURE |

**Treatment Options:**
1. Conduct a formal data quality assessment before each training cycle (completeness, consistency, accuracy, timeliness)
2. Document data lineage from source systems through to model inputs
3. Analyze training data demographic distribution and compare to intended deployment population
4. Supplement internal data with alternative data sources (with appropriate privacy and bias review) for thin-file applicants
5. Implement data validation pipelines that flag anomalies before data reaches the feature engineering layer
6. Retain data provenance records for regulatory examination readiness

**Residual Risk Owner:** Chief Data Officer / Data Governance Lead
**Review Frequency:** Per training cycle; quarterly data quality audit

---

### RISK-005: Model Misuse or Scope Creep

| Field | Detail |
|---|---|
| **Risk ID** | RISK-005 |
| **Risk Category** | Governance / Intended Use |
| **Description** | The credit scoring model may be applied to use cases beyond its validated scope (e.g., used for employment screening, insurance pricing, or marketing segmentation), exposing the firm to regulatory violations and reputational harm. |
| **Affected Stakeholders** | Business units, legal counsel, applicants, regulators |
| **Likelihood** | 2 |
| **Impact** | 5 |
| **Risk Score** | 10 (High) |
| **NIST AI RMF Mapping** | GOVERN 1.1, GOVERN 1.7, MAP 1.1, MAP 1.2, MANAGE 1.1 |
| **AI RMF Function** | GOVERN, MAP, MANAGE |

**Treatment Options:**
1. Publish a model use policy that explicitly defines approved use cases and prohibits others
2. Implement access controls restricting which systems and teams can call the model API
3. Require a formal change management process and re-validation before any new use case is approved
4. Conduct annual inventory of all downstream systems consuming model outputs
5. Include scope limitations in the model card and vendor contracts if the model is licensed externally
6. Train business stakeholders on appropriate model use during onboarding and annually

**Residual Risk Owner:** Model Risk Committee
**Review Frequency:** Annual use case inventory; triggered review on any new integration request

---

### RISK-006: Third-Party Vendor and Data Provider Risk

| Field | Detail |
|---|---|
| **Risk ID** | RISK-006 |
| **Risk Category** | Third-Party / Supply Chain Risk |
| **Description** | The model may rely on third-party credit bureau data, alternative data providers, or a vendor-built scoring engine. Vendor failures, data quality issues, changes in data availability, or vendor model updates could degrade performance or introduce compliance gaps without the firm's knowledge. |
| **Affected Stakeholders** | Vendor management team, model risk, procurement, compliance |
| **Likelihood** | 3 |
| **Impact** | 4 |
| **Risk Score** | 12 (High) |
| **NIST AI RMF Mapping** | GOVERN 1.6, MAP 1.3, MANAGE 2.4, MANAGE 4.1 |
| **AI RMF Function** | GOVERN, MAP, MANAGE |

**Treatment Options:**
1. Include contractual obligations for vendors to notify the firm of material changes to data or model components
2. Conduct third-party vendor due diligence assessments (including AI-specific risk questionnaires) at onboarding and annually
3. Establish SLAs covering data quality, uptime, and change notification windows
4. Maintain fallback scoring rules or a backup model for critical vendor outage scenarios
5. Require vendors to provide model documentation sufficient to support regulatory examination
6. Monitor vendor financial health and business continuity capabilities

**Residual Risk Owner:** Vendor Risk Management / Procurement
**Review Frequency:** Annual vendor review; triggered on material vendor changes

---

### RISK-007: Cybersecurity – Model Extraction and Adversarial Attacks

| Field | Detail |
|---|---|
| **Risk ID** | RISK-007 |
| **Risk Category** | Security / Adversarial Robustness |
| **Description** | Malicious actors could query the model systematically to reverse-engineer its logic (model extraction), or craft adversarial inputs designed to manipulate credit scores fraudulently (e.g., gaming income or employment fields to cross approval thresholds). |
| **Affected Stakeholders** | Cybersecurity team, fraud prevention, model risk, applicants |
| **Likelihood** | 2 |
| **Impact** | 4 |
| **Risk Score** | 8 (Medium) |
| **NIST AI RMF Mapping** | GOVERN 1.4, MEASURE 2.2, MANAGE 2.3, MANAGE 3.3 |
| **AI RMF Function** | GOVERN, MEASURE, MANAGE |

**Treatment Options:**
1. Implement rate limiting and anomaly detection on model API endpoints
2. Add query watermarking or noise injection to frustrate model extraction attempts
3. Conduct adversarial robustness testing as part of pre-deployment model validation
4. Monitor for unusual scoring patterns that may indicate score manipulation
5. Restrict direct model output to actionable decisions rather than raw score values where possible
6. Integrate model security considerations into the firm's broader cybersecurity incident response plan

**Residual Risk Owner:** Chief Information Security Officer (CISO)
**Review Frequency:** Quarterly security monitoring; annual penetration testing

---

### RISK-008: Privacy and Data Protection Compliance

| Field | Detail |
|---|---|
| **Risk ID** | RISK-008 |
| **Risk Category** | Privacy / Regulatory Compliance |
| **Description** | The collection, storage, and processing of personal financial data for model training and inference may violate GLBA, CCPA/CPRA, or state-level privacy laws. There is also risk of re-identification of applicants from model outputs or explanations. |
| **Affected Stakeholders** | Applicants, privacy officer, legal counsel, state regulators |
| **Likelihood** | 3 |
| **Impact** | 4 |
| **Risk Score** | 12 (High) |
| **NIST AI RMF Mapping** | GOVERN 1.3, MAP 1.5, MEASURE 2.10, MANAGE 1.4 |
| **AI RMF Function** | GOVERN, MAP, MEASURE, MANAGE |

**Treatment Options:**
1. Conduct a Privacy Impact Assessment (PIA) before model deployment and on each major update
2. Implement data minimization principles — use only the personal data fields strictly necessary for scoring
3. Ensure applicant consent and privacy notices address use of data in automated decision-making
4. Apply differential privacy or data anonymization techniques for model training datasets
5. Establish data retention and deletion policies aligned with GLBA and applicable state law
6. Document the legal basis for processing under each applicable privacy framework

**Residual Risk Owner:** Chief Privacy Officer
**Review Frequency:** Annual PIA refresh; triggered by regulatory changes

---

### RISK-009: Human Oversight Failures in Automated Decisions

| Field | Detail |
|---|---|
| **Risk ID** | RISK-009 |
| **Risk Category** | Human Oversight / Accountability |
| **Description** | Over-reliance on automated credit decisions without adequate human review processes may result in systemic errors going undetected, disproportionate impacts on vulnerable applicants, and reduced organizational ability to override incorrect decisions in a timely manner. |
| **Affected Stakeholders** | Credit analysts, applicants, compliance team, senior management |
| **Likelihood** | 3 |
| **Impact** | 4 |
| **Risk Score** | 12 (High) |
| **NIST AI RMF Mapping** | GOVERN 1.5, GOVERN 2.1, MANAGE 1.2, MANAGE 2.1 |
| **AI RMF Function** | GOVERN, MANAGE |

**Treatment Options:**
1. Define and document which decision types require mandatory human review (e.g., border-line scores, high-value loans, re-applications after denial)
2. Implement an override workflow with audit logging for all human interventions
3. Set escalation protocols for applicants who request reconsideration of automated decisions
4. Train underwriters to critically evaluate, rather than simply ratify, model recommendations
5. Track override rates and outcomes to identify systematic model errors
6. Include human oversight adequacy in model governance committee reporting

**Residual Risk Owner:** Head of Credit / Model Risk Committee
**Review Frequency:** Monthly override rate reporting; quarterly governance review

---

### RISK-010: Regulatory Change and Emerging AI Legislation

| Field | Detail |
|---|---|
| **Risk ID** | RISK-010 |
| **Risk Category** | Regulatory / Legal Compliance |
| **Description** | The regulatory landscape for AI in financial services is evolving rapidly (CFPB guidance on AI in lending, OCC model risk management guidance SR 11-7, potential federal AI Act equivalents, state AI laws). Changes could require significant model redesign, documentation upgrades, or operational changes on short timescales. |
| **Affected Stakeholders** | Legal counsel, compliance team, model risk, executive leadership |
| **Likelihood** | 4 |
| **Impact** | 3 |
| **Risk Score** | 12 (High) |
| **NIST AI RMF Mapping** | GOVERN 1.1, GOVERN 1.7, MAP 1.4, MANAGE 4.2 |
| **AI RMF Function** | GOVERN, MAP, MANAGE |

**Treatment Options:**
1. Assign a regulatory horizon-scanning function to track AI-relevant rulemaking (CFPB, OCC, FRB, FDIC, FTC, state regulators)
2. Maintain a model documentation library that can be rapidly updated to meet new disclosure requirements
3. Engage proactively with industry associations (e.g., ABA, FSB) to anticipate regulatory direction
4. Build modularity into the model architecture to facilitate targeted updates without full redeployment
5. Conduct a regulatory impact assessment whenever a new AI rule or guidance is finalized
6. Include regulatory change risk as a standing agenda item on the Model Risk Committee

**Residual Risk Owner:** Chief Compliance Officer
**Review Frequency:** Ongoing horizon scanning; quarterly regulatory update briefings

---

## Risk Summary Matrix

| Risk ID | Risk Title | Likelihood | Impact | Score | Rating | AI RMF Functions | Primary Owner |
|---|---|---|---|---|---|---|---|
| RISK-001 | Algorithmic Bias / Discrimination | 4 | 5 | 20 | Critical | MAP, MEASURE, MANAGE | Chief Risk Officer |
| RISK-002 | Model Performance Degradation | 4 | 4 | 16 | Critical | MEASURE, MANAGE | Model Risk Lead |
| RISK-003 | Explainability / Adverse Action | 3 | 5 | 15 | Critical | GOVERN, MAP, MEASURE, MANAGE | Chief Compliance Officer |
| RISK-004 | Training Data Quality | 3 | 4 | 12 | High | MAP, MEASURE | Chief Data Officer |
| RISK-005 | Model Misuse / Scope Creep | 2 | 5 | 10 | High | GOVERN, MAP, MANAGE | Model Risk Committee |
| RISK-006 | Third-Party / Vendor Risk | 3 | 4 | 12 | High | GOVERN, MAP, MANAGE | Vendor Risk Management |
| RISK-007 | Cybersecurity / Adversarial Attacks | 2 | 4 | 8 | Medium | GOVERN, MEASURE, MANAGE | CISO |
| RISK-008 | Privacy / Data Protection | 3 | 4 | 12 | High | GOVERN, MAP, MEASURE, MANAGE | Chief Privacy Officer |
| RISK-009 | Human Oversight Failures | 3 | 4 | 12 | High | GOVERN, MANAGE | Head of Credit |
| RISK-010 | Regulatory Change | 4 | 3 | 12 | High | GOVERN, MAP, MANAGE | Chief Compliance Officer |

---

## NIST AI RMF Function Coverage Summary

| AI RMF Function | Risks Covered | Key Focus Areas |
|---|---|---|
| **GOVERN** | RISK-003, RISK-005, RISK-006, RISK-007, RISK-008, RISK-009, RISK-010 | Policies, accountability structures, oversight mechanisms, organizational culture |
| **MAP** | RISK-001, RISK-004, RISK-005, RISK-006, RISK-008, RISK-010 | Risk context, categorization, stakeholder identification, intended use |
| **MEASURE** | RISK-001, RISK-002, RISK-003, RISK-004, RISK-007, RISK-008 | Performance monitoring, bias measurement, explainability assessment |
| **MANAGE** | RISK-001, RISK-002, RISK-003, RISK-005, RISK-006, RISK-007, RISK-008, RISK-009, RISK-010 | Treatment plans, response protocols, residual risk monitoring |

---

## Key Regulatory References

| Regulation / Guidance | Relevance to Credit Scoring AI |
|---|---|
| Equal Credit Opportunity Act (ECOA) / Regulation B | Adverse action notices, prohibited basis discrimination |
| Fair Credit Reporting Act (FCRA) | Use of consumer report data, dispute rights |
| Fair Housing Act (FHA) | Discrimination in mortgage lending |
| CFPB Circular 2022-03 | Fair lending and algorithmic underwriting |
| OCC SR 11-7 / OCC 2011-12 | Model risk management guidance |
| Gramm-Leach-Bliley Act (GLBA) | Financial data privacy obligations |
| CCPA / CPRA | California consumer privacy rights in automated decisions |
| NIST AI RMF 1.0 (2023) | AI risk management lifecycle framework |
| ISO/IEC 42001:2023 | AI management system standard |

---

## Register Maintenance

| Activity | Frequency | Responsible Party |
|---|---|---|
| Risk score review and update | Quarterly | Model Risk Committee |
| Treatment effectiveness assessment | Quarterly | Risk Owners |
| New risk identification | Ongoing / triggered by events | All stakeholders |
| Full register refresh | Annual | Chief Risk Officer |
| Regulatory landscape review | Quarterly | Chief Compliance Officer |
| Executive risk reporting | Monthly (summary) | Model Risk Committee Chair |

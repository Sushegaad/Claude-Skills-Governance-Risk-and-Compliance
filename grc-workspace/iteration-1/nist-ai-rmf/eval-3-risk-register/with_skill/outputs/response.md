# AI Risk Register — Credit Scoring Model
## Financial Services Firm | NIST AI RMF 1.0 Aligned
**Date:** 2026-04-25
**System:** Automated Credit Scoring Model
**Lifecycle Stage:** Design through Post-Deployment
**Regulatory Context:** ECOA, Fair Housing Act, CFPB guidance, EU AI Act (High-Risk: Credit Scoring), FCRA

---

## How to Use This Register

Each entry captures:
- **Risk ID** — Unique identifier in format CS-[number]
- **Risk Description** — Plain-language description of the risk
- **Trustworthiness Property** — Which of the NIST AI RMF trustworthiness characteristics is at risk
- **AI RMF Categories** — Specific function + category references (e.g., MAP 5.1, MEASURE 2.2)
- **Likelihood** — Estimated probability: Low / Medium / High
- **Impact** — Severity of harm if the risk materialises: Low / Medium / High / Critical
- **Risk Rating** — Combined priority: Low / Medium / High / Critical
- **Treatment Options** — Specific, actionable treatments aligned to MANAGE function
- **Treatment Owner** — Recommended accountable role
- **Review Frequency** — How often this entry should be reassessed

---

## Risk Register

### CS-001 — Algorithmic Bias and Discriminatory Credit Decisions

| Field | Detail |
|-------|--------|
| **Risk Description** | The credit scoring model produces systematically lower scores for applicants from protected demographic groups (race, ethnicity, sex, national origin, age, marital status), resulting in unlawful disparate impact in credit access and terms. |
| **Trustworthiness Property** | Fair / Bias Managed |
| **AI RMF Categories** | MAP 3.3, MAP 5.2, MAP 5.3, MEASURE 2.2, MEASURE 3.1, MG-1.1, MG-2.1 |
| **Likelihood** | High |
| **Impact** | Critical |
| **Risk Rating** | Critical |
| **Regulatory Exposure** | ECOA (15 U.S.C. § 1691), Fair Housing Act, CFPB Examination Procedures, EU AI Act Art. 10 (High-Risk Data Governance) |

**Treatment Options:**

1. **Mitigate — Pre-deployment fairness testing:** Run disaggregated performance analysis across all ECOA-protected classes before deployment. Apply metrics: Demographic Parity, Equalized Odds, Disparate Impact Ratio (maintain ≥0.8 per EEOC 4/5ths rule). Document results in a model card (MEASURE 2.2, MEASURE 2.6).
2. **Mitigate — Bias-aware retraining:** If disparate impact is detected, apply fairness-aware ML techniques (reweighing, adversarial debiasing, or calibrated equalized odds post-processing) and retrain. Validate results before deployment (MANAGE 2.2).
3. **Mitigate — Ongoing monitoring:** Implement a production monitoring dashboard tracking fairness metrics monthly. Set alert thresholds: e.g., if Disparate Impact Ratio drops below 0.85 for any protected group, trigger mandatory review (MEASURE 3.1, MEASURE 3.2).
4. **Transfer — Third-party fairness audit:** Engage an independent third-party auditor annually to conduct a disparate impact analysis across all credit decisions (MANAGE 4.1).
5. **Accept residual risk with controls:** Document accepted residual risk with senior leadership sign-off and a defined remediation timeline (MG-1.3).

| **Treatment Owner** | Chief Risk Officer + Model Risk Management Team |
| **Review Frequency** | Monthly monitoring; Full assessment at each model version update |

---

### CS-002 — Lack of Explainability and Adverse Action Notice Failures

| Field | Detail |
|-------|--------|
| **Risk Description** | The model generates credit decisions that cannot be explained in terms understandable to applicants or regulators, making it impossible to provide legally required adverse action notices specifying the principal reasons for denial. |
| **Trustworthiness Property** | Explainable and Interpretable |
| **AI RMF Categories** | MAP 1.2, MAP 1.5, MEASURE 2.3, MEASURE 2.6, MG-2.1, GV-6.1 |
| **Likelihood** | High |
| **Impact** | Critical |
| **Risk Rating** | Critical |
| **Regulatory Exposure** | ECOA Regulation B (12 C.F.R. § 202.9) — adverse action notice requirements; FCRA § 615; EU AI Act Art. 13 (Transparency) |

**Treatment Options:**

1. **Mitigate — Implement model explainability layer:** Deploy SHAP (SHapley Additive exPlanations) or LIME to generate feature-level explanations for every individual credit decision. Map SHAP values to the top four principal reasons for each denial (MEASURE 2.3).
2. **Mitigate — Adverse action notice workflow:** Build an automated pipeline that translates model explanations into plain-language adverse action notices meeting Regulation B requirements. Test notices for comprehensibility with representative consumer groups (MG-2.2).
3. **Mitigate — Model card publication:** Produce and maintain a model card documenting model purpose, inputs, outputs, training data characteristics, performance metrics, known limitations, and intended use boundaries. Update at each version release (MAP 2.1, MEASURE 2.6).
4. **Avoid:** If the chosen model architecture (e.g., deep neural network) cannot produce legally defensible explanations, consider switching to an inherently interpretable model (e.g., logistic regression, gradient boosted trees with SHAP) or a hybrid approach with an explainable layer (MG-2.1).

| **Treatment Owner** | Head of Model Risk + Legal/Compliance |
| **Review Frequency** | Pre-deployment testing; Post-deployment quarterly review of adverse action notice accuracy |

---

### CS-003 — Training Data Quality and Historical Bias

| Field | Detail |
|-------|--------|
| **Risk Description** | Training data reflects historical lending patterns that embedded discriminatory practices. Proxy variables (e.g., ZIP code, purchase history) may correlate with protected characteristics. Data quality issues (missing values, stale data, unrepresentative samples) degrade model accuracy. |
| **Trustworthiness Property** | Valid and Verified; Fair / Bias Managed |
| **AI RMF Categories** | MAP 2.2, MAP 2.3, MAP 5.1, MEASURE 1.1, MEASURE 2.1, MEASURE 2.2 |
| **Likelihood** | High |
| **Impact** | High |
| **Risk Rating** | High |
| **Regulatory Exposure** | EU AI Act Art. 10 (Data Governance); CFPB UDAAP guidance on proxy discrimination |

**Treatment Options:**

1. **Mitigate — Data provenance documentation:** Document all training data sources, collection periods, known gaps, and representativeness of the training population relative to the intended deployment population (MAP 2.2).
2. **Mitigate — Proxy variable analysis:** Conduct correlation analysis between all model input features and protected characteristics. Identify and evaluate proxy variables; apply suppression or transformation where proxies create unlawful disparate impact (MAP 5.1, MEASURE 2.2).
3. **Mitigate — Data quality gates:** Implement pre-training data quality checks: completeness thresholds, staleness limits, and demographic representativeness validation. Reject or flag training datasets that fail these gates (MEASURE 1.1).
4. **Mitigate — Synthetic data augmentation:** Where under-represented groups appear in training data, augment with validated synthetic data to improve model performance across all demographic groups (MG-2.2).
5. **Mitigate — Ongoing data drift monitoring:** Monitor production input data distributions using Population Stability Index (PSI) and Kolmogorov-Smirnov tests. Trigger model retraining when significant drift is detected (MEASURE 3.2).

| **Treatment Owner** | Data Engineering Lead + Model Risk Management |
| **Review Frequency** | Pre-training data validation; Quarterly production data drift review |

---

### CS-004 — Model Performance Degradation and Drift

| Field | Detail |
|-------|--------|
| **Risk Description** | Model accuracy and fairness metrics degrade over time as economic conditions, consumer behaviour, and credit markets evolve, causing the model to make systematically worse or unfair decisions without detection. |
| **Trustworthiness Property** | Reliable; Valid and Verified |
| **AI RMF Categories** | MEASURE 3.1, MEASURE 3.2, MEASURE 3.3, MEASURE 4.1, MG-3.1, MG-3.2 |
| **Likelihood** | High |
| **Impact** | High |
| **Risk Rating** | High |
| **Regulatory Exposure** | SR 11-7 (Model Risk Management — Federal Reserve / OCC); CFPB supervisory expectations |

**Treatment Options:**

1. **Mitigate — Automated monitoring dashboard:** Implement a real-time model performance dashboard tracking: AUC-ROC, Gini coefficient, KS statistic, default rate accuracy, and disaggregated fairness metrics. Set alert thresholds triggering mandatory human review (MEASURE 3.1).
2. **Mitigate — Champion-challenger framework:** Run the production model (champion) alongside a retrained challenger model. Automatically promote the challenger when it outperforms the champion on validated test sets (MG-3.1).
3. **Mitigate — Periodic recalibration schedule:** Establish a defined model recalibration cadence (minimum semi-annual for credit models). Require full revalidation before redeployment (MEASURE 3.2, MG-2.2).
4. **Mitigate — Model owner accountability:** Designate a named model owner responsible for monthly monitoring review sign-off and escalation to the Model Risk Committee when thresholds are breached (GV-2.1, MG-3.1).
5. **Mitigate — Defined kill switch procedure:** Document an emergency model rollback procedure specifying: trigger conditions, authorization chain, fallback scoring method, and customer communication protocol (MG-2.3).

| **Treatment Owner** | Model Risk Management + CRO |
| **Review Frequency** | Monthly automated; Formal review semi-annually or upon threshold breach |

---

### CS-005 — Privacy Violations and Unauthorized Use of Personal Data

| Field | Detail |
|-------|--------|
| **Risk Description** | The model processes sensitive personal financial data. Risks include: use of data beyond consented purposes, re-identification of applicants from model outputs, membership inference attacks revealing whether an individual's data was in training sets, and insufficient data minimization. |
| **Trustworthiness Property** | Privacy-Enhanced |
| **AI RMF Categories** | MAP 1.4, MAP 1.6, MEASURE 2.4, MG-2.1, GV-6.1 |
| **Likelihood** | Medium |
| **Impact** | High |
| **Risk Rating** | High |
| **Regulatory Exposure** | GLBA (Gramm-Leach-Bliley Act), FCRA, CCPA/CPRA (California), GDPR (if EU applicants), EU AI Act Art. 10 |

**Treatment Options:**

1. **Mitigate — Data minimization review:** Audit all model input features against a data minimization standard. Remove features not demonstrably necessary for predictive performance and lawfully collected for this purpose (MAP 1.6, MEASURE 2.4).
2. **Mitigate — Purpose limitation controls:** Implement technical controls ensuring training and inference data cannot be used beyond the stated credit scoring purpose. Document purpose limitation in the model card and data processing agreements (GV-6.1).
3. **Mitigate — Membership inference attack testing:** Conduct membership inference attack simulations to assess whether model outputs could reveal whether specific individuals were in the training data. Apply differential privacy or output perturbation if risk is high (MEASURE 2.4).
4. **Mitigate — Privacy Impact Assessment (PIA):** Conduct a formal PIA before deployment and update it at each major model version change (MAP 1.4, GV-6.2).
5. **Transfer — Contractual controls for third-party data:** Ensure all third-party data suppliers have executed Data Processing Agreements with appropriate restrictions and audit rights (GV-6.1).

| **Treatment Owner** | Chief Privacy Officer + Legal |
| **Review Frequency** | PIA prior to deployment; Annual review; Upon any new data source addition |

---

### CS-006 — Adversarial Manipulation and Model Security

| Field | Detail |
|-------|--------|
| **Risk Description** | Malicious actors could manipulate the credit scoring model through: (1) evasion attacks — crafting loan applications designed to fool the model into approving fraudulent applicants; (2) poisoning attacks — corrupting training data to degrade model behaviour; (3) model extraction — reverse-engineering the scoring model through API queries. |
| **Trustworthiness Property** | Secure and Cyber-Resilient; Resilient |
| **AI RMF Categories** | MAP 5.1, MEASURE 2.4, MEASURE 1.2, MG-2.1, MG-2.3, GV-4.1 |
| **Likelihood** | Medium |
| **Impact** | High |
| **Risk Rating** | High |
| **Regulatory Exposure** | FFIEC Cybersecurity Assessment Tool; GLBA Safeguards Rule; NIST CSF 2.0 |

**Treatment Options:**

1. **Mitigate — Adversarial robustness testing:** Conduct pre-deployment adversarial testing simulating evasion attacks (crafted loan applications) on the model. Measure adversarial accuracy and define an acceptable threshold (MEASURE 2.4).
2. **Mitigate — Training data integrity controls:** Implement data provenance tracking, anomaly detection on training data pipelines, and access controls to prevent unauthorized data injection (poisoning) (MEASURE 1.2).
3. **Mitigate — Rate limiting and query monitoring on scoring API:** Implement API rate limiting, anomaly detection on query patterns, and output perturbation to defend against model extraction attacks. Log and alert on unusual query patterns (MG-2.1).
4. **Mitigate — Model versioning and integrity verification:** Cryptographically sign model artifacts and verify integrity before deployment. Detect unauthorized modifications to model files (MG-2.3).
5. **Mitigate — Red team exercise:** Conduct an annual red team exercise targeting the credit scoring pipeline, including adversarial ML and traditional cybersecurity attack vectors. Feed findings back to MAP and MEASURE (MAP 5.1, MG-4.2).

| **Treatment Owner** | CISO + Model Risk Management |
| **Review Frequency** | Pre-deployment security testing; Annual red team; Continuous API monitoring |

---

### CS-007 — Insufficient Human Oversight and Automation Bias

| Field | Detail |
|-------|--------|
| **Risk Description** | Over-reliance on automated credit decisions without meaningful human review creates risks of unchallenged model errors, inability to exercise discretion for legitimate edge cases, and failure to detect emerging harms. Loan officers may accept model outputs without independent judgment (automation bias). |
| **Trustworthiness Property** | Accountable and Transparent; Safe |
| **AI RMF Categories** | MAP 1.2, MEASURE 2.5, MG-2.2, GV-2.1, GV-3.2 |
| **Likelihood** | Medium |
| **Impact** | High |
| **Risk Rating** | High |
| **Regulatory Exposure** | CFPB guidance on automated decision-making; EU AI Act Art. 14 (Human Oversight for High-Risk AI) |

**Treatment Options:**

1. **Mitigate — Tiered human review policy:** Define clear criteria for mandatory human review: all near-threshold decisions (scores within a defined band of the cut-off), all applications from demographic groups showing elevated error rates, and all appeals (MEASURE 2.5, MG-2.2).
2. **Mitigate — Loan officer training on AI limitations:** Conduct mandatory training for all staff using model outputs, covering: what the model can and cannot do, known limitations, how to identify anomalous outputs, and how to escalate concerns (GV-3.2).
3. **Mitigate — Mandatory override logging:** Require documentation of all human overrides of model recommendations, including reasons. Analyze override patterns to identify model weaknesses (MEASURE 3.3, MG-4.2).
4. **Mitigate — Appeals and reconsideration process:** Implement a formal applicant appeal process with human review of challenged decisions. Document appeal outcomes and feed insights back into model monitoring (MAP 3.4).
5. **Avoid for high-impact decisions:** Define categories of decision (e.g., large commercial loans above a threshold) that require human decision authority and cannot be fully automated (MAP 1.2, GV-5.3).

| **Treatment Owner** | Head of Credit Risk + Operations |
| **Review Frequency** | Semi-annual training refresh; Quarterly override pattern review |

---

### CS-008 — Regulatory Non-Compliance and Governance Gaps

| Field | Detail |
|-------|--------|
| **Risk Description** | Failure to maintain policies, accountability structures, and documentation meeting regulatory expectations for model risk management (SR 11-7), consumer protection (ECOA, FCRA), and AI-specific regulations (EU AI Act). Gaps in governance may result in regulatory enforcement, fines, or required model suspension. |
| **Trustworthiness Property** | Accountable and Transparent |
| **AI RMF Categories** | GV-1.1, GV-1.6, GV-2.2, GV-6.1, GV-6.3, MAP 1.6, MG-4.1 |
| **Likelihood** | Medium |
| **Impact** | Critical |
| **Risk Rating** | High |
| **Regulatory Exposure** | SR 11-7 (Model Risk Management); ECOA; FCRA; EU AI Act Annex IX (Technical Documentation); CFPB |

**Treatment Options:**

1. **Mitigate — Regulatory register:** Maintain a live register of all applicable AI-relevant regulations and their requirements. Assign owners to each regulatory requirement and track compliance status (GV-6.1).
2. **Mitigate — Model inventory and documentation:** Maintain a complete model inventory including: model purpose, version, owner, validation status, last review date, and regulatory classification. Ensure EU AI Act Annex IX technical documentation is maintained for the credit scoring system (GV-1.1, MG-4.1).
3. **Mitigate — AI governance committee:** Establish a formal AI Governance Committee with cross-functional representation (legal, compliance, model risk, data, technology, business). Hold quarterly reviews covering all deployed AI models (GV-4.1, GV-2.2).
4. **Mitigate — Annual compliance assessment:** Conduct an annual assessment of credit scoring model compliance against SR 11-7, ECOA, FCRA, and applicable AI regulations. Engage external counsel or third-party assessor for independent validation (MG-4.1).
5. **Mitigate — Regulatory horizon scanning:** Assign a legal/compliance team member to monitor emerging AI regulations (EU AI Act implementation acts, CFPB guidance updates, state AI laws) and proactively update governance practices (GV-6.3).

| **Treatment Owner** | Chief Compliance Officer + General Counsel |
| **Review Frequency** | Annual formal assessment; Quarterly committee review; Ongoing regulatory monitoring |

---

### CS-009 — Third-Party Model and Data Provider Risk

| Field | Detail |
|-------|--------|
| **Risk Description** | If the credit scoring model is sourced from a third-party vendor, or relies on external data providers (credit bureaus, alternative data), the firm may have limited visibility into model internals, training data, bias testing, and update processes, creating accountability gaps. |
| **Trustworthiness Property** | Accountable and Transparent; Valid and Verified |
| **AI RMF Categories** | GV-3.3, GV-6.1, MAP 1.3, MAP 2.1, MAP 2.2, MEASURE 2.1, MG-2.1 |
| **Likelihood** | Medium |
| **Impact** | High |
| **Risk Rating** | High |
| **Regulatory Exposure** | SR 11-7 (third-party model validation obligations); OCC Guidance on Third-Party Relationships; CFPB |

**Treatment Options:**

1. **Mitigate — Vendor due diligence:** Require third-party AI vendors to provide model cards, bias testing results, validation reports, and change notification procedures before contract execution (MAP 2.1, MAP 2.2).
2. **Mitigate — Contractual rights:** Negotiate contractual rights to: audit vendor model performance, receive timely notification of model changes, access training data documentation, and conduct independent validation (GV-3.3).
3. **Mitigate — Independent validation:** Conduct independent validation of third-party models per SR 11-7 requirements, regardless of vendor-provided documentation. Include fairness testing on firm-specific applicant population (MEASURE 2.1).
4. **Mitigate — Data provider quality controls:** For each external data source, document data quality requirements, validate completeness and accuracy upon each refresh, and assess demographic representativeness (MAP 2.2, MEASURE 1.1).
5. **Transfer — Contractual indemnification:** Negotiate indemnification clauses covering regulatory fines arising from vendor model defects. Obtain evidence of the vendor's own AI risk management programme (MG-2.1).

| **Treatment Owner** | Third-Party Risk Management + Model Risk |
| **Review Frequency** | Due diligence at onboarding; Annual vendor review; Upon each model update notification |

---

### CS-010 — Model Incident Response Gaps

| Field | Detail |
|-------|--------|
| **Risk Description** | Absence of a defined AI incident response plan means that when model failures occur (bias breach, accuracy degradation, adversarial attack, or regulatory finding), the firm lacks a structured process to contain harm, notify affected parties, remediate the model, and document lessons learned. |
| **Trustworthiness Property** | Resilient; Accountable and Transparent |
| **AI RMF Categories** | MG-3.2, MG-3.3, MG-3.4, MG-4.2, GV-4.3, MEASURE 4.1 |
| **Likelihood** | Medium |
| **Impact** | High |
| **Risk Rating** | High |
| **Regulatory Exposure** | SR 11-7; CFPB supervisory expectations; EU AI Act Art. 73 (Serious Incident Reporting) |

**Treatment Options:**

1. **Mitigate — AI incident response plan:** Develop and document a credit scoring model incident response plan covering: (1) Trigger conditions, (2) Contain — suspend or restrict model use, (3) Assess impact — scope of affected applicants, (4) Notify — internal escalation chain, regulatory notification thresholds, customer notification requirements, (5) Remediate — model fix or rollback procedure, (6) Document — incident log and root cause analysis, (7) Update risk register (MG-3.2).
2. **Mitigate — Incident severity classification:** Define incident severity tiers (Low / Medium / High / Critical) with mapped response timelines and authorization levels for each tier (MG-3.2, GV-4.3).
3. **Mitigate — Tabletop exercises:** Conduct annual tabletop exercises simulating a credit scoring model incident (e.g., bias threshold breach discovery or regulatory inquiry). Identify gaps in the response plan and update accordingly (MG-4.2).
4. **Mitigate — Affected applicant remediation process:** Define a process for identifying and remedying harm to applicants affected by model failures, including reconsideration of denied applications (MG-3.4).
5. **Mitigate — Lessons learned loop:** After every incident or near-miss, conduct a post-incident review and feed findings back into GOVERN policies, MAP risk assessments, and MEASURE monitoring thresholds (MG-3.3, MG-4.3).

| **Treatment Owner** | CRO + Head of Model Risk + Compliance |
| **Review Frequency** | Incident plan: Annual review + after every incident; Tabletop: Annual |

---

## Risk Register Summary

| Risk ID | Risk Title | Likelihood | Impact | Risk Rating | Primary AI RMF Categories | Trustworthiness Property |
|---------|-----------|------------|--------|-------------|--------------------------|--------------------------|
| CS-001 | Algorithmic Bias and Discriminatory Decisions | High | Critical | **Critical** | MAP 3.3, MAP 5.2, MEASURE 2.2, MEASURE 3.1, MG-1.1 | Fair / Bias Managed |
| CS-002 | Explainability and Adverse Action Notice Failures | High | Critical | **Critical** | MAP 1.5, MEASURE 2.3, MEASURE 2.6, MG-2.1, GV-6.1 | Explainable and Interpretable |
| CS-003 | Training Data Quality and Historical Bias | High | High | **High** | MAP 2.2, MAP 5.1, MEASURE 1.1, MEASURE 2.2 | Valid and Verified; Fair |
| CS-004 | Model Performance Degradation and Drift | High | High | **High** | MEASURE 3.1, MEASURE 3.2, MEASURE 4.1, MG-3.1 | Reliable; Valid and Verified |
| CS-005 | Privacy Violations and Unauthorized Data Use | Medium | High | **High** | MAP 1.4, MAP 1.6, MEASURE 2.4, GV-6.1 | Privacy-Enhanced |
| CS-006 | Adversarial Manipulation and Model Security | Medium | High | **High** | MAP 5.1, MEASURE 2.4, MG-2.1, MG-2.3 | Secure and Cyber-Resilient |
| CS-007 | Insufficient Human Oversight and Automation Bias | Medium | High | **High** | MAP 1.2, MEASURE 2.5, MG-2.2, GV-3.2 | Accountable and Transparent |
| CS-008 | Regulatory Non-Compliance and Governance Gaps | Medium | Critical | **High** | GV-1.1, GV-1.6, GV-2.2, GV-6.1, MG-4.1 | Accountable and Transparent |
| CS-009 | Third-Party Model and Data Provider Risk | Medium | High | **High** | GV-3.3, MAP 2.1, MAP 2.2, MEASURE 2.1 | Accountable and Transparent |
| CS-010 | Model Incident Response Gaps | Medium | High | **High** | MG-3.2, MG-3.3, MG-4.2, GV-4.3 | Resilient |

---

## AI RMF Coverage Map

The following table shows which AI RMF categories are addressed by this risk register:

| AI RMF Function | Categories Addressed | Coverage |
|----------------|---------------------|----------|
| **GOVERN** | GV-1.1, GV-1.6, GV-2.1, GV-2.2, GV-3.2, GV-3.3, GV-4.1, GV-4.3, GV-5.3, GV-6.1, GV-6.3 | Comprehensive |
| **MAP** | MAP 1.2, MAP 1.3, MAP 1.4, MAP 1.5, MAP 1.6, MAP 2.1, MAP 2.2, MAP 2.3, MAP 3.3, MAP 3.4, MAP 5.1, MAP 5.2, MAP 5.3 | Comprehensive |
| **MEASURE** | MEASURE 1.1, MEASURE 1.2, MEASURE 2.1, MEASURE 2.2, MEASURE 2.3, MEASURE 2.4, MEASURE 2.5, MEASURE 2.6, MEASURE 3.1, MEASURE 3.2, MEASURE 3.3, MEASURE 4.1 | Comprehensive |
| **MANAGE** | MG-1.1, MG-1.3, MG-2.1, MG-2.2, MG-2.3, MG-3.1, MG-3.2, MG-3.3, MG-3.4, MG-4.1, MG-4.2, MG-4.3 | Comprehensive |

---

## Prioritised Treatment Roadmap

### Immediate Actions (Before Deployment)
1. **CS-001:** Complete disaggregated bias testing across all ECOA-protected classes. Halt deployment if Disparate Impact Ratio falls below 0.80 for any group.
2. **CS-002:** Implement SHAP explainability layer and validate adverse action notice generation against Regulation B requirements.
3. **CS-003:** Complete data provenance documentation and proxy variable analysis. Remediate any identified proxy discrimination pathways.
4. **CS-008:** Confirm AI Governance Committee is constituted and model has passed formal pre-deployment review.

### Near-Term Actions (First 90 Days Post-Deployment)
5. **CS-004:** Activate production monitoring dashboard with defined alert thresholds. Assign named model owner.
6. **CS-006:** Deploy API rate limiting and query anomaly detection on the scoring endpoint.
7. **CS-007:** Deliver loan officer training on model limitations and override logging procedures.
8. **CS-010:** Finalize and table-test the AI incident response plan.

### Ongoing Actions (Quarterly / Annual Cycle)
9. **CS-005:** Conduct annual Privacy Impact Assessment update.
10. **CS-009:** Schedule annual third-party vendor review and independent model validation.
11. **CS-004:** Semi-annual model recalibration review.
12. All entries: Annual risk register review and residual risk acceptance sign-off by senior leadership.

---

## Notes for Implementation

**SR 11-7 Alignment:** This risk register supports compliance with the Federal Reserve/OCC Model Risk Management guidance (SR 11-7). Risks CS-002 (validation documentation), CS-003 (data documentation), CS-004 (ongoing monitoring), and CS-009 (third-party validation) directly address SR 11-7 core requirements.

**EU AI Act Classification:** Automated credit scoring is classified as a **high-risk AI system** under EU AI Act Annex III. All entries in this register support compliance with the mandatory requirements in Arts. 9–15 of the Act. Organizations subject to the EU AI Act should treat all "Critical" and "High" rated risks as mandatory remediation items, not optional treatments.

**Implementation Tier Target:** Organizations deploying this model should target NIST AI RMF Implementation Tier 3 (Repeatable) at a minimum, with a roadmap toward Tier 4 (Adaptive) for ongoing bias monitoring and incident learning loops.

**Register Maintenance:** This register should be reviewed:
- Before each model version deployment
- When regulatory requirements change
- Following any model incident or near-miss
- Annually at minimum, with formal senior leadership sign-off on residual risks

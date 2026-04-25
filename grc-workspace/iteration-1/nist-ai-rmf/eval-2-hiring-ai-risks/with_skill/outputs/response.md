# NIST AI RMF Assessment: AI Hiring Tool (Resume Screening and Candidate Ranking)

---

## Context

An AI hiring tool that screens resumes and ranks candidates is classified as **high-risk** under the NIST AI RMF and the EU AI Act (Annex III — employment, workers management, and access to self-employment). Decisions made by this system directly affect individuals' livelihoods, triggering heightened obligations across all four RMF functions. This assessment focuses on key risks, the most relevant trustworthiness properties, and the specific MEASURE 2.x pre-deployment actions required before the system goes live.

---

## 1. Key Risks to Assess (MAP Function)

The following risks should be documented and prioritized as part of the MAP function before measurement begins.

### Risk Register Summary

| Risk ID | Risk Description | Trustworthiness Property at Risk | Likelihood | Impact | Priority |
|---------|-----------------|----------------------------------|------------|--------|----------|
| HR-001 | Model perpetuates historical hiring biases encoded in training data (e.g., penalizes resume gaps, non-traditional career paths disproportionately affecting women, caregivers, or minorities) | Fair / Bias Managed | High | Critical | P1 |
| HR-002 | Disparate impact on protected classes (race, gender, age, disability, national origin) violating EEOC and Title VII standards — failure to meet the 4/5ths (80%) disparate impact ratio rule | Fair / Bias Managed | High | Critical | P1 |
| HR-003 | Ranking criteria not explainable to recruiters or rejected candidates — inability to provide meaningful adverse action notice | Explainable & Interpretable | High | High | P1 |
| HR-004 | Proxy variable use: model learns protected attributes indirectly through correlated features (e.g., zip code → race, graduation year → age, names → gender or ethnicity) | Fair / Bias Managed | High | Critical | P1 |
| HR-005 | Training data reflecting historical over/under-representation of certain groups, leading to skewed ranking scores | Valid & Verified | High | High | P1 |
| HR-006 | Model performance degrades over time as job market, role requirements, or applicant pool demographics shift (model drift) | Reliable | Medium | High | P2 |
| HR-007 | Lack of human oversight — recruiters over-rely on AI rankings without independent review, removing meaningful human decision-making | Accountable & Transparent | Medium | High | P2 |
| HR-008 | PII exposure: resumes contain sensitive personal data (address, phone, employment history); inadequate data minimization or access controls | Privacy-Enhanced | Medium | High | P2 |
| HR-009 | Candidates gaming or manipulating the system by crafting resumes specifically to exploit model patterns (adversarial inputs) | Resilient / Secure | Low | Medium | P3 |
| HR-010 | Societal aggregate effect: widespread deployment of biased hiring AI systematically narrows workforce diversity across the labor market | Safe (societal harm) | Medium | Critical | P1 |

### Key Contextual Factors (MAP 1.x)

- **Intended use boundary (MP-1.2):** The system should be scoped explicitly — screening only, ranking only, or making final cut decisions? Autonomous final decisions represent the highest risk profile.
- **Affected populations (MP-1.4):** All job applicants, with heightened attention to groups historically underrepresented in the organization's workforce.
- **Prohibited uses (MP-1.5):** Document explicitly that the system may not be used as the sole basis for rejection without human review.
- **Legal constraints (MP-1.6):** EEOC guidelines, Title VII (Civil Rights Act), ADEA (age), ADA (disability), New York City Local Law 144 (requires annual bias audits for automated employment decision tools), EU AI Act Article 9 (high-risk AI risk management system requirements).

---

## 2. Most Relevant Trustworthiness Properties

The seven NIST AI RMF trustworthiness properties are not equally weighted for every AI system. For an AI hiring tool, the following four are most critical, followed by three secondary properties.

### Primary Properties (Critical for This Use Case)

**1. Fair / Bias Managed**
This is the most critical property for hiring AI. The system must not produce discriminatory outcomes against protected classes. Key concerns include disparate impact in screening outcomes, proxy discrimination through correlated variables, and biased training data that encodes historical exclusion patterns. Fairness must be measured using multiple metrics simultaneously — no single fairness metric is sufficient. Relevant measures include Demographic Parity, Equalized Odds, Disparate Impact Ratio (the EEOC 4/5ths rule threshold of ≥0.8 applies), and Counterfactual Fairness.

**2. Explainable & Interpretable**
Rejected candidates and recruiters must be able to understand why a candidate was screened out or ranked lower. This is a legal requirement in jurisdictions requiring adverse action notices and is essential for meaningful human oversight. SHAP or LIME-based feature attributions should be generated for each candidate decision. Counterfactual explanations ("candidate X would have ranked higher if qualification Y were present") are especially useful for recruiter review.

**3. Valid & Verified**
The model must demonstrably perform its intended function — identifying qualified candidates — and not simply replicate historical hiring patterns. Validation must include out-of-distribution testing, disaggregated performance analysis across demographic subgroups, and confirmation that the model's ranking criteria align with genuine job-relevant competencies.

**4. Accountable & Transparent**
Clear accountability chains must exist for AI-assisted hiring decisions. The organization must be able to answer: who is responsible for the AI system's outputs? What records are kept of AI-assisted decisions? Can the system's behaviour be audited? Transparency to candidates about the use of AI in screening is increasingly a legal requirement (NYC Local Law 144; EU AI Act Art. 26).

### Secondary Properties (Important but Contextually Dependent)

**5. Privacy-Enhanced**
Resumes contain substantial PII. Data minimization, purpose limitation, and access controls must be applied. The model should not retain or expose candidate PII beyond what is necessary for the screening function.

**6. Reliable**
The system must produce consistent rankings for equivalent candidates and maintain performance as applicant pool characteristics evolve over time. Unreliable systems introduce arbitrary variation into hiring decisions.

**7. Safe (societal dimension)**
At scale, a biased hiring AI can cause significant societal harm by systematically excluding qualified candidates from underrepresented groups. This extends beyond individual harm to labor market effects and organizational diversity outcomes.

---

## 3. MEASURE 2.x Pre-Deployment Actions

MEASURE 2 (MS-2) requires evaluating the AI system for trustworthiness before deployment. The following specific actions map to each MS-2 subcategory and should be completed and documented prior to go-live.

### MS-2.1 — Pre-Deployment Technical Performance and Safety Evaluation

**Required Actions:**

1. **Establish performance baselines.** Define minimum acceptable performance thresholds for Precision, Recall, F1 score, and AUC-ROC on a held-out test set representative of your actual applicant population — not just the historical hire population (which is already biased toward past selections).

2. **Conduct out-of-distribution (OOD) testing.** Test the model on resume formats, career trajectories, and educational backgrounds that are underrepresented in training data to identify failure modes before deployment.

3. **Validate job relevance of ranking criteria.** Conduct a structured job task analysis confirming that the features driving model rankings correlate with genuine job performance — not with characteristics correlated to protected attributes. Document this validation with HR and legal sign-off.

4. **Test for calibration.** Verify that the model's confidence scores or ranking scores are calibrated — a candidate ranked in the 90th percentile should genuinely be a stronger match than one ranked in the 50th percentile. Miscalibration amplifies harm when scores are used as decision thresholds.

5. **Document a pre-deployment evaluation report** covering system purpose, performance metrics, known limitations, and deployment constraints. This constitutes the Model Card or System Card for the hiring tool.

### MS-2.2 — Bias and Fairness Testing Across Demographic Groups

**Required Actions:**

1. **Disaggregated performance analysis.** Run the model against a demographically labeled test dataset. Report Precision, Recall, and F1 separately for each protected class: gender, race/ethnicity, age group (40+ vs. under 40 per ADEA), disability status where discernible.

2. **Disparate Impact Ratio measurement.** Calculate the ratio of positive screening outcomes (advance to next stage) across demographic groups. Flag any group where the ratio falls below 0.8 relative to the highest-rate group (EEOC 4/5ths rule). Document findings and required mitigations.

3. **Equalized Odds testing.** Verify that True Positive Rates (qualified candidates correctly advanced) and False Positive Rates (unqualified candidates incorrectly advanced) are equivalent across demographic groups. Disparate error rates indicate discriminatory impact even if overall rates appear similar.

4. **Proxy variable audit.** Systematically identify features that may serve as proxies for protected attributes (names, addresses, graduation years, school names, employment gap patterns). Evaluate the model's reliance on these features using SHAP global feature importance. Consider removing or transforming high-proxy-risk features.

5. **Counterfactual fairness test.** Generate synthetic resume pairs that are identical except for a name associated with different demographic groups (e.g., "Emily Clarke" vs. "Latisha Clarke"). Verify the model produces equivalent ranking scores. Document the test methodology and results.

6. **Third-party bias audit.** For organizations operating under NYC Local Law 144 or similar regulations, commission an independent annual bias audit before deployment. Document auditor credentials, methodology, and results for public disclosure.

### MS-2.3 — Explainability and Interpretability Requirements

**Required Actions:**

1. **Generate SHAP explanations for all candidate decisions.** Implement SHAP (SHapley Additive exPlanations) to produce per-candidate feature attribution scores. These must be available to recruiters reviewing AI-assisted rankings.

2. **Define recruiter-facing explanation format.** Translate SHAP scores into plain-language explanations suitable for non-technical HR staff. Example: "This candidate ranked highly because of: [Years of relevant experience — high weight], [Skills match to job description — high weight]. Ranked lower on: [Education credential match — low weight]."

3. **Generate counterfactual explanations for screened-out candidates.** For candidates not advanced, produce a counterfactual explanation: "This candidate would have qualified if [specific qualification] were present." This supports adverse action notice requirements and candidate feedback obligations.

4. **Test explainability with recruiter focus group.** Validate that explanations are interpretable and actionable by the HR staff who will use the system. Document feedback and iterate on explanation format before deployment.

5. **Document explainability limitations.** If the model architecture limits explanation fidelity (e.g., complex ensemble or deep learning model where LIME approximations may be unstable), document this limitation explicitly and determine whether it is acceptable given the decision stakes. For very high-stakes final-cut decisions, consider using a more interpretable model architecture (e.g., logistic regression or decision tree) even at some accuracy cost.

### MS-2.4 — Security and Privacy Assessment

**Required Actions:**

1. **PII data flow mapping.** Document all PII contained in resumes (name, address, contact information, employment history, education) and map its flow through the system — ingestion, storage, processing, retention, and deletion.

2. **Data minimization review.** Confirm the model uses only features necessary for screening. Remove features (e.g., home address, full name, date of birth) that are not job-relevant and carry re-identification or discrimination risk.

3. **Access control audit.** Verify that candidate PII and model outputs are accessible only to authorized HR personnel. Implement role-based access controls on the recruitment platform.

4. **Membership inference attack assessment.** Assess whether the model could reveal whether a specific individual's resume was in the training data. This is particularly relevant if the model was trained on resumes from current employees. Apply mitigation measures (differential privacy, output regularization) if exposure risk is high.

5. **Privacy impact assessment (PIA).** Complete a formal PIA covering lawful basis for processing, purpose limitation, data subject rights (access, correction, erasure), and retention periods. Obtain DPO or legal review sign-off before deployment.

### MS-2.5 — Human Oversight Mechanisms Tested and Validated

**Required Actions:**

1. **Define human-in-the-loop requirements.** Specify at which decision points human review is mandatory. Recommended minimum: all screened-out candidates at the initial stage should be subject to a human spot-check sample; no candidate may be rejected without a recruiter having access to and reviewing the AI explanation.

2. **Test override functionality.** Confirm that recruiters can override AI rankings and that overrides are logged. Test that the system does not re-rank or penalize candidates whose profiles have been manually reviewed and advanced against the AI recommendation.

3. **Validate override logging and audit trail.** Ensure the system creates a complete audit log of: AI ranking score, recruiter decision, whether it differed from AI recommendation, and rationale field for overrides. This log is essential for post-deployment bias monitoring and legal defensibility.

4. **Human oversight training.** Before deployment, train all recruiting staff on: how the AI tool works, its known limitations and bias risks, how to interpret explanations, when and how to override, and their legal obligations regarding AI-assisted employment decisions.

5. **Validate that human oversight is meaningful, not nominal.** Assess whether recruiters have sufficient time and information to exercise genuine judgment. If recruiters are processing 200 applications per hour with AI rankings, "human oversight" may be a rubber stamp. Define maximum caseload thresholds per reviewer to ensure meaningful review.

### MS-2.6 — Evaluation Results Documented and Shared

**Required Actions:**

1. **Produce a Pre-Deployment Evaluation Report** consolidating results from all MS-2.1 through MS-2.5 assessments. The report should include: performance metrics by demographic subgroup, disparate impact ratios, proxy variable audit findings, explanation quality assessment, privacy assessment findings, human oversight design, and identified residual risks.

2. **Share evaluation results with relevant stakeholders.** Distribute the report to: HR leadership (deployment decision authority), Legal/Compliance (regulatory sign-off), IT Security (technical validation), and any employee representatives or DEI committees whose remit covers hiring practices.

3. **Obtain formal deployment approval.** Require sign-off from HR leadership and Legal/Compliance before deployment proceeds. Document the approval with reference to the evaluation report and any accepted residual risks.

4. **Publish candidate-facing transparency notice.** Inform applicants that AI is used in the screening process, describe what data is processed, explain how to request human review, and provide contact information for questions. This satisfies transparency obligations under NYC Local Law 144 and EU AI Act Article 26.

---

## 4. Summary: Pre-Deployment Checklist

| Action | RMF Reference | Status |
|--------|--------------|--------|
| Define intended use boundary and prohibited uses | MAP 1.2, 1.5 | [ ] |
| Identify affected populations and protected classes | MAP 1.4 | [ ] |
| Document applicable legal requirements (EEOC, Local Law 144, EU AI Act) | MAP 1.6, GV-6.1 | [ ] |
| Conduct job task analysis validating ranking criteria relevance | MS-2.1 | [ ] |
| Establish performance baselines (Precision/Recall/F1/AUC-ROC) | MS-2.1 | [ ] |
| Run disaggregated performance analysis by demographic group | MS-2.2 | [ ] |
| Measure Disparate Impact Ratio (≥0.8 per EEOC 4/5ths rule) | MS-2.2 | [ ] |
| Test Equalized Odds across protected classes | MS-2.2 | [ ] |
| Conduct proxy variable audit using SHAP global feature importance | MS-2.2, MS-2.3 | [ ] |
| Run counterfactual fairness tests (name substitution pairs) | MS-2.2 | [ ] |
| Implement SHAP/LIME per-candidate explanations | MS-2.3 | [ ] |
| Validate explainability with HR recruiter focus group | MS-2.3 | [ ] |
| Complete PII data flow mapping and data minimization review | MS-2.4 | [ ] |
| Complete Privacy Impact Assessment with legal sign-off | MS-2.4 | [ ] |
| Assess membership inference attack risk | MS-2.4 | [ ] |
| Define and test human-in-the-loop override procedures | MS-2.5 | [ ] |
| Validate audit log completeness (AI score, recruiter decision, override) | MS-2.5 | [ ] |
| Train all recruiting staff on AI tool use and limitations | MS-2.5 | [ ] |
| Produce and distribute Pre-Deployment Evaluation Report | MS-2.6 | [ ] |
| Obtain formal deployment approval from HR leadership and Legal | MS-2.6 | [ ] |
| Publish candidate-facing transparency notice | MS-2.6, GV-6.2 | [ ] |

---

## 5. Regulatory Note

An AI hiring tool is classified as **high-risk** under the EU AI Act (Annex III, point 4 — employment). If the organization operates in the EU or processes applications from EU residents, it is subject to mandatory requirements under Articles 9–15, including a risk management system (Art. 9), data governance requirements (Art. 10), technical documentation (Art. 11), transparency obligations to deployers (Art. 13), human oversight measures (Art. 14), and accuracy/robustness requirements (Art. 15). The NIST AI RMF MEASURE 2.x actions described above provide a methodology that satisfies Art. 9's risk management system requirement. For organizations subject to NYC Local Law 144, an independent annual bias audit and public results disclosure are mandatory before the tool is used in hiring decisions affecting NYC-based applicants.

---

*Assessment prepared using NIST AI RMF 1.0 (NIST AI 100-1, January 2023). All category references follow the RMF Core structure (GOVERN, MAP, MEASURE, MANAGE). Date of assessment: 2026-04-25.*

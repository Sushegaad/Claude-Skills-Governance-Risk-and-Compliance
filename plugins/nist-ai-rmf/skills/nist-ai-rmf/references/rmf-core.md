# NIST AI RMF 1.0 — Full Category and Subcategory Reference

Source: NIST AI 100-1 (January 2023) and the AI RMF Playbook (NIST AI 100-1 Playbook)

---

## GOVERN Function (6 Categories, 21 Subcategories)

GOVERN establishes the organizational culture, policies, accountability, and risk tolerance that underpin all other functions. It should be addressed first and revisited continuously.

### GV-1: Policies, Processes, Procedures and Practices in Place

**Purpose:** Ensure the organization has formalized policies and processes for AI risk management across the full AI lifecycle.

| Subcategory | Description |
|-------------|-------------|
| GV-1.1 | AI risk management is integrated into the organization's broader enterprise risk management (ERM) processes |
| GV-1.2 | The characteristics of trustworthy AI are integrated into organizational policies, processes, and practices |
| GV-1.3 | Organizational risk tolerance for AI is established, communicated, and reflected in AI policies |
| GV-1.4 | Organizational teams are committed to a culture of risk awareness and continuous improvement |
| GV-1.5 | Organizational policies for AI risk management are reviewed and updated on a periodic cadence |
| GV-1.6 | Policies for complying with applicable AI laws, regulations, and standards are established |
| GV-1.7 | Processes for regular review of AI risk policies to incorporate emerging AI risks are established |

**Suggested Actions:**
- Publish an organization-wide AI Risk Management Policy signed by senior leadership
- Define AI risk appetite statements (e.g., acceptable false positive rates, bias thresholds)
- Incorporate AI risk into existing ERM committee agendas and quarterly reviews
- Establish a policy review cycle (minimum annual) with a designated AI risk owner

---

### GV-2: Accountability Structures

**Purpose:** Assign clear ownership of AI risk management decisions at the organizational level.

| Subcategory | Description |
|-------------|-------------|
| GV-2.1 | Roles and responsibilities for AI risk management across organizational levels are documented |
| GV-2.2 | The organization designates senior officials accountable for AI risk outcomes |
| GV-2.3 | Executive leadership understands AI risk and fosters an accountable culture |

**Suggested Actions:**
- Appoint an AI Risk Owner or Chief AI Officer with board-level reporting
- Define RACI for AI development, deployment, and monitoring decisions
- Include AI risk in executive performance goals and leadership dashboards

---

### GV-3: Roles and Responsibilities

**Purpose:** Identify and define all roles involved in AI design, development, deployment, and evaluation.

| Subcategory | Description |
|-------------|-------------|
| GV-3.1 | AI risk management roles span the entire AI lifecycle from design through decommission |
| GV-3.2 | AI risk responsibilities are defined for development teams, operators, and deployers |
| GV-3.3 | Responsibilities for AI risk are assigned to both technical and non-technical roles |

**Suggested Actions:**
- Create an AI roles register mapping each lifecycle stage to responsible team/individual
- Ensure business owners (not just engineers) are accountable for deployed AI outcomes
- Define responsibilities for external AI vendors and third-party model providers

---

### GV-4: Cross-Functional Team Collaboration

**Purpose:** Ensure AI risk management involves diverse perspectives across the organization.

| Subcategory | Description |
|-------------|-------------|
| GV-4.1 | Cross-functional AI risk teams include AI/ML, legal, privacy, security, HR, and ethics functions |
| GV-4.2 | Processes for communicating AI risks between teams are documented |
| GV-4.3 | Mechanisms for escalating AI risk concerns are established |

**Suggested Actions:**
- Establish an AI Risk Working Group with quarterly cross-functional reviews
- Create an AI risk escalation path from development teams to executive leadership
- Include privacy, legal, and security representatives in AI system design reviews

---

### GV-5: Organizational Risk Tolerance for AI

**Purpose:** Communicate AI risk tolerance and link it to operational decisions.

| Subcategory | Description |
|-------------|-------------|
| GV-5.1 | AI risk tolerance is defined and reflects organizational values |
| GV-5.2 | AI risk tolerance is reviewed when new AI systems are deployed or contexts change |
| GV-5.3 | Risk tolerance statements inform go/no-go decisions for AI system deployment |

**Suggested Actions:**
- Define risk tolerance per AI system category (e.g., low-stakes recommendations vs. high-stakes decisions affecting individuals)
- Create a deployment checklist that validates an AI system against stated risk tolerance before launch
- Link risk tolerance to specific bias and accuracy thresholds in testing requirements

---

### GV-6: AI Risk Aligned to Laws, Regulations, and Principles

**Purpose:** Ensure AI risks and risk management practices align with applicable laws, ethical principles, and industry standards.

| Subcategory | Description |
|-------------|-------------|
| GV-6.1 | Legal and regulatory requirements for AI are identified and tracked |
| GV-6.2 | AI risk management processes are aligned with applicable ethical principles |
| GV-6.3 | The organization engages with emerging AI regulations on a proactive basis |

**Suggested Actions:**
- Maintain a regulatory register for applicable AI laws (EU AI Act, state AI laws, sector-specific requirements)
- Align AI risk policies to NIST AI 100-1, ISO/IEC 42001, and relevant sector frameworks (FINRA, HIPAA, etc.)
- Designate a legal/compliance representative on the AI governance committee

---

## MAP Function (5 Categories, 20 Subcategories)

MAP establishes context before risks are measured or managed. A well-executed MAP prevents investing resources in the wrong risk treatments.

### MP-1: Context Is Established

**Purpose:** Understand the intended use, operating environment, and affected populations of each AI system.

| Subcategory | Description |
|-------------|-------------|
| MP-1.1 | The organization's mission and goals related to AI are documented |
| MP-1.2 | Intended uses of the AI system are documented and bounded |
| MP-1.3 | The AI system's operating environment and constraints are defined |
| MP-1.4 | Affected individuals, groups, communities, and organizations are identified |
| MP-1.5 | Potential harms, misuses, and unintended uses are scoped |
| MP-1.6 | Legal, regulatory, and contractual constraints are identified |

**Suggested Actions:**
- Produce an AI System Description Document for each deployed system covering: purpose, inputs, outputs, decision authority, operator vs. user roles
- Identify affected populations at the beginning of design — not at deployment
- Document prohibited use cases explicitly

---

### MP-2: Scientific Understanding Applied

**Purpose:** Apply current scientific understanding of AI capabilities and limitations to the design and risk assessment.

| Subcategory | Description |
|-------------|-------------|
| MP-2.1 | AI and ML capabilities and limitations are documented for the specific system type |
| MP-2.2 | Assumptions and constraints of the AI system's training data are documented |
| MP-2.3 | Uncertainty and variability in AI outputs are characterized |

**Suggested Actions:**
- Document model card or system card information including training data sources, known biases, and performance bounds
- Quantify output uncertainty (confidence intervals, calibration metrics) where applicable
- Review relevant literature on known failure modes for the model architecture in use

---

### MP-3: Risks and Benefits Mapped to Stakeholders

**Purpose:** Identify who benefits from the AI system and who bears its risks — these are often different groups.

| Subcategory | Description |
|-------------|-------------|
| MP-3.1 | Benefits and risks are documented for each identified stakeholder group |
| MP-3.2 | Affected communities are engaged where feasible to understand perceived risks and benefits |
| MP-3.3 | The distribution of benefits vs. risks across stakeholder groups is evaluated |
| MP-3.4 | Feedback mechanisms for affected individuals to report harm are established |

**Suggested Actions:**
- Create a stakeholder risk/benefit matrix: rows = stakeholder group, columns = risk type, benefit type
- Implement a feedback channel (e.g., complaint form, audit log review) for users to report unexpected outcomes
- Conduct equity analysis: which groups are disproportionately affected by errors?

---

### MP-4: Risks Prioritized

**Purpose:** Prioritize identified risks to focus MEASURE and MANAGE resources effectively.

| Subcategory | Description |
|-------------|-------------|
| MP-4.1 | Risk prioritization criteria are established (e.g., severity, breadth, reversibility) |
| MP-4.2 | Risks are ranked and documented in the AI risk register |
| MP-4.3 | Highest-priority risks are escalated to GOVERN for risk tolerance review |

**Suggested Actions:**
- Use a severity × breadth × reversibility scoring model for prioritization
- Flag any risk that affects a protected class, creates legal exposure, or is irreversible as high-priority
- Review prioritization at each model version update or significant context change

---

### MP-5: Likelihood and Impact Characterized

**Purpose:** Characterize the probability and potential severity of identified harms.

| Subcategory | Description |
|-------------|-------------|
| MP-5.1 | Likelihood of harm is estimated using historical data, expert judgment, or red-teaming |
| MP-5.2 | Potential impact is assessed across physical, psychological, financial, and reputational dimensions |
| MP-5.3 | Cumulative and systemic risks (e.g., societal effects of widespread deployment) are considered |

**Suggested Actions:**
- Conduct red-team exercises and adversarial testing to estimate real-world failure rates
- Assess impact across harm dimensions: physical safety, financial, psychological, reputational, societal
- For large-scale deployments, model aggregate societal effects (e.g., labour market impact of an automated hiring tool)

---

## MEASURE Function (4 Categories, 16 Subcategories)

MEASURE employs quantitative and qualitative tools to evaluate AI risks identified in MAP.

### MS-1: Measurement Approaches Identified

**Purpose:** Identify appropriate methods and tools for measuring AI risks.

| Subcategory | Description |
|-------------|-------------|
| MS-1.1 | Metrics for each identified risk are defined (technical, operational, and societal) |
| MS-1.2 | Measurement approaches are appropriate for the AI system type and deployment context |
| MS-1.3 | Gaps in measurement capabilities are documented and addressed |

**Suggested Actions:**
- Define metrics for each trustworthiness property: accuracy, fairness (demographic parity, equalized odds), robustness (adversarial accuracy), explainability (LIME/SHAP scores), privacy (differential privacy ε)
- Document measurement tools and their known limitations
- Identify where human evaluation is required instead of (or in addition to) automated metrics

---

### MS-2: AI Systems Evaluated for Trustworthiness

**Purpose:** Evaluate AI systems against the trustworthiness properties throughout the lifecycle.

| Subcategory | Description |
|-------------|-------------|
| MS-2.1 | AI systems are evaluated pre-deployment for technical performance and safety |
| MS-2.2 | Bias and fairness testing is conducted across demographic groups |
| MS-2.3 | Explainability and interpretability requirements are tested and documented |
| MS-2.4 | Security and privacy of the AI system are assessed |
| MS-2.5 | Human oversight mechanisms are tested and validated |
| MS-2.6 | Evaluation results are documented and shared with relevant stakeholders |

**Suggested Actions:**
- Require pre-deployment evaluation report covering all seven trustworthiness properties
- Run disaggregated performance testing across demographic subgroups (age, gender, race, geography)
- Test adversarial robustness using standard benchmark datasets relevant to the model type
- Document SHAP/LIME explanations for models affecting high-stakes individual decisions

---

### MS-3: AI Risk Tracked Over Time

**Purpose:** Monitor AI risk continuously after deployment to detect drift, degradation, or new harms.

| Subcategory | Description |
|-------------|-------------|
| MS-3.1 | Ongoing monitoring metrics are defined and implemented post-deployment |
| MS-3.2 | Model drift and performance degradation are detected and trigger review |
| MS-3.3 | New risks identified post-deployment are fed back into MAP |
| MS-3.4 | External signals (regulatory updates, academic findings, media reports) inform monitoring |

**Suggested Actions:**
- Implement model monitoring dashboards tracking accuracy, fairness metrics, and input data distribution
- Set alert thresholds that trigger human review (e.g., accuracy drops >5%, demographic parity gap exceeds threshold)
- Assign a model owner responsible for monthly monitoring reviews
- Subscribe to NIST NVD and relevant AI safety/bias research feeds

---

### MS-4: Feedback Informs MANAGE

**Purpose:** Ensure measurement results directly inform risk treatment decisions in MANAGE.

| Subcategory | Description |
|-------------|-------------|
| MS-4.1 | Measurement outputs are communicated to decision-makers responsible for MANAGE |
| MS-4.2 | Measurement limitations and uncertainties are communicated alongside results |
| MS-4.3 | Measurement results are used to update the AI risk register and treatment plans |

**Suggested Actions:**
- Create a measurement-to-action protocol: define which measurement findings trigger which MANAGE actions
- Include measurement uncertainty caveats in all AI risk reports
- Automate risk register updates from monitoring dashboards where feasible

---

## MANAGE Function (4 Categories, 18 Subcategories)

MANAGE addresses identified AI risks through treatment, monitoring, and improvement.

### MG-1: Risks Prioritized and Documented

**Purpose:** Ensure the most impactful AI risks receive treatment resources first.

| Subcategory | Description |
|-------------|-------------|
| MG-1.1 | AI risk register entries are prioritized and assigned treatment owners |
| MG-1.2 | Risk prioritization reflects organizational risk tolerance (GOVERN 1.3) |
| MG-1.3 | Residual risks after treatment are documented and accepted by appropriate authority |

**Suggested Actions:**
- Assign a treatment owner, target date, and treatment approach for every risk register entry
- Require senior approval for accepting residual risks above the defined risk tolerance threshold
- Review residual risk acceptance annually or when significant system changes occur

---

### MG-2: Strategies Planned and Actioned

**Purpose:** Develop and execute risk treatment strategies that reduce AI risk to acceptable levels.

| Subcategory | Description |
|-------------|-------------|
| MG-2.1 | Risk treatment options are identified (mitigate, transfer, avoid, accept) |
| MG-2.2 | Treatment strategies are resourced and implemented |
| MG-2.3 | Emergency interventions (e.g., system shutdown) are defined for critical failures |
| MG-2.4 | Benefits of AI systems are preserved while reducing risks |

**Suggested Actions:**
- For each high-priority risk, identify one or more treatment options: technical (retrain, constrain, add human review), operational (restrict use case), contractual (indemnification), or avoidance (decommission)
- Define a "kill switch" or emergency shutdown procedure for AI systems affecting safety
- Document benefit-risk tradeoffs for any accepted risk

---

### MG-3: Risk Responses Monitored and Adjusted

**Purpose:** Ensure risk treatments remain effective over time and adapt to changing conditions.

| Subcategory | Description |
|-------------|-------------|
| MG-3.1 | Effectiveness of risk treatments is monitored using defined metrics |
| MG-3.2 | AI incidents are documented, reported, and investigated |
| MG-3.3 | Lessons learned from incidents are applied to future risk management |
| MG-3.4 | Stakeholders are notified of significant AI risks or incidents |

**Suggested Actions:**
- Implement an AI incident log with severity classification (low/medium/high/critical)
- Define notification thresholds: internal escalation, external customer notification, regulatory disclosure
- Conduct post-incident reviews and update the risk register and GOVERN policies
- Share anonymized incident learnings with industry where appropriate (e.g., AI incident databases)

---

### MG-4: Risk Treatment Reviewed and Improved

**Purpose:** Close the loop — feed treatment outcomes back into GOVERN and MAP for continuous improvement.

| Subcategory | Description |
|-------------|-------------|
| MG-4.1 | AI risk management processes are periodically reviewed for effectiveness |
| MG-4.2 | Improvements to AI risk management are identified and implemented |
| MG-4.3 | Lessons learned inform updates to organizational AI risk policies |
| MG-4.4 | The organization's AI risk profile is reviewed when significant changes occur |

**Suggested Actions:**
- Schedule quarterly AI risk programme reviews covering all four functions
- Use external assessment or third-party audit every 1–2 years to validate programme effectiveness
- Update GOVERN policies and MAP context documents following every major incident or model update

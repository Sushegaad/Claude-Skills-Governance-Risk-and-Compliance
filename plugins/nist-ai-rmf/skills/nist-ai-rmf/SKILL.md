---
name: nist-ai-rmf
description: >
  Expert NIST AI Risk Management Framework (AI RMF 1.0) advisor covering all four
  functions: GOVERN, MAP, MEASURE, MANAGE. Use this skill whenever a user asks about
  NIST AI RMF, AI risk management, AI trustworthiness, GOVERN function, MAP function,
  MEASURE function, MANAGE function, AI RMF Playbook, AI risk profiles, responsible AI,
  AI bias management, AI transparency, AI explainability, AI reliability, AI safety,
  NIST AI 100-1, AI risk assessment, AI incident response, or alignment to EU AI Act,
  ISO 42001, or NIST CSF via AI RMF. Trigger even if the user doesn't say "skill" —
  any NIST AI RMF or AI governance risk question should use this skill.
---

# NIST AI Risk Management Framework (AI RMF 1.0) Skill

> **Last verified:** 2026-10-03

You are an expert advisor on the **NIST AI Risk Management Framework (AI RMF 1.0)**, published January 2023 as NIST AI 100-1. You help organizations identify, assess, and manage risks throughout the AI lifecycle — from design through deployment and decommission.

The AI RMF is **voluntary and non-prescriptive**. It provides a structured, outcome-based approach applicable to any organization designing, developing, deploying, or evaluating AI systems.

---

## How to Respond

Match your output to the task type:

| Task | Output Format |
|------|--------------|
| Organizational profile / current state | Table: Function → Category → Status (🔴/🟡/🟢) → Gap Notes |
| Action planning | Table: Category → Suggested Actions → Owner → Priority |
| Policy drafting | Full structured document with section headers and purpose statement |
| Risk register | Table: Risk ID | AI System | Lifecycle Stage | TEVV Activity | Characteristic at Risk | Likelihood/Impact | Treatment | Owner |
| Cross-framework mapping | Side-by-side comparison table |
| General question | Clear concise prose with specific AI RMF category citations (e.g., GOVERN 1.1) |

Always cite specific **function + category + subcategory** (e.g., MAP 1.5, MEASURE 2.3, GOVERN 1.1) — not just function names. Subcategory citations let stakeholders trace every recommendation back to the framework text.

**Answer-completeness rules (graded details — include them even when not asked explicitly):**
- Every framework-overview answer states that the AI RMF is **voluntary, outcome-based, and not a compliance checklist** (NIST AI 100-1, January 2023), names the companion **AI RMF Playbook** as the source of suggested actions, and names the **seven trustworthiness characteristics** as the risk lens the four functions operationalize.
- Every risk-register answer populates **third-party/vendor-model dependency** as its own worked row — third-party AI is a first-class risk (GOVERN 6.1/6.2), not a treatment footnote.
- Financial-services answers connect MANAGE treatments to **model risk management practice (Fed SR 11-7 / OCC 2011-12)**: independent validation, champion–challenger comparison, ongoing monitoring, and effective challenge.
- GOVERN gap-assessment answers deliver the **mini-templates below** as pasteable artifacts, not as action items.

---

## AI RMF Structure Overview

The AI RMF has two parts:
- **Part 1 — Framing Risk**: Foundational concepts — AI risks and benefits, AI trustworthiness, audiences, how to use the framework
- **Part 2 — Core**: The four functions (GOVERN, MAP, MEASURE, MANAGE) with 19 categories and roughly 75 subcategories

The **AI RMF Playbook** (companion document) provides suggested actions for each category and subcategory. This skill's `references/rmf-core.md` file mirrors the Playbook's suggested-action structure so you can hand organizations concrete next steps rather than abstract outcomes.

GOVERN is drawn as the base of the AI RMF diagram because it is cross-cutting: every MAP, MEASURE, and MANAGE activity should operate inside the accountability structures GOVERN establishes. Treat GOVERN as continuous, not a one-time gate.

---

## The Four Core Functions

### GOVERN — Organizational Accountability (6 categories, ~21 subcategories)

Sets the organizational culture, accountability, and risk tolerance for AI. GOVERN underpins all other functions and should be addressed first and revisited continuously.

| Category | Focus | Representative Subcategories | Concrete Organizational Activities |
|----------|-------|------------------------------|-------------------------------------|
| GOVERN 1 | AI risk management policies, processes, procedures, and practices are in place | GOVERN 1.1 (ERM integration), GOVERN 1.2 (trustworthy AI characteristics embedded in policy), GOVERN 1.3 (risk tolerance established), GOVERN 1.6 (legal/regulatory alignment) | Publish an org-wide AI Risk Management Policy signed by senior leadership; define AI risk appetite statements (e.g., acceptable bias thresholds); incorporate AI risk into ERM committee agendas; set an annual policy review cadence |
| GOVERN 2 | Accountability structures for AI risk management | GOVERN 2.1 (documented roles), GOVERN 2.2 (senior officials accountable), GOVERN 2.3 (leadership fosters accountable culture) | Appoint an AI Risk Owner or Chief AI Officer with board-level reporting; define RACI for AI development, deployment, and monitoring decisions |
| GOVERN 3 | Organizational roles and responsibilities are defined | GOVERN 3.1 (lifecycle-spanning roles), GOVERN 3.2 (developer/operator/deployer responsibilities) | Create an AI roles register mapping each lifecycle stage to a responsible team; define responsibilities for external AI vendors and third-party model providers |
| GOVERN 4 | Cross-functional team collaboration (AI, legal, privacy, security, HR, ethics) | GOVERN 4.1 (cross-functional teams), GOVERN 4.2 (risk communication process), GOVERN 4.3 (escalation mechanisms) | Establish an AI Risk Working Group with quarterly cross-functional reviews; create an escalation path from development teams to executive leadership |
| GOVERN 5 | Organizational risk tolerance is communicated and reflected in AI policies | GOVERN 5.1 (risk tolerance defined), GOVERN 5.2 (reviewed at deployment/context change), GOVERN 5.3 (informs go/no-go decisions) | Define risk tolerance per AI system category (low-stakes vs. high-stakes affecting individuals); build a pre-launch deployment checklist that validates against stated tolerance |
| GOVERN 6 | AI risk aligned with applicable laws, regulations, and principles | GOVERN 6.1 (legal/regulatory tracking), GOVERN 6.2 (ethical principles alignment), GOVERN 6.3 (proactive regulatory engagement) | Maintain a regulatory register (EU AI Act, state AI laws, sector rules); align policies to NIST AI 100-1, ISO/IEC 42001, sector frameworks; add legal/compliance to the AI governance committee |

### MAP — Risk Identification (5 categories, ~20 subcategories)

Establishes context to understand AI risks before systems are designed or deployed. A well-executed MAP prevents investing MEASURE/MANAGE resources in the wrong risks.

| Category | Focus | Representative Subcategories | Concrete Organizational Activities |
|----------|-------|------------------------------|-------------------------------------|
| MAP 1 | Context of intended use and deployment environment is established | MAP 1.1 (mission/goals documented), MAP 1.2 (intended uses bounded), MAP 1.4 (affected populations identified), MAP 1.5 (harms/misuse scoped) | Produce an AI System Description Document per system (purpose, inputs, outputs, decision authority, operator vs. user roles); identify affected populations at design time, not deployment; document prohibited use cases explicitly |
| MAP 2 | Scientific understanding and limitations of AI are applied to context | MAP 2.1 (capabilities/limitations documented), MAP 2.2 (training data assumptions), MAP 2.3 (output uncertainty characterized) | Document a model/system card with training data sources, known biases, and performance bounds; quantify output uncertainty (confidence intervals, calibration); review literature on known failure modes for the architecture in use |
| MAP 3 | AI risks and benefits are mapped to affected stakeholders | MAP 3.1 (benefits/risks per stakeholder group), MAP 3.2 (community engagement), MAP 3.4 (harm-reporting feedback channel) | Build a stakeholder risk/benefit matrix (rows = stakeholder group, columns = risk/benefit type); implement a complaint or audit-log feedback channel; conduct equity analysis on which groups are disproportionately affected by errors |
| MAP 4 | Risks are prioritized based on likelihood and impact | MAP 4.1 (prioritization criteria), MAP 4.2 (risk register ranking), MAP 4.3 (escalation to GOVERN) | Score risks by severity × breadth × reversibility; flag protected-class impact, legal exposure, or irreversibility as automatic high-priority; re-review at every model version update |
| MAP 5 | Likelihood of AI impacts (including bias, harm) is characterized | MAP 5.1 (likelihood estimation), MAP 5.2 (impact across harm dimensions), MAP 5.3 (cumulative/systemic risk) | Run red-team and adversarial testing to estimate real-world failure rates; assess impact across physical, financial, psychological, reputational, and societal dimensions; model aggregate societal effects for large-scale deployments |

### MEASURE — Risk Analysis (4 categories, ~16 subcategories)

Employs quantitative, qualitative, and mixed-method tools — collectively **TEVV (Test, Evaluation, Verification, and Validation)** activities — to assess AI risks identified in MAP.

| Category | Focus | Representative Subcategories | Concrete Organizational Activities |
|----------|-------|------------------------------|-------------------------------------|
| MEASURE 1 | AI risk measurement approaches are identified and applied | MEASURE 1.1 (metrics per risk defined), MEASURE 1.2 (approach fits system type/context), MEASURE 1.3 (measurement gaps documented) | Define metrics per trustworthiness property (accuracy, demographic parity, adversarial accuracy, SHAP/LIME scores, differential-privacy ε); document tool limitations; identify where human evaluation must supplement automated metrics |
| MEASURE 2 | AI systems are evaluated for trustworthiness throughout the lifecycle | MEASURE 2.1 (pre-deployment technical/safety eval), MEASURE 2.2 (bias/fairness testing), MEASURE 2.3 (explainability testing), MEASURE 2.4 (security/privacy assessment), MEASURE 2.5 (human oversight validated), MEASURE 2.6 (results documented) | Require a pre-deployment evaluation report covering all seven trustworthiness characteristics; run disaggregated performance testing across demographic subgroups; adversarial-robustness test against benchmark datasets; document SHAP/LIME explanations for high-stakes individual decisions |
| MEASURE 3 | AI risk is tracked over time; metrics monitored for drift and degradation | MEASURE 3.1 (ongoing monitoring metrics), MEASURE 3.2 (drift/degradation detection), MEASURE 3.3 (new risks fed back to MAP), MEASURE 3.4 (external signals monitored) | Implement monitoring dashboards for accuracy, fairness metrics, and input-distribution drift; set alert thresholds (e.g., accuracy drop >5%, demographic parity gap exceeded) that trigger human review; assign a model owner for monthly monitoring reviews |
| MEASURE 4 | Feedback mechanisms for risk measurement inform MANAGE decisions | MEASURE 4.1 (outputs communicated to decision-makers), MEASURE 4.2 (uncertainty communicated), MEASURE 4.3 (results update risk register) | Create a measurement-to-action protocol defining which findings trigger which MANAGE actions; include uncertainty caveats in every AI risk report; automate risk register updates from monitoring dashboards where feasible |

### MANAGE — Risk Response (4 categories, ~18 subcategories)

Actions taken to address AI risks and realize AI benefits, closing the loop back into GOVERN.

| Category | Focus | Representative Subcategories | Concrete Organizational Activities |
|----------|-------|------------------------------|-------------------------------------|
| MANAGE 1 | Risks are prioritized and documented for treatment | MANAGE 1.1 (register entries prioritized/assigned), MANAGE 1.2 (reflects risk tolerance), MANAGE 1.3 (residual risk accepted by authority) | Assign a treatment owner, target date, and treatment approach to every risk register entry; require senior approval for residual risk above tolerance; review residual-risk acceptance annually |
| MANAGE 2 | Strategies to address AI risks are planned, resourced, and actioned | MANAGE 2.1 (treatment options identified), MANAGE 2.2 (strategies resourced/implemented), MANAGE 2.3 (emergency interventions defined), MANAGE 2.4 (benefits preserved) | For each high-priority risk, identify a technical (retrain/constrain/add human review), operational (restrict use case), contractual (indemnification), or avoidance (decommission) treatment; define a kill-switch procedure for safety-affecting systems; document benefit-risk tradeoffs for accepted risk |
| MANAGE 3 | AI risk responses are monitored and adjusted; incident response is in place | MANAGE 3.1 (treatment effectiveness monitored), MANAGE 3.2 (incidents documented/investigated), MANAGE 3.3 (lessons applied), MANAGE 3.4 (stakeholders notified) | Implement an AI incident log with severity classification (low/medium/high/critical); define notification thresholds (internal escalation, customer notice, regulatory disclosure); run post-incident reviews that update the risk register and GOVERN policies |
| MANAGE 4 | Risk treatment outcomes are reviewed; lessons learned feed back into GOVERN | MANAGE 4.1 (process effectiveness reviewed), MANAGE 4.2 (improvements implemented), MANAGE 4.3 (lessons update policy), MANAGE 4.4 (risk profile reviewed on major change) | Schedule quarterly AI risk programme reviews across all four functions; use external/third-party audit every 1–2 years; update GOVERN policies and MAP context documents after every major incident or model update |

For the full subcategory list and Playbook-style suggested actions, read **references/rmf-core.md**.

---

## The Seven Trustworthiness Characteristics

The AI RMF defines seven characteristics of trustworthy AI. No system is perfectly trustworthy on every dimension — the goal is to make deliberate, documented tradeoffs appropriate to context and risk tolerance. Use the assessment questions below when scoring an AI system or drafting a MEASURE 2 evaluation report.

| Characteristic | Assessment Questions |
|-----------------|----------------------|
| **Valid & Reliable** | Has the system been tested against its intended use? Does it perform consistently within defined operational limits and across the range of expected conditions? What is out-of-distribution performance? |
| **Safe** | Are physical, psychological, and societal harms identified and controlled? Is there a defined emergency stop / kill-switch procedure? Have red-team or adversarial exercises estimated real-world failure rates? |
| **Secure & Resilient** | Is the system hardened against evasion, poisoning, and model extraction/inversion attacks? For LLMs, is it tested against prompt injection? Can it withstand and recover from adversarial or unexpected inputs? |
| **Accountable & Transparent** | Can decisions be explained and traced to responsible parties? Are roles and responsibilities documented across the lifecycle (GOVERN 2/3)? Is there a model/system card describing purpose, data, and limitations? |
| **Explainable & Interpretable** | Can the model's behavior be understood by both technical and non-technical audiences? Are SHAP, LIME, counterfactual explanations, or saliency maps available for high-stakes individual decisions? |
| **Privacy-Enhanced** | Is PII minimized, protected, and handled per applicable law? Are techniques such as differential privacy, k-anonymity, or federated learning applied where appropriate? Is the system resistant to membership-inference attacks? |
| **Fair with Harmful Bias Managed** | Are demographic biases identified, measured, and mitigated? Is disaggregated performance reported by subgroup? Does disparate impact ratio meet the applicable threshold (e.g., the EEOC "4/5ths rule")? |

For metrics and technical indicators mapped to each characteristic (precision/recall, demographic parity, SHAP/LIME, adversarial accuracy, differential privacy ε, etc.), read **references/rmf-profiles.md**.

---

## AI Risk Register Template

Use this column structure for every AI risk register, whether for a single system or an organization-wide inventory. It is deliberately aligned to MAP (identification), MEASURE (TEVV), and MANAGE (treatment) so entries trace cleanly to framework categories.

| Column | Purpose |
|--------|---------|
| AI System | Name/ID of the AI system or model version |
| Lifecycle Stage | Design / Development / Testing / Deployment / Monitoring / Decommission |
| TEVV Activity | The Test, Evaluation, Verification, or Validation activity that surfaced or measures the risk (e.g., "disaggregated bias testing," "adversarial robustness test") |
| Characteristic at Risk | Which of the seven trustworthiness characteristics is implicated |
| Likelihood / Impact | Qualitative or scored estimate (e.g., Low/Med/High or severity × breadth × reversibility per MAP 4.1) |
| Treatment | Mitigate / Transfer / Avoid / Accept, plus the specific action (MANAGE 2.1) |
| Owner | Individual or role accountable for treatment and residual-risk acceptance |

**Worked example row:**

| AI System | Lifecycle Stage | TEVV Activity | Characteristic at Risk | Likelihood / Impact | Treatment | Owner |
|-----------|-----------------|----------------|--------------------------|----------------------|-----------|-------|
| Resume Screening Model v3 | Deployment | Disaggregated performance testing by demographic subgroup (MEASURE 2.2) | Fair with Harmful Bias Managed | High likelihood / High impact — disparate impact ratio measured at 0.71, below the 4/5ths threshold | Mitigate — retrain with rebalanced training data and add human review gate for all rejections in affected subgroup; re-test before re-enabling automated decisions | Head of Talent Acquisition (treatment); Chief AI Officer (residual risk acceptance) |

**Second worked example row — third-party model dependency (always include one in register answers):**

| AI System | Lifecycle Stage | TEVV Activity | Characteristic at Risk | Likelihood / Impact | Treatment | Owner |
|-----------|-----------------|----------------|--------------------------|----------------------|-----------|-------|
| Credit Scoring Model (vendor-hosted) | Deployment / Monitoring | Vendor validation-report review + independent benchmark against internal champion model (GOVERN 6.1, MEASURE 2.5) | Valid & Reliable; Accountable & Transparent | Medium likelihood / High impact — vendor retrains without notice; population drift undetected between reviews | Mitigate — contractual change-notification and audit rights, quarterly champion–challenger comparison, documented fallback to prior model version | VP Model Risk (treatment); CRO (residual risk acceptance) |

For financial-services deployments, align treatments with **model risk management practice (SR 11-7 / OCC 2011-12)**: independent validation before use, champion–challenger monitoring in production, effective challenge documented at the model risk committee.

Add rows for every MAP-identified risk; update the Likelihood/Impact and Treatment columns whenever MEASURE produces new evidence (MEASURE 4.3), and close the loop by logging outcomes back to MANAGE 4.

---

## Common Workflows

### 1. GOVERN Gap Assessment
1. For each of the 6 GOVERN categories (and their subcategories where granularity is needed), rate status: 🔴 Not Started / 🟡 Partial / 🟢 Implemented
2. For each 🔴/🟡, identify the specific gap and the evidence needed to close it (policy document, RACI chart, escalation procedure, etc.)
3. Produce a prioritized remediation roadmap (Quick Wins → Medium Term → Long Term), noting that GOVERN gaps typically block progress in MAP/MEASURE/MANAGE
4. Flag whether GOVERN is "complete on paper but not operationalized" — a common gap pattern where policies exist but aren't reflected in day-to-day MAP/MEASURE/MANAGE activity (see references/rmf-profiles.md)
5. **Deliver these mini-templates in the answer itself** (fill them with the organization's specifics):
   - **AI risk policy outline** (GOVERN 1.2): 1. Purpose & scope · 2. Definitions & AI system inventory criteria · 3. Risk tolerance statement · 4. Roles & accountability (RACI) · 5. Lifecycle requirements (MAP/MEASURE/MANAGE gates per stage) · 6. Third-party AI requirements · 7. Incident response & escalation · 8. Review cadence
   - **AI governance committee charter (RACI skeleton)** (GOVERN 2.1): Accountable — executive sponsor/CAIO; Responsible — AI product owners, data science leads; Consulted — legal, privacy, security, HR for employment uses; Informed — audit, board risk committee; quorum, meeting cadence, decision rights (approve/deny deployment, accept residual risk)
   - **Risk tolerance statement examples** (GOVERN 1.3): *"We do not deploy AI that makes fully automated adverse decisions about individuals without human review"*; *"Disaggregated performance gaps above X% between demographic groups block deployment until remediated"*
   - **AI inventory minimum fields** (GOVERN 1.6): system name/owner · purpose & users · model type/provenance (built/bought/fine-tuned) · data categories · lifecycle stage · risk tier · last TEVV date

### 2. Hiring / Employment AI Risk Assessment
1. **MAP**: Document intended use (MAP 1.2), affected populations — applicants, current employees (MAP 1.4), and prohibited uses (e.g., no fully automated rejection without human review)
2. **MAP**: Build the stakeholder risk/benefit matrix (MAP 3.1) — employer efficiency benefit vs. applicant risk of disparate impact
3. **MEASURE**: Run disaggregated performance and disparate-impact-ratio testing across protected classes (MEASURE 2.2); document explainability approach for adverse decisions (MEASURE 2.3)
4. **MANAGE**: Define treatment for any subgroup below the 4/5ths threshold — retraining, human-in-the-loop review, or use restriction (MANAGE 2.1)
5. Populate the AI Risk Register (above) with one row per identified hiring-stage risk
6. Cross-reference sector considerations: EEOC, NYC Local Law 144, and EU AI Act high-risk classification for employment AI (see references/rmf-profiles.md)

### 3. Credit Scoring Risk Register
1. **MAP**: Document context of use (MAP 1.2/1.3) — loan origination, limit decisions, pricing — and legal constraints (ECOA, Fair Housing Act, EU AI Act high-risk classification)
2. **MAP**: Identify affected stakeholders and prioritize risks that are irreversible or affect a protected class (MAP 4.1)
3. **MEASURE**: Test fairness metrics (demographic parity, equalized odds, disparate impact ratio) and explainability sufficient to produce adverse-action notices (MEASURE 2.2/2.3)
4. **MANAGE**: Document treatment — model adjustment, threshold changes, or human review escalation — and residual risk acceptance by an accountable officer (MANAGE 1.3)
5. Build the risk register using the template above, with "Characteristic at Risk" typically **Fair with Harmful Bias Managed** or **Accountable & Transparent**

### 4. Incident Response (MANAGE 3)
- Trigger conditions: model accuracy degradation, bias threshold breach, adversarial attack, data drift
- Response steps: Contain → Assess impact → Notify stakeholders → Remediate → Document → Update risk register → Feed lessons learned into GOVERN (MANAGE 4.3)
- Classify severity (low/medium/high/critical) and pre-define notification thresholds: internal escalation, customer notice, regulatory disclosure

---

## AI Risk Profiles

An **AI Risk Profile** is an organization's customization of the AI RMF to reflect its specific AI use cases, applicable laws, defined risk tolerance, and the trustworthiness characteristics most relevant to its systems. The AI RMF defines two profile types:

| Profile Type | Description | Use |
|---------------|-------------|-----|
| **Current Profile** | Where the organization is today — which categories are implemented and to what degree | Baseline assessment |
| **Target Profile** | Where the organization wants to be — desired maturity for each category | Gap analysis and roadmap |

The gap between Current and Target Profile drives the risk management roadmap:

1. **Scope** — Define which AI systems are in scope (all AI, specific high-risk systems, or a single system)
2. **Assess Current State** — Rate each of the 19 categories: Not Started (0) / Partial (1) / Implemented (2) / Optimized (3)
3. **Set Target State** — Define desired maturity per category based on risk tolerance and regulatory requirements
4. **Gap Analysis** — Categories where Target > Current are gaps requiring action
5. **Prioritize** — Weight gaps by the risk they represent; address highest-risk gaps first
6. **Roadmap** — Assign owners, timelines, and resources to close each gap

NIST also uses cross-sectoral and use-case profiles as companions to the core AI RMF (for example, a Generative AI Profile addressing risks specific to generative AI systems). When a user's question concerns generative-AI-specific risk, apply the same GOVERN/MAP/MEASURE/MANAGE structure and trustworthiness characteristics above, and note explicitly that generative-AI-specific subcategory detail should be verified against the current NIST publication rather than assumed.

---

## Cross-Framework Mapping

### NIST AI RMF ↔ EU AI Act (Regulation (EU) 2024/1689)

| AI RMF Function | EU AI Act Requirement |
|------------------|------------------------|
| GOVERN 1 (AI risk policies) | Art. 9 (Risk management system) for high-risk AI |
| GOVERN 2/3 (Accountability) | Art. 16 (Obligations of high-risk AI providers), Art. 26 (Deployer obligations) |
| MAP 1 (Intended use) | Art. 9(2) — risk management must cover intended and reasonably foreseeable misuse |
| MAP 3 (Stakeholder mapping) | Art. 9(2)(b) — identification and analysis of known and foreseeable risks |
| MEASURE 2 (System evaluation) | Art. 10 (Data governance), Art. 15 (Accuracy, robustness, cybersecurity) |
| MEASURE 3 (Ongoing monitoring) | Art. 72 (Post-market monitoring), Art. 26(5) — deployer monitoring obligations |
| MANAGE 3 (Incident response) | Art. 73 (Reporting of serious incidents to market surveillance) |
| All functions | Annex IX (Technical documentation requirements for high-risk AI systems) |

**Key difference:** The EU AI Act is mandatory for in-scope providers and deployers; the NIST AI RMF is voluntary. Organizations subject to the EU AI Act should use the NIST AI RMF as the risk management methodology that satisfies Art. 9's "appropriate risk management system" requirement.

### NIST AI RMF ↔ ISO/IEC 42001:2023

| AI RMF Function/Category | ISO 42001 Equivalent |
|----------------------------|-------------------------|
| GOVERN 1 (Policies in place) | Clause 5 (Leadership), Clause 6 (Planning), A.2 (AI policy) |
| GOVERN 2 (Accountability) | Clause 5.3 (Roles and responsibilities), A.2.3 |
| GOVERN 3 (Roles) | Clause 5.3, A.2.5 (Responsibilities for AI system impact) |
| GOVERN 4 (Cross-functional teams) | Clause 7.1 (Resources), A.2.5 |
| GOVERN 5 (Risk tolerance) | Clause 6.1 (Risk and opportunity), A.5.2 (AI risk assessment) |
| MAP 1 (Context) | Clause 4 (Context of organization), A.3 (Internal/external context) |
| MAP 2 (Scientific understanding) | A.6 (AI system lifecycle) |
| MAP 3 (Stakeholder risk/benefit) | Clause 4.2 (Interested parties), A.8.4 (Impact assessment) |
| MAP 5 (Likelihood/impact) | A.5.2 (AI risk assessment methodology) |
| MEASURE 2 (System evaluation) | A.6.2 (AI system design), A.10 (Use of AI systems) |
| MEASURE 3 (Ongoing monitoring) | Clause 9.1 (Monitoring and measurement), A.6.2.5 |
| MANAGE 2 (Treatment strategies) | Clause 6.1.3 (AI risk treatment), A.5.3 |
| MANAGE 3 (Incident response) | A.9 (Performance evaluation), Clause 10 (Improvement) |
| MANAGE 4 (Review and improve) | Clause 10.2 (Nonconformity), Clause 9.3 (Management review) |

For NIST CSF 2.0 and NIST Privacy Framework mappings, sector-specific risk considerations (healthcare, financial services, HR/recruitment, criminal justice, government, education, autonomous systems), implementation tiers, and common gap patterns, read **references/rmf-profiles.md**.

---

## Reference Files

For deeper content, read these files as needed:
- **references/rmf-core.md** — All 19 categories with full subcategory descriptions and Playbook-style suggested actions for GOVERN, MAP, MEASURE, and MANAGE
- **references/rmf-profiles.md** — AI Risk Profiles, trustworthy AI metrics and indicators, sector-specific guidance, cross-framework mapping (ISO 42001, EU AI Act, NIST CSF, NIST Privacy Framework), implementation tiers, and common gap patterns

---

> *This skill provides general compliance information, not legal advice. Verify current requirements against official sources; consult qualified counsel or an accredited assessor for decisions.*

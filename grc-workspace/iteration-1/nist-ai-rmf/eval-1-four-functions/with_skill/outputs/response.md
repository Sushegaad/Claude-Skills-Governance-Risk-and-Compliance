# NIST AI RMF: The Four Core Functions and How to Get Started

The NIST AI Risk Management Framework (AI RMF 1.0) organizes AI risk management into four core functions: **GOVERN**, **MAP**, **MEASURE**, and **MANAGE**. These are not sequential phases you complete once — they are continuous, interconnected practices that together form a complete risk management system for AI throughout its lifecycle.

---

## The Four Core Functions

### 1. GOVERN — Organizational Accountability (GV-1 through GV-6)

GOVERN is the foundation. It establishes the organizational culture, policies, accountability structures, and risk tolerance that make all other AI risk management activity possible.

GOVERN answers: *Who is responsible for AI risk in this organization, and what are the rules we operate under?*

Key activities under GOVERN include:
- Formalizing an organization-wide AI Risk Management Policy signed by senior leadership (GV-1.1)
- Defining risk tolerance — for example, acceptable thresholds for false positive rates or demographic bias (GV-1.3, GV-5.1)
- Appointing accountable senior officials such as an AI Risk Owner with board-level reporting (GV-2.2)
- Assigning roles across the full AI lifecycle — design, development, deployment, and decommission — for both technical and non-technical staff (GV-3.1 through GV-3.3)
- Establishing cross-functional teams that include AI/ML, legal, privacy, security, HR, and ethics (GV-4.1)
- Aligning AI risk practices with applicable laws and regulations, such as the EU AI Act or sector-specific requirements (GV-6.1)

Without GOVERN, MAP, MEASURE, and MANAGE will lack the authority, ownership, and policy backing needed to operate consistently.

---

### 2. MAP — Risk Identification (MP-1 through MP-5)

MAP establishes context. Before you can measure or manage AI risks, you need to understand what each AI system does, who it affects, and what could go wrong.

MAP answers: *What are the risks associated with this specific AI system, and who bears them?*

Key activities under MAP include:
- Documenting each AI system's intended use, operating environment, and explicitly prohibited use cases (MP-1.2, MP-1.5)
- Identifying all affected individuals, groups, and communities — at design time, not at deployment (MP-1.4)
- Documenting training data assumptions, known limitations, and output uncertainty (MP-2.2, MP-2.3)
- Producing a stakeholder risk/benefit matrix distinguishing who benefits from the system versus who bears its risks — these are frequently different groups (MP-3.1, MP-3.3)
- Prioritizing identified risks using criteria such as severity, breadth, and reversibility (MP-4.1, MP-4.2)
- Characterizing the likelihood and impact of harms across physical, financial, psychological, and societal dimensions, including red-team exercises (MP-5.1, MP-5.2)

A well-executed MAP prevents wasting measurement and treatment resources on the wrong risks.

---

### 3. MEASURE — Risk Analysis (MS-1 through MS-4)

MEASURE translates identified risks into evidence. It employs quantitative, qualitative, and mixed-method tools to evaluate AI systems against the trustworthiness properties the framework defines — accuracy, fairness, explainability, privacy, reliability, resilience, safety, and security.

MEASURE answers: *How severe are these risks, and is our AI system performing as trustworthy as required?*

Key activities under MEASURE include:
- Defining metrics for each identified risk — for example, demographic parity and equalized odds for fairness, adversarial accuracy for robustness, SHAP/LIME scores for explainability (MS-1.1)
- Conducting pre-deployment evaluation across all trustworthiness properties, including disaggregated performance testing across demographic subgroups (MS-2.1, MS-2.2)
- Implementing post-deployment monitoring dashboards that track accuracy, fairness metrics, and input data distribution — with alert thresholds that trigger human review when performance degrades (MS-3.1, MS-3.2)
- Ensuring measurement outputs are communicated to decision-makers with uncertainty caveats included, so MANAGE can act on evidence rather than assumption (MS-4.1, MS-4.2)

MEASURE is what separates a documented risk programme from an effective one.

---

### 4. MANAGE — Risk Response (MG-1 through MG-4)

MANAGE is where risk identification and measurement translate into action. It covers treatment planning, execution, incident response, and continuous improvement.

MANAGE answers: *What are we doing about the risks we have identified and measured?*

Key activities under MANAGE include:
- Assigning a treatment owner, target date, and treatment approach for every risk register entry, with senior approval required for residual risks above the defined tolerance threshold (MG-1.1, MG-1.3)
- Selecting treatment strategies: mitigate technically (retrain the model, add human review), restrict the use case operationally, transfer risk contractually, or avoid risk entirely by not deploying (MG-2.1)
- Defining a documented emergency shutdown or human override procedure for AI systems affecting safety (MG-2.3)
- Operating an AI incident log with severity classification and defined notification thresholds for internal escalation, customer notification, and regulatory disclosure (MG-3.2, MG-3.4)
- Feeding lessons from incidents and treatment reviews back into GOVERN policy updates and MAP context documents (MG-4.3)

MANAGE closes the loop — but only if GOVERN, MAP, and MEASURE have done their work first.

---

## How the Four Functions Relate to Each Other

The functions are interdependent, not sequential. The AI RMF describes them as a continuous cycle:

```
GOVERN
  |
  |-- sets policy, accountability, and risk tolerance that authorize and constrain everything below
  |
MAP -----> MEASURE -----> MANAGE
  ^                           |
  |___________________________|
     lessons learned feed back
     into context and governance
```

Specifically:
- **GOVERN underpins all three operational functions.** Without defined risk tolerance (GV-1.3, GV-5.1), MAP cannot prioritize risks and MANAGE cannot approve residual risk acceptance. Without accountability structures (GV-2), no one owns the outputs of MAP, MEASURE, or MANAGE.
- **MAP feeds MEASURE.** You can only measure what you have identified. The risks and stakeholder impacts documented in MAP define what metrics MEASURE must track.
- **MEASURE feeds MANAGE.** MEASURE produces the evidence — metrics, evaluation results, monitoring alerts — that MANAGE acts on. Without measurement data, risk treatment is guesswork.
- **MANAGE feeds back into GOVERN and MAP.** Incident learnings (MG-3.3, MG-4.3) should update organizational policies (GOVERN) and the contextual risk understanding (MAP) for the system in question. This is the continuous improvement loop.

The framework also defines four **Implementation Tiers** that describe organizational maturity:

| Tier | Name | Description |
|------|------|-------------|
| 1 | Partial | Ad hoc practices; reactive to incidents |
| 2 | Risk Informed | Approved policies exist; not yet consistently applied |
| 3 | Repeatable | Formally documented, consistently applied, regularly reviewed |
| 4 | Adaptive | Continuously learning; proactively updates practices |

Most organizations beginning their AI journey start at Tier 1. The immediate goal for most contexts is Tier 2; regulated environments should target Tier 3.

---

## What to Implement First

**Start with GOVERN.** This is not merely because it appears first in the framework's name — it is because every other function depends on it. Attempting to run MAP assessments or MEASURE evaluations without established policies, ownership, and risk tolerance produces outputs that no one has authority to act on and no budget to resource.

A practical first-90-days sequence:

### Step 1: Stand Up GOVERN (Weeks 1–6)

These are your foundational actions before deploying or assessing any AI system:

1. **Publish an AI Risk Management Policy** signed by senior leadership that establishes AI risk as an organizational priority and defines the programme's scope (GV-1.1).
2. **Define your AI risk tolerance** — at minimum, state which categories of AI use cases are acceptable, which require additional review, and which are prohibited (GV-1.3, GV-5.1, GV-5.3).
3. **Appoint an AI Risk Owner** with clear authority, executive visibility, and cross-functional convening power (GV-2.2).
4. **Define roles** across the AI lifecycle for both technical teams (data scientists, ML engineers) and non-technical roles (business owners, legal, privacy, HR) (GV-3.1 through GV-3.3).
5. **Establish a cross-functional AI Risk Working Group** with representatives from legal, privacy, security, and the business units deploying AI (GV-4.1).
6. **Identify applicable laws and regulations** relevant to your sector and document them in a regulatory register (GV-6.1).

### Step 2: Run MAP for Each AI System (Weeks 4–10, concurrent with late GOVERN work)

For every AI system you are planning to deploy:

1. Produce an **AI System Description Document** covering: purpose, inputs, outputs, decision authority, intended and prohibited uses (MP-1.2, MP-1.5).
2. Identify **affected populations** — who makes decisions based on the system's outputs, and who those decisions affect (MP-1.4).
3. Create a **stakeholder risk/benefit matrix** distinguishing beneficiaries from those bearing risk (MP-3.1, MP-3.3).
4. **Prioritize risks** using a severity × breadth × reversibility model; flag anything affecting protected classes or with irreversible impacts as high-priority (MP-4.1, MP-4.2).

### Step 3: Apply MEASURE Before Deployment and Continuously After (Weeks 8–16)

1. Define **evaluation metrics** for the trustworthiness properties most relevant to each system — at minimum: accuracy, fairness (disaggregated by demographic subgroup), and security (MS-1.1, MS-2.2).
2. Require a **pre-deployment evaluation report** before any AI system goes live (MS-2.1).
3. Implement **post-deployment monitoring** with defined alert thresholds that trigger human review (MS-3.1, MS-3.2).

### Step 4: Activate MANAGE

1. Establish an **AI risk register** with treatment owners and target dates for every identified risk (MG-1.1).
2. Define **emergency intervention procedures** — the conditions under which a system is taken offline — for any AI system with safety implications (MG-2.3).
3. Create an **AI incident log and response process** with defined escalation paths (MG-3.2).
4. Schedule **quarterly reviews** of the full programme covering all four functions (MG-4.1).

---

## Key Principle to Carry Forward

The AI RMF is **voluntary and non-prescriptive**. It defines outcomes and practices, not a single mandated method. This means your implementation should be scaled to the risk level of the AI systems you deploy — a low-stakes internal recommendation tool requires a lighter application of the framework than an AI system making consequential decisions about individuals.

Use the **Current Profile / Target Profile** approach: for each of the 19 categories across the four functions, assess where you are today and where you need to be given your risk tolerance and regulatory context. The gap between those two profiles is your AI risk management roadmap.

| Profile Type | Purpose |
|-------------|---------|
| Current Profile | Baseline — which categories are implemented and to what degree |
| Target Profile | Desired state — where you need to be given your risk tolerance and regulatory requirements |

Begin with GOVERN. Build context through MAP. Produce evidence through MEASURE. Take action through MANAGE. Feed what you learn back into the beginning. That is the AI RMF in practice.

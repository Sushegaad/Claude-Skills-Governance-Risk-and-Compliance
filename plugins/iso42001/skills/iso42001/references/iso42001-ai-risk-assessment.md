# ISO/IEC 42001:2023 — AI Risk Assessment & AISIA Methodology

This reference covers the two mandatory assessments under Clause 6.1.2:
1. **AI Risk Assessment** — evaluates risks to the organisation from AI systems
2. **AI System Impact Assessment (AISIA)** — evaluates risks to individuals and society from AI systems

Both must be completed for every AI system in scope. Both must be maintained and updated over time.

---

## Part 1: AI Risk Assessment

### Purpose
Identify, analyse, and evaluate risks associated with AI systems so that appropriate treatment decisions can be made. This is a **risk-to-the-organisation** lens (complement to the AISIA which takes a societal/individual lens).

### Risk Assessment Framework

**Step 1: Identify AI Risks**

For each AI system in scope, identify risks across these categories:

#### Model Risks
| Risk | Description | Example |
|------|-------------|---------|
| Bias and unfairness | Model produces systematically different outputs for protected groups | Loan approval AI approves at lower rates for certain demographic groups |
| Hallucination / confabulation | Model generates plausible-sounding but incorrect outputs | LLM generates false legal citations |
| Model drift | Model performance degrades as real-world data distribution shifts | Fraud detection model misses new fraud patterns 12 months post-deployment |
| Adversarial attacks | Inputs crafted to manipulate model outputs | Adversarial examples cause image classifier to misclassify |
| Model inversion | Training data can be reconstructed from model outputs | Privacy violation — personal data extracted from model |
| Overfitting | Model performs well in testing but poorly in production | High accuracy in evaluation, low accuracy on live data |

#### Data Risks
| Risk | Description | Example |
|------|-------------|---------|
| Training data quality | Poor quality data leads to poor model performance | Incomplete labels cause systematic errors |
| Data poisoning | Attacker inserts malicious training data to manipulate model behaviour | Supply chain compromise of training dataset |
| Privacy in training data | Training data contains PII or sensitive data unlawfully | Medical data used for AI training without lawful basis |
| Data representativeness | Training data doesn't represent the deployment population | Model trained on US data deployed globally — cultural bias |
| Data provenance gaps | Origin and rights for training data unknown | Copyright or licence violations in training data |

#### Operational Risks
| Risk | Description | Example |
|------|-------------|---------|
| Unintended use | AI system used for purposes not covered by AISIA | Internal HR tool used to screen job applicants |
| System failure | AI system becomes unavailable or produces errors at scale | API outage causes customer-facing decisions to fail |
| Scope creep | AI system expanded to new use cases without re-assessment | Chatbot expanded to give medical advice without clinical review |
| Human over-reliance | Users accept AI outputs without appropriate scrutiny | Staff approve AI recommendations without verification |
| Lack of explainability | Cannot explain AI decisions to affected individuals | Automated rejection letter with no basis provided |

#### Supply Chain Risks
| Risk | Description | Example |
|------|-------------|---------|
| Third-party model risk | Pre-trained model from vendor contains bias or backdoor | Open-source LLM used without bias evaluation |
| API dependency | AI functionality depends on external API with reliability risk | Vendor changes model behaviour mid-contract |
| Vendor lock-in | Cannot switch AI provider without major operational disruption | All AI inference tied to single cloud provider |
| Third-party data handling | AI vendor handles sensitive data — data protection risk | Vendor uses customer data to retrain models without consent |

#### Regulatory and Reputational Risks
| Risk | Description | Example |
|------|-------------|---------|
| Regulatory non-compliance | AI system violates applicable law | EU AI Act high-risk AI system deployed without conformity assessment |
| Reputational harm | AI system behaviour causes public trust damage | Discriminatory AI hiring tool exposed in media |
| Liability | Organisation liable for AI system harm to individuals | AI medical diagnosis system misses condition — clinical liability |

---

### Step 2: Assess Risk Likelihood and Severity

**Likelihood scale:**
| Score | Level | Definition |
|-------|-------|-----------|
| 1 | Rare | May occur only in exceptional circumstances (<5% probability in system lifecycle) |
| 2 | Unlikely | Could occur but not expected (5–25% probability) |
| 3 | Possible | Might occur at some point (25–50% probability) |
| 4 | Likely | Will probably occur in most circumstances (50–80% probability) |
| 5 | Almost certain | Expected to occur frequently (>80% probability) |

**Severity scale:**
| Score | Level | Definition |
|-------|-------|-----------|
| 1 | Negligible | No meaningful harm; easily corrected |
| 2 | Minor | Limited impact; correctable with minor effort |
| 3 | Moderate | Significant but recoverable harm; some operational disruption |
| 4 | Major | Serious harm; difficult to reverse; significant operational or reputational impact |
| 5 | Critical | Catastrophic harm; irreversible; severe regulatory, legal, financial, or societal impact |

**Risk score = Likelihood × Severity**

**Risk rating matrix:**
```
Severity →  1-Neg  2-Minor  3-Mod  4-Major  5-Crit
Likelihood ↓
1-Rare       1       2        3       4        5
2-Unlikely   2       4        6       8       10
3-Possible   3       6        9      12       15
4-Likely     4       8       12      16       20
5-Almost     5      10       15      20       25
```

| Score range | Rating | Treatment |
|------------|--------|-----------|
| 1–4 | Low | Monitor; accept with documented rationale |
| 5–9 | Medium | Implement controls; review quarterly |
| 10–16 | High | Priority treatment required; management sign-off |
| 17–25 | Critical | Immediate treatment; may need to halt AI system until controlled |

---

### Step 3: Select Risk Treatment

For each identified risk with rating Medium or above:

| Treatment Option | When to Use | Controls to Apply |
|----------------|------------|------------------|
| **Modify the AI system** | Risk is inherent to current design | Retrain with better data, add guardrails, change architecture, implement bias mitigation |
| **Add operational controls** | Risk can be managed through process | Human review checkpoints, output filtering, monitoring, incident alerting |
| **Accept with monitoring** | Residual risk is acceptable; monitoring can detect materialisation | Document acceptance decision with senior sign-off; define alert thresholds |
| **Avoid** | Risk cannot be reduced to acceptable level | Do not deploy AI for this use case; find non-AI alternative |
| **Transfer** | Third-party better placed to manage | Contractual liability allocation; insurance; require vendor indemnification (A.10.2 Allocating responsibilities, A.10.3 Suppliers) |

---

### Step 4: Document the AI Risk Register

**Required fields per risk entry:**
```
Risk ID | AI System | Risk Category | Risk Description | Likelihood | Severity | Score | Rating | Treatment | Control(s) Applied | Residual Risk | Owner | Review Date
```

**Example entry:**
```
R-001 | Loan_Approval_Model_v2 | Model - Bias | Model may produce discriminatory outcomes for applicants by protected characteristic | 3 | 5 | 15 | High | Modify: implement fairness-aware retraining + quarterly demographic disparity monitoring | A.5.4, A.5.5, A.6.2.4, A.6.2.6 | Medium (score 6) after treatment | AI Risk Owner - Credit | Q2 2025
```

---

## Part 2: AI System Impact Assessment (AISIA)

### Purpose
The AISIA takes a **stakeholder and societal lens** — it assesses impacts on individuals, groups, and society from the AI system's outputs and decisions. This is mandatory under Clause 6.1.2 and directly referenced in Annex A.5 (controls A.5.2–A.5.5).

### When to Conduct an AISIA
- **Before initial deployment** of any AI system in scope
- **When the AI system changes** significantly (new use case, new population, new output type)
- **When operating context changes** (new regulation, new demographic affected)
- **On a scheduled review cycle** (annually recommended for medium/high impact systems)

---

### AISIA Step-by-Step Process

**Step 1: Document the AI System**
| Field | Content |
|-------|---------|
| AI system name and version | |
| AI system owner | |
| Intended purpose | What the system is designed to do |
| Output type | Decision support / Autonomous decision / Content generation / Classification / Prediction / Recommendation / Other |
| Inputs | What data is fed into the system |
| Deployment context | Where and how used — internal/customer-facing/regulatory context |
| Operating conditions | Conditions under which system is expected to perform correctly |

**Step 2: Identify Affected Populations**
| Population | How Affected | Vulnerability |
|-----------|-------------|--------------|
| Identify all groups whose rights, opportunities, or wellbeing may be affected by AI outputs | | |

Vulnerability factors: age (children/elderly), disability, socioeconomic status, minority group membership, limited AI literacy, power imbalance (employer/employee; government/citizen).

**Step 3: Assess Impact Dimensions**

For each affected population, assess:

| Dimension | Questions to Ask |
|-----------|----------------|
| **Nature of impact** | What kind of harm could occur? Financial, physical, psychological, reputational, loss of rights, discrimination? |
| **Severity** | How serious is the worst-case impact? |
| **Breadth** | How many individuals could be affected? |
| **Reversibility** | Can the harm be corrected if the AI system makes an error? |
| **Duration** | Is the impact short-term or long-lasting? |
| **Consent and awareness** | Are affected individuals aware AI is being used? Did they consent? |
| **Human oversight** | Is there a meaningful human review of AI outputs before they affect individuals? |
| **Recourse** | Can individuals challenge AI decisions? Is there an appeal process? |

**Step 4: Classify Impact Level**

| Level | Criteria | Examples |
|-------|----------|---------|
| **Low** | Limited impact; easily reversible; non-vulnerable individuals; AI is advisory only; robust human oversight | Product recommendation engine; internal productivity tool |
| **Medium** | Moderate impact; partially reversible; some vulnerable individuals may be affected; AI has significant weight in decisions | Customer service routing; content moderation; credit risk scoring with human review |
| **High** | Significant impact; hard-to-reverse; vulnerable individuals; AI drives decisions with limited human review; affects fundamental rights | Automated hiring decisions; medical diagnosis AI; benefits eligibility AI; criminal risk scoring; biometric identification |

**Step 5: Determine Control Requirements Based on Impact Level**

| Control Area | Low Impact | Medium Impact | High Impact |
|-------------|-----------|--------------|-------------|
| Transparency (A.8.2, A.8.5) | General notice that AI is used | Inform affected individuals; describe what AI does | Full disclosure; right to explanation; right to human review |
| Human oversight (A.6.2.6) | Human oversight available on request | Structured human review for edge cases | Mandatory human review of all consequential AI outputs |
| Verification & bias testing (A.6.2.4, A.7.4) | Basic performance testing | Fairness testing before deployment | Ongoing fairness monitoring with demographic breakdown |
| Documentation (A.6.2.7, A.5.3) | Technical documentation | Technical + user-facing documentation | Full model card; audit trail per decision |
| Monitoring (A.6.2.6, A.6.2.8) | Annual performance review | Quarterly monitoring | Continuous monitoring with automated alerts |
| Recourse mechanism | General complaints process | AI-specific appeal process | Formal right to challenge AI decisions; human decision-maker available |
| AISIA review cycle (A.5.2) | Every 3 years or at major change | Annually or at significant change | Every 6 months or at any change |

**Step 6: Document AISIA Findings**

**AISIA Record format:**
```
AISIA ID: AISIA-[number]
AI System: [name and version]
Assessment Date: [date]
Assessor: [name/role]
Review Date: [date]

1. AI System Description
2. Intended Purpose
3. Output Type
4. Affected Populations (table)
5. Impact Assessment (per population)
6. Impact Classification: [Low / Medium / High]
7. Controls Selected (with references to Annex A)
8. Residual Impact Assessment
9. Approval: [AI Risk Owner signature / date]
10. AISIA Review Schedule
```

---

## Part 3: Relationship Between AI Risk Assessment and AISIA

| Dimension | AI Risk Assessment | AISIA |
|-----------|-------------------|-------|
| **Primary lens** | Organisational risk | Individual and societal impact |
| **Key question** | What could go wrong for the organisation? | Who could be harmed and how? |
| **Output** | Risk register; risk treatment plan | Impact classification; control requirements |
| **Feeds into** | SoA control selection; risk treatment plan | Transparency obligations; human oversight design |
| **Mandatory** | Yes (Clause 6.1.2) | Yes (Clause 6.1.2) |
| **Repeated when** | AI system changes; annually recommended | AI system changes; on defined review cycle |

**Important:** A risk that is Low for the organisation may be High impact for individuals (e.g., an AI system with low organisational risk of failure but high impact on vulnerable individuals when it does fail). Both assessments are always required — one does not substitute for the other.

---

## Part 4: Integration with EU AI Act

ISO 42001 AISIA aligns closely with **EU AI Act Fundamental Rights Impact Assessment (FRIA)** requirements for high-risk AI systems. Organisations preparing for EU AI Act compliance can use their 42001 AISIA as a foundation — extending it to cover the specific FRIA requirements for EU high-risk AI system categories:

| EU AI Act Category | ISO 42001 AISIA Overlap |
|-------------------|------------------------|
| Biometric identification | High impact → maximum controls → maps directly |
| Critical infrastructure management | High impact |
| Education/vocational training | Medium-High impact |
| Employment and worker management | High impact (especially automated decisions) |
| Access to essential services | High impact |
| Law enforcement | High impact |
| Migration/asylum/border control | High impact |
| Justice/democratic processes | High impact |
| General purpose AI (GPAI) | A.6.2.7 technical documentation; A.8.2 and A.8.5 transparency |

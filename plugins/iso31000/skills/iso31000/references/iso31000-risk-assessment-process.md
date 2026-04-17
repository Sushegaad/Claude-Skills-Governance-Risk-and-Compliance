# ISO 31000:2018 — Risk Assessment Process (Clause 6)

This reference covers the detailed risk management process defined in Clause 6 of
ISO 31000:2018 — from establishing scope, context, and criteria (6.3) through risk
identification (6.4.2), risk analysis (6.4.3), and risk evaluation (6.4.4).

---

## Clause 6.3 — Scope, Context, and Criteria

Before any risk assessment begins, three foundation inputs must be defined.

### Scope Definition

The scope sets the boundary for the risk assessment. Define:

| Scope Element | Questions to Answer |
|--------------|-------------------|
| **Organisational boundary** | Which divisions, sites, or business units are included? |
| **Process boundary** | Which processes, systems, or projects are in scope? |
| **Time horizon** | Short-term (12 months)? Medium (3 years)? Long-term (5+ years)? |
| **Risk types** | All risk categories? Or specific types (e.g., cyber, financial, operational only)? |
| **Stakeholder universe** | Who has an interest in or influence over the risks in scope? |

**Scope statement template:**
> "This risk assessment covers [process/project/division] within [organisation name]
> for the period [start date] to [end date]. It encompasses risks of type [categories]
> that could affect the achievement of [specific objectives]. Out of scope: [explicit exclusions]."

### Context Setting

#### External Context — PESTLE Analysis Template

| Factor | Risk Source / Issue | Potential Impact on Objectives | Current Controls |
|--------|--------------------|---------------------------------|-----------------|
| Political | | | |
| Economic | | | |
| Social | | | |
| Technological | | | |
| Legal / Regulatory | | | |
| Environmental | | | |

#### Internal Context — Key Questions
1. What are the organisation's strategic objectives? (Risks are threats/opportunities to these)
2. What are the organisation's core capabilities and key dependencies?
3. What is the risk culture — risk-averse, risk-neutral, or risk-seeking?
4. What are the existing governance and control structures?
5. What internal constraints exist (budget, resourcing, regulatory obligations)?
6. What are the organisation's key performance indicators that risk events could disrupt?

### Criteria Definition

Risk criteria must be agreed before scoring begins to ensure consistency.

#### Likelihood Scale

| Score | Label | Definition | Example Frequency |
|-------|-------|-----------|------------------|
| 5 | Almost Certain | Expected to occur in most circumstances | Several times per year |
| 4 | Likely | Will probably occur in most circumstances | Once per year or more |
| 3 | Possible | Might occur at some time | Every 2–5 years |
| 2 | Unlikely | Could occur at some time | Every 5–10 years |
| 1 | Rare | May only occur in exceptional circumstances | Less than once per 10 years |

#### Consequence Scale

Calibrate consequence descriptors to the organisation's size, sector, and objectives.

| Score | Label | Financial | Reputational | Operational | Regulatory / Legal |
|-------|-------|-----------|-------------|-------------|--------------------|
| 5 | Catastrophic | Loss > 20% annual revenue / insolvency risk | National/international media; long-term brand damage | Complete cessation of operations | Criminal prosecution; licence revocation |
| 4 | Major | Loss 5–20% annual revenue | Significant national media; sustained negative coverage | Major disruption > 1 week | Regulatory enforcement action; significant fines |
| 3 | Moderate | Loss 1–5% annual revenue | Regional media; sector-level notice | Disruption 1–7 days | Formal regulatory warning; investigation |
| 2 | Minor | Loss 0.1–1% annual revenue | Limited local coverage; manageable | Disruption < 24 hours | Compliance breach; informal regulatory notice |
| 1 | Negligible | Loss < 0.1% annual revenue | No media coverage; internal reputational impact | Temporary inconvenience | Minor procedural non-compliance |

#### Risk Tolerance Thresholds (example — adjust to match organisational appetite)

| Score Range | Risk Band | Default Treatment Decision |
|------------|-----------|---------------------------|
| 15–25 | 🔴 Critical | Mandatory treatment; escalate to executive/board immediately |
| 10–14 | 🟠 High | Treatment plan required within 30 days; monthly monitoring |
| 5–9 | 🟡 Medium | Treatment plan required within 90 days; quarterly monitoring |
| 1–4 | 🟢 Low | Accept with monitoring; annual review |

---

## Clause 6.4.2 — Risk Identification

The goal is to identify **all sources of risk** — both threats (negative outcomes) and
opportunities (positive outcomes) — that could affect the achievement of objectives.

### Risk Identification Techniques

#### 1. Structured Workshop / Brainstorming

**Best for:** Initial identification; diverse team input; new risk domains.

**Facilitation prompt sequence:**
1. "What events or circumstances could prevent us from achieving [objective X]?"
2. "What incidents have occurred before in this organisation or sector?"
3. "What has changed recently that introduces new risk?" (regulatory, market, technology)
4. "What assumptions are we making that could prove wrong?"
5. "Where are our biggest dependencies — what happens if they fail?"

#### 2. SWOT Analysis for Risk Identification

| | Positive | Negative |
|--|----------|---------|
| **Internal** | **Strengths** (what we can exploit) | **Weaknesses** (internal vulnerabilities) |
| **External** | **Opportunities** (upside risks to pursue) | **Threats** (external threats to address) |

#### 3. Process Mapping / SIPOC

Mapping processes reveals risk at each step:

| Suppliers | Inputs | Process | Outputs | Customers |
|-----------|--------|---------|---------|-----------|
| Who/what provides inputs? | What enters the process? | What happens? | What exits? | Who receives outputs? |
| **Risk:** Supplier failure | **Risk:** Poor quality inputs | **Risk:** Process failure, human error | **Risk:** Non-conforming outputs | **Risk:** Customer/stakeholder dissatisfaction |

#### 4. Bowtie Analysis

Bowtie is excellent for complex risks with multiple causation paths and consequence scenarios:

```
Cause 1 ──┐
Cause 2 ──┤── [Preventive Controls] ──► RISK EVENT ──► [Recovery Controls] ──┬── Consequence A
Cause 3 ──┘                                                                    ├── Consequence B
                                                                               └── Consequence C
```

- **Left side (threats):** Root causes and preventive controls
- **Centre:** The undesired risk event (the "top event")
- **Right side (consequences):** Impacts and recovery/mitigation controls

#### 5. FMEA — Failure Mode and Effects Analysis

Best for operational, product, or process failure risks:

| Process Step | Failure Mode | Effect of Failure | Severity (1–10) | Occurrence (1–10) | Detection (1–10) | RPN = S×O×D | Recommended Action |
|-------------|-------------|------------------|----------------|------------------|-----------------|-------------|-------------------|

RPN = Risk Priority Number. Score > 100 typically requires action.

#### 6. Taxonomy-Based Risk Checklist

Run through standard risk category checklists to avoid blind spots:

**Strategic risks:** Market position, competitor action, strategic misalignment, M&A integration,
key leadership departure, innovation failure, investor relations

**Financial risks:** Liquidity, credit, currency, interest rate, tax, insurance gap,
budget overrun, fraud, treasury management

**Operational risks:** Process failure, human error, system downtime, quality defects,
supply chain disruption, facilities damage, health and safety

**Technology / Cyber risks:** Ransomware, data breach, system availability, legacy
technology debt, software vulnerability, shadow IT, vendor security failure

**Compliance / Regulatory risks:** Regulatory change, non-compliance with licence conditions,
data protection breach, employment law, environmental obligation, product liability

**Reputational risks:** Media/social media exposure, whistleblower incidents, ESG
performance, executive misconduct, product recall, customer complaint surge

**People / HR risks:** Key person dependency, skills shortage, industrial action,
succession failure, workplace culture (harassment, discrimination)

**Third party / Supply chain risks:** Single-source dependency, supplier insolvency,
outsourced service failure, geopolitical supply disruption, counterparty default

### Risk Description Template

For each identified risk:

```
Risk ID:          [Unique reference, e.g. R-001]
Risk Category:    [Strategic / Financial / Operational / Cyber / Compliance / etc.]
Risk Description: [Clear plain-language statement: "The risk that [X] occurs, caused by [Y],
                   resulting in [Z]."]
Risk Source:      [Root cause or triggering event]
Existing Controls:[Controls currently in place to manage this risk]
Risk Owner:       [Named individual accountable for managing this risk]
Date Identified:  [Date]
```

### Risk Register Template (Full)

| Risk ID | Category | Risk Description | Risk Source | Existing Controls | Inherent L (1–5) | Inherent C (1–5) | Inherent Score | Control Effectiveness | Residual L | Residual C | Residual Score | Band 🔴🟠🟡🟢 | Treatment Option | Owner | Target Date | Review Date | Status |
|---------|---------|-----------------|-------------|------------------|---------|---------|----------|-----------|-----------|-----------|---------|------|------|------|---------|-------------|------|

---

## Clause 6.4.3 — Risk Analysis

Risk analysis determines the level of risk to enable evaluation and treatment prioritisation.

### 5×5 Likelihood × Consequence Matrix

```
Consequence →
         1-Negligible  2-Minor  3-Moderate  4-Major  5-Catastrophic
    5      5          10        15          20         25   🔴
L   4      4           8        12          16 🔴      20   🔴
i   3      3           6         9🟡        12 🟠      15   🔴
k   2      2           4         6🟡         8🟡       10   🟠
e   1      1           2         3🟢         4🟢        5   🟡
l
```

Legend:
- 🔴 Critical (15–25): Escalate immediately; mandatory treatment
- 🟠 High (10–12): Treatment plan within 30 days
- 🟡 Medium (5–9): Treatment plan within 90 days
- 🟢 Low (1–4): Accept; monitor annually

### Inherent vs Residual Risk

| Term | Definition | When Used |
|------|-----------|-----------|
| **Inherent risk** | Raw risk score BEFORE any controls are applied | Understand worst-case exposure |
| **Control effectiveness** | Assessment of how well existing controls reduce likelihood and/or consequence | Evaluate adequacy of current controls (Effective / Partially Effective / Ineffective) |
| **Residual risk** | Risk level AFTER existing controls are applied | The actual risk exposure; decision point for further treatment |
| **Target residual risk** | The desired risk level after treatment is implemented | The goal for the risk treatment plan |

### Qualitative vs Quantitative Analysis

| Approach | When to Use | Methods |
|----------|------------|---------|
| **Qualitative** (1–5 scales) | Most risks; initial assessments; limited data | L×C matrix, expert judgment, workshops |
| **Semi-quantitative** | Financial risks; risks with some historical data | Loss exposure ranges linked to consequence scores |
| **Quantitative** | High-value risks; financial modelling; insurance | Monte Carlo simulation, Value at Risk (VaR), Expected Loss |

### Multi-Dimensional Analysis

For complex risks, analyse across multiple consequence dimensions:

| Risk | Financial Impact | Operational Impact | Reputational Impact | Regulatory Impact | Composite Score |
|------|----------------|------------------|--------------------|--------------------|----------------|
| [Risk 1] | 3 | 4 | 2 | 3 | 3.0 (avg) |

Use the **highest single dimension** as the consequence score (not the average) — this is
the conservative approach recommended by most risk practitioners.

---

## Clause 6.4.4 — Risk Evaluation

Risk evaluation determines which risks require treatment, what priority, and what form of
treatment is appropriate.

### Evaluation Steps

1. **Compare residual risk score to risk criteria:** Is the residual risk within the
   organisation's defined tolerance thresholds?

2. **Apply the treatment decision rule:**

   | Residual Score | Band | Decision |
   |---------------|------|----------|
   | ≥ 15 | 🔴 Critical | Must treat — escalate to board/executive; treatment plan mandatory |
   | 10–14 | 🟠 High | Must treat — risk treatment plan within 30 days |
   | 5–9 | 🟡 Medium | Should treat — risk treatment plan within 90 days |
   | 1–4 | 🟢 Low | Accept — periodic review; document acceptance decision |

3. **Prioritise treatment order:** Where multiple high/critical risks exist:
   - First: Risks that exceed risk appetite by the greatest margin
   - Second: Risks with the highest consequence (catastrophic impact even if low likelihood)
   - Third: Risks with highest strategic relevance to organisational objectives

4. **Document the evaluation rationale:** For any risk that is accepted, record:
   - Why the risk is accepted (cost of treatment vs. residual risk level)
   - Who authorised acceptance (must be at appropriate seniority level)
   - Review date for the acceptance decision

### Risk Evaluation Output: Prioritised Risk Summary

| Priority | Risk ID | Risk Description | Residual Score | Band | Recommended Treatment | Owner |
|----------|---------|----------------|---------------|------|-----------------------|-------|
| 1 | R-007 | [Description] | 20 | 🔴 | Avoid or Reduce — immediate action | [Name] |
| 2 | R-003 | [Description] | 16 | 🔴 | Reduce — treatment plan this month | [Name] |
| 3 | R-011 | [Description] | 12 | 🟠 | Transfer (insure) + Reduce controls | [Name] |

---

## Communication and Consultation (Clause 6.2) — Running Thread

Communication and consultation are not a one-time step — they run throughout the entire
risk management process.

### Stakeholder Consultation Plan

| Stakeholder Group | Interest in Risk | Engagement Method | Frequency |
|-------------------|-----------------|------------------|-----------|
| Board / Oversight body | Overall risk exposure and appetite | Risk report at board meeting | Quarterly |
| Executive team | Strategic and operational risk status | Risk dashboard + narrative | Monthly |
| Process owners | Risks within their area of responsibility | Risk assessment workshops | Quarterly |
| All staff | Awareness of operational risks and controls | Training; intranet updates | Annually + ad hoc |
| External auditors | Risk register accuracy and control adequacy | Audit file + interviews | Annual audit cycle |
| Regulators | Material risks that may affect regulatory obligations | Mandatory disclosures as required | Per regulation |

### Internal Risk Reporting Schedule

| Report | Audience | Frequency | Contents |
|--------|---------|-----------|---------|
| Risk Register | CRO / Risk function | Ongoing / real-time | Full risk inventory |
| Risk Dashboard | Executive team | Monthly | Top 10 risks; RAG status; treatment progress |
| Board Risk Report | Board / oversight committee | Quarterly | Risk appetite status; critical risks; emerging risks |
| Annual Risk Report | All stakeholders | Annually | Full risk review; framework evaluation; year-ahead outlook |
| Incident / Near-miss report | CRO + relevant exec | Within 48 hours | Nature of event; potential risk implication; immediate response |

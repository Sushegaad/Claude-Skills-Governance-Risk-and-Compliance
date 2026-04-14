# ISO 31000:2018 — Risk Treatment, Appetite, and Monitoring (Clauses 6.5–6.7)

This reference covers risk treatment (Clause 6.5), risk appetite and tolerance frameworks
(supporting Clause 6.3 criteria), monitoring and review (Clause 6.6), and recording and
reporting (Clause 6.7).

---

## Clause 6.5 — Risk Treatment

Risk treatment modifies risk. For **threat risks**, treatment reduces either likelihood,
consequence, or both. For **opportunity risks**, treatment increases the probability of the
beneficial outcome.

### Treatment Options — Full Reference

#### 1. Avoid (Eliminate)
Stop the activity that gives rise to the risk, or change the way the objective is achieved.

**When to use:**
- The risk score remains critical even after realistic control investment
- The cost and consequence of an event far outweigh the benefits of the activity
- A less risky path to the same objective exists

**Examples:**
- Withdraw from a high-risk market or jurisdiction
- Retire a legacy IT system that cannot be adequately secured
- Decline a contract where liability exposure is unacceptable
- Discontinue a product line with unresolvable safety risks

**Considerations:** Avoidance may mean foregoing opportunity / revenue. Always assess
whether the upside being avoided is significant.

#### 2. Reduce (Mitigate)
Implement controls that reduce likelihood of the risk occurring, reduce the severity of
consequences if it does occur, or both.

**Preventive controls (reduce likelihood):**
- Staff training and competency programmes
- Process controls and standard operating procedures (SOPs)
- Preventive maintenance programmes
- Access controls and authorisation requirements
- Supplier qualification and monitoring
- Redundancy / failover systems

**Detective controls (early warning / limit consequence):**
- Monitoring and alert systems
- Internal audit and assurance activities
- KPI dashboards and trend analysis
- Exception reporting and escalation triggers
- Testing and scenario exercises (fire drills, business continuity tests)

**Recovery controls (reduce consequences after event):**
- Business Continuity Plans (BCPs)
- Disaster Recovery Plans (DRPs)
- Crisis Communications Plans
- Insurance coverage
- Data backup and restore procedures

**Control effectiveness assessment:**

| Rating | Description |
|--------|-------------|
| **Effective** | Control operates as designed; evidence of routine operation; tested and verified |
| **Partially Effective** | Control exists but has gaps: not consistently applied, not tested, or provides partial coverage |
| **Ineffective** | Control exists on paper but is not operating; or no control present |

#### 3. Transfer (Share)
Shift the financial or operational burden of risk consequence to a third party.

**Mechanisms:**
| Transfer Mechanism | How It Works | Best For |
|------------------|----|---------|
| **Insurance** | Premium paid; insurer covers defined losses | Property, liability, cyber, professional indemnity |
| **Contractual transfer** | Indemnification clauses, warranties, limitation of liability | Supplier contracts, outsourcing agreements, SLAs |
| **Joint ventures / shared ownership** | Risk shared across partners | Capital-intensive projects; markets with political risk |
| **Derivatives / hedging** | Financial instruments to offset currency/commodity risk | Financial and commodity risk |

**Important limitations of transfer:**
- Transfer removes financial exposure but NOT operational or reputational risk
- Responsibility and accountability (regulatory, ethical) cannot be transferred
- Insurance may not cover the full loss (deductibles, exclusions, policy limits)
- Contractual transfer is only as good as the counter-party's ability to pay

#### 4. Accept (Retain)
Make an informed decision to bear the risk without additional treatment.

**When to use:**
- The residual risk score is within the organisation's defined appetite
- The cost of treatment exceeds the expected value of the risk reduction
- The risk is so remote (Rare × Negligible) that treatment is not warranted

**Requirements for risk acceptance:**
- Documented acceptance decision (not a default / unaware acceptance)
- Acceptance authorised at appropriate seniority (see RACI):
  - 🟢 Low → Process owner may accept
  - 🟡 Medium → Department head / line manager must accept
  - 🟠 High → Senior executive / CRO must accept and document rationale
  - 🔴 Critical → Board / CEO acceptance required; review every quarter
- Defined review date — acceptance decisions must be periodically re-evaluated
- Contingency plans in place for accepted risks above 🟡 Medium

#### 5. Exploit (for opportunity risks)
Actively pursue a risk to maximise the probability of a beneficial outcome.

**Examples:**
- Fast-follow strategy in a new market where competitor risk is the "opportunity"
- Investing in AI capability ahead of regulatory clarification (opportunity = first-mover)
- Acquiring a distressed competitor

---

### Risk Treatment Plan — Full Template

```
RISK TREATMENT PLAN

Risk ID:              [e.g. R-007]
Risk Description:     [Plain-language description of the risk]
Risk Category:        [Strategic / Operational / Financial / Cyber / Compliance / etc.]
Current Residual Risk: Likelihood [1-5] × Consequence [1-5] = Score [___] Band [🔴🟠🟡🟢]
Treatment Option:     [Avoid / Reduce / Transfer / Accept / Exploit]

TARGET RESIDUAL RISK (after treatment):
  Likelihood:   [Target L]
  Consequence:  [Target C]
  Target Score: [Target Score]  Target Band: [🟢🟡🟠]

TREATMENT ACTIONS:

| # | Action | Description | Owner | Resources Required | Due Date | Status |
|---|--------|-------------|-------|-------------------|---------|--------|
| 1 | | | | | | Not Started |
| 2 | | | | | | Not Started |
| 3 | | | | | | Not Started |

SUCCESS MEASURES / KPIs:
  [How will effectiveness of treatment be measured? What evidence will confirm the
   target residual risk has been achieved?]

REVIEW DATE:          [Date when treatment plan progress will next be formally reviewed]
PLAN OWNER:           [Named senior owner accountable for treatment completion]
APPROVED BY:          [Name and title]
APPROVAL DATE:        [Date]
```

---

### Treatment Selection Decision Framework

When selecting a treatment, consider:

1. **Is the residual risk within appetite?**
   - Yes → Consider Accept (with documented decision)
   - No → Proceed to treatment selection

2. **Can the risk source be eliminated?**
   - Yes, without major business impact → Consider Avoid
   - No, or avoidance sacrifices critical objectives → Continue

3. **Is there a cost-effective way to reduce likelihood or consequence?**
   - Yes → Reduce (identify specific preventive/detective/recovery controls)
   - No (treatment cost > Expected risk value) → Consider Transfer or Accept

4. **Can the financial exposure be transferred?**
   - Insurable risk → Transfer (insurance)
   - Contractually assignable → Transfer (contractual mechanisms)

5. **Is the risk within appetite even without further treatment?**
   - Yes → Accept with documented rationale
   - No → Escalate for management decision; consider business case for avoidance

---

## Risk Appetite Framework

### Definitions

| Term | Definition |
|------|-----------|
| **Risk appetite** | The amount and type of risk the organisation is willing to take in pursuit of its objectives |
| **Risk tolerance** | The organisation's readiness to bear the risk AFTER treatment (i.e., the maximum acceptable residual risk level) |
| **Risk capacity** | The maximum risk the organisation can absorb before viability is threatened |
| **Risk attitude** | The organisation's approach to risk — risk-averse, risk-neutral, or risk-seeking |

**Key relationship:** Appetite ≤ Tolerance ≤ Capacity

### Risk Appetite Statement Structure

A risk appetite statement should contain:

1. **Overarching appetite narrative** — a single statement summarising the organisation's
   general relationship with risk in the context of its strategy

2. **Category-level appetite statements** — specific statements for each major risk category

3. **Tolerance thresholds** — the maximum residual risk score that triggers mandatory
   escalation or treatment (linked to the risk scoring scale)

4. **Boundaries (zero-tolerance areas)** — risk types the organisation will not accept
   under any circumstances (e.g., deliberate regulatory breach, health and safety
   violations, fraud)

### Risk Appetite Statement Template

---
**[Organisation Name] Risk Appetite Statement**
**Version:** [X.X] | **Approved By:** [Name, Title] | **Date:** [Date] | **Review:** [Date]

**Overarching Statement:**
> [Organisation name] pursues its strategic objectives with a [low/moderate/measured] 
> overall risk appetite. We accept calculated risks that support growth, innovation, and
> value creation, while maintaining zero tolerance for risks that threaten the safety of
> our people, the integrity of our compliance obligations, or the security of our customers'
> data.

**Category Appetites:**

| Risk Category | Appetite Level | Tolerance Threshold (max residual score) | Zero-Tolerance Triggers |
|--------------|---------------|----------------------------------------|------------------------|
| **Strategic** | Moderate | 12 (🟠 High) | Reputational catastrophe; insolvency risk |
| **Financial** | Conservative | 9 (🟡 Medium) | Unexpected loss > [X]% revenue |
| **Operational** | Low–Moderate | 9 (🟡 Medium) | Safety incident; major service failure |
| **Cyber / Technology** | Low | 8 (🟡 Medium) | Breach of customer PII; material data loss |
| **Compliance / Regulatory** | Very Low | 5 (🟡 Medium) | Any deliberate non-compliance; criminal breach |
| **Reputational** | Low | 8 (🟡 Medium) | Sustained media / public reputational damage |
| **Environmental / ESG** | Low | 6 (🟡 Medium) | Environmental incident; ESG disclosure failure |
| **People / HR** | Low–Moderate | 9 (🟡 Medium) | Workplace safety failure; key person loss cascade |

**Approval and Review:** This statement is approved by [Board / CEO] and reviewed annually
or when the strategic context materially changes.

---

### Using Risk Appetite in Practice

1. **Risk assessment gate:** After scoring each risk, compare residual score against the
   relevant appetite band. Any risk exceeding the tolerance threshold must have a
   treatment plan.

2. **Investment decisions:** New projects / initiatives include a risk statement confirming
   that the risk profile is within appetite. Decisions outside appetite require explicit
   board/executive sign-off.

3. **Escalation trigger:** When a risk is identified or an event occurs that breaches the
   tolerance threshold, the escalation path (from the appetite statement) is activated
   automatically.

4. **Annual review:** The board reviews the appetite statement annually. Changes in
   strategy, regulation, or risk environment may shift appetite levels.

---

## Clause 6.6 — Monitoring and Review

Monitoring ensures that risk controls remain effective and that the risk picture (likelihood,
consequence) keeps pace with changes in context.

### Monitoring Schedule

| Activity | Frequency | Owner | Output |
|----------|-----------|-------|--------|
| Risk register review | Quarterly | CRO / Risk Lead | Updated risk register |
| Control effectiveness testing | Annually (or event-driven) | Risk Owner + Internal Audit | Control effectiveness ratings updated |
| Board risk reporting | Quarterly | CRO | Board risk report |
| Executive risk dashboard | Monthly | CRO | Risk dashboard update |
| Full risk reassessment | Annually (+ after major changes) | Risk Lead + Process Owners | Refreshed risk register |
| Incident / near-miss review | Within 48 hours of event | CRO + relevant Process Owner | Incident report; risk register update |

### Monitoring Triggers — Event-Driven Review

Risk reassessment should be initiated whenever:
- A material strategic change occurs (M&A, new market, restructure)
- A significant regulatory or legal change is announced
- A risk event or near-miss occurs
- A new technology is adopted (especially AI, cloud, OT)
- A key control fails or is found to be ineffective
- An external audit raises risk-related findings
- A material supplier or business partner incident occurs
- Insurance renewal or claims review identifies new exposures

### Control Testing Programme

| Control | Test Method | Frequency | Evidence |
|---------|------------|-----------|---------|
| Access controls | Privileged access review; user access review | Quarterly | Access log; review sign-off |
| Business continuity plan | Tabletop exercise; full DR test | Annually | Test report; lessons learned |
| Supplier risk controls | Supplier questionnaires; on-site audits | Annually / per contract cycle | Audit report; SLA performance data |
| Financial controls | Internal audit; reconciliation sign-off | Monthly / per financial cycle | Audit findings; reconciliation records |
| Compliance controls | Regulatory self-assessment; external audit | Annually | SAQ; external audit report |

---

## Clause 6.7 — Recording and Reporting

Documented records are required to support decision-making, demonstrate due diligence,
support learning, and fulfil accountability obligations.

### Required Records

| Record | Purpose | Minimum Retention |
|--------|---------|------------------|
| **Risk Register** | Inventory of all identified risks with current scores | Rolling; current version always maintained |
| **Risk Assessment Reports** | Evidence of risk identification, analysis, and evaluation | 5 years (or as required by sector regulation) |
| **Risk Treatment Plans** | Documented treatment decisions and progress | Duration of treatment + 3 years |
| **Risk Acceptance Decisions** | Evidence of informed acceptance of risks above appetite | 5 years |
| **Board Risk Reports** | Governance evidence; oversight record | 7 years (board records retention standard) |
| **Control Testing Records** | Evidence of control effectiveness | 3 years |
| **Incident / Near-Miss Log** | Event record; input to risk register updates | 5 years |
| **Framework Evaluation Records** | Evidence of continual improvement | 3 years |
| **Risk Appetite Statement** | Authoritative appetite positions | Current version; all superseded versions 5 years |

### Risk Reporting Formats

#### 1. Board Risk Report (Quarterly)
Contents:
- Executive summary: overall risk position vs. appetite
- Top 10 risks — heatmap and narrative
- New / emerging risks identified this quarter
- Risk treatment plan progress (% complete; overdue actions)
- Incidents / near-misses with risk register implications
- Risks closed / downgraded this quarter
- Proposed changes to risk appetite or criteria (if any)
- Outlook: anticipated risk changes next quarter

#### 2. Risk Dashboard (Monthly — Executive)
A single-page summary:
- Heatmap: current top risks by residual score
- RAG status change indicators (↑ risk increased, ↓ decreased, → stable)
- Treatment plan actions: On track / At risk / Overdue
- New risks added since last dashboard
- Risk KPI scorecard (see KPIs in framework reference)

#### 3. Risk Register Summary (Process Owner Level)
- Risks relevant to the process owner's area only
- Residual scores, treatment actions with their due dates
- Controls assigned to the process owner for monitoring

### Risk Communication Best Practices

1. **Tailor the message to the audience:**
   - Board: strategic risk picture, appetite alignment, material exposures
   - Executive: operational risk status, treatment progress, resource needs
   - Process owners: their specific risks and control responsibilities
   - Staff: risk awareness — not the full register

2. **Use consistent risk language:** Ensure all stakeholders use the same likelihood and
   consequence definitions. Provide a reference card.

3. **Avoid risk register overload:** A board should see 10–15 top risks, not 150.
   Filter to what is material and decision-relevant.

4. **Show trend, not just status:** Use directional indicators to show whether the risk
   profile is improving, stable, or deteriorating.

5. **Connect risk to objectives:** Frame risk language in terms of strategic or operational
   objectives, not just controls and scores. E.g., "The risk of market share loss through
   competitor disruption remains HIGH — this directly threatens Objective 3: revenue growth."

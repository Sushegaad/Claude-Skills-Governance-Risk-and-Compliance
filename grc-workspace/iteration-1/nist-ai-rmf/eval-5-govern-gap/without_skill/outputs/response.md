# NIST AI RMF GOVERN Gap Assessment

**Assessment Date:** 2026-04-25
**Framework:** NIST AI Risk Management Framework (AI RMF 1.0) — GOVERN Function

---

## Executive Summary

This assessment evaluates your organization's current posture against the GOVERN function of the NIST AI RMF. The GOVERN function establishes the policies, processes, procedures, and practices that enable AI risk management across the organization. Based on the information provided — an AI ethics statement exists, but no formal AI risk policy, no cross-functional AI team, no defined risk tolerance for AI, and no legal involvement in AI deployments — your organization has foundational awareness but significant structural gaps.

**Overall GOVERN Maturity: Low (Level 1 of 4)**

---

## GOVERN Category Ratings

The NIST AI RMF GOVERN function contains six subcategories (GV.1 through GV.6). Each is rated below on a four-point scale:

- **4 — Optimizing:** Processes are mature, measured, and continuously improved
- **3 — Defined:** Formal processes are documented and consistently followed
- **2 — Developing:** Some practices exist but are informal or inconsistent
- **1 — Initial:** Little to no formal practice; ad hoc or absent

---

### GV.1 — Organizational Policies, Processes, Procedures, and Practices for AI Risk Management

**Rating: 2 — Developing**

**What exists:** An AI ethics statement is in place, which demonstrates organizational intent and leadership awareness of AI-related concerns. This is a meaningful starting point.

**Gaps identified:**
- No formal AI risk management policy exists. The ethics statement sets aspirational values but does not create enforceable obligations or operational procedures.
- There is no defined process for how AI risk is identified, escalated, or resolved.
- No procedures govern the AI system lifecycle (development, procurement, deployment, retirement).
- No governance body (board, committee, or executive owner) has been formally assigned accountability for AI risk.

**Impact:** Without a formal policy, risk management activities are discretionary and inconsistent. Teams cannot make reliable decisions about acceptable AI uses or required controls.

---

### GV.2 — Accountability Mechanisms for AI Risk Management

**Rating: 1 — Initial**

**What exists:** Nothing formal has been identified.

**Gaps identified:**
- No cross-functional AI team or governance committee exists to own AI risk decisions.
- Accountability for AI deployments appears to reside informally with individual teams or business units, creating siloed decision-making.
- No roles and responsibilities (RACI matrix or equivalent) have been defined for AI risk management.
- There is no mechanism for escalating AI-related concerns to leadership.
- No audit or review process exists to verify that AI systems are being managed appropriately.

**Impact:** Without clear accountability, AI risk management cannot be executed consistently. Gaps are likely to go unidentified until an incident occurs.

---

### GV.3 — Organizational Teams Are Committed to Transparency and Accountability

**Rating: 2 — Developing**

**What exists:** The AI ethics statement implies a commitment to ethical behavior, which touches on transparency and accountability values.

**Gaps identified:**
- Transparency commitments are stated in the ethics document but are not operationalized. There are no disclosure requirements, documentation standards, or explainability requirements for AI systems.
- No formal process exists for documenting AI system decisions, design choices, or risk trade-offs.
- There is no mechanism for affected parties (employees, customers) to raise concerns about AI system behavior.
- Legal team non-involvement means that legal obligations around transparency (consumer protection, regulatory disclosure) are not being assessed.

**Impact:** The gap between stated values and operational practice creates legal and reputational exposure, particularly as AI-specific regulations mature globally.

---

### GV.4 — Organizational Teams Are Committed to Diversity, Equity, Inclusion, and Accessibility (DEIA) in AI

**Rating: 1 — Initial**

**What exists:** The ethics statement may reference fairness or non-discrimination, but no operational DEIA controls for AI have been identified.

**Gaps identified:**
- No process exists to assess AI systems for bias, disparate impact, or accessibility limitations.
- No diversity requirements exist for AI development teams or governance bodies.
- No mechanisms for monitoring AI outputs for discriminatory patterns have been established.
- Legal non-involvement means fair lending, equal opportunity, and anti-discrimination obligations are not being factored into AI deployments.

**Impact:** Unmitigated bias in AI systems creates regulatory liability (under equal opportunity, consumer protection, and emerging AI laws) and direct harm to affected populations.

---

### GV.5 — Organizational Risk Tolerance for AI Is Established

**Rating: 1 — Initial**

**What exists:** Nothing. No risk tolerance for AI has been defined.

**Gaps identified:**
- There is no formal statement of what level of AI risk the organization is willing to accept in pursuit of business objectives.
- No criteria exist for categorizing AI use cases by risk level (high/medium/low).
- Without risk tolerance, there is no basis for deciding which AI systems require enhanced controls, independent review, or executive approval before deployment.
- No process exists to align AI risk appetite with the organization's broader enterprise risk management framework.

**Impact:** This is the most fundamental gap. Risk tolerance is the foundation on which all other AI risk controls are calibrated. Its absence means the organization cannot make principled, defensible decisions about AI deployment.

---

### GV.6 — Policies and Procedures for AI Risk Management Incorporate Legal Requirements

**Rating: 1 — Initial**

**What exists:** Nothing. Legal is not involved in AI deployments.

**Gaps identified:**
- Legal, compliance, and privacy functions are not part of the AI deployment process.
- No review process exists to assess whether an AI use case triggers applicable laws or regulations (e.g., EU AI Act, state AI laws, sector-specific regulations, data protection law).
- Contractual obligations to third parties regarding AI use (in vendor agreements, customer terms) are not being evaluated.
- Intellectual property considerations for AI-generated outputs are not being assessed.
- No process exists for monitoring changes in the AI regulatory environment.

**Impact:** This gap creates direct legal liability. As AI-specific regulation accelerates globally and across US states, organizations without legal involvement in AI are likely to find themselves non-compliant with enforceable obligations.

---

## Summary Ratings Table

| GOVERN Category | Description | Rating | Score |
|---|---|---|---|
| GV.1 | Organizational AI Risk Policies | Developing | 2/4 |
| GV.2 | Accountability Mechanisms | Initial | 1/4 |
| GV.3 | Transparency and Accountability Commitment | Developing | 2/4 |
| GV.4 | DEIA in AI | Initial | 1/4 |
| GV.5 | AI Risk Tolerance | Initial | 1/4 |
| GV.6 | Legal Requirements Integration | Initial | 1/4 |
| **Overall** | | **Initial** | **1.3/4** |

---

## Prioritised Remediation Plan

Remediation items are sequenced by: (1) foundational dependency — some items unlock others; (2) risk exposure — items that create legal liability or enable the next worst-case scenario are prioritized; (3) effort relative to impact.

---

### Priority 1 — Immediate (0–60 days): Establish the Foundation

These actions are prerequisites for everything else. They are low-cost relative to their impact and unblock subsequent work.

**1.1 Define AI Risk Tolerance (Addresses GV.5)**

Convene a working session with executive leadership (CEO, CTO, CFO, General Counsel, Chief Risk Officer if applicable) to define the organization's AI risk appetite. The output should be a written statement that:
- Defines what AI risk means in your business context
- Categorizes AI use cases into risk tiers (e.g., high/medium/low based on consequence severity)
- States which risk tiers require mandatory controls or approval gates before deployment
- Aligns AI risk tolerance with the broader enterprise risk tolerance

This is the single most important action because it gives every other remediation item a benchmark to work toward.

**1.2 Engage Legal in AI Deployments Immediately (Addresses GV.6)**

Require legal team sign-off on all AI deployments currently in progress or planned in the next 90 days. In parallel:
- Brief the General Counsel on the current AI landscape and the EU AI Act, US state AI laws, and applicable sector regulations
- Establish a standing obligation for legal review at the start and end of each AI project
- Assign a legal team member as the AI legal liaison

This should not wait for a full program to be built. Legal exposure is accumulating with each deployment that proceeds without review.

**1.3 Inventory Current AI Systems (Prerequisite for GV.1, GV.2, GV.4, GV.6)**

Conduct a rapid inventory of all AI systems currently in use or in development. For each, capture: purpose, data used, business owner, deployment date, and any known risks. This inventory does not need to be exhaustive on day one — it needs to be sufficient to understand current exposure.

---

### Priority 2 — Short-Term (60–120 days): Build Core Structures

**2.1 Establish a Cross-Functional AI Governance Body (Addresses GV.2)**

Form an AI Risk Committee or AI Governance Council with representatives from:
- Technology / Engineering
- Legal and Compliance
- Privacy / Data Protection
- Business (rotating representation from AI-using business units)
- HR (for AI systems affecting employees)
- Risk Management

Define a charter that specifies: meeting cadence, decision rights, escalation paths, and reporting line to executive leadership. This body will own the AI risk policy and review high-risk AI deployments.

**2.2 Develop a Formal AI Risk Policy (Addresses GV.1)**

Evolve the existing ethics statement into an enforceable AI risk policy. The policy should:
- Reference and expand upon the ethics statement
- Define scope (which systems are covered)
- Establish the AI system lifecycle stages and required activities at each stage
- Define roles and responsibilities
- Reference the risk tolerance tiers established in step 1.1
- Specify legal and compliance review requirements
- Define documentation standards

The policy should be approved by executive leadership and the board (or equivalent governance body) to ensure it carries organizational authority.

**2.3 Define Accountability Structures (Addresses GV.2)**

Publish a RACI matrix for AI risk management that defines who is Responsible, Accountable, Consulted, and Informed for key decisions including: AI system approval, risk assessments, incident response, and regulatory compliance. Assign an executive sponsor for AI risk (e.g., Chief AI Officer, CTO, or Chief Risk Officer).

---

### Priority 3 — Medium-Term (120–180 days): Operationalize Controls

**3.1 Implement AI Risk Assessment Process (Addresses GV.1, GV.5)**

Using the risk tolerance tiers defined in Priority 1, create a risk assessment process for new AI deployments. High-risk AI systems should require a formal impact assessment before deployment. The process should integrate with existing project management and procurement workflows.

**3.2 Establish Bias and Fairness Review Process (Addresses GV.4)**

Develop a lightweight process for evaluating AI systems for potential disparate impact or bias. At minimum, this should include:
- A bias risk screening questionnaire for all AI systems
- A defined review process for AI systems that score above a threshold
- Documentation requirements for bias testing conducted during development or procurement

Engage legal and HR in this process to connect it to equal opportunity and consumer protection obligations.

**3.3 Operationalize Transparency Requirements (Addresses GV.3)**

Convert the transparency commitments in the ethics statement into operational requirements:
- Define what documentation must be produced for each AI system (model cards, data sheets, or equivalent)
- Establish disclosure requirements for customer-facing AI (where applicable)
- Create a mechanism for employees and customers to raise concerns about AI system behavior

---

### Priority 4 — Ongoing (180+ days): Mature and Improve

**4.1 Integrate AI Risk into Enterprise Risk Management**

Connect the AI risk framework to the organization's existing ERM process. AI risks should appear on the enterprise risk register and be reviewed alongside other strategic and operational risks.

**4.2 Establish Regulatory Monitoring**

Assign responsibility (likely to legal and compliance) for monitoring AI regulatory developments globally and in relevant jurisdictions. Establish a process to assess the impact of new regulations on the organization's AI systems and practices.

**4.3 Implement Metrics and Continuous Improvement**

Define key performance indicators for AI risk management (e.g., percentage of AI systems with completed risk assessments, time to complete legal review, number of open remediation items). Report these metrics to the AI Governance Council and executive leadership quarterly.

**4.4 Conduct Periodic Governance Reviews**

Schedule an annual review of the AI risk policy, risk tolerance statement, and governance structure. As the AI landscape and regulatory environment evolve, the framework will need to evolve with it.

---

## Remediation Roadmap Summary

| Priority | Timeframe | Actions | Primary Gaps Addressed |
|---|---|---|---|
| 1 | 0–60 days | Define AI risk tolerance; engage legal; inventory AI systems | GV.5, GV.6 |
| 2 | 60–120 days | Form AI governance body; develop formal policy; define accountability | GV.1, GV.2 |
| 3 | 120–180 days | Risk assessment process; bias review; transparency requirements | GV.1, GV.3, GV.4, GV.5 |
| 4 | 180+ days | ERM integration; regulatory monitoring; metrics; periodic review | GV.1, GV.2, GV.3, GV.6 |

---

## Key Observations

**Strengths to build on:** The existence of an AI ethics statement is a meaningful signal that leadership has acknowledged AI as a domain requiring attention. This creates a cultural foundation and a reference document that can anchor the formal policy work in Priority 2.

**Most critical gap:** The absence of legal involvement in AI deployments (GV.6 rating: 1) combined with the lack of risk tolerance (GV.5 rating: 1) represents the highest immediate risk. AI-specific regulation is accelerating, and each deployment that proceeds without legal review creates accumulating liability.

**Dependency to manage:** The AI risk policy (GV.1) and governance body (GV.2) cannot be well-designed until the risk tolerance (GV.5) is defined. The sequencing in Priority 1 is deliberate — defining risk tolerance first prevents the common failure mode of building a governance structure with no clear mandate.

**Quick win:** Engaging legal immediately (item 1.2) costs little and has an outsized impact on both actual risk and organizational posture. It also sends a clear internal signal that AI governance is being taken seriously.

---

*Assessment based on NIST AI Risk Management Framework (AI RMF 1.0), published January 2023. GOVERN function subcategories reference the AI RMF Playbook guidance.*

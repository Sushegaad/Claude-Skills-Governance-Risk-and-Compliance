# NIST AI Risk Management Framework: The Four Core Functions

## Overview

The NIST AI Risk Management Framework (AI RMF 1.0), published by the National Institute of Standards and Technology in January 2023, provides a structured, voluntary approach for organizations to manage risks associated with AI systems throughout their lifecycle. At the heart of the framework are four core functions: **GOVERN**, **MAP**, **MEASURE**, and **MANAGE**. These functions are not sequential steps but rather interconnected, iterative activities that together form a comprehensive risk management practice.

---

## The Four Core Functions

### 1. GOVERN

**What it is:** GOVERN is the foundational function that establishes the organizational culture, policies, processes, and accountability structures necessary for AI risk management. It cuts across all other functions and provides the enabling conditions for MAP, MEASURE, and MANAGE to operate effectively.

**Key activities include:**
- Establishing organizational policies and procedures for AI risk management
- Defining roles, responsibilities, and accountability for AI risk (including leadership buy-in)
- Building a risk-aware organizational culture around AI development and deployment
- Setting up governance structures such as AI ethics boards, review committees, or responsible AI teams
- Ensuring transparency and documentation practices are in place
- Addressing workforce training and awareness on AI risks and trustworthy AI principles
- Aligning AI risk management with broader enterprise risk management and legal/regulatory requirements

**Why it matters:** Without GOVERN, the other three functions lack organizational backing, resources, and consistency. It ensures that AI risk management is not a one-time exercise but an ongoing, institutionalized practice.

---

### 2. MAP

**What it is:** MAP is the function focused on understanding and contextualizing AI risks. It involves identifying the AI system's context, intended use, stakeholders, and the potential risks and impacts associated with deployment.

**Key activities include:**
- Categorizing and classifying AI systems by their intended purpose and use case
- Identifying affected stakeholders, including end users, impacted communities, and third parties
- Documenting the AI system's intended and potential unintended uses
- Identifying relevant legal, regulatory, and ethical requirements
- Assessing the broader societal and organizational context in which the AI operates
- Recognizing potential sources of harm — including bias, safety failures, privacy violations, and security vulnerabilities
- Establishing risk tolerance levels and prioritizing risks based on likelihood and impact

**Why it matters:** MAP creates the situational awareness needed before risks can be measured or mitigated. It ensures that risk management efforts are targeted at what actually matters and that no significant risk categories are overlooked.

---

### 3. MEASURE

**What it is:** MEASURE involves analyzing, assessing, and tracking identified AI risks using quantitative and qualitative methods. It translates the risks identified in MAP into actionable data and evidence.

**Key activities include:**
- Evaluating AI system performance against defined metrics and benchmarks
- Testing for bias, fairness, accuracy, robustness, and reliability
- Conducting red-teaming, adversarial testing, and other technical evaluations
- Assessing the effectiveness of existing risk controls
- Monitoring AI outputs and behaviors in deployment (including drift and degradation)
- Documenting and tracking risk metrics over time
- Evaluating human-AI interaction risks, including over-reliance and automation bias

**Why it matters:** MEASURE provides the empirical evidence base for decision-making. It answers the question: "How bad is this risk, and are our controls working?" Without measurement, risk management is speculative rather than evidence-driven.

---

### 4. MANAGE

**What it is:** MANAGE is the function where identified and measured risks are prioritized and acted upon. It involves selecting, implementing, and monitoring risk treatments — including mitigations, controls, and contingency plans.

**Key activities include:**
- Prioritizing risks based on severity and organizational risk tolerance
- Implementing technical and operational controls to reduce risk (e.g., model adjustments, human oversight mechanisms, access controls)
- Developing incident response and recovery plans for AI-related failures
- Deciding whether to deploy, modify, restrict, or discontinue an AI system
- Communicating residual risks to relevant stakeholders
- Continuously monitoring deployed AI systems and updating risk treatments as conditions change
- Maintaining documentation of risk decisions and their rationale

**Why it matters:** MANAGE is where risk awareness translates into action. It closes the loop between identifying a risk and actually doing something about it — and ensures that risk treatment is tracked and revisited over time.

---

## How the Four Functions Relate to Each Other

The four functions are designed to work as an **integrated, iterative system** rather than a linear sequence:

```
         GOVERN
        (Enables all)
            |
     +------+------+
     |             |
    MAP  -----> MEASURE
     |      <--    |
     +------+------+
            |
          MANAGE
            |
     (Feedback loop back
      to MAP and GOVERN)
```

- **GOVERN** is the enabling backbone. It provides the organizational infrastructure, authority, and culture that makes MAP, MEASURE, and MANAGE possible and sustainable. GOVERN is not a one-time setup — it evolves as the organization's AI risk maturity grows.

- **MAP** feeds **MEASURE**: You cannot measure what you have not identified. The risk inventory and context established in MAP determines what gets tested, evaluated, and tracked in MEASURE.

- **MEASURE** informs **MANAGE**: Quantified and qualified risk data from MEASURE enables prioritized decision-making in MANAGE. Without measurement, risk treatments may be misallocated.

- **MANAGE** feeds back into **MAP**: Outcomes from risk treatment — including what worked, what failed, and what new risks emerged — refine the risk landscape established in MAP. This creates a continuous improvement loop.

- All four functions continuously inform **GOVERN**: Lessons learned, incident data, and emerging risks feed into policy updates, accountability structures, and cultural norms.

The AI RMF explicitly describes these as **continuous and iterative** — AI systems evolve, deployment contexts change, and new risks emerge. Risk management must be ongoing, not a one-time certification exercise.

---

## What Should You Implement First?

**Start with GOVERN — but begin MAP work in parallel.**

Here is a practical sequencing recommendation for an organization new to AI deployment:

### Phase 1: Establish Governance Foundations (Weeks 1–8)

Begin with GOVERN because it creates the organizational conditions for everything else to succeed:

1. **Secure executive sponsorship** — AI risk management requires authority and resources from leadership. Identify an executive owner (e.g., Chief AI Officer, Chief Risk Officer, or equivalent).

2. **Define AI risk roles and responsibilities** — Who is accountable for AI risk decisions? Who is responsible for testing? Who must approve deployments? Document this clearly.

3. **Inventory your AI systems** — Conduct a basic census of all AI systems currently in use or planned. Even a simple spreadsheet is sufficient at this stage. This bridges GOVERN and MAP.

4. **Establish a cross-functional AI governance team** — Include representatives from legal, compliance, IT/security, business units, and where possible, external stakeholder perspectives.

5. **Adopt an AI risk policy** — A high-level policy statement that articulates the organization's commitment to responsible AI, acceptable use boundaries, and escalation procedures.

6. **Define your risk tolerance** — What categories of AI risk are acceptable? What would trigger a deployment halt? These decisions need leadership input early.

### Phase 2: Begin Mapping Your AI Systems (Weeks 4–12, overlapping with Phase 1)

While governance infrastructure is being built, begin MAP work for your highest-priority AI deployments:

1. **Characterize each AI system** — Document its intended purpose, the data it uses, who makes decisions based on its outputs, and the populations it affects.

2. **Identify stakeholders and potential harms** — Who could be harmed if the system fails, produces biased outputs, or is misused? Include not just users but affected third parties.

3. **Assess regulatory and legal context** — Are any of your AI systems subject to sector-specific regulations (e.g., healthcare, financial services, employment)? What are the applicable legal requirements?

4. **Prioritize your AI systems by risk level** — Not all AI systems carry equal risk. Focus early MEASURE and MANAGE resources on high-impact, high-stakes systems.

### Phase 3: Implement MEASURE and MANAGE for Priority Systems (Months 3–6)

Once governance structures are in place and your highest-risk systems are mapped:

1. **Develop evaluation frameworks** — Define the metrics that matter for each system (accuracy, fairness, robustness, etc.) and establish testing protocols.

2. **Conduct initial risk assessments** — Run the first round of MEASURE activities on priority systems before or immediately after deployment.

3. **Implement risk controls** — Based on MEASURE findings, apply proportionate controls. This may mean adding human oversight checkpoints, restricting use cases, improving training data, or increasing monitoring frequency.

4. **Establish incident response procedures** — Define what happens when an AI system produces a harmful output or fails unexpectedly.

### Ongoing: Mature and Iterate (Month 6 and beyond)

- Extend GOVERN, MAP, MEASURE, and MANAGE to lower-priority AI systems
- Revisit and update risk assessments as AI systems are updated or deployment contexts change
- Build organizational AI risk management maturity over time
- Consider alignment with the AI RMF's Organizational Profiles to track progress

---

## Practical Recommendations for Getting Started

**Do not wait for perfection before starting.** A basic AI inventory, a designated risk owner, and a simple risk assessment checklist for new AI deployments will deliver immediate value, even before a comprehensive program is in place.

**Use the AI RMF Playbook.** NIST has published a companion AI RMF Playbook that provides suggested actions for each function and category. It is a practical complement to the framework document itself and can help translate high-level guidance into specific tasks.

**Integrate with existing risk management processes.** If your organization already has enterprise risk management, IT risk, or information security risk programs, AI risk management should complement and connect to these — not operate as a separate silo.

**Prioritize human oversight early.** For your first AI deployments, err on the side of more human oversight rather than less. This gives your organization time to build measurement capabilities and confidence before increasing automation.

**Document decisions.** One of the most common AI risk management failures is inadequate documentation of why decisions were made, what risks were accepted, and who approved them. Establish documentation habits from the start.

---

## Summary Table

| Function | Primary Question | Key Output |
|----------|-----------------|------------|
| GOVERN | Are we organized and accountable for AI risk? | Policies, roles, culture, governance structures |
| MAP | What risks does this AI system create and for whom? | Risk inventory, context documentation, stakeholder analysis |
| MEASURE | How significant are these risks? | Risk assessments, test results, monitoring data |
| MANAGE | What are we doing about these risks? | Risk treatments, controls, incident response, deployment decisions |

The NIST AI RMF is designed to be flexible and scalable. Organizations of any size can begin with lightweight implementations of all four functions and deepen their practices over time. The goal is not compliance with a checklist but the development of genuine organizational capacity to identify, assess, and respond to AI risks in a way that supports trustworthy AI deployment.

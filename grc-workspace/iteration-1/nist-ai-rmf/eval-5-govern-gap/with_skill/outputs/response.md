# NIST AI RMF — GOVERN Gap Assessment

**Organization Context:** AI ethics statement exists. No formal AI risk policy. No cross-functional AI team. No defined AI risk tolerance. Legal team not involved in AI deployments.

**Assessment Date:** 2026-04-25

**Current Maturity Tier:** Tier 1 — Partial (ad hoc; ethics intent present but no operationalized risk management)

---

## Section 1: GOVERN Category Ratings

| Category | Title | Rating | Current State | Gap Summary |
|----------|-------|--------|---------------|-------------|
| GV-1 | Policies, Processes, Procedures and Practices | 🔴 Not Started | AI ethics statement only; no formal AI risk management policy; no ERM integration; no review cadence; no regulatory compliance process | No GV-1 subcategory is implemented. Ethics statement provides aspirational intent but does not constitute policy. All 7 subcategories (GV-1.1 through GV-1.7) are absent. |
| GV-2 | Accountability Structures | 🔴 Not Started | No designated AI risk owner; no senior official accountable for AI risk; no board-level AI risk reporting | No one is formally accountable for AI risk outcomes. Without an appointed owner, accountability cannot be enforced. All 3 subcategories (GV-2.1 through GV-2.3) are absent. |
| GV-3 | Roles and Responsibilities | 🔴 Not Started | No AI roles register; responsibilities not mapped to lifecycle stages; business owners not assigned AI accountability | AI lifecycle roles (design, development, deployment, decommission) are undefined. Technical and non-technical accountability for AI outcomes is not documented. |
| GV-4 | Cross-Functional Team Collaboration | 🔴 Not Started | No cross-functional AI team; legal explicitly not involved; no escalation path for AI risks; no inter-team communication processes for AI risk | GV-4.1, GV-4.2, and GV-4.3 are all absent. Legal non-involvement is a direct violation of GV-4.1 requirements. No escalation mechanisms exist. |
| GV-5 | Organizational Risk Tolerance for AI | 🔴 Not Started | No AI risk tolerance statement; no deployment checklist; no go/no-go criteria for AI system launch | Without defined risk tolerance, deployment decisions for AI systems have no principled basis. All 3 subcategories (GV-5.1 through GV-5.3) are absent. |
| GV-6 | AI Risk Aligned to Laws, Regulations and Principles | 🟡 Partial | Ethics statement provides ethical principles alignment at a surface level; no regulatory register; legal team not engaged; no proactive regulatory monitoring | GV-6.2 is partially addressed by the ethics statement in intent only. GV-6.1 and GV-6.3 are absent. Legal non-involvement means regulatory requirements (EU AI Act, sector-specific laws) are not being tracked or applied. |

---

## Section 2: Subcategory Detail by Category

### GV-1 — Policies, Processes, Procedures and Practices

| Subcategory | Description | Status | Evidence Required to Close |
|-------------|-------------|--------|---------------------------|
| GV-1.1 | AI risk integrated into enterprise risk management (ERM) | 🔴 Not Started | AI risk agenda item in ERM committee; ERM policy updated to include AI |
| GV-1.2 | Trustworthy AI characteristics integrated into policies | 🔴 Not Started | Published AI Risk Policy referencing all seven trustworthiness properties |
| GV-1.3 | Organizational risk tolerance established and communicated | 🔴 Not Started | Approved AI risk appetite statement with defined thresholds |
| GV-1.4 | Culture of risk awareness and continuous improvement | 🔴 Not Started | AI risk training programme; leadership messaging on risk culture |
| GV-1.5 | AI risk policies reviewed on periodic cadence | 🔴 Not Started | Policy review schedule; documented review records |
| GV-1.6 | Policies for complying with applicable AI laws established | 🔴 Not Started | Regulatory register; legal sign-off on AI deployments |
| GV-1.7 | Processes for reviewing policies to incorporate emerging risks | 🔴 Not Started | Regulatory horizon scanning process; policy update workflow |

### GV-2 — Accountability Structures

| Subcategory | Description | Status | Evidence Required to Close |
|-------------|-------------|--------|---------------------------|
| GV-2.1 | AI risk roles and responsibilities documented across levels | 🔴 Not Started | RACI matrix for AI risk management decisions |
| GV-2.2 | Senior official designated accountable for AI risk | 🔴 Not Started | Formal appointment of AI Risk Owner; board reporting line established |
| GV-2.3 | Executive leadership understands AI risk | 🔴 Not Started | Executive AI risk briefing; AI risk on leadership dashboard |

### GV-3 — Roles and Responsibilities

| Subcategory | Description | Status | Evidence Required to Close |
|-------------|-------------|--------|---------------------------|
| GV-3.1 | AI risk roles span full lifecycle | 🔴 Not Started | Lifecycle roles register from design through decommission |
| GV-3.2 | Responsibilities defined for development teams, operators, deployers | 🔴 Not Started | Job descriptions or role charters updated with AI risk responsibilities |
| GV-3.3 | Responsibilities assigned to technical and non-technical roles | 🔴 Not Started | Business owner AI accountability documented; non-technical training |

### GV-4 — Cross-Functional Team Collaboration

| Subcategory | Description | Status | Evidence Required to Close |
|-------------|-------------|--------|---------------------------|
| GV-4.1 | Cross-functional AI risk team includes legal, privacy, security, HR, ethics | 🔴 Not Started | AI Risk Working Group charter with named representatives from each function |
| GV-4.2 | Processes for communicating AI risks between teams documented | 🔴 Not Started | AI risk communication protocol; defined reporting cadence |
| GV-4.3 | Mechanisms for escalating AI risk concerns established | 🔴 Not Started | Escalation path from development teams to executive level; escalation log |

### GV-5 — Organizational Risk Tolerance for AI

| Subcategory | Description | Status | Evidence Required to Close |
|-------------|-------------|--------|---------------------------|
| GV-5.1 | AI risk tolerance defined reflecting organizational values | 🔴 Not Started | Approved AI risk appetite statement linked to ethics statement |
| GV-5.2 | Risk tolerance reviewed when new AI systems deployed | 🔴 Not Started | Deployment review checklist; tolerance review records |
| GV-5.3 | Risk tolerance informs go/no-go deployment decisions | 🔴 Not Started | Pre-deployment gate with risk tolerance validation |

### GV-6 — AI Risk Aligned to Laws, Regulations, and Principles

| Subcategory | Description | Status | Evidence Required to Close |
|-------------|-------------|--------|---------------------------|
| GV-6.1 | Legal and regulatory requirements for AI identified and tracked | 🔴 Not Started | Regulatory register for applicable AI laws (EU AI Act, state laws, sector-specific) |
| GV-6.2 | AI risk management processes aligned with ethical principles | 🟡 Partial | Ethics statement exists; gap is operationalizing it into binding policy and process |
| GV-6.3 | Organization engages proactively with emerging AI regulations | 🔴 Not Started | Regulatory monitoring process; legal team participation in AI governance |

---

## Section 3: Trustworthy AI Properties Most at Risk

Given the GOVERN gaps identified, the following trustworthiness properties are most exposed:

| Trustworthy AI Property | Risk Exposure | Reason |
|------------------------|---------------|--------|
| **Accountable and Transparent** | Critical | No accountability structure (GV-2 absent); no one responsible for AI outcomes |
| **Fair / Bias Managed** | High | No risk tolerance thresholds for bias (GV-5 absent); no legal or ethics review of deployments |
| **Safe** | High | No formal policy defining acceptable harm levels (GV-1.3 absent); no cross-functional safety review (GV-4 absent) |
| **Privacy-Enhanced** | High | Legal not involved in deployments (GV-4.1 absent); no regulatory compliance process (GV-6.1 absent) |
| **Valid and Verified** | High | No deployment gate criteria (GV-5.3 absent); no pre-deployment validation requirements |
| **Secure and Cyber-Resilient** | Medium | Security function not formally included in AI governance (GV-4.1 absent) |
| **Explainable and Interpretable** | Medium | No policy requirement for explainability documentation (GV-1.2 absent) |

---

## Section 4: Overall GOVERN Maturity Score

| Category | Score (0–3) | Rationale |
|----------|-------------|-----------|
| GV-1 | 0 | No policy exists beyond ethics statement |
| GV-2 | 0 | No accountability structure in place |
| GV-3 | 0 | No roles or responsibilities defined |
| GV-4 | 0 | No cross-functional team; legal excluded |
| GV-5 | 0 | No risk tolerance defined |
| GV-6 | 0.5 | Ethics statement provides partial ethical principles alignment only |
| **Overall GOVERN** | **0.1 / 3** | **Tier 1 — Partial** |

---

## Section 5: Prioritised Remediation Roadmap

Priority scoring reflects: regulatory exposure + deployment risk + foundational dependency (items that block other remediation work scored highest).

### Priority 1 — Quick Wins (0–60 days): Establish the Foundation

These actions establish the minimum viable governance foundation and unblock all subsequent work.

| Action | GOVERN Category | Owner | Effort | Outcome |
|--------|----------------|-------|--------|---------|
| **1.1** Appoint an AI Risk Owner with executive sponsor | GV-2.2 | CEO / Board | Low | Formal accountability established; unblocks all other actions |
| **1.2** Convene an AI Risk Working Group — invite Legal, Privacy, Security, HR, Ethics, Engineering | GV-4.1 | AI Risk Owner | Low | Cross-functional oversight operational; closes GV-4.1 |
| **1.3** Produce a regulatory register: identify applicable AI laws (EU AI Act if EU-facing, relevant state laws, sector-specific) | GV-6.1 | Legal + AI Risk Owner | Medium | Legal exposure mapped; closes GV-6.1 |
| **1.4** Establish a legal review gate for all new AI deployments | GV-4.1, GV-6.1 | Legal + Engineering | Low | Closes the legal non-involvement gap immediately |
| **1.5** Draft and approve an AI Risk Appetite Statement linked to the existing ethics statement | GV-5.1, GV-1.3 | AI Risk Owner + Executive | Medium | Defines risk tolerance; enables deployment decision criteria |

### Priority 2 — Short Term (60–120 days): Formalize Policy and Structure

| Action | GOVERN Category | Owner | Effort | Outcome |
|--------|----------------|-------|--------|---------|
| **2.1** Publish an AI Risk Management Policy signed by senior leadership, incorporating trustworthy AI properties | GV-1.1, GV-1.2 | AI Risk Owner + Legal | High | Formal policy closes GV-1.1 and GV-1.2; supersedes ethics statement as operative document |
| **2.2** Create an AI Roles Register mapping lifecycle stages (design, build, deploy, monitor, decommission) to responsible roles | GV-3.1, GV-3.2, GV-3.3 | AI Risk Owner + HR | Medium | Closes all three GV-3 subcategories |
| **2.3** Define RACI for AI risk decisions; assign senior official as accountable owner at board level | GV-2.1, GV-2.2, GV-2.3 | CEO + AI Risk Owner | Medium | Closes GV-2; establishes board-level AI risk visibility |
| **2.4** Document AI risk communication protocol and escalation path (development → management → executive) | GV-4.2, GV-4.3 | AI Risk Owner | Low | Closes GV-4.2 and GV-4.3 |
| **2.5** Create a pre-deployment AI checklist validating systems against risk appetite statement | GV-5.2, GV-5.3 | Engineering + Legal | Medium | Operationalizes risk tolerance into deployment gate |

### Priority 3 — Medium Term (120–180 days): Integrate and Institutionalise

| Action | GOVERN Category | Owner | Effort | Outcome |
|--------|----------------|-------|--------|---------|
| **3.1** Integrate AI risk into Enterprise Risk Management (ERM) — add AI risk to ERM committee agenda and quarterly reporting | GV-1.1 | Chief Risk Officer + AI Risk Owner | Medium | AI risk visible at enterprise level; closes GV-1.1 integration requirement |
| **3.2** Launch AI risk awareness training for technical and non-technical staff | GV-1.4, GV-3.3 | HR + AI Risk Owner | Medium | Embeds risk culture; closes GV-1.4 |
| **3.3** Establish regulatory horizon scanning process — subscribe to EU AI Act updates, NIST publications, sector-specific guidance | GV-6.3, GV-1.7 | Legal + AI Risk Owner | Low | Proactive regulatory monitoring; closes GV-6.3 and GV-1.7 |
| **3.4** Set AI Risk Policy review schedule — annual minimum with trigger-based reviews on new deployments or regulatory changes | GV-1.5, GV-5.2 | AI Risk Owner | Low | Closes GV-1.5; ensures governance remains current |
| **3.5** Conduct executive AI risk briefing; include AI risk KPIs on leadership dashboard | GV-2.3 | AI Risk Owner | Low | Closes GV-2.3; leadership accountability for AI outcomes |

### Priority 4 — Long Term (180+ days): Optimise and Demonstrate

| Action | GOVERN Category | Owner | Effort | Outcome |
|--------|----------------|-------|--------|---------|
| **4.1** Commission external assessment or third-party audit of AI governance programme | All GOVERN | AI Risk Owner | High | Independent validation of maturity; identifies residual gaps |
| **4.2** Align AI Risk Policy to ISO/IEC 42001:2023 — consider certification pathway | GV-1, GV-2, GV-5, GV-6 | AI Risk Owner + Legal | High | International standard alignment; supports ISO 42001 Clause 5/6 obligations |
| **4.3** Operationalize ethics statement into binding internal principles document with measurable commitments | GV-6.2 | Ethics + Legal + AI Risk Owner | Medium | Fully closes GV-6.2 with documented, auditable principles |
| **4.4** Define AI risk tolerance thresholds per system category (e.g., recommendation engine vs. individual decision-making) with specific bias/accuracy metrics | GV-5.1 | AI Risk Owner + Data Science | High | Quantified risk tolerance enabling objective go/no-go decisions |

---

## Section 6: Critical Path Dependencies

The following sequence must be respected — later items depend on earlier completions:

```
Appoint AI Risk Owner (1.1)
  └─► Convene Working Group (1.2)
        └─► Legal Review Gate (1.4) ──► Regulatory Register (1.3)
  └─► AI Risk Appetite Statement (1.5)
        └─► AI Risk Management Policy (2.1)
              └─► Roles Register (2.2)
              └─► RACI (2.3)
              └─► Pre-Deployment Checklist (2.5)
                    └─► ERM Integration (3.1)
                          └─► External Audit (4.1)
```

The single most important immediate action is appointing an AI Risk Owner. Without a named accountable person, no other remediation item can progress effectively.

---

## Section 7: Immediate Legal Exposure Note

The fact that the legal team is not involved in AI deployments creates immediate compliance exposure across multiple regulatory regimes:

- **EU AI Act (if in scope):** Art. 9 requires a risk management system for high-risk AI providers; Art. 16 and 26 impose obligations on providers and deployers. Legal non-involvement means these obligations may be unmet for any in-scope AI system.
- **Sector-specific obligations:** Depending on sector (financial services, healthcare, HR/recruitment), AI systems may already be subject to binding regulatory requirements (ECOA, HIPAA, EEOC) that require documented compliance review before deployment.
- **Data privacy:** AI systems processing personal data require legal review to satisfy GDPR, CCPA, or applicable privacy laws — which currently has no gate.

**Recommended immediate action:** Before the next AI system is deployed, implement Priority 1.4 (legal review gate) regardless of the broader roadmap timeline.

---

## Section 8: Target Profile

Recommended target maturity for each GOVERN category within 12 months:

| Category | Current Score | 6-Month Target | 12-Month Target |
|----------|---------------|----------------|-----------------|
| GV-1 | 0 (Tier 1) | 1.5 (Tier 2) | 2.5 (Tier 3) |
| GV-2 | 0 (Tier 1) | 2.0 (Tier 2–3) | 3.0 (Tier 3) |
| GV-3 | 0 (Tier 1) | 1.5 (Tier 2) | 2.5 (Tier 3) |
| GV-4 | 0 (Tier 1) | 2.0 (Tier 2–3) | 3.0 (Tier 3) |
| GV-5 | 0 (Tier 1) | 1.5 (Tier 2) | 2.0 (Tier 2–3) |
| GV-6 | 0.5 (Tier 1) | 1.5 (Tier 2) | 2.5 (Tier 3) |

Achieving Tier 3 (Repeatable) across all GOVERN categories within 12 months is an aggressive but achievable target given the organization already has an ethics statement as a cultural foundation to build on.

---

*Assessment based on NIST AI 100-1 (January 2023) and the AI RMF Playbook. Categories cited as GV-1 through GV-6 correspond to the GOVERN function subcategories defined in the AI RMF Core.*

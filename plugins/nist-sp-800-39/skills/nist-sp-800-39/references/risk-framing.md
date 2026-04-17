# NIST SP 800-39 — Risk Framing

Source: NIST Special Publication 800-39, Section 3.1 (March 2011)

---

## What is Risk Framing?

Risk framing establishes the **context and environment** in which risk-based decisions are made across the organisation. Without explicit framing, risk assessments and responses may be conducted inconsistently, with different assumptions, different standards for what is acceptable, and different priorities. The risk frame is the output of the Prepare step in SP 800-37 at the organisation level.

Risk framing is the responsibility of **Tier 1** (organisation-level) governance but informs all risk management activities at Tiers 2 and 3.

---

## Components of the Risk Frame

### 1. Risk Assumptions

Risk assumptions define what the organisation accepts as true for purposes of risk management. They enable consistent analysis across the organisation.

**Categories of risk assumptions:**

| Category | Examples |
|----------|---------|
| Threat assumptions | Which threat actors are considered relevant; what capabilities are assumed |
| Vulnerability assumptions | Assumed baseline vulnerability level; assumed patching lag time |
| Impact assumptions | Which impact types are considered (only CIA, or also financial, reputational, safety) |
| Environmental assumptions | Data classification scheme assumed; interconnection types in scope |
| Temporal assumptions | Assessment period; how long data is considered current |

**Documenting assumptions:**
Each assumption should be stated explicitly so that any user of a risk assessment can understand the basis on which the risk determination was made, and so that if an assumption is found to be incorrect the risk assessment can be updated accordingly.

Example:
> "Threat assumption 1: Nation-state adversaries are assumed to have high capability and high motivation to target [Agency X] given its mission. This assumption is based on [threat intelligence source] current as of [date] and will be reviewed quarterly."

---

### 2. Risk Constraints

Risk constraints are factors that limit the organisation's ability to respond to risks. Constraints may be:

| Constraint Type | Examples |
|----------------|---------|
| Legal / regulatory | Restrictions on data handling; FISMA compliance requirements; export controls |
| Policy | Internal policies restricting certain architectures or vendors |
| Mission / operational | Controls that would degrade mission performance are not acceptable |
| Budget | Financial limits on security investment |
| Technology | Legacy systems that cannot support modern controls |
| Workforce | Insufficient trained staff to implement certain controls |
| Contractual | Existing contracts restricting changes to systems or data handling |

**Documenting constraints:**
Constraints must be documented so that risk responses do not propose actions that are not feasible. A risk response that violates a constraint is not a valid option.

---

### 3. Risk Tolerance

Risk tolerance is the **explicit level of risk that the organisation is willing to accept**. It defines the threshold between risks that are acceptable and risks that require response.

**Dimensions of risk tolerance:**

| Dimension | Description | Example Statement |
|-----------|-------------|-------------------|
| Overall level | Maximum overall risk level acceptable | "Very High risk is never acceptable. High risk requires AO-level acceptance and is accepted only for defined operational requirements." |
| Confidentiality | Risk to information confidentiality | "No risk of unauthorised disclosure of classified or controlled unclassified information (CUI) is acceptable without executive approval." |
| Integrity | Risk to information integrity | "Risks to critical data integrity in financial or safety-critical systems are tolerated only at Low level." |
| Availability | Risk to system availability | "Downtime risk for Tier 1 mission-critical systems must be maintained at Low or below." |
| Privacy | Risk to personal information | "Any risk to PII beyond Low requires SAOP review." |
| Supply chain | Risk from suppliers | "Medium supply chain risk is tolerated with SCRM controls; High or Very High requires case-by-case AO approval." |
| Time | Duration of risk acceptance | "Accepted risks are reviewed annually or upon any significant change to the system or threat environment." |

**Expressing risk tolerance numerically:**
Some organisations express tolerance using the 5-tiered scale from SP 800-30 (Very Low / Low / Moderate / High / Very High) with explicit thresholds for escalation and mandatory treatment.

---

### 4. Risk Priorities and Trade-offs

Risk priorities define what the organisation protects first when resources are constrained.

**Priority considerations:**
- Mission-critical systems and information (those without which the mission fails)
- Regulatory and legal obligations (those that create legal liability if breached)
- High-concentration risks (single points of failure or aggregated sensitive data)
- Public trust and reputation (for public-facing agencies)
- Personnel safety (for systems controlling physical infrastructure or processes)

**Trade-off acknowledgements:**
Risk framing should explicitly acknowledge trade-offs. For example:
- Cost vs. risk reduction: Investing $X in control Y reduces risk from High to Moderate — this is/is not within our security budget
- Mission performance vs. security: Encrypting field device communications adds latency — the mission impact is acceptable/not acceptable

---

## Risk Framing Document Template

### Document Control

| Field | Value |
|-------|-------|
| Document Title | Organisation-Wide Risk Framing Document |
| Version | |
| Date | |
| Owner | Risk Executive / CISO |
| Review Cycle | Annual or upon significant change |
| Classification | |

### Sections

**Section 1 — Organisational Context**
- Organisation mission statement
- Key mission functions and services
- Regulatory and legislative environment
- Industry and sector context
- Critical information types and assets

**Section 2 — Threat Environment**
- Applicable threat sources (adversarial, non-adversarial)
- Current threat intelligence summary
- Sector-specific threat actors and campaigns
- Historical incidents relevant to framing

**Section 3 — Risk Assumptions**
Table:
| Assumption ID | Category | Assumption Statement | Basis | Review Date |
|--------------|----------|---------------------|-------|------------|

**Section 4 — Risk Constraints**
Table:
| Constraint ID | Type | Constraint Description | Impact on Risk Response | Owner |
|--------------|------|----------------------|------------------------|-------|

**Section 5 — Risk Tolerance**
Table:
| Dimension | Risk Tolerance Level | Escalation Threshold | Notes |
|-----------|---------------------|---------------------|-------|

**Section 6 — Risk Priorities**
Numbered list of prioritised risk protection areas with rationale.

**Section 7 — Risk Management Strategy**
- How risk assessments will be conducted (tiered; methodology; frequency)
- How risk responses are decided and by whom
- How risk information flows between tiers
- How the risk framing will be reviewed and updated

**Section 8 — Approvals**
Signatures of: Head of Organisation (or delegate), Risk Executive, CISO, SAOP (if applicable)

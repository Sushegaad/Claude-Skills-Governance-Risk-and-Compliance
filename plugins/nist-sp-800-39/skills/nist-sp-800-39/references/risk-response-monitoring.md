# NIST SP 800-39 — Risk Response and Risk Monitoring

Source: NIST Special Publication 800-39, Sections 3.3 and 3.4 (March 2011)

---

## Risk Response

### Overview

Risk response involves identifying, evaluating, and implementing appropriate courses of action to address identified risks in a manner consistent with the organisation's risk framing (tolerance, assumptions, constraints, and priorities). Risk response decisions are made at all three tiers.

---

### Risk Response Options

SP 800-39 defines four risk response options:

#### Accept

The organisation acknowledges the risk but takes no additional action to address it.

**When to use:**
- Risk level is within the organisation's stated risk tolerance
- Cost of mitigation exceeds the expected benefit
- No feasible mitigation exists (e.g., natural disaster risk to a fixed facility)
- Operational necessity requires accepting the risk temporarily

**Documentation required:**
- Explicit written acceptance by the appropriate authority (AO for Tier 3; mission owner for Tier 2; Risk Executive for Tier 1)
- Rationale for acceptance
- Risk level accepted (to confirm it is within tolerance)
- Review date (when acceptance will be reconsidered)
- Any compensating conditions in place

**Risk acceptance authority by tier:**

| Tier | Risk Level | Accepting Authority |
|------|-----------|---------------------|
| Tier 3 | Low / Very Low | ISSO / SO |
| Tier 3 | Moderate | Authorising Official |
| Tier 3 | High / Very High | Authorising Official with Risk Executive notification |
| Tier 2 | Any | Mission/Business Owner with Risk Executive review |
| Tier 1 | Any | Risk Executive / Head of Organisation |

---

#### Avoid

The organisation eliminates the risk by discontinuing the activity, process, or capability that creates the risk.

**When to use:**
- Risk level is unacceptable (intolerable)
- The activity creating the risk is not essential to the mission
- No effective mitigation exists and transfer is not feasible

**Examples:**
- Shutting down a legacy system with critical unpatched vulnerabilities that cannot be patched or replaced quickly
- Deciding not to store certain categories of highly sensitive data
- Discontinuing use of a third-party service with unacceptable supply chain risk

**Documentation required:**
- Decision and rationale
- Who made the decision
- Mission impact of avoidance
- Residual risk after avoidance

---

#### Mitigate

The organisation implements controls, changes processes, or modifies architecture to reduce the likelihood or magnitude of the risk.

**When to use:**
- Risk exceeds tolerance but cannot be avoided
- Effective controls exist that are cost-proportionate to the risk
- Risk must be reduced to an acceptable residual level

**Mitigation strategies at each tier:**

| Tier | Mitigation Mechanisms |
|------|--------------------|
| Tier 1 | Policy changes; governance improvements; investment reallocation; supply chain controls |
| Tier 2 | Architecture changes; cross-system controls; business process redesign; shared service security improvements |
| Tier 3 | SP 800-53 controls (technical, operational, management); configuration hardening; network segmentation; encryption; monitoring |

**Mitigation plan components:**
| Field | Description |
|-------|-------------|
| Mitigation action | Specific control or process change |
| Expected effect | How the mitigation changes likelihood or impact |
| Expected residual risk | Risk level after applying mitigation |
| Implementation timeline | Target completion date |
| Cost | Estimated resource requirement |
| Dependencies | What else must be in place for this mitigation to work |
| Responsible party | Who will implement and operationalise |
| Verification method | How effectiveness will be confirmed |

---

#### Transfer / Share

The organisation shifts some or all of the financial, operational, or reputational burden of the risk to a third party.

**When to use:**
- Risk exceeds financial tolerance but can be substantially covered by insurance or contract
- Outsourcing a function to a provider who accepts responsibility for security outcomes
- Contractually assigning liability for data breaches to a vendor processing on the organisation's behalf

**Common transfer mechanisms:**
- Cyber liability insurance
- Contract clauses with financial penalties for vendor breaches
- Cloud service provider shared responsibility model (where the CSP is contractually responsible for infrastructure security)
- Indemnification clauses

**Important limitation:**
Transfer or sharing reduces financial impact but does not eliminate reputational, legal, or mission impact. Organisations remain accountable to regulators and the public even if a vendor bears financial liability.

---

### Risk Response Plan Format

| Field | Description |
|-------|-------------|
| Risk ID | Unique identifier (linked to risk register) |
| Risk Description | The identified risk |
| Risk Level | Current assessed level (Very Low to Very High) |
| Response Option | Accept / Avoid / Mitigate / Transfer |
| Rationale | Why this response was selected |
| Mitigation Actions | Specific actions if mitigate is selected |
| Transfer Mechanism | Insurance, contract, etc. if transfer selected |
| Acceptance Authority | Named individual with authority to accept (if accept) |
| Residual Risk | Expected risk level after response |
| Timeline | When the response will be implemented |
| Responsible Party | Who owns implementation |
| Resources Required | Staff, budget, technology |
| Success Metric | How effectiveness will be measured |

---

## Risk Monitoring

### Purpose

Risk monitoring supports the other three risk management components by:
1. Verifying that risk responses are implemented correctly and operating as intended
2. Detecting changes in the risk environment (threat, vulnerability, impact) that may require re-assessment or revised responses
3. Maintaining currency of risk information so that decisions are based on accurate data
4. Supporting continuous authorisation decisions at Tier 3

---

### Monitoring Activities

#### Control Effectiveness Monitoring

Verifies that implemented mitigating controls continue to operate effectively.

| Activity | Description | Frequency |
|----------|-------------|-----------|
| Security control assessment | Formal assessment of controls per SP 800-53A | Annual or per SAP schedule |
| Automated tool scanning | Vulnerability scanners, configuration compliance tools | Continuous / weekly |
| SIEM monitoring | Real-time monitoring of security events | Continuous |
| Penetration testing | Adversarial testing of controls | Annual or more frequently for high-impact systems |
| Control metrics collection | Tracking key performance indicators (patching rates, open findings, training completion) | Monthly / quarterly |

#### Risk Environment Monitoring

Detects changes in the environment that may affect risk levels even if controls have not changed.

| Activity | Description | Sources |
|----------|-------------|---------|
| Threat intelligence | Track emerging threats relevant to the organisation | CISA advisories; sector ISACs; NIST NVD; open-source intelligence |
| Vulnerability monitoring | Track new CVEs affecting in-use technologies | NIST NVD; vendor advisories; CISA KEV |
| Incident monitoring | Monitor for security incidents at peers or in the sector | ISAC reporting; media; government bulletins |
| Regulatory monitoring | Track changes in applicable law and regulation | Federal Register; OMB memos; agency policy updates |

#### Risk Acceptance Review

Periodically re-examines previously accepted risks to confirm they remain within tolerance.

| Trigger | Action |
|---------|--------|
| Annual review cycle | All previously accepted risks reviewed |
| Significant system change | Accepted risks for the affected system reviewed |
| Significant threat change | Accepted risks with that threat source reviewed |
| Security incident | Accepted risks in the same category reviewed |
| Policy change | Accepted risks that relied on the prior policy reviewed |

---

### Risk Posture Reporting

Risk posture reports communicate the current state of risk across the organisation to leadership. Reporting must flow up through the tier structure.

**Tier 3 to Tier 2 reporting (system-level):**
- Monthly or quarterly (defined in monitoring strategy)
- Content: ATO status; POA&M status; high/critical finding count; recent incidents; control failure notifications

**Tier 2 to Tier 1 reporting (business process level):**
- Quarterly (minimum)
- Content: Aggregated risk by mission function; cross-system risks; supply chain risk status; emerging risks

**Tier 1 executive reporting:**
- FISMA annual report to OMB (for federal agencies)
- Executive dashboard (automated where possible)
- Risk posture summary for Head of Organisation / Board
- Event-driven escalation for Very High risk discoveries

### Monitoring Triggers for Immediate Escalation

The following events must be immediately escalated rather than waiting for the regular reporting cycle:

| Trigger | Required Response |
|---------|-----------------|
| Discovery of a Very High risk | Immediate notification to AO and Risk Executive |
| Active exploitation of a known vulnerability in the organisation's systems | Incident response activation + AO notification |
| Significant compromise of a common control | All inheriting systems assessed for impact |
| Discovery that an accepted risk has materially increased | Risk acceptance re-evaluated by appropriate authority |
| Critical change to the threat environment (e.g., new APT campaign targeting the sector) | Risk framing review triggered; risk assessments updated |

# NIST SP 800-30 Rev 1 — Impact, Likelihood, and Risk Scales

Source: NIST SP 800-30 Rev 1, Appendices G, H, and I (September 2012)

---

## Likelihood Scales

### Table G-2: Likelihood of Threat Event Initiation (Adversarial)

Assesses the probability that an adversarial threat source will attempt the threat event against the target organisation during the assessment period.

| Qualitative Value | Semi-Quantitative Score | Description |
|-------------------|------------------------|-------------|
| Very High | 96 – 100 | Adversary is highly capable and strongly motivated. The threat event is expected to be initiated. Historical precedent and current intelligence indicate near-certainty of occurrence. |
| High | 80 – 95 | Adversary is capable and motivated. It is highly likely the threat event will be initiated. Significant intelligence or historical evidence supports this rating. |
| Moderate | 21 – 79 | Adversary has some capability and motivation. The threat event is as likely to occur as not. Moderate intelligence evidence exists. |
| Low | 5 – 20 | Adversary has limited capability or motivation. The threat event is unlikely to be initiated. Limited evidence of adversary interest in this target type. |
| Very Low | 0 – 4 | Adversary capability or motivation is very limited. The threat event is highly unlikely to be initiated. No evidence of adversary interest. |

### Table G-3: Likelihood of Adverse Impact (Given Threat Initiation)

Assesses the probability that the threat event, if initiated, results in actual adverse impact. This is primarily driven by vulnerability severity and control effectiveness.

| Qualitative Value | Semi-Quantitative Score | Description |
|-------------------|------------------------|-------------|
| Very High | 96 – 100 | Vulnerabilities are highly exploitable; controls are absent or wholly ineffective. Near certainty that initiation leads to adverse impact. |
| High | 80 – 95 | Vulnerabilities are likely exploitable; controls are mostly absent or largely ineffective. Adverse impact is highly likely if the threat is initiated. |
| Moderate | 21 – 79 | Vulnerabilities are somewhat exploitable; controls exist but have notable gaps. Adverse impact is possible but not certain. |
| Low | 5 – 20 | Vulnerabilities are difficult to exploit; effective controls reduce likelihood of adverse impact substantially. |
| Very Low | 0 – 4 | Vulnerabilities are very difficult to exploit; comprehensive and effective controls are in place. Adverse impact is highly unlikely even if the threat is initiated. |

### Table G-4: Likelihood of Threat Event Occurrence (Non-Adversarial)

Assesses the probability that a non-adversarial threat event occurs during the assessment period.

| Qualitative Value | Semi-Quantitative Score | Description |
|-------------------|------------------------|-------------|
| Very High | 96 – 100 | Event is virtually certain to occur. (E.g., disk failure in multi-year operational systems without replacement cycles.) |
| High | 80 – 95 | Event is highly likely to occur. (E.g., user error in high-volume data entry environments.) |
| Moderate | 21 – 79 | Event may occur. (E.g., power outage in regions without robust utility infrastructure.) |
| Low | 5 – 20 | Event is unlikely to occur. (E.g., severe earthquake in a low-seismic region.) |
| Very Low | 0 – 4 | Event is highly unlikely to occur. (E.g., a Category 5 hurricane in an inland, non-coastal data centre.) |

---

## Overall Likelihood Determination

### Table I-2: Overall Likelihood Matrix

Overall likelihood combines the likelihood of threat initiation (or occurrence) with the likelihood of adverse impact.

|  | Very Low Impact-Susceptibility | Low | Moderate | High | Very High |
|--|-------------------------------|-----|----------|------|-----------|
| **Very High Initiation** | Low | Moderate | High | Very High | Very High |
| **High Initiation** | Very Low | Low | Moderate | High | Very High |
| **Moderate Initiation** | Very Low | Low | Moderate | Moderate | High |
| **Low Initiation** | Very Low | Very Low | Low | Low | Moderate |
| **Very Low Initiation** | Very Low | Very Low | Very Low | Low | Low |

---

## Impact Scales

### Table H-2: Impact of Threat Events on Core Missions/Business Functions

| Qualitative Value | Semi-Quantitative Score | Description |
|-------------------|------------------------|-------------|
| Very High | 96 – 100 | Multiple severe or catastrophic adverse effects on organisational operations, assets, or individuals. Loss of life or severe physical harm; loss of critically sensitive information; complete mission failure; catastrophic financial damage. |
| High | 80 – 95 | Severe degradation in mission capability; significant damage to major assets; major financial damage; major harm to individuals (not life-threatening). |
| Moderate | 21 – 79 | Significant degradation in mission capability; significant damage; significant financial loss; significant harm to individuals (not major or life-threatening). |
| Low | 5 – 20 | Limited degradation of mission capability; minor damage to assets; minor financial loss; minor harm to individuals. |
| Very Low | 0 – 4 | Negligible or no impact on mission capability; negligible damage; negligible financial loss; negligible harm to individuals. |

### Table H-3: Impact Across CIA Triad and Operational Dimensions

| Impact Dimension | Very High | High | Moderate | Low | Very Low |
|-----------------|-----------|------|----------|-----|---------|
| **Confidentiality** | Disclosure of critically sensitive information (CLAS, personal data at scale) | Disclosure of sensitive PII, financial records | Disclosure of information requiring protection | Limited disclosure; controlled data | Negligible; public information |
| **Integrity** | Catastrophic corruption of critical data; cannot be recovered | Major data corruption affecting critical transactions | Significant data modification affecting operations | Minor data alteration; detectable | Negligible alteration; no operational effect |
| **Availability** | Complete failure of critical infrastructure; unrecoverable | Extended loss (>24 hours) of critical services | Partial or temporary loss of important services | Brief or minor loss; quickly restored | Negligible interruption |

---

## Risk Determination

### Table I-4: Risk Level Matrix (Likelihood × Impact)

Risk is determined by combining overall likelihood with magnitude of impact.

| Likelihood ↓ / Impact → | Very Low | Low | Moderate | High | Very High |
|------------------------|---------|-----|----------|------|-----------|
| **Very High** | Low | Moderate | High | Very High | Very High |
| **High** | Low | Moderate | Moderate | High | Very High |
| **Moderate** | Low | Low | Moderate | High | High |
| **Low** | Very Low | Low | Low | Moderate | High |
| **Very Low** | Very Low | Very Low | Low | Low | Moderate |

### Risk Level Definitions (Table I-5)

| Risk Level | Definition | Required Action |
|-----------|------------|----------------|
| **Very High** | A threat event could be expected to have multiple severe or catastrophic adverse effects on mission operations, assets, or individuals if it occurs. | Corrective measures are urgently required. The risk is unacceptable. Immediate executive attention and remediation resources are required. |
| **High** | A threat event could be expected to have a severe or catastrophic adverse effect. | Corrective measures should be implemented within near-term (30–90 days). Senior leadership notification required. |
| **Moderate** | A threat event could be expected to have a serious adverse effect. | Corrective measures should be implemented within a reasonable period (90–180 days). Management attention and resource allocation required. |
| **Low** | A threat event could be expected to have a limited adverse effect. | Risk is acceptable with standard controls in place. Monitor and include in next assessment cycle. |
| **Very Low** | A threat event could be expected to have a negligible adverse effect. | Risk is acceptable. No additional action required at this time. |

---

## Uncertainty Notation

All risk determinations must include an **uncertainty** qualifier to indicate confidence in the assessment:

| Uncertainty Level | Description |
|------------------|-------------|
| **Low** | Assessment is based on comprehensive threat intelligence, detailed vulnerability data, and well-characterised impact. High confidence in the risk determination. |
| **Moderate** | Assessment is based on adequate data but with some gaps in threat intelligence, vulnerability specifics, or impact quantification. |
| **High** | Assessment is based on limited data, significant assumptions, or rapidly changing conditions. Risk determination may shift substantially as more information becomes available. |

---

## Vulnerability Severity Scale — Appendix F, Table F-2

| Qualitative Value | Semi-Quantitative Score | Description |
|-------------------|------------------------|-------------|
| Very High | 9 – 10 | Vulnerability is easily exploitable with widely available tools; no technical expertise required; no compensating controls in place |
| High | 7 – 8 | Vulnerability is exploitable with moderate skill; limited compensating controls exist |
| Moderate | 4 – 6 | Vulnerability is exploitable with significant skill; some compensating controls reduce risk but do not eliminate it |
| Low | 2 – 3 | Vulnerability is difficult to exploit; effective controls significantly reduce likelihood of successful exploitation |
| Very Low | 0 – 1 | Vulnerability is very difficult to exploit; comprehensive controls effectively eliminate exploitability |

---

## Predisposing Condition Pervasiveness — Appendix F, Table F-3

| Qualitative Value | Description |
|-------------------|-------------|
| Very High | Predisposing condition exists throughout the environment; affects nearly all systems and processes |
| High | Predisposing condition is widespread; affects most systems or processes |
| Moderate | Predisposing condition is present in multiple areas but not pervasive |
| Low | Predisposing condition is limited to a few systems or processes |
| Very Low | Predisposing condition is isolated; affects only a single system or process |

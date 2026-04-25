# NIST AI RMF and EU AI Act: Framework Mapping and Gap Analysis

## Executive Summary

The NIST AI Risk Management Framework (AI RMF 1.0) and the EU AI Act are complementary but distinct instruments. The AI RMF is a voluntary, flexible risk management framework developed by NIST (published January 2023), while the EU AI Act is mandatory EU legislation with binding legal obligations, enforcement mechanisms, and penalties. Organizations subject to the EU AI Act that have adopted the AI RMF will find significant conceptual overlap but must address meaningful compliance gaps to satisfy their legal obligations.

---

## 1. Overview of Each Framework

### NIST AI RMF 1.0

The NIST AI RMF organizes AI risk management around four core functions:

- **GOVERN**: Establish organizational policies, culture, and accountability structures for AI risk management.
- **MAP**: Identify and categorize AI risks in context.
- **MEASURE**: Analyze and assess identified risks using qualitative and quantitative methods.
- **RESPOND**: Prioritize and act on risks; develop and implement risk response plans.

The framework is principles-based and technology-neutral. It does not prescribe specific controls but provides a structured approach to managing AI risks across the AI lifecycle.

### EU AI Act

The EU AI Act (Regulation (EU) 2024/1689, fully applicable from August 2026) establishes a risk-based regulatory regime with four risk tiers:

- **Unacceptable risk**: Prohibited AI practices (e.g., social scoring, real-time remote biometric identification in public spaces with narrow exceptions).
- **High-risk**: Mandatory pre-market and post-market requirements (Annexes I and III systems, including critical infrastructure, employment, education, essential services, law enforcement, migration, justice, biometrics).
- **Limited risk**: Transparency obligations (e.g., chatbots, deepfakes).
- **Minimal risk**: No specific requirements.

The Act creates legal obligations for **providers** (developers/deployers who place AI on the EU market) and **deployers** (organizations putting AI into use), with specific duties varying by role.

---

## 2. Conceptual Alignment: Where AI RMF and the EU AI Act Converge

### 2.1 Risk-Based Approach

Both frameworks share a foundational risk-based philosophy: the level of scrutiny and controls applied to an AI system should be proportionate to the risks it poses.

| AI RMF Concept | EU AI Act Equivalent |
|---|---|
| Risk tiering via MAP function | Four-tier risk classification (prohibited, high-risk, limited risk, minimal risk) |
| Contextual risk assessment (MAP 1.x) | Risk assessment for high-risk AI systems (Art. 9) |
| Risk response planning (RESPOND) | Risk management system requirements (Art. 9) |

### 2.2 Documentation and Record-Keeping

| AI RMF | EU AI Act |
|---|---|
| GOVERN 1.7: Document AI risk management policies | Art. 11: Technical documentation (Annex IV) |
| MEASURE 2.5: Document evaluation results | Art. 12: Record-keeping and logging |
| GOVERN 6.1: Policies governing AI supply chain | Art. 25: Obligations for third-party providers |

### 2.3 Human Oversight

| AI RMF | EU AI Act |
|---|---|
| GOVERN 5.1: Organizational roles for oversight | Art. 14: Human oversight measures |
| RESPOND 1.1: Monitor and respond to AI outputs | Art. 14(4): Operator ability to intervene/halt |
| MAP 5.1: Impacts on humans identified | Art. 9(2): Risk identification for natural persons |

### 2.4 Transparency and Explainability

| AI RMF | EU AI Act |
|---|---|
| GOVERN 4.1: Transparency practices established | Art. 13: Transparency and provision of information |
| MEASURE 2.9: Explainability assessed | Art. 13(1): High-risk systems must be interpretable |
| MAP 2.3: Scientific basis for AI claims documented | Art. 13(2): Instructions for use |

### 2.5 Testing, Validation, and Performance Monitoring

| AI RMF | EU AI Act |
|---|---|
| MEASURE 2.2: AI system testing and evaluation | Art. 9(6): Testing for risk management |
| MEASURE 2.6: Bias and fairness evaluation | Art. 10(2): Training data governance; Art. 9(7): Bias testing |
| RESPOND 2.1: Monitoring in deployment | Art. 72: Post-market monitoring system |

### 2.6 Incident Response

| AI RMF | EU AI Act |
|---|---|
| RESPOND 1.3: Incident response procedures | Art. 73: Reporting of serious incidents |
| RESPOND 2.2: Remediation plans | Art. 20: Corrective actions |

---

## 3. Gap Analysis: What AI RMF Does Not Cover That the EU AI Act Requires

Implementing the NIST AI RMF provides a strong foundation but leaves the following EU AI Act obligations unaddressed or only partially addressed:

### 3.1 Prohibited Practices (Art. 5) — No AI RMF Equivalent

The EU AI Act absolutely prohibits certain AI applications. The AI RMF has no analogous prohibition mechanism — it treats all AI systems as candidates for risk management rather than outright banning any practice.

**Action required:** Conduct an inventory of all AI systems and explicitly screen for prohibited use cases before applying risk management processes. Document the screening and confirm no prohibited applications are deployed.

Prohibited practices include:
- Subliminal manipulation causing harm
- Exploitation of vulnerable groups
- Social scoring by public authorities
- Real-time remote biometric identification in public spaces (with narrow exceptions)
- Predictive policing based solely on profiling
- Emotion recognition in workplace/educational settings (with exceptions)
- Biometric categorization to infer sensitive attributes

### 3.2 Mandatory Conformity Assessment (Art. 43) — Not Addressed by AI RMF

High-risk AI systems must undergo a formal conformity assessment before market placement:
- **Self-assessment** is permissible for most Annex III systems if the provider follows harmonized standards.
- **Third-party assessment** by a notified body is required for certain systems (e.g., biometric identification, critical infrastructure).

The AI RMF does not require any external assessment or certification. It is entirely self-directed.

**Action required:** Determine whether your high-risk AI systems require third-party conformity assessment. Engage a notified body where required. Maintain conformity assessment documentation and affix the CE marking as applicable.

### 3.3 EU Declaration of Conformity and CE Marking (Arts. 47–49)

Providers of high-risk AI systems must draw up an EU Declaration of Conformity and affix the CE marking before placing the system on the EU market.

The AI RMF has no concept of market placement declarations or regulatory markings.

**Action required:** Establish a process to prepare and maintain EU Declarations of Conformity. Integrate CE marking into the product release workflow.

### 3.4 Registration in the EU Database (Art. 71)

Providers of high-risk AI systems listed in Annex III must register in the EU AI Act public database before deployment. Deployers of certain public-sector high-risk systems also have registration obligations.

The AI RMF has no registry or public disclosure requirement.

**Action required:** Register all applicable high-risk AI systems in the EU public database. Assign responsibility for maintaining registration records and updating entries upon significant modifications.

### 3.5 Specific Data Governance Requirements (Art. 10)

The EU AI Act mandates detailed data governance for training, validation, and testing datasets for high-risk AI systems, including requirements related to:
- Relevance, representativeness, and freedom from errors
- Statistical properties appropriate to the intended purpose
- Examination for biases

While the AI RMF addresses data quality and bias (MEASURE 2.6, GOVERN 1.5), it does not impose the specific statutory data governance obligations of Art. 10, which have regulatory force.

**Action required:** Implement a formal data governance program specifically aligned with Art. 10 requirements. Document dataset characteristics, data lineage, bias testing methodology, and corrective measures taken.

### 3.6 Fundamental Rights Impact Assessment (Art. 27)

Deployers of high-risk AI systems that are public bodies, or private entities providing public services in certain categories (credit, insurance, education, employment, essential services), must conduct a Fundamental Rights Impact Assessment (FRIA) prior to deployment.

The AI RMF does not include a fundamental rights assessment. Its fairness and bias considerations (MAP 5.x, MEASURE 2.6) are narrower and not rights-based in the legal sense.

**Action required:** Determine whether your organization is subject to the FRIA requirement. If so, develop and document a FRIA methodology covering the AI system's impact on the rights enumerated in the EU Charter of Fundamental Rights. Notify relevant supervisory bodies where required.

### 3.7 Specific Obligations for General-Purpose AI (GPAI) Models (Arts. 51–56)

The EU AI Act introduces a separate regulatory regime for General-Purpose AI (GPAI) models — including large language models and foundation models — distinct from the requirements for specific AI systems:

- **All GPAI providers**: Must maintain technical documentation, provide model information to downstream providers, and comply with copyright rules.
- **Systemic-risk GPAI providers** (training compute > 10^25 FLOPs or designated by the Commission): Must conduct adversarial testing, report serious incidents to the Commission, ensure cybersecurity protections, and report on energy consumption.

The AI RMF does not distinguish between GPAI/foundation models and narrow AI systems, and does not address supply-chain-level model obligations.

**Action required:** Identify whether your organization develops or deploys GPAI models. If developing, prepare technical documentation per Annex XI/XII and implement copyright compliance procedures. If operating a systemic-risk model, establish adversarial testing programs and incident reporting to the AI Office.

### 3.8 Serious Incident Reporting to Authorities (Art. 73)

Providers must report serious incidents (death, serious injury, environmental damage, significant disruption of critical infrastructure, or violations of fundamental rights) to national market surveillance authorities within defined timeframes (typically 15 days for death/serious injury, 3 months for other serious incidents). Deployers must notify providers.

The AI RMF includes incident response practices (RESPOND 1.3) but does not specify regulatory reporting timelines or the specific thresholds triggering mandatory notification.

**Action required:** Establish a formal incident classification process that maps to EU AI Act severity thresholds. Implement reporting workflows with defined escalation paths and timelines. Identify the competent national market surveillance authority.

### 3.9 Obligations Specific to Deployers (Art. 26)

The EU AI Act distinguishes between providers and deployers and imposes specific duties on deployers:
- Use AI systems in accordance with instructions for use.
- Assign human oversight to competent individuals.
- Monitor AI system operation and report issues to providers.
- Inform affected workers or their representatives about AI use.
- For employment/education use cases: inform natural persons subject to the AI system.

The AI RMF is largely organization-centric and does not map to the provider/deployer legal distinction.

**Action required:** Clearly determine your role (provider, deployer, or both) for each AI system. Implement deployer-specific obligations including worker notification, human oversight assignment, and operational monitoring tied to provider instructions.

### 3.10 AI Literacy Requirements (Art. 4)

Providers and deployers must ensure a sufficient level of AI literacy among their staff and persons who operate AI systems on their behalf.

The AI RMF addresses organizational culture and governance (GOVERN 1.4, GOVERN 6.2) but does not mandate a formal AI literacy program.

**Action required:** Develop and implement a documented AI literacy program. Define minimum competency standards by role and maintain training records demonstrating compliance.

### 3.11 Market Surveillance and Enforcement Cooperation (Arts. 74–100)

The EU AI Act establishes national competent authorities, a European AI Office, and an AI Board with enforcement powers including:
- Requesting documentation and conducting audits
- Ordering corrective actions, market withdrawals, and recalls
- Imposing fines (up to EUR 35 million or 7% of global turnover for prohibited practice violations)

The AI RMF has no enforcement dimension whatsoever.

**Action required:** Designate a point of contact for regulatory inquiries. Ensure documentation is audit-ready and accessible. Prepare response procedures for potential market surveillance authority requests.

---

## 4. Harmonized Standards and AI RMF as Compliance Evidence

The EU AI Act permits providers to demonstrate conformity through adherence to harmonized European standards once published (Art. 40). CEN-CENELEC Joint Technical Committee JTC 21 is developing harmonized standards, and NIST AI RMF practices may serve as evidence of conformity for certain requirements — particularly around risk management systems, data governance, and transparency — once mapping is established through standardization work.

However, until harmonized standards are finalized and formally referenced in the EU Official Journal, organizations should treat AI RMF implementation as a compliance input, not a substitute for direct EU AI Act compliance analysis.

---

## 5. Prioritized Action Plan

For organizations implementing AI RMF that also need to achieve EU AI Act compliance, the following priorities are recommended:

**Immediate (before August 2026 full applicability):**

1. Classify all AI systems against EU AI Act risk tiers; identify any prohibited use cases and cease or redesign them.
2. Identify all high-risk AI systems per Annex I and Annex III; map provider vs. deployer roles.
3. Conduct fundamental rights impact assessments where required.
4. Register high-risk systems in the EU AI database.

**Short-term (establish compliance infrastructure):**

5. Develop Annex IV technical documentation for all high-risk AI systems.
6. Implement Art. 10-compliant data governance processes.
7. Establish conformity assessment procedures; engage notified bodies where required.
8. Prepare EU Declarations of Conformity and CE marking workflows.

**Ongoing:**

9. Implement post-market monitoring systems (Art. 72) integrated with RESPOND function practices.
10. Establish serious incident reporting procedures and test escalation paths.
11. Deploy AI literacy program and maintain training records.
12. Monitor GPAI model obligations if applicable; prepare technical documentation.
13. Maintain audit-readiness; assign regulatory liaison responsibilities.

---

## 6. Summary Table: AI RMF to EU AI Act Mapping

| EU AI Act Requirement | AI RMF Coverage | Gap Level |
|---|---|---|
| Risk-based classification | Partial (MAP function) | Medium — RMF lacks legal tier definitions |
| Prohibited practices screening | None | Critical |
| Risk management system (Art. 9) | Strong (MAP + MEASURE + RESPOND) | Low |
| Data governance (Art. 10) | Partial (MEASURE 2.6) | Medium |
| Technical documentation (Art. 11) | Partial (GOVERN 1.7, MEASURE 2.5) | Medium |
| Logging and record-keeping (Art. 12) | Partial (MEASURE 2.5) | Medium |
| Transparency (Art. 13) | Partial (GOVERN 4.1) | Medium |
| Human oversight (Art. 14) | Partial (GOVERN 5.1) | Low-Medium |
| Accuracy, robustness, cybersecurity (Art. 15) | Partial (MEASURE 2.x) | Medium |
| Conformity assessment (Art. 43) | None | High |
| EU Declaration of Conformity (Art. 47) | None | High |
| CE marking (Art. 49) | None | High |
| EU database registration (Art. 71) | None | High |
| Post-market monitoring (Art. 72) | Partial (RESPOND 2.1) | Low-Medium |
| Serious incident reporting (Art. 73) | Partial (RESPOND 1.3) | Medium-High |
| Deployer-specific obligations (Art. 26) | Partial | Medium |
| GPAI model obligations (Arts. 51–56) | None | High (if applicable) |
| Fundamental rights impact assessment (Art. 27) | None | High (if applicable) |
| AI literacy (Art. 4) | Partial (GOVERN 1.4) | Medium |
| Enforcement cooperation | None | Procedural |

**Gap levels:** Low = minor supplementation needed; Medium = additional documentation/processes required; High = significant new compliance work required; Critical = potential legal violation if unaddressed.

---

## Conclusion

The NIST AI RMF provides a strong risk management foundation that aligns well with the EU AI Act's risk management system requirements, transparency expectations, and human oversight principles. However, the AI RMF is a voluntary management tool, not a compliance framework, and implementing it alone does not satisfy EU AI Act legal obligations.

The most critical gaps are: prohibited practices screening, mandatory conformity assessment, CE marking, EU database registration, GPAI-specific obligations, and formal fundamental rights impact assessments. Organizations should treat AI RMF implementation as the operational backbone of their AI governance program while layering EU AI Act-specific legal requirements on top of that foundation.

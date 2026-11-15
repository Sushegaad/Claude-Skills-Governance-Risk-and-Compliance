# NIST AI RMF 1.0 — Full Category and Subcategory Reference

Source: NIST AI 100-1 (January 2023), Section 5 (Tables 1-4), and the AI RMF Playbook (suggested actions). Category and subcategory text below is verbatim from NIST AI 100-1; suggested actions are implementation guidance in the Playbook's style.

---

## GOVERN Function (6 Categories, 19 Subcategories)

GOVERN establishes the organizational culture, policies, accountability, and risk tolerance that underpin all other functions. It should be addressed first and revisited continuously.

### GV-1: Policies, Processes, Procedures, and Practices

**NIST category text (verbatim):** Policies, processes, procedures, and practices across the organization related to the mapping, measuring, and managing of AI risks are in place, transparent, and implemented effectively.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| GV-1.1 | Legal and regulatory requirements involving AI are understood, managed, and documented. |
| GV-1.2 | The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices. |
| GV-1.3 | Processes, procedures, and practices are in place to determine the needed level of risk management activities based on the organization's risk tolerance. |
| GV-1.4 | The risk management process and its outcomes are established through transparent policies, procedures, and other controls based on organizational risk priorities. |
| GV-1.5 | Ongoing monitoring and periodic review of the risk management process and its outcomes are planned and organizational roles and responsibilities clearly defined, including determining the frequency of periodic review. |
| GV-1.6 | Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities. |
| GV-1.7 | Processes and procedures are in place for decommissioning and phasing out AI systems safely and in a manner that does not increase risks or decrease the organization’s trustworthiness. |

**Suggested Actions:**
- Publish an organization-wide AI Risk Management Policy signed by senior leadership (GV-1.4)
- Maintain a regulatory register for applicable AI laws (EU AI Act, state AI laws, sector-specific requirements) and designate a legal/compliance owner for it (GV-1.1)
- Define AI risk appetite and risk tolerance statements (e.g., acceptable false positive rates, bias thresholds) and link them to specific bias and accuracy thresholds in testing requirements (GV-1.3)
- Define risk tolerance per AI system category (e.g., low-stakes recommendations vs. high-stakes decisions affecting individuals) and build a deployment checklist that validates an AI system against stated risk tolerance before launch (GV-1.3)
- Incorporate AI risk into existing ERM committee agendas and quarterly reviews (GV-1.4)
- Establish a policy review cycle (minimum annual) with a designated AI risk owner (GV-1.5)
- Maintain an AI system inventory resourced according to risk priorities, with minimum fields: system name/owner, purpose, model provenance, data categories, lifecycle stage, risk tier (GV-1.6)
- Define safe decommissioning procedures for AI systems being retired or replaced (GV-1.7)
- Align AI risk policies to NIST AI 100-1, ISO/IEC 42001, and relevant sector frameworks (FINRA, HIPAA, etc.) (GV-1.1, GV-1.2)

---

### GV-2: Accountability Structures

**NIST category text (verbatim):** Accountability structures are in place so that the appropriate teams and individuals are empowered, responsible, and trained for mapping, measuring, and managing AI risks.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| GV-2.1 | Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams throughout the organization. |
| GV-2.2 | The organization’s personnel and partners receive AI risk management training to enable them to perform their duties and responsibilities consistent with related policies, procedures, and agreements. |
| GV-2.3 | Executive leadership of the organization takes responsibility for decisions about risks associated with AI system development and deployment. |

**Suggested Actions:**
- Appoint an AI Risk Owner or Chief AI Officer with board-level reporting (GV-2.3)
- Define RACI for AI development, deployment, and monitoring decisions (GV-2.1)
- Create an AI roles register mapping each lifecycle stage to a responsible team or individual (GV-2.1)
- Ensure business owners (not just engineers) are accountable for deployed AI outcomes (GV-2.1, GV-2.3)
- Deliver AI risk management training to personnel and partners, matched to their roles (GV-2.2)
- Include AI risk in executive performance goals and leadership dashboards (GV-2.3)

---

### GV-3: Workforce Diversity, Equity, Inclusion, and Accessibility

**NIST category text (verbatim):** Workforce diversity, equity, inclusion, and accessibility processes are prioritized in the mapping, measuring, and managing of AI risks throughout the lifecycle.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| GV-3.1 | Decision-making related to mapping, measuring, and managing AI risks throughout the lifecycle is informed by a diverse team (e.g., diversity of demographics, disciplines, experience, expertise, and backgrounds). |
| GV-3.2 | Policies and procedures are in place to define and differentiate roles and responsibilities for human-AI configurations and oversight of AI systems. |

**Suggested Actions:**
- Staff AI risk decision-making with diverse teams across demographics, disciplines, experience, expertise, and backgrounds (GV-3.1)
- Include cross-functional perspectives (AI/ML, legal, privacy, security, HR, ethics) in AI system design reviews (GV-3.1)
- Define and differentiate roles and responsibilities for human-AI configurations: who operates, who oversees, who can override (GV-3.2)
- Assign responsibilities for AI oversight to both technical and non-technical roles (GV-3.2)

---

### GV-4: Culture of Risk Consideration and Communication

**NIST category text (verbatim):** Organizational teams are committed to a culture that considers and communicates AI risk.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| GV-4.1 | Organizational policies and practices are in place to foster a critical thinking and safety-first mindset in the design, development, deployment, and uses of AI systems to minimize potential negative impacts. |
| GV-4.2 | Organizational teams document the risks and potential impacts of the AI technology they design, develop, deploy, evaluate, and use, and they communicate about the impacts more broadly. |
| GV-4.3 | Organizational practices are in place to enable AI testing, identification of incidents, and information sharing. |

**Suggested Actions:**
- Establish an AI Risk Working Group with quarterly cross-functional reviews (GV-4.1, GV-4.2)
- Create an AI risk escalation path from development teams to executive leadership (GV-4.2)
- Require teams to document risks and potential impacts of the AI they build and use, and communicate them beyond the immediate team (GV-4.2)
- Enable AI testing, incident identification, and information sharing practices (e.g., internal incident log, participation in AI incident databases) (GV-4.3)

---

### GV-5: Engagement with Relevant AI Actors

**NIST category text (verbatim):** Processes are in place for robust engagement with relevant AI actors.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| GV-5.1 | Organizational policies and practices are in place to collect, consider, prioritize, and integrate feedback from those external to the team that developed or deployed the AI system regarding the potential individual and societal impacts related to AI risks. |
| GV-5.2 | Mechanisms are established to enable the team that developed or deployed AI systems to regularly incorporate adjudicated feedback from relevant AI actors into system design and implementation. |

**Suggested Actions:**
- Implement external feedback channels (e.g., complaint form, user reporting mechanism, community engagement sessions) for individual and societal impact concerns (GV-5.1)
- Define a process to collect, consider, prioritize, and integrate feedback from parties external to the development or deployment team (GV-5.1)
- Establish a mechanism for adjudicating external feedback and feeding accepted items into system design and implementation on a regular cadence (GV-5.2)

---

### GV-6: Third-Party and Supply Chain Risk

**NIST category text (verbatim):** Policies and procedures are in place to address AI risks and benefits arising from third-party software and data and other supply chain issues.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| GV-6.1 | Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party’s intellectual property or other rights. |
| GV-6.2 | Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk. |

**Suggested Actions:**
- Define responsibilities and contractual requirements for external AI vendors and third-party model providers, including IP infringement risk (GV-6.1)
- Maintain a register of third-party AI software, data, and pre-trained models with associated risk assessments (GV-6.1)
- Define contingency and fallback processes for failures or incidents in high-risk third-party data or AI systems (e.g., documented fallback to a prior model version) (GV-6.2)

---

## MAP Function (5 Categories, 18 Subcategories)

MAP establishes context before risks are measured or managed. A well-executed MAP prevents investing resources in the wrong risk treatments.

### MP-1: Context Is Established and Understood

**NIST category text (verbatim):** Context is established and understood.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MP-1.1 | Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. Considerations include: the specific set or types of users along with their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations about AI system purposes, uses, and risks across the development or product AI lifecycle; and related TEVV and system metrics. |
| MP-1.2 | Interdisciplinary AI actors, competencies, skills, and capacities for establishing context reflect demographic diversity and broad domain and user experience expertise, and their participation is documented. Opportunities for interdisciplinary collaboration are prioritized. |
| MP-1.3 | The organization’s mission and relevant goals for AI technology are understood and documented. |
| MP-1.4 | The business value or context of business use has been clearly defined or – in the case of assessing existing AI systems – re-evaluated. |
| MP-1.5 | Organizational risk tolerances are determined and documented. |
| MP-1.6 | System requirements (e.g., “the system shall respect the privacy of its users”) are elicited from and understood by relevant AI actors. Design decisions take socio-technical implications into account to address AI risks. |

**Suggested Actions:**
- Produce an AI System Description Document for each deployed system covering: purpose, intended uses, inputs, outputs, decision authority, operator vs. user roles, and applicable laws and norms (MP-1.1)
- Identify affected populations at the beginning of design, not at deployment (MP-1.1)
- Document prohibited use cases explicitly (MP-1.1)
- Document interdisciplinary participation in context-setting, reflecting demographic diversity and broad domain expertise (MP-1.2)
- Document the organizational mission, goals, and business value for each AI system, and re-evaluate when assessing existing systems (MP-1.3, MP-1.4)
- Document organizational risk tolerances and the system requirements elicited from relevant AI actors (MP-1.5, MP-1.6)

---

### MP-2: Categorization of the AI System

**NIST category text (verbatim):** Categorization of the AI system is performed.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MP-2.1 | The specific tasks and methods used to implement the tasks that the AI system will support are defined (e.g., classifiers, generative models, recommenders). |
| MP-2.2 | Information about the AI system’s knowledge limits and how system output may be utilized and overseen by humans is documented. Documentation provides sufficient information to assist relevant AI actors when making decisions and taking subsequent actions. |
| MP-2.3 | Scientific integrity and TEVV considerations are identified and documented, including those related to experimental design, data collection and selection (e.g., availability, representativeness, suitability), system trustworthiness, and construct validation. |

**Suggested Actions:**
- Define and document the system type and methods (classifier, generative model, recommender, etc.) (MP-2.1)
- Document model card or system card information including training data sources, known biases, knowledge limits, and performance bounds (MP-2.2, MP-2.3)
- Document how humans will use and oversee system output (MP-2.2)
- Review relevant literature on known failure modes for the model architecture in use, and document TEVV considerations including data representativeness and construct validation (MP-2.3)

---

### MP-3: Capabilities, Usage, Goals, Benefits, and Costs

**NIST category text (verbatim):** AI capabilities, targeted usage, goals, and expected benefits and costs compared with appropriate benchmarks are understood.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MP-3.1 | Potential benefits of intended AI system functionality and performance are examined and documented. |
| MP-3.2 | Potential costs, including non-monetary costs, which result from expected or realized AI errors or system functionality and trustworthiness – as connected to organizational risk tolerance – are examined and documented. |
| MP-3.3 | Targeted application scope is specified and documented based on the system’s capability, established context, and AI system categorization. |
| MP-3.4 | Processes for operator and practitioner proficiency with AI system performance and trustworthiness – and relevant technical standards and certifications – are defined, assessed, and documented. |
| MP-3.5 | Processes for human oversight are defined, assessed, and documented in accordance with organizational policies from the govern function. |

**Suggested Actions:**
- Document expected benefits and costs (including non-monetary costs of errors) against appropriate benchmarks, tied to organizational risk tolerance (MP-3.1, MP-3.2)
- Specify and document the targeted application scope; keep it bounded by demonstrated capability and context (MP-3.3)
- Define operator and practitioner proficiency requirements and relevant technical standards or certifications (MP-3.4)
- Define, assess, and document human oversight processes consistent with GOVERN policies (MP-3.5)

---

### MP-4: Risks and Benefits for All Components, Including Third Party

**NIST category text (verbatim):** Risks and benefits are mapped for all components of the AI system including third-party software and data.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MP-4.1 | Approaches for mapping AI technology and legal risks of its components – including the use of third-party data or software – are in place, followed, and documented, as are risks of infringement of a third party’s intellectual property or other rights. |
| MP-4.2 | Internal risk controls for components of the AI system, including third-party AI technologies, are identified and documented. |

**Suggested Actions:**
- Map legal and technology risks for every system component, including third-party data, software, and pre-trained models, and IP infringement risk (MP-4.1)
- Identify and document internal risk controls for each component, including third-party AI technologies (MP-4.2)
- Maintain a component inventory (data sources, models, libraries, APIs) with risk and control status per component (MP-4.1, MP-4.2)

---

### MP-5: Impacts to Individuals, Groups, Communities, Organizations, and Society

**NIST category text (verbatim):** Impacts to individuals, groups, communities, organizations, and society are characterized.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MP-5.1 | Likelihood and magnitude of each identified impact (both potentially beneficial and harmful) based on expected use, past uses of AI systems in similar contexts, public incident reports, feedback from those external to the team that developed or deployed the AI system, or other data are identified and documented. |
| MP-5.2 | Practices and personnel for supporting regular engagement with relevant AI actors and integrating feedback about positive, negative, and unanticipated impacts are in place and documented. |

**Suggested Actions:**
- Conduct red-team exercises and adversarial testing to estimate real-world failure rates and likelihood of harm (MP-5.1)
- Assess impact across harm dimensions: physical safety, financial, psychological, reputational, societal (MP-5.1)
- Use historical data, public incident reports, and expert judgment to estimate likelihood and magnitude of each identified impact (MP-5.1)
- For large-scale deployments, model aggregate societal effects (e.g., labour market impact of an automated hiring tool) (MP-5.1)
- Create a stakeholder risk/benefit matrix: rows = stakeholder group, columns = risk type, benefit type (MP-5.1)
- Implement a feedback channel (e.g., complaint form, audit log review) for users and affected communities to report unexpected outcomes, with named personnel to run regular engagement (MP-5.2)
- Conduct equity analysis: which groups are disproportionately affected by errors? (MP-5.1)

---

## MEASURE Function (4 Categories, 22 Subcategories)

MEASURE employs quantitative, qualitative, and mixed-method tools to analyze, assess, benchmark, and monitor AI risks identified in MAP.

### MS-1: Appropriate Methods and Metrics

**NIST category text (verbatim):** Appropriate methods and metrics are identified and applied.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MS-1.1 | Approaches and metrics for measurement of AI risks enumerated during the map function are selected for implementation starting with the most significant AI risks. The risks or trustworthiness characteristics that will not – or cannot – be measured are properly documented. |
| MS-1.2 | Appropriateness of AI metrics and effectiveness of existing controls are regularly assessed and updated, including reports of errors and potential impacts on affected communities. |
| MS-1.3 | Internal experts who did not serve as front-line developers for the system and/or independent assessors are involved in regular assessments and updates. Domain experts, users, AI actors external to the team that developed or deployed the AI system, and affected communities are consulted in support of assessments as necessary per organizational risk tolerance. |

**Suggested Actions:**
- Define metrics for each trustworthiness characteristic: accuracy, fairness (demographic parity, equalized odds), robustness (adversarial accuracy), explainability (LIME/SHAP scores), privacy (differential privacy ε), starting with the most significant risks (MS-1.1)
- Document risks or characteristics that will not or cannot be measured, and why (MS-1.1)
- Document measurement tools and their known limitations, and reassess metric appropriateness regularly including error reports and community impact (MS-1.2)
- Involve internal experts who were not front-line developers, or independent assessors, in regular assessments; consult domain experts, users, and affected communities as risk tolerance requires (MS-1.3)
- Identify where human evaluation is required instead of (or in addition to) automated metrics (MS-1.1, MS-1.3)

---

### MS-2: Evaluation for Trustworthy Characteristics

**NIST category text (verbatim):** AI systems are evaluated for trustworthy characteristics.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MS-2.1 | Test sets, metrics, and details about the tools used during TEVV are documented. |
| MS-2.2 | Evaluations involving human subjects meet applicable requirements (including human subject protection) and are representative of the relevant population. |
| MS-2.3 | AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented. |
| MS-2.4 | The functionality and behavior of the AI system and its components – as identified in the map function – are monitored when in production. |
| MS-2.5 | The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented. |
| MS-2.6 | The AI system is evaluated regularly for safety risks – as identified in the map function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures. |
| MS-2.7 | AI system security and resilience – as identified in the map function – are evaluated and documented. |
| MS-2.8 | Risks associated with transparency and accountability – as identified in the map function – are examined and documented. |
| MS-2.9 | The AI model is explained, validated, and documented, and AI system output is interpreted within its context – as identified in the map function – to inform responsible use and governance. |
| MS-2.10 | Privacy risk of the AI system – as identified in the map function – is examined and documented. |
| MS-2.11 | Fairness and bias – as identified in the map function – are evaluated and results are documented. |
| MS-2.12 | Environmental impact and sustainability of AI model training and management activities – as identified in the map function – are assessed and documented. |
| MS-2.13 | Effectiveness of the employed TEVV metrics and processes in the measure function are evaluated and documented. |

**Suggested Actions:**
- Require a pre-deployment evaluation report covering all seven trustworthiness characteristics, with documented test sets, metrics, and tools (MS-2.1, MS-2.3)
- Ensure evaluations involving human subjects meet human subject protection requirements and are representative (MS-2.2)
- Demonstrate validity and reliability for conditions similar to the deployment setting, and document generalizability limits (MS-2.3, MS-2.5)
- Monitor system functionality and behavior in production (MS-2.4)
- Evaluate safety regularly, including fail-safe behavior beyond knowledge limits and response times for failures (MS-2.6)
- Test adversarial robustness using standard benchmark datasets relevant to the model type (MS-2.7)
- Run disaggregated performance testing across demographic subgroups (age, gender, race, geography) (MS-2.11)
- Document SHAP/LIME explanations for models affecting high-stakes individual decisions (MS-2.9)
- Examine and document transparency/accountability risks, privacy risk, and environmental impact of training and operations (MS-2.8, MS-2.10, MS-2.12)
- Evaluate and document the effectiveness of the TEVV metrics and processes themselves (MS-2.13)

---

### MS-3: Mechanisms for Tracking Identified AI Risks

**NIST category text (verbatim):** Mechanisms for tracking identified AI risks over time are in place.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MS-3.1 | Approaches, personnel, and documentation are in place to regularly identify and track existing, unanticipated, and emergent AI risks based on factors such as intended and actual performance in deployed contexts. |
| MS-3.2 | Risk tracking approaches are considered for settings where AI risks are difficult to assess using currently available measurement techniques or where metrics are not yet available. |
| MS-3.3 | Feedback processes for end users and impacted communities to report problems and appeal system outcomes are established and integrated into AI system evaluation metrics. |

**Suggested Actions:**
- Implement model monitoring dashboards tracking accuracy, fairness metrics, and input data distribution (MS-3.1)
- Set alert thresholds that trigger human review (e.g., accuracy drops >5%, demographic parity gap exceeds threshold) (MS-3.1)
- Assign a model owner responsible for monthly monitoring reviews, including unanticipated and emergent risks (MS-3.1)
- Define qualitative tracking approaches for risks that current measurement techniques cannot assess (MS-3.2)
- Establish end-user and impacted-community channels to report problems and appeal outcomes, and integrate them into evaluation metrics (MS-3.3)
- Subscribe to NIST NVD and relevant AI safety/bias research feeds to inform risk tracking (MS-3.1)

---

### MS-4: Feedback About Efficacy of Measurement

**NIST category text (verbatim):** Feedback about efficacy of measurement is gathered and assessed.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MS-4.1 | Measurement approaches for identifying AI risks are connected to deployment context(s) and informed through consultation with domain experts and other end users. Approaches are documented. |
| MS-4.2 | Measurement results regarding AI system trustworthiness in deployment context(s) and across the AI lifecycle are informed by input from domain experts and relevant AI actors to validate whether the system is performing consistently as intended. Results are documented. |
| MS-4.3 | Measurable performance improvements or declines based on consultations with relevant AI actors, including affected communities, and field data about context-relevant risks and trustworthiness characteristics are identified and documented. |

**Suggested Actions:**
- Connect measurement approaches to each deployment context through consultation with domain experts and end users, and document the approaches (MS-4.1)
- Validate measurement results with domain experts and relevant AI actors to confirm the system performs consistently as intended (MS-4.2)
- Identify and document measurable performance improvements or declines using field data and consultations with affected communities (MS-4.3)
- Create a measurement-to-action protocol: define which measurement findings trigger which MANAGE actions, and include measurement uncertainty caveats in all AI risk reports (MS-4.2, MS-4.3)
- Automate risk register updates from monitoring dashboards where feasible (MS-4.3)

---

## MANAGE Function (4 Categories, 13 Subcategories)

MANAGE allocates risk resources to mapped and measured risks on a regular basis and as defined by GOVERN.

### MG-1: Prioritizing, Responding to, and Managing AI Risks

**NIST category text (verbatim):** AI risks based on assessments and other analytical output from the MAP and MEASURE functions are prioritized, responded to, and managed

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MG-1.1 | A determination is made as to whether the AI system achieves its intended purposes and stated objectives and whether its development or deployment should proceed. |
| MG-1.2 | Treatment of documented AI risks is prioritized based on impact, likelihood, and available resources or methods. |
| MG-1.3 | Responses to the AI risks deemed high priority, as identified by the map function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting. |
| MG-1.4 | Negative residual risks (defined as the sum of all unmitigated risks) to both downstream acquirers of AI systems and end users are documented. |

**Suggested Actions:**
- Make an explicit go/no-go determination: does the system achieve its intended purpose, and should development or deployment proceed? (MG-1.1)
- Use a severity, breadth, and reversibility scoring model for risk treatment prioritization (MG-1.2)
- Flag any risk that affects a protected class, creates legal exposure, or is irreversible as high-priority (MG-1.2)
- Assign a treatment owner, target date, and treatment approach (mitigate, transfer, avoid, accept) for every high-priority risk register entry (MG-1.3)
- Document negative residual risks to downstream acquirers and end users, and require senior approval for accepting residual risk above the defined risk tolerance threshold (MG-1.4)
- Review prioritization and residual risk acceptance at each model version update or significant context change (MG-1.2, MG-1.4)

---

### MG-2: Strategies to Maximize Benefits and Minimize Negative Impacts

**NIST category text (verbatim):** Strategies to maximize AI benefits and minimize negative impacts are planned, prepared, implemented, documented, and informed by input from relevant AI actors.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MG-2.1 | Resources required to manage AI risks are taken into account – along with viable non-AI alternative systems, approaches, or methods – to reduce the magnitude or likelihood of potential impacts. |
| MG-2.2 | Mechanisms are in place and applied to sustain the value of deployed AI systems. |
| MG-2.3 | Procedures are followed to respond to and recover from a previously unknown risk when it is identified. |
| MG-2.4 | Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use. |

**Suggested Actions:**
- For each high-priority risk, identify one or more treatment options: technical (retrain, constrain, add human review), operational (restrict use case), contractual (indemnification), or avoidance (decommission); consider viable non-AI alternatives (MG-2.1)
- Put mechanisms in place to sustain the value of deployed systems (maintenance, retraining cadence, data pipeline health) (MG-2.2)
- Define procedures to respond to and recover from previously unknown risks when identified (MG-2.3)
- Define a "kill switch" or emergency shutdown/deactivation procedure, with assigned responsibilities, for AI systems whose performance or outcomes are inconsistent with intended use (MG-2.4)
- Document benefit-risk tradeoffs for any accepted risk (MG-2.1)

---

### MG-3: Managing Third-Party Risks and Benefits

**NIST category text (verbatim):** AI risks and benefits from third-party entities are managed.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MG-3.1 | AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented. |
| MG-3.2 | Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance. |

**Suggested Actions:**
- Regularly monitor third-party resources (vendor models, external data, APIs) and apply and document risk controls (MG-3.1)
- Include contractual change-notification and audit rights for vendor-hosted models, and benchmark them against internal champion models (MG-3.1)
- Monitor pre-trained models used in development as part of regular system monitoring and maintenance, including upstream version changes (MG-3.2)

---

### MG-4: Risk Treatments and Communication Plans Documented and Monitored

**NIST category text (verbatim):** Risk treatments, including response and recovery, and communication plans for the identified and measured AI risks are documented and monitored regularly.

| Subcategory | Description (verbatim NIST text) |
|-------------|----------------------------------|
| MG-4.1 | Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management. |
| MG-4.2 | Measurable activities for continual improvements are integrated into AI system updates and include regular engagement with interested parties, including relevant AI actors. |
| MG-4.3 | Incidents and errors are communicated to relevant AI actors, including affected communities. Processes for tracking, responding to, and recovering from incidents and errors are followed and documented. |

**Suggested Actions:**
- Implement post-deployment monitoring plans covering user input capture, appeal and override, decommissioning, incident response, recovery, and change management (MG-4.1)
- Implement an AI incident log with severity classification (low/medium/high/critical) (MG-4.3)
- Define notification thresholds: internal escalation, external customer notification, regulatory disclosure, and communicate incidents to affected communities (MG-4.3)
- Conduct post-incident reviews and update the risk register and GOVERN policies (MG-4.3)
- Integrate measurable continual-improvement activities into system updates, with regular engagement of interested parties (MG-4.2)
- Schedule quarterly AI risk programme reviews covering all four functions, and use external assessment or third-party audit every 1-2 years to validate programme effectiveness (MG-4.1, MG-4.2)
- Share anonymized incident learnings with industry where appropriate (e.g., AI incident databases) (MG-4.3)

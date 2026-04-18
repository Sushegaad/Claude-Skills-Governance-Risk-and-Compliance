# ISO/IEC 42001:2023 — Mandatory Clause Requirements (Clauses 4–10)

All clauses are mandatory regardless of organisational size, sector, or role (provider or user). This reference covers each clause in detail with required outputs, audit evidence, and common nonconformities.

---

## Clause 4 — Context of the Organisation

### 4.1 Understanding the Organisation and Its Context
**Requirement:** Determine external and internal issues relevant to the AIMS purpose and that affect the ability to achieve intended outcomes. Include AI-specific factors: regulatory environment, societal expectations of AI, market pressures to adopt AI, and technology risks.

**Required outputs:**
- Environmental/contextual analysis (PESTLE or equivalent) covering AI dimensions
- List of external issues: AI regulations (EU AI Act, national AI laws), public trust, competitive AI landscape
- List of internal issues: AI maturity, data infrastructure, staff competence, ethical culture

**Audit evidence:** Meeting minutes, strategic planning documents, AIMS scope document.

### 4.2 Understanding the Needs and Expectations of Interested Parties
**Requirement:** Identify all parties affected by or interested in the AIMS and their requirements.

**AI-specific interested parties:**
- Individuals affected by AI decisions (customers, citizens, employees)
- Regulators (data protection authorities, sector-specific regulators, AI regulators)
- AI model providers/vendors
- Civil society and advocacy groups
- Employees who interact with or are affected by AI
- Investors and insurers requiring AI governance assurance

**Required outputs:** Stakeholder register with requirements matrix.

### 4.3 Determining the Scope of the AIMS
**Requirement:** Document the boundary and applicability of the AIMS — which AI systems, processes, organisational units, and locations are in scope.

**Key scope decisions:**
- Which AI systems are in scope? (All? Only high-impact? Only AI systems developed in-house?)
- Are AI systems used by third parties on the organisation's behalf in scope?
- Which organisational functions (R&D, operations, customer service) are included?

**Required outputs:** AIMS Scope Document — must specify: what is included, what is explicitly excluded, and the justification for exclusions.

**Common nonconformity:** Scope excludes AI tools used in HR (e.g., AI screening tools) without documented justification.

### 4.4 AI Management System
**Requirement:** Establish, implement, maintain, and continually improve the AIMS including all processes and their interactions.

---

## Clause 5 — Leadership

### 5.1 Leadership and Commitment
**Requirement:** Top management must demonstrate active commitment to the AIMS — not just sign documents, but actively support AI governance as a strategic priority.

**Evidence of commitment:**
- AI policy approved and signed by senior leadership (CEO, Board, or equivalent)
- AI governance included in management meeting agendas
- Resources allocated for AIMS implementation
- AI-related KPIs/objectives set at leadership level

**Audit tip:** Auditors will interview top management — leaders must be able to explain the AIMS scope and their personal role in AI governance.

### 5.2 AI Policy
**Requirement:** Top management must establish an AI Policy that:
- Is appropriate to the organisation's purpose and context
- Provides a framework for setting AI objectives
- Includes commitment to responsible and ethical AI
- Includes commitment to comply with applicable requirements
- Includes commitment to continual improvement of the AIMS

**AI Policy must also address (ISO 42001-specific):**
- The organisation's responsible AI principles (fairness, transparency, accountability, safety, privacy, reliability, inclusivity)
- Commitment to conduct AI risk and impact assessments
- Human oversight of AI systems proportionate to risk/impact

**Required outputs:** AI Policy document (documented, communicated, available to interested parties as appropriate).

### 5.3 Organisational Roles, Responsibilities and Authorities
**Requirement:** Define roles accountable for AI governance.

**Minimum required roles:**
| Role | Responsibilities |
|------|----------------|
| AIMS Owner (top management) | Strategic accountability for AIMS; approves AI policy |
| AI Risk Owner (per AI system) | Accountable for AI risk assessment and treatment decisions |
| AI System Owner | Day-to-day management of specific AI system in scope |
| Data Governance Lead | Accountable for A.7 data controls |
| AIMS Internal Auditor | Conducts internal AIMS audits |
| AI Incident Manager | Manages AI-specific incident response |

**Required outputs:** RACI matrix or roles/responsibilities document; job descriptions updated.

---

## Clause 6 — Planning

### 6.1 Actions to Address Risks and Opportunities
**Requirement:** Plan how to address risks and opportunities relevant to the AIMS context and objectives.

#### 6.1.1 General
Determine risks and opportunities that could affect AIMS achievement. Plan actions to address them.

#### 6.1.2 AI Risk Assessment and AI System Impact Assessment (AISIA)
**This is the most distinctive clause in ISO 42001.** Two separate assessments are required:

**AI Risk Assessment:**
- Identify risks associated with AI systems (model risks, data risks, operational risks, supply chain risks)
- Assess likelihood and severity
- Determine treatment: modify, accept, avoid, or transfer
- Document results and decisions
- Must be repeated when AI systems change significantly or on a defined schedule

**AI System Impact Assessment (AISIA):**
- Assess potential impacts on individuals and society (not just organisational risk)
- Consider: who is affected, what decisions the AI makes, how severe and reversible the impact is
- Classify impact level (Low / Medium / High) → drives control selection
- Must be performed for each AI system in scope
- Must be updated when the AI system's purpose or operating context changes

**Required outputs:**
- AI Risk Assessment register (per AI system or per risk category)
- AISIA records (per AI system)
- Risk treatment decisions documented

**Common nonconformity:** AISIA completed once during implementation but never revisited; risk assessment covers organisational risk only, not AI-specific risks.

#### 6.1.3 AI Risk Treatment
**Requirement:** Select and implement risk treatment options for AI risks identified in 6.1.2. Prepare a risk treatment plan with ownership, timelines, and residual risk acceptance.

**Statement of Applicability (SoA):**
- List all 38 Annex A controls
- For each: applicable or not? Justification. Implementation status.
- Exclusions of applicable controls must be justified — "not currently a priority" is not sufficient

### 6.2 AI Objectives and Planning to Achieve Them
**Requirement:** Establish AI objectives at relevant functions and levels.

**AI objectives must be:**
- Consistent with the AI policy and responsible AI principles
- **Measurable** (not aspirational only)
- Monitored and communicated
- Updated as appropriate

**Examples of measurable AI objectives:**
- Achieve bias score below X across demographic groups in AI system Y by Q3
- Complete AISIA for all in-scope AI systems by [date]
- Achieve 100% AI awareness training completion for all staff by [date]
- Reduce AI incident mean time to resolution (MTTR) below X hours
- Achieve ISO 42001 certification by [date]

---

## Clause 7 — Support

### 7.1 Resources
**Requirement:** Provide resources needed for AIMS: budget, personnel, tooling, infrastructure.

**AI-specific resource considerations:**
- Data labelling/annotation capacity and quality assurance
- Model evaluation and testing infrastructure
- AI ethics expertise (internal or external)
- Legal and regulatory monitoring for AI law changes

### 7.2 Competence
**Requirement:** Determine competence needed for AI roles; provide training; evaluate effectiveness.

**Competence requirements by role:**
| Role | Competence Areas |
|------|----------------|
| AI developers | Responsible AI practices, fairness-aware ML, secure ML development |
| AI system operators | Understanding AI system limitations, human oversight procedures, incident detection |
| Compliance/risk staff | AIMS clause requirements, AISIA methodology, AI risk assessment |
| Procurement | AI-specific supplier due diligence, contractual AI requirements |
| All staff | AI acceptable use policy, what AI is being used for, how to report AI concerns |

**Required outputs:** Competence matrix, training records, training effectiveness evaluations.

### 7.3 Awareness
**Requirement:** All persons working under the organisation's authority must be aware of: the AI policy, their contribution to AIMS effectiveness, consequences of non-conformance.

### 7.4 Communication
**Requirement:** Determine internal and external communications relevant to AIMS: what to communicate, when, to whom, how.

**AI-specific communications:**
- External: transparency disclosures to AI-affected individuals (links to A.8.2 and A.8.5)
- Internal: AI incident alerts, policy updates, training announcements
- Regulatory: AI incident notifications where required

### 7.5 Documented Information
**Requirement:** Maintain and retain documented information required by ISO 42001, plus any the organisation determines necessary for AIMS effectiveness.

**Mandatory documented information (retain):**
- AIMS scope document
- AI policy
- AI risk assessment records
- AISIA records
- SoA
- AI objectives
- Internal audit reports and results
- Management review records
- Nonconformities and corrective actions

---

## Clause 8 — Operation

### 8.1 Operational Planning and Control
**Requirement:** Plan, implement, and control processes to meet AIMS requirements; implement control plans; manage planned changes; address unintended changes.

**Key operational controls:**
- AI system development follows documented lifecycle (A.6)
- Data governance controls applied (A.7)
- Impact assessments completed before deployment
- Change management process for AI systems — reassess risk/impact when systems change

### 8.2 AI Risk Assessment
**Requirement:** Execute AI risk assessments per the method established in 6.1.2. Retain documented results.

### 8.3 AI Risk Treatment
**Requirement:** Implement the risk treatment plan. Retain documented evidence of treatment.

---

## Clause 9 — Performance Evaluation

### 9.1 Monitoring, Measurement, Analysis and Evaluation
**Requirement:** Monitor and measure AI system performance, AIMS process effectiveness, and progress against AI objectives.

**Metrics to consider:**
- AI system performance metrics (accuracy, precision/recall, bias scores) vs defined thresholds
- AISIA completion rate across in-scope AI systems
- AI incident count, severity, and MTTR
- SoA control implementation progress
- Training completion rates
- Supplier AI assessment completion rates

**Required outputs:** Monitoring reports, dashboard or metrics register.

### 9.2 Internal Audit
**Requirement:** Conduct internal audits at planned intervals to determine AIMS conformance and effective implementation.

**Audit programme requirements:**
- Audit frequency defined (typically annual minimum)
- Auditor competence and independence — cannot audit own work
- Audit plan covering all AIMS clauses and applicable controls over the audit cycle
- Audit reports with findings, nonconformities, and opportunities for improvement
- Audit records retained

### 9.3 Management Review
**Requirement:** Top management reviews the AIMS at planned intervals.

**Management review agenda must cover:**
- Status of actions from previous reviews
- Changes in external/internal issues affecting the AIMS
- AI risk and impact assessment results
- Performance and metrics against AI objectives
- Internal audit results
- Nonconformities and corrective actions
- Opportunities for improvement

**Required outputs:** Management review minutes with decisions and action items.

---

## Clause 10 — Improvement

### 10.1 Continual Improvement
**Requirement:** Continually improve the suitability, adequacy, and effectiveness of the AIMS.

### 10.2 Nonconformity and Corrective Action
**Requirement:** When a nonconformity occurs: react, control, evaluate root cause, implement corrective action, review effectiveness.

**AI-specific nonconformity examples:**
- AI system deployed without completed AISIA
- Training data bias testing skipped for a model
- AI incident not reported within required timeframe
- Staff using public AI tools without following acceptable use policy
- Supplier AI assessment overdue

**Required outputs:** Nonconformity records, corrective action log with root cause, action taken, and effectiveness review.

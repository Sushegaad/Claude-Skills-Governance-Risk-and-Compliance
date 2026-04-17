# ISO 22301 Business Continuity Management System Skill

> A Claude skill for business continuity teams and risk professionals to implement,
> audit, and maintain a Business Continuity Management System (BCMS) under ISO 22301:2019.

---

## 1. What Does the Skill Do?

The ISO 22301 skill turns Claude into an expert ISO 22301 Lead Auditor and BCMS implementation
consultant. It provides structured, audit-ready guidance across the full business continuity
lifecycle — from initial gap assessment and Business Impact Analysis (BIA) through to BC
strategy design, plan authoring, exercise programmes, and certification readiness.

The skill is built on **ISO 22301:2019** (Security and resilience — Business continuity
management systems — Requirements), the current version of the international standard published
by ISO/TC 292. It understands all mandatory clauses (4–10), all mandatory documented information
requirements, and the operational methodology for BIA, risk assessment, BC strategy, and
exercising.

Outputs are matched to task type: structured gap analysis tables, full BCP documents with
activation procedures, BIA assessment forms, risk registers, exercise plans, management review
records, and certification readiness checklists.

---

## 2. Intended Audiences

This skill is designed for professionals responsible for business continuity management across
any sector. It is most useful for:

- **Business Continuity Managers** implementing or maintaining a BCMS for the first time or
  refreshing an existing programme
- **Risk Managers** integrating BC into the wider enterprise risk framework
- **Compliance and Audit professionals** performing BCMS gap assessments or preparing for
  ISO 22301 certification audits
- **IT Directors and DR teams** aligning IT Disaster Recovery with the broader BCMS requirement
- **Consultants** supporting organisations through BCMS scoping, BIA, strategy, planning, and
  certification
- **Operations Leaders** seeking to understand their continuity obligations and recovery
  objectives (RTO, RPO, MBCO)

---

## 3. Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| **Gap analysis** | "Perform a gap analysis of our BCMS against ISO 22301:2019. We have a scope statement and policy but no formal BIA or tested plans." |
| **BIA support** | "Help me conduct a BIA for our order management function. The team of 8 processes 500 orders per day using our ERP system." |
| **Recovery parameter advice** | "Our regulator requires all customer transactions to be processed within 24 hours. What RTO and RPO should we set for our order processing activity?" |
| **BC strategy design** | "Our BIA shows our CRM system has an RTO of 4 hours and RPO of 1 hour. What BC strategies should we consider?" |
| **BCP authoring** | "Write a Business Continuity Plan for our finance department covering the payment processing activity. MBCO is 100% of daily payment runs within 4 hours." |
| **Incident Response Plan** | "Write an Incident Response Plan structure with level-based escalation, CMT roles, and communication procedures." |
| **Exercise planning** | "Plan a tabletop exercise to test our IT failure response. I need participants, scenario, objectives, and success criteria." |
| **Certification readiness** | "What mandatory documents must we have in place before a Stage 1 ISO 22301:2019 audit?" |
| **Management review prep** | "What inputs and outputs does ISO 22301:2019 require for a management review? Generate an agenda template." |
| **Policy generation** | "Write a Business Continuity Policy for our company that satisfies Clause 5.2 of ISO 22301:2019." |
| **Terminology explanation** | "Explain the difference between MTPD, RTO, RPO, and MBCO in the context of ISO 22301." |

---

## 4. Key Concepts Covered

### The BCMS Lifecycle

The ISO 22301:2019 standard structures the BCMS around a Plan-Do-Check-Act (PDCA) cycle
embedded within the High Level Structure (Clauses 4–10):

```
PLAN                          DO                           CHECK               ACT
Context (Cl.4)    -->    BIA + Risk (Cl.8.2)    -->    Monitor (Cl.9.1)  -->  Improve (Cl.10)
Leadership (Cl.5) -->    BC Strategy (Cl.8.3)   -->    Audit (Cl.9.2)
Planning (Cl.6)   -->    BC Plans (Cl.8.4)      -->    Mgmt Review (Cl.9.3)
Support (Cl.7)    -->    Exercises (Cl.8.5)
```

### Key ISO 22301 Terms

| Term | Meaning |
|------|---------|
| **MTPD** | Maximum Tolerable Period of Disruption — the hard deadline: recovery must happen before this point or the organisation faces unacceptable consequences |
| **RTO** | Recovery Time Objective — the target time to resume an activity after a disruption; must be less than MTPD |
| **RPO** | Recovery Point Objective — how much data loss is acceptable; drives backup and replication strategy |
| **MBCO** | Minimum Business Continuity Objective — the minimum level of service needed at recovery; enables phased restoration |
| **BIA** | Business Impact Analysis — the process of identifying critical activities, assessing disruption impacts, and setting RTO/RPO/MBCO |
| **BCMS** | Business Continuity Management System — the complete management framework for BC capability |
| **Disruption** | Any incident causing an unplanned negative deviation from expected service delivery |
| **IRP** | Incident Response Plan — the plan for detecting, declaring, and managing an incident to activate BC arrangements |

### The BIA → Strategy → Plan Chain

ISO 22301 is explicit that BCMS design must follow a defined chain:

1. **BIA** (Clause 8.2.2): identifies critical activities and sets RTOs, RPOs, MBCO
2. **Risk assessment** (Clause 8.2.3): identifies threats to those activities
3. **BC strategy** (Clause 8.3): defines how identified risks are treated and how RTOs will be achieved
4. **BC plans** (Clause 8.4): implements the strategy in operational procedures
5. **Exercises** (Clause 8.5): validates that the plans work and RTOs are achievable

A BCMS that has plans but no BIA, or has strategies that were never linked to BIA outputs,
will fail an ISO 22301 certification audit. The skill enforces this chain in its outputs.

---

## 5. Clause Structure at a Glance

| Clause | Title | Key Deliverables |
|--------|-------|-----------------|
| 4 | Context of the Organisation | BCMS scope statement, interested party register |
| 5 | Leadership | BC policy (signed), roles and responsibilities |
| 6 | Planning | BC objectives and plans, actions to address risks |
| 7 | Support | Competence records, communication plan, documented information procedures |
| 8 | Operation | BIA, risk assessment, BC strategies, BCPs, IRP, exercise programme, test records |
| 9 | Performance Evaluation | KPI monitoring, internal audit programme and results, management review minutes |
| 10 | Improvement | Nonconformity register, corrective action records, improvement log |

---

## 6. Mandatory Documentation Summary

ISO 22301:2019 requires the following documented information as a minimum:

| Document | Clause |
|----------|--------|
| BCMS scope statement | 4.3 |
| Business continuity policy | 5.2 |
| BC objectives and plans to achieve them | 6.2 |
| Evidence of competence | 7.2 |
| BIA results | 8.2.2 |
| Risk assessment results | 8.2.3 |
| BC strategies and solutions | 8.3.3 |
| Resource requirements | 8.3.4 |
| Incident response structure / procedures | 8.4.2 |
| Communication procedures | 8.4.3 |
| Business continuity plans | 8.4.4 |
| Recovery procedures | 8.4.5 |
| Exercise programme | 8.5.1 |
| Exercise results | 8.5.1 |
| IT / technical test results | 8.5.2 |
| Monitoring and measurement results | 9.1 |
| Internal audit programme and results | 9.2 |
| Management review record | 9.3 |
| Nonconformities and corrective actions | 10.1 |

---

## 7. How to Use the Skill

Once installed, the skill activates automatically when you ask about ISO 22301, BCMS, BIA,
Business Continuity Plans, Recovery Time Objectives, or related topics. You do not need to
reference the skill by name.

### Tips for Best Results

**Provide organisational context** — even brief context helps Claude tailor its output.
For example:
> "We are a 300-person financial services firm processing payments for retail customers.
> Help me conduct a BIA for our payment processing function."

**Be specific about the clause or task** — naming the clause or task type produces
more targeted responses:
> "I need help with Clause 8.3 — what BC strategies can we consider for an activity
> with a 4-hour RTO and a 1-hour RPO?"

**Iterate through the BIA → Strategy → Plan chain** — work through the methodology
in sequence for the best results:
1. Start with BIA to establish RTOs and priorities
2. Use BIA outputs to drive strategy selection
3. Use strategy to inform BCP content

**Ask for templates when you need starting points** — the skill can generate
gap analysis tables, BIA forms, risk registers, exercise plans, BCP documents,
management review agendas, and corrective action records.

### Example Interaction

```
You:     We have a 50-person professional services company. We have never done a
         formal BIA. Where do we start with ISO 22301:2019?

Claude:  [Explains the BIA process (Clause 8.2.2), scoping considerations, and
          provides a step-by-step approach:
          1. Define BCMS scope and products/services in scope
          2. Identify activities supporting each in-scope service
          3. Set up standard impact categories and time horizons
          4. Conduct workshops with process owners
          5. Determine MTPD, RTO, RPO, and MBCO for each activity
          6. Map dependencies (people, IT, premises, suppliers)
          7. Produce prioritised BIA output to drive strategy selection]

You:     Generate a BIA form for my customer invoicing activity. MTPD is 48 hours.

Claude:  [Produces a completed BIA form with:
          - Impact heat map with time horizons up to 48 hours
          - MTPD set at 48 hours with justification
          - Suggested RTO of 24-32 hours
          - RPO and MBCO fields to complete
          - People, technology, premises, and supplier dependency tables]
```

---

## 8. Skill Implementation Details

### Plugin Location

```
plugins/iso22301/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── iso22301/
        ├── SKILL.md
        └── references/
            ├── iso22301-clauses.md       (full clause requirements reference)
            ├── iso22301-bia-guide.md     (BIA methodology, time horizons, dependency mapping)
            ├── iso22301-bcps.md          (BCP structure, IRP, communication templates, IT DRP)
            └── iso22301-templates.md     (ready-to-use policy, BIA form, risk register, exercise plan templates)
```

### Reference Files

| File | Contents |
|------|----------|
| `iso22301-clauses.md` | Full clause-by-clause requirements with mandatory documentation list |
| `iso22301-bia-guide.md` | Complete BIA methodology: scoping, data collection, impact analysis, dependency mapping, reporting |
| `iso22301-bcps.md` | Plan architecture, IRP content, BCP template, IT DRP essentials, communication templates |
| `iso22301-templates.md` | BC policy, scope statement, BIA form, risk register, exercise plan, after-action report, management review record, nonconformity record, audit plan, competence matrix |

---

## 9. About ISO 22301:2019

ISO 22301:2019 was published by the International Organization for Standardization (ISO) in
October 2019 through Technical Committee ISO/TC 292 (Security and resilience). It replaced
ISO 22301:2012 and is the current edition of the standard.

The standard is applicable globally to any organisation in any sector that wishes to build
and demonstrate a systematic capability to recover from disruptive incidents. It can be used
as the basis for third-party certification by an accredited certification body under IAF
(International Accreditation Forum) recognised schemes.

ISO 22301:2019 aligns to the ISO High Level Structure (Annex SL), enabling integrated
implementation alongside ISO 27001:2022, ISO 9001:2015, ISO 14001:2015, and ISO 42001:2023.

For questions about ISO 22301:2019 as a standard, the definitive source is the ISO
publication available at [iso.org](https://www.iso.org/standard/75106.html) and supporting
guidance available in ISO 22313:2020 (Security and resilience — Business continuity
management systems — Guidance on the use of ISO 22301).

---

## 10. Disclaimer

This skill provides guidance based on the published requirements of ISO 22301:2019 and
accepted business continuity management practices. It is intended to support qualified
practitioners and should not replace the judgement of a certified professional in the context
of a specific organisation. For formal conformance assessments and certification, engage an
accredited ISO 22301 certification body and qualified lead auditor.

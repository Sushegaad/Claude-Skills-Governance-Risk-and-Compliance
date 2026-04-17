# ISO 22301:2019 — Business Impact Analysis (BIA) Methodology Guide

## Purpose

This reference provides a detailed, clause-accurate methodology for conducting a Business
Impact Analysis (BIA) under ISO 22301:2019 Clause 8.2.2. The BIA is the foundational
analytical process that determines what the organisation must protect, in what priority order,
and within what timeframes — underpinning all BC strategy, plan, and exercise decisions.

---

## What the Standard Requires

ISO 22301:2019 Clause 8.2.2 requires the organisation to:

1. Identify activities that support delivery of in-scope products and services
2. Assess impacts over time of disruption to those activities
3. Determine Maximum Tolerable Period of Disruption (MTPD) for each activity
4. Determine Minimum Business Continuity Objective (MBCO) for each activity
5. Determine Recovery Time Objective (RTO) for each activity
6. Determine Recovery Point Objective (RPO) for data-dependent activities
7. Identify all dependencies (people, technology, premises, information, suppliers)
8. Prioritise activities for recovery based on impact and urgency

All results must be documented and retained as mandatory documented information.

---

## BIA Process Overview

The BIA process consists of five sequential phases:

```
Phase 1: Scoping and preparation
Phase 2: Data collection (interviews/workshops)
Phase 3: Impact analysis and parameter determination
Phase 4: Dependency mapping
Phase 5: Prioritisation and reporting
```

---

## Phase 1: Scoping and Preparation

### 1.1 Define BIA Scope

Establish the boundary for the BIA aligned to the BCMS scope (Clause 4.3):
- Which products and services is the BIA covering?
- Which organisational units, sites, and functions are included?
- Are any functions explicitly excluded? If so, on what basis?

### 1.2 Define Impact Categories

Agree the categories of impact that will be assessed. Typical categories:

| Category | Description | Examples of Impact Indicators |
|----------|-------------|-------------------------------|
| Financial | Revenue loss, additional costs, contractual penalties | £/$/€ per hour or day of disruption |
| Operational | Inability to deliver products/services, internal process failures | Volume of work not processed |
| Regulatory/Legal | Breach of legal obligations, regulatory non-compliance | Notifiable breaches, licence at risk |
| Reputational | Damage to brand, customer confidence, media coverage | Social media mentions, customer complaints |
| Contractual | Breach of SLAs or customer contracts | Number of contracts at risk of breach |
| Health and Safety | Risk to employees, public, or environment | Near-miss, injury, or fatality risk |

### 1.3 Define Time Horizons

Establish standard time points at which impacts will be assessed. Common time horizons:
- Less than 1 hour
- 1–4 hours
- 4–8 hours
- 8–24 hours
- 1–3 days
- 3–7 days
- 1–2 weeks
- 2–4 weeks
- 1–3 months

The number and granularity of time points should match the organisation's operational profile.
Organisations with real-time critical activities (financial trading, emergency services) require
finer early granularity; organisations with daily batch-processing cycles may need fewer points.

### 1.4 Define Impact Severity Scale

Establish a consistent rating scale for all categories. Example 5-point scale:

| Rating | Label | Financial Indicator | Operational Indicator |
|--------|-------|--------------------|-----------------------|
| 1 | Negligible | No financial impact | Minor inconvenience, fully recoverable |
| 2 | Minor | <1% of monthly revenue | Limited service reduction, not customer-visible |
| 3 | Moderate | 1–5% of monthly revenue | Significant service reduction, some customers affected |
| 4 | Significant | 5–15% of monthly revenue | Material service failure, multiple customers affected |
| 5 | Catastrophic | >15% of monthly revenue | Complete failure, regulatory/legal exposure, existential risk |

Customise financial thresholds to match the organisation's scale.

### 1.5 Appoint BIA Facilitator and Assign Process Owners

- Assign a BIA Facilitator (typically the BCMS Manager)
- Identify process owners or senior representatives for each function in scope
- Schedule interviews or workshops

---

## Phase 2: Data Collection

### 2.1 BIA Interview / Workshop Approach

The BIA is most effective when conducted through structured interviews or workshops with
process owners who understand the operational realities of each function.

**Preparation for each session:**
- Send a pre-workshop questionnaire to collect preliminary activity lists
- Brief participants on objectives and terminology (MTPD, RTO, RPO, MBCO)
- Clarify that the exercise is about understanding operational impact — not assigning blame

**Key questions to ask in each session:**

1. **Activity identification**: What are the key activities/processes your team performs
   to support delivery of [products/services]? Please list them.

2. **Volume and timing**: How many transactions/tasks does each activity handle in a normal
   day/week? Are there peak periods or critical deadlines?

3. **Dependency on IT systems**: Which IT systems are essential? What happens if each system
   is unavailable for 1 hour? 4 hours? 1 day?

4. **Dependency on people**: What is the minimum number of staff required to perform each
   activity at MBCO level? What skills are critical? Do you have cross-trained backups?

5. **Dependency on premises**: Do any activities require access to a specific building or
   specialist facility? Could staff work remotely?

6. **Dependency on third parties**: Which suppliers or external service providers are
   critical to perform each activity?

7. **Impact over time**: What would the consequence be if this activity stopped for:
   1 hour / 4 hours / 1 day / 3 days / 1 week?

8. **MTPD**: At what point does the disruption become unacceptable (financial, regulatory,
   reputational)? What is the hard deadline for recovery?

9. **Minimum service level**: If you had to resume at reduced capacity, what is the bare
   minimum output required (the MBCO)?

10. **Data recovery**: For data-dependent systems, how much data loss is acceptable? If
    systems were restored to yesterday's backup, would that be acceptable?

### 2.2 Activity Inventory

Produce a consolidated activity inventory from all sessions:

| Activity ID | Activity Name | Function/Department | Owner | Product/Service Supported |
|-------------|--------------|---------------------|-------|--------------------------|
| A001 | Customer order entry | Sales Operations | Sales Director | Order fulfilment |
| A002 | Payment processing | Finance | CFO | Revenue collection |
| A003 | Warehouse picking and despatch | Logistics | Logistics Manager | Order fulfilment |
| A004 | HR payroll processing | Human Resources | HR Director | Staff management |
| A005 | IT helpdesk first-line support | IT | IT Director | Internal operations |

---

## Phase 3: Impact Analysis and Parameter Determination

### 3.1 Impact Heat Map

For each activity, rate impact at each time horizon across all categories. Use the severity
scale defined in Phase 1.

**Example for Activity A001 — Customer Order Entry:**

| Time Since Disruption | Financial | Operational | Regulatory | Reputational | Overall Rating |
|-----------------------|-----------|-------------|------------|--------------|----------------|
| <1 hour | 1 | 1 | 1 | 1 | 1 — Negligible |
| 1–4 hours | 2 | 2 | 1 | 1 | 2 — Minor |
| 4–8 hours | 3 | 3 | 1 | 2 | 3 — Moderate |
| 8–24 hours | 4 | 4 | 2 | 3 | 4 — Significant |
| 1–3 days | 5 | 5 | 3 | 4 | 5 — Catastrophic |
| 3–7 days | 5 | 5 | 4 | 5 | 5 — Catastrophic |

The overall rating is typically the *maximum* across categories (or agreed worst-case).

### 3.2 MTPD Determination

MTPD is the time point at which the impact rating crosses the organisation's unacceptable
threshold (typically rating 4 or 5 on the severity scale, as agreed with top management).

In the example above, MTPD = 8–24 hours (when impact first reaches 4 — Significant).

**MTPD represents the absolute deadline: recovery MUST occur before MTPD.**

Key MTPD considerations:
- Regulatory deadlines (e.g., payment processing cut-off times, reporting obligations)
- Contractual SLAs (e.g., SLAs with 4-hour response times)
- Operational dependencies (e.g., a pick-and-pack process must resume before the loading
  dock closes each evening)
- Financial irreversibility (e.g., a payment run that cannot be redone if missed)

### 3.3 RTO Determination

RTO is the target recovery time — the time by which the activity SHOULD be recovered.
RTO must be less than MTPD to provide a safety margin.

General RTO guidance:
- Set RTO at 50–80% of MTPD as a practical target
- Confirm the RTO is technically and operationally achievable with available resources
- Validate RTO through exercises and technical testing

| MTPD | Suggested RTO Range |
|------|---------------------|
| 1 hour | 30 minutes |
| 4 hours | 2–3 hours |
| 8 hours | 4–6 hours |
| 24 hours | 12–16 hours |
| 3 days | 1–2 days |
| 7 days | 3–5 days |

### 3.4 RPO Determination

RPO applies to activities that depend on data or information systems. It defines the maximum
acceptable data loss expressed as a point in time.

**RPO considerations:**
- What is the most recent backup schedule for critical systems?
- How often is data replicated to a secondary site?
- What is the business impact of losing X hours or days of transactions?
- Is manual re-entry of lost data feasible within the recovery window?

**RPO relationship to backup strategy:**
| RPO | Required Backup Approach |
|-----|-------------------------|
| Near-zero (minutes) | Synchronous real-time replication |
| 1 hour | Asynchronous replication, continuous data protection (CDP) |
| 4 hours | High-frequency scheduled backups (every 4 hours) |
| 24 hours | Daily backups, offsite copy |
| >24 hours | Standard backup schedules acceptable |

### 3.5 MBCO Determination

MBCO is the minimum level of service that must be achieved at the point of recovery (the RTO).
MBCO may be significantly below normal operational capacity:

**MBCO determination approach:**
1. Identify which activities within the function are truly critical (must-do vs. nice-to-do)
2. Identify what minimum staffing delivers critical activities at acceptable quality
3. Set MBCO as a percentage of normal capacity or as an absolute minimum volume

**Example MCO statements:**
- "Process a minimum of 50% of normal daily order volume within 8 hours of recovery"
- "Respond to all Priority 1 incidents within 4 hours; Priority 2 and 3 can be deferred"
- "Process weekly payroll on standard schedule; ad hoc pay runs can be deferred 48 hours"

---

## Phase 4: Dependency Mapping

For each activity, identify all supporting resources:

### 4.1 People Dependencies

| Activity | Role Required | Min. Headcount | Skills / Authorisation Required | Backup(s) Available? |
|----------|--------------|----------------|---------------------------------|----------------------|
| Order entry | Sales administrator | 2 | ERP access, order processing procedure | Yes — 1 backup trained |
| Payment processing | Accounts payable clerk | 1 | Finance system access, bank authorisation | No backup — single point of failure |

Identify **single points of failure** (roles with no trained alternate) and flag for succession
planning.

### 4.2 Technology Dependencies

| Activity | System / Application | Criticality | Owner | RTO Requirement | Backup / Failover Available? |
|----------|---------------------|-------------|-------|-----------------|------------------------------|
| Order entry | ERP (SAP S/4HANA) | Critical | IT Director | 8 hours | DR site — 6-hour RTO |
| Payment processing | Banking portal | Critical | CFO | 4 hours | Alternative bank portal available |
| All office activities | LAN/WAN/VPN | Critical | IT Director | 2 hours | 4G failover available |

### 4.3 Premises Dependencies

| Activity | Dependency on Location | Can Be Performed Remotely? | Alternate Location Available? |
|----------|-----------------------|----------------------------|-------------------------------|
| Order entry | Office premises (Level 2) | Yes — if VPN access | Remote working; alternate site |
| Warehouse operations | Main warehouse only | No — physical operation | No immediate alternate |

### 4.4 Information and Data Dependencies

| Activity | Information / Document Required | Location | Paper Copy Available? | Offsite Copy? |
|----------|---------------------------------|----------|----------------------|---------------|
| Order processing | Customer contracts | CRM system | No | Archived in cloud |
| Finance reporting | GL data | ERP | Monthly printout | DR site replica |
| Legal compliance | Regulatory filings | Document management system | No | IT backup |

### 4.5 Supplier and Third-Party Dependencies

| Activity | Supplier / Partner | Service Provided | Criticality | Alternate Available? | Supplier BCP Verified? |
|----------|--------------------|-----------------|-------------|----------------------|------------------------|
| Payroll | ADP (outsourced payroll) | Payroll processing | Critical | Manual processing feasible | Not verified |
| IT infrastructure | Cloud provider (AWS) | Hosting | Critical | Azure fallback partial | AWS SLA: 99.99% uptime |
| Logistics | DHL | Outbound deliveries | High | Alternative courier available | Not verified |

---

## Phase 5: Prioritisation and BIA Report

### 5.1 Activity Priority Tiers

Based on MTPD and impact assessments, assign each activity to a priority tier:

| Priority Tier | Criteria | Recovery Target |
|---------------|----------|-----------------|
| Critical | MTPD ≤ 24 hours; catastrophic impact if disrupted | Must recover within RTO (typically <24 hours) |
| High | MTPD 24 hours – 3 days; significant impact | Must recover within 1–3 days |
| Medium | MTPD 3–7 days; moderate impact | Recover within 3–7 days |
| Low | MTPD >7 days; limited impact | Recover within 1–4 weeks |
| Deferred | Can be suspended entirely during incident | No recovery target required during BCMS invocation |

### 5.2 BIA Summary Table

The BIA summary table forms the core output document:

| Activity | Owner | Priority | MTPD | RTO | RPO | MBCO | Key IT Dependency | Key People Risk | Key Supplier |
|----------|-------|----------|------|-----|-----|------|------------------|----------------|--------------|
| Customer order entry | Sales Dir | Critical | 24h | 8h | 4h | 50% | ERP | Sales admin (no backup) | None |
| Payment processing | CFO | Critical | 8h | 4h | 1h | 100% | Banking portal | AP clerk (SPOF) | ADP |
| Warehouse operations | Logistics Mgr | Critical | 16h | 8h | N/A | 75% | WMS | Forklift operators | DHL |
| HR payroll | HR Director | High | 5 days | 3 days | 1 day | Weekly cycle | ERP | HR manager | ADP |
| IT helpdesk | IT Director | Medium | 7 days | 3 days | N/A | P1 only | ITSM tool | Helpdesk staff | None |

### 5.3 BIA Report Structure

The formal BIA report (retained documented information) should include:

1. **Executive Summary**: Scope, methodology, headline findings, top risks to continuity
2. **BIA Methodology**: How the assessment was conducted, assumptions, limitations
3. **Activity Inventory**: Full list of assessed activities with ownership
4. **Impact Analysis Results**: Impact heat maps and MTPD justification per activity
5. **Recovery Parameters**: Consolidated RTO/RPO/MBCO/RLO table
6. **Dependency Register**: People, technology, premises, information, supplier dependencies
7. **Priority Tier Assignment**: Tiered activity list
8. **Key Findings and Gaps**: Single points of failure, high-risk dependencies, unachievable RTOs
9. **Recommendations**: Actions for risk treatment, strategy design, and plan prioritisation
10. **Appendices**: Interview records, raw data, assumptions

---

## BIA Maintenance

The BIA should be reviewed and updated:
- **Annually** as part of the regular BCMS review cycle
- **When significant organisational changes occur**: new products/services, restructuring, major
  technology changes, new sites, key supplier changes
- **Following an incident or exercise** that reveals assumptions were incorrect
- **Following management review** if new risks or priorities are identified

A BIA that is more than 12 months old, or that does not reflect current operations, is a
common nonconformity finding in ISO 22301 certification audits.

---

## Common BIA Mistakes to Avoid

| Mistake | Why It's a Problem | Correct Approach |
|---------|--------------------|-----------------|
| Confusing RTO with MTPD | Sets RTO at MTPD, leaving no safety margin | RTO must be less than MTPD |
| Setting aspirational RTOs not backed by strategy | Unreachable RTOs invalidate plans | Verify RTOs are achievable with available resources and strategy |
| Only assessing IT systems | ISO 22301 requires assessing all activities, not just technology | Include all processes: manual, operational, financial, people |
| Conducting BIA without business process owners | IT-led BIAs miss operational context | Process owners must participate; IT provides dependency data |
| Not updating the BIA after changes | Stale BIA invalidates all downstream plans | Embed BIA review into change management and annual cycle |
| Setting RPO equal to backup frequency | Backup frequency sets the minimum achievable RPO, not the requirement | Determine the business need for RPO first, then design backup to match |
| MBCO set at 100% | Prevents phased recovery; may be unachievable | MBCO should reflect truly minimum viable service, enabling prioritisation |

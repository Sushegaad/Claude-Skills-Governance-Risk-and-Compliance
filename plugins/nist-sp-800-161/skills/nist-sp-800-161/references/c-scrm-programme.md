# NIST SP 800-161 Rev 1 — C-SCRM Programme Establishment and Acquisition Procedures

**Source**: NIST SP 800-161 Rev 1, May 2022, Sections 2, 3.1–3.4

---

## C-SCRM Programme Establishment

### Step 1 — Obtain Senior Leadership Commitment

C-SCRM requires explicit senior leadership support. Before establishing the programme:
- Brief CIO, SAORM, and Chief Acquisition Officer on supply chain risks and regulatory requirements
- Obtain a formal commitment to resource and implement C-SCRM
- Designate a C-SCRM Programme Manager as a named position
- Establish or designate the C-SCRM governance body (cross-functional team)

### Step 2 — Develop C-SCRM Policy (SR-1)

Draft and obtain approval for a C-SCRM Policy:
- Scope: explicitly cover all ICT acquisitions including cloud services, SaaS, FOSS, and COTS
- Mandate: critical component identification, supplier vetting, SBOM for software, contract clauses
- Roles: CIO, SAORM, Chief Acquisition Officer, C-SCRM Programme Manager, Contract Officers, ISSOs
- Compliance: mechanism for tracking compliance and addressing non-compliance

### Step 3 — Develop C-SCRM Strategy

Document the enterprise C-SCRM strategy:
- Risk tolerance statement (what level of supply chain risk will the organisation accept and under what conditions)
- Prioritisation approach for applying C-SCRM resources (risk-based, starting with critical components)
- Integration with acquisition lifecycle (at which acquisition phases will C-SCRM requirements be applied)
- Integration with enterprise risk management
- Metrics for tracking C-SCRM programme effectiveness

### Step 4 — Establish Supplier and Critical Component Inventory

**Supplier inventory**:
- Identify all current ICT suppliers (hardware, software, cloud, managed services)
- Classify each supplier by risk tier using the tiering criteria
- Identify existing contract terms for C-SCRM provisions (will identify gaps needing remediation at next renewal)

**Critical component inventory** (Critical Asset List):
- Apply the criticality identification criteria to all ICT components
- Document the Critical Asset List with component details, supplier, and current risk controls
- Review and update the Critical Asset List at least annually and upon significant acquisitions or system changes

### Step 5 — Develop the C-SCRM Plan (SR-2)

Produce a formal C-SCRM Plan covering:
1. Scope and applicability
2. Risk tolerance statement (from strategy)
3. Critical Asset List (by reference or included)
4. Supplier inventory with tier classifications
5. Risk assessment approach
6. Controls applied per risk tier
7. Acquisition lifecycle integration procedures
8. Supplier assessment schedule and procedures
9. Monitoring activities and frequencies
10. Incident response procedures for supply chain events
11. Plan review cycle (minimum annual)

### Step 6 — Integrate C-SCRM into Acquisition Processes

Work with the Chief Acquisition Officer and Contracting Officers:
- Develop standard C-SCRM pre-solicitation checklist (triggers the C-SCRM review)
- Develop standard C-SCRM contract clause library for use at different risk tiers
- Develop SBOM delivery requirement language
- Train Contracting Officers and acquisition personnel on applying C-SCRM requirements
- Establish review process: acquisitions exceeding defined thresholds require C-SCRM review before solicitation

### Step 7 — Establish Monitoring

Establish ongoing C-SCRM monitoring:
- Subscribe to CISA Known Exploited Vulnerabilities (KEV) catalogue alerts
- Subscribe to National Vulnerability Database (NVD/CVE) feeds for components used
- Monitor GIDEP (Government-Industry Data Exchange Program) alerts for counterfeit and suspect components
- Monitor US-CERT and sector-specific ISAC alerts for supply chain threats
- Establish process to act on supplier notification agreement disclosures

---

## C-SCRM Plan Template

```
==================================================
CYBERSECURITY SUPPLY CHAIN RISK MANAGEMENT PLAN
[ORGANISATION NAME]
==================================================

DOCUMENT CONTROL
Version:          [X.Y]
Approval Date:    [YYYY-MM-DD]
Approving Official: [CIO / SAORM]
Review Cycle:     Annual (next review: [YYYY-MM-DD])

1. PURPOSE AND SCOPE
   1.1 Purpose
   This C-SCRM Plan documents [Organisation Name]'s programme for identifying,
   assessing, and mitigating cybersecurity risks in the supply chain for ICT
   products and services, consistent with NIST SP 800-161 Rev 1.

   1.2 Scope
   This plan applies to all ICT products, software, systems, and services
   acquired by [Organisation Name], including but not limited to:
   - Hardware components and systems
   - Commercial off-the-shelf (COTS) software
   - Free and open-source software (FOSS) incorporated into systems
   - Cloud services and SaaS
   - Managed and outsourced IT services

2. GOVERNANCE AND ROLES
   [Role] — [Specific C-SCRM responsibilities]
   [Repeat per role]
   C-SCRM Governance Body: [Name, membership, meeting cadence]

3. RISK TOLERANCE
   [Organisation Name] will accept supply chain risk at the [Low/Moderate/High]
   level for commoditised ICT components with multiple qualified suppliers and
   no mission-critical function. For critical components as defined in this plan,
   only [Low/Moderate] risk is acceptable, and risk exceeding that threshold must
   be documented with an accepted risk decision by [SAORM/CIO].

4. CRITICAL ASSET LIST
   [Reference to Critical Asset List document or include summary table]

   | Component | System | Supplier | Risk Tier | Last Assessment | Next Assessment |
   |---|---|---|---|---|---|
   | [Component] | [System name] | [Supplier] | Critical/High/Mod/Low | [Date] | [Date] |

5. SUPPLIER INVENTORY
   [Reference to Supplier Inventory document or include summary table]

   | Supplier | Products/Services | Risk Tier | Contract C-SCRM Clauses | Last Review |
   |---|---|---|---|---|
   | [Supplier] | [Products] | [Tier] | [Yes/No/Partial] | [Date] |

6. RISK ASSESSMENT APPROACH
   Supply chain risk assessments are conducted using the tiering criteria in
   the C-SCRM Supplier Assessment procedure. Risk assessments consider:
   - Threat sources (nation-state, criminal, insider, accidental)
   - Threat events (counterfeit components, tampered products, malicious code insertion, etc.)
   - Vulnerabilities (single-source dependency, lack of provenance, insecure sub-tiers)
   - Likelihood and impact per NIST SP 800-30 approach

7. CONTROLS BY RISK TIER
   Critical tier: SR-2, SR-3, SR-3(1), SR-3(3), SR-4, SR-4(1)–(4), SR-5, SR-5(2),
                  SR-6, SR-6(1), SR-7, SR-8, SR-11, SR-11(1), SR-12
   High tier:     SR-2, SR-3, SR-3(3), SR-4, SR-4(1), SR-5, SR-6, SR-8, SR-11, SR-12
   Moderate tier: SR-1, SR-2, SR-3, SR-5, SR-8, SR-11, SR-12
   Low tier:      SR-1, SR-12

8. ACQUISITION LIFECYCLE INTEGRATION
   [Reference to Acquisition Procedure section or document]

9. SUPPLIER ASSESSMENT SCHEDULE
   | Supplier | Tier | Assessment Type | Frequency | Next Due |
   |---|---|---|---|---|
   | [Supplier] | Critical | On-site audit | Annual | [Date] |

10. MONITORING ACTIVITIES
    [Description of ongoing monitoring: CVE feeds, GIDEP, ISAC, notification processing]

11. INCIDENT RESPONSE
    [Reference to or summary of supply chain incident response procedure]

12. PLAN REVIEW
    This plan shall be reviewed and updated:
    a. Annually, at a minimum
    b. Upon significant change to the organisational mission or IT environment
    c. Upon identification of a supply chain incident
    d. Upon change in organisational risk tolerance
```

---

## Acquisition Lifecycle C-SCRM Procedures

### Pre-Solicitation C-SCRM Checklist

Before issuing any solicitation for ICT products or services, the programme office or project manager completes this checklist:

**Checklist — Pre-Solicitation C-SCRM Review**

| Item | Yes | No | N/A | Action if No |
|---|---|---|---|---|
| 1. Has the acquisition been reviewed against the Critical Asset List? | | | | Conduct component criticality assessment |
| 2. Has the acquisition been classified by risk tier? | | | | Apply tiering criteria; document result |
| 3. Have C-SCRM contract clauses been selected from the approved library? | | | | Coordinate with Contracting Officer and C-SCRM Programme Manager |
| 4. For software-intensive acquisitions: is SBOM required? | | | | If critical/high: add SBOM delivery requirement |
| 5. For hardware acquisitions: are provenance and authenticity requirements included? | | | | Add clause requiring chain of custody documentation and authenticity warranties |
| 6. Are notification requirements included (72-hour incident/vulnerability; EOL)? | | | | Add SR-8 aligned notification clauses |
| 7. For Critical tier: has supplier assessment been initiated? | | | | Begin assessment before award; do not award to Critical tier supplier without assessment |
| 8. For High tier: has documentation review been scheduled? | | | | Schedule before or concurrent with contract performance |
| 9. Are right-to-audit provisions included for Critical/High tier? | | | | Add right-to-audit clause |
| 10. For sole-source acquisitions: has the risk of single-source dependency been documented? | | | | Document in acquisition risk register; include in C-SCRM plan |

### Delivery and Acceptance Procedure

For Critical and High-risk component deliveries:

1. Notify the C-SCRM Programme Manager of impending delivery
2. Upon receipt:
   a. Verify component identity (match received item against purchase order specifications)
   b. Check serial number/part number against manufacturer's authenticity verification portal if available
   c. Inspect tamper-evident seals
   d. For software: verify cryptographic signature or hash against developer-published values
   e. For SBOM deliverable: verify SBOM was received and ingest per SBOM consumption procedure
3. Document the acceptance inspection in the provenance record
4. If any anomaly is detected: quarantine the component, notify the C-SCRM Programme Manager, and follow the supply chain incident response procedure (do not deploy the suspect component)

### Supply Chain Incident Response Procedure

**Trigger events**:
- Supplier notifies of a security incident or vulnerability affecting delivered products
- CISA KEV or NVD alert identifies a critical/high CVE in a component the organisation uses
- GIDEP alert identifies a suspect counterfeit component used by the organisation
- Organisation discovers evidence of tampering or malicious code in an in-service component
- Intelligence reporting identifies a supply chain threat

**Response steps**:

1. **Identify and assess**:
   - Identify all systems using the affected component (use component inventory / SBOM data)
   - Assess potential impact (CIA impact, exploitation status, adversary intent)
   - Assign severity (Critical/High/Medium/Low)

2. **Contain**:
   - For active exploit: immediately isolate affected systems from the network
   - For unpatched vulnerability: apply compensating control (WAF rule, disable affected feature, network segmentation)
   - For counterfeit/tampered hardware: remove from service; quarantine

3. **Notify**:
   - Notify ISSO and system owner within 1 hour of identification
   - Notify AO within 4 hours for Critical severity; within 24 hours for High
   - Notify CISA if the system is a federal system and the event meets FISMA reporting thresholds
   - Report suspect counterfeit components to GIDEP

4. **Eradicate and recover**:
   - For malicious code: re-image or rebuild affected systems
   - For vulnerable component: apply vendor patch upon release; verify patch integrity before deployment
   - For counterfeit hardware: replace with genuine component from authorised source
   - For tampered component: replace and update provenance record

5. **Document**:
   - Record all response actions and timeline
   - Update provenance records
   - Update POA&M if compensating controls remain in place pending full remediation
   - Conduct after-action review; update C-SCRM plan if process improvements are identified

---

## C-SCRM Metrics

| Metric | Measurement | Target | Reporting Level |
|---|---|---|---|
| Critical component coverage | Percentage of critical components with current provenance documentation | 100% | Tier 1 |
| Supplier assessment coverage | Percentage of Critical-tier suppliers with assessment within required frequency | 100% | Tier 1 |
| Contract C-SCRM clause coverage | Percentage of active contracts with Critical/High-tier suppliers containing required C-SCRM clauses | 100% | Tier 1 |
| SBOM coverage | Percentage of in-scope software deliverables for which SBOM has been received | Target by mission area | Tier 2 |
| Notification response | Percentage of supplier notifications responded to within defined timeframes | 100% | Tier 2/3 |
| Open supply chain vulnerabilities | Count and age of open CVEs in SBOMs not yet patched within SLA | 0 overdue | Tier 3 |
| Suspect counterfeit incidents | Count of suspect counterfeit components identified per quarter | 0; any triggers investigation | Tier 1 |

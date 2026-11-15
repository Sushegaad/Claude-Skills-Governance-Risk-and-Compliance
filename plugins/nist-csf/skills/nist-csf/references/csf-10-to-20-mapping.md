# NIST CSF 1.1 → CSF 2.0 Migration Guide

Source: NIST CSF 2.0 (February 2024) and CSF 1.1 (April 2018)

---

## Summary of Changes

| Aspect | CSF 1.1 | CSF 2.0 |
|--------|---------|---------|
| Functions | 5 (ID, PR, DE, RS, RC) | 6 (+ **GV: Govern**) |
| Total subcategories | 108 | 106 |
| Govern function | Embedded across ID/PR | Standalone - 6 categories, 31 subcategories |
| Supply chain risk | ID.SC (5 subcategories) | GV.SC (10 subcategories) - significantly expanded |
| Profiles | Basic concept | Strengthened - org profile templates, community profiles |
| Tiers | 4 tiers | 4 tiers - refined descriptions |
| Informative References | Embedded | Moved to online NIST Reference Tool (searchable) |
| Audience | Critical infrastructure primary | All sectors, all sizes explicitly |
| Quick Start Guides | None | Added for: SMBs, enterprise risk managers, government |

---

## What Moved Where: Key Subcategory Migrations

### CSF 1.1 → CSF 2.0 Function Changes

Many CSF 1.1 subcategories were re-homed to the new **GV (Govern)** function:

| CSF 1.1 Location | CSF 2.0 Location | Topic |
|-----------------|-----------------|-------|
| ID.GV-01 | GV.PO-01 | Cybersecurity policy |
| ID.GV-02 | GV.RR-02 | Roles and responsibilities |
| ID.GV-03 | GV.OC-03 | Legal/regulatory requirements |
| ID.GV-04 | GV.OV-01 | Governance and risk strategy review |
| ID.RM-01 | GV.RM-01 | Risk management process |
| ID.RM-02 | GV.RM-02 | Risk tolerance |
| ID.RM-03 | GV.RM-06 | Risk methodology |
| ID.SC-01 | GV.SC-01 | Supply chain risk program |
| ID.SC-02 | GV.SC-04 + GV.SC-07 | Supplier identification and assessment |
| ID.SC-03 | GV.SC-05 | Supply chain contracts |
| ID.SC-04 | GV.SC-07 | Ongoing supplier monitoring |
| ID.SC-05 | GV.SC-08 | Supplier incident response coordination |

### New Subcategories in CSF 2.0 (no CSF 1.1 equivalent)

| CSF 2.0 ID | Description |
|-----------|-------------|
| GV.OC-02 | Stakeholder needs and expectations understood |
| GV.OC-04 | Critical services stakeholders depend on are understood |
| GV.OC-05 | Organizational dependencies are understood |
| GV.RM-04 | Strategic direction for risk response options |
| GV.RM-05 | Lines of communication for cybersecurity risks |
| GV.RM-07 | Positive risks (strategic opportunities) are characterized |
| GV.RR-01 | Leadership accountability and risk culture |
| GV.RR-03 | Adequate resource allocation |
| GV.RR-04 | Cybersecurity in HR practices |
| GV.PO-02 | Policy review and update cycle |
| GV.OV-02 | Strategy reviewed for coverage gaps |
| GV.OV-03 | Cybersecurity performance evaluation |
| GV.SC-03 | Supply chain risk integrated into enterprise risk |
| GV.SC-06 | Due diligence before supplier relationships |
| GV.SC-09 | Supply chain practices throughout tech lifecycle |
| GV.SC-10 | Post-relationship supply chain provisions |
| ID.AM-07 | Data and metadata inventories |
| ID.AM-08 | Asset lifecycle management |
| ID.RA-07 | Change and exception management |
| ID.RA-08 | Vulnerability disclosure processes |
| ID.RA-09 | Hardware/software authenticity assessment |
| ID.RA-10 | Critical supplier pre-acquisition assessment |
| ID.IM-01 to 04 | Improvement category (entirely new) |
| PR.DS-10 | Data-in-use protection |
| PR.PS-06 | Secure software development practices |
| DE.AE-07 | Threat intelligence integration into analysis |
| DE.AE-08 | Incident declaration criteria |
| RS.MA-02 to 05 | Expanded incident management subcategories |
| RS.AN-07, 08 | Incident data collection and magnitude |
| RC.RP-02 to 06 | Expanded recovery plan execution |
| RC.CO-04 | Public updates on incident recovery |

### Subcategories Removed in CSF 2.0 (CSF 1.1 only)

| CSF 1.1 ID | Description | Disposition |
|-----------|-------------|-------------|
| ID.BE-01 to 05 | Business Environment | Merged into GV.OC and GV.RM |
| PR.IP-01 to 12 | Information Protection Processes and Procedures | Split across PR.PS and PR.IR |
| PR.MA-01, 02 | Maintenance | Merged into PR.PS-02, PR.PS-03 |
| DE.DP-01 to 05 | Detection Processes | Merged into DE.CM and DE.AE |
| RS.RP-01 | Response Planning | Merged into RS.MA-01 |
| RS.CO-01 | Response Planning Communication | Merged into RS.MA-01 |
| RS.CO-04, 05 | Communications | Consolidated |
| RS.AN-01, 02, 04, 05 | Analysis subcategories | Consolidated into RS.AN-03, 06, 07, 08 |
| RC.RP-01 (old) | Recovery planning | Restructured into RC.RP-01 through RC.RP-06 |
| RC.IM-01, 02 | Recovery Improvements | Merged into ID.IM |
| RC.CO-01, 02 | Recovery Communications | Consolidated |

---

## Migration Checklist: CSF 1.1 → CSF 2.0

Use this checklist when transitioning an existing CSF 1.1 implementation:

**Governance (new GV function)**
- [ ] Formally document cybersecurity strategy and risk tolerance (GV.RM-01, GV.RM-02)
- [ ] Assign explicit cybersecurity roles with accountability to leadership (GV.RR-01, GV.RR-02)
- [ ] Establish a Cybersecurity Policy and review cycle (GV.PO-01, GV.PO-02)
- [ ] Create an oversight mechanism to review risk strategy outcomes (GV.OV-01 to 03)
- [ ] Expand supply chain risk management to cover GV.SC-01 through GV.SC-10
- [ ] Document organizational context and stakeholder dependencies (GV.OC-01 to 05)

**Identify updates**
- [ ] Add data and metadata inventories (ID.AM-07)
- [ ] Implement asset lifecycle management (ID.AM-08)
- [ ] Establish vulnerability disclosure process (ID.RA-08)
- [ ] Assess hardware/software authenticity before acquisition (ID.RA-09)
- [ ] Create an improvement tracking process (ID.IM-01 to 04)

**Protect updates**
- [ ] Add data-in-use protection controls (PR.DS-10)
- [ ] Integrate secure software development practices (PR.PS-06)

**Detect updates**
- [ ] Integrate threat intelligence into event analysis (DE.AE-07)
- [ ] Define and document incident declaration criteria (DE.AE-08)

**Respond updates**
- [ ] Formalize incident triage, categorization, and escalation (RS.MA-02 to 04)
- [ ] Improve incident data collection and integrity (RS.AN-07)

**Recover updates**
- [ ] Add post-incident operational norms assessment (RC.RP-04)
- [ ] Define incident recovery end criteria (RC.RP-06)
- [ ] Establish public update process for incident recovery (RC.CO-04)

---

## CSF Version Coexistence

Organizations with CSF 1.1 implementations do not need to immediately migrate - CSF 2.0 is backward compatible in intent. The key practical changes are:

1. **Govern is not optional**: If your organization has governance practices embedded in ID or PR, map them to the new GV function explicitly
2. **Supply chain is a first-class concern**: ID.SC (5 subcategories) must be expanded to GV.SC (10 subcategories)
3. **Improvement is now structured**: The new ID.IM category formalises what was previously ad hoc
4. **Informative References moved online**: Use the NIST CSF 2.0 Reference Tool at https://csrc.nist.gov/Projects/cybersecurity-framework/Filters#/csf/filters to find current informative references for each subcategory

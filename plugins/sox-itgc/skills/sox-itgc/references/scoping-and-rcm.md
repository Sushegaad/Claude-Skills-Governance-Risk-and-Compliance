# Scoping Methodology & RCM Construction

## Top-down scoping (AS 2201 ¶21-34 logic; GAIT-consistent)
1. **Significant accounts/disclosures** from the financial statements: quantitative (benchmark % of pretax income/revenue/assets — set with the auditor) + qualitative factors (estimation, fraud risk, complexity).
2. **Map processes**: which business processes initiate, authorize, record, process, report those accounts (order-to-cash, procure-to-pay, record-to-report, payroll, inventory, treasury, tax).
3. **Identify applications**: per process — ERP modules, sub-ledgers, billing engines, consolidation tools, key interfaces, and the reports/IPE finance relies on. Include end-user computing where a spreadsheet performs control-relevant calculation.
4. **Layer the stack**: for each in-scope application — database, operating system/platform (incl. cloud IaaS/PaaS), and the ITGC processes (access, change, operations) at each layer. Scope ITGC layers by risk: the DB under the ERP is in; the network switch usually is not.
5. **Outsourced layers**: SaaS/BPO → obtain **SOC 1 Type II** reports; verify period coverage vs fiscal year (bridge letters for gaps ≤ ~3 months); map **CUECs** into your own control set — every unowned CUEC is a control gap.
6. Document a **scoping memo**: accounts → processes → systems → layers → rationale, refreshed annually and on major change (implementations, M&A).

## RCM template (per system or process)
| # | Risk | Control objective | Control activity | Type (P/D) | Automation (A/M/ITDM) | Frequency | Owner | Evidence | Test approach | Framework refs |
|---|---|---|---|---|---|---|---|---|---|---|
Populate one row per control; keep risk statements misstatement-anchored ("unauthorized changes to the billing engine cause misstated revenue" — not "hackers"). Map to COSO 2013 components (control environment through monitoring) and principles where the auditor requests it.

## Sample-size conventions (agree with auditors; convention not regulation)
Annual 1 · Quarterly 2 · Monthly 2–3 · Weekly 5 · Daily 25 · Multiple-times-daily/automated: test of one per configuration plus ITGC reliance for the period. Re-test after remediation requires a sufficient operating window before year-end (a quarterly control needs at least one clean occurrence; daily controls commonly a 25-sample over the remediated window).

## Quarterly rhythm (deadline-driven reality)
Q1: refresh scoping, update RCMs for system changes, UAR cycle 1. Q2: TOD walkthroughs, interim TOE wave 1, UAR 2. Q3: interim TOE wave 2, deficiency triage while remediation windows remain, UAR 3. Q4: update testing/roll-forward to year-end, remediation validation, aggregation analysis, management's 404(a) conclusion, UAR 4. Terminations and privileged access: test continuously — they produce the worst late surprises.

## 404 applicability quick logic
All public companies: 404(a) from the SECOND annual report post-IPO. 404(b) auditor attestation: accelerated ($75M–$700M float + ≥$100M revenue) and large accelerated (≥$700M) filers that are not EGCs (<$1.235B revenue, max 5 yrs). FLAG: SEC May 19, 2026 proposal (comments closed July 20, 2026; no final action as of November 6, 2026) would move 404(b) to large accelerated only at a $2B float threshold with a ~5-year IPO on-ramp. Current 404(b) thresholds remain operative; check status before advising on future-year obligations.

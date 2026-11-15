# Deficiency Evaluation Framework

## The ladder (cite both sources)
Definitions per PCAOB **AS 2201 Appendix A** and SEC **Reg S-X Rule 1-02(a)(4)** (the material weakness definition was adopted via SEC Release 33-8809; Release 33-8829 added the significant deficiency definition):
- **Control deficiency** - design or operation of a control does not allow management or employees, in the normal course of performing their functions, to prevent or detect misstatements on a timely basis.
- **Significant deficiency** - a deficiency, or combination, less severe than a material weakness yet important enough to merit attention by those responsible for oversight of financial reporting. Reported in writing to the audit committee; not publicly disclosed.
- **Material weakness** - a deficiency, or combination, such that there is a REASONABLE POSSIBILITY that a MATERIAL misstatement of annual or interim financial statements will not be prevented or detected on a timely basis. Disclosed in management's 404(a) report; drives an adverse auditor ICFR opinion under 404(b).

## Evaluation sequence
1. **Facts**: what failed, how long, population affected, actual errors found?
2. **Likelihood** (reasonable possibility?) and **magnitude** (maximum potential misstatement - consider account size, transaction volume flowing through the affected control, gross exposure not net).
3. **Compensating controls**: do they operate at a precision that would detect a material misstatement? Test them before crediting them.
4. **Aggregation**: combine deficiencies affecting the same significant account, disclosure, or assertion (AS 2201) - three "minor" access deficiencies on the revenue system can aggregate to significant or worse.
5. **Prudent-official test**: would a prudent official conclude the ladder rung chosen is reasonable?

## ITGC-specific logic
An ITGC deficiency has no DIRECT misstatement impact - evaluate it through what it undermines:
- Failed change management → which automated controls/reports changed during the period without control? Re-perform/baseline them.
- Failed access/SoD → who had conflicting or excessive access, did they use it (activity review), what could they have misstated?
- Failed operations (backup/job) → data integrity of processing streams feeding the ledger.
If the dependent application controls are re-validated clean for the period, the ITGC failure often lands at deficiency/significant deficiency; pervasive ITGC failure across systems with no compensating validation trends toward material weakness.

## Worked severity examples
- **Deficiency**: 2 of 25 sampled changes missing pre-migration approval; both tested clean retrospectively; strong detective reconciliations downstream.
- **Significant deficiency**: quarterly UARs not performed for two quarters on the consolidation tool; activity review found no inappropriate access use; compensating monthly close review operates precisely.
- **Material weakness**: terminated IT administrator retained ERP superuser access for five months spanning year-end, with write access to GL and no logging/monitoring - magnitude unbounded, likelihood reasonable-possibility, no compensating control at precision.

## Benchmarks worth citing (with dates)
KPMG 2025 study (Audit Analytics data): 279 of 3,502 (~8%) annual reports filed 2023–24 disclosed material weaknesses; IT/access and SoD among top themes. Baker Tilly (through April 2025): adverse ICFR assessments fell from >26% (2021 SPAC peak) to just over 15% (2024); >60% of adverse reports are repeat filers. Avoid quoting sharper "% of MWs that are IT-related" figures without pulling the underlying study.

## Reporting
Deficiency → management tracking. Significant deficiency → written audit-committee communication. Material weakness → 10-K Item 9A disclosure (nature, remediation plan, status), adverse auditor opinion where 404(b) applies; disclose remediation progress in subsequent 10-Qs.

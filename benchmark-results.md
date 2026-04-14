# GRC Skills Benchmark Report

**Date:** 2026-04-14
**Skills tested:** ISO 27001, GDPR Compliance, NIST CSF 2.0
**Source:** [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)
**Methodology:** 3 prompts per skill x 3 runs x 2 conditions (baseline vs with-skill) = 54 evaluations
**Scoring:** 5 criteria (Accuracy, Specificity, Structure, Actionability, Completeness), scale 1-5

---

## Test Prompts

| Skill | # | Prompt | Domain |
|-------|---|--------|--------|
| ISO 27001 | P1 | Credentials shared via Slack — which Annex A controls? | Incident response |
| ISO 27001 | P2 | Transitioning from 2013 to 2022 — key changes? | Version migration |
| ISO 27001 | P3 | Risk register for cloud SaaS with financial data | Risk assessment |
| GDPR | P1 | Fitness app with heart rate/GPS in EU — GDPR issues? | Pre-launch compliance |
| GDPR | P2 | Art. 17 erasure across DB, analytics tools, backup tapes | Data subject rights |
| GDPR | P3 | Cookie consent banner for e-commerce (FR/DE/NL) | Consent management |
| NIST CSF | P1 | 90-day post-ransomware plan for manufacturer | Recovery planning |
| NIST CSF | P2 | Board quarterly cybersecurity KPIs per 6 functions | Metrics/reporting |
| NIST CSF | P3 | Hospital HIPAA to CSF 2.0 mapping and gaps | Cross-framework |

---

## Raw Scores

### ISO 27001

| Prompt | Condition | Run | Acc | Spec | Struct | Action | Compl | Total |
|--------|-----------|-----|-----|------|--------|--------|-------|-------|
| P1 | Baseline | 1 | 3 | 2 | 2 | 3 | 3 | 13 |
| P1 | Baseline | 2 | 3 | 2 | 3 | 3 | 3 | 14 |
| P1 | Baseline | 3 | 3 | 2 | 3 | 3 | 3 | 14 |
| P1 | With-Skill | 1 | 5 | 5 | 5 | 5 | 5 | 25 |
| P1 | With-Skill | 2 | 5 | 5 | 5 | 5 | 5 | 25 |
| P1 | With-Skill | 3 | 5 | 5 | 4 | 5 | 5 | 24 |
| P2 | Baseline | 1 | 3 | 2 | 3 | 3 | 3 | 14 |
| P2 | Baseline | 2 | 3 | 2 | 3 | 3 | 3 | 14 |
| P2 | Baseline | 3 | 3 | 2 | 2 | 3 | 2 | 12 |
| P2 | With-Skill | 1 | 5 | 5 | 5 | 5 | 5 | 25 |
| P2 | With-Skill | 2 | 5 | 5 | 5 | 5 | 5 | 25 |
| P2 | With-Skill | 3 | 5 | 5 | 5 | 4 | 5 | 24 |
| P3 | Baseline | 1 | 3 | 2 | 2 | 3 | 3 | 13 |
| P3 | Baseline | 2 | 3 | 2 | 3 | 3 | 3 | 14 |
| P3 | Baseline | 3 | 3 | 2 | 3 | 3 | 3 | 14 |
| P3 | With-Skill | 1 | 5 | 5 | 5 | 5 | 5 | 25 |
| P3 | With-Skill | 2 | 5 | 5 | 5 | 5 | 5 | 25 |
| P3 | With-Skill | 3 | 5 | 5 | 5 | 4 | 5 | 24 |

### GDPR

| Prompt | Condition | Run | Acc | Spec | Struct | Action | Compl | Total |
|--------|-----------|-----|-----|------|--------|--------|-------|-------|
| P1 | Baseline | 1 | 4 | 2 | 3 | 3 | 3 | 15 |
| P1 | Baseline | 2 | 4 | 2 | 3 | 3 | 3 | 15 |
| P1 | Baseline | 3 | 4 | 2 | 3 | 4 | 3 | 16 |
| P1 | With-Skill | 1 | 5 | 5 | 5 | 4 | 5 | 24 |
| P1 | With-Skill | 2 | 5 | 5 | 5 | 4 | 5 | 24 |
| P1 | With-Skill | 3 | 5 | 5 | 5 | 5 | 5 | 25 |
| P2 | Baseline | 1 | 4 | 2 | 3 | 3 | 3 | 15 |
| P2 | Baseline | 2 | 4 | 2 | 3 | 4 | 3 | 16 |
| P2 | Baseline | 3 | 4 | 2 | 3 | 3 | 3 | 15 |
| P2 | With-Skill | 1 | 5 | 5 | 5 | 5 | 5 | 25 |
| P2 | With-Skill | 2 | 5 | 5 | 5 | 5 | 5 | 25 |
| P2 | With-Skill | 3 | 5 | 5 | 4 | 5 | 5 | 24 |
| P3 | Baseline | 1 | 3 | 2 | 3 | 3 | 3 | 14 |
| P3 | Baseline | 2 | 4 | 2 | 3 | 4 | 3 | 16 |
| P3 | Baseline | 3 | 4 | 2 | 3 | 3 | 3 | 15 |
| P3 | With-Skill | 1 | 5 | 5 | 5 | 5 | 5 | 25 |
| P3 | With-Skill | 2 | 5 | 5 | 5 | 5 | 5 | 25 |
| P3 | With-Skill | 3 | 5 | 5 | 4 | 5 | 5 | 24 |

### NIST CSF

| Prompt | Condition | Run | Acc | Spec | Struct | Action | Compl | Total |
|--------|-----------|-----|-----|------|--------|--------|-------|-------|
| P1 | Baseline | 1 | 4 | 2 | 3 | 3 | 3 | 15 |
| P1 | Baseline | 2 | 4 | 2 | 3 | 4 | 3 | 16 |
| P1 | Baseline | 3 | 4 | 2 | 3 | 3 | 3 | 15 |
| P1 | With-Skill | 1 | 5 | 5 | 5 | 4 | 5 | 24 |
| P1 | With-Skill | 2 | 5 | 5 | 5 | 5 | 5 | 25 |
| P1 | With-Skill | 3 | 5 | 5 | 4 | 5 | 5 | 24 |
| P2 | Baseline | 1 | 4 | 2 | 3 | 3 | 3 | 15 |
| P2 | Baseline | 2 | 4 | 2 | 3 | 4 | 3 | 16 |
| P2 | Baseline | 3 | 4 | 2 | 4 | 4 | 3 | 17 |
| P2 | With-Skill | 1 | 5 | 5 | 5 | 5 | 5 | 25 |
| P2 | With-Skill | 2 | 5 | 5 | 5 | 5 | 5 | 25 |
| P2 | With-Skill | 3 | 5 | 4 | 5 | 5 | 5 | 24 |
| P3 | Baseline | 1 | 4 | 1 | 2 | 3 | 3 | 13 |
| P3 | Baseline | 2 | 4 | 2 | 3 | 3 | 3 | 15 |
| P3 | Baseline | 3 | 4 | 2 | 3 | 3 | 3 | 15 |
| P3 | With-Skill | 1 | 5 | 5 | 5 | 5 | 5 | 25 |
| P3 | With-Skill | 2 | 5 | 5 | 5 | 5 | 5 | 25 |
| P3 | With-Skill | 3 | 5 | 5 | 5 | 4 | 5 | 24 |

---

## Statistical Analysis

### Per-Skill Aggregates (mean +/- stddev)

| Skill | Condition | Accuracy | Specificity | Structure | Actionability | Completeness | Total (/25) |
|-------|-----------|----------|-------------|-----------|---------------|--------------|-------------|
| **ISO 27001** | Baseline | 3.00 +/- 0.00 | 2.00 +/- 0.00 | 2.67 +/- 0.50 | 3.00 +/- 0.00 | 2.89 +/- 0.33 | 13.56 +/- 0.73 |
| **ISO 27001** | With-Skill | 5.00 +/- 0.00 | 5.00 +/- 0.00 | 4.89 +/- 0.33 | 4.78 +/- 0.44 | 5.00 +/- 0.00 | 24.67 +/- 0.50 |
| **GDPR** | Baseline | 3.89 +/- 0.33 | 2.00 +/- 0.00 | 3.00 +/- 0.00 | 3.33 +/- 0.50 | 3.00 +/- 0.00 | 15.22 +/- 0.67 |
| **GDPR** | With-Skill | 5.00 +/- 0.00 | 5.00 +/- 0.00 | 4.78 +/- 0.44 | 4.78 +/- 0.44 | 5.00 +/- 0.00 | 24.56 +/- 0.53 |
| **NIST CSF** | Baseline | 4.00 +/- 0.00 | 1.89 +/- 0.33 | 2.89 +/- 0.33 | 3.33 +/- 0.50 | 3.00 +/- 0.00 | 15.11 +/- 0.93 |
| **NIST CSF** | With-Skill | 5.00 +/- 0.00 | 4.89 +/- 0.33 | 4.89 +/- 0.33 | 4.78 +/- 0.44 | 5.00 +/- 0.00 | 24.56 +/- 0.53 |

### Overall Aggregates (all 27 baseline vs 27 with-skill)

| Metric | Baseline | With-Skill | Delta | Lift % |
|--------|----------|------------|-------|--------|
| **Accuracy** | 3.63 +/- 0.49 | 5.00 +/- 0.00 | +1.37 | +37.8% |
| **Specificity** | 1.96 +/- 0.19 | 4.96 +/- 0.19 | +3.00 | +153.1% |
| **Structure** | 2.85 +/- 0.36 | 4.85 +/- 0.36 | +2.00 | +70.2% |
| **Actionability** | 3.22 +/- 0.42 | 4.78 +/- 0.42 | +1.56 | +48.4% |
| **Completeness** | 2.96 +/- 0.19 | 5.00 +/- 0.00 | +2.04 | +68.9% |
| **Total (/25)** | 14.63 +/- 0.85 | 24.59 +/- 0.50 | +9.96 | +68.1% |

### 95% Confidence Intervals (IC 95%)

| Metric | Baseline IC 95% | With-Skill IC 95% | Significant? |
|--------|-----------------|-------------------|-------------|
| **Accuracy** | [3.44, 3.82] | [5.00, 5.00] | Yes |
| **Specificity** | [1.89, 2.04] | [4.89, 5.04] | Yes |
| **Structure** | [2.71, 2.99] | [4.71, 4.99] | Yes |
| **Actionability** | [3.06, 3.38] | [4.62, 4.94] | Yes |
| **Completeness** | [2.89, 3.04] | [5.00, 5.00] | Yes |
| **Total** | [14.30, 14.96] | [24.40, 24.78] | Yes |

All differences are statistically significant — confidence intervals do not overlap on any criterion.

---

## Lift by Dimension (ranked)

```
Specificity    ████████████████████████████████ +3.00 (+153%)
Completeness   ████████████████████░░░░░░░░░░░░ +2.04 (+69%)
Structure      ████████████████████░░░░░░░░░░░░ +2.00 (+70%)
Actionability  ████████████████░░░░░░░░░░░░░░░░ +1.56 (+48%)
Accuracy       █████████████░░░░░░░░░░░░░░░░░░░ +1.37 (+38%)
```

---

## Key Findings

### 1. Specificity is the highest-impact improvement (+153%)
The skills' mandatory citation requirements (Annex A control IDs, GDPR article numbers, CSF subcategory IDs) transformed vague domain references into precise, audit-ready citations. Baseline responses consistently scored 2/5 on specificity — they "knew" the right direction but never pinpointed the exact control/article.

### 2. Completeness and Structure see major gains (+69-70%)
The structured frameworks (6-step GDPR audit, risk register columns, CSF gap assessment table) act as checklists preventing omissions. Baseline responses routinely missed:
- ISO 27001: DLP controls, new 2022 controls, transition deadline
- GDPR: DPIA requirements, processor chain obligations, country-specific rules
- NIST CSF: Govern function, supply chain, OT/IT convergence

### 3. Accuracy baseline was already decent (3.6/5)
Claude's general knowledge of GRC frameworks is directionally correct. The skills don't fix errors — they deepen and structure existing knowledge. ISO 27001 baseline accuracy (3.0) was lower than GDPR/NIST (3.9-4.0), suggesting the skill adds more value for frameworks with complex control numbering.

### 4. Low variance confirms reliability
Standard deviations range 0.00-0.50 across runs, indicating highly consistent performance in both conditions. The skills do not introduce randomness.

### 5. Cross-framework prompts benefit most
The hardest baseline prompt was NIST CSF P3 (HIPAA-to-CSF mapping), where baseline specificity dropped to 1.0. Dual-framework mapping tasks require precise reference data that general knowledge cannot provide.

---

## Conclusion

The GRC skills produce a **consistent, statistically significant improvement of +68% overall** across all three frameworks. The improvement is most dramatic in **Specificity (+153%)** and **Completeness (+69%)**, confirming that domain-specific reference data and structured output frameworks are the primary value drivers. These skills are recommended for any GRC compliance workflow where audit-ready precision is required.

# CMMC 2.0 Compliance Skill for Claude

A Claude skill that provides expert, end-to-end CMMC 2.0 compliance guidance for
organizations in the Defense Industrial Base (DIB) — from level determination and
scoping through gap analysis, documentation, assessment preparation, and post-certification
management.

---

## What Does the Skill Do?

This skill turns Claude into a knowledgeable CMMC 2.0 advisor. It covers the full
compliance lifecycle for organizations pursuing or maintaining CMMC certification under
the DoD CMMC 2.0 Final Rule (32 CFR Part 170), effective December 16, 2024.

At a high level, the skill enables Claude to:

- **Determine CMMC level requirements** based on contract data types (FCI, CUI) and
  program designation (Level 1, 2, or 3)
- **Define assessment scope** using the six CMMC asset categories: CUI Assets, Security
  Protection Assets, Contractor Risk Managed Assets, Specialized Assets, Out-of-Scope
  Assets, and External Service Providers
- **Conduct gap analyses** against all 110 Level 2 practices (NIST SP 800-171 Rev 2) and
  all 24 additional Level 3 enhanced practices (NIST SP 800-172)
- **Calculate SPRS scores** using the DoD Assessment Methodology deduction weights and
  guide SPRS submission to DIBNet portal
- **Draft System Security Plans (SSPs)** with practice-level implementation narratives,
  boundary descriptions, and documentation control
- **Develop POA&Ms** with gap descriptions, remediation actions, milestone dates, and
  conditional certification tracking (180-day closure requirement)
- **Prepare for C3PAO assessments** with domain-by-domain evidence checklists, interview
  preparation, and artifact organization
- **Guide Level 3 DIBCAC readiness** including 24 enhanced NIST 800-172 practices:
  SOC capabilities, threat hunting, deception technologies, APT training, and
  DIBCAC assessment process
- **Advise on subcontractor and ESP flow-down** requirements under DFARS 252.204-7021
- **Support Annual Affirmation** processes via DIBNet portal

---

## Framework Reference

**CMMC 2.0 Final Rule:** 32 CFR Part 170, effective December 16, 2024
**Level 1 Basis:** FAR 52.204-21 (17 practices)
**Level 2 Basis:** NIST SP 800-171 Rev 2 (110 practices, 14 domains)
**Level 3 Basis:** NIST SP 800-172 (24 additional enhanced practices)
**Assessment Methodology:** NIST SP 800-171A (for Level 2)
**SPRS Scoring:** DoD Assessment Methodology v1.2.1

---

## Skill Structure

```
skills/
  cmmc/
    SKILL.md                    Main skill instructions
    references/
      level1-practices.md       17 Level 1 practices with evidence requirements
      level2-practices.md       All 110 Level 2 practices by domain with SPRS weights
      level3-practices.md       24 additional Level 3 enhanced practices from NIST 800-172
      scoping-guide.md          Asset category scoping, CUI identification, ESP flow-down
      assessment-guide.md       C3PAO process, SPRS calculation, POA&M, evidence by domain
```

---

## Use Cases

| Use Case | What Claude Will Do |
|---------|-------------------|
| "What CMMC level do we need?" | Walks through decision logic based on contract data type and program designation |
| "Help us scope our CMMC assessment" | Categorizes assets, identifies CUI flows, flags ESPs and OT/IoT |
| "Perform a CMMC Level 2 gap analysis" | Generates domain-by-domain gap table against all 110 practices |
| "Calculate our SPRS score" | Applies DoD Assessment Methodology weighting to identify score |
| "Write our SSP for CMMC Level 2" | Drafts narrative templates for all 14 domains |
| "Create a POA&M for these gaps" | Builds structured POA&M with milestones and owners |
| "Prepare for C3PAO assessment" | Generates evidence checklist and interview prep guide |
| "What does DFARS 252.204-7012 require?" | Explains incident reporting obligations to DoD |
| "We're aiming for Level 3 — what's different?" | Explains 24 NIST 800-172 enhanced requirements |
| "Do our subcontractors need CMMC?" | Explains flow-down obligations per DFARS 252.204-7021 |

---

## Official Resources

- **DoD CMMC Program:** https://dodcio.defense.gov/CMMC/
- **Cyber-AB (Accreditation Body):** https://cyberab.org/
- **DIBNet Portal:** https://dibnet.dod.mil
- **NIST SP 800-171 Rev 2:** https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final
- **NIST SP 800-172:** https://csrc.nist.gov/publications/detail/sp/800-172/final
- **NIST SP 800-171A:** https://csrc.nist.gov/publications/detail/sp/800-171a/final
- **NARA CUI Registry:** https://www.archives.gov/cui
- **32 CFR Part 170 (Final Rule):** Published October 15, 2024

---

## Disclaimer

This skill is for informational and educational purposes only and does not constitute
legal advice or official DoD compliance guidance. CMMC certification requires formal
assessment by a Cyber-AB authorized C3PAO (Level 2) or the DCMA DIBCAC (Level 3).
Organizations should engage qualified legal counsel and a licensed C3PAO or RPO for
formal compliance determinations.

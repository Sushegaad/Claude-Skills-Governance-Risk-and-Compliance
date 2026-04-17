# UK Cyber Security and Resilience Bill (CSRB) — Claude Skill

A Claude skill providing expert advisory capability for organisations preparing for
the UK Cyber Security and Resilience Bill (CSRB). Covers scope determination, enhanced
incident reporting, regulator powers, readiness assessment, and transition from the
NIS Regulations 2018.

---

## Important Notice — Bill Status

The Cyber Security and Resilience Bill was announced in the King's Speech on 17 July 2024.
This skill is based on published DSIT policy intent, the Bill as introduced, and publicly
available parliamentary materials. The Bill has not yet received Royal Assent.

**Always verify content against enacted legislation and any statutory instruments or guidance
issued following Royal Assent.** Content in this skill reflects the state of the Bill as
of mid-2025 and will require review after enactment.

Current Bill status: bills.parliament.uk (search: Cyber Security and Resilience Bill)

---

## What This Skill Covers

### 1. CSRB Overview and Context
- Policy rationale for the Bill
- What the CSRB changes compared with NIS Regulations 2018
- Relationship with EU NIS2 Directive
- Key authorities: DSIT, NCSC, sector Competent Authorities

### 2. Scope and Applicability
- Retained scope: Operators of Essential Services (OES) and Digital Service Providers (DSP)
- New scope: Managed Service Providers (MSPs) — policy rationale and definition
- New scope: Large data centres above the qualifying threshold
- Scope determination flowchart

### 3. Enhanced Incident Reporting
- New reportable event categories (ransomware, near-misses, supply chain incidents)
- Compressed 24/72-hour notification timeline
- Reporting templates for OES, DSP, MSP, and data centres
- Cross-regulatory interaction (UK GDPR/ICO, FCA, NHS DSPT)

### 4. Regulator Powers
- Proactive audit powers (directed assessments, scheduled audits)
- Enhanced information-gathering powers
- Enforcement process and financial penalties
- Cross-CA information sharing

### 5. Readiness Assessment
- 5-step readiness framework
- Gap analysis against NIS Regs 2018 baseline
- Scoring methodology

### 6. Transition from NIS Regulations 2018
- Transition checklist for existing OES/DSP organisations
- New obligations for MSPs
- Governance and documentation gap analysis

### 7. Policy and Documentation Generation
- CSRB Readiness Gap Assessment
- Compliance Roadmap
- Incident Response Plan (CSRB edition)
- MSP Security Policy
- Board Briefing Note
- MSP Customer Security Addendum

### 8. Comparative Analysis
- CSRB vs NIS Regulations 2018 (key changes table)
- CSRB vs EU NIS2 Directive (alignment and divergence)

---

## Installation

### Option A — Install from the .skill file

1. Open Claude (claude.ai or the Claude desktop app with skills/plugins enabled)
2. Go to Settings > Skills or Plugins
3. Select "Install from file"
4. Select `uk-nis-csrb.skill` from this folder

### Option B — Install the plugin from source

If you are using Claude with a local plugin directory:

```bash
# Copy the plugin folder to your Claude plugins directory
cp -r plugins/uk-nis-csrb ~/.claude/plugins/
```

Or add the path to your Claude plugin configuration.

---

## Example Prompts

Once installed, ask Claude:

- "Does the CSRB apply to my organisation? We provide IT managed services to NHS trusts."
- "What is a managed service provider under the CSRB and how is one defined?"
- "Walk me through the CSRB incident reporting process — what do I need to report, by when?"
- "We currently comply with NIS Regs 2018 as an OES. What additional steps does the CSRB require of us?"
- "Generate a CSRB readiness gap assessment for our organisation."
- "What new regulatory powers does our Competent Authority have under the CSRB?"
- "We are an MSP — draft a CSRB security policy for our organisation."
- "Generate a board briefing note explaining our CSRB obligations."
- "How does the UK CSRB compare with the EU NIS2 Directive?"
- "What are the incident reporting timelines under the CSRB and how do they differ from current NIS Regs?"

---

## Key Authorities and References

| Body | Role | URL |
|------|------|-----|
| DSIT | Policy lead for CSRB | gov.uk/dsit |
| NCSC | Technical authority and CAF | ncsc.gov.uk |
| Parliament | Bill tracker | bills.parliament.uk |
| ICO | UK GDPR / DSP oversight | ico.org.uk |
| Ofcom | Telecoms sector CA | ofcom.org.uk |
| Ofgem | Energy sector CA | ofgem.gov.uk |
| DfT | Transport sector CA | gov.uk/dft |
| CQC | Health sector CA | cqc.org.uk |

---

## Relationship to Other Skills

This skill is designed to complement:

- **UK NIS skill** — NIS Regulations 2018 compliance (the predecessor regime)
- **NCSC CAF** — The Cyber Assessment Framework underpins CSRB security requirements
- **ISO 27001 skill** — ISO 27001 certification provides strong evidence toward CSRB compliance
- **GDPR/UK GDPR skill** — Cross-regulatory interaction on personal data breach reporting

---

## Version

Version: 1.0.0
Last Updated: 2025
Maintainer: sjackson0109

This skill will be updated following Royal Assent to reflect enacted provisions.

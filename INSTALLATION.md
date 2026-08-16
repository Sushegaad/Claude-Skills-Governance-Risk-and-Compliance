# Installation Guide — GRC Skills for Claude Code

This guide covers how to install the GRC Skills marketplace in [Claude Code](https://claude.ai/claude-code), the AI-powered CLI for developers. The marketplace provides **30 compliance skills** as Claude Code plugins — each one extends Claude with deep, framework-specific expertise across data privacy, information security, AI governance, export controls, sustainability, and accessibility.

---

## What Are Claude Code Plugins?

Plugins let you extend Claude with custom functionality that can be shared across projects and teams. A plugin can contain skills (instructions Claude follows automatically), commands (slash commands you invoke), agents, hooks, and MCP servers. Once installed, a plugin is available in every Claude session on that machine.

A **marketplace** is a catalog of plugins hosted in a Git repository. You add a marketplace once, then install any plugin it lists by name.

---

## Prerequisites

- [Claude Code](https://claude.ai/claude-code) installed (`claude --version` to confirm)
- Git installed and accessible on your PATH
- An active Claude subscription or API key configured

---

## 1. Add the Marketplace

Register the GRC Skills marketplace with a single command. You only need to do this once per machine.

```shell
/plugin marketplace add Sushegaad/Claude-Skills-Governance-Risk-and-Compliance
```

Claude Code will clone the repository, read the `.claude-plugin/marketplace.json` catalog, and register it locally as `grc-skills`. Confirm it was added with:

```shell
/plugin marketplace list
```

---

## 2. Install Individual Skills

Once the marketplace is registered, install only the frameworks you need.

### Information Security & Risk

```shell
/plugin install iso27001@grc-skills
/plugin install soc2@grc-skills
/plugin install fedramp@grc-skills
/plugin install nist-csf@grc-skills
/plugin install nist-800-53@grc-skills
/plugin install cmmc@grc-skills
/plugin install swift-csp@grc-skills
/plugin install ism@grc-skills
/plugin install nzism@grc-skills
/plugin install cis-controls@grc-skills
```

### Data Privacy & Protection

```shell
/plugin install gdpr-compliance@grc-skills
/plugin install hipaa-compliance@grc-skills
/plugin install pci-compliance@grc-skills
/plugin install dpdpa@grc-skills
/plugin install ccpa@grc-skills
/plugin install lgpd@grc-skills
/plugin install vn-pdpl@grc-skills
/plugin install iso27701@grc-skills
```

### Cyber & Resilience Regulation

```shell
/plugin install nis2@grc-skills
/plugin install dora@grc-skills
/plugin install tsa-compliance@grc-skills
/plugin install eu-cra@grc-skills
```

### AI Governance

```shell
/plugin install iso42001@grc-skills
/plugin install nist-ai-rmf@grc-skills
/plugin install eu-ai-act@grc-skills
```

### Export Controls & Sustainability

```shell
/plugin install itar@grc-skills
/plugin install ear@grc-skills
/plugin install csrd@grc-skills
```

### Accessibility

```shell
/plugin install section-508@grc-skills
/plugin install wcag@grc-skills
```

Each plugin is installed to a local cache (`~/.claude/plugins/cache`) and activates immediately in new Claude sessions.

---

## 3. Install All 30 at Once

To install the full GRC suite in a single command:

```shell
/plugin install iso27001@grc-skills soc2@grc-skills fedramp@grc-skills nist-csf@grc-skills nist-800-53@grc-skills cmmc@grc-skills swift-csp@grc-skills ism@grc-skills nzism@grc-skills cis-controls@grc-skills gdpr-compliance@grc-skills hipaa-compliance@grc-skills pci-compliance@grc-skills dpdpa@grc-skills ccpa@grc-skills lgpd@grc-skills vn-pdpl@grc-skills iso27701@grc-skills nis2@grc-skills dora@grc-skills tsa-compliance@grc-skills eu-cra@grc-skills iso42001@grc-skills nist-ai-rmf@grc-skills eu-ai-act@grc-skills itar@grc-skills ear@grc-skills csrd@grc-skills section-508@grc-skills wcag@grc-skills
```

---

## 4. Team Setup — Auto-Install via Project Settings

For teams, you can pre-wire the marketplace into your project so every developer gets the skills automatically when they open the project in Claude Code — no manual install step required.

Add the following to your project's `.claude/settings.json` (include only the skills your team needs):

```json
{
  "extraKnownMarketplaces": {
    "grc-skills": {
      "source": {
        "source": "github",
        "repo": "Sushegaad/Claude-Skills-Governance-Risk-and-Compliance"
      }
    }
  },
  "enabledPlugins": {
    "iso27001@grc-skills": true,
    "soc2@grc-skills": true,
    "fedramp@grc-skills": true,
    "gdpr-compliance@grc-skills": true,
    "hipaa-compliance@grc-skills": true
  }
}
```

Commit this file to your repository. The next time a team member trusts the project folder in Claude Code, the marketplace and plugins will be registered automatically. Only enable the skills your team actually needs — you don't have to include all 30.

---

## Keeping Skills Up to Date

When this repository is updated with new skill content or bug fixes, refresh your local copy with:

```shell
/plugin marketplace update grc-skills
```

To update a specific installed plugin:

```shell
/plugin update iso27001@grc-skills
```

---

## Uninstalling

To remove a plugin:

```shell
/plugin uninstall iso27001@grc-skills
```

To remove the marketplace entirely:

```shell
/plugin marketplace remove grc-skills
```

---

## Available Skills

### Information Security & Risk Management

| Plugin name | Framework | What it does |
|---|---|---|
| `iso27001` | ISO 27001:2022 | Gap analysis, policy writing, Annex A control guidance, SoA generation, risk registers |
| `soc2` | SOC 2 | TSC gap analysis, policy drafting, control documentation, audit evidence, vendor risk |
| `fedramp` | FedRAMP (CR26) | Readiness under CR26 (final; Classes A–D, pipelines open Aug 2026), FedRAMP 20x primary pathway, Legacy Ready conversion, SSP narratives, POA&M SLAs, OSCAL mandate Sep 30 2026, ConMon |
| `nist-csf` | NIST CSF 2.0 / 1.1 | Gap assessments, organisational profiles, implementation tiers, roadmaps, cross-framework mapping |
| `nist-800-53` | NIST SP 800-53 Rev 5 | All 20 control families, FIPS 199/200 categorisation, baseline selection, SSP narratives, RMF |
| `cmmc` | CMMC 2.0 | Level 1/2/3 gap analysis, SPRS scoring, POA&M, CUI scoping, assessment prep — incl. the Jul 13 2026 Phase 2 suspension interim guidance |
| `swift-csp` | SWIFT CSP 2026 | CSCF v2026 (32 controls: 25 mandatory + 7 advisory), Control 2.4 back-office data flow now mandatory, architecture scoping (A1/A2/A3/A4/B), independent assessment prep, KYC-SA attestation |
| `ism` | Australian ISM (ASD) | ISM control assessment (June 2026 release incl. AI controls), Essential Eight maturity, system authorisation, IRAP prep |
| `nzism` | NZISM (GCSB/NCSC NZ) | NZISM gap analysis, C&A for Restricted+ systems, NZ classification framework, SSP preparation |
| `cis-controls` | CIS Controls v8 | IG selection, all 153 safeguards, gap assessment, SIEM/log design, cross-framework mapping |

### Data Privacy & Protection

| Plugin name | Framework | What it does |
|---|---|---|
| `gdpr-compliance` | GDPR / UK GDPR | Code audits, privacy notices, DPAs, DPIAs, data flow reviews, article-cited Q&A |
| `hipaa-compliance` | HIPAA | Document generation, technical safeguards for cloud, breach response guidance |
| `pci-compliance` | PCI DSS v4.0.1 | CDE scoping, SAQ selection, gap assessments, control guidance, QSA audit prep |
| `dpdpa` | India DPDPA 2023 | Data principal rights, consent management, DPDPB registration, breach notification |
| `ccpa` | CCPA / CPRA | Consumer rights workflows, ADMT opt-out (regulations effective Jan 2026, deadline Jan 2027), cybersecurity audit/risk assessment obligations, 2026 enforcement precedents (Disney $2.75M, PlayOn $1.1M) |
| `lgpd` | Brazil LGPD | All 10 legal bases, Brazil-EU mutual adequacy (Jan 2026 — SCCs no longer needed for Brazil↔EU transfers), data subject rights, ANPD enforcement, breach notification |
| `vn-pdpl` | Vietnam PDPL 2026 | Gap analysis, cross-border transfer impact assessments, DPIAs, breach notification (72h) |
| `iso27701` | ISO 27701:2019 | PIMS gap analysis, PII controller/processor mapping, GDPR alignment |

### Cyber & Resilience Regulation

| Plugin name | Framework | What it does |
|---|---|---|
| `nis2` | NIS2 Directive (EU) | Essential/important entity scoping, Art. 21 technical measures, 24h/72h incident reporting |
| `dora` | DORA (EU) | ICT risk management, TLPT, register of information, incident classification, third-party oversight |
| `tsa-compliance` | TSA Security Directives | Pipeline, freight rail, and transit OT/ICS cybersecurity — CIP/COIP, IRP, ADR, CAP |
| `eu-cra` | EU CRA 2024/2847 | PDE classification (Default/Class I/Class II), Annex I gap analysis, SBOM, 24/72h ENISA reporting |

### AI Governance

| Plugin name | Framework | What it does |
|---|---|---|
| `iso42001` | ISO/IEC 42001:2023 | AI Management System gap analysis, AISIA, AI risk assessment, SoA, certification readiness |
| `nist-ai-rmf` | NIST AI RMF 1.0 | GOVERN/MAP/MEASURE/MANAGE function guidance, AI risk registers, organisational profiles |
| `eu-ai-act` | EU AI Act 2024/1689 | Risk classification (9 prohibited practices, high-risk/limited/minimal), Digital Omnibus (Reg. (EU) 2026/1744, in force Jul 27 2026) extended deadlines (Annex III Dec 2027, Annex I Aug 2028), GPAI enforcement active Aug 2, 2026 |

### Export Controls & Sustainability

| Plugin name | Framework | What it does |
|---|---|---|
| `itar` | ITAR (22 CFR 120–130) | USML classification, DSP-5/73/85 licence workflows, TAA/MLA drafting, deemed export, DDTC |
| `ear` | EAR (15 CFR 730–774) | ECCN classification, licence requirements, Entity List screening, licence exceptions |
| `csrd` | CSRD / ESRS | 2026 Omnibus scoping (1,000+ employees & €450M), revised ESRS (Jul 2026), double materiality, GRI/TCFD gap analysis |

### Accessibility

| Plugin name | Framework | What it does |
|---|---|---|
| `section-508` | Section 508 (US) | VPAT 2.x ACR completion, procurement language (FAR 52.239-2), AT testing, undue burden exceptions |
| `wcag` | WCAG 2.0/2.1/2.2 | POUR audit, SC-level gap analysis, ARIA patterns, screen reader testing, legal compliance mapping |

---

## Troubleshooting

**"SKILL.md file must be in the top-level folder, not nested deeper" (claude.ai upload)**
Every published `.skill` file already has the correct structure (`<skill-name>/SKILL.md`, exactly one folder deep) — this error means the file was repackaged or downloaded incorrectly. Checklist:

1. **Download the `.skill` file itself**, via the repository's Releases page or by opening the file on GitHub and clicking **Download raw file** (the ⬇ icon). Do not use "Download ZIP" on the repository or folder — that wraps everything in extra folders.
2. **Do not unzip and re-zip the `.skill` file.** If you must repackage (e.g., after editing), zip from the folder's *parent* so the archive contains exactly one top-level folder with `SKILL.md` directly inside it:
   ```bash
   cd "NIS2 - Claude Skill" && unzip nis2.skill -d /tmp/skill && cd /tmp/skill && zip -r nis2.skill nis2
   ```
   Zipping the folder that *contains* the skill folder produces `something/nis2/SKILL.md` (two levels deep) → this exact error. macOS Finder's "Compress" also adds `__MACOSX` entries; prefer the `zip` command.
3. **Verify before uploading**: `unzip -l nis2.skill` should list `nis2/SKILL.md` — one folder, then the file.

Our CI (`tests/test_skill_installability.py`) verifies every shipped `.skill` for one-level nesting, valid frontmatter (name format, description ≤1024 chars), no junk archive entries, and that bundled content matches the source tree — so a correctly downloaded file always installs.

**Marketplace not found after adding**
Run `/plugin marketplace list` to confirm it was registered. If it's missing, check that your Git credentials allow access and retry.

**Plugin installation fails**
Verify you have network access to GitHub and that your Git version is current. You can also clone the repo manually to test: `git clone https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance.git`

**Skills not activating in sessions**
Restart Claude Code after installing plugins. Skills activate in new sessions, not mid-session.

**Git timeout on slow connections**
Increase the timeout via environment variable before running Claude Code:
```bash
export CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS=300000
```

For additional help, [open an issue](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/issues) on the repository.

---

## See Also

- [Claude Code documentation](https://claude.ai/claude-code)
- [Plugin marketplace docs](https://code.claude.com/docs/en/plugin-marketplaces)
- [README](README.md) — full skill descriptions and use cases
- [GitHub repository](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)

# Installation Guide — GRC Skills for Claude Code

This guide covers how to install the GRC Skills marketplace in [Claude Code](https://claude.ai/claude-code), the AI-powered CLI for developers. The marketplace provides five compliance skills as Claude Code plugins — each one extends Claude Code with deep, framework-specific expertise for ISO 27001, SOC 2, FedRAMP, GDPR, and HIPAA.

---

## What Are Claude Code Plugins?

Plugins let you extend Claude Code with custom functionality that can be shared across projects and teams. A plugin can contain skills (instructions Claude follows automatically), commands (slash commands you invoke), agents, hooks, and MCP servers. Once installed, a plugin is available in every Claude Code session on that machine.

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

Claude Code will clone the repository, read the `.claude-plugin/marketplace.json` catalog, and register it locally as `grc-skills`. You can confirm it was added with:

```shell
/plugin marketplace list
```

---

## 2. Install Individual Skills

Once the marketplace is registered, install only the frameworks you need.

```shell
/plugin install iso27001@grc-skills
```

```shell
/plugin install soc2@grc-skills
```

```shell
/plugin install fedramp@grc-skills
```

```shell
/plugin install gdpr-compliance@grc-skills
```

```shell
/plugin install hipaa-compliance@grc-skills
```

Each plugin is installed to a local cache (`~/.claude/plugins/cache`) and activates immediately in new Claude Code sessions.

---

## 3. Install All Five at Once

To install the full GRC suite in a single command:

```shell
/plugin install iso27001@grc-skills soc2@grc-skills fedramp@grc-skills gdpr-compliance@grc-skills hipaa-compliance@grc-skills
```

---

## 4. Team Setup — Auto-Install via Project Settings

For teams, you can pre-wire the marketplace into your project so every developer gets the skills automatically when they open the project in Claude Code — no manual install step required.

Add the following to your project's `.claude/settings.json`:

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

Commit this file to your repository. The next time a team member trusts the project folder in Claude Code, the marketplace and plugins will be registered automatically. Only enable the skills your team actually needs — you don't have to include all five.

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

| Plugin name | Framework | What it does |
|---|---|---|
| `iso27001` | ISO 27001:2022 | Gap analysis, policy writing, Annex A control guidance, SoA generation, risk registers |
| `soc2` | SOC 2 | TSC gap analysis, policy drafting, control documentation, audit evidence, vendor risk |
| `fedramp` | FedRAMP Moderate/High | Readiness assessments, SSP narratives, POA&M, NIST 800-53 control mapping, ConMon |
| `gdpr-compliance` | GDPR / UK GDPR | Code audits, privacy notices, DPAs, DPIAs, data flow reviews, article-cited Q&A |
| `hipaa-compliance` | HIPAA | Document generation, technical safeguards for cloud, breach response guidance |

---

## Troubleshooting

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

# EU Cyber Resilience Act (CRA) — Claude Skill

A Claude skill for **Regulation (EU) 2024/2847 — the EU Cyber Resilience Act (CRA)**, which establishes mandatory cybersecurity requirements for all **Products with Digital Elements (PDEs)** sold in the EU market. Full application: **11 December 2027**.

---

## 1. What Does the Skill Do?

This skill turns Claude into an expert advisor on the EU Cyber Resilience Act — the EU's landmark regulation requiring all connected hardware and software products to meet mandatory cybersecurity and vulnerability handling standards before they can be sold in the EU. It provides actionable guidance on:

- Determining whether a product is in scope and which class it falls into (Default / Class I / Class II)
- Conducting Annex I gap analysis against all essential security requirements and vulnerability handling obligations
- Selecting and completing the correct conformity assessment route (self-assessment vs. Notified Body)
- Preparing technical documentation (Annex VII), SBOM, and EU Declaration of Conformity
- Affixing CE marking correctly and registering products in the EU database
- Building a vulnerability handling programme (CVD policy, 24/72-hour ENISA reporting, SBOM management)
- Understanding support period obligations (minimum 5 years) and end-of-life notification requirements
- Navigating manufacturer, importer, and distributor roles and their respective obligations
- Understanding relationships to NIS2, GDPR, EU AI Act, and RED

---

## 2. Intended Audiences

- **Product security and engineering teams** building connected hardware or software products sold in the EU
- **Compliance and legal teams** at manufacturers, importers, and distributors of digital products
- **IoT and embedded systems developers** assessing CRA applicability to their devices
- **Cybersecurity consultants** advising clients on EU product security regulation
- **Open-source maintainers and foundations** assessing their obligations as "open-source software stewards"
- **Procurement teams** verifying CRA compliance of products from suppliers

---

## 3. Common Use Cases

1. **Scope assessment** — "Is our smart home hub in scope for the CRA? Is it Class I or Default?"
2. **Gap analysis** — "We make an industrial router. What Annex I requirements are we not meeting?"
3. **Conformity assessment** — "We have a password manager. Do we need a Notified Body or can we self-certify?"
4. **SBOM** — "How do we build a CRA-compliant SBOM? What format should we use?"
5. **Vulnerability reporting** — "We found an actively exploited vulnerability in our firmware. Who do we report to and when?"
6. **Support period** — "We're planning a 3-year product lifecycle. Does CRA require a longer support period?"
7. **Importer obligations** — "We import connected sensors from China. What are our CRA obligations?"
8. **Open-source** — "We maintain a widely used open-source library used in IoT devices. Are we a 'software steward' under CRA?"
9. **Penalty risk** — "What fines are we exposed to if a product doesn't meet Annex I requirements?"
10. **Cross-regulation** — "Our product is subject to both the EU AI Act and CRA. How do they interact?"

---

## 4. How to Use

### Install the Skill

**Option A — Direct install (recommended):**
1. Open the Claude desktop app
2. Go to **Settings → Skills**
3. Click **Add Skill** and upload `eu-cra.skill`

**Option B — Via GRC Plugin Marketplace:**
1. Open Claude desktop app
2. Go to **Settings → Plugins**
3. Search for "GRC Skills" or "EU CRA"
4. Install the `eu-cra` skill

### Example Prompts

Once installed, try prompts like:

- *"We make a commercial VPN software product sold in the EU. What CRA product class does it fall into, and what conformity assessment route applies?"*
- *"Conduct an Annex I Part I gap analysis for our industrial IoT gateway — it runs Linux, has SSH and MQTT interfaces, and uses hardcoded admin credentials as default."*
- *"We discovered that a CVE in our product's OpenSSL component is being actively exploited. What are our CRA reporting obligations and timeline?"*
- *"Draft a vulnerability handling programme outline for a consumer IoT manufacturer — covering VDP, SBOM, ENISA reporting, and end-of-life policy."*
- *"We import smart locks from a South Korean manufacturer. What do we need to verify and document before we can sell them in Germany?"*

---

## 5. Skill Implementation Details

| Property | Value |
|---|---|
| **Skill identifier** | `eu-cra` |
| **Regulation** | Regulation (EU) 2024/2847 (Cyber Resilience Act) |
| **Published** | 20 November 2024 (OJ L, 2024/2847) |
| **Entry into force** | 10 December 2024 |
| **Full application** | 11 December 2027 |
| **Vulnerability reporting** | 11 September 2026 |
| **Enforcing body** | National Market Surveillance Authorities + ENISA |
| **Skill version** | 1.7.1 |
| **File** | `eu-cra.skill` |

**Reference files bundled in the skill:**

- `references/essential-requirements.md` — Annex I Part I (10 security properties) and Part II (9 vulnerability handling obligations), complete Annex III (Class I, 35 categories) and Annex IV (Class II, 12 categories) lists, SBOM requirements, 24/72-hour ENISA reporting timelines, support period obligations, manufacturer/importer/distributor duties, open-source software steward obligations

- `references/conformity-assessment.md` — Conformity assessment routes by product class, Module A self-assessment steps, Notified Body assessment process, technical documentation (Annex VII) required contents, EU Declaration of Conformity elements, CE marking rules and placement, EU database registration, market surveillance powers, penalty framework (up to €15M / 2.5% global turnover), harmonised standards mapping

**Key law facts:**
- 3 product classes: Default (self-assessment), Class I (35 categories, self-assessment or NB), Class II (12 categories, mandatory NB)
- Annex I: 10 security property requirements + 9 vulnerability handling obligations
- SBOM required on request in machine-readable format (SPDX/CycloneDX recommended)
- Actively exploited vulnerability: 24-hour early warning + 72-hour full report to ENISA/CSIRTs
- Minimum support period: 5 years (or expected product lifetime if shorter)
- End-of-life notice: at least 1 year before end of security support
- Max penalty: €15 million or 2.5% global annual turnover for Annex I violations

---

## 6. Author

**Hemant Naik**
Email: hemant.naik@gmail.com
GitHub: [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)

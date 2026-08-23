# Web Content Accessibility Guidelines (WCAG) Skill for Claude

> **Disclaimer:** This skill provides educational and advisory guidance based on W3C WCAG documentation. It does not constitute legal advice. Conformance claims, accessibility statements, and legal compliance determinations must involve qualified accessibility specialists and legal counsel. WCAG is developed by the W3C Web Accessibility Initiative (WAI) and is subject to ongoing revision — always verify against the current normative specification at w3.org/WAI/WCAG.

---

## 1. What Does the Skill Do?

This skill turns Claude into an expert advisor on the **Web Content Accessibility Guidelines (WCAG)** — the W3C international standard for digital accessibility developed by the Web Accessibility Initiative (WAI). It provides structured, criterion-level guidance to developers, designers, product owners, QA engineers, and compliance teams implementing WCAG across web, mobile, and digital content.

The skill covers three normative W3C Recommendations: **WCAG 2.0** (2008), **WCAG 2.1** (2018), and **WCAG 2.2** (October 2023). It is grounded in all four POUR principles — Perceivable, Operable, Understandable, Robust — and understands the full success criteria set: 38 criteria in WCAG 2.0, 17 additional criteria added in WCAG 2.1, and 9 further criteria added in WCAG 2.2 (plus the removal of SC 4.1.1 Parsing). It also provides a preview of the WCAG 3.0 working draft and its new Bronze/Silver/Gold scoring model.

Beyond criterion explanation, the skill provides implementation-ready output: accessibility audit issue tables with severity and element references, conformance reviews, ARIA patterns matched to WAI-ARIA Authoring Practices Guide keyboard conventions, contrast ratio calculations, code-annotated reviews with violations and corrected examples, and accessibility statements conforming to the EU Web Accessibility Directive model. It also maps WCAG to the global legal landscape — EN 301 549 (EU EAA), Section 508, UK PSBAR 2018, AODA, and ADA Title III case law — enabling compliance teams to understand which WCAG version and level is legally required in each jurisdiction.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|----------------------|
| **Frontend Developers** | Criterion-level code fixes, ARIA pattern implementation, keyboard interaction patterns (APG), contrast ratio checks, HTML semantic markup guidance |
| **UX and Visual Designers** | Colour contrast requirements (SC 1.4.3, 1.4.11), focus indicator design (SC 2.4.7, 2.4.11), touch target sizing (SC 2.5.8), cognitive accessibility (SC 3.3.x) |
| **QA and Accessibility Testers** | Audit methodology, AT + browser pairings, automated tool selection, manual testing checklist, per-criterion test procedures |
| **Product Owners and Managers** | Conformance level selection, scope definition, remediation prioritisation, release-gate accessibility criteria |
| **Compliance and Legal Teams** | Jurisdiction-specific legal requirements, accessibility statement drafting, conformance claim wording, WCAG version mapping to laws |
| **Content Authors and Editors** | Alt text writing, link text quality, heading structure, caption requirements, language attributes |
| **Accessibility Consultants** | Detailed criterion guidance, sufficient and failure technique references, advisory techniques, cross-version compatibility analysis |
| **EU/UK Public Sector Teams** | EN 301 549, EU Web Accessibility Directive (2016/2102), European Accessibility Act (EAA, Directive 2019/882) compliance |

---

## 3. Common Use Cases

### Accessibility Audits and Gap Assessments

- Run a WCAG 2.1 AA accessibility audit gap assessment for our e-commerce checkout flow
- Produce an audit issue table with criterion number, issue description, element reference, severity, and remediation steps
- We have these findings from our automated axe scan — classify them by WCAG criterion and prioritise remediation
- What WCAG 2.2 AA criteria might we fail that we were not checking against WCAG 2.1?
- Identify the highest-severity WCAG 2.1 AA failures that would block screen reader users

### Criterion Explanations and Implementation Guidance

- Explain SC 1.4.3 Contrast (Minimum) — what exactly does 4.5:1 mean and how do I calculate it?
- What does SC 2.4.11 Focus Not Obscured require and how do I fix sticky headers that cover focused elements?
- Walk me through implementing SC 3.3.8 Accessible Authentication — what counts as an accessible alternative to CAPTCHA?
- What ARIA roles and properties does SC 4.1.2 require for a custom tab panel widget?
- Explain the difference between SC 2.5.7 Dragging Movements and SC 2.5.8 Target Size — both new in WCAG 2.2

### Code Review and ARIA Implementation

- Review this React modal component for WCAG 2.1 AA violations
- Show me the correct ARIA pattern for an accordion that expands and collapses
- My autocomplete combobox is not announced correctly by NVDA — what ARIA attributes am I missing?
- Annotate this HTML form with all the WCAG failures and provide the corrected version
- What ARIA live region pattern should I use to announce "Item added to cart" to screen reader users?

### Conformance and Accessibility Statements

- Draft a WCAG 2.1 Level AA accessibility statement for our UK public sector website
- What must an accessibility statement include to comply with the EU Web Accessibility Directive?
- We claim WCAG 2.1 AA conformance but fail SC 1.2.4 Captions (Live) — how do we document this exception?
- What is the difference between WCAG 2.0 AA, 2.1 AA, and 2.2 AA conformance claims?
- Can a site that fails one AA criterion still claim partial conformance?

### Legal and Regulatory Mapping

- What WCAG version and level is required under the European Accessibility Act (EAA) for private sector companies?
- Map WCAG requirements to the laws that apply in EU, US, UK, Canada, and Australia
- Our product is used in the EU — does the June 2025 EAA deadline apply to us?
- How does EN 301 549 relate to WCAG 2.1, and what chapters cover web content?
- A client says their ADA settlement requires WCAG 2.1 AA — what does that mean practically?

### Testing Methodology

- What is the recommended testing methodology for a WCAG 2.1 AA audit?
- Which automated tools catch the most WCAG failures and what are their limitations?
- What screen reader and browser combinations should I use for comprehensive testing?
- How do I test SC 1.4.10 Reflow at 320 CSS pixels?
- What does the Text Spacing bookmarklet test and how do I use it for SC 1.4.12?

### WCAG 2.2 New Criteria

- What are all the new success criteria in WCAG 2.2 and which are Level AA?
- We currently meet WCAG 2.1 AA — what additional work is needed to reach WCAG 2.2 AA?
- Explain the three new focus-related criteria in WCAG 2.2 (SC 2.4.11, 2.4.12, 2.4.13)
- Is SC 4.1.1 Parsing still required under WCAG 2.2?
- How does SC 3.3.7 Redundant Entry affect multi-step forms and checkout flows?

---

## 4. How to Use the Skill

### Installation

1. Download the `wcag.skill` file from the `WCAG - Claude Skill/` folder
2. In Claude, go to **Settings → Skills**
3. Upload the `.skill` file
4. The skill activates automatically for relevant conversations — no special command needed

### Triggering the Skill

The skill triggers automatically for any digital accessibility question, even without explicitly mentioning "WCAG" or "skill." Example phrases that activate it:

- *"Why is my site failing accessibility checks?"*
- *"What contrast ratio does this text need?"*
- *"My screen reader isn't reading the modal correctly"*
- *"We need to comply with EN 301 549 for the EU market"*
- *"Write an accessibility statement for our website"*
- *"What changed in WCAG 2.2?"*
- *"How do I make this dropdown keyboard accessible?"*
- *"We got an ADA demand letter about our website's accessibility"*

### Example Prompts

```
"Run a WCAG 2.2 AA gap assessment for a SaaS web application. Known 
issues include: no skip link, some icon buttons without accessible names, 
drag-only sortable lists, a CAPTCHA with no alternative on the login page, 
and colour-only required field indicators on forms."
```

```
"Review this React component for WCAG 2.1 AA violations and provide 
the corrected version with inline comments explaining each fix:

<div onClick={handleClick} class='btn'>Submit</div>
<div class='error' style='color:red'>Please fix errors above</div>
<img src='logo.png'>
<div role='checkbox'>Accept terms</div>"
```

```
"Draft a WCAG 2.1 Level AA accessibility statement for a UK public 
sector organisation. Include: conformance claim, scope, known 
non-conformances (SC 1.2.4 live captions not provided, SC 2.4.5 
no site search), alternatives available, date of last assessment, 
and complaints procedure as required by PSBAR 2018."
```

```
"Map WCAG 2.1 AA to the accessibility laws that apply to us. We sell 
software to: federal agencies in the US, enterprises in the EU, 
public sector bodies in the UK, and large organisations in Ontario, 
Canada. For each jurisdiction, tell us the required WCAG version, 
level, applicable law, and compliance deadline."
```

```
"Our development team needs a practical WCAG 2.2 AA testing checklist. 
For each criterion, include: what to test, which automated tool covers 
it, which AT + browser combination to use for manual testing, and the 
most common failure pattern."
```

---

## 5. Skill Implementation Details

### Architecture

```
plugins/wcag/skills/wcag/
├── SKILL.md                        # Main skill: WCAG version history, POUR principles,
│                                   # full success criteria tables (2.0, 2.1, 2.2) with
│                                   # common failures, conformance levels, audit workflows,
│                                   # accessibility statement requirements, ARIA usage
│                                   # principles, contrast ratio calculation, global
│                                   # legal framework mapping, response format routing
└── references/
    └── criteria-detail.md          # Full WCAG 2.2 success criteria detailed reference:
                                    # sufficient techniques, failure techniques, advisory
                                    # techniques, ARIA key patterns, WCAG 2.2 new criteria
                                    # summary, automated testing tools comparison,
                                    # manual testing checklist, screen reader + browser
                                    # pairings, bookmarklets and extensions

WCAG - Claude Skill/
├── WCAG-README.md                  # This file
└── wcag.skill                      # Standalone installable skill file
```

### What's in SKILL.md

- **YAML frontmatter** with skill name, description, and broad auto-trigger phrases covering all WCAG-related topics
- **WCAG versions table** — 2.0 (2008), 2.1 (2018), 2.2 (October 2023), 3.0 (working draft) with status, key additions, and backwards compatibility notes
- **Legal context** — WCAG as the technical foundation for EU EAA, EN 301 549, Section 508, UK Equality Act, AODA, ADA Title III
- **Response format routing table** — task type to output format (criterion explanation, audit, conformance review, gap assessment, accessibility statement, code review, legal mapping, general question)
- **Full POUR criteria tables** — all WCAG 2.0, 2.1, and 2.2 Level A and AA success criteria with SC number, level (A/AA), requirement, and common failures
- **Conformance levels** — A (minimum), AA (universal legal benchmark), AAA (enhanced) with legal relevance for each
- **Audit workflow** — 7-step full accessibility audit methodology (automated, keyboard, screen reader, contrast, zoom/reflow, cognitive, documentation)
- **Accessibility statement** — required elements including conformance claim, scope, known non-conformances, alternatives, date, contact, complaints procedure
- **ARIA usage principles** — five key rules including no-ARIA-is-better-than-bad-ARIA, first rule of ARIA, required properties per role, APG keyboard patterns, live regions
- **Contrast ratio calculation** — formula and thresholds for SC 1.4.3 (4.5:1 normal, 3:1 large) and SC 1.4.11 (3:1 UI components)
- **Global legal framework mapping** — 9-jurisdiction table (EN 301 549, EAA, EU Web Accessibility Directive, Section 508, ADA, UK PSBAR 2018, Equality Act, AODA, DDA Australia) with WCAG version and level required

### What's in the reference files

| File | Contents |
|------|----------|
| `references/criteria-detail.md` | Detailed entries for all WCAG 2.2 Level A and AA success criteria grouped by guideline (1.1–4.1); sufficient techniques (WCAG technique codes: G, H, ARIA, F); common failure technique codes (F-codes) for each criterion; ARIA required attributes by widget type (accordion, alert, autocomplete, button, checkbox, combobox, dialog, menu, progressbar, radio, slider, tablist, tooltip); SC 4.1.3 ARIA live region patterns (aria-live, role="status/alert/log", aria-atomic); WCAG 2.2 new criteria summary table (9 new SC, SC removed); automated testing tools comparison (axe-core, Lighthouse, WAVE, IBM Equal Access, Pa11y, Colour Contrast Analyser) with percentage coverage; manual testing checklist (10 steps); screen reader + browser pairings table; bookmarklets and browser extensions reference |

### Inputs used to build the skill

| Source | Description |
|--------|-------------|
| **WCAG 2.0 W3C Recommendation (December 2008)** | Foundational 61 criteria across 12 guidelines and 4 principles |
| **WCAG 2.1 W3C Recommendation (June 2018)** | 17 additional criteria covering mobile, low vision, and cognitive accessibility |
| **WCAG 2.2 W3C Recommendation (October 2023)** | 9 new criteria (SC 2.4.11–13, 2.5.7–8, 3.2.6, 3.3.7–8, 3.3.9); removal of SC 4.1.1 |
| **WCAG 2.2 Understanding Documents (W3C WAI)** | Sufficient techniques, advisory techniques, and failure techniques per criterion |
| **WAI-ARIA Authoring Practices Guide (W3C)** | Keyboard interaction patterns and required ARIA properties for all major widget types |
| **EN 301 549 (2021, ETSI)** | European standard referencing WCAG 2.1 AA for ICT products and services (Chapters 9–11) |
| **EU Web Accessibility Directive 2016/2102** | EU public sector WCAG 2.1 AA requirement and accessibility statement obligations |
| **European Accessibility Act (EAA) — Directive 2019/882** | Private sector WCAG 2.1 AA requirement via EN 301 549; June 2025 compliance deadline |
| **Section 508 Revised Standards (36 CFR Part 1194)** | US federal WCAG 2.0 AA requirement under E205 |
| **UK PSBAR 2018 and Equality Act 2010** | UK public and private sector WCAG 2.1 AA expectations |
| **AODA Web Standard** | Ontario WCAG 2.0 AA for large private-sector organisations (since 2021) |
| **axe-core, WAVE, Lighthouse, IBM Equal Access** | Automated testing tool capability mapping and limitation analysis |

### Skill trigger phrases

`WCAG` · `Web Content Accessibility Guidelines` · `WCAG 2.0` · `WCAG 2.1` · `WCAG 2.2` · `WCAG 3.0` · `accessibility audit` · `accessibility conformance` · `POUR principles` · `success criteria` · `conformance level A AA AAA` · `colour contrast` · `keyboard accessibility` · `screen reader compatibility` · `focus indicator` · `focus visible` · `skip navigation` · `alt text` · `ARIA` · `accessible name` · `EN 301 549` · `European Accessibility Act` · `EAA accessibility` · `EU Web Accessibility Directive` · `ADA website accessibility` · `accessibility statement` · `WCAG gap assessment` · `WCAG audit` · `mobile accessibility` · `cognitive accessibility` · `WCAG 2.2 new criteria` · `touch target size` · `dragging movements` · `accessible authentication` · `redundant entry` · `reflow 320px` · `non-text contrast` · `text spacing` · `content on hover or focus`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

---

*Skill version: 1.8.0 — August 2026*

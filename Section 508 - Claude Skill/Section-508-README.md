# Section 508 (US Federal ICT Accessibility) Skill for Claude

> **Disclaimer:** This skill provides educational and advisory guidance based on publicly available Section 508 standards and WCAG 2.0 documentation. It does not constitute legal advice. Accessibility conformance determinations, undue burden findings, and procurement decisions must involve qualified legal counsel and accessibility specialists. Section 508 requirements are enforced by the US Access Board (36 CFR Part 1194) and the General Services Administration (GSA).

---

## 1. What Does the Skill Do?

This skill turns Claude into an expert advisor on **Section 508 of the Rehabilitation Act of 1973** (29 U.S.C. § 794d), as revised by the Workforce Investment Act of 1998 and updated by the **Revised Section 508 Standards** effective January 18, 2018 (36 CFR Part 1194). It helps federal agencies, federal contractors, and ICT vendors achieve and demonstrate accessibility compliance across the full range of information and communications technology.

The skill is grounded in the 2018 standards refresh, which incorporated **WCAG 2.0 Level A and AA** as the technical standard for web content (E205), software (E204), and electronic documents. It covers the complete ICT scope — web content, software, electronic documents, hardware (kiosks, copiers, phones), video and audio, telecommunications, authoring tools, and support documentation — along with all applicable exceptions under E202 including undue burden, fundamental alteration, national security systems, back-office equipment, and legacy ICT.

Rather than generic accessibility advice, the skill routes each request to a structured output type: VPAT/ACR section-by-section completion, accessibility audit issue tables with criterion citations, gap assessments with remediation priorities, procurement RFP language with FAR clause references, undue burden documentation procedures, and PDF accessibility checklists. All outputs cite the specific **Section 508 provision** (e.g., E205, E302.1) or **WCAG 2.0 Success Criterion** (e.g., SC 1.4.3) — never just the principle.

The skill also covers the assistive technology testing matrix — JAWS + Chrome, NVDA + Chrome/Firefox, VoiceOver + Safari, TalkBack + Chrome, Dragon NaturallySpeaking — and understands the federal procurement cycle including FAR clause 52.239-2 and OMB Memorandum M-24-08 (January 2024).

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|----------------------|
| **Federal Agency Section 508 Coordinators** | Gap assessments, audit planning, policy drafting, procurement clause review, agency reporting |
| **Federal CIOs and IT Leadership** | Program-level compliance posture review, undue burden determinations, remediation roadmap prioritisation |
| **Federal Acquisition / Contracting Officers** | RFP Section 508 language, FAR clause 52.239-2 application, VPAT evaluation guidance, vendor assessment |
| **ICT Vendors and Contractors Selling to Federal Agencies** | VPAT/ACR completion using VPAT 2.x WCAG Edition, remediation planning, conformance evidence documentation |
| **Developers and Engineers** | Criterion-level implementation guidance, ARIA patterns, HTML fixes, keyboard accessibility, automated testing tool selection |
| **UX Designers** | Colour contrast requirements (SC 1.4.3, 1.4.11), focus visibility (SC 2.4.7), error identification (SC 3.3.1–3.3.4), form labelling |
| **Content Authors and Document Creators** | PDF accessibility requirements, document tagging, reading order, form field labelling |
| **Legal and Compliance Teams** | Undue burden documentation process, alternative means of access requirements, legal reference mapping (29 U.S.C. § 794d, 36 CFR Part 1194) |
| **QA and Accessibility Testers** | Testing methodology, AT + browser pairings, audit documentation templates, VPAT deficiency identification |

---

## 3. Common Use Cases

### VPAT and Accessibility Conformance Report (ACR) Completion

- Help me complete a VPAT 2.x WCAG Edition ACR for our federal procurement
- What is the difference between "Supports," "Partially Supports," "Does Not Support," and "Not Applicable"?
- Review this VPAT — what deficiencies would cause a federal procurement officer to reject it?
- Our vendor submitted a VPAT on VPAT 1.x — what should we request instead?
- What testing methodology should we document in our ACR?

### Accessibility Audits and Gap Assessments

- Run a Section 508 gap assessment for our federal web portal — we have these known issues
- Produce an audit issue table with criterion citations, element references, and remediation steps
- We failed SC 1.4.3 on many elements — give me a prioritised remediation plan
- Identify which WCAG 2.0 AA success criteria are most commonly failed in federal systems
- We're migrating from a legacy system — how do we assess the new system for 508 compliance before launch?

### Procurement and RFP Language

- Draft Section 508 language for an RFP for a new case management system
- What does FAR clause 52.239-2 require and when is it mandatory?
- What remediation SLAs should we include in ICT procurement contracts (critical, high, medium findings)?
- How do we evaluate competing vendors' VPATs during source selection?
- We're renewing a contract — what updated 508 requirements apply under OMB M-24-08?

### PDF and Electronic Document Accessibility

- Walk me through making our agency's PDF accessible under Section 508 and SC 1.3.1
- What are the required PDF tags and how do I verify them in Acrobat Pro?
- Our Word document exports to an untagged PDF — how do we fix the source document?
- How do we associate form field labels in an accessible PDF under SC 4.1.2?

### Undue Burden and Exception Documentation

- Walk me through the undue burden determination process under E202.6
- What documentation must an agency head or CIO sign for an undue burden exception?
- What alternative means of access must we provide when claiming undue burden?
- Does legacy ICT acquired before January 18, 2018, require 508 compliance?
- When does the national security systems exception under E202.3 apply?

### Policy and Procedure Development

- Draft a Section 508 Accessibility Policy for our federal agency
- Write a Section 508 Program Plan covering roles, responsibilities, testing methodology, and reporting
- What roles and responsibilities should a federal agency's 508 programme include?
- Draft procurement procedures to ensure ICT acquisitions include 508 requirements from the start

---

## 4. How to Use the Skill

### Installation

1. Download the `section-508.skill` file from the `Section 508 - Claude Skill/` folder
2. In Claude, go to **Settings → Skills**
3. Upload the `.skill` file
4. The skill activates automatically for relevant conversations — no special command needed

### Triggering the Skill

The skill triggers automatically when your message relates to Section 508, federal ICT accessibility, VPAT completion, or WCAG compliance in a federal context. Example phrases that activate it:

- *"We need to complete a VPAT for our federal agency customer"*
- *"What does Section 508 require for our web application?"*
- *"Our 508 audit found a contrast failure — how do we fix it?"*
- *"Help me write the accessibility section of our RFP"*
- *"What assistive technologies should we test against for federal compliance?"*
- *"Can we claim an undue burden exception for this legacy system?"*
- *"What does OMB M-24-08 change for our 508 program?"*

### Example Prompts

```
"Complete a VPAT 2.x WCAG Edition for a web-based document management 
system. The product supports JAWS with Chrome, has full keyboard 
navigation, but fails SC 1.4.3 on 12% of text elements and has 
unlabelled form fields in the advanced search module."
```

```
"Run a Section 508 gap assessment for our federal web portal. Flag all 
WCAG 2.0 AA criteria we likely fail based on these audit findings: 
missing alt text on charts, no skip navigation, session timeouts with 
no warning, and auto-playing video on the homepage."
```

```
"Draft Section 508 procurement language for an RFP for a new HR 
information system. Include FAR clause 52.239-2, VPAT requirements, 
testing methodology requirements, and remediation SLAs for critical, 
high, and medium accessibility findings."
```

```
"Walk me through the complete PDF accessibility checklist for a 50-page 
regulatory guidance document that needs to comply with Section 508. 
Include tag structure, reading order, form fields, images, and 
verification steps in Acrobat Pro."
```

```
"Our agency wants to claim an undue burden exception for a legacy 
financial system. Walk me through the determination process: what cost 
analysis is required, who must sign the determination, what alternative 
means of access we must provide, and how to document it for audit."
```

---

## 5. Skill Implementation Details

### Architecture

```
plugins/section-508/skills/section-508/
├── SKILL.md                        # Main skill: regulatory framework, who must comply,
│                                   # ICT coverage (E101–E103), exceptions (E202),
│                                   # all WCAG 2.0 POUR criteria tables (Level A and AA),
│                                   # common workflows (VPAT, audit, PDF, procurement,
│                                   # undue burden), response format routing
└── references/
    └── wcag-mapping.md             # Section 508 provision map; WCAG 2.0 A and AA
                                    # common failures with testing methods and fixes;
                                    # Functional Performance Criteria (Chapter 3);
                                    # assistive technology testing matrix;
                                    # PDF accessibility checklist; common VPAT
                                    # deficiencies; key legal references

Section 508 - Claude Skill/
├── Section-508-README.md           # This file
└── section-508.skill               # Standalone installable skill file
```

### What's in SKILL.md

- **YAML frontmatter** with skill name, description, and auto-trigger phrases
- **Response format routing table** — task type to output format mapping (VPAT/ACR, audit, gap assessment, remediation plan, procurement language, policy, general question)
- **Regulatory framework** — who must comply, the 2018 Revised Standards structure (WCAG 2.0 AA for E205/E204, functional performance, hardware, support documentation)
- **ICT coverage** — complete list of ICT types covered (web, software, documents, hardware, video/audio, telecoms, authoring tools, support docs)
- **Exceptions (E202)** — undue burden, fundamental alteration, national security systems, back-office equipment, legacy ICT
- **Full POUR criteria tables** — all WCAG 2.0 Level A and Level AA success criteria with criterion code, level, and requirement (Perceivable, Operable, Understandable, Robust)
- **Common workflows** — VPAT 2.x completion step-by-step, accessibility audit methodology, PDF accessibility requirements, procurement (FAR 52.239-2), undue burden documentation process
- **Reference file pointers** — instructions directing Claude to load `references/wcag-mapping.md` for deep content

### What's in the reference files

| File | Contents |
|------|----------|
| `references/wcag-mapping.md` | Section 508 provision map (E205.2/E205.3/E205.4/E204/Chapter 3/Chapter 4/Chapter 6 ↔ WCAG 2.0); WCAG 2.0 Level A common failures (1.1.1, 1.3.1, 2.1.1, 1.4.1, 4.1.2) with specific failure patterns, testing methods, and code-level fixes; WCAG 2.0 Level AA common failures (1.4.3, 1.4.4, 2.4.5, 2.4.7, 3.3.3, 3.3.4); Functional Performance Criteria (Chapter 3, 302.1–302.9); assistive technology testing matrix (JAWS, NVDA, VoiceOver macOS/iOS, TalkBack, Dragon, keyboard, high contrast, browser zoom, ZoomText); PDF accessibility checklist with verification methods and Acrobat Pro tools; common procurement VPAT deficiencies; key legal references (29 U.S.C. § 794d, 36 CFR Part 1194, FAR 39.2, FAR 52.239-2, OMB M-24-08) |

### Inputs used to build the skill

| Source | Description |
|--------|-------------|
| **29 U.S.C. § 794d** | Section 508 statutory authority and scope |
| **36 CFR Part 1194** | US Access Board Revised Section 508 Standards (effective January 18, 2018) — the authoritative technical standard |
| **WCAG 2.0 (W3C, December 2008)** | All 38 Level A and Level AA success criteria incorporated by reference under E205 |
| **VPAT 2.x WCAG Edition** | ITI VPAT template structure — Tables 1–3, Functional Performance Criteria, Software/Support Documentation chapters |
| **FAR Subpart 39.2 and clause 52.239-2** | Federal Acquisition Regulation Section 508 procurement requirements |
| **OMB Memorandum M-24-08 (January 2024)** | Updated federal agency Section 508 program management requirements |
| **Section508.gov guidance** | GSA testing resources, agency reporting, VPAT templates, accessibility maturity model |
| **ARIA Authoring Practices Guide (W3C)** | Keyboard patterns and ARIA requirements for custom widgets |
| **PDF/UA (ISO 14289)** | PDF accessibility standard referenced for electronic document requirements |
| **Assistive technology compatibility** | JAWS, NVDA, VoiceOver, TalkBack, Dragon NaturallySpeaking compatibility testing methodology |

### Skill trigger phrases

`Section 508` · `508 compliance` · `Revised Section 508 Standards` · `36 CFR Part 1194` · `VPAT` · `Accessibility Conformance Report` · `ACR` · `federal ICT accessibility` · `federal accessibility` · `WCAG 2.0 AA federal` · `508 audit` · `508 gap assessment` · `508 remediation` · `PDF accessibility` · `508 procurement` · `FAR 52.239-2` · `OMB M-24-08` · `undue burden` · `fundamental alteration exception` · `legacy ICT exception` · `assistive technology testing` · `JAWS NVDA VoiceOver federal` · `Section 508 testing` · `functional performance criteria` · `508 VPAT completion` · `federal web accessibility`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

---

*Skill version: 1.8.0 — August 2026*

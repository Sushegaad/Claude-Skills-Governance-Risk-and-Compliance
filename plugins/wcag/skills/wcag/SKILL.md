---
name: wcag
description: >
  Expert WCAG (Web Content Accessibility Guidelines) advisor covering WCAG 2.0,
  2.1, and 2.2 — the W3C international accessibility standards. Use this skill
  whenever a user asks about WCAG success criteria, conformance levels (A/AA/AAA),
  accessibility audits, POUR principles, accessibility statements, ARIA patterns,
  colour contrast, keyboard accessibility, screen reader compatibility, mobile
  accessibility, cognitive accessibility, WCAG 2.2 new criteria, WCAG 3.0 preview,
  legal requirements referencing WCAG (EN 301 549, EAA, ADA, Section 508), or
  mapping WCAG to accessibility laws. Trigger for any web or digital content
  accessibility question — even if the user doesn't say "skill" or "WCAG".
---

# Web Content Accessibility Guidelines (WCAG) Skill

> **Last verified:** 2026-10-03

You are an expert advisor on the **Web Content Accessibility Guidelines (WCAG)** — the W3C international standard for digital accessibility, developed by the Web Accessibility Initiative (WAI). You help developers, designers, product owners, and compliance teams understand, audit, and implement WCAG across web, mobile, and digital content.

WCAG is the technical foundation for accessibility laws worldwide: the EU Web Accessibility Directive, the European Accessibility Act (EN 301 549), the US Section 508, the UK Equality Act, Australia's DDA, and ADA Title III web cases all reference WCAG conformance.

---

## How to Respond

| Task | Output Format |
|------|--------------|
| Criterion explanation | Definition · Level (A/AA/AAA) · Why it matters · Common failures · Fix |
| Accessibility audit | Table: Criterion → Issue → Element/Location → Severity → Remediation |
| Conformance review | Summary: pass/fail per criterion, overall conformance level achieved |
| Gap assessment | Table: Criterion → Status (🔴/🟡/🟢) → Gap Notes → Priority |
| Accessibility statement | Structured document with conformance claim, known issues, contact |
| Code review | Annotated code with specific WCAG violations and corrected version |
| Legal mapping | Side-by-side: WCAG criterion → applicable law/standard |
| General question | Clear prose citing specific criterion numbers (e.g., SC 1.4.3) |

Always cite the **criterion number and name** (e.g., SC 2.4.7 Focus Visible) — never just the principle.

---

## WCAG Versions

| Version | Status | Key Additions |
|---------|--------|---------------|
| WCAG 2.0 (2008) | W3C Recommendation | Foundational 61 criteria across 12 guidelines and 4 principles |
| WCAG 2.1 (2018) | W3C Recommendation — current minimum | +17 criteria: mobile, low vision, cognitive accessibility |
| WCAG 2.2 (Oct 2023) | W3C Recommendation — latest | +9 new criteria (SC 2.4.11–13, 2.5.7–8, 3.2.6, 3.3.7–8); removes 4.1.1 |
| WCAG 3.0 | W3C Working Draft (updated **September 10, 2026**) — not normative; Recommendation not expected before ~2029 | Six cumulative conformance tiers (avoid physical harm → foundational access → conformance → Bronze → Silver → Gold); requirements split core/supplemental/assertions with impact labels (Physical harm, Risk, Barrier, Friction). WCAG 2.2 remains the conformance target (Aug 2026 errata editorial only) |

**Backwards compatibility:** WCAG 2.2 is fully backwards-compatible. A site conforming to WCAG 2.2 AA also conforms to 2.1 AA and 2.0 AA. **Most legal requirements today cite WCAG 2.1 AA; EN 301 549 (2021) references WCAG 2.1; the EAA compliance deadline of June 2025 uses EN 301 549 which maps to WCAG 2.1 AA.**

---

## The Four POUR Principles

### 1. Perceivable — Information must be presentable in ways users can perceive

| SC | Level | Requirement | Common Failures |
|----|-------|-------------|-----------------|
| 1.1.1 Non-text Content | A | Alt text for all images, icons, charts; empty alt for decorative | Missing alt; alt="image.png"; meaningful image alt="" |
| 1.2.1 Audio-only/Video-only | A | Transcript for audio; text alternative for silent video | No transcript for podcast; no description for infographic video |
| 1.2.2 Captions (Pre-recorded) | A | Synchronised captions for all pre-recorded video with audio | Auto-captions only; no captions for embedded YouTube |
| 1.2.3 Audio Description/Media Alt | A | Audio description or full text alternative for pre-recorded video | Video with on-screen actions not described in audio |
| 1.2.4 Captions (Live) | AA | Real-time captions for live video with audio | Live webinar or event with no live captions |
| 1.2.5 Audio Description (Pre-recorded) | AA | Audio description track for pre-recorded video | Tutorial video showing UI steps with no narration of what is shown |
| 1.3.1 Info and Relationships | A | Structure conveyed via markup (headings, labels, tables) | Styled divs as headings; unlabelled form fields; layout tables |
| 1.3.2 Meaningful Sequence | A | Reading order correct in DOM | CSS positioning creating visual order mismatched from DOM order |
| 1.3.3 Sensory Characteristics | A | Instructions not based solely on shape, colour, size, position | "Click the red button"; "see the box on the right" |
| 1.3.4 Orientation (2.1) | AA | Content not locked to a single orientation | Mobile page forces landscape; kiosk locked to portrait |
| 1.3.5 Identify Input Purpose (2.1) | AA | Autocomplete attributes on personal data fields | No autocomplete="name" or autocomplete="email" on personal data inputs |
| 1.4.1 Use of Colour | A | Colour not the only means of conveying information | Red/green status only; required fields by red colour alone |
| 1.4.2 Audio Control | A | Auto-playing audio can be stopped | Background music autoplays with no control |
| 1.4.3 Contrast (Minimum) | AA | Normal text: 4.5:1; large text: 3:1 | Grey text on white; light blue links on white |
| 1.4.4 Resize Text | AA | Text scalable to 200% without loss of content | Fixed-height containers clip text at 200% zoom |
| 1.4.5 Images of Text | AA | Text used rather than images of text | Button label is a PNG; styled quote is a JPG |
| 1.4.10 Reflow (2.1) | AA | Content reflowable at 320 CSS px width without horizontal scroll | Mobile layout breaks at 320px; content requires 2D scrolling |
| 1.4.11 Non-text Contrast (2.1) | AA | UI components and graphics: 3:1 contrast against adjacent colour | Light grey input border on white; low-contrast chart lines |
| 1.4.12 Text Spacing (2.1) | AA | No loss of content with specific text spacing overrides | Overflow hidden clips content when line-height: 2.5 applied |
| 1.4.13 Content on Hover or Focus (2.1) | AA | Hover/focus-triggered content: dismissable, hoverable, persistent | Tooltip disappears when cursor moves to it; not dismissable with Esc |

### 2. Operable — Interface components must be operable

| SC | Level | Requirement | Common Failures |
|----|-------|-------------|-----------------|
| 2.1.1 Keyboard | A | All functionality via keyboard; no keyboard trap | Mouse-only dropdowns; drag-and-drop with no keyboard alternative |
| 2.1.2 No Keyboard Trap | A | Focus can be moved away from any component | Modal with no close mechanism; widget trapping Tab permanently |
| 2.1.4 Character Key Shortcuts (2.1) | A | Single-character shortcuts can be turned off/remapped | Keyboard shortcut fires when user types in text field |
| 2.2.1 Timing Adjustable | A | Time limits adjustable, extendable, or removable | Session timeout with no warning or extension option |
| 2.2.2 Pause, Stop, Hide | A | Moving/blinking/scrolling content can be paused | Auto-rotating carousel with no pause button; parallax scrolling |
| 2.3.1 Three Flashes or Below | A | Nothing flashes more than 3 times/second | Animated GIF with fast flicker; strobe effect in video |
| 2.4.1 Bypass Blocks | A | Mechanism to skip repeated navigation | No skip link; no ARIA landmark navigation |
| 2.4.2 Page Titled | A | Pages have descriptive, unique titles | All pages titled "Home" or just the site name |
| 2.4.3 Focus Order | A | Focus order logical and meaningful | Tab order jumps around page; modal focus sent to wrong element |
| 2.4.4 Link Purpose (In Context) | A | Link purpose determinable from link text or context | "Click here", "Read more" with no accessible context |
| 2.4.5 Multiple Ways | AA | Multiple ways to locate pages | Site with only one navigation method and no search |
| 2.4.6 Headings and Labels | AA | Headings and labels are descriptive | Heading text "Section 1"; form label "Field 1" |
| 2.4.7 Focus Visible | AA | Keyboard focus indicator visible | CSS outline:none with no replacement; invisible focus on dark bg |
| 2.4.11 Focus Not Obscured (Minimum) (2.2) | AA | Focused element not entirely hidden by sticky header/footer | Sticky nav covers the focused element |
| 2.4.12 Focus Not Obscured (Enhanced) (2.2) | AAA | Focused element fully visible | Partially covered focused element |
| 2.4.13 Focus Appearance (2.2) | AAA | Focus indicator meets size and contrast requirements | Thin 1px focus ring with insufficient contrast |
| 2.5.1 Pointer Gestures (2.1) | A | Multipoint/path gestures have single-pointer alternative | Pinch-only zoom; swipe-only carousel navigation |
| 2.5.2 Pointer Cancellation (2.1) | A | Mousedown-triggered actions can be aborted | Button action fires on mousedown not mouseup |
| 2.5.3 Label in Name (2.1) | A | Accessible name contains visible label text | Button visually says "Submit" but aria-label="Send form" |
| 2.5.4 Motion Actuation (2.1) | A | Device motion alternatives exist; can be disabled | Shake-to-undo with no alternative; tilt navigation only |
| 2.5.7 Dragging Movements (2.2) | AA | Dragging operations have single-pointer alternative | Sortable list drag-only; slider with drag-only interaction |
| 2.5.8 Target Size (Minimum) (2.2) | AA | Target size ≥ 24×24 CSS px (or spacing compensates) | Icon buttons smaller than 24px with no adequate spacing |

### 3. Understandable — Content and operation must be understandable

| SC | Level | Requirement | Common Failures |
|----|-------|-------------|-----------------|
| 3.1.1 Language of Page | A | Default human language programmatically determined | Missing `lang` attribute on `<html>`; `lang=""` |
| 3.1.2 Language of Parts | AA | Language of passages identified | French quote on English page with no `lang="fr"` |
| 3.2.1 On Focus | A | No context change when component receives focus | New window opens when element receives focus |
| 3.2.2 On Input | A | No unexpected context change when user inputs data | Form submits automatically when option selected |
| 3.2.3 Consistent Navigation | AA | Navigation consistent across pages | Navigation order changes between pages |
| 3.2.4 Consistent Identification | AA | Components with same function identified consistently | Search button labelled "Search" on one page, "Go" on another |
| 3.2.6 Consistent Help (2.2) | A | Help mechanisms in consistent location | Live chat and help link appear in different positions across pages |
| 3.3.1 Error Identification | A | Input errors identified and described | "Invalid input" with no description; visual-only error indicator |
| 3.3.2 Labels or Instructions | A | Labels or instructions for user input | Unlabelled form fields; no format hint for date (DD/MM/YYYY) |
| 3.3.3 Error Suggestion | AA | Correction suggestions provided | Error message says "wrong" without explaining correct format |
| 3.3.4 Error Prevention (Legal, Financial, Data) | AA | Legal/financial submissions: reversible, checked, or confirmable | One-click irreversible purchase with no confirmation step |
| 3.3.7 Redundant Entry (2.2) | A | Information already entered not re-requested in same session | Billing address required again on confirmation page |
| 3.3.8 Accessible Authentication (Minimum) (2.2) | AA | Cognitive function test not required for login unless alternatives exist | CAPTCHA with no alternative; memory puzzle required to log in |

### 4. Robust — Content must be interpreted by assistive technologies

| SC | Level | Requirement | Common Failures |
|----|-------|-------------|-----------------|
| 4.1.1 Parsing | A (removed in WCAG 2.2) | Valid markup (duplicate IDs, unclosed tags) | Still relevant for 2.0/2.1; duplicate IDs break AT |
| 4.1.2 Name, Role, Value | A | UI components have name, role, state/value | Custom widgets with no ARIA; toggle buttons missing aria-pressed |
| 4.1.3 Status Messages (2.1) | AA | Status messages programmatically determinable without focus | "Item added to cart" with no ARIA live region announcement |

---

## WCAG Conformance Levels

| Level | Description | Legal relevance |
|-------|-------------|-----------------|
| **A** | Minimum — removes most critical barriers | Rarely sufficient alone for legal compliance |
| **AA** | Standard — the universal legal benchmark; removes significant barriers | Required by: Section 508, EU EAA/EN 301 549, UK GDS, ADA case law, AODA |
| **AAA** | Enhanced — removes remaining barriers for specific user groups | Not required as a blanket policy (WCAG itself notes full conformance may not be achievable for all content) |

**Conformance claim:** To claim WCAG X.X Level AA conformance, a web page must satisfy **all Level A and Level AA success criteria** with no exceptions (or document exceptions explicitly in an accessibility statement).

---

## Common Workflows

### Full Accessibility Audit (WCAG 2.1 AA)
1. **Automated scan** — axe-core, Lighthouse, WAVE, or IBM Equal Access Checker. Catches ~30–40% of issues.
2. **Keyboard-only test** — Tab / Shift-Tab / Enter / Space / Arrow keys through all interactive elements. Tests SC 2.1.1, 2.1.2, 2.4.3, 2.4.7.
3. **Screen reader test** — NVDA + Chrome; JAWS + Chrome; VoiceOver + Safari (macOS); VoiceOver + Safari (iOS); TalkBack + Chrome (Android). Tests SC 1.1.1, 1.3.1, 4.1.2, and all informational criteria.
4. **Colour contrast** — Colour Contrast Analyser or browser DevTools. Tests SC 1.4.3, 1.4.11.
5. **Zoom/reflow** — Browser zoom to 400%; viewport at 320 CSS px. Tests SC 1.4.4, 1.4.10.
6. **Cognitive review** — Consistent navigation, clear labels, error messages, no complex CAPTCHA. Tests SC 3.x criteria.
7. **Document issues** — Per criterion, with element reference, severity, and remediation.

### Accessibility Statement
A WCAG-conformant accessibility statement should include:
- The specific WCAG version and level claimed (e.g., "WCAG 2.1 Level AA")
- Scope: which pages or products the claim covers
- Known non-conformances: list each SC not met with an explanation
- Alternatives available: e.g., accessible PDF version, phone support
- Date of last assessment and assessment methodology
- Contact for feedback and accessibility requests
- Formal complaints procedure (required under EU Web Accessibility Directive)

### ARIA Usage Principles
ARIA (Accessible Rich Internet Applications) adds semantics when HTML alone is insufficient. Key rules:
1. **No ARIA is better than bad ARIA** — incorrect ARIA is worse than no ARIA
2. **First rule of ARIA:** Use native HTML elements before adding ARIA roles
3. Required attributes: every `role` has required properties — e.g., `role="checkbox"` requires `aria-checked`
4. Interactive widgets must follow the **ARIA Authoring Practices Guide (APG)** keyboard patterns
5. Use `aria-live` regions for dynamic content (status messages, loading states, errors)

### Contrast Ratio Calculation
- **Normal text (< 18pt regular or < 14pt bold):** minimum 4.5:1
- **Large text (≥ 18pt regular or ≥ 14pt bold):** minimum 3:1
- **UI components and graphics** (SC 1.4.11): minimum 3:1
- **Enhanced (AAA):** normal text 7:1; large text 4.5:1
- Formula: (L1 + 0.05) / (L2 + 0.05) where L1 is the lighter and L2 the darker relative luminance

---

## Global Legal Framework Mapping

| Law / Standard | Jurisdiction | WCAG Requirement |
|----------------|-------------|-----------------|
| EN 301 549 (2021) | EU/EEA | WCAG 2.1 Level AA (Chapters 9–11) |
| European Accessibility Act (EAA) — Directive 2019/882 | EU | EN 301 549 → WCAG 2.1 AA; private sector deadline: June 28, 2025 |
| EU Web Accessibility Directive — 2016/2102 | EU public sector | WCAG 2.1 AA; in force since 2018–2020 |
| Section 508 (Revised 2018) | US federal sector | WCAG 2.0 AA (E205) |
| ADA Title III (case law) | US private sector | Courts increasingly apply WCAG 2.1 AA as the benchmark |
| UK Public Sector Accessibility Regulations 2018 | UK public sector | WCAG 2.1 AA |
| Equality Act 2010 | UK private sector | Reasonable adjustments — WCAG 2.1 AA widely used |
| AODA (WCAG Standard 2.0) | Ontario, Canada | WCAG 2.0 Level AA (large organisations since 2021) |
| DDA / Disability Discrimination Act | Australia | WCAG 2.1 AA (AHRC guidance) |

---

## Reference Files

For deeper content, read as needed:
- **references/criteria-detail.md** — Full WCAG 2.2 success criteria with techniques, sufficient techniques, advisory techniques, and failure techniques for each AA criterion

---

> *This skill provides general compliance information, not legal advice. Verify current requirements against official sources; consult qualified counsel or an accredited assessor for decisions.*

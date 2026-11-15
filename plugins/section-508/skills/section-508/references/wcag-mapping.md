# Section 508 / WCAG 2.0 AA - Detailed Reference

## Section 508 Provision Map

| 508 Provision | Scope | WCAG Equivalent |
|---------------|-------|-----------------|
| E205.2 | Public facing content | WCAG 2.0 Level A and AA (via E205.4) |
| E205.3 | Agency official communication (non-public-facing communications of specified types) | WCAG 2.0 Level A and AA (via E205.4) |
| E205.4 | Accessibility Standard for electronic content | Incorporates WCAG 2.0 Level A and AA |
| E204 | Functional Performance Criteria | Chapter 3, provisions 302.1–302.9 |
| E207 + 503 (Chapter 5) | Software (user interface) | WCAG 2.0 Level A and AA |
| 504 (Chapter 5) | Authoring tools | 504.2: content creation/editing conforming to WCAG 2.0 Level A and AA |
| Chapter 4 | Hardware | Physical ICT accessible controls, display, clearance |
| Chapter 6 | Support docs and services | Documentation and help in accessible formats |

---

## WCAG 2.0 Level A Success Criteria - Common Failures

### 1.1.1 Non-text Content
- **Failure:** `<img>` missing `alt` attribute, or `alt=""` on informative image
- **Failure:** Icon buttons with no accessible name (`aria-label` or `aria-labelledby`)
- **Failure:** Charts and graphs with no text alternative describing data
- **Testing:** Automated (axe, WAVE) + manual screen reader review
- **Fix:** Add meaningful `alt` text; use `alt=""` only for decorative images; use `aria-label` on icon-only buttons

### 1.3.1 Info and Relationships
- **Failure:** Visual headings not marked up with `<h1>`–`<h6>` (styled `<div>` or `<span>` used instead)
- **Failure:** Data tables with no `<th>` or `scope` attributes
- **Failure:** Form fields with visual label not programmatically associated (missing `<label for="">` or `aria-labelledby`)
- **Failure:** Required fields indicated only by colour or asterisk with no screen-reader-accessible text
- **Testing:** DOM inspection, NVDA/JAWS, automated (partial)
- **Fix:** Semantic HTML first; `aria-*` attributes only when semantic HTML insufficient

### 2.1.1 Keyboard
- **Failure:** Custom dropdowns, date pickers, modal dialogs not operable by keyboard
- **Failure:** Mouse-only event handlers (`onclick` on non-interactive elements, `mouseover` without `focus` equivalent)
- **Failure:** Drag-and-drop with no keyboard alternative
- **Failure:** Keyboard trap in modal - Tab cycles only within modal but no way to close it
- **Testing:** Tab through entire page; activate all controls; open/close modals
- **Fix:** Use native HTML controls where possible; for custom widgets, implement ARIA keyboard patterns (ARIA Authoring Practices Guide)

### 1.4.1 Use of Colour
- **Failure:** Form validation errors shown only by red border with no text or icon
- **Failure:** Required field indicator is colour-only (red asterisk with no "required" text)
- **Failure:** Link text colour is the only differentiator from surrounding body text (no underline or other visual cue)

### 4.1.2 Name, Role, Value
- **Failure:** Custom checkboxes/radio buttons styled with CSS, no ARIA role or checked state
- **Failure:** Tab panels with no `role="tab"`, `role="tablist"`, `aria-selected`
- **Failure:** Toggle buttons with no `aria-pressed` attribute
- **Failure:** Expanded/collapsed accordions with no `aria-expanded`
- **Testing:** Inspect ARIA properties in browser accessibility tree; test with NVDA/JAWS
- **Fix:** Follow WAI-ARIA Authoring Practices Guide patterns for each widget type

---

## WCAG 2.0 Level AA Success Criteria - Common Failures

### 1.4.3 Contrast (Minimum)
- Normal text (< 18pt or < 14pt bold): **4.5:1** minimum contrast ratio against background
- Large text (≥ 18pt or ≥ 14pt bold): **3:1** minimum
- **Failure:** Light grey text on white background lighter than #767676 (e.g., #777777 on #FFFFFF = 4.48:1 - fails AA); #767676 on #FFFFFF = 4.54:1 passes AA and is the canonical lightest passing grey
- **Failure:** Placeholder text in input fields (often fails; placeholder is not a label substitute)
- **Exception:** Text in logos, inactive UI components, decorative text
- **Tool:** WebAIM Contrast Checker, Colour Contrast Analyser (desktop app), browser DevTools

### 1.4.4 Resize Text
- **Failure:** Text rendered in `px` units inside CSS `@media` queries that prevent browser zoom from scaling text
- **Failure:** Fixed-height containers that clip text when zoomed to 200%
- **Fix:** Use relative units (`rem`, `em`) for font sizes and container heights; test at 200% browser zoom

### 2.4.5 Multiple Ways
- **Requirement:** Provide at least two ways to find content: search + navigation, OR sitemap + navigation
- **Exception:** Pages that are the result of a process (e.g., checkout confirmation page) are excluded

### 2.4.7 Focus Visible
- **Failure:** CSS `outline: none` or `outline: 0` removing the default focus ring with no replacement
- **Failure:** Focus ring present but invisible against background colour
- **Fix:** Never remove focus styling without replacing it; use `focus-visible` CSS pseudo-class

### 3.3.3 Error Suggestion
- **Failure:** Form validation says "invalid input" without specifying what is wrong or how to fix it
- **Fix:** "Please enter a date in MM/DD/YYYY format" - specific, actionable suggestion

### 3.3.4 Error Prevention
- **Requirement:** For legal, financial, or data deletion transactions: provide a review-and-confirm step, OR allow the submission to be reversed/cancelled

---

## Functional Performance Criteria (Chapter 3) - Section 508

| Criterion | Requirement |
|-----------|-------------|
| 302.1 Without Vision | At least one mode operable without vision (screen reader support) |
| 302.2 With Limited Vision | At least one mode with features that accommodate limited vision (zoom, high contrast) |
| 302.3 Without Perception of Colour | Colour not the only means to convey information |
| 302.4 Without Hearing | At least one mode operable without hearing (captions, transcripts, visual alerts) |
| 302.5 With Limited Hearing | At least one mode with features for limited hearing (volume control, captioning) |
| 302.6 Without Speech | At least one mode operable without speech |
| 302.7 With Limited Manipulation | At least one mode operable without fine motor control (no simultaneous key presses, no timed actions) |
| 302.8 With Limited Reach and Strength | At least one mode for limited reach (reachable controls) |
| 302.9 With Limited Language, Cognitive, and Learning | At least one mode that accommodates limited cognitive ability |

---

## Assistive Technology Testing Matrix

| AT + Browser | Primary Use Case | Notes |
|--------------|-----------------|-------|
| JAWS + Chrome | Federal agency standard; most common screen reader in US gov | Test all interactive widgets, form flows, dynamic content (ARIA live regions) |
| NVDA + Chrome or Firefox | Open-source; widely used for testing; required for VPAT testing | Free; good for broad coverage |
| VoiceOver + Safari (macOS) | Mac users; required if product targets Mac/iOS | Keyboard shortcut: Cmd+F5 |
| VoiceOver + Safari (iOS) | Mobile web and native iOS apps | Swipe navigation; activate with triple-click Home/Side button |
| TalkBack + Chrome (Android) | Android web and native apps | Swipe navigation; activate in Accessibility settings |
| Dragon NaturallySpeaking | Voice control users | Test all link text and button labels are speakable |
| Keyboard only | Most impactful test; catches most 2.1.x failures | Tab, Shift-Tab, Enter, Space, Arrow keys |
| High Contrast Mode (Windows) | OS-level contrast override | Ensure no information lost; images must not disappear |
| Browser Zoom 200% | SC 1.4.4 | Check for horizontal scroll, content overlap, clipped text |
| ZoomText / Magnifier | Low-vision users | Test with 4x magnification |

---

## PDF Accessibility Checklist

| Requirement | How to Verify | Tool |
|-------------|---------------|------|
| Document is tagged | File → Properties → Description tab: "Tagged PDF: Yes" | Acrobat Pro |
| Tag tree structure correct | Accessibility → Reading Order; Tags panel | Acrobat Pro |
| Reading order = visual order | View → Read Out Loud; or Articles panel | Acrobat Pro |
| Images have Alt text | Right-click image tag → Properties → Alternate Text | Acrobat Pro |
| Form fields have Tooltip/name | Open Form Editor; check Tooltip field for each control | Acrobat Pro |
| Table tags with TH/Scope | Tags panel; Table Inspector | Acrobat Pro |
| Document language set | File → Properties → Advanced → Reading Options | Acrobat Pro |
| Document title set | File → Properties → Description → Title | Acrobat Pro |
| No flicker/motion (if any) | Review any embedded multimedia | Manual |
| Passes automated check | Accessibility → Full Check → Run | Acrobat Pro |

---

## Common Procurement Deficiencies in VPATs

1. **Outdated template** - using VPAT 1.x instead of VPAT 2.x (WCAG Edition). Reject and require resubmission.
2. **"Supports" without evidence** - vendor claims support with no remarks. Require explanation for each "Supports" claim.
3. **"Not Applicable" overuse** - vendor marks criteria N/A without justification. Challenge: almost no product has 100% N/A for interactive criteria.
4. **Missing functional performance criteria** - vendors skip Chapter 3 entirely. Required for all ICT.
5. **No testing methodology disclosed** - VPAT must state how testing was conducted (automated tools, AT + browser combinations, dates).
6. **Version mismatch** - VPAT covers version 1.0 but agency is procuring version 2.0. Require VPAT for the exact version being procured.

---

## Key Legal References

- **29 U.S.C. § 794d** - Section 508 statutory text
- **36 CFR Part 1194** - Access Board's Revised Section 508 Standards (effective 18 January 2018)
- **FAR Subpart 39.2** - Federal Acquisition Regulation provisions on Section 508
- **FAR Subpart 39.2 / 11.002(f)**: Section 508 applies through acquisition planning and requirements documents; there is no governmentwide FAR 508 clause, only agency supplement clauses (for example HHS 352.239-74, DOT 1252.239-93)
- **OMB Memorandum M-24-08** - "Strengthening Digital Accessibility and the Management of Section 508 of the Rehabilitation Act" (December 21, 2023)
- **Section508.gov** - GSA's official guidance, VPAT templates, testing resources
- **WCAG 2.0** - W3C Recommendation (11 December 2008) - the incorporated technical standard
- **WCAG 2.1** - W3C Recommendation (5 June 2018) - supersedes 2.0; additional mobile/cognitive criteria (not yet mandated by 508 but recommended)

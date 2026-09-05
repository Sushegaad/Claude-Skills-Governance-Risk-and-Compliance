# Digital Operational Resilience Act (DORA) Skill for Claude

> **Disclaimer:** This skill provides informational guidance on DORA obligations based on Regulation (EU) 2022/2554 and adopted RTS/ITS issued by EBA, ESMA, and EIOPA. It does not constitute legal advice. DORA compliance involves significant obligations under EU financial services law — for matters involving competent authority interaction, major incident reporting, TLPT scoping, or Register of Information submission, consult a qualified DORA compliance professional or your legal counsel.

---

## 1. What Does the Skill Do?

This skill turns Claude into an expert **DORA compliance advisor** for EU financial entities and their ICT third-party service providers. It covers the full text of **Regulation (EU) 2022/2554** — the Digital Operational Resilience Act — which has applied since **17 January 2025**, along with all adopted **Regulatory Technical Standards (RTS)** and **Implementing Technical Standards (ITS)** issued by EBA, ESMA, and EIOPA (the European Supervisory Authorities).

DORA is structured across 9 chapters covering five substantive compliance areas: the **ICT risk management framework** (Chapter II, Art. 5–16), **ICT-related incident management, classification, and reporting** (Chapter III, Art. 17–23), **digital operational resilience testing** (Chapter IV, Art. 24–27), **ICT third-party risk management** (Chapter V, Art. 28–44), and **information-sharing arrangements** (Chapter VI, Art. 45). The skill provides article-level guidance across all chapters, with particular depth in the areas where compliance gaps are most commonly found.

A defining feature of this skill is its precision in distinguishing between DORA's chapters, frameworks, and the specific adopted RTS/ITS that implement each obligation. The skill always cites the correct Commission Delegated/Implementing Regulation number (for example, CDR (EU) 2024/1774 for the ICT risk management RTS, CDR (EU) 2024/1772 for the incident classification criteria, and CIR (EU) 2024/2956 for the Register of Information template). It explicitly avoids the two most common DORA compliance errors: conflating DORA with NIS2 (DORA is lex specialis for the financial sector; NIS2 applies where DORA does not) and citing the pre-DORA EBA ICT/security Risk guidelines as current standards (those guidelines were superseded by DORA on 17 January 2025).

The skill is particularly comprehensive on **ICT third-party risk management** — the most complex DORA chapter — covering the ICT third-party risk policy, the Register of Information (with all mandatory fields per CIR (EU) 2024/2956), contractual provisions for critical and important ICT arrangements (Art. 30(2) checklist), ICT concentration risk assessment, exit strategy planning, and the oversight framework for Critical ICT Third-Party Service Providers (CTPPs) designated by the ESAs.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|----------------------|
| **Chief Risk Officers (CROs)** | ICT risk framework design, board governance obligations (Art. 5), ICT risk appetite setting |
| **CISOs and IT security teams** | ICT risk management framework (Art. 6–14), protection controls, detection, BCP/BIA |
| **Compliance managers** | Gap assessment across all 5 DORA pillars, evidence mapping, competent authority readiness |
| **Incident response teams** | Art. 17–19 incident classification, major incident determination, 3-stage reporting timelines |
| **Vendor/third-party risk teams** | Register of Information build-out, Art. 30 contract reviews, concentration risk assessment |
| **Legal and contracts teams** | Art. 30(2) contractual provision checklists, subcontracting RTS, exit clause drafting |
| **Boards and management bodies** | Art. 5 board obligations, ICT risk appetite, budget and training accountability |
| **ICT service providers (cloud, SaaS)** | Understanding CTPP designation criteria, oversight obligations, audit and access rights |
| **Penetration testers and TLPT providers** | Art. 26 TLPT scope, CDR (EU) 2025/1190 requirements, threat intelligence phase |
| **Smaller financial entities** | Simplified ICT risk management framework (Art. 16) eligibility and obligations |

---

## 3. Common Use Cases

### Gap Analysis and Readiness Assessment
- *"Run a DORA gap analysis for a mid-size payment institution. We have an IT risk framework but no formal ICT RMF per Art. 6."*
- *"Assess our compliance with Chapter II (ICT risk management) and Chapter V (third-party risk)."*
- *"What are the most commonly missed DORA obligations for banks with pre-existing ICT governance frameworks?"*
- *"We applied Art. 16 simplified framework — are we eligible, and what does that framework require?"*

### ICT Risk Management Framework (Chapter II)
- *"Draft an ICT risk management framework policy that satisfies Art. 6 and CDR (EU) 2024/1774."*
- *"What does Art. 5 require from our board? Draft the board-level ICT risk accountability statement."*
- *"What must our ICT asset register include per Art. 8? How should we map assets to critical functions?"*
- *"Design our patch management process to satisfy Art. 7(d)."*
- *"What does Art. 11 require for ICT business continuity? How do we set RTO and RPO for critical functions?"*

### Incident Classification and Reporting (Chapter III)
- *"We had a system outage lasting 6 hours affecting 3,000 payment transactions. Is this a major ICT incident under DORA?"*
- *"Walk me through the 3-stage major ICT incident reporting timeline under Art. 19."*
- *"What content is required in the initial notification (4-hour) report to our competent authority?"*
- *"Draft our ICT incident classification matrix using the Art. 18 criteria and CDR (EU) 2024/1772 thresholds."*
- *"We had a significant cyber threat but no actual incident. Can we submit a voluntary report under Art. 19(2)?"*

### Resilience Testing (Chapter IV)
- *"What testing does Art. 24 require from all financial entities annually?"*
- *"Does our organization meet the TLPT threshold under Art. 26(8)? We're a large investment firm."*
- *"Walk me through the TLPT process under Art. 26 and CDR (EU) 2025/1190."*
- *"What qualifications must our external TLPT tester hold under Art. 27?"*

### ICT Third-Party Risk (Chapter V)
- *"We have 45 ICT service arrangements. How do we build our Register of Information per CIR (EU) 2024/2956?"*
- *"Review our contract with AWS for DORA Art. 30(2) compliance. Which provisions are missing?"*
- *"What is ICT concentration risk under Art. 28(6), and how do we assess it?"*
- *"Draft an exit strategy for our critical cloud infrastructure provider."*
- *"Which of our ICT service arrangements require full Art. 30(2) provisions vs. the lighter Art. 30(3) set?"*

---

## 4. How to Use the Skill

### Installation
1. Download the `dora.skill` file from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `dora.skill`
4. The skill is immediately active in your Claude sessions

### Triggering the Skill
The skill activates automatically when your message relates to DORA or its implementing standards. Example phrases that trigger it:

- *"DORA compliance"*
- *"DORA gap analysis"*
- *"ICT risk management framework DORA"*
- *"Art. 17 incident reporting"*
- *"Register of Information DORA"*
- *"DORA third-party risk"*
- *"TLPT financial entity"*
- *"DORA contractual provisions"*
- *"digital operational resilience"*
- *"DORA vs NIS2"*
- *"critical ICT third-party service provider"*

### Example Prompts

```
"Run a full DORA gap analysis for a mid-size EU investment firm. We have 
existing ISO 27001 certification, a basic incident response process, and 
a vendor management policy. We do not have a formal DORA ICT risk 
management framework, no Register of Information, and our cloud contracts 
predate DORA. Produce a gap table across all four substantive DORA pillars."
```

```
"We experienced a ransomware incident that encrypted our trading system 
for 8 hours, affecting approximately €2.3M in delayed transactions and 
15,000 client accounts. Walk me through: (1) whether this is a major ICT 
incident under Art. 18, (2) the reporting timeline, and (3) what content 
the initial 4-hour notification must contain."
```

```
"We have 60 ICT service arrangements including AWS (critical), Microsoft 
365, Bloomberg Terminal, and 57 other SaaS vendors. Build us a Register 
of Information structure per CIR (EU) 2024/2956 and identify which 
arrangements require full Art. 30(2) contractual provisions."
```

```
"Review the following ICT service contract with our cloud provider against 
DORA Art. 30(2)(a)–(i) requirements. Identify missing provisions and draft 
the replacement clauses needed for compliance."
```

```
"We are a large payment institution. Do we meet the TLPT threshold under 
Art. 26(8)? If yes, walk us through the complete TLPT process from scope 
definition through competent authority notification and attestation."
```

---

## 5. Skill Implementation Details

### Architecture

```
dora/
├── SKILL.md                          # Core skill — 9-chapter DORA structure, in-scope
│                                     #   entities, Art. 5–16 (ICT RMF), Art. 17–23
│                                     #   (incident management), Art. 24–27 (testing),
│                                     #   Art. 28–44 (third-party risk), gap analysis
│                                     #   workflows, Register of Information, TLPT process,
│                                     #   common DORA errors
└── references/
    ├── rts-its-guide.md              # All 12 adopted RTS/ITS: regulation number, article
    │                                 #   mapping, application date, and key requirements
    ├── article-reference.md          # All 64 DORA articles with obligation summaries
    │                                 #   and key sub-paragraph citations
    ├── third-party-risk.md           # Deep-dive: Art. 28–44, Register of Information
    │                                 #   mandatory fields, Art. 30 contractual provisions,
    │                                 #   ICT concentration risk, exit strategies, CTPP oversight
    └── incident-classification.md    # Art. 17–23 incident management process, CDR 2024/1772
                                      #   classification criteria, 3-stage reporting timelines,
                                      #   templates, and voluntary reporting provisions
```

**Total:** ~1,650 lines across 5 files (SKILL.md + 4 reference files)

### What's in SKILL.md

- **Six foundational rules** — preventing the most common DORA advisory errors (NIS2 conflation, legacy EBA guidelines, chapter naming, article-level citation, Chapter II vs. III distinction, correct RTS/ITS citation)
- **Response format routing** — 9 task types mapped to specific output formats
- **DORA structure at a glance** — chapter-by-chapter table (Art. 1–64) with topic summary
- **In-scope financial entities (Art. 2)** — 10+ entity types; proportionality and simplified framework eligibility (Art. 4, Art. 16)
- **Chapter II (Art. 5–16)** — article-by-article: governance, ICT RMF, systems/tools, identification, protection, detection, response/recovery, backup, learning, communication, simplified framework
- **Chapter III (Art. 17–23)** — incident management process, classification criteria, 3-stage reporting timeline table, payment-related incidents
- **Chapter IV (Art. 24–27)** — annual testing programme, TLPT threshold criteria, TLPT process, tester qualifications, TIBER-EU alignment
- **Chapter V (Art. 28–44)** — ICT third-party risk policy, Register of Information, concentration risk, exit strategy, Art. 30(2) provisions checklist, CTPP oversight framework, Lead Overseer powers
- **Chapter VI (Art. 45)** — voluntary information-sharing arrangements
- **4-phase gap analysis framework** — across governance, incident management, testing, and third-party risk
- **Register of Information mandatory fields** — per CIR (EU) 2024/2956
- **TLPT process** — 7-step end-to-end process
- **Common DORA compliance errors** — 7 errors with correct approaches

### What's in the reference files

| File | Contents |
|------|----------|
| `rts-its-guide.md` | All 12 adopted Commission Delegated/Implementing Regulations: CDR (EU) 2024/1502 (CTPP criteria), CDR (EU) 2024/1773 (third-party risk policy), CDR (EU) 2024/1774 (ICT RMF), CDR (EU) 2024/1772 (incident classification), CIR (EU) 2024/2956 (Register of Information), CDR (EU) 2025/301 (incident reporting), CIR (EU) 2025/302 (reporting templates), CDR (EU) 2025/1190 (TLPT), CDR (EU) 2025/532 (subcontracting), CDR (EU) 2025/420 (JETs), CDR (EU) 2025/295 (oversight harmonization), CDR (EU) 2024/1505 (oversight fees) |
| `article-reference.md` | All 64 DORA articles: short obligation summary, key sub-paragraphs, and applicable RTS/ITS reference for each article |
| `third-party-risk.md` | Art. 28–44 deep dive: full Register of Information mandatory field set; Art. 30(2)(a)–(i) contractual provisions with explanatory notes; ICT concentration risk assessment methodology; exit strategy planning requirements; CTPP designation criteria and Lead Overseer oversight process |
| `incident-classification.md` | Art. 17–23 incident management: classification criteria per CDR (EU) 2024/1772 with materiality thresholds; decision flowchart for major incident determination; 3-stage reporting timeline with content requirements per stage; voluntary significant cyber threat reporting; payment incident rules (Art. 23) |

### Inputs used to build the skill

| Input | Description |
|-------|-------------|
| **Regulation (EU) 2022/2554** | Full DORA text — all 64 articles and 9 chapters; published OJ L 333, 27 December 2022 |
| **12 adopted RTS/ITS (CDR/CIR)** | All Commission Delegated and Implementing Regulations adopted by EBA, ESMA, EIOPA (see rts-its-guide.md for full list) |
| **EBA, ESMA, EIOPA guidance** | ESA Q&A, consultation papers, and final opinions on DORA implementation |
| **NIS2 Directive (EU) 2022/2555** | Referenced for Art. 4(2) DORA lex specialis clarification |
| **TIBER-EU framework** | Referenced for TLPT alignment (Art. 26) |
| **Pre-DORA EBA Guidelines (EBA/GL/2019/04)** | Referenced only to flag that these are superseded for in-scope entities since 17 January 2025 |

### Skill trigger phrases

`DORA`, `Digital Operational Resilience Act`, `Regulation (EU) 2022/2554`, `DORA compliance`, `DORA gap analysis`, `ICT risk management framework`, `ICT RMF DORA`, `Art. 6 DORA`, `Art. 17 DORA`, `Art. 19 DORA`, `Art. 26 DORA`, `Art. 28 DORA`, `Art. 30 DORA`, `TLPT`, `threat-led penetration testing`, `Register of Information`, `major ICT incident`, `ICT incident reporting`, `ICT third-party risk`, `critical ICT third-party`, `CTPP`, `DORA third-party policy`, `ICT concentration risk`, `DORA contractual provisions`, `DORA simplified framework`, `digital operational resilience testing`, `DORA vs NIS2`, `EBA DORA`, `ESMA DORA`, `EIOPA DORA`, `financial entity ICT`, `DORA RTS`, `DORA ITS`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.9.0 — September 2026

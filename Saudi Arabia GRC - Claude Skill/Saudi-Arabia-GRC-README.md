# Saudi Arabia GRC — Claude Skill

**File:** `saudi-arabia-grc.skill`

Turns Claude into a **Saudi Arabia governance, risk & compliance advisor** — a compliance router that first determines which Saudi regulations apply, then guides framework-specific compliance. Saudi compliance is fragmented across NCA (cybersecurity), SDAIA (personal data), SAMA (financial sector), and CST (telecom/cloud); this skill establishes organization type, sector, data, and cloud posture before advising.

## What it covers
- **NCA ECC-2:2024** — 4 domains / 28 subdomains / 108 controls; mandatory for government entities and CNI operators
- **Saudi PDPL** (Royal Decree M/19 as amended M/148) — fully enforced since September 14, 2024: SDAIA registration, 72-hour breach notification, SCC modules for transfers, active enforcement (~48 first-wave decisions)
- **NCA Cloud Cybersecurity Controls (CCC)** + **CST Cloud Computing Regulatory Framework** — CSP/tenant role-split controls, CSP registration classes, Level 3–4 and government data residency
- **SAMA Cyber Security Framework** — 4 domains, maturity levels 0–5 (minimum level 3), for banks/insurers/fintechs
- **Router coverage** of DCC, OTCC, TCC, CSCC, and CMA guidelines

## What it does
Applicability matrices before detail · per-framework gap assessments with evidence columns · PDPL breach response and transfer mechanics · market-entry roadmaps · cross-mapping to ISO 27001:2022, NIST CSF 2.0, and SOC 2.

**Trigger phrases:** `Saudi Arabia compliance`, `KSA`, `NCA ECC`, `SDAIA`, `Saudi PDPL`, `SAMA CSF`, `CST cloud`, `Saudi data residency`, `expanding to Saudi Arabia`, `نظام حماية البيانات الشخصية`

---
Skill version: 1.9.0 — September 2026

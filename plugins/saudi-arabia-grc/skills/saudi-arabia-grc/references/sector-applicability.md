# Saudi Regulator & Framework Map (router reference)

| Regulator | Instruments | Who / When |
|---|---|---|
| **NCA** (National Cybersecurity Authority) | ECC-2:2024; CCC (cloud); DCC-1:2022 (data); OTCC-1:2022 (OT/ICS); TCC-1:2021 (telework); CSCC-1:2019 (critical systems) | Government entities + subsidiaries and CNI operators (mandatory); recommended for others |
| **SDAIA** | PDPL + Implementing & Transfer Regulations; National Data Governance Platform; NDMO data-governance rules | Anyone processing Saudi residents' personal data |
| **SAMA** | Cyber Security Framework; IT Governance Framework; BCM Framework; CTI Principles | Banks, insurers, financing companies, credit bureaus, fintechs |
| **CST** | Cloud Computing Regulatory Framework v3 (CSP classes, data levels, residency); telecom licensing | CSPs and telecom operators |
| **CMA** | Cybersecurity Guidelines for Capital Market Institutions (4 domains, 26 subdomains) | Capital market institutions |
| **Health (MOH/CCHI)** | NPHIES health-data exchange platform requirements; PDPL sensitive-data rules govern health data | Health providers and insurers |

## NCA sibling controls — one-liners
- **DCC-1:2022** — Data Cybersecurity Controls: 3 domains, 11 subdomains, 19 main controls + 47 subcontrols; minimum data-lifecycle protections for ECC-covered entities
- **OTCC-1:2022** — OT/ICS control extension (replaces ECC-1's ICS domain)
- **TCC-1:2021** — secure telework baseline
- **CSCC-1:2019** — heightened controls for critical systems, layered on ECC

## Routing heuristics
- Government or CNI? → ECC first; add CCC/OTCC/DCC/CSCC as environment dictates.
- Any Saudi personal data? → PDPL always rides along.
- SAMA license? → SAMA CSF (min. maturity 3) + PDPL; ECC too if CNI.
- Selling cloud to anyone regulated? → CST class + CCC provider-side.
- No Saudi presence but Saudi customers? → PDPL extraterritorial reach still applies.

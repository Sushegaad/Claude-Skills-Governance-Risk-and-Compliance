# Saudi Cloud Stack — NCA CCC + CST Cloud Framework

## NCA Cloud Cybersecurity Controls (CCC)

Baseline: **CCC-1:2020**, with an updated **CCC-2:2024** reflected on NCA's site (data-localization responsibility referenced to NDMO). Extension of the ECC for cloud.

- **Role-split control IDs**: CSP-side controls (e.g., 1-3-P-1-1) vs tenant-side controls (e.g., 1-3-T-1-1) — always identify whether the user is the provider or the tenant before citing obligations.
- **Cloud levels tied to data classification** (Top Secret / Secret / Confidential / Public): higher classifications require higher-level cloud environments and stricter controls.
- Applies to CSPs serving ECC-covered entities and to those entities as tenants; tenant remains accountable for its data.

## CST Cloud Computing Regulatory Framework (v3)

- **CSP registration with CST** is required to operate; registration classes (Qualification / A / B / C) determine which customer data levels a CSP may host.
- **Customer data classified Levels 1–4**; **Levels 3–4 require in-Kingdom residency**.
- **Government data localization is exclusive** — government workloads must remain in KSA (narrow exceptions only).

## Practical routing

| Situation | Obligations |
|---|---|
| Hyperscaler/CSP entering KSA | CST registration (class per target data levels) + CCC CSP-side controls + PDPL (processor posture) for personal data |
| Government entity adopting cloud | ECC + CCC tenant-side controls + in-Kingdom hosting; classification drives cloud level |
| Private SaaS selling to government | Treat as CSP for that workload: CST class, CCC CSP controls, residency |
| Private company using foreign cloud for its own data | PDPL transfer rules for personal data; CCC only if ECC-covered |

Cite CCC control IDs only with the role marker and only from confirmed knowledge; otherwise cite by domain and direct to the official CCC document and its methodology/mapping annex.

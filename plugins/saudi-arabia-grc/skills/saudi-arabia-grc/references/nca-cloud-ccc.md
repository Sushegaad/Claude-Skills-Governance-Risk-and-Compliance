# Saudi Cloud Stack - NCA CCC + CST Cloud Regulations

## NCA Cloud Cybersecurity Controls (CCC)

Baseline: **CCC-1:2020**, with an updated **CCC-2:2024** reflected on NCA's site (data-localization responsibility referenced to NDMO). Extension of the ECC for cloud.

- **Role-split control IDs**: CSP-side controls (e.g., 1-3-P-1-1) vs tenant-side controls (e.g., 1-3-T-1-1) - always identify whether the user is the provider or the tenant before citing obligations.
- **Cloud levels tied to data classification** (Top Secret / Secret / Confidential / Public): higher classifications require higher-level cloud environments and stricter controls.
- Applies to CSPs serving ECC-covered entities and to those entities as tenants; tenant remains accountable for its data.

## CST Cloud Computing Services Provisioning Regulations (2023)

- The operative CST instrument is the **Cloud Computing Services Provisioning Regulations**, effective **October 10, 2023**, which replaced the Cloud Computing Regulatory Framework (history: CCRF v2, repealed December 2020, then CCRF v3, then the 2023 Regulations).
- **CSP registration with CST** is required to operate, with provider registration classes under the 2023 Regulations.
- Residency under the current regime distinguishes **Saudi Government Data**, which must remain in-Kingdom (narrow exceptions only), from **Non-Government Data**.
- The CCRF v2 scheme of customer data Levels 1-4 with in-Kingdom residency for Levels 3-4 is **repealed**; do not cite it as current.
- For registration class thresholds and other specifics, direct users to CST's published 2023 Regulations.

## Practical routing

| Situation | Obligations |
|---|---|
| Hyperscaler/CSP entering KSA | CST registration under the 2023 Regulations + CCC CSP-side controls + PDPL (processor posture) for personal data |
| Government entity adopting cloud | ECC + CCC tenant-side controls + in-Kingdom hosting; classification drives cloud level |
| Private SaaS selling to government | Treat as CSP for that workload: CST registration, CCC CSP controls, in-Kingdom residency for government data |
| Private company using foreign cloud for its own data | PDPL transfer rules for personal data; CCC only if ECC-covered |

Cite CCC control IDs only with the role marker and only from confirmed knowledge; otherwise cite by domain and direct to the official CCC document and its methodology/mapping annex.

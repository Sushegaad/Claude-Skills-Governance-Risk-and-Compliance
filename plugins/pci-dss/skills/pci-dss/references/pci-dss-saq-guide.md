# PCI DSS v4.0.1 — SAQ Selection Guide

Source: PCI DSS v4.0 SAQ documents (PCI Security Standards Council)
https://www.pcisecuritystandards.org/document_library/

---

## What is a Self-Assessment Questionnaire (SAQ)?

An SAQ is a validation tool intended to assist merchants and service providers in self-evaluating their compliance with PCI DSS. There are multiple SAQ types — each designed for a specific payment channel and cardholder data environment profile. The correct SAQ type depends on **how** your organisation accepts payments and **who** handles cardholder data.

Level 1 merchants and Level 1 service providers are **not eligible** for SAQs — they require an on-site Report on Compliance (ROC) completed by a Qualified Security Assessor (QSA).

---

## SAQ Selection Decision Tree

**Step 1: Are you a Level 1 Merchant or Level 1 Service Provider?**
- Yes → ROC required (not an SAQ). Stop here.
- No → Continue to Step 2.

**Step 2: Are you a Service Provider (not a merchant)?**
- Yes → **SAQ D for Service Providers** (unless Level 1)
- No (Merchant) → Continue to Step 3.

**Step 3: Do you accept card-present (face-to-face) transactions?**
- Yes, using ONLY imprint machines (no electronic transactions) → **SAQ B**
- Yes, using ONLY standalone dial-out terminals (no IP connectivity) → **SAQ B**
- Yes, using standalone IP-connected PTS POI devices only → **SAQ B-IP**
- Yes, using a validated P2PE solution only (PCI-listed) → **SAQ P2PE**
- Yes, using virtual payment terminals (isolated device, web-based) → **SAQ C-VT**
- Yes, using payment application systems connected to internet → **SAQ C**
- Yes, with any other scenario → **SAQ D for Merchants**

**Step 4: Do you accept card-not-present (CNP) — e-commerce or MOTO — only?**
- Yes, and ALL cardholder data functions fully outsourced, no redirect control → **SAQ A**
- Yes, e-commerce only, but you control the customer redirect to the payment page → **SAQ A-EP**
- Yes, MOTO only with virtual payment terminals (web-based, isolated device) → **SAQ C-VT**
- Any other CNP scenario → **SAQ D for Merchants**

---

## SAQ Types — Full Reference

### SAQ A — Fully Outsourced Card-Not-Present
**Applies to**: E-commerce and/or MOTO (mail order/telephone order) merchants only. No card-present transactions. All cardholder data functions (storage, processing, transmission) fully outsourced to PCI DSS-compliant third-party service providers. Merchant retains no electronic cardholder data.

**Requirements covered**: Subset of Req 2, 6, 8, 9, 10, 11, 12 (~22 controls)

**Eligibility criteria**:
- Cards not present at any time during the transaction
- All payment processing delegated to a PCI-compliant third party
- Merchant website does not directly receive cardholder data
- No cardholder data stored, processed, or transmitted by merchant systems or premises

**Examples**: Merchant uses a payment link or hosted payment page (Stripe, PayPal, Square Checkout). Customer is redirected completely to the provider's hosted page.

---

### SAQ A-EP — E-commerce with Partial Outsourcing
**Applies to**: E-commerce merchants ONLY. Merchant outsources payment processing but controls/influences how the customer is directed to the payment service. No card-present transactions.

**Requirements covered**: Subset of Req 2, 6, 8, 9, 10, 11, 12 (~191 controls)

**Eligibility criteria**:
- E-commerce only; no card-present
- Merchant's website includes payment page elements or partially controls redirect
- All cardholder data capture outsourced to compliant third party
- Merchant systems do not receive, store, process, or transmit CHD

**Examples**: Merchant website uses JavaScript-based payment widgets or iFrames that embed third-party payment capture within the merchant's own page.

**Key distinction from SAQ A**: SAQ A-EP requires script integrity controls (Req 6.4.3, 11.6.1) because the merchant controls the page hosting the widget.

---

### SAQ B — Imprint Machines or Standalone Dial-Out Terminals
**Applies to**: Merchants using ONLY imprint machines (knuckle-busters) OR standalone, dial-out (non-IP) terminals. No e-commerce.

**Requirements covered**: Subset of Req 2, 8, 9, 10, 11, 12 (~41 controls)

**Eligibility criteria**:
- Transactions processed only via imprint machines or dial-out (telephone-line) terminals
- Terminals not IP-connected and not connected to any other system in the environment
- No electronic cardholder data stored on any computer system
- No e-commerce

**Examples**: Small retail using a standalone Dial-Up terminal or old knuckle-buster imprinter.

---

### SAQ B-IP — Standalone IP-Connected PTS POI Devices
**Applies to**: Merchants using ONLY standalone PTS (PIN Transaction Security) POI devices with IP connectivity. Devices must be PCI-listed PTS POI devices. No e-commerce.

**Requirements covered**: Subset of Req 1, 2, 6, 8, 9, 10, 11, 12 (~83 controls)

**Eligibility criteria**:
- ONLY standalone PCI-listed PTS POI devices with IP connection used
- Devices not connected to any other system in the merchant environment
- No e-commerce

**Examples**: Merchant using a certified IP-connected payment terminal (e.g., Ingenico, Verifone) with an IP connection but isolated from other systems.

---

### SAQ C-VT — Virtual Payment Terminals (Web-Based)
**Applies to**: Merchants using only web-based virtual payment terminal solutions accessed via a web browser on an isolated computing device. No e-commerce; no cardholder data electronically stored.

**Requirements covered**: Subset of Req 1, 2, 6, 8, 9, 10, 11, 12 (~90 controls)

**Eligibility criteria**:
- Payment processing via web-browser virtual terminal only
- Device used for virtual terminal is isolated and dedicated to payment processing
- No cardholder data storage on any system
- No card-present (physical card swiped) via this method
- Device not connected to other systems in the environment

**Examples**: MOTO merchant logs into a hosted virtual terminal (e.g., PayPal Virtual Terminal, Authorize.Net) on a dedicated PC to key-enter card details.

---

### SAQ C — Payment Application Systems Connected to Internet
**Applies to**: Merchants with payment application systems connected to the internet. No e-commerce. Device/application(s) not connected to other systems in the environment.

**Requirements covered**: Subset of Req 1, 2, 5, 6, 8, 9, 10, 11, 12 (~160 controls)

**Eligibility criteria**:
- Payment application connected to internet (e.g., point-of-sale system with internet connectivity)
- Not an e-commerce channel
- Payment application not connected to other systems within the facility (segmented)
- No electronic storage of CHD after authorisation

**Examples**: Retail merchant using an internet-connected POS application (e.g., Square POS, Lightspeed) on a device isolated from other business systems.

---

### SAQ P2PE — Validated P2PE Solution
**Applies to**: Merchants using ONLY hardware payment terminals in a PCI-validated, PCI-listed P2PE solution. No e-commerce.

**Requirements covered**: Very small subset of Req 9, 12 (~33 controls)

**Eligibility criteria**:
- ALL cardholder data captured via terminals included in a PCI-validated P2PE solution
- P2PE solution is on the PCI SSC list of validated P2PE solutions
- No e-commerce
- Merchant has no access to clear-text CHD

**Examples**: Merchant using a Verifone or Ingenico terminal within a certified P2PE solution (e.g., Bluefin PayConex P2PE, Worldpay Total P2PE).

**Key benefit**: Dramatically reduces PCI DSS scope — merchants only attest to physical security of terminals and selecting a compliant P2PE provider.

---

### SAQ D — All Other Merchants and Service Providers

**SAQ D for Merchants**
**Applies to**: All merchants who do not meet criteria for SAQ A, A-EP, B, B-IP, C, C-VT, or P2PE. Covers all 12 PCI DSS requirements.

**Requirements covered**: All 12 requirements (~340+ controls)

**Examples**: Merchants that store CHD, have complex multi-channel environments, or don't qualify for a simpler SAQ.

---

**SAQ D for Service Providers**
**Applies to**: All service providers eligible for SAQ validation (Level 2 service providers). Covers all 12 PCI DSS requirements.

**Requirements covered**: All 12 requirements (~340+ controls, service-provider-specific questions)

**Note**: Service providers have additional requirements vs merchants, particularly around Req 12.8 (TPSP management), Req 12.9 (TPSP acknowledgement), and Req 3.3.2 (SAD protection).

---

## Report on Compliance (ROC)

An ROC is required for:
- **Level 1 Merchants**: >6 million Visa/MC transactions per year, OR any merchant that has suffered a breach that resulted in account data compromise
- **Level 1 Service Providers**: >300,000 transactions per year OR designated by a card brand

**ROC process**:
1. Engage a Qualified Security Assessor (QSA) from the PCI SSC's list
2. QSA performs on-site assessment against all applicable PCI DSS controls
3. QSA completes the ROC Template (v4.0.1 template released 2024)
4. Organisation completes the Attestation of Compliance (AOC) signed by QSA and officer
5. Submit ROC + AOC to acquiring bank or card brand

---

## Attestation of Compliance (AOC)

The AOC is a declaration of the organisation's PCI DSS compliance status. It is:
- Completed alongside the ROC (Level 1) or SAQ (Levels 2–4)
- Signed by both the organisation's officer and the QSA (for ROC) or responsible officer (for SAQ)
- Submitted annually to the acquiring bank or card brand
- A merchant-specific or service provider-specific version exists

---

## Approved Scanning Vendor (ASV) Scans

Quarterly external vulnerability scans by an ASV are required for all merchants and service providers. An ASV is a company approved by PCI SSC to perform external network vulnerability scanning services.

- Scans must result in a **passing scan** (no unresolved high-severity vulnerabilities)
- If a scan fails, remediate and re-scan until a passing result is achieved
- Passing scan reports must be retained for compliance evidence
- Internal scans (Req 11.3.1) may be performed by internal staff

---

## Qualified Security Assessor (QSA) vs Internal Security Assessor (ISA)

| Role | Who | Used For |
|------|-----|---------|
| **QSA** | External PCI SSC-approved company | Required for ROC (Level 1); optional for SAQs to guide/verify |
| **ISA** | Internal employee trained and certified by PCI SSC | Can perform internal assessments; cannot sign ROC for Level 1 |

ISAs are useful for ongoing internal compliance monitoring and SAQ validation for Levels 2–4.

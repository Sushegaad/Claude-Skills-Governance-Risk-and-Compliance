---
name: nist-sp-800-63
description: >
  Expert NIST SP 800-63 Rev 3 Digital Identity Guidelines advisor. Use this skill
  whenever a user asks about digital identity, identity assurance levels (IAL1, IAL2,
  IAL3), authenticator assurance levels (AAL1, AAL2, AAL3), federation assurance levels
  (FAL1, FAL2, FAL3), identity proofing, credential service providers (CSPs), verifiers,
  relying parties, multi-factor authentication, phishing-resistant authenticators,
  TOTP, FIDO2/WebAuthn, PIV, CAC, federation protocols (OIDC, SAML), identity
  verification for online services, remote or in-person identity proofing, binding
  of authenticators, digital identity risk assessment, selecting identity assurance
  levels, or building an identity and access management (IAM) programme aligned to
  NIST standards. Also trigger for questions about: "what IAL do I need?", "does MFA
  satisfy AAL2?", "what is identity proofing?", "how do I verify a user's identity
  remotely?", "what authenticator types are allowed at AAL2?", "what is a CSP?",
  "how do I federate identity?", or any NIST identity, authentication, or digital
  credential question.
---

# NIST SP 800-63 Rev 3 — Digital Identity Guidelines Skill

You are an expert digital identity advisor specialising in **NIST Special Publication 800-63 Revision 3: Digital Identity Guidelines** (June 2017, with errata as of March 2020). This suite comprises four volumes: SP 800-63-3 (the overarching guideline), **SP 800-63A** (Enrollment and Identity Proofing), **SP 800-63B** (Authentication and Lifecycle Management), and **SP 800-63C** (Federation and Assertions).

You assist **federal agencies, identity architects, IAM engineers, security architects, and application developers** in selecting appropriate assurance levels, implementing identity proofing, choosing and deploying authenticators, and building federation architectures.

---

## How to Respond

| Task | Output Format |
|------|--------------|
| Assurance level selection | Table: Level | Requirements Met | Recommendation |
| Identity proofing requirements | Structured list per IAL level |
| Authenticator type guidance | Table: Type | AAL | Phishing Resistance | FIPS 140 | Notes |
| Federation/assertion guidance | Protocol comparison or structured requirements list |
| Risk assessment for identity | Structured risk table: xAL | Impact | Confidence | Recommended level |
| General question | Concise prose with SP 800-63 section citations |

---

## SP 800-63 Rev 3 Overview

### Purpose

SP 800-63 Rev 3 establishes technical requirements for federal agencies implementing digital identity services. It defines three assurance dimensions and the technical requirements for each level:

- **Identity Assurance Level (IAL)**: Confidence in the binding between the claimed identity and the real person
- **Authenticator Assurance Level (AAL)**: Strength of the authentication process itself (how confident are we that the person holds the claimed authenticator)
- **Federation Assurance Level (FAL)**: Strength of assertions passed between identity providers and relying parties in a federated system

These three dimensions are **selected independently** — an application may require IAL2 but only AAL1, or IAL1 with AAL2.

### Key Roles (SP 800-63-3)

| Role | Definition |
|------|-----------|
| **Claimant** | An individual whose identity is being asserted |
| **Credential Service Provider (CSP)** | An entity that issues credentials and manages authenticators |
| **Verifier** | An entity that verifies the claimant's identity through a protocol |
| **Relying Party (RP)** | An entity that uses authentication assertions to provide services |
| **Identity Provider (IdP)** | In a federated model, the entity that manages the subscriber's identity |
| **Subscriber** | A party that has undergone identity proofing and received credentials from the CSP |
| **Applicant** | A party undergoing the enrolment and identity proofing process |

---

## Identity Assurance Levels (IAL) — SP 800-63A

IAL defines the level of confidence in the claimed identity of the subscriber.

### IAL1 — No Identity Proofing Required

**Requirements**: No identity proofing. Self-asserted attributes accepted.
**Use when**: The application has no need to bind a real-world identity to the digital identity (e.g., anonymous access, low-risk applications where the service can be accessed by anyone).
**Acceptable evidence**: None required
**Proofing method**: None

### IAL2 — In-Person or Remote Proofing with Documentary Evidence

**Requirements**: Identity proofing required; real-world existence of the claimed identity verified. Attributes are verified against authoritative sources or documentary evidence.
**Use when**: The service relies on the subscriber's identity (e.g., accessing government benefits, e-signature, court filings).
**Acceptable evidence**:
- **Superior evidence** (1 sufficient): Passport (US or foreign with MRZ), Real ID driver's licence or state ID, military ID
- **Strong evidence** (2 sufficient, or 1 strong + 2 fair): Driver's licence (non-Real ID), state ID, national ID card, military retiree ID, Permanent Resident Card
- **Fair evidence** (2 required in combination): Voter registration card, utility bills (current), bank statement, government-issued document with photo

**Proofing methods** (IAL2):
1. **In-person proofing**: Present original documents to trained operator; operator verifies authenticity; biometric binding optional
2. **Supervised remote proofing**: Live video session with a trained operator; document scan verified via automated and/or human review; biometric comparison against AAMVA/DMV records or passport chip

**Biometric**: Optional at IAL2; if collected, must be used to prevent duplicate enrolment

### IAL3 — In-Person Proofing with Biometric Binding

**Requirements**: In-person proofing with a trained representative. Physical inspection of original documents. Biometric collection required and bound to the subscriber's identity record.
**Use when**: The highest confidence in identity is required; national security systems; issuing physical identity credentials.
**Acceptable evidence**: Superior evidence OR strong + biometric comparison against a government authoritative database
**Proofing method**: In-person only; biometric capture (fingerprint, facial image) bound to the enrolment record

---

## Authenticator Assurance Levels (AAL) — SP 800-63B

AAL defines the strength of the authentication process.

### Authenticator Types and AAL Eligibility

| Authenticator Type | Description | AAL1 | AAL2 | AAL3 |
|-------------------|-------------|------|------|------|
| Memorised Secret (Password/PIN) | Something the user knows | Yes | No (alone) | No (alone) |
| Look-Up Secrets (backup codes) | Static codes from a printed list | Yes | No (alone) | No |
| Out-of-Band (SMS/PSTN) | One-time code sent via SMS or voice | Yes | Restricted (see below) | No |
| Single-Factor OTP (TOTP app) | Time-based or HMAC-based OTP | Yes | Yes (as 2nd factor) | No |
| Multi-Factor OTP Device | Hardware OTP with PIN | Yes | Yes | No |
| Single-Factor Cryptographic Software | Private key in software (e.g., browser key) | Yes | No (alone) | No |
| Single-Factor Cryptographic Device | Hardware key (e.g., FIDO2 security key) | Yes | Yes (as 2nd factor) | Yes (with PIN) |
| Multi-Factor Cryptographic Software | Software private key with memorised secret | Yes | Yes | No |
| Multi-Factor Cryptographic Device (hardware) | PIV card, CAC, FIDO2 hardware key with PIN | Yes | Yes | Yes |

**AAL1**: Single-factor authentication. Any permitted authenticator type. Memorised secrets acceptable alone.
**AAL2**: Multi-factor authentication required. At least two of: something you know, something you have, something you are. Phishing resistance not required but recommended.
**AAL3**: Phishing-resistant hardware-based multi-factor authentication. Cryptographic device (hardware) required. Verifier impersonation resistance required. In-person verification of hardware bond may be required.

### Phishing Resistance at AAL

- **AAL1**: No phishing resistance required
- **AAL2**: Phishing resistance not required but recommended; SMS OTP is "restricted" at AAL2 (agencies must document risk)
- **AAL3**: Verifier impersonation resistance required — only hardware cryptographic authenticators that bind to the specific verifier (e.g., FIDO2 with origin binding, PIV with card-validated TLS) satisfy this requirement

### SMS/PSTN at AAL2 — "Restricted" Status

SP 800-63B designates SMS and PSTN-based out-of-band authenticators as "RESTRICTED" at AAL2. Agencies using them must:
1. Document the risk assessment justifying the use
2. Offer subscribers at least one alternative AAL2-eligible authenticator
3. Implement additional risk controls (fraud detection, anomaly detection)
4. Notify subscribers of risk

### FIPS 140 Requirements

| AAL | FIPS 140 Requirement |
|-----|---------------------|
| AAL1 | No FIPS 140 required |
| AAL2 | If cryptographic authenticator used: FIPS 140 Level 1 overall (Level 2 physical security for hardware authenticators) |
| AAL3 | FIPS 140 Level 2 overall; Level 3 physical security |

### Reauthentication Requirements

| AAL | Inactivity Timeout | Absolute Session Limit |
|-----|-------------------|----------------------|
| AAL1 | 30 days | No absolute limit |
| AAL2 | 30 minutes inactivity OR 12 hours absolute | 12 hours (with reauthentication) |
| AAL3 | 15 minutes inactivity OR 12 hours absolute | 12 hours |

---

## Federation Assurance Levels (FAL) — SP 800-63C

FAL describes the strength of an assertion passed from an IdP to an RP in a federated authentication scenario.

### FAL1 — Bearer Assertion from IdP

**Requirements**: Bearer assertion from the IdP; assertion must be signed (e.g., with RS256) so the RP can verify it was issued by the IdP; assertion delivered through the front channel (browser redirect) or back channel
**Protocols**: OpenID Connect (OIDC) ID tokens via implicit or authorization code flow; SAML 2.0 basic

### FAL2 — Bearer Assertion Encrypted for RP

**Requirements**: Assertion must be encrypted for the specific RP so that only the RP can decrypt it; prevents honest-but-curious IdP from observing what the RP is doing with the assertion
**Protocols**: OIDC with token endpoint using RS256 signing + RSA-OAEP encryption for ID token; SAML with XML Encryption

### FAL3 — Holder-of-Key Assertion

**Requirements**: Assertion must be cryptographically bound to the subscriber's authenticator so that only a holder of the matching key can use the assertion; provides protection against assertion theft
**Protocols**: token binding or equivalent mechanisms; FIDO2 with attestation; SAML HoK profile

### Selecting FAL

| FAL | When to Use |
|-----|------------|
| FAL1 | Low-risk federated applications; internal enterprise applications; where assertion interception risk is low |
| FAL2 | Moderate-risk applications where assertion confidentiality is important; where the IdP should not know what the RP is doing with the assertion |
| FAL3 | High-risk applications; national security systems; where assertion replay or theft is a significant threat |

---

## Digital Identity Risk Assessment

SP 800-63-3 Section 6 defines a risk assessment process for selecting the appropriate xAL levels.

### Step 1 — Identify Transactions and Potential Harms

For each transaction in the application, identify what could go wrong if:
- The wrong person was authenticated (authentication failure)
- The identity proofing was wrong (the person is not who they claim)
- A federation assertion was compromised

### Step 2 — Assess Potential Harm Categories

| Harm Category | Description |
|--------------|-------------|
| Inconvenience, distress, or damage to standing | Embarrassment, loss of reputation |
| Financial loss or liability | Direct financial harm to the subscriber or RP |
| Harm to agency programs or public interests | Mission failure, regulatory violation |
| Unauthorised release of sensitive information | Disclosure of PII, PHI, or classified material |
| Personal safety | Physical harm to the subscriber or others |
| Civil or criminal violations | Legal liability |

### Step 3 — Determine Impact Level

For each harm category, assess impact as Low, Moderate, or High.

| Impact | Definition |
|--------|-----------|
| Low | Limited adverse effect; minor inconvenience; easily recoverable |
| Moderate | Significant adverse effect; substantial harm to reputation, financial loss, mission degradation |
| High | Severe or catastrophic adverse effect; major financial loss, serious mission degradation, loss of safety |

### Step 4 — Select xAL Based on Maximum Impact

| Maximum Impact | Minimum IAL | Minimum AAL | Minimum FAL |
|--------------|-------------|-------------|-------------|
| Low | IAL1 | AAL1 | FAL1 |
| Moderate | IAL2 | AAL2 | FAL2 |
| High | IAL3 | AAL3 | FAL3 |

Agencies may select a higher xAL than the minimum if mission requirements, policy, or risk acceptance decisions warrant.

---

## Credential and Authenticator Lifecycle — SP 800-63B

### Binding and Enrollment
- New authenticators must be **bound to the subscriber's account** during enrolment
- If the subscriber already has an existing authenticator, adding a new authenticator requires **re-authentication with the existing authenticator** (or identity verification at the appropriate IAL)
- Lost authenticator: replacement requires identity proofing at or above the IAL of the original enrolment

### Authenticator Requirements
- **Memorised secrets**: Minimum 8 characters; no complexity requirements mandated (complexity rules are deprecated in 800-63B); check against breach corpora (Have I Been Pwned list); no mandatory periodic expiry; expiry required only on suspicion of compromise
- **TOTP apps**: Algorithm: TOTP (RFC 6238) or HOTP (RFC 4226); 6-8 digit codes; valid window up to 30 seconds
- **Hardware OTP**: Nonce-based or time-based; must be validated by the verifier within acceptable time window

### Account Recovery
At AAL2 and AAL3, account recovery must be at the same or higher assurance level as the original enrollment. Recovery codes (Look-up Secrets) may be issued at setup time.

---

## Core Workflows

### 1. Selecting xAL Levels for an Application
1. Identify all transactions in the application
2. For each transaction, identify potential harms from misrepresented identity, authentication failure, or assertion compromise
3. Assess impact level (Low / Moderate / High) for each harm category
4. Select xAL at Minimum based on maximum impact; document rationale
5. Review against agency policy and OMB guidance (M-19-17 for high-value assets)
6. Document the Digital Identity Risk Assessment in the system security documentation

### 2. Advising on Authenticator Selection
1. Confirm the required AAL (from risk assessment)
2. For AAL1: any authenticator permitted; memorised secret adequate
3. For AAL2: two factors required; recommend hardware FIDO2 key or multi-factor OTP over SMS; flag SMS as RESTRICTED
4. For AAL3: hardware cryptographic MFA only; FIDO2 hardware key with PIN or PIV/CAC; document FIPS 140 requirement

### 3. Planning Identity Proofing
1. Confirm the required IAL (from risk assessment)
2. For IAL1: no proofing required; document rationale
3. For IAL2: select in-person or supervised remote proofing; identify acceptable documentary evidence; plan biometric binding if needed
4. For IAL3: plan in-person proofing; identify trained operators; plan biometric collection

---

## Reference Files

- `references/assurance-levels.md` — Detailed IAL, AAL, and FAL requirements tables, selection matrices, and xAL combinations
- `references/authenticator-requirements.md` — Per-authenticator-type requirements, FIPS 140 levels, OTP algorithm requirements, reauthentication tables, lifecycle requirements
- `references/identity-proofing.md` — Identity proofing processes for IAL2 and IAL3 including evidence types, validation methods, biometric requirements, remote proofing requirements

**When to load:**
- Selecting assurance levels or performing a digital identity risk assessment → load `references/assurance-levels.md`
- Choosing authenticator types or designing authentication flows → load `references/authenticator-requirements.md`
- Planning identity proofing or CSP enrolment → load `references/identity-proofing.md`

---

## Disclaimer

This skill is based on NIST SP 800-63 Rev 3 (June 2017) and its errata (March 2020), a freely available NIST publication. NIST SP 800-63-4 is in draft as of 2024; agencies should monitor csrc.nist.gov for the final publication and update their implementations accordingly. This skill does not constitute legal or compliance advice. Federal agencies must also comply with OMB M-19-17 (Enabling Mission Delivery through Improved Identity, Credential, and Access Management).

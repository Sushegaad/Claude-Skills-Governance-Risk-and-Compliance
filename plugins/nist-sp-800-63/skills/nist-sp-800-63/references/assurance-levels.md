# Assurance Levels Reference — NIST SP 800-63 Rev 3

Source: NIST SP 800-63-3 (June 2017), SP 800-63A Rev 3, SP 800-63B Rev 3, SP 800-63C Rev 3

---

## Identity Assurance Level (IAL) — Detailed Requirements

### IAL1

No identity proofing. Self-asserted attributes accepted without verification.

**Risks accepted by using IAL1**:
- The subscriber may not be who they claim to be
- Any person can create an account
- Attributes (name, email) are unverified

**Appropriate for**:
- Public-facing applications with no access to personal data
- Anonymous or pseudonymous services
- Services where the user's real identity is irrelevant to the service provided

**Not appropriate for**:
- Services that disburse benefits or funds to individuals
- Applications with access to personal health, financial, or safety data
- High-value asset systems

---

### IAL2 — Full Requirements Table

| Requirement | Remote (Unsupervised) | Remote (Supervised) | In-Person |
|------------|----------------------|---------------------|----------|
| Identity proofing required | Yes | Yes | Yes |
| Evidence required | 1 Superior OR 1 Strong + 2 Fair | 1 Superior OR 1 Strong + 2 Fair | 1 Superior OR 1 Strong + 2 Fair |
| Evidence must be unexpired | Yes | Yes | Yes |
| Evidence validation against issuer | Against available authoritative sources | Against available authoritative sources | Against available authoritative sources |
| Address confirmation required | Yes (notice to home address on record) | Yes | Yes |
| Biometric required | No (optional) | No (optional) | No (optional) |
| Live operator involvement | No | Yes (via video link) | Yes (in-person) |
| Allowed? (as of 800-63A-3 errata) | See note below | Yes | Yes |

**Note on unsupervised remote proofing (IAL2)**: The original SP 800-63A permitted unattended remote proofing with strong document validation and liveness detection. Agencies must use approved KBV (knowledge-based verification) limitations — KBV alone is NOT sufficient at IAL2; it may only be used as a secondary supplement. As of the March 2020 errata, agencies should consider whether their unsupervised remote proofing implementation meets the normative requirements.

**Address confirmation at IAL2**:
If not verified in-person:
- Send enrollment code to the address of record via postal mail
- Enrollment code must be validated by the subscriber within 5-day validity window
- OR, a USPS National Change of Address (NCOA) query is performed

---

### IAL3 — Full Requirements Table

| Requirement | IAL3 |
|------------|------|
| Proofing type | In-person only |
| Operator | Trained, authorised CSP representative |
| Evidence | Superior (1) AND physical document check; or Strong evidence with biometric match against authoritative source |
| Evidence validation | Physical authentication features checked (holograms, watermarks, MRZ validation) |
| Biometric collection | Required; facial image and/or fingerprint |
| Biometric binding | Biometric template bound to the identity record; used for future in-person re-verification |
| Duplicate enrolment check | Required — biometric compared against existing records to prevent creation of multiple identities |
| FIPS 140 for biometric capture | Level 1 minimum for the capture device |

---

## Authenticator Assurance Level (AAL) — Requirements Summary

### AAL1 Requirements

- **Factors**: Single factor
- **Permitted types**: Any authenticator type in SP 800-63B Table 1
- **Memorised secrets**: Minimum 8 characters; no other requirements
- **Reauthentication**: After 30 days of inactivity
- **FIPS 140**: Not required
- **Phishing resistance**: Not required
- **Verifier compromise resistance**: Not required
- **Communications security**: Approved cryptography required for authenticator output transmission

### AAL2 Requirements

- **Factors**: Multi-factor (two or more)
- **Permitted multi-factor combinations**:
  - Multi-Factor OTP Device (hardware) + Memorised Secret
  - Single-Factor OTP Device + Memorised Secret
  - Multi-Factor Cryptographic Software + Memorised Secret (or inherence)
  - Single-Factor Cryptographic Device + Memorised Secret
  - Multi-Factor Cryptographic Device
- **SMS/PSTN**: RESTRICTED — permitted with documented risk assessment and alternative authenticator offered
- **Reauthentication**: 30 minutes inactivity AND 12 hours absolute (with reauthentication)
- **FIPS 140**: Level 1 overall for cryptographic authenticators; Level 2 physical security for hardware cryptographic authenticators
- **Phishing resistance**: Not required but recommended
- **Verifier compromise resistance**: Not required
- **Man-in-the-Middle resistance**: Required (secure channel)

### AAL3 Requirements

- **Factors**: Multi-factor hardware cryptographic
- **Permitted types only**:
  - Multi-Factor Cryptographic Device (hardware)
  - Single-Factor Cryptographic Device + Memorised Secret
- **Phishing resistance / verifier impersonation resistance**: Required — the authenticator must bind to a specific verifier (e.g., FIDO2 origin binding, TLS channel binding)
- **Reauthentication**: 15 minutes inactivity AND 12 hours absolute
- **FIPS 140**: Level 2 overall; Level 3 physical security
- **Verifier compromise resistance**: Required
- **Intent**: Authenticator must require explicit user action (e.g., pressing a button on the hardware key)

---

## Federation Assurance Level (FAL) — Requirements Summary

### FAL1

| Requirement | Value |
|------------|-------|
| Assertion type | Bearer |
| Assertion signed | Yes (IdP's private key) |
| Assertion encrypted | Not required |
| Delivery | Front or back channel |
| Example protocol | OIDC with RS256-signed ID token; SAML with XML-DSig |
| Subscriber binding | Not required |

### FAL2

| Requirement | Value |
|------------|-------|
| Assertion type | Bearer |
| Assertion signed | Yes |
| Assertion encrypted | Yes — encrypted for the specific RP's public key |
| Delivery | Front or back channel |
| Example protocol | OIDC with encrypted ID token (RS256 + RSA-OAEP or A128KW); SAML with XML Encryption |
| Subscriber binding | Not required |

### FAL3

| Requirement | Value |
|------------|-------|
| Assertion type | Holder-of-key |
| Assertion signed | Yes |
| Assertion encrypted | Recommended |
| Delivery | Back channel preferred |
| Example protocol | FIDO2 with assertion cryptographically bound to subscriber key; Token Binding; SAML HoK profile |
| Subscriber binding | Required — assertion can only be used by the holder of the matching private key |

---

## xAL Selection Matrix

### By Impact Level (SP 800-63-3 Table 6-2)

| Impact Level | Recommended IAL | Recommended AAL | Recommended FAL |
|-------------|----------------|----------------|----------------|
| Low | IAL1 | AAL1 | FAL1 |
| Moderate | IAL2 | AAL2 | FAL2 |
| High | IAL3 | AAL3 | FAL3 |

### Allowed xAL Combinations

The three assurance levels are independent. Common valid combinations:

| Scenario | IAL | AAL | FAL | Rationale |
|---------|-----|-----|-----|----------|
| Public information service | 1 | 1 | 1 | No PII, no harm from misidentification |
| Benefits eligibility inquiry (no disbursement) | 2 | 2 | 2 | Moderate impact if wrong person accesses data |
| Benefits disbursement | 2 | 2 | 2 | Moderate financial harm if wrong person claims |
| Healthcare portal (PHI access) | 2 | 2 | 2 | Moderate harm from PHI disclosure |
| High-value asset system (HVA) | 3 | 3 | 3 | Severe mission harm; OMB M-19-17 applies |
| Internal admin app (federated SSO) | 1 | 2 | 1 | No external identity; strong auth required |
| PIV-gated federal system | 2 or 3 | 3 | 3 | PIV satisfies IAL2/3 + AAL3 |

### Notable Decoupled Combinations

- **IAL1 + AAL2**: No identity proofing needed, but strong authentication required (e.g., a service that grants access by role after strong auth, but doesn't need to verify who the person is in the real world)
- **IAL2 + AAL1**: Identity verified but single-factor auth acceptable (e.g., low-sensitivity service that still needs to know who the person is — uncommon and discouraged for most scenarios)

---

## OMB Supplemental Requirements (M-19-17)

OMB Memorandum M-19-17 (May 2019) directed ICAM policy for federal agencies:

| Requirement | When Applicable |
|------------|----------------|
| Identity proofing at IAL2 minimum for all government-issued digital credentials | All federal programs issuing digital credentials |
| PIV or PIV-derived credentials for federal employee and contractor access to federal systems | Federal employees and contractors accessing High Value Assets |
| Strong authentication (AAL2 minimum) for all federal applications | All federal agencies |
| Phishing-resistant authentication for all high-value assets | HVAs per OMB M-19-03 |

---

## PIV and CAC in the 800-63B Framework

The PIV card (FIPS 201) and the Common Access Card (CAC) are **Multi-Factor Cryptographic Devices** that satisfy:
- AAL2 (contact or contactless interface with PIN)
- AAL3 (contact interface with PIN; satisfies verifier impersonation resistance via TLS channel binding or key confirmation)

PIV-Derived Credentials (PIV-D) issued to mobile devices satisfy AAL2.

---

## Deprecated Practices (SP 800-63B)

The following practices from older NIST guidance are deprecated in SP 800-63B:

| Deprecated Practice | Why Deprecated |
|--------------------|---------------|
| Mandatory password expiration (periodic rotation without cause) | Forces users to choose weaker predictable patterns |
| Knowledge-Based Authentication (KBA/KBV) as sole authenticator | KBV data often publicly available; does not constitute possession factor |
| Password complexity rules (upper/lower/number/special) | Shown to reduce entropy and increase predictable substitutions |
| Limiting password characters (excluding special chars) | Reduces entropy |
| Password hints | Reduces security of memorised secret |
| Security questions for account recovery | KBV; same deprecation reasons as KBA |

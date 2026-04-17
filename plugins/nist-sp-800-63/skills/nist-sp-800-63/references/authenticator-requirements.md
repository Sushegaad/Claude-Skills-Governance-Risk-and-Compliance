# Authenticator Requirements — NIST SP 800-63B Rev 3

Source: NIST SP 800-63B Rev 3 (June 2017), errata March 2020

---

## Authenticator Type Definitions

### 1. Memorised Secret (Password or PIN)

**Definition**: A secret value that is intended to be chosen and memorised by the user.

**Requirements**:
- Minimum 8 characters for user-chosen passwords
- Minimum 6 digits for PINs used as a single factor (AAL1 only)
- Maximum length: at least 64 characters must be supported
- All printable ASCII characters and Unicode MUST be accepted
- Spaces MUST be counted when calculating length (leading/trailing spaces may be trimmed for comparison)
- Passwords SHALL be compared in a case-sensitive manner

**Verifier requirements**:
- Check against a list of commonly-used, expected, or compromised passwords (e.g., HIBP breach lists, dictionary words, context-specific words like the service name)
- Rate limiting or lockout required after repeated failed attempts (NIST does not define exact thresholds; agencies should implement based on risk)
- No truncation of passwords — full character set must be preserved
- Passwords MUST be stored as salted hashes using an approved algorithm (e.g., Argon2, bcrypt, scrypt, or PBKDF2 with SHA-256 and at least 10,000 iterations)
- Temporary passwords (for reset) must be single-use and expire after a short time period

**What is deprecated (MUST NOT do)**:
- Mandatory periodic rotation without evidence of compromise
- Password complexity rules (mixed case + numbers + special chars combinations)
- Password hints
- Security questions for account recovery as sole mechanism
- Restricting what characters can be used

---

### 2. Look-Up Secrets (Backup Codes)

**Definition**: Physical or electronic record containing a set of secrets shared between the claimant and the CSP. Examples: printed backup codes, recovery codes.

**Requirements**:
- At least 112 bits of entropy (or at least 6 characters from a 64-character set; a common implementation is 8-10 alphanumeric characters)
- Each look-up secret must be used only once (single-use)
- Any remaining unused look-up secrets must be invalidated after a new set is issued
- Must be stored hashed at the verifier

**AAL eligibility**: AAL1 only (count as a single factor — possession)

---

### 3. Out-of-Band Authenticators (OOB) — Includes SMS, Email, Voice

**Definition**: A separate communications channel (the "out-of-band" device) is used to verify possession.

**Requirements (for push notifications on dedicated app)**:
- Uniquely addressable device; authenticity of device verified at binding time
- Push notifications require user action to approve (not just passive receipt)

**SMS/PSTN requirements (RESTRICTED)**:
Because the PSTN is not end-to-end encrypted and SIM-swapping attacks exist, SMS and PSTN-based OOB is designated RESTRICTED at AAL2. Agencies using SMS must:
1. Document the risk in a formal risk assessment
2. Offer subscribers at least one non-restricted alternative (e.g., TOTP app or hardware key)
3. Monitor for evidence that SMS is not longer adequately protecting the application
4. Issue risk notifications to subscribers

**Email-based OTP**: NOT PERMITTED as an out-of-band authenticator at AAL2. Email is not a "separate channel" for identity verification purposes and is a common attack target.

---

### 4. Single-Factor OTP (TOTP/HOTP Application)

**Definition**: A software authenticator app (Authenticator app) that generates short-term OTP codes using TOTP (RFC 6238) or HOTP (RFC 4226).

**Algorithm requirements**:
- TOTP: 30-second time step; X.509-level time synchronisation recommended; validity window: adjacent ±1 step acceptable
- HOTP: Counter-based; must accept at a look-ahead window (SP 800-63B recommends a maximum look-ahead of 10 counter values)
- OTP length: At least 6 digits; 8 digits preferred for increased entropy
- Each OTP code must be single-use; verifier must store last used OTP to prevent reuse

**Security**: App is locked to the device via a secret seed; seed must be securely provisioned and stored on the device
**FIPS 140**: Not required for AAL2 software OTP apps; required at Level 1 for any software used in an AAL3 scenario

---

### 5. Multi-Factor OTP Device (Hardware Token)

**Definition**: A hardware device that generates OTP codes, activated by a second factor (typically a PIN or biometric).

**Examples**: RSA SecurID with PIN, YubiKey OTP mode with PIN

**Requirements**:
- Must require a PIN or other second activation factor to generate the OTP
- Hardware must resist physical tampering to extract the seed
- FIPS 140 Level 2 physical security required

**AAL eligibility**: AAL2 (satisfies both factors in a single hardware device)

---

### 6. Single-Factor Cryptographic Software

**Definition**: Private key stored in software (e.g., in a browser, in a software certificate store).

**Examples**: Browser TLS client certificates (software key), software-stored FIDO2 keys

**Requirements**:
- Must use approved cryptographic algorithms (RSA-2048+, EC P-256 or higher)
- Key must be bound to the application (origin, relying party)
- Single-factor only — requires combination with second factor for AAL2

**AAL eligibility**: AAL1 only (single factor); AAL2 as second factor combined with memorised secret

---

### 7. Single-Factor Cryptographic Device (Hardware Key)

**Definition**: A hardware device containing a cryptographic key, activated by a simple user presence check (e.g., button press) without a PIN.

**Examples**: FIDO2 hardware security key without PIN configured (activation by touch only)

**Requirements**:
- Hardware must resist extraction of private key
- Must require an explicit user action (button press, card insert) to sign
- FIPS 140 Level 2 physical security required

**AAL eligibility**: AAL2 as second factor (combined with memorised secret)

---

### 8. Multi-Factor Cryptographic Software

**Definition**: Private key stored in software, where activation requires a memorised secret or biometric (the second factor is software-internal).

**Examples**: Software certificate protected by a PIN or passphrase; PIV-derived credential in a locked key container on a mobile device

**Requirements**:
- Activation secret (PIN/passphrase) must meet memorised secret requirements
- Key storage protected by the OS or secure enclave

**AAL eligibility**: AAL2 (satisfies both factors within one software authenticator)

---

### 9. Multi-Factor Cryptographic Device (Hardware Token with PIN)

**Definition**: A hardware device containing a cryptographic key, activated by a PIN or biometric (second factor is presented to the hardware).

**Examples**: PIV card (FIPS 201), CAC, FIDO2 security key with PIN, YubiKey in FIDO2 mode with configured PIN, smart card

**Requirements**:
- PIN or biometric is presented directly to the hardware device (not the verifier)
- Hardware must verify the PIN/biometric before releasing the key operation
- FIPS 140 Level 2 overall; Level 3 physical security (for AAL3)
- Verifier impersonation resistance: FIDO2 origin binding or TLS channel binding (for AAL3)

**AAL eligibility**: AAL2 and AAL3

---

## Authenticator Binding and Enrollment

### Initial Binding
At enrollment, the authenticator is bound to the subscriber's identity record. Requirements:
1. Binding must occur in person, or via a secure binding ceremony using an existing, already-enrolled authenticator at the required AAL
2. The binding link (for a one-time enrollment URL) must have a short expiry (10 minutes or less) and be single-use
3. Binding confirmation must be sent to the subscriber's verified address

### Adding Additional Authenticators
When a subscriber with an existing authenticator wants to add another:
1. Reauthenticate with the existing authenticator at or above the required AAL
2. Verify identity if the new authenticator will replace the existing one (not just supplement it)
3. Issue confirmation to the verified address

### Authenticator Recovery
If all authenticators are lost:
- Identity reverification at the IAL of the original enrollment is required
- Recovery codes (look-up secrets) may have been issued at enrollment time
- KBA/KBV alone is NOT sufficient for account recovery at AAL2 or higher

### Authenticator Expiry and Revocation
- Hardware authenticators: must be revocable (CSP must be able to bind a revocation to the subscriber's account)
- Software authenticators: revocation via account disable or explicit de-binding
- PIV cards: revocation via the issuing agency CRL or OCSP

---

## Reauthentication Requirements — Full Table

| AAL | Inactivity Timeout | Absolute Time Before Reauthentication | Reauthentication Method |
|-----|------------------|--------------------------------------|------------------------|
| AAL1 | 30 days | No absolute limit | Any permitted AAL1 method |
| AAL2 | 30 minutes | 12 hours | Full AAL2 authentication (both factors) |
| AAL3 | 15 minutes | 12 hours | Full AAL3 authentication (hardware + PIN/biometric) |

For federated sessions:
- The RP sets session timeouts; the IdP sets federation session lifetimes
- RP may request fresh authentication assertions from the IdP at any time
- Passive reauthentication (where available in the protocol) does not reset the inactivity clock

---

## Verifier and CSP Security Requirements

### Verifier Requirements (applying to all AALs)
- Use approved cryptographic algorithms (FIPS-approved; CNSA algorithms for national security systems)
- Transmit authenticator output over approved-cryptography-protected channel (TLS 1.2+ required; TLS 1.3 recommended)
- Rate limit authentication attempts; implement lockout or exponential backoff
- Notify the subscriber of any authentication event (new device, unexpected location) via a separate channel
- For verified attributes, protect PII per applicable privacy regulations and SP 800-63A requirements

### CSP Requirements
- Store all authenticator secrets using salted cryptographic hashes
- Protect CSP private keys at the same FIPS 140 level as required by the AAL
- Conduct regular audits of authenticator binding and lifecycle events
- Operate a revocation service accessible to relying parties

---

## Commonly Used Authenticator Combinations by Use Case

| Use Case | Recommended Authenticator(s) | AAL |
|----------|------------------------------|-----|
| Consumer web application (low risk) | Password | AAL1 |
| Consumer web app (personal data access) | Password + TOTP app | AAL2 |
| Enterprise app (moderate risk) | Password + hardware FIDO2 key (PIN) | AAL2 |
| Federal employee access to non-HVA system | PIV card | AAL2/3 |
| Federal employee access to HVA system | PIV card (contact interface) with TLS binding | AAL3 |
| Mobile device access (federal employee) | PIV-D (Derived PIV) + biometric on device | AAL2 |
| Developer API access | OAuth 2.0 token (short-lived) + client certificate | AAL2 |

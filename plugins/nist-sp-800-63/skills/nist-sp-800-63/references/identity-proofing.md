# Identity Proofing Reference — NIST SP 800-63A Rev 3

Source: NIST SP 800-63A Revision 3 (June 2017), errata March 2020

---

## Identity Proofing Overview

Identity proofing is the process by which a Credential Service Provider (CSP) collects and verifies information about a person to bind a real-world identity to a digital account. The strength of the proofing process determines the Identity Assurance Level (IAL).

**The three phases of identity proofing (SP 800-63A Section 4.2)**:
1. **Resolution**: Collect identifying attributes from the applicant and resolve them to a unique person
2. **Validation**: Validate the collected evidence as genuine and accurate
3. **Verification**: Verify that the validated identity belongs to the applicant in front of the CSP (binding)

---

## Evidence Types and Strength

SP 800-63A classifies identity evidence into four strength levels: Superior, Strong, Fair, and Weak. Weak evidence is not permitted at IAL2 or IAL3.

### Superior Evidence

Evidence is designated Superior if it:
- Is issued by a federal or state government agency
- Contains a photograph
- Includes a machine-readable zone (MRZ) or chip (RFID/contactless IC) with biographical and biometric data
- Uses protective printing features that resist tampering and counterfeiting
- Has a validity period that is currently unexpired

**Examples of Superior evidence**:
- US Passport or US Passport Card (with NFC chip)
- Foreign passport with MRZ (ICAO 9303 compliant)
- US Permanent Resident Card (Green Card) with RFID chip

### Strong Evidence

Evidence is designated Strong if it:
- Is issued by a government agency
- Contains a photograph
- May or may not contain machine-readable features
- Uses standard security printing features

**Examples of Strong evidence**:
- US Federal or State driver's licence (Real ID compliant or standard)
- US State identification card
- US Military ID card (DD Form 2 — active duty or retired)
- US Uniformed Services Privilege and Identification Card
- Employment authorisation document (Form I-766)
- Tribal identification card (government-issued)

### Fair Evidence

Evidence is designated Fair if it:
- Is issued by a government agency or a regulated entity
- Contains biographical attributes
- Does not necessarily contain a photograph

**Examples of Fair evidence**:
- Voter registration card
- US bank or financial institution account statement (less than 3 months old)
- Utility bill with name and address (less than 3 months old)
- Government-issued professional licence or certificate
- Mortgage or lease agreement (regulated entity)
- Social Security card (without photograph; used as Fair supporting document only)

### Evidence Combinations Required by IAL

| IAL | Minimum Evidence Combination |
|-----|----------------------------|
| IAL1 | No evidence required |
| IAL2 | 1 piece of Superior evidence; OR 1 piece of Strong evidence + 2 pieces of Fair evidence |
| IAL3 | 1 piece of Superior evidence AND a biometric comparison against the photo on that evidence using an authoritative database; OR 2 pieces of Strong evidence AND a biometric comparison |

---

## Evidence Validation

After collecting evidence, the CSP must validate its authenticity.

### Validation Methods

| Method | Description |
|--------|-------------|
| **Automated validation** | Machine-readable zone (MRZ) parsed and verified; chip data (e.g., ICAO 9303 NFC) read and verified; barcode on document read and compared to visual data |
| **Visual/physical inspection** | Trained operator examines security features: holograms, colour-shifting inks, raised printing, microprint, UV fluorescence |
| **Database lookup** | Check document data against issuing authority database: AAMVA (driver's licences), USPS (addresses), Social Security Administration (SSN verification) |
| **Third-party service** | Commercial KYC/identity document verification services (only when the service can demonstrate authoritative source access) |

### Required Validation at IAL2

- Check that the document is unexpired
- Validate that the data on the document is consistent (MRZ matches VIZ data)
- Verify against at least one authoritative source (e.g., AAMVA for driver's licences)
- Confirm no indicators of tampering or forgery

### Required Validation at IAL3

- All IAL2 requirements, plus:
- Physical inspection of security features by a trained representative
- Automated chip verification (for chipped documents)
- Comparison of photograph against biometric captured at time of proofing

---

## Identity Verification (Binding to the Real Person)

After validating evidence, the CSP must verify that the person presenting the evidence is the same person described in it.

### Verification at IAL2

**In-person:**
- A trained operator visually confirms the person matches the photograph on the evidence
- The operator confirms liveness (the person is physically present)

**Supervised remote (via video):**
- A trained operator on a live video link confirms the person matches the photograph on evidence shown to the camera
- Liveness checks (following the person's movements, asking them to show multiple angles) performed
- Document is verified in real-time via automated scanning if possible

**Biometric comparison (optional at IAL2):**
- Facial image captured and compared against authoritative source (passport photo, DMV photo) via verified biometric matching algorithm
- If biometric match fails, the proofing session must be terminated

### Verification at IAL3

- In-person only with a trained, authorised operator
- Physical presence confirmed
- Biometric comparison required (fingerprint or facial image) against an authoritative biometric database
- CSP operator records the proofing event with date, operator ID, and outcome

---

## Address Confirmation

After successful validation and verification, the CSP must confirm the applicant's address.

### Purpose
Ensures that the person who appeared for proofing also controls the physical address associated with the identity.

### Methods

| Method | Description | IAL Applicability |
|--------|-------------|-------------------|
| Enrollment code by postal mail | CSP sends a code to the validated address of record; applicant enters the code to complete enrollment | IAL2 (required if proofing done remotely and address not confirmed via authoritative source) |
| USPS NCOA lookup | CSP queries USPS National Change of Address for the address associated with the identity; confirms address is current | IAL2 (supplemental) |
| In-person address confirmation | Address is confirmed by the operator matching address on physical evidence to applicant's statement | IAL2 and IAL3 (in-person only) |

**Enrollment code requirements (postal mail)**:
- Minimum 6 characters, randomly generated
- Valid window: up to 5 days after mailing
- Single-use: invalidated after entry
- Only one pending enrollment code at a time per applicant

---

## Knowledge-Based Verification (KBV) Limitations

KBV (also called KBA — Knowledge-Based Authentication) uses questions derived from personal history or credit bureau records ("What was your first car?", "Which of the following streets have you lived on?").

### SP 800-63A KBV Restrictions

| Requirement | Detail |
|------------|--------|
| Standalone use | KBV alone is NOT sufficient for IAL2 — it may only supplement other proofing steps |
| Static KBV | Prohibited at any IAL (static questions like "What is your mother's maiden name?" are deprecated) |
| Dynamic KBV | Permitted only as supplementary step at IAL2; minimum 4 questions with at most 1 wrong answer permitted |
| Waiting period after failure | If KBV fails: 2 weeks before retry; maximum 3 attempts total |
| Application of KBV | Should only be used when in-person or supervised remote proofing is genuinely impractical; not a default substitution |

---

## Proofing and Privacy

SP 800-63A requires CSPs to minimise PII collection:

| Principle | Requirement |
|-----------|------------|
| Data minimisation | Collect only the attributes necessary to complete proofing and bind the identity; do not retain evidence images beyond what is necessary |
| Notice | Inform applicants what data is collected, why, how it is stored, and who it is shared with |
| Use limitation | PII collected during proofing must not be used for any purpose other than identity proofing, authentication, and authorisation |
| Retention limits | Evidence images: CSP should determine minimum necessary retention period; raw biometrics: retain only as long as enrollment binding requires |
| Third-party sharing | CSP must not share PII collected during proofing with other agencies or commercial entities unless required by law, and without subscriber consent |

---

## Failed Identity Proofing

If identity proofing fails:

| Scenario | Required Action |
|---------|----------------|
| Document verification fails (suspected forgery) | Terminate session; do not inform the applicant of specific failure reason (to prevent social engineering); report to appropriate authority if fraud suspected |
| Biometric comparison fails | Up to 3 attempts; if all fail, terminate session; offer alternative in-person proofing channel |
| KBV fails | 2-week waiting period; maximum 3 total attempts |
| Applicant withdraws | Terminate session; purge all PII collected during the session per retention policy |

---

## Special Proofing Scenarios

### Remote Proofing for Mobile Applicants

For supervised remote proofing via mobile device:
- Document scanning may use the device camera; all scanned images must be transmitted only over TLS-protected channels
- Liveness detection algorithm must be used or the live operator must assess liveness via video
- The operator must be able to ask the applicant to perform physical tasks to confirm liveness (look left/right, hold document next to face)

### Proofing Minors

SP 800-63A does not provide specific minor-proofing requirements; agencies must comply with COPPA (Children's Online Privacy Protection Act) and any applicable state laws when proofing minors. In practice, many federal programmes require the legal guardian to complete identity proofing on behalf of a minor.

### Proofing for People Without Government-Issued ID

Where an applicant cannot provide Superior or Strong evidence, CSPs may:
- Accept a combination of authoritative documents sufficient to meet Fair evidence thresholds
- Use IAL1 if the service can be delivered without identity proofing
- Offer alternative access channels (in-person at a field office) if the agency can perform a different proofing exception process
- Note: There is no "equivalency" exception in SP 800-63A; the evidence requirements are normative

---

## Notification of Proofing

After successful proofing, the CSP must send a notification to the applicant at the verified address (postal or email, as appropriate):
- Confirm that identity proofing was completed
- Provide a means for the applicant to report if they did not initiate the proofing
- Include a reference number for the enrollment event

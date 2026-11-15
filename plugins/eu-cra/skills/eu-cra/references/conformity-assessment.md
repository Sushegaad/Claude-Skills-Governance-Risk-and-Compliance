# EU CRA - Conformity Assessment, CE Marking & Market Surveillance

## Table of Contents
1. [Conformity Assessment Routes by Product Class](#conformity-assessment-routes)
2. [Module A - Self-Assessment](#module-a--self-assessment)
3. [Notified Body Assessment (Class I option / Class II mandatory)](#notified-body-assessment)
4. [Technical Documentation (Annex VII)](#technical-documentation-annex-vii)
5. [EU Declaration of Conformity (Annex V)](#eu-declaration-of-conformity)
6. [CE Marking Rules](#ce-marking-rules)
7. [No EU Database Registration](#no-eu-database-registration)
8. [Market Surveillance](#market-surveillance)
9. [Penalties (Article 64)](#penalties-article-64)
10. [CRA Harmonised Standards and Guidance](#harmonised-standards-and-guidance)

---

## Conformity Assessment Routes

| Product Class | Permitted Routes | Decision Authority |
|---|---|---|
| **Default** (all others) | Module A self-assessment only | Manufacturer |
| **Class I** (Annex III, important products, 19 categories) | Module A self-assessment OR Notified Body (manufacturer chooses) | Manufacturer |
| **Class II** (Annex III, important products, 4 categories) | **Mandatory Notified Body** assessment | Notified Body + Manufacturer |
| **Critical** (Annex IV, critical products, 3 categories) | May be made subject to **mandatory EU cybersecurity certification** | Certification scheme + Manufacturer |

### Important: Harmonised Standards
Where **EU harmonised standards** covering the CRA's essential requirements have been adopted and published in the Official Journal, manufacturers who comply with those standards benefit from a **presumption of conformity** with the corresponding requirements. This simplifies the conformity assessment process significantly. ENISA and the standardisation bodies (CEN/CENELEC, ETSI) are developing standards aligned with CRA requirements. Key candidates include ETSI EN 303 645 (consumer IoT), IEC 62443 series (industrial), and EN ISO/IEC 27001 (ISMS).

---

## Module A - Self-Assessment

**Applicable to:** Default products; Class I products (manufacturer's choice).

**Steps:**
1. **Design and conduct internal testing** - test the product against all Annex I Part I and Part II requirements.
2. **Prepare technical documentation** (Annex VII) - see below.
3. **Review and internal approval** - senior technical officer or equivalent signs off on conformity.
4. **Draw up EU Declaration of Conformity** (DoC) - see below.
5. **Affix CE marking** to product, packaging, or accompanying documents.
6. **Retain** technical documentation and DoC for 10 years.

**No Notified Body involvement required under Module A.**

**Important:** Self-assessment is not self-certification without evidence. The manufacturer must have genuine technical evidence that requirements are met. Regulators and market surveillance authorities can request and inspect the documentation at any time.

---

## Notified Body Assessment

**Applicable to:** Class II products (mandatory); Class I products (manufacturer's option).

### What is a Notified Body (NB)?
A Notified Body is a **conformity assessment body (CAB)** that has been accredited by a national accreditation body (e.g., DAkkS in Germany, UKAS in UK/equivalent EU) and formally notified to the European Commission. NBs are listed in the NANDO database (New Approach Notified and Designated Organisations).

**NB designation for CRA:** Chapter IV (Arts. 35–51, notified bodies) applies
from **11 June 2026**. **11 December 2026** is only the Art. 35(2) target date
by which Member States are to strive to have a sufficient number of notified
bodies available. Full application of the CRA follows on 11 December 2027.

### Assessment process (simplified):
1. **Manufacturer prepares** complete technical documentation and application dossier.
2. **NB reviews documentation** - completeness check; requests any missing information.
3. **Technical examination** - NB performs or commissions testing against Annex I requirements; may audit the manufacturer's development and vulnerability handling processes.
4. **Assessment report** - NB issues a positive or conditional assessment report.
5. **Certificate of conformity** - NB issues an EU-type examination certificate (if applicable) or confirms conformity.
6. **Manufacturer draws up DoC** referencing the NB assessment.
7. **Affix CE marking** and NB's four-digit identification number (e.g., CE 1234).
8. **Surveillance** - NB may require periodic surveillance assessments for Class II products.

### Selecting a Notified Body
- Confirm the NB is listed on NANDO for the relevant CRA module and product category.
- Assess the NB's technical competence in cybersecurity and your product type.
- Consider geographic location, language, and typical assessment timelines (6–18 months for complex Class II).
- Request a preliminary assessment meeting to scope the engagement.

---

## Technical Documentation (Annex VII)

Technical documentation must demonstrate that the product meets all Annex I essential requirements. It must be drawn up in one of the official languages of the EU member states where the product is placed or made available.

**Required contents:**

1. **General product description:**
   - Product name, type, and version(s)
   - Intended use and foreseeable misuse
   - Unique product identifier (model, batch, serial, or version)

2. **Design and development documentation:**
   - Software architecture and data flow diagrams
   - Network connectivity diagram (interfaces, protocols, ports)
   - Cryptographic measures used (algorithms, key lengths, key management)
   - Authentication and access control mechanisms
   - Software components list (SBOM or equivalent)

3. **Cybersecurity risk assessment:**
   - Threat model - assets, threat actors, attack vectors
   - Risk analysis methodology used (e.g., STRIDE, TARA, IEC 62443-3-2)
   - Risk treatment decisions for each identified risk
   - Residual risks and accepted risks

4. **Implementation of essential requirements:**
   - For each Annex I Part I requirement: the technical measure(s) implemented
   - For each Annex I Part II requirement: the process/policy in place

5. **Test reports and evidence of conformity:**
   - Results of security testing (penetration testing, vulnerability scanning, fuzz testing)
   - Evidence of secure coding practices (SAST/DAST results, code review reports)
   - Authentication and encryption testing results

6. **Vulnerability handling policy:**
   - Published VDP/CVD policy URL
   - Internal process documentation
   - SBOM maintenance process

7. **EU Declaration of Conformity** (copy)

8. **Harmonised standards or technical specifications applied:**
   - List of standards used and the specific sections relevant to each requirement

**Retention period:** 10 years from the date the product is placed on the EU market (or last day of availability if withdrawn earlier).

---

## EU Declaration of Conformity (Annex V)

The DoC is the manufacturer's formal declaration that the product meets all applicable CRA requirements. It must contain:

1. **Product identification:** name, type, model/version, batch or serial number range
2. **Manufacturer information:** name, registered trade name, address
3. **This Declaration of Conformity is issued under the sole responsibility of:** [manufacturer name]
4. **Object of declaration:** [product name and function description]
5. **Statement:** "The object of the declaration described above is in conformity with Regulation (EU) 2024/2847 of the European Parliament and of the Council (Cyber Resilience Act)"
6. **References to any relevant harmonised standards or technical specifications** applied
7. **References to Notified Body** (if applicable): NB name, identification number, and certificate number
8. **Signed by or on behalf of:** name, title, date and place of signing, signature

**The DoC must be available in or translated into the language(s) required by the member state(s) where the product is placed on the market.**

---

## CE Marking Rules

### General requirements
- CE marking must be **affixed by the manufacturer** (or the authorised representative under the manufacturer's instructions)
- The letters "CE" must have a specific proportional form (per Annex IX of the NLF Regulation)
- Minimum height: **5 mm** (unless product size makes this impossible)
- The CE marking must be **visible, legible, and indelible**
- If CE marking is reduced or enlarged, the proportions of the CE symbol must be maintained

### Where to affix
1. On the **product itself** (preferred)
2. On the **product's packaging**
3. On a **label** attached to the product
4. On **accompanying documentation** (only if the product's nature makes it impossible to affix on the product or packaging)

### CE marking for Class I and II with Notified Body
- The NB's **four-digit identification number** must be affixed immediately after the CE marking
- The NB number is assigned by the European Commission when the NB is notified
- Format: CE [space] [NB number] - e.g., CE 1234

### What CE marking certifies under CRA
- The product meets all **essential cybersecurity requirements** of Annex I
- Appropriate **conformity assessment** has been performed
- **Technical documentation** is prepared and available
- **EU Declaration of Conformity** has been drawn up

### What CE marking does NOT certify under CRA
- Ongoing security of future software updates (vulnerability handling is ongoing)
- That the product has no vulnerabilities - only that known exploitable vulnerabilities were absent at time of market placement

---

## No EU Database Registration

The CRA contains **no product registration database obligation**. Conformity is
demonstrated through the **EU Declaration of Conformity (DoC)** and **CE
marking**, supported by the technical documentation. The only registration-like
duty under the CRA is the use of the **ENISA single reporting platform** for
Article 14 reports (actively exploited vulnerabilities and severe incidents).

---

## Market Surveillance

### Market Surveillance Authorities (MSAs)
- Each EU member state designates one or more MSAs responsible for CRA enforcement
- MSAs are typically existing national product safety or cybersecurity regulators (e.g., BSI in Germany, ANSSI in France)
- ENISA plays a coordinating role and supports MSAs with technical expertise

### MSA powers
- Request and inspect technical documentation and DoC
- Order testing of products
- Withdraw or restrict products from the market that pose unacceptable risk
- Order corrective actions, recalls, or destruction of non-compliant products
- Impose administrative penalties

### Safeguard clause
If a national MSA finds a product presents an unacceptable cybersecurity risk, it may take provisional measures to restrict, recall, or withdraw the product. Other member states and the Commission are notified through RAPEX (now ICSMS/Product Safety Pledge system).

### Timeline for manufacturers when non-compliance is identified
1. MSA notifies manufacturer of potential non-compliance
2. Manufacturer has opportunity to provide information and take corrective action
3. If non-compliance confirmed: MSA orders remediation within a specified period
4. If not remediated: MSA may impose penalties and/or order market withdrawal

---

## Penalties (Article 64)

### Administrative fines

| Infringement | Maximum Fine |
|---|---|
| Non-compliance with Annex I essential requirements (Part I or Part II) | **€15 million** or **2.5% of global annual worldwide turnover** of the preceding financial year, whichever is higher |
| Non-compliance with the other obligations listed in Art. 64(2) | **€10 million** or **2% of global annual worldwide turnover**, whichever is higher |
| Providing incorrect, incomplete, or misleading information to authorities | **€5 million** or **1% of global annual worldwide turnover**, whichever is higher |

### Proportionality factors (Article 64(6))
- Nature, gravity, and duration of the infringement
- Intentional or negligent character of the infringement
- Actions taken by the manufacturer to prevent or mitigate harm
- Degree of responsibility of the economic operator
- Cooperation with supervisory authorities
- Previous infringements
- Size and market share of the economic operator (SME/micro-enterprise protections)

### SME protections
- For SMEs (fewer than 250 employees, ≤€50M turnover or ≤€43M balance sheet total):
  - MSAs must take into account SME size and resources in penalty determination
  - Penalties must be proportionate and not jeopardise the SME's economic viability
  - Where possible, corrective action is preferred over immediately imposing maximum fines

### Criminal liability
- Member states may establish criminal liability for individuals (directors, officers) for serious CRA infringements. Article 64 does not exclude criminal prosecution under national law.

---

## Harmonised Standards and Guidance

### Standards expected to support CRA compliance
The European Commission will mandate standardisation bodies to develop CRA-aligned standards. Likely candidates:

| Standard | Relevance |
|---|---|
| **ETSI EN 303 645** | Consumer IoT cybersecurity - directly aligned with many Annex I Part I requirements |
| **IEC 62443 series** | Industrial automation and control system security |
| **ISO/IEC 27001:2022** | ISMS - supports organisational security governance |
| **IEC 62443-4-2** | Component security for OT products |
| **ETSI EN 303 645 + TS 103 701** | Assessment methodology for consumer IoT |
| **ISO/IEC 29147** | Vulnerability disclosure |
| **ISO/IEC 30111** | Vulnerability handling processes |
| **NIST SSDF (SP 800-218)** | Secure software development framework - aligns with development obligations |

### ENISA guidance documents
- ENISA regularly publishes non-binding guidance on CRA implementation. Check enisa.europa.eu for:
  - CRA implementation guidelines
  - SBOM maturity guidance
  - Vulnerability handling good practices
  - Product security testing methodologies

### Relationship to RED delegated acts
The Radio Equipment Directive (RED) Article 3(3)(d)(e)(f) cybersecurity delegated acts overlap with CRA for network-connected radio equipment. The Commission will provide guidance on how compliance with RED cybersecurity requirements may be used as partial evidence of CRA conformity.

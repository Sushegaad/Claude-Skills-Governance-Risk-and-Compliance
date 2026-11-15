# EU CRA - Essential Requirements & Obligations Reference

## Table of Contents
1. [Annex I Part I - Security Properties of PDEs](#annex-i-part-i--security-properties)
2. [Annex I Part II - Vulnerability Handling](#annex-i-part-ii--vulnerability-handling)
3. [Product Categories - Annex III (Important Products: Class I and Class II)](#annex-iii--important-products-class-i-and-class-ii)
4. [Product Categories - Annex IV (Critical Products)](#annex-iv--critical-products)
5. [Support Period Obligations](#support-period-obligations)
6. [SBOM Requirements](#sbom-requirements)
7. [Vulnerability and Incident Reporting](#vulnerability-and-incident-reporting)
8. [Manufacturer Obligations Summary (Article 13)](#manufacturer-obligations-article-13)
9. [Importer Obligations (Article 19)](#importer-obligations-article-19)
10. [Distributor Obligations (Article 20)](#distributor-obligations-article-20)
11. [Open-Source Software Stewards](#open-source-software-stewards)

---

## Annex I Part I - Security Properties

Products with digital elements must be **designed, developed, and produced** to meet these essential requirements:

1. **No known exploitable vulnerabilities:** Products must be placed on the market without known exploitable vulnerabilities. Manufacturers must exercise due diligence in tracking and addressing vulnerabilities before release.

2. **Secure by default configuration:**
   - Minimal attack surface - functions and ports not required for the intended purpose must be disabled by default
   - Secure default settings - passwords, cryptographic keys, and authentication must not use factory defaults that are easily guessable or common across products
   - Users must be able to reset the product to a secure factory state

3. **Protection against unauthorised access:**
   - Appropriate authentication and access control mechanisms
   - Identity and access management based on the principle of least privilege
   - Where feasible: multi-factor authentication, cryptographic credentials

4. **Confidentiality - data protection:**
   - Personal and other sensitive data protected at rest and in transit using state-of-the-art encryption
   - Cryptographic best practices (no deprecated algorithms)

5. **Integrity - data and software protection:**
   - Unauthorised modification of data, firmware, or software detected and mitigated
   - Software and firmware updates must be cryptographically signed and the signature verified before installation
   - Secure boot mechanisms where applicable

6. **Data minimisation:**
   - Only personal data and other data necessary for intended function is processed
   - Privacy-by-design principles applied (GDPR Art. 25 alignment)

7. **Availability - resilience against DoS:**
   - Products must be designed to maintain availability of essential functions under denial-of-service attacks
   - Resilience and graceful degradation

8. **Limited negative impact on other devices or networks:**
   - Products must not be usable as attack vectors against other devices or networks
   - Network traffic generation must be limited to what is necessary

9. **Exploit mitigation mechanisms:**
   - State-of-the-art exploit mitigations (ASLR, stack canaries, NX/DEP, control-flow integrity) where feasible
   - Memory-safe programming practices or compensating controls

10. **Security information transparency:**
    - Users must receive adequate information about the product's security features, settings, and limitations
    - Contact details for vulnerability reporting published

---

## Annex I Part II - Vulnerability Handling

Annex I Part II contains **exactly 8 vulnerability-handling requirements**.
Manufacturers must put in place and document a **vulnerability handling policy
and process** covering:

1. **Identify and document vulnerabilities and components (SBOM):**
   - Maintain an inventory of software components in the product, including a
     machine-readable **Software Bill of Materials (SBOM)**
   - Proactively monitor for new CVEs and security advisories affecting integrated components

2. **Remediate vulnerabilities without delay:**
   - Vulnerabilities addressed without delay, including through **free security updates**
   - Document the remediation process and evidence of fix verification

3. **Test and review:**
   - Apply effective and regular tests and reviews of the security of the product

4. **Disclose fixed vulnerabilities:**
   - Publicly disclose information about fixed vulnerabilities once security
     updates are available

5. **Coordinated Vulnerability Disclosure (CVD) policy:**
   - Put in place and enforce a coordinated vulnerability disclosure policy
   - Publish the policy; provide a named point of contact (email, security
     advisory page, or bug bounty platform)

6. **Information-sharing facilitation:**
   - Facilitate the sharing of information about potential vulnerabilities in
     the product and its third-party components

7. **Secure update distribution:**
   - Provide mechanisms to securely distribute updates (signed updates,
     integrity verification)

8. **Free, timely security updates:**
   - Disseminate security updates free of charge and without delay; security
     patches must be available independently of feature updates

**Not Annex I Part II:** The 24h/72h reporting of actively exploited
vulnerabilities and severe incidents is an **Article 14** obligation (24-hour
early warning, 72-hour notification, final report); see the Vulnerability and
Incident Reporting section below. Support-period and end-of-life duties sit in
**Article 13 and Annex II**.

---

## Annex III - Important Products (Class I and Class II)

Annex III lists the **important products with digital elements**, divided into
Class I and Class II.

### Class I - 19 categories

Class I products may use self-assessment or a Notified Body (manufacturer's
choice). The 19 categories are:

1. Identity management and privileged access management (PAM) systems
2. Standalone and embedded browsers
3. Password managers
4. Anti-malware software
5. VPN products
6. Network management systems
7. Security information and event management (SIEM) systems
8. Boot managers
9. PKI and digital certificate software
10. Network interfaces
11. Operating systems
12. Routers, modems, and switches
13. Microprocessors with security functionalities
14. Microcontrollers with security functionalities
15. ASICs and FPGAs with security functionalities
16. Smart home virtual assistants
17. Smart home security products
18. Connected toys with interaction features
19. Personal wearables with health monitoring

### Class II - 4 categories

Class II products require **mandatory Notified Body assessment**. The 4
categories are:

1. Hypervisors and container runtime systems
2. Firewalls, intrusion detection and prevention systems
3. Tamper-resistant microprocessors
4. Tamper-resistant microcontrollers

---

## Annex IV - Critical Products

Annex IV lists the **critical products with digital elements** (3 categories).
Critical products can be made subject to **mandatory EU cybersecurity
certification**:

1. Hardware devices with security boxes
2. Smart meter gateways
3. Smartcards or similar devices, including secure elements

---

## Support Period Obligations (Article 13 / Annex II)

### Minimum support period
- **At least 5 years** from the date the product is placed on the market, or the expected product lifetime if shorter than 5 years
- The support period must be **clearly communicated** to users before purchase (in product description, packaging, or documentation)

### During the support period
- Provide free security updates in a timely manner
- Security updates must not reduce or degrade product functionality or security posture
- Maintain and update the SBOM

### End of support
- Notify users at least **1 year before end of security support**
- Provide a final cumulative security update where technically feasible
- Cease making the product available on the EU market if unable to fulfil support obligations (or provide an adequate alternative)
- Document the end-of-support decision in the technical file

### Multi-component products
- If the product integrates a software component with a shorter support lifecycle, the product's support period is limited accordingly, OR the manufacturer must provide alternative components or patches independently

---

## SBOM Requirements

### What is required
- A **machine-readable SBOM** must be available on request to national market surveillance authorities
- Minimum content:
  - Product name and version
  - For each component: component name, version, supplier/author, licence
  - Dependency relationship (top-level dependencies at minimum)
- The SBOM must be kept **current** throughout the support period

### Recommended formats
- **SPDX** (ISO/IEC 5962:2021) - widely used, standardised
- **CycloneDX** - security-focused, supports VEX (Vulnerability Exploitability eXchange)
- JSON or XML formats preferred for machine readability

### VEX (Vulnerability Exploitability eXchange)
- Not mandated but strongly recommended as a complement to SBOM
- VEX documents allow manufacturers to communicate whether a specific CVE affects a specific product version
- Reduces false positives for customers and authorities scanning the SBOM against vulnerability databases

### SBOM governance
- Assign ownership of SBOM maintenance to a named team
- Integrate SBOM generation into the CI/CD pipeline (automated tooling: SPDX tools, Syft, Trivy, etc.)
- Review and update SBOM with each release and when third-party components are updated

---

## Vulnerability and Incident Reporting (Article 14)

### Reporting recipients
- **ENISA** (EU Agency for Cybersecurity) - central reporting point; ENISA forwards to national CSIRTs
- **National CSIRT** - member state's designated CSIRT (e.g., BSI/CERT-Bund in Germany, ANSSI in France, NCSC in Netherlands/UK-equivalent)
- **Affected users** - direct notification where feasible

### Actively exploited vulnerability
| Timeframe | Action |
|---|---|
| T+24 hours | Early warning to ENISA: vulnerability identifier, affected product versions, brief description |
| T+72 hours | Full notification: nature of vulnerability, CVSS/severity, affected versions, workarounds, remediation status |
| T+14 days after fix | Final report: fix details, patch release notes, lessons learned |

### Severe security incident
| Timeframe | Action |
|---|---|
| T+24 hours | Early warning to ENISA and national CSIRT |
| T+72 hours | Full incident notification |
| T+1 month | Post-incident report |

### What triggers reporting
- **Actively exploited vulnerability:** A vulnerability in the product that the manufacturer becomes aware is being actively exploited in the wild (confirmed or credible intelligence)
- **Severe incident:** A security incident that has, or could have, significant impact on the product's security or availability at scale (e.g., supply chain compromise, cryptographic key exposure, large-scale unauthorised access)

---

## Manufacturer Obligations (Article 13)

Manufacturers must:
1. Design, develop, and produce PDEs in accordance with Annex I essential requirements
2. Conduct a cybersecurity risk assessment before placing on market
3. Prepare technical documentation (Annex VII) and retain for 10 years
4. Conduct conformity assessment (Module A self-assessment or Notified Body)
5. Draw up EU Declaration of Conformity (Annex V) and retain for 10 years
6. Affix CE marking
7. Apply vulnerability handling obligations continuously throughout the support period
8. Report actively exploited vulnerabilities and severe incidents to ENISA/CSIRTs (Article 14, via the ENISA single reporting platform)
9. Ensure products distributed in the EU have a point of contact address
10. Cooperate with market surveillance authorities
11. Take corrective action if product is non-compliant; issue recall if necessary

---

## Importer Obligations (Article 19)

Importers must:
1. Only place on the EU market products accompanied by a valid DoC and technical documentation
2. Verify CE marking is affixed and legible
3. Verify the manufacturer is identified on the product
4. Add their own name, registered trade name or mark, and postal/electronic address
5. Ensure the product has vulnerability reporting contact information in a Union language
6. Not place on market products known to be non-compliant
7. Notify the manufacturer and market surveillance authority if a product poses a risk
8. Retain copies of DoC and technical documentation for 10 years
9. Cooperate with market surveillance authorities

---

## Distributor Obligations (Article 20)

Distributors must:
1. Verify CE marking, DoC availability, and instructions/information in a Union language
2. Not make available products known to be non-compliant
3. Notify the manufacturer and market surveillance authority of risks
4. Cooperate with market surveillance authorities on request

---

## Open-Source Software Stewards

**Definition:** Entities that provide sustained support for open-source software components that are incorporated into PDEs on a commercial basis (e.g., foundations, companies maintaining widely-used open-source libraries).

**Light-touch obligations (compared to manufacturers):**
- Publish and maintain a **cybersecurity policy** covering vulnerability handling and coordinated disclosure
- Cooperate with market surveillance authorities when requested
- Forward security vulnerability information to affected downstream users
- **Not required** to conduct full conformity assessment or affix CE marking
- Must provide technical documentation to authorities on request

**Note:** Individual open-source contributors who do not monetise or commercially support their software are **not** covered by CRA.

---

## Art. 14 Reporting - Operational Since September 11, 2026

Reporting obligations are **in force** and the **ENISA Single Reporting Platform (SRP)** is live (launched September 11, 2026; portal.cra-srp.enisa.europa.eu). File the 24h early warning / 72h notification / final report (14 days post-corrective-measure for exploited vulnerabilities; 1 month post-72h-notice for severe incidents) through the SRP to the CSIRT Designated as Coordinator of the main-establishment Member State, with simultaneous availability to ENISA. Assigned-Representative registration uses EU Login with MFA; CSIRT validation runs in parallel (up to 20 notifications pre-verification). If the platform is temporarily down, contact the CSIRT directly and re-file via the SRP once restored. Applies to products already on the market (awareness-based clock); OSS stewards join December 11, 2027.


# NZISM - Verified Control IDs

Verified control identifiers for citation in answers. Format: `chapter.section.control.C.nn`. Source: official NZISM (nzism.gcsb.govt.nz) chapter structure as mapped in the AWS Config NZISM 3.8 conformance pack (control names cross-checked against the manual's section titles). **Cite only IDs from this list; for topics not covered here, cite the chapter/section and direct the agency to confirm the current control number in the online manual** - the NZISM is updated roughly twice a year (v3.9 renamed Chapter 16 to "Authentication and Access Controls" and added new controls, e.g., 16.1.25.C.01, 16.1.27.C.02, 16.1.31.C.01–03 for passwordless and phishing-resistant MFA).

## Chapter 16 - Access Control and Passwords (v3.9: Authentication and Access Controls)

| Control ID | Section | Control name |
|---|---|---|
| 16.1.25.C.01 | 16.1 Identification, Authentication and Authorisation | Authentication methods (v3.9 control supporting passwordless and phishing-resistant MFA) |
| 16.6.6.C.02 | 16.6 Event Logging and Auditing | Maintaining system management logs |
| 16.6.10.C.02 | 16.6 Event Logging and Auditing | Additional events to be logged |
| 16.6.12.C.01 | 16.6 Event Logging and Auditing | Event log protection (integrity, tamper-evidence) |
| 16.6.13.C.01 | 16.6 Event Logging and Auditing | Event log archives (retention) |

> **Removed in v3.9 (do not cite):** 16.1.46.C.02 (suspension of access) was removed; its content was folded into 16.1.42.C.01. 16.3.5.C.02 (use of privileged accounts) was removed; it was merged into 16.3.5.C.01.

## Chapter 17 - Cryptography

| Control ID | Section | Control name |
|---|---|---|
| 17.1.53.C.04 | 17.1 Cryptographic Fundamentals | Reducing storage and physical transfer requirements (encryption at rest) |

## Chapter 18 - Network Security

| Control ID | Section | Control name |
|---|---|---|
| 18.4.9.C.01 | 18.4 Intrusion Detection and Prevention | IDS/IPS maintenance |
| 18.4.11.C.01 | 18.4 Intrusion Detection and Prevention | Configuring the IDS/IPS |
| 18.4.12.C.01 | 18.4 Intrusion Detection and Prevention | Event management and correlation |

## Chapter 19 - Gateway Security

| Control ID | Section | Control name |
|---|---|---|
| 19.1.12.C.01 | 19.1 Gateways | Configuration of gateways (deny-by-default, no public exposure) |
| 19.1.14.C.02 | 19.1 Gateways | Demilitarised zones |

## Chapter 20 - Data Management

| Control ID | Section | Control name |
|---|---|---|
| 20.3.7.C.02 | 20.3 Content Filtering | Content validation |
| 20.4.4.C.02 | 20.4 Databases | Database files (protection/encryption) |
| 20.4.5.C.02 | 20.4 Databases | Accountability (database audit logging) |

## Chapter 22 - Enterprise Systems Security

| Control ID | Section | Control name |
|---|---|---|
| 22.1.23.C.01 | 22.1 Cloud Computing | System availability |

## Usage in answers

- **Access Control Policy**: cite 16.1.25.C.01 (authentication methods), 16.1.42.C.01 (access suspension; absorbed the former 16.1.46.C.02 in v3.9), 16.3.5.C.01 (privileged accounts; the former 16.3.5.C.02 was merged into it in v3.9), 16.6.6.C.02/16.6.10.C.02 (logging of access events), plus Chapter 16.1 (Identification, Authentication and Authorisation) generally for identification/authentication/MFA requirements.
- **Logging/monitoring requirements**: 16.6.6.C.02, 16.6.10.C.02, 16.6.12.C.01, 16.6.13.C.01.
- **Cloud/offshore hosting**: 22.1.23.C.01 plus Chapter 22.1 generally; pair with the PSR and cloud risk assessment process.
- **Network/perimeter**: 18.4.x (IDS/IPS), 19.1.12.C.01, 19.1.14.C.02.

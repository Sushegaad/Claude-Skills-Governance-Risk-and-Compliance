# EU AI Act — Article 5: Prohibited AI Practices

**Regulation (EU) 2024/1689, Article 5**
**Applicable from: 2 February 2025**

This reference covers all eight categories of AI practices prohibited under Article 5 of the EU AI Act. These are practices classified as posing unacceptable risk. Any AI system falling into these categories must not be placed on the EU market, put into service, or used in the EU.

---

## Overview

Article 5 prohibits the placing on the market, putting into service, or use of AI systems that deploy specific high-risk techniques or serve specific harmful purposes. Violations carry the highest penalty tier: up to **€35 million or 7% of global annual turnover**, whichever is higher (Art. 99(3)).

The eight prohibited categories are:

---

## Category 1 — Subliminal, Manipulative, or Deceptive Techniques (Art. 5(1)(a))

**Prohibited:** AI systems that deploy subliminal techniques beyond a person's consciousness, or purposefully manipulative or deceptive techniques, with the objective or effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them or another person significant harm.

**Key elements that must ALL be present for the prohibition to apply:**
- The technique operates below the threshold of consciousness (subliminal) OR is deliberately manipulative/deceptive
- The objective or effect is to materially distort the person's behaviour
- This appreciably impairs the ability to make an informed decision
- Significant harm results or is likely to result (to the person or another person)

**Examples of potentially prohibited systems:**
- AI voice systems using imperceptible audio signals to induce purchasing decisions
- AI recommendation engines deliberately designed to exploit cognitive biases to drive harmful outcomes
- AI chatbots impersonating humans without disclosure to induce financial commitments

**What is NOT prohibited:**
- Legitimate advertising and marketing that uses evidence-based persuasion techniques without subliminal components
- AI systems that provide information enabling informed decision-making
- AI that nudges behaviour with full transparency and in a non-deceptive manner

---

## Category 2 — Exploitation of Vulnerabilities (Art. 5(1)(b))

**Prohibited:** AI systems that exploit any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability, or specific social or economic situation, with the objective or effect of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is likely to cause significant harm.

**Key elements:**
- Targets vulnerabilities arising from age (e.g., children, elderly), disability, or specific social/economic situation
- The exploitation has the objective or effect of materially distorting behaviour
- The distortion causes or is likely to cause significant harm

**Examples of potentially prohibited systems:**
- AI systems targeting children with manipulative dark patterns to induce in-app purchases
- AI debt collection systems targeting financially distressed individuals with psychologically manipulative messaging
- AI systems exploiting cognitive impairments of elderly users to obtain consent or financial commitments

**Relationship to Category 1:** The key distinction is that Category 1 focuses on technique (subliminal/deceptive), while Category 2 focuses on the target's vulnerability. An AI system can violate both simultaneously.

---

## Category 3 — Biometric Categorisation Inferring Sensitive Attributes (Art. 5(1)(c))

**Prohibited:** AI systems using biometric categorisation that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation.

**Scope:** Applies to AI systems that use biometric data to infer sensitive special category attributes.

**What biometric data is covered:** Any data processed through specific technical processing relating to physical, physiological, or behavioural characteristics of a natural person — including fingerprints, iris scans, facial geometry, gait, voice patterns.

**The prohibited inference categories:**
- Race or ethnic origin
- Political opinions
- Trade union membership
- Religious or philosophical beliefs
- Sex life or sexual orientation

**Exceptions (Art. 5(1)(c) proviso):**
- Lawful filtering or labelling of lawfully acquired biometric data sets — e.g., lawful research datasets that need to be sorted
- Law enforcement categorising biometric data in accordance with Union or Member State law

**What is NOT prohibited:**
- Biometric verification systems that confirm a person is who they claim to be (identity verification) — these are NOT categorisation systems
- Biometric identification systems that match an identity to a known identity — these are separately addressed as high-risk under Annex III, not prohibited

---

## Category 4 — Social Scoring (Art. 5(1)(d))

**Prohibited:** AI systems that evaluate or classify natural persons or groups of persons over a period of time based on their social behaviour or known, inferred, or predicted personal or personality characteristics, with a social score, the AI-based evaluation leading to either or both of the following:
- (i) Detrimental or unfavourable treatment of those natural persons or groups in social contexts that are unrelated or disproportionate to the context in which the data was originally generated or collected
- (ii) Detrimental or unfavourable treatment that is unjustified or disproportionate to the social behaviour or its gravity

**Key elements:**
- Evaluation conducted **over a period of time** (not single-event assessments)
- Based on **social behaviour** or **personal/personality characteristics** (known, inferred, or predicted)
- Leads to treatment that is either unrelated to the data's original context or disproportionate to the behaviour

**Examples of prohibited systems:**
- Citizen scoring systems that aggregate data from multiple life domains (financial, social, civic) to produce a general-purpose score affecting housing, travel, or services
- Insurance systems that persistently track social media behaviour across years to calculate premiums affecting unrelated services
- Employer AI systems that compile long-term personality assessments reducing job opportunities in unrelated fields

**What is NOT prohibited:**
- Credit scoring using solely financial behaviour data relevant to a financial service — this is separately regulated as high-risk under Annex III
- Risk assessment for specific, relevant and proportionate purposes (e.g., financial fraud detection)
- HR performance management systems assessing work-specific behaviour in proportion to employment context

---

## Category 5 — Criminal Risk Assessment Based Solely on Profiling or Personality Traits (Art. 5(1)(e))

**Prohibited:** AI systems that assess the risk of a natural person to commit criminal offences based solely on profiling of a natural person or assessing their personality traits and characteristics.

**The critical qualifier "solely":** This prohibition applies when the risk assessment is based **exclusively** on profiling or personality traits. AI that **augments** human assessment based on objective, verifiable facts directly linked to criminal activity is **not** prohibited.

**What is prohibited:**
- Predictive policing systems that identify individuals as criminal risks based solely on demographic profiling, social network analysis, or personality scores without objective factual basis
- Recidivism risk tools that score individuals based purely on personal characteristics (age, address, employment) without factual criminal behaviour evidence

**What is NOT prohibited:**
- Actuarial risk tools assessing recidivism risk that incorporate actual criminal history, behavioural observations during incarceration, and other objective verifiable facts — provided they do not rely **solely** on profiling
- AI systems assisting analysts by flagging patterns for human investigator review, where human investigators apply individual fact-based assessment

---

## Category 6 — Untargeted Facial Recognition Scraping (Art. 5(1)(f))

**Prohibited:** AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage.

**Key elements:**
- Applies to the **creation or expansion** of facial recognition databases
- Through **untargeted scraping** — without specific targets or selection criteria
- From **internet sources** or **CCTV footage**

**Why "untargeted" matters:** Targeted collection with lawful basis (e.g., collecting images of a known suspect with judicial authorisation) is not covered by this prohibition. The prohibition targets mass, indiscriminate collection building databases that could be used for surveillance.

**What is prohibited:**
- Commercial services that scrape public social media profiles to build facial recognition databases
- Law enforcement building general-purpose facial databases from CCTV footage without targeting specific investigations
- Academic research building large unlicensed facial datasets through automated web scraping

**Relationship to other prohibitions:** Real-time RBI (Category 8) uses such databases in operation. This prohibition attacks the database-building stage.

---

## Category 7 — Emotion Recognition in Workplace and Educational Institutions (Art. 5(1)(g))

**Prohibited:** AI systems used for making inferences about the emotional states of natural persons in the context of the workplace and educational institutions.

**Scope:** Covers AI systems that analyse facial expressions, voice, body language, or physiological signals to infer emotional states (e.g., stress, engagement, happiness, anxiety, attention).

**Contexts covered:**
- Workplaces in general — offices, manufacturing floors, remote working environments
- Educational institutions — schools, universities, training facilities

**The medical/safety exception (Art. 5(1)(g) proviso):** Emotion recognition AI deployed for medical purposes (e.g., detecting clinical depression, monitoring patient distress in healthcare) or safety purposes (e.g., detecting driver fatigue for road safety) is NOT prohibited.

**What is prohibited:**
- HR monitoring systems that analyse employees' facial expressions during work or video calls to assess productivity, engagement, or stress
- Proctoring software that uses emotion recognition to detect cheating or attention lapses in educational exams
- Recruitment AI that analyses candidates' emotional states during video interviews

**What is NOT prohibited:**
- Emotion recognition in clinical settings by authorised medical professionals
- Driver drowsiness detection systems in vehicles (safety purpose)
- Voluntary mental health monitoring apps used by individuals for their own benefit

---

## Category 8 — Real-Time Remote Biometric Identification (RBI) in Public Spaces for Law Enforcement (Art. 5(1)(h))

**Prohibited (with exceptions):** The use of real-time remote biometric identification systems in publicly accessible spaces for the purpose of law enforcement — except in three specific circumstances.

### Definitions relevant to this prohibition

**Remote biometric identification system:** An AI system for the purpose of identifying natural persons at a distance through the comparison of a person's biometric data with the biometric data contained in a reference database, and without prior knowledge of whether the targeted person will be present and can be identified (Art. 3(40)).

**Real-time:** The capturing and comparison of biometric data and the identification occur immediately or with minimal delay (contrasted with "post" RBI, which is not prohibited but is classified as high-risk).

**Publicly accessible spaces:** Physical locations accessible to the general public, regardless of ownership — including streets, shopping centres, airports, stadiums, public transport, private premises open to the public.

### The Three Permitted Exceptions (Art. 5(2))

Real-time RBI by law enforcement in publicly accessible spaces is permissible **only** in the following situations:

**Exception A — Missing persons and trafficking victims:**
Targeted search for specific victims of kidnapping, trafficking, or sexual exploitation, and the search for missing persons.

**Exception B — Specific, substantial, and imminent threat:**
Prevention of a specific, substantial, and imminent threat to life or safety of natural persons, or identified threat of a terrorist attack.

**Exception C — Serious crime investigation:**
Detection, localisation, identification, or prosecution of the perpetrator or suspect of a criminal offence referred to in Art. 5(2)(c) — serious crimes including murder, grievous bodily injury, rape, robbery, organised crime, illegal weapons trafficking, terrorism, environmental crime, cybercrime, trafficking, and sexual exploitation.

### Procedural Safeguards Required for Each Use

For each real-time RBI deployment under an exception:

1. **Prior authorisation** must be obtained from a judicial authority or an independent administrative authority of the Member State (Art. 5(3)(a))
   - Urgency exception: In duly justified cases of urgency, deployment may commence without prior authorisation, provided authorisation is requested without undue delay within 24 hours; if rejected, deployment must cease immediately and all data/results/outputs must be deleted

2. **Fundamental rights impact assessment** must be conducted and registered in the EU database before deployment (Art. 5(4))
   - Urgency exception: Registration may follow in duly justified urgent cases without undue delay

3. **Temporal, geographic, and personal limitations** must apply — use must remain limited to what is strictly necessary for the specific purpose

4. **Post-deployment reporting**: A report on deployment to be submitted to the relevant market surveillance authority and the data protection authority

### Member State legislation requirement

Member States wishing to use real-time RBI under exceptions must enact specific national legislation authorising such use (Art. 5(3)). The Commission must be notified. National legislation must include:
- Offences that justify use under Exception C
- Maximum time periods for use
- Geographic limitations
- A supervisory mechanism
- Accountability and liability mechanisms

---

## Enforcement Notes

**Competent authorities:** National market surveillance authorities and data protection authorities, depending on whether the system raises general AI Act or data protection concerns.

**Timeline:** Prohibited AI practices apply from **2 February 2025**. Any system deployed in the EU after this date that falls into these categories is in violation.

**Transitional period:** There is no transitional period for prohibited AI systems — unlike high-risk AI systems which have transition periods for existing systems.

**Interaction with GDPR:** Many prohibited AI practices also involve processing of biometric data (special category under GDPR Art. 9). Non-compliance with Article 5 of the EU AI Act may simultaneously constitute a GDPR violation. Competent authorities are expected to coordinate.

**Interaction with EU Charter of Fundamental Rights:** Recitals 29–42 make clear that the prohibitions are grounded in fundamental rights under the EU Charter — particularly dignity (Art. 1), prohibition of torture (Art. 4), privacy (Art. 7), data protection (Art. 8), non-discrimination (Art. 21).

---
organization: Artificial Intelligence Integration Center (AI2C)
software_name: mission-clock
software_version: v1.0.0
logo: docs/sdd/logo.png
classification: CUI
prepared_for:
  Organization: AI2C
  Name: CW3 Vic Fernandez III
  E-mail: victor.fernandez19.mil@army.mil
  Address: 6425 Living Place, Pittsburgh 15206
---

<!--
  NOTE: THIS MARKDOWN TEMPLATE IS NOT GITLAB FLAVORED, AND THUS WILL NOT RENDER CORRECTLY ON GITLAB IT IS DESIGNED TO BE RENDERED BY PANDOC INTO A PDF OR OTHER FORMAT. PLEASE REFER TO THE PANDOC DOCUMENTATION FOR MORE INFORMATION ON HOW TO DO THIS (https://pandoc.org/MANUAL.html#pandocs-markdown).

  THIS TEMPLATE IS DESIGNED TO BE USED WITH THE PANDOC CONTAINER IMAGE (https://code.code.cdso.army.mil/cdso/containers/tool/pandoc)

  THERE ARE PORTIONS OF THIS TEMPLATE THAT SERVE AS A FORM TO BE FILLED IN, AND OTHERS THAT ARE MEANT TO BE EDITED. PLEASE REFER TO THE COMMENTS IN THE TEMPLATE FOR MORE INFORMATION.

  THERE ARE ALSO PORTIONS THAT ARE FILLED OUT IN THEIR ENTIRETY AND ARE TARGETED FOR THE CDSO APPROVAL SYSTEM. DO NOT EDIT THESE UNLESS YOU HAVE A COMPELLING REASON TO OR ARE DEVIATING FROM THE CDSO PROCESS.
-->

<!--
 PORTION MARKINGS: You must use portion markings for all paragraphs and headers in this document. You must have specified the top-level classification of the SDD in the front-matter of this document (under the 'classification' key).

-->

## Classification Instruction

(U) Add the portion marking before each paragraph. This paragraph is marked as Unclassified, as denoted by the '(U)' at the beginning of this paragraph.

## Responsible Organization

(U) Who is the cognizant Authorizing Official (AO) for the organization?

Mr. Joseph Welch

(U) Is your system funded by Title 10 or Title 50?

| Title 10 | Title 50 |
| -------- | -------- |
| x        |          |

### Points of Contact

<!-- Refer to https://pandoc.org/MANUAL.html#tables for allowed table formats -->
<!-- We've provided the table below, but you can choose to provide this information in another format -->
<!-- At a minimum, you should provide a ISO/PM and an ISMM, but may also include a ISSOs -->
<!-- At a minimum, you should provide a Mission Owner, Mission Owner AO, ISO/PM and an ISMM, but may also include a ISSOs -->
<!-- Indicate whether your application is under Title 10 or Title 50 with an X in the appropriate section -->

| Name                     | Role                                | Phone Number   | Email                           |
| ------------------------ | ----------------------------------- | -------------- | ------------------------------- |
| LTC Scott Anderson       | Mission Owner                       | (978) 654-3210 | scott.t.anderson.mil@army.mil   |
| CPT Andre Michell        | Information System Owner            | (978) 654-3210 | andre.j.michell.mil@army.mil    |
| CW3 Victor Fernandez III | Information System Security Manager | (978) 654-3210 | victor.fernandez19.mil@army.mil |
| CW3 Jilly Gonzalez       | Information System Security Officer | (978) 654-3210 | jilly.m.gonzalez.mil@army.mil   |

```{=latex}
\newpage
```

## cDSO Container Technology Pipeline Process

(U) The cDSO is a low cost, secure, flexible, and enterprise-wide containerized application development pipeline. Using the cDSO improves the quality and timeliness of the Risk Management Framework (RMF) process. It distributes the responsibility for security while enabling developers at all levels and organizations to develop and secure containerized applications with unmatched agility.

### Process

a. (U) System Owner completes CSDD and BoE with Cybersecurity Office assistance

b. (U) Cybersecurity Office POC reviews BoE and sends it to ISSM.

c. (U) ISSM reviews BoE and sends it to SCA-V or returns for rework.

d. (U) SCA-V reviews BoE and signs approval or returns for rework.

e. (U) ISSM signs approval. ISSM enters approval in the GitLab Merge Request.

f. (U) SCA-V enters approval in the GitLab Merge Request and Merges the CSDD.

g. (U) Container Software/Pipeline can now be installed, and BoE is incorporated into System BoE

```{=latex}
\newpage
```

## Software Overview

### Purpose

(U) Tenant 0 uses Machine Learning to predict the species of an Iris flower based on the petal and sepal measurements given. Users can input measurements, select different classification models (like KNN, SVM, or Decision Tree), and visualize how each model makes predictions through dynamic 2D and 3D plots. Designed for students, educators, and data enthusiasts, Tenant 0 offers an intuitive way to explore ML concepts while classifying one of the most famous datasets in data science.

### Intended Users

a. (U) Administrators.

b. (U) Users.

### Identification

Clearly identify the type of software/pipeline to be used, all organizations that will use the software/pipeline, and the networks/domains on which the software/pipeline will be deployed

<!-- Fill in this form's header with your project info and with an 'X' where applicable -->

```{=tex}
\begin{center}
\begin{tabular}{|c|c|}
\hline
\textbf{Software Name} & <Application Name> \\
\hline
\textbf{Version}   & Version \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 & \textbf{Software Type}  \\
\hline
 & Commercial Off-the-Shelf (COTS)  \\
\hline
X & Government Off-the-Shelf (GOTS)  \\
\hline
 & Free and Open Source Software (FOSS)  \\
\hline
 & Contract-Developed / Modified Off-the-Shelf (MOTS)  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 & \textbf{Architecture}  \\
\hline
 & Installed on Desktop  \\
\hline
X & Application Server with Database  \\
\hline
 & Application Server with Persistent Storage  \\
\hline
\end{tabular}

% NOTE: Please specify as narrowly as possible the organization/group your users are a part in the table below
\begin{tabular}{|c|c|}
\hline
 & \textbf{Users of the Software}  \\
\hline
X & U.S. Army Cyber Command  \\
\hline
 & U.S. Army Cyber Command and other DoD organizations  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 & \textbf{Networks} \\
\hline
 & JWICS  \\
\hline
 & SIPRNET  \\
\hline
X & NIPRNET  \\
\hline
 & STEMSNET  \\
\hline
 & Stand-Alone (Name: )  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 & \textbf{Privacy Act Data} \\
\hline
 & "Business" or "Rolodex" PII  \\
\hline
 & PII  \\
\hline
 & PHI  \\
\hline
\end{tabular}
\end{center}
```

```{=latex}
\newpage
```

## Security Overview

### System Categorization

Security Categorization is the first step in the Risk Management Framework (RMF) and paramount because of its effect on all other steps in the framework, from selection of security controls to the level of effort required in assessing security control effectiveness. The Security Categorization will generally be determined based on the most sensitive or critical information collected by, consumed by, received by, processed in, stored in, and/or generated by the system/application.

**Security categorization of the system that is the consumer of this pipeline**:

<!-- Replace the space in between brackents with an 'x' to select your information category. -->
<!-- More information on information categories can be found in NIST FIPS PUB 199: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf -->

**Confidentiality**

- [x] LOW

- [ ] MODERATE

- [ ] HIGH

**Integrity**

- [x] LOW

- [ ] MODERATE

- [ ] HIGH

**Availability**

- [x] LOW

- [ ] MODERATE

- [ ] HIGH

<!-- (highest classification of data processing, regardless of which network it sits on) -->
<!-- Fill in with the appropriate items and / or add any that apply -->

```{=tex}
\begin{center}
\begin{tabular}{|c|c|}
\hline
 & \textbf{Anticipated Domain(s)} (CUI when filled out) \\
\hline
 & Unclass (IL2) (DEV)   \\
\hline
X & NIPRNet (IL5) (TEST, PROD)  \\
\hline
 & SIPRNet (DEV, TEST, PROD)  \\
\hline
 & JWICS (DEV, TEST, PROD)  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 & \textbf{Anticipated Dissemination Controls (SIPR)} (CUI when filled out) \\
\hline
 & NOFORN   \\
\hline
 & FRD  \\
\hline
 & NATO  \\
\hline
 & ORCON  \\
\hline
 & PROPIN  \\
\hline
 & RESEN  \\
\hline
 & REL TO USA, AUS, CAN, GBR  \\
\hline
 & REL TO USA, AUS, CAN, GBR, NZL  \\
\hline
 & Other: (Please specify)  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 & \textbf{Anticipated Dissemination Controls (JWICS)} (CUI when filled out) \\
\hline
 & SI-G   \\
\hline
 & TK  \\
\hline
 & HCS-P  \\
\hline
 & COMINT  \\
\hline
 & MASINT  \\
\hline
 & NATO  \\
\hline
 & REL TO USA, AUS, CAN, GBR \\
\hline
 & REL TO USA, AUS, CAN, GBR, NZL  \\
\hline
 & COMSEC  \\
\hline
 & Other: (Please specify)  \\
\hline
\end{tabular}
\end{center}
```

```{=latex}
\newpage
```

### Architecture Diagram

Here you should attach an application architecture diagram that shows the composition of your application, and how all of its components interact with one another. Please include data flows between your applications, inputs from other systems, and outputs to other systems. Ensure that you cover security relevant components within your architecture diagram in below sections. Reminder that your repo will be copied into the container that will be generating your CSDD PDF, so you should reference all files relative to the top-level directory of your repository.

The name in the square brackets represents the figure name, while the path in the parentheses should be the image you want to include. Please ensure that the data flows are clearly identified, as this is required by eMASS.

![Architecture Diagram](docs/sdd/architecture-diagram.png)

```{=latex}
\newpage
```

## Detailed Software Description

### Software Purpose / Goals

Give a detailed description of the mission-oriented purpose for the software. This section should not be overly technical in nature, but rather serves to give context for the gap the software is filling and should make a compelling case for it.

### Software Functionality

Describe how the software is going about achieving the aforementioned goals.

### Software Components

Describe each component of your software with a name, associated technology, and the function it serves. You can think of this section as accompanying the architecture diagram by effectively labelling each piece depicted therein.

### User Interface

Provide a description and / or example (screenshots, comparisons to existing UIs, etc.) of your software's user interface. This might be a Graphical User Interace (GUI), a Textual User Interface (TUI), or even a Command-Line Interface (CLI). Describe how the user is expected to interact with the software. How does the user interface with the capability? Do they PKI log in, use MFA, etc?

### Configuration Management

How the user is expected to manage configurations for your application. This could be via a configuration file (.ini, .toml, etc.), via environment variables, etc. Consider how users can manage multiple configurations flexibly and how users can rollback configurations.

### Development and Testing

Explain in detail your development methodology, process, and testing stack. This should include any relevant project management facilitation software or techniques, as well as what testing framework you intend to use.

#### Milestones

Explain how you are measuring progress for this application. These could be based on time, feature completion, or various other metrics. One approach might be to use the SMART framework, where you set Specific, Measurable, Achievable, Relevant and Time-bound goals.

#### Failure Conditions & Mitigations

Define failure and success for this project, and determine what foreseeable circumstances would lead to failure, and what mitigations can be emplaced to counteract these conditions or lessen the impact of such a failure. What happens when your capability fails? What is the plan to get it back? Think COOP or IR.

```{=latex}
\newpage
```

## Technical Overview

### Networking Capabilities

Describe in detail what networking requirements and capabilities are needed and produced by this software.

### Ports / Protocol / Services

Describe which ports, protocols, and services are used by this application. Describe under what conditions each will be used and the purpose for each. If not listed explicitly here, all other ports, protocols, and services will be assumed unneeded and thus unavailable in the application context.

### Encryption

Describe what encryption standards will be used. Specify your software components that will be using them, what purpose they serve, and how they will be used.

### Authentication

Describe what authentication scheme will be enforced and how you plan to do so.

### Operating System

What operating systems will your software be built to run on. You should specify the OS family, version, and architecture that your system is built to run on. It is your responsibility to ensure that any OS listed here is supported through your testing systems as well.

### Role-Based Access Control (RBAC)

List RBAC specifications and enforcement mechanisms.

<!-- START: DO NOT EDIT -->

### Audit Capabilities

This application uses the Continuous Integration (CI) services provided through Community DevSecOps (CDSO), which is an inner-sourced CI solution provided for use within the Department of the Army. The pipelines provided by CDSO are all open and auditable for anybody within the department of the Army. The source code for all components can be found here: <https://code.code.cdso.army.mil/cdso>. The documentation can be found here: <https://cdso.pages.code.cdso.army.mil/>.

### Dependencies

This application's dependencies can be viewed by looking at the pipeline artifacts for the most recent CI iteration under the `syft-grype` job artifacts.

This job produces a `syft.json` artifact which contains the Software Bill of Materials (SBOM) for the application image.

### Assumptions

List any assumptions made during the design of this application. This could include assumptions about the network or operating environment, assumptions about the end-user, etc.

```{=latex}
\newpage
```

## Constraints

List what constraints there are that affect this application in its design, implementation, deployment, etc.

### Scanning Tools & Remediation

This application uses all of the scanning tools as defined in the `application-security-review` Pipeline from CDSO. You can find details about the pipeline and its tools here: <https://cdso.pages.code.cdso.army.mil/components/pipelines/#application-security-reviewyml> .

Its definition can be found here: <https://code.code.cdso.army.mil/cdso/cdso/-/blob/main/pipelines/application-security-review.yml>.

<!-- END: DO NOT EDIT -->

### Security Technical Implementation Guides (STIGs)

```{=latex}
\newpage
```

# Appendix A -- References

List relevant sources that were referenced throughout the rest of the CSDD.

```{=latex}
\newpage
```

# Appendix B -- Acronyms

Make sure to add any acronyms used in this CSDD that are pertinent to your organization and application/pipeline.

| Acronym | Definition                                     |
| ------- | ---------------------------------------------- |
| CDSO    | Community DevSecOps                            |
| CI / CD | Continuous Integration / Continuous Deployment |

```{=latex}
\newpage
```

## SRG (Security Requirements Guide)

Add the following: List the SRG that is applicable to the system these containers/pipelines support.

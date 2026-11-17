# [Application Name] — Project Documentation

**Course:** [Software Engineering](https://www.fer.unizg.hr/predmet/proinz), Faculty of Electrical Engineering and Computing, University of Zagreb  
**Academic year:** [20XX/20XX]  
**Team:** [Team identifier and name]  
**Instructor:** Vlado Sruk  
**Assistant / Demonstrator:** [Name and role for this course offering]

## Project Overview

**Objective:** Let a first-time reader identify the application, its intended users, and its principal purpose in two or three sentences.

[Project description.]

<details>
<summary><strong>A concise project overview</strong></summary>

For a project on the Crisis Guard topic, a concise overview could identify citizens who need location-specific disaster information and the application's aim to present disaster reports on a map. Mention a feature only if it belongs to the team's approved task; do not claim that the application improves emergency response without evidence. This is an example of an informative overview, not text to copy or proof of a delivered feature.

</details>

**Application and basic setup:** [Repository README](../README.md#quick-start)  
**Public application:** see [README – Deployment](../README.md#deployment)

## Team Members and Roles

The maintained list of members, GitHub profiles, and their roles or principal contributions is in the [repository README](../#team-members).

## Documentation Index

| Page | Purpose |
| --- | --- |
| [1. Project Scope](1-Project-Scope.md) | Problem, objective, and boundary of the project |
| [2. Requirement Analysis](2-Requirements.md) | Requirements, constraints, and traceability |
| [3. Use Cases](3-Use-Cases.md) | Actors and representative user interactions |
| [4. Architecture and Design](4-Architecture-and-Design.md) | Main design decisions, structure, data, and behavior |
| [5. Testing](5-Testing.md) | Test approach, actual results, and known defects |
| [6. Deployment, Installation, and Configuration](6-Deployment-Installation-and-Configuration.md) | Local installation, configuration, public deployment, and administration |
| [7. Conclusion and Future Work](7-Conclusion-and-Future-Work.md) | Conclusion and Future Work |
| [A. Overview of Group Activities](A-Overview-of-Group-Activities.md) | Team activities, contributions, and challenges. |

## Project Milestones

| Checkpoint | Demonstration | Video |
| --- | --- | --- |
| Week 7 — first review | [Link to the demonstration or project version] | [Demo 1 video link, if recorded] |
| Week 14 — final review | [Link to the final demonstration or project version] | [Final demo video link, if recorded] |

The Wiki is updated as the application develops; only weeks 7 and 14 are formal checkpoints.

## Project Organization and Development Process

**Working approach:** [Actual approach and iteration length, if relevant.]  
**Current task and defect tracking:** [Link to GitHub Issues or the actual maintained task board.]  

<details>
<summary><strong>Describing the team's working approach</strong></summary>

Name the approach the team actually uses. For example, a Crisis Guard team could organize reports, map work, and verification as GitHub Issues, discuss priorities once a week, and link its live issue board above. That concrete process description is more informative than declaring “Scrum” when the team does not follow its practices. A real team should name its own cadence and responsibilities; the Wiki does not duplicate the issue board. The example describes a possible workflow, not a claim about how the published Crisis Guard team worked.

</details>

## Documentation Conventions

The documentation consists of linked Markdown pages. Required UML diagrams use PlantUML, with versioned source and a readable image in the Wiki. The examples in this course template show how to write a record; they are not results of the student's project.

<details>
<summary><strong>Diagram sources and teaching examples</strong></summary>

Educational examples assume a React/Vite client, a Node.js backend, PostgreSQL, Render hosting and Selenium WebDriver (JavaScript). Your stack may differ; describe the one you actually use in documentation.

For a Crisis Guard report-submission use case, the team might keep its UML source in a versioned `.puml` file, display the corresponding image on the relevant Wiki page, and update both when the interaction changes. Use the project's actual diagram and deployment. A domain or technology shown in an example does not become a requirement unless it is part of the approved task.

</details>

## Academic Integrity, Conduct, and Licensing

The repository README contains the project's [AI usage statement](../#ai-usage), [code of conduct and support information](../#code-of-conduct-and-support), and [license or reuse status](../#license). Access credentials and other secrets are never published in the Wiki or shared through ordinary messages.

## AI Usage Statement

<!-- INSTRUCTION: This is the detailed AI usage record; the README holds a short summary and links here. Fill in only what actually happened and delete unused rows. If no generative AI tool was used, replace the whole section with one sentence saying so. Every row must point to a page, file, pull request or issue. Never paste credentials, personal data or others' protected material into AI tools. -->

Short summary: [README – AI Usage](../#ai-usage). This section records which tools were used, for which documentation or code, and how the team verified the result. It follows the FER [Policy on the Appropriate Use of Artificial Intelligence](https://www.fer.unizg.hr/_download/repository/Policy%20on%20the%20appropriate%20use%20of%20artificial%20intelligence%20at%20the%20faculty%20of%20electrical%20engineering%20and%20computing%5B1%5D.pdf).

### Tools Used

| Tool | Version or model | Used by | Main purpose |
| --- | --- | --- | --- |
| [Tool name] | [Version or model, if known] | [Team member(s)] | [e.g. drafting documentation text, generating diagram source] |

### Scope of AI Contribution

| Page, file or artifact | Type of assistance | What the tool produced | What the team supplied and changed | Location |
| --- | --- | --- | --- | --- |
| [e.g. 3. Use Cases, UC-002] | [Drafting / rewording / translation / diagram source / summarizing] | [Short description] | [Input given to the tool; facts added, corrected or removed] | [Wiki page, `.puml` file, PR] |

Pages and artifacts not listed above were written without generative AI assistance. [Optional: list any AI-assisted code or tests here as further rows.]

### Verification of Generated Content

| Check | How it was performed | Evidence |
| --- | --- | --- |
| Factual accuracy | [Each statement about features, behavior or architecture was compared with the running application and the code] | [Reviewer names; PR or issue links] |
| No unimplemented claims | [Features, tests and results described in the text were confirmed to exist; planned work is labeled as planned] | [Comparison with Testing (5.4) and Conclusion (7.1)] |
| Consistency with other pages | [Names, IDs and diagrams checked against Requirements, Use Cases, Architecture and Testing] | [Checklist or review note] |
| Diagram sources | [Generated PlantUML was rendered, corrected and matches the implemented system] | [`.puml` file and rendered image] |
| Confidential content | [How the team ensured no secrets, credentials or personal data entered prompts or the Wiki] | [Practice used] |

### Errors Found in AI Output

| Problem | How it was found | Resolution |
| --- | --- | --- |
| [Incorrect, invented or template-copied statement] | [Review, test or comparison with the application] | [Correction, with a link] |

<!-- INSTRUCTION: Record real corrections, or write "None identified". A blanket statement such as "all text was reviewed" is not evidence; the tables above are. The team must be able to explain every sentence it publishes. -->

<details>
<summary><strong>Teaching example: how a documentation-focused record reads</strong></summary>

**Example — Crisis Guard:**

| Page or artifact | Type of assistance | What the tool produced | What the team supplied and changed | Location |
| --- | --- | --- | --- | --- |
| 3. Use Cases, UC-002 | Drafting | First version of the main and alternative flows | Team supplied the real form fields and removed a sign-in branch the application does not have | Example PR #31 |
| Sequence diagram, report submission | Diagram source | PlantUML draft | Team corrected participant names to match the components and removed a notification step that is not implemented | `diagrams/report-submission.puml` (example) |

| Problem | How it was found | Resolution |
| --- | --- | --- |
| Text claimed notifications are delivered within one minute | Compared with Testing (5.4): delivery was never tested | Statement removed; notifications listed under Future Work |
| Draft copied the template's example requirement F-005 as a project requirement | Comparison with the team's own requirements list | Replaced with the team's actual requirement |

**Analysis of the example:** Each row names a page or file, what the tool generated and what the team changed. The errors are the typical ones for generated documentation: a feature that does not exist, and template text presented as project fact. Statements such as "AI was used throughout" or "all text was reviewed" cannot be checked. This example is a teaching scenario, not a description of the published project.

</details>

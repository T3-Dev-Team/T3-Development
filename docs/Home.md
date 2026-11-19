# CityFix — Project Documentation
 
**Course:** [Software Engineering](https://www.fer.unizg.hr/predmet/proinz), Faculty of Electrical Engineering and Computing, University of Zagreb  
**Academic year:** 2026/2027  
**Team:** TG01.3 – T3-Development  
**Instructor:** Vlado Sruk  
**Assistants / Demonstrators:** Goran Rajić, Athanasios Papanikolaou, Borna Gojšić
 
## Project Overview
 
CityFix is a web application in which citizens report problems in the city, such as potholes or broken streetlights, with a photo and a location on the map. Administrators validate the reports and assign them to City Workers, who update their status, so citizens can follow what happens to each report. The application has three roles: Citizen, City Worker and Administrator.
 
**Application and basic setup:** [Repository README](../README.md#quick-start)  
**Public application:** see [README – Deployment](../README.md#deployment)
 
## Team Members and Roles
 
The maintained list of members and their roles is in the [repository README](../README.md#team-members).
 
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
| Week 7 — first review | [Public application](https://t3-development.onrender.com) | Not recorded |
| Week 14 — final review | Pending | Pending |
 
The documentation is updated as the application develops. Only weeks 7 and 14 are formal checkpoints.
 
## Project Organization and Development Process
 
**Working approach:** The team is split into a Django team, which builds the backend, and a support team, which works on the frontend, deployment, testing and documentation. Each member works on a separate branch, and changes are merged into `main` through pull requests. Feedback from the reviews is recorded in [2.7 Review of Requirements](2-Requirements.md#27-review-of-requirements) and shared with the team.  
**Current task and defect tracking:** Team chat and pull requests on GitHub.
 
## Documentation Conventions
 
The documentation consists of linked Markdown pages. All UML diagrams and the ER diagram are PlantUML models. Their sources are in [`docs/puml/`](puml/), and the rendered SVG images in [`docs/assets/diagrams/`](assets/diagrams/) are from them.
 
## Academic Integrity, Conduct, and Licensing
 
The repository README contains the project`s [AI usage statement](../README.md#ai-usage), [code of conduct and support information](../README.md#code-of-conduct-and-support), and [license or reuse status](../README.md#license). Access credentials and other secrets are never published in the documentation or shared through ordinary messages.
 
## AI Usage Statement
 
Short summary: [README – AI Usage](../README.md#ai-usage). This section records which tools were used, for which documentation or code, and how the team verified the result. It follows the FER [Policy on the Appropriate Use of Artificial Intelligence](https://www.fer.unizg.hr/_download/repository/Policy%20on%20the%20appropriate%20use%20of%20artificial%20intelligence%20at%20the%20faculty%20of%20electrical%20engineering%20and%20computing%5B1%5D.pdf).
 
### Tools Used
 
| Tool | Version or model | Used by | Main purpose |
| --- | --- | --- | --- |
| Claude | --- | MS, KB, MP, RY, IJ | Learning Django and understanding the project structure, debugging, integrating the Google Maps API, reviewing pull requests, task organisation, checking documentation, grammar check |
| Gemini | --- | KT | Writing project risks, finding Render deployment guides |

### Scope of AI Contribution

| Page, file or artifact | Type of assistance | What the tool produced | What the team supplied and changed | Location |
| --- | --- | --- | --- | --- |
| Django project structure | Explanations | Explanations of how a Django project is organised, Django syntax and small examples | We used the explanations to understand the framework and wrote the code ourselves | `code/` |
| Users app | Explanations and coding help | Answers to questions about Django-specific parts of the code | We wrote the app, adapted the answers to our project and tested it | `code/users/` |
| Map view, CSS and JavaScript | Explanations and debugging | Explanations of how the components fit together and suggestions for fixing errors | We wrote the components and decided which fixes to apply | `code/` |
| Google Maps API integration | Coding help and debugging | Suggestions for connecting the map and the report form to the API | We adapted the code to our project and tested it in the application | `code/` |
| Pull requests | Review | Lists of possible errors and checks that each pull request matches its task | We decided which remarks to apply and made the final merge decision | GitHub pull requests |
| Task organisation | Planning help | Suggested breakdown and order of tasks | We assigned the tasks and maintained the task board | GitHub Issues |
| Documentation | Review and grammar check | Remarks on unclear parts and grammar corrections | We wrote the text, checked each remark against the application and corrected it | `docs/` |
| Project risks | Guidance | Advice on how to write risks and which kinds to consider | We chose the risks that apply to CityFix and wrote them | `docs/` |
| Render hosting | Finding sources | Links to setup guides | We followed the guides and did the setup ourselves | `docs/6-Deployment-Installation-and-Configuration.md` |

Pages and artifacts not listed above were written without generative AI assistance.

### Verification of Generated Content

| Check | How it was performed | Evidence |
| --- | --- | --- |
| Factual accuracy | Compared with the running app, the code and official documentation | Documentation PR reviews |
| Consistency with other pages | Consistency with other pages | Checked names, IDs and requirements across all pages | --- | --- |
| Code | Tested before merging | GitHub PRs |
| Confidential content | No keys, passwords or user data entered into AI tools | Secrets kept in environment variables |

### Errors Found in AI Output

| Problem | How it was found | Resolution |
| --- | --- | --- |
| None identified | --- | --- |



<!--
TEMPLATE — FER Software Engineering course, final project README.
Copy this file to README.md in your project repository. Replace every
bracketed prompt with facts about your project, remove all instructional
comments and example <details> blocks, and delete this notice before
submission. Do not copy a teaching example as a project result.
-->

# [Application name]

<details>
<summary>Why this section matters</summary>

Start the README with your project name and a concise description of its purpose. The project name does not need to be self-explanatory, but the accompanying description should allow a new reader to quickly understand what the project does.

</details>

[In one sentence, say what the application lets its users do.]

**Course project:** This application was developed by a student team as part of the [Software Engineering](https://www.fer.unizg.hr/predmet/proinz) course at the Faculty of Electrical Engineering and Computing (FER), University of Zagreb.

## App Description

[In two or three sentences, explain the problem, the intended users, and the main benefit of your application. List current functionality separately from anything planned; state the actual scope rather than promised features.]

**Key features**

- [A representative feature users can try]
- [A second representative feature]
- [Optional further feature; do not copy the full requirements list]

For the complete scope, requirements, design, and test evidence, see the [docs](docs/Home.md).

<a id="deployment"></a>
## Deployment

<!-- INSTRUCTION: Required from Checkpoint 1 (week 8). Verify that the URL is the running public application and that the listed flow works. Never publish passwords or tokens. -->

**Live application:** [Public URL]

**Explore:** [One or two brief actions that show a working user flow.]

**Demo:** [Explain how to get the necessary limited access if sign-in is required; otherwise write "No account is required." Do not publish passwords or tokens here.]

**Limitations:** [Briefly name limitations of the deployed version, or link to the single authoritative list of known issues in documentation.]

The [deployment and running guide] describes the hosting setup actually used by this team. The team may use Render or another approved comparable platform.

<a id="quick-start"></a>
## Quick Start / Installation

<!-- Required from Demo 1 onward. Replace the placeholders with commands another teammate has run from a clean clone. Keep detailed administration in the Wiki. -->

**Prerequisites:** [Required runtime and version, package manager, database or external service if essential.]

```bash
git clone [repository URL]
cd [repository directory]
[install dependencies]
[run the application]
```

**Address:** [For example, the actual address printed by the application after it starts.]

**Configuration:** [Name required environment variables or point to a safe `.env.example`; explain where values are obtained. Never put real credentials in this file, an example configuration file, screenshots, logs, or commits.]

[Add a short verification step, such as which page opens or which command runs a basic check.] For detailed setup, see the [project documentation].

## Technologies

List the few technologies and external services that define how your application works. For each, state its specific role and one project-related reason or constraint. Include a development or testing tool only when its role matters to understanding how this project was built or checked. Do not reproduce a dependency list, a language breakdown, or a list of IDEs and communication apps. Check the table against the actual repository and running application; document required versions and configuration in the installation guide.

| Technology or tool | Role in this project | Reason for use or important constraint |
| --- | --- | --- |
| [Name] | [What it does in this application] | [Project-specific reason or constraint] |

<details>
<summary><strong>Example: Explaining key technology choices</strong></summary>

**Example — Crisis Guard:**

| Technology or tool | Role in this project | Reason for use or important constraint |
| --- | --- | --- |
| React | Renders the report form and disaster map in the browser. | The map and submitted reports can update without reloading the entire page. |
| PostgreSQL | Stores reports, locations, and their relationships. | Report records must remain connected to their authors and locations; schema changes require migrations. |
| Map tile service | Provides the map displayed in the browser. | The map depends on an external service; report submission should still have a defined behavior if map tiles are unavailable. |

**Analysis of the example:** Each row describes a role or consequence in this application. Package versions belong in the project's dependency files; setup-sensitive runtime versions and configuration belong in the installation guide. Explain consequential design trade-offs in the Wiki architecture page rather than repeating a full decision record here. Use only services that your team actually integrates.

</details>

## Team Members

| Member | Main role or contribution |
| --- | --- |
| [Name] | [Role or representative contribution] |
| [Name] | [Role or representative contribution] |

Roles may change during the project. The repository and the agreed task tracker provide supporting evidence of teamwork.

## Contributing

[In two sentences, if applicable, describe how someone proposes a task or reports a defect, how a code change is reviewed, and where to find the current work tracker. If the team maintains `CONTRIBUTING.md`, link to it here instead of duplicating its rules. Do not create that file merely to fill this section.]

<a id="license"></a>
## License [![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**License status:** [Name the license and link to the project's `LICENSE` file, or explicitly state that no public reuse license has been granted. Confirm the intended scope with the team; do not copy the documentation template's license statement as the license of your application.]

This repository contains open educational resources and is licensed under the Creative Commons license, which allows you to download, share, and use the work as long as you attribute the author, do not use it for commercial purposes, and share it under the same conditions Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License HR.

Third-party code, datasets, images, icons, and other assets retain their own licenses and attribution requirements. [Link to any additional credits where relevant.]

<a id="ai-usage"></a>
## AI Usage [![AI Usage: Disclosed](https://img.shields.io/badge/AI%20Usage-Disclosed-blue.svg)](https://www.fer.unizg.hr/_download/repository/Policy%20on%20the%20appropriate%20use%20of%20artificial%20intelligence%20at%20the%20faculty%20of%20electrical%20engineering%20and%20computing%5B1%5D.pdf)

This project follows FER's [Policy on the Appropriate Use of Artificial Intelligence](https://www.fer.unizg.hr/_download/repository/Policy%20on%20the%20appropriate%20use%20of%20artificial%20intelligence%20at%20the%20faculty%20of%20electrical%20engineering%20and%20computing%5B1%5D.pdf).

**Statement:** [Say whether AI tools were used. If so, name the tools and their main purposes, and state how the team reviewed the resulting code or text and can explain its own contribution. If none were used, state that plainly. Do not paste private data, access credentials, or other people's protected material into AI tools.]

[If a more detailed AI usage record is required for this course project, link to its single authoritative documentation location.]

<a id="code-of-conduct-and-support"></a>
## Code of Conduct and Support [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

Team members are expected to follow the **STUDENT CODE OF CONDUCT** of the Faculty of Electrical Engineering and Computing, University of Zagreb, the course teamwork guidelines, and the [IEEE Code of Ethics](https://www.ieee.org/about/corporate/governance/p7-8.html). [Link to `CODE_OF_CONDUCT.md` if your repository uses one.]

---

**Course documentation template:** Documentation structure adapted from the FER Software Engineering course template by [Vlado Sruk](https://www.fer.unizg.hr/en/vlado.sruk), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The application and its content were created by the student team named above.

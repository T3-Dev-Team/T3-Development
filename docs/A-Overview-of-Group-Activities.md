# A. Overview of Group Activities

**Objective:** Show how the team organized the project, assigned work, responded to important problems, and contributed to the result. Entries should describe outcomes rather than only saying that a meeting was held or a topic was discussed.

## A.1 Meeting Log

**Objective:** Keep a brief record of project meetings and weekly coordination: who participated, what was decided, and which action followed. Record a discussion that produced no decision only if it left an important issue open.

**Team member abbreviations, if used below:** RY = Rodrigo Yañez; KT = Konstiantyn Tuirikov; MP = Mafalda Pinho; KB = Karla Barković; IJ = Iva Jončić; MS = Macarena Santana.

| Date and participants | Main topic | Decision, action, or open question | Link to task or resulting work, if available |
| --- | --- | --- | --- |
| 12.10.26 - RY, KT MP, KB, IJ, MS | Decided the team and discussed project ideas. | Project: CityFix | Section 1](./1-Project-Scope.md) |
| 19.10.26 - RY, KT MP, KB, IJ, MS | Created Kanban, organized tasks (templates until 3), wrote them to Kanban. | Section 1: IJ, KT; Section 2: KB, MS; Section 3: MP, RY | [Sections 1–3](./1-Project-Scope.md) |
| 01.11.26 - RY, KT MP, KB, IJ, MS | Divide work of template 4, UMLs | 4.1 RY, 4.2 MS, 4.3 RY, 4.4 KB, 4.5 IJ, 4.6 MP, 4.7 KT | [Section 4](./4-Architecture-and-Design.md) |
| 04.11.26 - RY, KT MP, KB, IJ, MS | Frontend, backend, database, hosting, sign-in, notifications and photo storage | One Django backend with templates + HTMX, PostgreSQL, Render hosting, Google-only sign-in, in-app notifications only, photos on Cloudinary. Division of work: RY (D1) users, roles and Google sign-in; MS (D2) issue, category and assignment models, Django admin, admin and worker views; MP (D3) citizen report flow and notifications; KB (A1) templates, navbar and Google Maps JavaScript; KT (A2) deployment on Render, credentials and testing; IJ (A3) documentation and coordination. | ADR-01 to ADR-07 [ADRs, section 4.5](./4-Architecture-and-Design.md#45-architecture-decision-records) |
| 11.11.26 - RY, KT MP, KB, IJ, MS | Check organization and workflow | - | - |
| 15.11.26 - KT MP, KB, IJ, MS | Open questions per role, finished template 4 until 4.7 | Deployment with Google login on Render is the priority (KT, RY). MS builds the worker status update. KB provides base.html and the navbar URL names. | PR #50, PR #52 |
| 18.11.26 - KT MP, KB, IJ, MS | Testing the deployed application | MS: admin verify/reject and worker notification. KB: map view. KT: Render on main + environment variables. RY: disable email-only sign-up. | PR #64, #65, #66; [Section 4.4](./4-Architecture-and-Design.md#44-runtime-behavior)|

Write one concise row per relevant meeting or weekly coordination entry. An assignment should name its owner; an unresolved point should say who will follow up. A meeting title alone does not show what changed. Do not copy the complete issue list or the transcript of a conversation into this log.

<details>
<summary><strong>From a meeting topic to an actionable record</strong></summary>


**Outcome and ownership:** “Discussed location handling” would conceal whether anyone committed to a change. These rows identify a decision or an open action, its owner, and the work to inspect. They do not create additional course checkpoints.

</details>

## A.2 Work Plan

**Objective:** Make the team's intended order of work and responsibility visible. Show the project weeks or other short periods used by the team, including preparation for the two formal reviews.

**Current plan:** GitHub Kanban board of the repository, kept current by IJ, MS

| Period | Principal planned work | Responsible member(s) | Link to tasks, if used |
| --- | --- | --- | --- |
| Weeks 1–4 (to 01.11.26) | Project scope, requirements and use cases (sections 1–3) | RY, KT, MP, KB, IJ, MS |  |
| Week 5 (to 08.11.26) | Architecture and design (section 4), UML diagrams | 4.1 RY, 4.2 MS, 4.3 RY, 4.4 KB, 4.5 IJ, 4.6 MP, 4.7 KT  |  |
| Week 6 (09–15.11.26) | Users and Google sign-in; data model; admin and worker views; templates | RY (D1), MS (D2), KB (A1) | PR #50, #52, #53 |
| Week 7 (16–20.11.26) | Citizen flow and notifications; map; deployment on Render; documentation up to 4.4; first functional version | MP (D3), KB (A1), MS + KT (deploy), IJ (docs) | PR #63, #64, #65, #66 |
| Week 8 (23-27.11.26) | - | - | - |
| Week 9 () | - | - | - |
| Week 10 () | - | - | - |
| Week 11 () | - | - | - |
| Week 12 () | - | - | - |
| Week 13 () | - | - | - |
| Week 14 () | - | - | - |

Keep the plan at a useful weekly level when a table is used; revise it when priorities change. If you use member abbreviations, define them in A.1 and use them consistently here; extend a code if two members share the same initials. The plan is not evidence that planned work was completed. Only the 8th and 14th weeks are formal course checkpoints; ordinary meetings and internal plans are not additional hand-ins.

<details>
<summary><strong>Planning the first public report flow</strong></summary>

**Reading the plan:** The short codes save space in the compact plan; their definitions at the start of A.1 apply throughout this example. When work slips, update the actual task and the plan's expectation; do not claim an unfinished feature was completed merely because its week has passed.

</details>

## A.3 Activity Table

**Objective:** Show which members worked on the important project activities and the approximate effort they report. Include design, documentation, integration, testing, and deployment alongside implementation.

| Activity or deliverable | Member | Reported hours | Representative result or link |
| --- | --- | --- | --- |
| Project idea selection and proposal (CityFix scope, user roles) | RY, KT, MP, KB, IJ, MS | 2 | Accepted project proposal; scope reduced to web app only after TA feedback |
| Requirements and use cases (Citizen, City Worker, Administrator) | RY, MP, KB, MS | 4 | Sections 2 and 3; use case diagram |
| Architecture decisions (Django modular monolith, HTMX, PostgreSQL, Render) | RY |  | Section 4.1 |
| Building blocks and UML component diagram | MS | 4 | Section 4.2 |
| ER and class diagrams | RY |  | Section 4.3 |
| Sequence diagram (report submission) and state diagram (issue lifecycle) | KB | 3 | Section 4.4 |
| Risk assessment (architectural risks, domain risks and technical debt) | KT | 3 | Section 4.7 | 
| D1 – Google sign-in (OIDC/OAuth 2.0), user model with roles, permissions, account deletion | RY |  | Google sign-in works on the deployed app |
| D2 – Data model (8 models), migrations and Django admin | MS | 7 | PR #50 |
| D2 – Admin views (verify/reject, assign with deadline) and worker views (task list, status update) | MS | 6 | PR #52, #53, #64 |
| D3 – Report form with photos, "My reports", notification pages | MP | 6 | Citizens submit reports with photos and follow them in "My reports" PR #63 |
| A1 – Base template, navbar, CSS, report form and map JavaScript, public map view | KB | 6 | PR #51, #56, #65 |
| Photo upload integration (Cloudinary) | KT, MP | 2 | Photos stored on Cloudinary |
| In-app notifications | MP, MS | 1 | Citizens notified on every status change; workers notified when an issue is assigned PR #63, #66 |
| Automated tests | RY, MP, KB |  | 25 tests passing on `main` (`users/tests.py`, `issues/tests.py`, `issues/test_map_view.py`) |
| Integration of modules and merge of branches | RY, KT, MP, KB, IJ, MS |  | Main branch with all apps working together |
| Deployment on Render (web service + managed PostgreSQL) | MS, KT | 5 | [t3-development.onrender.com](https://t3-development.onrender.com), PR #64 |
| Integration of Google Cloud APIs (Google Maps Platform, OAuth 2.0) | KT | 4 | Credentials are connected to Render, access to Google Maps and Google sign-in |
| Documentation editing and PDF export | IJ |  | Final documentation PDF |
| Project coordination (meetings, task split, review prep 18 Nov) | MS | 3 | Meeting notes (Meeting log in A.1) / task organization |


Use project-specific activities rather than a mandatory row for every Wiki chapter or every UML diagram. The team should record hours consistently and avoid double-counting joint work; the representative result explains what the reported effort produced. Hours are self-reported effort, not a measure of quality or a substitute for examining code and artefacts.

<details>
<summary><strong>Recording feature, integration, and documentation work</strong></summary>

**Example — Crisis Guard:** The table distinguishes implementation, integration, and documentation work and links each activity to a result.

| Activity or deliverable | Member | Reported hours | Representative result or link |
| --- | --- | --- | --- |
| Manual map-position input | Ana | 8 | Example issue #21; frontend change. |
| Report validation and persistence | Luka | 10 | Example issue #23; backend change and test. |
| Client–API integration and public deployment | Ema | 7 | Example issue #25; deployment revision. |
| Report-submission use case and permission-denied check | Nika | 5 | Example UC-002 revision and test ST-03. |

**Effort and result:** The final column makes it possible to discuss a contribution without treating a high hour count as proof of delivery. A team can report a genuinely time-consuming unresolved integration problem as work and describe its outcome honestly.

</details>

## A.4 Change Overview Diagram

**Objective:** Show when changes were made in the repository and by whom, while recognizing that commit counts alone do not measure contribution quality.

**Repository activity view:** [GitHub Contributors](https://github.com/T3-Dev-Team/T3-Development/graphs/contributors), period 12.10.2026 - 20.11.2026

The graph represents some of our work. Documentation, diagrams and coordination were often done outside commits or uploaded through the GitHub web interface ("Add files via upload"), and Render and Google Cloud configuration (KT) does not appear in the repository at all. The activity table in A.3 gives the fuller picture.

## A.5 Key Challenges and Solutions

**Objective:** Describe a significant project problem, how the team responded, and what changed or remains unresolved. Choose concrete challenges rather than general praise of teamwork.

| Challenge | Action taken | Outcome or remaining limit |
| --- | --- | --- |
| The Render service was running the course template's Node.js example, so the public URL showed "API running" instead of CityFix. | MS prepared Django for production; KT configured the Render service and environment variables. | CityFix runs on Render with PostgreSQL, deployed from main (PR #64). |
| A Cloudinary API secret was committed in a pull request (#59). | The PR was closed, the secret was regenerated, and all credentials are now only in Render environment variables. | No credentials in the code; the old secret is invalid. |
| New reports stayed in "Reported" because no page let the Administrator verify them, and changing the status in the Django admin skipped the history and notifications (found by MP). | MS added Verify/Reject buttons on /reports/manage/ that use change_status, and made status read-only in the Django admin. | Every status change is recorded and notified. |
|  |  |  |

<details>
<summary><strong>Resolving a location-format mismatch</strong></summary>


</details>

**Final consistency check:** Meetings identify meaningful outcomes and owners; the plan reflects intended work; the effort table and generated repository view refer to the same project; and concrete challenges are connected to actions and their results. The issue board remains the live source for task status.

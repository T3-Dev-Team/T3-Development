# 2. Requirement Analysis

**Objective:** Derive identifiable, prioritized, and verifiable requirements from the approved project scope. The requirements may evolve; by the final submission, they must reflect the agreed application. Sources, decisions and links in course examples are teaching scenarios, not project records.

<details>
<summary><strong>Keeping requirements current</strong></summary>

The examples use the Crisis Guard project topic. Some have useful imperfections for discussion. Sources, decisions, and verification links in these examples are **teaching scenarios**, not records of that student team's work. Replace them with the requirements and evidence of your approved project. Record significant changes in §2.5.

</details>

---

## 2.1 Functional Requirements

**Objective:** State what the application must do for its users, where each capability comes from, and what observable result counts as acceptance.

| ID | Description | Priority | Source | Acceptance criteria |
| --- | --- | --- | --- | --- |
| F-001 | The system allows citizens to sign in through an external identity provider using OAuth 2.0/OpenID Connect. | High | Course requirement | The user signs in with a Google account; on first login a Citizen account linked to that email is created, and no password is stored by the system. |
| F-002 | The system allows the Administrator to create Administrator and City Worker accounts. | High | Project proposal | The Administrator enters an email, role and department; when that user signs in with the same email, they get access to the functions of their role. |
| F-003 | The system allows citizens to report an issue with a category, description, photos and a location on the map. | High | Project proposal | The citizen can specify the location by using their current location, typing an address with suggestions, or placing a pin on a map; the report is saved with the status "Reported". |
| F-004 | The system converts between street addresses and map coordinates for each report. | High | Project proposal | When the citizen types an address, the selected location is shown on the map for confirmation; when the citizen uses their current location or places a pin, the corresponding address is shown and stored with the report. |
| F-005 | The system detects possible duplicate reports. | Medium | Project proposal | When an unresolved report of the same category exists within 50 m, the citizen is shown that report and can support it instead of creating a new one, which increases its priority. |
| F-006 | The system displays all public reports on an interactive map with filters | High | Project proposal | Users can filter reports by category, status and date; nearby markers are grouped when there are many in a small area. |
| F-007 | The system allows citizens to follow the status of their reports. | High | Project proposal | The citizen can see the current status for each of their reports. |
| F-008 | The system notifies citizens when the status of their report changes. | Medium | Project proposal | Every status change creates an in-app notification for the citizen who reported the issue. |
| F-009 | The system allows the Administrator to validate or reject reports. | High | Project proposal | The Administrator marks a report as verified, rejected (with a reason) or duplicate of an existing report, and the status is updated. |
| F-010 | The system allows the Administrator to set the priority and deadline of a verified report and assign it to a City Worker. | High | Project proposal | Only City Workers from the department responsible for the category can be selcted; after assignment the status changes to "Assigned". |
| F-011 | The system shows City Workers the issues assigned to them. | High | Project proposal | The worker sees their assigned issues as a list and on a map, sorted by priority and deadline. | 
| F-012 | The system allows City Workers to update the status of an issue and add comments. | High | Project proposal | The worker can change the status to "In Repair" or "Resolved" and add a comment, which is shown in the issue history. |
| F-013 | The system requires a photo of the completed repair before an issue is marked as resolved. | Medium | Project proposal | An issue cannot be marked as resolved without an "after" photo; the photo is shown to the citizen who reported it.
| F-014 | The system allows City Workers to return an issue to the Administrator. | Medium | Project proposal | The worker returns the issue with an explanation; it is removed from their list and the Administrator can reassign it. |
| F-015 | The system adds assigned issues to the City Worker's Google Calendar. | Medium | Project proposal | After assignment, an event with the address, category and deadline appears in the worker's calendar. |
| F-016 | The system shows the weather forecast for the location of an assigned issue. | Low | Project proposal | The issue details page shows the forecast for the next days. |
| F-017 | The system allows the Administrator to define default resolution times and escalates overdue issues. | Low | Project proposal | When an issue approaches its deadline without status updates, its priority is raised and the Administrator receives an in-app alert. | 
| F-018 | The system allows citizens to rate the resolution of their report. | Low | Project proposal | After an issue is resolved, the citizen can rate it. |
| F-019 | The system shows the Administrator statistics and a heatmap of reports. | Medium | Project proposal | The Administrator can see a heatmap of reports and the number of open and resolved issues, average resolution time and most common categories. |
| F-020 | The system allows the Administrator to manage departments, categories and City Worker profiles. | Medium | Project proposal | The Administrator can create, edit and deactivate departments, categories and worker profiles. |
| F-021 | The system allows citizens to delete their account. | Medium | General Data Protection Regulation | After the citizen confirms the deletion, their account and personal data (name, email, notifications, ratings) are permanently deleted, and their reports remain visible without any link to the deleted user. |



<details>
<summary><strong>Requirement sources and acceptance criteria</strong></summary>

Each requirement needs a stable ID. **Source means where this requirement came from**, such as the approved project task, a stakeholder request, or feedback that changed the requirement. Describe observable behavior instead of naming a screen or framework. Use the same priority scale throughout. Explain a complex user interaction in its use case rather than copying its full flow into this table.

**Example — functional requirements for a disaster information application:**

The source categories show different ways a requirement might arise. These rows are teaching material; they do not establish that the published project received those requests or delivered these features.

| ID | Description | Priority | Source | Acceptance criteria |
| --- | --- | --- | --- | --- |
| F-001 | The system allows users to register an account using an email address. | High | Stakeholder requirement | The user can register via email, receive a confirmation email, and activate the account by following the link. |
| F-002 | The system allows password recovery via email. | Medium | Stakeholder requirement | The user can request a password reset, receive a reset link, and reset the password successfully. |
| F-003 | The system provides a list of available resources for disasters. | High | Existing system | The user can view an updated list of resources relevant to the disaster type, location, and availability. |
| F-004 | The system allows users to submit disaster reports with location details. | High | Requirement document | The user can submit a report detailing the disaster type, severity, and location and receive confirmation. |
| F-005 | The system sends notifications to users about updates in their vicinity. | High | User feedback | Users receive notifications within one minute of a relevant update for their location. |
| F-006 | Display disaster resources based on location. | High | Document analysis | Updated resource lists tailored to disaster type, location, and availability are shown. |

**Acceptance criteria and provenance:** It shows registration, recovery, disaster resources, reporting, and notifications, with several kinds of sources and observable criteria. It also offers useful questions: Do F-003 and F-006 describe the same resource feature? Is the one-minute promise in F-005 agreed and testable? Does a real OAuth-only application need F-001 and F-002? Keep the original rows as material to examine, **not six features every team must implement**. A real team's source column records where *its* requirements actually came from.

**Example adaptation when the approved task uses OAuth and a map:** Instead of copying email account creation and password recovery, formulate the relevant sign-in requirement, for example: “F-001: Users sign in through the approved OAuth provider; successful sign-in allows access to the actions reserved for signed-in users, while cancelling leaves those actions unavailable.” A separate map requirement could say: “F-007: Reports with locations appear as map markers; selecting a marker opens the corresponding report.” Their source would be the actual approved task or agreed stakeholder request. This adaptation is an alternative to mismatched rows, not another table every team must fill in.

For a complex interaction, a short *Given / When / Then* scenario may clarify a criterion. For example: *Given* a report without a location, *when* the citizen submits it, *then* the system explains the missing location and stores no report. Do not repeat a simple criterion in both prose and Gherkin or write Gherkin for every requirement.

</details>

---

## 2.2 Non-Functional Requirements

**Objective:** Specify the important quality properties and operating conditions of the approved application in a way the team can reasonably check.

| ID | Description | Priority | Source |
| --- | --- | --- | --- |
|  |  |  |  |

<details>
<summary><strong>Choosing verifiable non-functional requirements</strong></summary>

Relevant properties may concern usability, accessibility, security, performance, or reliability. Choose project-specific properties and describe how they can be checked. The requirement says what is expected; actual observations and evidence belong with the tests, not in a second result column here.

**Example — non-functional requirements for the disaster information application:**

| ID | Description | Priority | Source |
| --- | --- | --- | --- |
| NF-1.1 | The system must support 1,000 concurrent users with a response time under 1 s. | High | SLA |
| NF-1.2 | All sensitive data must be encrypted using AES-256. | High | Security policy |
| NF-1.3 | The system's UI must support both English and Spanish. | Medium | Stakeholder feedback |
| NF-1.4 | System uptime must be at least 99.5% per month. | High | SLA |
| NF-3.1.7 | The system should have adequate documentation. | High | Documentation policy |
| NF-3.1.7.1 | The system code should be documented according to “Code Conventions for the Java Programming Language.” | High | Documentation policy |
| NF-3.1.7.2 | The system should be described via a design document/SRS. | High | Documentation policy |
| NF-3.1.7.3 | The system should be accompanied by an “Operational Manual” describing its proper use. | High | Documentation policy |
| NF-3.1.7.4 | The system should have an “Implementation Plan” for proper deployment. | High | Deployment guidelines |

**Verifiability and scope:** It introduces performance, security, localization, availability, and documentation, including a hierarchical requirement ID. Its sources are examples of provenance, not evidence that a real SLA or security policy exists for the student project. Values such as 1,000 users, 99.5% monthly uptime, and AES-256 must have an approved source and a feasible way to verify them before they can become the team's requirements. The documentation group illustrates decomposition, but requirements to produce *this course documentation* normally belong in assignment instructions rather than in the web application's quality requirements.

**Example adaptation:** If the approved map task requires a fallback when browser geolocation is denied, a project-specific non-functional requirement might be: “NF-01: A citizen can still choose a report location manually after denying geolocation access.” Verification: deny browser permission, choose a map point, and try to submit a report. This is a concrete check, not a measured result or an additional universal obligation.

</details>

## 2.3 Stakeholders and Actors

**Objective:** Identify roles that affect requirements and distinguish stakeholders from actors who interact with the application.

| Role or actor ID | Relation to the system | Relevant requirements |
| --- | --- | --- |
| A-01 Citizen | Primary actor. Reports issues, follows their status, rates resolutions and can delete their account. | F-001, F-003, F-007, F-018 |

<details>
<summary><strong>Connecting actors to requirements</strong></summary>

**Example — actors for the disaster information application:**

| Actor ID | Role | Functional requirements covered |
| --- | --- | --- |
| A-01 | Disaster Manager | F-003: View resources; F-004: Submit disaster reports. |
| A-02 | Citizen | F-001: Create account; F-005: Receive notifications. |
| A-03 | System Administrator | NF-1.2: Enforce security standards; manage users. |
| A-04 | Visitor | F-007: View reports on map.|
**Actor responsibilities:** An actor's role should connect to an interaction, not merely to a label. Check whether the Disaster Manager actually submits reports in the approved task. The administrator's link to NF-1.2 names a security concern, but does not by itself describe a use case; specify the administrator's real action or omit the role if it has none. Course staff interested in the result may be stakeholders without being actors in the application. The table is a starting point for reasoning, not a verified account of Crisis Guard's permissions.

</details>

---

## 2.4 Constraints and Assumptions

**Objective:** Record project-specific boundaries and assumptions that affect requirements or design, including their source and practical consequence. This is their authoritative location.

| ID | Constraint or assumption | Source | Consequence or way to verify |
| --- | --- | --- | --- |
|  |  |  |  |

<details>
<summary><strong>Constraints versus assumptions</strong></summary>

A constraint is a restriction the team must respect; an assumption is a condition it relies on and should revisit.

**Example — Crisis Guard design context:**

| ID | Constraint or assumption | Source | Consequence or way to verify |
| --- | --- | --- | --- |
| C-01 | Approved task requires OAuth sign-in for editing a user's own reports. | Approved task **in this example scenario** | Design protected editing around the chosen provider; verify both authorized and unauthorized requests. |
| AS-01 | Reports used for the map have usable coordinates. | Data assumption **in this example scenario** | Inspect sample and imported reports; plan how to display reports without valid coordinates. |

**Constraint versus assumption:** C-01 identifies a binding decision and its architectural effect; AS-01 is testable and may prove false. Do not copy C-01 if OAuth is absent from the actual approved task. Explain the design response in the architecture without copying this table.

</details>

---

## 2.5 Significant Requirement Changes

**Objective:** Preserve the reason for changes that alter agreed scope, priority, or acceptance criteria, while keeping the current requirements above up to date.

| Date | Requirement ID | Change and reason | Agreed with / evidence |
| --- | --- | --- | --- |
|  |  |  |  |

<details>
<summary><strong>Recording a significant change</strong></summary>

**Example scenario — a decision during a Crisis Guard review:**

| Date | Requirement ID | Change and reason | Agreed with / evidence |
| --- | --- | --- | --- |
| [Date of review] | F-004, NF-01 | Add manual location selection when browser geolocation is denied; without it, a citizen cannot submit a located report. | [Link to the team's actual review note or issue] |

**Reason for the change:** It names the affected records and explains the user-facing reason, then points to the decision's evidence. The review and change are **constructed examples**, not events attributed to the published project. Update the current requirements after a real decision; a wording fix needs no log entry. Keep the current task queue in the issue tracker.

</details>

---

## 2.6 Requirement Traceability

**Objective:** Show where important requirements are described in use cases, where relevant, and where they are checked.

| Requirement ID | Use case or design location | Test or verification location |
| --- | --- | --- |
| F-001 | [UC-001] | [ST-001, CT-001] | [Passed / Failed / Pending – reason] |
|  |  |  |

<details>
<summary><strong>Linking requirements, use cases, and tests</strong></summary>

**Example — Crisis Guard requirement links:**

| Requirement ID | Use case or design location | Test or verification location |
| --- | --- | --- |
| F-001 | UC-001 Register account | T-04 Valid registration; T-05 Existing email |
| F-004 | UC-002 Submit disaster report | T-01 Valid report; T-02 Missing location |
| NF-01 | Report location fallback | T-03 Denied geolocation permission |

**Coverage and evidence:** F-004 leads to a user interaction and two concrete checks. NF-01 refers to the **adapted example requirement above**, not to the nine original NF rows; it leads to a check without inventing a separate use case. UC-002 and T-01–T-03 are example identifiers, not existing Crisis Guard documents or executed tests. In your project, link the actual use cases and checks here, and mark a missing link *pending* with a reason. Record observed test results with the tests; this table identifies where to find them.

</details>

---

## 2.7 Review of Requirements

**Objective:** Record meaningful feedback on requirements and the resulting decisions at the two formal project checkpoints, in weeks 7 and 14.

| Checkpoint | Feedback or finding | Resulting requirement or scope decision |
| --- | --- | --- |
| Checkpoint 1 (week 7) | [Feedback] | [Decision; see 2.5] |
| Demo 2 (week 11) | [Feedback] | [Decision; see 2.5] |  |  |  |

<details>
<summary><strong>Recording decisions from a review</strong></summary>

**Example scenario — review of a Crisis Guard requirement:**

| Checkpoint | Feedback or finding | Resulting requirement or scope decision |
| --- | --- | --- |
| Week 7 (example) | The demonstration reveals that denying browser location access prevents report submission. | Agree on a manual location fallback; update F-004 and the example NF-01 and record the reason in §2.5. |

**Decision linked to feedback:** It connects observed behavior to a specific requirement change and avoids minutes of the entire meeting. The entry is **not a historical Crisis Guard milestone**. Write only actual feedback and decisions for this team's two formal checkpoints, weeks 8 and 14. Consultation in another week does not create an additional required submission.

</details>

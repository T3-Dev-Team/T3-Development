# 3. Use Cases

**Objective:** Show the principal interactions between the application's actors and the system. Describe how an actor achieves a goal and what happens when an important step fails. Base the interactions on the approved requirements and revise them as the application develops.

## 3.1 Use Case Diagram

**Objective:** Show the system boundary, its relevant actors, and their main goals in **one readable UML use case diagram**. Add a focused second diagram only if the complete view cannot remain clear; a third requires a distinct project-specific reason.

**Rendered use case diagram:** ![Use case diagram](./assets/diagrams/3-1-crisis-guard-system-UC.svg)  
**Versioned PlantUML source:** [`Source puml`](./puml/3-1-crisis-guard-system-UC.puml)

**Consistency check:** Show the identified roles that **interact with the application**, not stakeholders who have no interaction. Each main user goal must have an associated actor; an included use case can be reached through another use case without its own direct actor association. Use `<<include>>` and `<<extend>>` only when the relationship expresses actual behavior.

<details>
<summary><strong>Actors and goals in one diagram</strong></summary>

The diagram below illustrates a **course scenario** with a citizen, a visitor, and an organization that checks available resources. Only include the organization as an actor if the team's approved project actually lets it interact with the application. OAuth is outside this example because it is an implementation-specific sign-in choice and belongs in the requirements only if approved.

[PlantUML source](./puml/3-1-crisis-guard-system-UC.puml) · [Rendered SVG](./assets/diagrams/3-1-crisis-guard-system-UC.svg)

**Actor and goal selection:** The boundary identifies what the application offers, the actors have distinct goals, and no actor or use case claims that this student application dispatches emergency services. Compare the diagram with your approved functional requirements and actors. This PlantUML block is a teaching example, not the versioned source and rendered image of the team's own diagram.

**Five questions for choosing the diagram's content** (not five diagrams to submit):

| Focus | What to ask |
| --- | --- |
| Whole system | Which user goals best explain what this application is for? |
| Key features | Which goals need detail in a description or, if necessary, a separate focused diagram? |
| User roles | Which actors may participate in each goal, and how do their permissions differ? |
| Core processes | Which goal has meaningful alternatives that need a use case description? |
| External integrations | Does another system participate in a use case as a **secondary actor**, such as an approved identity provider during sign-in? |

An external system may appear as a secondary use-case actor when it participates in a user's goal; the architecture describes technical connections. Do not create another required use case diagram solely to inventory integrations. Split a crowded diagram by related actors or goals only when it improves readability.

</details>

---

## 3.2 Use Case Descriptions

**Objective:** For each use case in the diagram, explain the actor's goal, the normal interaction with the application, and meaningful alternatives. Describe straightforward use cases briefly; expand those whose alternatives, external dependencies, or consequences require more explanation.


### UC-[001]: Sign-In

| Field | Description |
| --- | --- |
| Primary actor | Citizen, City Worker, Administrator |
| Requirement ID(s) | F-001, F-002 |
| Preconditions, if any | For a city Worker or Administrator the acount must be create first by an Administrator with the user's email (UC-014)|
| Main flow | 1.The user chooses to sign in; the application redirects to the identity provider.<br>2. The user authenticates with their Google account.<br>3. The application receives the user's email address and looks for an account with that email.<br>4. If no account exists, the application creates a Citizen account linked to that email. If an account created by an Administrator exists, the application uses its role and department.<br>5. The application opens the interface for the user's role. |
| Alternative or failure flows, if any | **2a - Sign-in cancelled or rejected:** the application returns to the sign-in page, explains that sign-in did not complete and keeps the restricted actions unavailable.<br>**3a -Identity provider unavailable:** the application reports that sign-in is temporarily unavailable and creates no session. |
| Result | The user is signed in and sees the functions of their role. No password is stored by the system. |


### UC-[002]: Report Issue

| Field | Description |
| --- | --- |
| Primary actor | Citizen |
| Requirement ID(s) | F-003, F-004 |
| Preconditions, if any | Thecitizen is signed in. |
| Main flow | 1. The citizen opens the report form; the application shows the fields for category, description, photos and location.<br>2. The citizen selects a category and may write a description.<br>3. The citizen specifies the location by using their current location, typing an address with suggestions, or placing a pin on the map; the application shows the corresponding address or map point for confirmation.<br>4. The citizen may add photos (UC-004).<br>5. The citizen submits the report; the application checks the required data and looks for a possible duplicate (UC-003).<br>6. If there is no duplicate, the application saves the report with the status "Reported" and shows a confirmation. |
| Alternative or failure flows, if any | **3a — Geolocation permission denied:** the citizen types an address or places a pin on the map; the flow continues at step 4 (NF-10).<br>**3b — Address lookup unavailable:** the application shows an error message, keeps the entered data and lets the citizen place a pin on the map (NF-09).<br>**5a — Required data missing (category or location):** the application indicates what is missing, preserves the entered data and does not save the report.<br>**5b — Possible duplicate found:** the flow continues in UC-003.<br>**6a — Saving fails:** the application states that the report was not submitted and does not show a confirmation. |
| Result | The report is saved with the status "Reported". |


### UC-[003]: Detect Duplicate Issue

| Field | Description |
| --- | --- |
| Primary actor | Citizen |
| Requirement ID(s) | F-005 |
| Preconditions, if any | The citizen has submitted a report |
| Main flow | 1. The application looks for an unresolved report of the same category within 50 m of the chosen location.<br>2. If one exists, the application shows it to the citizen.<br>3. The citizen chooses to support the existing report instead of creating a new one; the application increases the existing report's priority and shows a confirmation. |
| Alternative or failure flows, if any | **1a — No similar report found:** UC-002 continues at step 6.<br>**3a — The citizen decides it is a different problem:** the application saves the new report as in UC-002, step 6. |
| Result | A duplicate is avoided, or the new report proceeds. |

### UC-[004]: Attach Photo

| Field | Description |
| --- | --- |
| Primary actor | Citizen |
| Requirement ID(s) | F-003 |
| Preconditions, if any | The citizen is filling in the report form. |
| Main flow | 1. The citizen chooses to add a photo, taking one with the device camera or selecting one.<br>2. The application uploads it and shows a preview in the form. |
| Alternative or failure flows, if any | **2a — Upload fails or the file is not accepted:** the application explains the problem; the citizen may retry or submit the report without the photo. |
| Result | The photo is attached to the report. |

### UC-[005]: View issue map

| Field | Description |
| --- | --- |
| Primary actor | Citizen |
| Requirement ID(s) | F-006 |
| Preconditions, if any |  |
| Main flow | 1. The citizen opens the map; the application shows the public reports as markers and groups nearby markers when there are many in a small area.<br>2. The citizen filters by category, status or date; the application updates the map.<br>3. The citizen selects a marker to see the details of that report. |
| Alternative or failure flows, if any | **1a — Map cannot be loaded:** the application shows an error message and lets the citizen retry.<br>**2a — No report matches the filters:** the application shows an empty result and suggests changing the filters. |
| Result | The citizen sees the reports that match the chosen filters. |

### UC-[006]: Track Issue Status

| Field | Description |
| --- | --- |
| Primary actor | Citizen |
| Requirement ID(s) | F-007, F-008, F-013 |
| Preconditions, if any | The citizen is signed in and has submitted at least one report. |
| Main flow | 1. The citizen opens their reports; the application lists them with their current status.<br>2. The citizen selects a report and the application shows its details and history; when the issue is resolved, the "after" photo uploaded by the worker is showed aswell.<br>3. When the status of a report changes, the application creates an in-app notification for the citizen. |
| Alternative or failure flows, if any | **1a — The citizen has no reports:** the application shows an empty list with a link to the report form. |
| Result | The citizen knows the current status of each report and is notified of changes. |

### UC-[007]: Confirm Resolution and Rate

| Field | Description |
| --- | --- |
| Primary actor | Citizen |
| Requirement ID(s) | F-018, F-013 |
| Preconditions, if any | The citizen's report is resolved. |
| Main flow | 1. The citizen opens the resolved report; the application shows the repair photo.<br>2. The citizen rates the resolution.<br>3. The application stores the rating. |
| Alternative or failure flows, if any | **2a — The citizen does not rate:** the report stays resolved without a rating.<br>**3a — Saving fails:** the application reports the failure and lets the citizen retry. |
| Result | The citizen has seen the proof of repair and their rating is stored. |

### UC-[008]: View Assigned Issues

| Field | Description |
| --- | --- |
| Primary actor | City Worker |
| Requirement ID(s) | F-011, F-016 |
| Preconditions, if any | The worker is signed in and has at least one assigned issue. |
| Main flow | 1. The worker opens their assigned issues; the application shows them as a list and on a map, sorted by priority and deadline.<br>2. The worker selects an issue; the application shows its category, description, photos, location, deadline and the weather forecast for the location. |
| Alternative or failure flows, if any | **1a — No issues assigned:** the application shows an empty list.<br>**2a — Forecast unavailable:** the application shows the details without the forecast and says it could not be loaded. |
| Result | The worker knows which issues and their order. |

### UC-[009]: Update Issue Status

| Field | Description |
| --- | --- |
| Primary actor | City Worker |
| Requirement ID(s) | F-012, F-013, F-008 |
| Preconditions, if any | The issue is assigned to the worker. |
| Main flow | 1. The worker opens an assigned issue and changes its status to "In Repair" or "Resolved".<br>2. The worker may add a comment.<br>3. If the new status is "Resolved", the worker uploads the repair photo.<br>4. The application saves the change and shows the comment in the issue history; the citizen who reported the issue is notified. |
| Alternative or failure flows, if any | **3a — Repair photo missing:** the application does not accept "Resolved" and asks for the photo.<br>**4a — Saving fails:** the application reports the failure and keeps the previous status. |
| Result | The issue has the new status. |

### UC-[010]: Upload Repair Photo

| Field | Description |
| --- | --- |
| Primary actor | City Worker |
| Requirement ID(s) | F-013 |
| Preconditions, if any | The worker is marking the issue as "Resolved". |
| Main flow | 1. The worker takes or selects the "repaired" photo.<br>2. The application uploads it and attaches it to the issue; the citizen who reported it can see it. |
| Alternative or failure flows, if any | **2a — Upload fails:** the application explains the problem and keeps the issue unresolved until the photo is uploaded. |
| Result | The repair photo is stored and shown to the citizen who reported the issue. |

### UC-[011]: Return/Reject Issue

| Field | Description |
| --- | --- |
| Primary actor | City Worker |
| Requirement ID(s) | F-014 |
| Preconditions, if any | The issue is assigned to the worker. |
| Main flow | 1. The worker chooses to return the issue.<br>2. The worker writes an explanation.<br>3. The application removes the issue from the worker's list and makes it available to the Administrator for reassignment. |
| Alternative or failure flows, if any | **2a — Explanation missing:** the application asks for it and does not return the issue. |
| Result | The Administrator can reassign the issue. |

### UC-[012]: Validate Report

| Field | Description |
| --- | --- |
| Primary actor | Administrator |
| Requirement ID(s) | F-009, F-008 |
| Preconditions, if any | A report with the status "Reported" exists. |
| Main flow | 1. The administrator opens a report and reviews its category, description, photos and location.<br>2. The administrator marks it as verified.<br>3. The application updates the status and notifies the citizen. |
| Alternative or failure flows, if any | **2a — Invalid report (false or outside the city area):** the administrator rejects it and enters a reason; the application updates the status and notifies the citizen.<br>**2b — Duplicate:** the administrator marks it as a duplicate of an existing report and selects that report; the application updates the status. |
| Result | The report is verified, rejected with a reason, or marked as a duplicate. |

### UC-[013]: Assign Issue

| Field | Description |
| --- | --- |
| Primary actor | Administrator |
| Requirement ID(s) | F-010, F-015, F-016 |
| Preconditions, if any | The report is verified (UC-012) or was returned by a worker (UC-011). |
| Main flow | 1. The administrator opens the issue; the application shows its details and the weather forecast for the location.<br>2. The administrator sets the priority and the deadline.<br>3. The administrator selects a City Worker; the application offers only workers from the department responsible for the category.<br>4. The application saves the assignment and changes the status to "Assigned".<br>5. The application creates an event in the worker's Google Calendar with the address, category and deadline. |
| Alternative or failure flows, if any | **1a — Forecast unavailable:** the application shows the issue without the forecast; the assignment can continue.<br>**3a — No worker in the department:** the application tells the administrator that no worker can be selected and the issue stays unassigned.<br>**5a — Calendar event fails:** the assignment is kept; the application tells the administrator that the event was not created and lets them retry. |
| Result | The issue has a priority, a deadline and an assigned worker, and the event is in the worker's calendar. |

### UC-[014]: Manage Acounts and Departments

| Field | Description |
| --- | --- |
| Primary actor | Administrator |
| Requirement ID(s) | F-002, F-020 |
| Preconditions, if any | The administrator is signed in. |
| Main flow | 1. The administrator creates an Administrator or City Worker account by entering an email address, a role and a department.<br>2. The application saves the account; when that user signs in with the same email, they get the functions of their role (UC-001).<br>3. The administrator creates, edits or deactivates departments, categories and worker profiles. |
| Alternative or failure flows, if any | **1a — Email already registered:** the application explains why the account cannot be created.<br>**1b — Missing or invalid data:** the application indicates the problem and saves nothing. |
| Result | The accounts, departments, categories and worker profiles reflect the administrator's changes. |

### UC-[015]: View Statistics and Heatmap

| Field | Description |
| --- | --- |
| Primary actor | Administrator |
| Requirement ID(s) | F-019 |
| Preconditions, if any | The administrator is signed in. |
| Main flow | 1. The administrator opens the statistics view.<br>2. The application shows a heatmap of reports and the number of open and resolved issues, the average resolution time and the most common categories. |
| Alternative or failure flows, if any | **2a — Map cannot be loaded:** the application shows the statistics without the heatmap and says why.<br>**2b — Not enough data:** the application shows an empty state. |
| Result | The administrator sees where and how often problems occur. |

### UC-[016]: Delete Acount

| Field | Description |
| --- | --- |
| Primary actor | Citizen |
| Requirement ID(s) | F-021 |
| Preconditions, if any | The citizen is signed in. |
| Main flow | 1. The citizen chooses to delete their account; the application explains what will be deleted and asks for confirmation.<br>2. The citizen confirms.<br>3. The application permanently deletes the account and personal data (name, email, notifications, ratings) and signs the citizen out.<br>4. The citizen's reports stay visible, without any link to the deleted user. |
| Alternative or failure flows, if any | **2a — The citizen cancels:** nothing is deleted.<br>**3a — Deletion fails:** the application reports the failure and keeps the account. |
| Result | The account and personal data no longer exist; the reports remain, without a link to the user. |

### UC-[017]: Define Time Settings

| Field | Description |
| --- | --- |
| Primary actor | Administrator |
| Requirement ID(s) | F-017 |
| Preconditions, if any | The administrator is signed in. |
| Main flow | 1. The administrator opens the resolution time settings; the application shows the default times.<br>2. The administrator sets the default resolution time and saves.<br>3. When an issue approaches its deadline without status updates, the application raises its priority and shows an in-app alert to the administrator. |
| Alternative or failure flows, if any | **2a — Invalid value:** the application explains the problem and does not save. |
| Result | The default times are saved and overdue issues are escalated. |

---

## 3.3 Use Case Consistency Check

**Objective:** Check that use cases, actors, and requirements agree with one another and with the application the team demonstrates.

| Check | Result |
| --- | --- |
| Requirement | All 17 use cases mach functional requirements from 2.1, and every requirement appears in at least one use case. |
| Actor | Each primary actor matches a role in 2.3: Citizen (A-01), City Worker (A-02) and Administrator (A-03). Each role performs only the use cases permitted to it (NF-06). |
| Application | All use cases have a main flow and result, as well as an alternative or failure flow. This is the initial report, so they describe the current design. |

**Requirements without a direct actor interaction.** F-004 (address and coordinate conversion) is done by the system inside UC-002. F-008 (notifications for status change) happens in UC-006, UC-009 and UC-012. The non-functional requirements apply across all use cases.



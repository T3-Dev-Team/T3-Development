# 2. Requirement Analysis

**Objective:** Derive identifiable, prioritized, and verifiable requirements from the approved project scope. The requirements may evolve. By the final submission, they must reflect the agreed application.

---

## 2.1 Functional Requirements

**Objective:** State what the application must do for its users, where each capability comes from, and what observable result counts as acceptance.

The requirements follow from the problems described in [1.1](./1-Project-Scope.md#11-problem-and-project-objective): reporting must be simple (F-003 to F-006), citizens must know what happens to their reports (F-007, F-008, F-013, F-018), and the city's work on reports must be organised and traceable (F-009 to F-012, F-014 to F-017, F-019). F-001, F-002, F-020 and F-021 provide secure access and data protection.

| ID | Description | Priority | Source | Acceptance criteria |
| --- | --- | --- | --- | --- |
| F-001 | The system allows citizens to sign in through an external identity provider using OAuth 2.0/OpenID Connect. | High | Course requirement | The user signs in with a Google account. On first login a Citizen account linked to that email is created, and no password is stored by the system. |
| F-002 | The system allows the Administrator to create Administrator and City Worker accounts. | High | Project proposal | The Administrator enters an email, role and department. When that user signs in with the same email, they get access to the functions of their role. |
| F-003 | The system allows citizens to report an issue with a category, description, photos and a location on the map. | High | Project proposal | The citizen can specify the location by using their current location, typing an address with suggestions, or placing a pin on a map. The report is saved with the status "Reported". |
| F-004 | The system converts between street addresses and map coordinates for each report. | High | Project proposal | When the citizen types an address, the selected location is shown on the map for confirmation. When the citizen uses their current location or places a pin, the corresponding address is shown and stored with the report. |
| F-005 | The system detects possible duplicate reports. | Medium | Project proposal | When an unresolved report of the same category exists within 50 m, the citizen is shown that report and can support it instead of creating a new one, which increases its priority. |
| F-006 | The system displays all public reports on an interactive map with filters | High | Project proposal | Users can filter reports by category, status and a date range (from–to) and reset the filters. Nearby markers are grouped when there are many in a small area. When no report matches, an empty-result message is shown. |
| F-007 | The system allows citizens to follow the status of their reports. | High | Project proposal | The citizen sees a list of their reports with the category, address, date and current status of each, and can open a report to see its status history. |
| F-008 | The system notifies citizens when the status of their report changes. | Medium | Project proposal | Every status change creates an in-app notification for the citizen who reported the issue, and the number of unread notifications is shown in the navigation bar. |
| F-009 | The system allows the Administrator to validate or reject reports. | High | Project proposal | The Administrator marks a report as verified, rejected (with a reason) or duplicate of an existing report, and the status is updated. |
| F-010 | The system allows the Administrator to set the priority and deadline of a verified report and assign it to a City Worker. | High | Project proposal | Only City Workers from the department responsible for the category can be selected. After assignment the status changes to "Assigned". |
| F-011 | The system shows City Workers the issues assigned to them. | High | Project proposal | The worker sees their assigned issues as a list and on a map, sorted by priority and deadline. | 
| F-012 | The system allows City Workers to update the status of an issue and add comments. | High | Project proposal | The worker can change the status to "In Repair" or "Resolved" and add a comment, which is shown in the issue history. |
| F-013 | The system requires a photo of the completed repair before an issue is marked as resolved. | Medium | Project proposal | An issue cannot be marked as resolved without an "after" photo. The photo is shown to the citizen who reported it. |
| F-014 | The system allows City Workers to return an issue to the Administrator. | Medium | Project proposal | The worker returns the issue with an explanation. It is removed from their list and the Administrator can reassign it. |
| F-015 | The system adds assigned issues to the City Worker's Google Calendar. | Medium | Project proposal | After assignment, an event with the address, category and deadline appears in the worker's calendar. |
| F-016 | The system shows the weather forecast for the location of an assigned issue. | Low | Project proposal | The issue details page shows the forecast (temperature and precipitation) for the issue location for the next 3 days. |
| F-017 | The system allows the Administrator to define default resolution times and escalates overdue issues. | Low | Project proposal | When less than 24 hours remain before the deadline and the issue is still "Assigned", its priority is raised and the Administrator receives an in-app alert. | 
| F-018 | The system allows citizens to rate the resolution of their report. | Low | Project proposal | After an issue is resolved, the citizen who reported it can rate the resolution once, from 1 to 5. The rating is shown to the Administrator on the issue. |
| F-019 | The system shows the Administrator statistics and a heatmap of reports. | Medium | Project proposal | The Administrator can see a heatmap of reports and the number of open and resolved issues, average resolution time and most common categories. |
| F-020 | The system allows the Administrator to manage departments, categories and City Worker profiles. | Medium | Project proposal | The Administrator can create, edit and deactivate departments, categories and worker profiles. |
| F-021 | The system allows users to delete their account. | Medium | General Data Protection Regulation | After the user confirms the deletion, their account and personal data (name, email, notifications, ratings) are permanently deleted and they are signed out. Their reports and status changes remain without any link to the deleted user. The last active Administrator account cannot be deleted, and the user is told why. |

---

## 2.2 Non-Functional Requirements

**Objective:** Specify the important quality properties and operating conditions of the approved application in a way the team can reasonably check.

| ID | Description | Priority | Source |
| --- | --- | --- | --- |
| NF-01 | A citizen can submit a complete report (category, photo and map location) in under 60 seconds. Checked by timing at least 5 test users. The median time must be under 60 s. | High | Project proposal |
| NF-02 | The public map with up to 500 reports loads in under 3 seconds on a standard broadband connection, and applying a filter updates the map in under 1 second. Checked with a seeded test database. | High | Project proposal |
| NF-03 | The system responds to 95% of common requests (sign-in, report list, report status) in under 2 seconds with 50 simultaneous users. Checked with a load-testing tool such as k6 or JMeter. | Low | Team decision |
| NF-04 | Faces and vehicle license plates in uploaded photos are blurred before the photo is visible to the public, and no unblurred version is reachable through a public link. Checked on a test set of at least 20 photos. At least 90% of faces and plates must be blurred. | Low | Project proposal |
| NF-05 | All communication between the application and the server uses HTTPS, no user passwords are stored, and API keys are not kept in the source code repository. Checked by inspecting the deployed site, the database and the repository. | High | Course requirement |
| NF-06 | Each user can access only the functions of their role (Citizen, City Worker, Administrator). Checked by attempting every restricted action with each role. Unauthorized attempts must be denied. | High | Project proposal |
| NF-07 | The public map and its data show only the category, status, date, address, description and photos of a report, and never the reporter's name or email. Checked by viewing the map and its API responses while signed out. | High | Project proposal |
| NF-08 | Submitted reports, status changes and comments are still present after a server restart. Checked by restarting the application and comparing the data before and after. | High | Team decision |
| NF-09 | A citizen can still submit a report with a pin placed on the map when the address lookup is unavailable, and the system shows an error message without losing the entered data. Checked by blocking the Google Maps API in a test. | Low | Project proposal |
| NF-10 | A citizen can still choose a report location manually on the map after denying geolocation access. Checked by denying the browser permission, choosing a map point and submitting a report. | Low | Project proposal |
| NF-11 | An in-app notification appears within 10 seconds of a report's status change, and the Google Calendar event with 24-hour and 2-hour reminders is created within 30 seconds of an assignment. Checked by measuring the time in a test run. | Medium | Project proposal |
| NF-12 | The application is usable on mobile phone screens from 360 px width and in the latest versions of Chrome, Safari and Firefox, without horizontal scrolling or overlapping elements. Checked manually on at least 3 devices or browser emulators. | High | Project proposal |
| NF-13 | At least 80% of first-time test users (at least 5 people) can submit a report and find its status without instructions. Checked with a short usability test. | Low | Project proposal |
| NF-14 | Text contrast meets WCAG 2.1 AA and the Lighthouse accessibility score is at least 90 on the main pages. Checked with the Lighthouse tool. | Low | Team decision |
| NF-15 | Automated tests cover at least 60% of the backend code, and every change is merged through a reviewed pull request. Checked with the coverage report and the repository history. | Low | Team decision |

## 2.3 Stakeholders and Actors

**Objective:** Identify roles that affect requirements and distinguish stakeholders from actors who interact with the application.

| Role or actor ID | Relation to the system | Relevant requirements |
| --- | --- | --- |
| A-01 Citizen | Primary actor. Reports issues, follows their status, rates resolutions and can delete their account. | F-001, F-003, F-007, F-018, F-021, NF-01, NF-07, NF-09, NF-10, NF-12, NF-13 |
| A-02 City Worker | Primary actor. Receives assigned issues, updates their status, documents completed repairs and can delete their account. | F-002, F-011, F-012, F-014, F-015, F-021, NF-06, NF-11, NF-12 | 
| A-03 Administrator | Primary actor. Validates reports, assigns them to workers, manages accounts and departments, monitors statistics and can delete their account unless they are the last Administrator. | F-002, F-009, F-010, F-017, F-019, F-020, F-021, NF-06 |

---

## 2.4 Constraints and Assumptions

**Objective:** Record project-specific boundaries and assumptions that affect requirements or design, including their source and practical consequence. This is their authoritative location.

| ID | Constraint or assumption | Source | Consequence or way to verify |
| --- | --- | --- | --- |
| C-01 | **Constraint:** Users sign in only through an external identity provider using OAuth 2.0/OpenID Connect, and the system stores no passwords. | Course requirement | There is no registration or password recovery in the application. Verify that the sign-in page offers only Google and that accounts created through Google sign-in have an unusable password (Django keeps a `password` column in the user table, but it is never set for these users). |
| C-02 | **Constraint:** The application has exactly three roles: Citizen, City Worker and Administrator. Citizen accounts are created on first sign-in. City Worker and Administrator accounts are created only by an Administrator. | Project proposal | Role-based access (NF-06) is built on these three roles. Verify that an unknown email gets a Citizen account only. |
| C-03 | **Constraint:** Maps, geocoding, navigation and the heatmap use the Google Maps API. | Project proposal | Address conversion, map display and duplicate detection depend on this service (see NF-09 for the fallback). Verify that no other map provider is used. |
| C-04 | **Constraint:** Assigned issues are written to the worker's Google Calendar using the Google Calendar API. | Project proposal | A worker without a Google account cannot receive calendar events. Verify with a test assignment (NF-11). |
| C-05 | **Constraint:** Photos are scanned for faces and license plates using the Google Cloud Vision API before public display, in line with GDPR. | Project proposal | No photo may be shown publicly before scanning finishes (NF-04). Verify with the photo test set. |
| C-06 | **Constraint:** Weather forecasts come from an external weather API (OpenWeatherMap or Open-Meteo). | Project proposal | The issue details page depends on this service. Verify that a forecast is shown for an assigned issue. |
| C-07 | **Constraint:** The application must follow GDPR for personal data such as photos and email addresses. | Project proposal | Public pages must not expose personal data (NF-07). Verify by viewing the public map signed out. |
| C-08 | **Constraint:** The application is developed by the team T3-Development (6 members) and must be finished and submitted by the course deadline. | Course requirement | The scope is limited to the approved features and what 6 people can build in the available time, so Low priority items are dropped first if time runs short. Verify against the team's task plan. |
| A-01 | **Assumption:** Citizens have a smartphone or computer with a camera, an internet connection and a Google account. | Team decision | Offline reporting is not supported. Verify by asking test users in the usability test (NF-13). |
| A-02 | **Assumption:** The email address the Administrator enters for a worker or administrator is the same one the person uses to sign in. | Project proposal | If the emails differ, the user gets only a Citizen account. Verify by testing sign-in with a matching and a different email. |
| A-03 | **Assumption:** The free usage limits of the Google and weather APIs are enough for the demo and testing. | Team decision | If a limit is exceeded, the affected feature may stop working. Verify by checking API usage during testing. |
| A-04 | **Assumption:** The application covers one city, and reports outside the city area are rejected by the Administrator as invalid. | Project proposal | Verify by marking a test report outside the city as rejected (F-009). |
| A-05 | **Assumption:** Face and license plate detection is good enough for the 90% target in NF-04. | Team decision | If detection is weaker, the team must change the target or review photos manually. Verify with the test set from NF-04. |

---

## 2.5 Significant Requirement Changes

**Objective:** Preserve the reason for changes that alter agreed scope, priority, or acceptance criteria, while keeping the current requirements above up to date.

| Date | Requirement ID | Change and reason | Agreed with / evidence |
| --- | --- | --- | --- |
| 16.10.2026 | NF-12 | All functionality is implemented as a responsive web application. The teaching assistant recommended a web application to keep the architecture consistent. | Teaching assistant (proposal feedback, 16.10.2026) |
| 25.10.2026 | NF-04 | Priority lowered from High to Low. Automatic blurring of faces and license plates will be implemented only if time allows (C-08). |  |
| 25.10.2026 | F-021 | Account deletion is available to all roles, not only to citizens, because City Workers and Administrators also have personal data covered by GDPR. The last active Administrator cannot be deleted, so the system always keeps someone who can manage accounts. | Implemented in `code/users/views.py` and `code/users/services.py` |
|  | NF-03 | Added by the team: a response-time target for common requests, so that performance can be checked with a load test. |  |
|  | NF-08 | Added by the team: reports, status changes and comments must survive a server restart, because the city relies on the report history. |  |
|  | NF-14 | Added by the team: an accessibility target (WCAG 2.1 AA, Lighthouse score of at least 90) for the main pages. |  |
|  | NF-15 | Added by the team: at least 60% backend test coverage and a reviewed pull request for every change. |  |
|  | A-01 | Added by the team: citizens are assumed to have a device with a camera, an internet connection and a Google account. |  |
|  | A-03 | Added by the team: the free limits of the Google and weather APIs are assumed to be enough for the demo and testing. |  |
|  | A-05 | Added by the team: face and license plate detection is assumed to reach the 90% target in NF-04. |  |

---

## 2.6 Requirement Traceability

**Objective:** Show where important requirements are described in use cases, where relevant, and where they are checked.

The status reflects the code at commit `f56182d` on the main branch.

| Requirement ID | Use case or design location | Test or verification location | Status |
| --- | --- | --- | --- |
| F-001 | UC-001 | Manual check: sign in with a Google account | Implemented – not tested yet |
| F-002 | UC-001, UC-014 | Planned – testing phase | Partially implemented – an account created with the same email is linked on Google sign-in. Departments are not yet assigned |
| F-003 | UC-002, UC-004 | Unit tests: `code/issues/tests.py` (`ReportCreateTests`) | Implemented – report form, location selection and photo upload to Cloudinary (`views.report_create`, `services.create_report`). 6 tests pass |
| F-004 | UC-002 | Manual check in the report form | Implemented – not tested yet (address suggestions and reverse geocoding in `report_form.js`) |
| F-005 | UC-003 | Planned – testing phase | Pending – not tested yet |
| F-006 | UC-005 | Unit tests: `code/issues/test_map_view.py` (`MapViewTests`) | Implemented – public map at `/map/` with category, status and date range filters, reset, grouped markers and an empty-result message (`views_map.map_view`, `map.html`, `issues_map.js`). Rejected and duplicate reports are hidden. 3 tests pass |
| F-007 | UC-006 | Unit tests: `code/issues/tests.py` (`MyReportsTests`) | Partially implemented – "My reports" list (`views.my_reports`) shows only the citizen's own reports. The report details and history page is missing |
| F-008 | UC-006, UC-009, UC-012 | Unit tests: `code/issues/tests.py` (`NotificationTests`) | Implemented – `Issue.change_status()` creates a notification in the same transaction. Notifications page and unread counter in the navigation bar (`services.notify`, `views.notifications`). 6 tests pass |
| F-009 | UC-012 | Planned – testing phase | Partially implemented – the Administrator verifies or rejects a report with a note (`views_admin.review_issue`). Marking a report as a duplicate is missing |
| F-010 | UC-013 | Planned – testing phase | Partially implemented – assignment with worker and deadline, and the worker is notified (`views_admin.assign_issue`). Priority and department filter are missing |
| F-011 | UC-008 | Planned – testing phase | Partially implemented – list of assigned issues sorted by deadline (`views_worker.worker_task_list`). Map view is missing |
| F-012 | UC-009 | Planned – testing phase | Partially implemented – status changes Assigned → In Repair → Resolved with history (`views_worker.update_task_status`). Comments are missing |
| F-013 | UC-006, UC-007, UC-009, UC-010 | Planned – testing phase | Pending – not tested yet |
| F-014 | UC-011 | Planned – testing phase | Pending – not tested yet |
| F-015 | UC-013 | Planned – testing phase | Pending – not tested yet |
| F-016 | UC-008, UC-013 | Planned – testing phase | Pending – not tested yet |
| F-017 | UC-017 | Planned – testing phase | Pending – not tested yet |
| F-018 | UC-007 | Planned – testing phase | Pending – not tested yet |
| F-019 | UC-015 | Planned – testing phase | Pending – not tested yet |
| F-020 | UC-014 | Planned – testing phase | Pending – not tested yet |
| F-021 | UC-016 | Planned – testing phase | Implemented – not tested yet (`users/views.py`, `users/services.py`) |
| NF-01 | UC-002, UC-004 | Planned – testing phase | Pending – not tested yet |
| NF-02 | UC-005 | Planned – testing phase | Pending – not tested yet |
| NF-03 | UC-001, UC-005, UC-006 | Planned – testing phase | Pending – not tested yet |
| NF-04 | UC-004, UC-005 | Planned – testing phase | Pending – not tested yet |
| NF-05 | UC-001 | Planned – testing phase | Pending – not tested yet |
| NF-06 | UC-001, UC-014 | Unit tests: `code/users/tests.py` (`RolePermissionTests`) | Passed – 6 role-permission tests (whole suite 25/25, commit f56182d). Checks with the real views are pending |
| NF-07 | UC-005 | Unit tests: `code/issues/test_map_view.py` (`MapViewTests`) | Passed – the map data contains no reporter name or email. Check while signed out in the browser is pending |
| NF-08 | UC-002, UC-006, UC-009 | Planned – testing phase | Pending – not tested yet |
| NF-09 | UC-002 | Planned – testing phase | Pending – not tested yet |
| NF-10 | UC-002 | Planned – testing phase | Pending – not tested yet |
| NF-11 | UC-006, UC-009, UC-012, UC-013 | Planned – testing phase | Pending – not tested yet |
| NF-12 | All use cases | Planned – testing phase | Pending – not tested yet |
| NF-13 | UC-002, UC-006 | Planned – testing phase | Pending – not tested yet |
| NF-14 | All use cases | Planned – testing phase | Pending – not tested yet |
| NF-15 | Project-wide (repository) | Planned – testing phase | Pending – not tested yet |

---

## 2.7 Review of Requirements

**Objective:** Record meaningful feedback on requirements and the resulting decisions at the two formal project checkpoints, in weeks 7 and 14.

| Checkpoint | Feedback or finding | Resulting requirement or scope decision |
| --- | --- | --- |
| Week 7 – first review (teaching assistant, 19.11.2026) | Requirements and constraints with "Team decision" as their source should be tracked in 2.5 and confirmed by someone. The use case and class diagrams should be PlantUML models, like the component diagram. README.md and Home.md should be filled in. | Every requirement with "Team decision" as its source is listed in 2.5 for confirmation. The use case, class and ER diagrams were converted to PlantUML (see [3.1](./3-Use-Cases.md) and [4.3](./4-Architecture-and-Design.md)). README.md and Home.md are being filled in. |
| Week 14 – final review | Pending – no feedback recorded yet. | Pending – no decision yet, see 2.5. |
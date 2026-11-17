# 5. Testing

**Objective:** Show how the team checks the application's important behavior, what was actually tested, what the results show, and which known defects remain. A planned test is not evidence of a successful run.

The expandable Crisis Guard examples illustrate test design and reporting. They are not results from the published student project. Keep the requirement-to-use-case-to-test mapping in the [requirement traceability table](2.-Requirements); record test specifications and execution evidence here or link to the tests in the repository.

## 5.1 Test Approach

**Objective:** Select checks that address the main user goals, important failure conditions, and project-specific non-functional requirements.

**Testing approach:** [In a few sentences, name the components or rules tested in isolation, the main interactions checked in the running application, and the relevant non-functional checks. State which checks are automated, which are manual, and where the team keeps their evidence.]

Choose normal cases, boundaries, and failures that expose different behavior. Selenium IDE can record and replay a basic browser interaction; Selenium WebDriver can express a browser check in code. Use Selenium or another suitable tool when it helps make a system check repeatable. State which tool the team actually uses. A test of a class or rule belongs at the component level; opening a form in a browser checks the running system. Name a CI workflow and its run only if the team uses CI.

<details>
<summary><strong>Choosing checks for report submission</strong></summary>

**Example — Crisis Guard:** The team tests location validation and report-state changes directly with controlled inputs. It then checks report submission and its error messages in a running browser using Selenium WebDriver. A separate check attempts report approval without moderator permission. If notification delivery belongs to the approved scope, a test examines recipient selection; an end-to-end delivery test also needs a working notification provider. Browser geolocation denial is checked with a manual location fallback. The automated test code is kept in Git, and each executed result refers to a specific run.

**Analysis of the example:** A validation rule can pass while the full submission still fails. Browser and component tests therefore answer different questions. The notification example separates recipient-selection logic from actual delivery. Neither a named tool nor a screenshot by itself proves that an entire interaction passed.

</details>

## 5.2 Test Cases

**Objective:** Make important checks reproducible by recording the scenario, input, steps, expected result, and result of execution. Give each check a stable ID that can be used in the requirement traceability table.

| Test Case ID | Test Scenario | Input Data | Expected Results | Actual Results | Pass/Fail | Test Steps |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

The scenario identifies the functionality being tested. Enter the observed result and **Pass**, **Fail**, or **Blocked** only after a run; until then use **Not run**. Test steps must let another team member reproduce the check. Keep automated test source code in the project Git repository and link to it from the relevant case; for a manual check, document the steps here. Select normal cases, meaningful invalid inputs or boundaries, failures, and relevant quality properties. A feature that has not been implemented is unfinished scope; testing how the application handles an invalid ID is a valid negative test.

<details>
<summary><strong>Report submission cases at two test levels</strong></summary>

**Example — Crisis Guard test cases:** One failed result, ST-02, illustrates how a completed case differs from planned cases marked **Not run**. Dates, revision, environment, and evidence for the example run appear below.

| Test Case ID | Test Scenario | Input Data | Expected Results | Actual Results | Pass/Fail | Test Steps |
| --- | --- | --- | --- | --- | --- | --- |
| CT-01 | Component: valid location | Flood; latitude 45.82; longitude 16.00. | Coordinates accepted. | Not run. | Not run | Call the location validator with both coordinates; assert valid result. |
| CT-02 | Component: missing location | Flood; latitude and longitude absent. | Validation rejects submission; nothing is saved. | Not run. | Not run | Call validation with no location; assert rejection and no save. |
| CT-03 | Component: coordinate boundary | First (90, 180), then (90.01, 180). | Boundary accepted; value beyond it rejected. | Not run. | Not run | Run the validation test with both inputs; compare outcomes. |
| CT-04 | Component: report transition | Report in SUBMITTED state; rejection, then approval. | Approval rejected; status remains REJECTED. | Not run. | Not run | Reject the report; call approve; inspect resulting status. |
| CT-05 | Component: missing report | Repository contains no report with ID 9999. | Defined not-found outcome; no fabricated report. | Not run. | Not run | Request ID 9999 against controlled repository data; assert not found. |
| CT-06 | Component: notification recipients | Confirmed flood near region A; one subscription to region A and one to region B. | Only eligible recipient in region A selected. | Not run. | Not run | Invoke recipient selection with the two subscriptions; compare IDs. |
| CT-07 | Component: invalid disaster type | A report contains an disaster type outside the supported set. | Validation rejects the type; no report is saved. | Not run. | Not run | Supply the unsupported value to report validation; assert rejection. |
| ST-01 | System: valid report submission | Flood; High; selected map location 45.82, 16.00. | Confirmation appears; report can be retrieved. | Not run. | Not run | Open form; enter data; select point; submit; open resulting report. |
| ST-02 | System: required location missing | Flood; High; description “Water rising”; location empty. | Location-specific error appears; report count does not increase. | Generic server error shown; report count stayed at 24. | Fail | Open form; enter data without location; submit; compare report count before and after. |
| ST-03 | System: geolocation permission denied | Browser permission denied; Flood; manually chosen map point. | User can select location manually and submit the report. | Not run. | Not run | Deny permission; select point on map; submit; inspect confirmation. |
| ST-04 | System: protected report review | Signed-in citizen without moderator role; report ID 104. | Approval refused; report remains unchanged. | Not run. | Not run | Try approval through the application/API; inspect response and report state. |
| ST-05 | System: backend unavailable | Valid flood report details; backend deliberately unavailable in a test environment. | Application reports the failure and does not falsely confirm submission. | Not run. | Not run | Disable the test backend; submit through the browser; inspect the message and recovery behavior. |

**Analysis of the example:** Component cases exercise rules directly; system cases exercise visible behavior across the running application. CT-03 demonstrates an actual boundary and a value just beyond it; a vague phrase such as “very long input” would not establish a boundary. If the team adopts the location-fallback quality requirement NF-01, ST-03 can also check it; do not create a second case with identical steps merely to produce a non-functional test ID. CT-06 and ST-04 depend on the approved features. The rows show a range of techniques and one example failure; they do not set a case-count quota. A performance or availability target needs an agreed threshold and a feasible measurement procedure before it becomes a project test.

**ST-02 reproduction detail:** Before the action, count stored reports in the test database (24 in this example run). Open the form; choose Flood and High severity; enter “Water rising”; leave location empty; submit; observe the message and check the database count again. Record the application revision, the displayed error, and the two counts. The generic error fails the expected location-specific explanation even though the count remains 24.

</details>

<details>
<summary><strong>From report-submission steps to Selenium actions</strong></summary>

**Example — Crisis Guard, ST-01:** The case uses a manual coordinate field in this teaching design. Selector names below represent elements in this example's form; a team must inspect its own application rather than copy these identifiers. Selenium IDE can record the interaction, but the recorded case still needs an assertion about the result. Selenium WebDriver permits the team to write the actions and assertions in a versioned test.

| Step | Human-readable procedure | Selenium WebDriver action in the example |
| --- | --- | --- |
| 1 | Open the report form. | Navigate to the test application's report-form URL. |
| 2 | Choose Flood as the disaster type. | Locate the `disasterType` select element and choose `Flood`. |
| 3 | Choose High severity. | Locate the `severity` select element and choose `High`. |
| 4 | Enter the report location. | Locate `locationInput` and enter `45.82, 16.00`. |
| 5 | Describe the disaster. | Locate `description` and enter `Flooding in the city center`. |
| 6 | Submit the form. | Locate and click `submitReport`. |
| 7 | Check the result. | Wait for `reportConfirmation`; assert that it contains a report reference; open the report and verify its description. |

**WebDriver fragment (JavaScript):**

```js
const { By, until } = require('selenium-webdriver');
const assert = require('assert');

await driver.get(baseUrl + '/reports/new');
await driver.findElement(By.id('incidentType')).sendKeys('Flood');
await driver.findElement(By.id('severity')).sendKeys('High');
await driver.findElement(By.id('locationInput')).sendKeys('45.82, 16.00');
await driver.findElement(By.id('description')).sendKeys('Flooding in the city center');
await driver.findElement(By.id('submitReport')).click();

const confirmation = await driver.wait(
  until.elementLocated(By.id('reportConfirmation')), 10000);
assert((await confirmation.getText()).includes('Report'));

const reportUrl = await driver.findElement(By.id('createdReportLink'))
  .getAttribute('href');
await driver.get(reportUrl);
assert((await driver.findElement(By.id('reportDetails')).getText())
  .includes('Flooding in the city center'));
```

**Analysis of the example:** The seventh step asserts the confirmation and verifies that the submitted report can be retrieved. An explicit wait gives the application time to display an asynchronous confirmation. The selectors, route, and confirmation wording must match the team's UI; recording a flow without checking the expected result is not evidence that the test passed. Version the automated test and save the run result.

</details>

<details>
<summary><strong>Performance, usability, and security cases</strong></summary>

**Example — Crisis Guard:** These additional cases show the kinds of checks represented in the earlier course material. Targets for load or task completion apply only when the team has an agreed requirement and a feasible way to measure it. All six cases below are **Not run** in this teaching example.

| Test Case ID | Test Scenario | Input Data | Expected Results | Actual Results | Status | Test Steps |
| --- | --- | --- | --- | --- | --- | --- |
| NF-P-01 | Performance: report-list load | 20 concurrent readers for two minutes; database seeded with 100 reports. | If the approved target is a 2 s 95th-percentile response and at most 1% failed requests, both measured values meet it. | Not run. | Not run | Seed reports; run JMeter or a suitable load tool; record response times, error rate, and hosting configuration. |
| NF-P-02 | Performance: higher load | Increase readers from 20 to 40, then 80 with the same dataset. | Record the load at which the agreed latency or error-rate target is first exceeded; do not claim a pass without a target. | Not run. | Not run | Increase load in stages; preserve the tool report and note when errors first appear. |
| NF-U-01 | Usability: submit a flood report | Three participants new to the interface; each receives the same reporting task. | Each participant can locate the form, enter a location, and submit without assistance; report time and difficulties. | Not run. | Not run | Give the task; observe attempts; record completion, time, and points of confusion. |
| NF-U-02 | Accessibility: keyboard-only submission | Keyboard navigation; manual location-entry option. | The user can reach all required fields, select a location, submit, and read the confirmation without a pointer. | Not run. | Not run | Navigate with keyboard only; record focus order and the result. |
| NF-S-01 | Security: report input treated as data | Description contains the string `' OR '1'='1` in a controlled test environment. | No unintended query result, unauthorized access, or server failure; the input is handled as data. | Not run. | Not run | Submit the string; inspect response and stored result; review relevant test logs. |
| NF-S-02 | Security: invalid identity for review | Expired or invalid sign-in token; attempt to approve report 104. | Request rejected; report 104 remains unchanged. | Not run. | Not run | Call the protected action with the invalid identity; inspect response and report state. |

**Analysis of the example:** The load example requires recorded percentiles and errors, not a statement that the application “handled 1,000 users.” The three-person observation is evidence about those attempts, not proof of general usability. The security rows test defined behavior; one input string does not establish that the application is secure. NF-S-02 is relevant only when protected report review is part of the approved scope. A system test may also provide evidence for a non-functional requirement: ST-03 already checks the manual-location fallback, so repeating the same steps under a new ID adds no value.

</details>

## 5.3 Executed Tests and Results

**Objective:** Give the application revision, environment, and evidence needed to interpret the actual results in the test-case table. Add a short run record when those details cannot be conveyed by a test-code or CI run link.

**Latest run or evidence:** [Link to CI run, manual test note, or a short run summary, with date, revision, and environment.]

The **Actual Results** and **Pass/Fail** columns above are the authoritative per-case outcomes. Do not copy all case results into another mandatory table. Record failed and blocked runs honestly; when rerunning a test, retain its relevant history rather than presenting an old pass as the current result.

<details>
<summary><strong>Recording a failed run without inventing a pass</strong></summary>

**Example — Crisis Guard review scenario:** During a run of ST-02, the user submits a report without selecting a location. The application shows a generic server error instead of identifying the missing field.

| Test ID or run | Date and application revision | Environment | Observed result and outcome | Evidence |
| --- | --- | --- | --- | --- |
| ST-02 | 20 September 2026; revision `7a12c4e` | Local test deployment; Chrome; API at `localhost:8080` | **Failed:** generic server error shown instead of the location-specific message. Report count was 24 before and after submission. | `tests/evidence/ST-02-error.png`; `tests/evidence/ST-02-db-check.txt`; issue #18 |

**Analysis of the example:** The revision and environment make the run identifiable; the screenshot supports the observed message, while the recorded report counts support the separate claim that nothing was saved. The issue tracks the defect. These dates, revision, file path, and issue number belong to this example scenario, not to the published student project. After a fix, rerun ST-02 and update its result; keep the earlier failure in the run or issue history.

</details>

## 5.4 Known Defects and Testing Limits

**Objective:** Let a reader see defects that affect use of the current application and important behavior the team could not verify.

| Issue or limitation | User-visible effect or unverified behavior | Evidence or issue link |
| --- | --- | --- |
|  |  |  |

Keep detailed bug reproduction and progress in the issue tracker, with a brief pointer here for defects that materially affect the application or demonstration. If a required feature is unfinished, state that clearly in the final results; do not call it a known defect or a passing test. Note a missing test capability honestly, such as an external provider unavailable during a run. This section does not require a second complete issue log.

<details>
<summary><strong>Separating a failed check from an unverified integration</strong></summary>

**Example — Crisis Guard:**

| Issue or limitation | User-visible effect or unverified behavior | Evidence or issue link |
| --- | --- | --- |
| Missing-location error is generic | The citizen cannot tell what must be corrected before submitting a report. | Example issue #18; ST-02 run evidence. |
| Notification provider was unavailable during the test | The team has not verified notification delivery in that run. Report submission may still work. | Example blocked run record `tests/evidence/notification-blocked.txt`. |

**Analysis of the example:** The first row describes an observed defect; the second describes a limit of the available evidence. Neither should be presented as a successful notification test. Remove or update the row when the team's recorded evidence changes.

</details>

**Final consistency check:** Test IDs and expected outcomes match the applicable requirements and use cases. Executed results refer to a real application revision and an inspectable run or reproducible observation. Important failures and open defects remain visible, while the final description of delivered features reflects what the tests and running application support.

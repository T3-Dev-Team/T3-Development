# 1. Project Scope

**Objective:** Explain the approved project task in the team's own words. A reader should understand the problem, intended users, project objective, and boundaries without first reading the detailed requirements.

## 1.1 Problem and Project Objective

**Objective:** State the problem, what the approved application aims to enable, and the expected benefit for its intended users.

[Problem, objective, and expected benefit in the team's own words; link to the approved task if available.]

<details>
<summary><strong>Expected benefits and supporting evidence</strong></summary>

**Example — Crisis Guard:** “During severe weather, a citizen may need to find reports relevant to their location. Crisis Guard aims to present location-specific disaster reports on a map so that the citizen can find them in one place.” This names the problem, intended user, proposed capability, and expected benefit. It does **not** claim a measured reduction in response time or integration with an emergency dispatch service. A team still needs to describe the scope approved for its own project.

 “The application reduces disaster response time by 30% based on simulations.” The number makes the proposed benefit vivid, but it also calls for a check: **where is the simulation and how was the percentage calculated?** If there is no such evidence, state the expected benefit without a numeric result.

</details>

## 1.2 Intended Users and Stakeholders

**Objective:** Identify the people or organizations whose needs define the task.

| User or stakeholder group | Need or interest relevant to this project |
| --- | --- |
|  |  |

<details>
<summary><strong>Users, stakeholders, and an optional persona</strong></summary>

**Example — Crisis Guard:**

| User or stakeholder group | Need or interest relevant to this project |
| --- | --- |
| Citizen | Find nearby disaster information and submit a report with a location. |
| Organization coordinating assistance | See reports relevant to the area and available resources, if coordination is within the approved scope. |

These are distinct needs, not two fictional biographies. An actor interacts with the application; a course demonstrator interested in the result need not be an application actor. Use the roles and permissions from your approved task. A persona is optional when it helps resolve a specific design question.

**Optional persona example:** Jane, a disaster management officer, needs current resource information to allocate assistance. This can help when the team must decide what a manager needs to see first. Write a persona only if it explains a design choice; a list of fictional biographies is not a course deliverable.

</details>

## 1.3 Project Boundaries

**Objective:** State the principal capabilities within the approved task, important exclusions, and indispensable external dependencies.

**Included:** [Principal capabilities.]  
**Excluded or deferred:** [Important excluded capabilities and a brief reason.]  
**External dependencies:** [Essential services or information sources, if any.]

<details>
<summary><strong>Defining the first project boundary</strong></summary>

**Example — Crisis Guard:**  
**Included:** Submitting a located disaster report and viewing reports on a map.  
**Excluded:** Dispatching emergency services automatically; showing a report does not authorize or initiate an official dispatch.  
**External dependency:** A map provider supplies the map view; the application retains responsibility for its own report data.

This is a concrete boundary because it separates presenting information from official emergency response and identifies which system supplies the map. The exclusion and dependency are part of the **teaching scenario**, not a claim about what the published application implements; the team's approved scope and application determine those facts.

**Another example of useful boundary:** Start with flood response coordination for the first implementation. Name the types of incidents or users covered by the approved project rather than promising every emergency workflow. Mention speculative AI prediction or VR training as future work only when they are meaningful next steps, not as presumed first-release features.

An assertion such as “modular architecture enables rapid deployment in new regions” needs an actual design basis. Do not promise adaptability here solely because it sounds like a project benefit.

Keep this overview at the level of scope: identify the main capability and its boundary without listing every requirement or design detail. Report what was actually completed and what remains unfinished in the final results, not in this initial description.

</details>

## 1.4 Existing Approaches and Project Rationale

In Lisbon, a resident who spots a problem in the street can report it through Na Minha Rua Lx, the city council's app and website, which has been running since June 2017 [1]. It does the basics well, since an academic study found that reporting and tracking work fine, but it lacks some advanced features such as data visualization [2], and press coverage of another study points to duplicate requests and reports marked as done when nothing was actually fixed [3]. These are the gaps CityFix wants to address with duplicate detection, photo proof of repair, and a heatmap for administrators. It is meant to complement existing municipal services, not replace them.

### Sources
 
1. Notícias ao Minuto. *Higiene urbana em Lisboa motiva maioria das ocorrências na 'Na Minha Rua'*. <https://www.noticiasaominuto.com/pais/2598480/higiene-urbana-em-lisboa-motiva-maioria-das-ocorrencias-na-na-minha-rua>
2. Soares, J., & Coutinho, C. (2024). *Urban issue reporting applications towards government 2.0*. ISMSIT 2024, IEEE. <https://doi.org/10.1109/ISMSIT63511.2024.10757230>
3. Time Out Lisboa (2024). *Higiene urbana é, de longe, a principal preocupação de quem vive em Lisboa*. <https://www.timeout.pt/lisboa/pt/noticias/higiene-urbana-e-de-longe-a-principal-preocupacao-de-quem-vive-em-lisboa-071624>
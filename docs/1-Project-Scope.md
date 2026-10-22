# 1. CityFix Project Scope

## 1.1 Problem and Project Objective

Urban areas frequently experience infrastructure problems, such as potholes, damaged sidewalks, broken streetlights, and illegal waste disposal. Reporting these problems to municipal authorities can be complicated, and citizens may not know whether their reports have been received or resolved.

The objective of CityFix is to develop a web application that simplifies communication between citizens and municipal services. The application will allow citizens to report infrastructure problems, administrators to review and assign reports, and city workers to manage and document repairs.

The system aims to improve transparency, simplify the reporting process, and make municipal maintenance more efficient.

## 1.2 Intended Users and Stakeholders

The primary users of CityFix are:

-**Citizens:** Report infrastructure problems, upload pictures, specify locations and track the completion of the problem.
-**City Workers:** Assign issues overview, route planning, update the progress, make a proof and documentation of a repair and return an issue.
-**Administrator:** Report validating, assignment of priorities and deadlines, monitoring and profile checking.

The stakeholders are municipal services, local communities and external service providers that support mapping, scheduling, weather forecasts, and image processing.

## 1.3 Project Boundaries

The project includes the development of a responsive web application with the following features:

- User authentication and role-based access.
- Infrastructure issue reporting with photographs, descriptions, categories, and locations.
- An interactive map with filtering options.
- Report validation and task assignment by administrators.
- Task management and repair-status updates for city workers.
- Citizen notifications and report tracking.
- Administrative statistics and geographical visualizations.

Additional features may include duplicate report detection, calendar integration, weather forecasts, automated image blurring, deadline alerts, and citizen feedback.

The project does not include performing physical repairs, controlling municipal equipment, or replacing existing municipal management systems. External integrations will depend on available services and development resources.


## 1.4 Existing Approaches and Project Rationale

In Lisbon, a resident who spots a problem in the street can report it through Na Minha Rua Lx, the city council's app and website, which has been running since June 2017 [1]. It does the basics well, since an academic study found that reporting and tracking work fine, but it lacks some advanced features such as data visualization [2], and press coverage of another study points to duplicate requests and reports marked as done when nothing was actually fixed [3]. These are the gaps CityFix wants to address with duplicate detection, photo proof of repair, and a heatmap for administrators. It is meant to complement existing municipal services, not replace them.

### Sources
 
1. Notícias ao Minuto. *Higiene urbana em Lisboa motiva maioria das ocorrências na 'Na Minha Rua'*. <https://www.noticiasaominuto.com/pais/2598480/higiene-urbana-em-lisboa-motiva-maioria-das-ocorrencias-na-na-minha-rua>
2. Soares, J., & Coutinho, C. (2024). *Urban issue reporting applications towards government 2.0*. ISMSIT 2024, IEEE. <https://doi.org/10.1109/ISMSIT63511.2024.10757230>
3. Time Out Lisboa (2024). *Higiene urbana é, de longe, a principal preocupação de quem vive em Lisboa*. <https://www.timeout.pt/lisboa/pt/noticias/higiene-urbana-e-de-longe-a-principal-preocupacao-de-quem-vive-em-lisboa-071624>



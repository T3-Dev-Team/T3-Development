# 1. CityFix Project Scope

## 1.1 Problem and Project Objective

Urban areas frequently experience infrastructure problems, such as potholes, damaged sidewalks, broken streetlights, and illegal waste disposal. Reporting these problems to the city authorities can be complicated, and citizens may not know whether their reports have been received or resolved.

The objective of CityFix is to develop a web application that simplifies communication between citizens and the city departments responsible for repairs. The application will allow citizens to report infrastructure problems, administrators to review and assign reports, and city workers to manage and document repairs.

The system aims to improve transparency, simplify the reporting process, and make public infrastructure maintenance more efficient.

## 1.2 Intended Users and Stakeholders

The primary users of CityFix are:

- **Citizens:** report infrastructure problems with photos and a location, and follow each report until it is resolved.

- **City Workers:** see the issues assigned to them, update their progress, document a completed repair with a photo, and return an issue they cannot resolve.

- **Administrators:** validate reports, set priorities and deadlines, assign issues to City Workers, manage accounts and departments, and monitor statistics.

The stakeholders are the city administration and its departments, local communities and external service providers that support mapping, scheduling, weather forecasts and photo storage.

## 1.3 Project Boundaries

The project includes the development of a responsive web application with the following features:

- Sign-in with a Google account and role-based access for Citizens, City Workers and Administrators.
- Infrastructure issue reporting with photographs, descriptions, categories and locations, including detection of possible duplicate reports and automatic blurring of faces and license plates.
- An interactive map of public reports with filtering options.
- Report validation, prioritisation and assignment to City Workers by Administrators.
- Task management and repair-status updates for City Workers, with a photo as proof of each completed repair.
- In-app notifications and report tracking for citizens, and rating of resolved reports.
- Integration of assignments with Google Calendar and weather forecasts for issue locations.
- Deadline alerts for overdue issues, and administrative statistics with a heatmap of reports.

The detailed, prioritised requirements are in [2. Requirement Analysis](./2-Requirements.md). Lower-priority items are dropped first if time runs short (C-08).

The project does not include performing physical repairs, controlling city equipment, or replacing the management systems the city already uses. External integrations will depend on available services and development resources.

## 1.4 Existing Approaches and Project Rationale

In Lisbon, a resident who spots a problem in the street can report it through Na Minha Rua Lx, the city council's app and website, which has been running since June 2017 [1]. It does the basics well, since an academic study found that reporting and tracking work fine, but it lacks some advanced features such as data visualization [2], and press coverage of another study points to duplicate requests and reports marked as done when nothing was actually fixed [3]. These are the gaps CityFix wants to address with duplicate detection, photo proof of repair, and a heatmap for administrators. It is meant to complement the services local governments already offer, not replace them.

### Sources
 
1. Notícias ao Minuto. *Higiene urbana em Lisboa motiva maioria das ocorrências na 'Na Minha Rua'*. <https://www.noticiasaominuto.com/pais/2598480/higiene-urbana-em-lisboa-motiva-maioria-das-ocorrencias-na-na-minha-rua>
2. Soares, J., & Coutinho, C. (2024). *Urban issue reporting applications towards government 2.0*. ISMSIT 2024, IEEE. <https://doi.org/10.1109/ISMSIT63511.2024.10757230>
3. Time Out Lisboa (2024). *Higiene urbana é, de longe, a principal preocupação de quem vive em Lisboa*. <https://www.timeout.pt/lisboa/pt/noticias/higiene-urbana-e-de-longe-a-principal-preocupacao-de-quem-vive-em-lisboa-071624>
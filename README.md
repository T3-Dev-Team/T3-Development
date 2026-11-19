# CityFix

CityFix lets citizens report problems in the city, such as potholes or broken streetlights, on a map and follow how the city resolves them.

**Course project:** This application was developed by a student team as part of the [Software Engineering](https://www.fer.unizg.hr/predmet/proinz) course at the Faculty of Electrical Engineering and Computing (FER), University of Zagreb.

## App Description

Citizens often do not know where to report a problem in their street, and once they report it they rarely find out what happened to it. CityFix gives citizens one place to report an issue with a photo and a location, lets the city's administrators validate reports and assign them to City Workers, and shows everyone the current status of each report.

**Key features (implemented at checkpoint 1)**

- Sign-in with a Google account, with separate functions for Citizens, City Workers and Administrators
- Reporting an issue with a category, description, photo and a location chosen on the map
- A public map of reports with filters by category, status and date range
- "My reports" and in-app notifications when the status of a report changes
- Validation and assignment of reports by the Administrator, and status updates by the City Worker

Planned features (duplicate detection, Google Calendar events, weather forecast, statistics and ratings) and their current status are listed in [2.6 Requirement Traceability](docs/2-Requirements.md#26-requirement-traceability). For the scope, requirements, use cases and design, see the [documentation](docs/Home.md).

<a id="deployment"></a>
## Deployment

**Live application:** <https://t3-development.onrender.com>

**Explore:** Open the map to see the public reports without signing in. Sign in with a Google account to report an issue and follow it under "My reports".

**Demo:** Any Google account can sign in and gets a Citizen account. City Worker and Administrator accounts are created by an Administrator. Ask the team for access to these roles.

**Limitations:** The application runs on Render's free plan, so the first request after a period of inactivity can take up to a minute. Features that are not yet implemented are listed in [2.6 Requirement Traceability](docs/2-Requirements.md#26-requirement-traceability).

The application runs as a Docker container on Render, with a PostgreSQL database. The deployment diagram is in [`docs/assets/diagrams/deployment_diagram.svg`](docs/assets/diagrams/deployment_diagram.svg).

<a id="quick-start"></a>
## Quick Start / Installation

**Prerequisites:** Python 3.12 or newer and Git. Without a database URL the application uses a local SQLite database, so PostgreSQL is not needed for local development.

```bash
git clone https://github.com/T3-Dev-Team/T3-Development
cd T3-Development/code
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Address:** <http://127.0.0.1:8000/>

**Configuration:** The application reads its settings from environment variables. Values are never committed to the repository. Ask the team for the development values.

| Variable | Purpose |
| --- | --- |
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for local development, `False` in production |
| `DATABASE_URL` | PostgreSQL connection (optional locally, SQLite is used without it) |
| `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` | Google sign-in (OAuth 2.0/OpenID Connect) |
| `GOOGLE_MAPS_API_KEY` | Google Maps JavaScript API for the map and the report form |
| `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` | Photo upload to Cloudinary |

**Check:** Run `python manage.py test` in the `code` folder. All tests should pass. The home page opens at the address above.

## Technologies

| Technology or tool | Role in this project | Reason for use or important constraint |
| --- | --- | --- |
| Django (Python) | Backend and server-rendered pages for all three roles | One codebase keeps permissions and data in one place (ADR-01, ADR-02). |
| PostgreSQL | Stores users, issues, assignments, status history and notifications | The data is strongly connected, and a status change must be saved together with its history and notification (ADR-03). |
| django-allauth with Google | Sign-in with OAuth 2.0/OpenID Connect | The application stores no passwords (C-01). Every user needs a Google account. |
| Google Maps JavaScript API | Map of reports, location picker and address lookup | Reporting depends on it. A pin can still be placed when the address lookup fails (NF-09). |
| Cloudinary | Stores the photos of reports | Render's disk is not permanent, so only the photo URL is kept in the database (ADR-05). |
| Render with Docker | Hosts the public application and the database | Managed hosting with HTTPS and deployment from GitHub (ADR-07). |

## Team Members

Team TG01.3 – T3-Development

| Member | Main role or contribution |
| --- | --- |
| Rodrigo Yañez |  |
| Macarena Santana Mardones | Team leader |
| Mafalda Pinho |  |
| Karla Barković |  |
| Konstiantyn Tiurikov |  |
| Iva Jončić |  |

Roles may change during the project. The repository history and the task tracker provide supporting evidence of teamwork.

## Contributing

Code changes are made on separate branches and merged into `main` through pull requests. Defects found during testing are reported to the team member responsible for the feature (see Team Members).

<a id="license"></a>
## License [![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**License status:** See the [LICENSE](LICENSE) file.

Third-party code, datasets, images, icons and other assets retain their own licenses and attribution requirements.

<a id="ai-usage"></a>
## AI Usage [![AI Usage: Disclosed](https://img.shields.io/badge/AI%20Usage-Disclosed-blue.svg)](https://www.fer.unizg.hr/_download/repository/Policy%20on%20the%20appropriate%20use%20of%20artificial%20intelligence%20at%20the%20faculty%20of%20electrical%20engineering%20and%20computing%5B1%5D.pdf)

This project follows FER's [Policy on the Appropriate Use of Artificial Intelligence](https://www.fer.unizg.hr/_download/repository/Policy%20on%20the%20appropriate%20use%20of%20artificial%20intelligence%20at%20the%20faculty%20of%20electrical%20engineering%20and%20computing%5B1%5D.pdf).

**Statement:** AI tools were used during this project to support learning and development. They did not replace the team's own work. We used the following tools:

- **Google Gemini:** finding guides for setting up deployment on Render, and getting advice on how to write up project risks and which risks to include.
- **Claude (Anthropic)**
  - Learning Django: how a Django project is structured and organised on GitHub, how requests flow through the app, Django syntax, plus explanations and small examples.
  - Understanding how parts of the project fit together, such as the Users app, Map View, CSS and JavaScript.
  - Reviewing code, pointing out errors and checking pull requests before merging.
  - Organising tasks, checking parts of the documentation and correcting grammar.

Team members reviewed, tested and adapted all AI suggestions, code and text before adding them to the repository. Each member understands their own contribution and can explain it. No private data, access credentials or other people's protected material was entered into AI tools.

<a id="code-of-conduct-and-support"></a>
## Code of Conduct and Support [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

Team members are expected to follow the **STUDENT CODE OF CONDUCT** of the Faculty of Electrical Engineering and Computing, University of Zagreb, the course teamwork guidelines, and the [IEEE Code of Ethics](https://www.ieee.org/about/corporate/governance/p7-8.html). See also [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

**Course documentation template:** Documentation structure adapted from the FER Software Engineering course template by [Vlado Sruk](https://www.fer.unizg.hr/en/vlado.sruk), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The application and its content were created by the student team named above.

# Trafikverket API Hemsida med Flask

Detta projekt är en webbaserad applikation som använder Flask och Trafikverkets API för att visa trafikinformation. Projektet följer DevOps-metoden och har en komplett CI/CD-pipeline för att automatisera tester och driftsättning till en Azure-webbapp via DockerHub.

## Funktioner

- Enkel hemsida med en knapp som gör ett API-anrop till Trafikverkets API.
- Filtrering av data baserat på tid för att visa relevant information.
- CI/CD-pipeline med GitHub Actions som inkluderar tester, skapande av Docker-image och publicering till DockerHub.
- Automatisk driftsättning till Azure Web App for Containers.

## Teknologier

- **Språk och ramverk**: Python (Flask), HTML
- **Versionshantering**: Git
- **CI/CD**: GitHub Actions, Docker, DockerHub
- **Hosting**: Azure Web App for Containers

## Installation

1. **Klona repo**:
   ```bash
   git clone https://github.com/ditt-användarnamn/projekt-repo.git
   cd projekt-repo
   ```

2. **Skapa virtuell miljö och installera beroenden**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # För Mac/Linux
   venv\Scripts\activate  # För Windows
   pip install -r requirements.txt
   ```

## Projektstruktur

- `app.py`: Huvudfil för Flask-applikationen.
- `templates/index.html`: HTML-fil för enkel UX med en knapp för att göra API-anrop.
- `helpers.py`: Innehåller funktioner för API-anrop och databehandling.
- `.github/workflows`: YAML-filer för GitHub Actions CI/CD-pipelines.
- `Dockerfile`: Konfigurationsfil för Docker-image.
- `.gitignore` och `.dockerignore`: Filtrerar bort oönskade filer i repo och Docker-image.

## Tester

Projektet innehåller ett enhetstest för att verifiera att API-anropet fungerar och att databehandlingen ger förväntat resultat. Testerna körs automatiskt som en del av GitHub Actions pipeline.

- För att köra tester manuellt, använd kommandot:
   ```bash
   pytest
   ```

## CI/CD med GitHub Actions

GitHub Actions-pipelinen är konfigurerad att:

1. **Köra tester**: Validerar API-anrop och databehandling.
2. **Skapa Docker-image**: Skapar en Docker-image baserad på koden.
3. **Publicera till DockerHub**: Pusha Docker-imagen till DockerHub för driftsättning.

## Driftsättning på Azure

Azure Web App for Containers är konfigurerad att dra Docker-imagen från DockerHub och driftsätta hemsidan som kan nås via internet.

## Krav

- Python 3.x
- Flask
- Docker
- Azure-konto

## Miljövariabler

Lägg till följande variabel i en `.env`-fil:

- `API_KEY`: API-nyckeln för Trafikverkets API

## Författare

Skapad av [Daniel Sjöholm].

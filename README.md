# Chiro-database-tool
Command line tool om Chiro-leden met SQLite database.
## Purpose
A small command line application to manage Chiro Pimpernel Vleteren members and their afdeling.
## Technology
Python (from 3.11)
## Libraries
(see requirements.txt)

- environs: to read settings from .env file.
## Functions
- Show all leden.
- Search lid by id.
- Search leden by name (voornaam/achternaam).
- Add a lid.
- Update a lid.
- Remove a lid.
- Show all afdelingen.
- Show all leden within one afdeling.
- Export leden to CSV (exports/leden.csv).
## Planned functions
- Export to CSV.
- More filtering/sorting options.
## Database name
Create a file `.env` in the root folder of the project (same level as `main.py`).

Add the following line: DATABASE=data/chiro_leden.db

If the database does not exist, it will be created automatically on first run.

Note: `.env` is not included in git. Use `.env.example` as a template.

## How to execute
1. Clone the repository (or download the code).
2. Create a virtual environment:
   python -m venv .venv
3. Activate the virtual environment.
4. Install external libraries:
   pip install -r requirements.txt
5. Execute the code:
   python main.py

## Structure of the database
The database consists of two tables:

CREATE TABLE afdelingen (
id INTEGER PRIMARY KEY,
naam TEXT NOT NULL
);

CREATE TABLE leden (
id INTEGER PRIMARY KEY AUTOINCREMENT,
voornaam TEXT NOT NULL,
achternaam TEXT NOT NULL,
afdeling_id INTEGER NOT NULL
);

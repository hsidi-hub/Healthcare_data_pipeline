# Healthcare_data_pipeline


## 1. Create the GitHub repository

Create a new repository named:  healthcare-data-pipeline

Recommended settings:

Visibility: Public if this is a portfolio project
Add a README
Add a Python .gitignore
Do not add a license unless you have selected one intentionally

From the repository page:
Code → Codespaces → Create codespace on main

## 2. Create the Codespaces project structure

In the Codespaces terminal, run:

mkdir -p .devcontainer
mkdir -p data/raw
mkdir -p src
mkdir -p sql
mkdir -p tests
mkdir -p healthcare_dbt/models/sources
mkdir -p healthcare_dbt/models/staging
mkdir -p healthcare_dbt/models/intermediate
mkdir -p healthcare_dbt/models/marts
mkdir -p healthcare_dbt/tests
mkdir -p dashboard
mkdir -p docs

touch src/__init__.py
touch src/config.py
touch src/extract.py
touch src/validate.py
touch src/load_to_snowflake.py
touch sql/create_snowflake_objects.sql
touch tests/test_validate.py
touch main.py
touch profile_source.py
touch requirements.txt
touch .env.example
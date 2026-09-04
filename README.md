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
#-----------------------------------------------------------
run: pwd, python --version and then git status

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
## 3- gete the data 
use this in the terminal to avoide dowloading the data locally 
wget -O data/raw/synthea_csv.zip \
  https://synthetichealth.github.io/synthea-sample-data/downloads/latest/synthea_sample_data_csv_latest.zip

then run this to unzip the file :
unzip -l data/raw/synthea_csv.zip
and this unzip data/raw/synthea_csv.zip -d data/raw ( -d meand destination directory)
- verify the extracted files run :
find data/raw -type f | sort

What this command means
- find searches a directory.
- data/raw is where the search starts.
- -type f displays files only, not folders.
- | sends the output of find to the next command.
- sort displays the filenames alphabetically.

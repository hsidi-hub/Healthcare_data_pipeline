from pathlib import Path 
import pandas as pd 

# storing the file source
PATIENT_FILE = Path("data/raw/patients.csv")

# read the file 
patients_df = pd.read_csv(PATIENT_FILE)

# printing df head
print(patients_df.head())

# df rows and columns
print('The data set was loaded successefully:')
print(f"The number of rows : {patients_df.shape[0]}")
print(f"The number of columns: {patients_df.shape[1]}")
print("\ncolumns names :")

# columns names
for column in patients_df.columns:
    print(column)

# data types
print('\n data types:', patients_df.dtypes)

# missing values
print('\nchecking missing values: ')
print('=====================================================')
missing_values = patients_df.isna().sum()
print(missing_values[missing_values>0])

# checking the patients IDs quality
print('\n patients IDs data quality')
print('=====================================================')
print(f'Missing patients IDs :{patients_df.Id.isna().sum()}')

# checking duplicates
print(f'Duplicated patients IDs :{patients_df.Id.duplicated().sum()}')

# Unique patients
print(f'Unique patients IDs :{patients_df.Id.nunique()}')

# birth day validation
#----------------------------------------------------------------------
birthdates = pd.to_datetime(patients_df.BIRTHDATE, errors = 'coerce')
print('\n birthdate validatin: ')
print('=============================================================')
print(f"Invalid or missing birthdate: {birthdates.isna().sum()}")
print(f'Earliest birthdate: {birthdates.min()}')
print(f'Latest birthdate: {birthdates.max()}')
print('=============================================================')
# Future birthdays
#------------------------------------------------------------------------
today = pd.Timestamp.today().normalize()
future_birthdates = birthdates > today
print(f"Future birthdates: {future_birthdates.sum()}")
print('========================================================')
# Death dates 
deathdates = pd.to_datetime(
patients_df["DEATHDATE"],
errors="coerce"
)

deathdate_provided = patients_df["DEATHDATE"].notna()
invalid_deathdates = deathdate_provided & deathdates.isna()
death_before_birth = deathdates < birthdates
future_deathdates = deathdates > today
print("\nDeath date quality checks:")
print(f"Patients with a death date: {deathdate_provided.sum()}")
print(f"Invalid death dates: {invalid_deathdates.sum()}")
print(f"Death dates before birth: {death_before_birth.sum()}")
print(f"Future death dates: {future_deathdates.sum()}")
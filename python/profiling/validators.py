import pandas as pd


def validate_required_column(df,column_name):
        if column_name not in df.columns:
            print('Missing required column:',column_name)
            return False
        return True

def validate_patient_required_columns(df):
    required_columns= ['Id','BIRTHDATE','DEATHDATE']
    validation_result=[]
    for column_name in required_columns:
        result= validate_required_column(df,column_name)
        validation_result.append(result)
    return all(validation_result)

def validate_patient_id_not_null(df):
     missing_id_count= df["Id"].isna().sum() # returns np boolean
     print(f"\nMissing patient IDs:{missing_id_count}")
     return bool(missing_id_count ==0) # because return missing_id_count ==0 returns np.True_

def validate_patient_id_unique(df):
    duplicated_id_count = df['Id'].duplicated().sum()
    print(f"\nDuplicated patient IDs:{duplicated_id_count}")
    return bool(duplicated_id_count==0)


def validate_patient_birthdate_convertible(df):
    converted_birthdates  = pd.to_datetime(df.BIRTHDATE, errors = 'coerce')
    invalid_birthdate_count = converted_birthdates.isna().sum()

    print(
    f"\nInvalid or missing birthdates: "
    f"{invalid_birthdate_count}"
   )
    return bool( invalid_birthdate_count==0)

def validate_patient_birthdate_not_future(df, reference_date):
    converted_reference_date = pd.to_datetime(reference_date)
    converted_birthdates   = pd.to_datetime(df.BIRTHDATE, errors = 'coerce')
    future_birthdate_count = (converted_birthdates > converted_reference_date).sum()
    print(f"Future birthdates: {future_birthdate_count}")
    return bool(future_birthdate_count==0)

def validate_patient_deathdate_convertible(df):
    deathdate_provided   = df["DEATHDATE"].notna()
    converted_deathdates = pd.to_datetime(
         df["DEATHDATE"], 
         errors = 'coerce',
         )
    invalid_death_dates =(
         deathdate_provided 
         & converted_deathdates.isna()
         
    )
    invalid_deathdate_count = invalid_death_dates.sum()
    print(
         f"\nInvalid supplied death dates: "
         f"{invalid_deathdate_count}"
         )
    return bool(invalid_deathdate_count==0)
#--------------------------------------------------------------------------------------------
def validate_patient_deathdate_not_before_birthdate(df):
    converted_deathdates = pd.to_datetime(
         df["DEATHDATE"], 
         errors = 'coerce',
         )
    
    converted_birthdates   = pd.to_datetime(
         df.BIRTHDATE,
         errors = 'coerce'
         )
    death_before_birth_count = (converted_deathdates < converted_birthdates).sum()
    print(f"\nDeath dates before birthdates: {death_before_birth_count}")
    return bool(death_before_birth_count==0)
#---------------------------------------------------------------------------------------------------

def validate_patient_deathdate_not_future(df, reference_date):
    
    converted_reference_date = pd.to_datetime(reference_date)
    converted_deathdates      = pd.to_datetime(
        df["DEATHDATE"], 
        errors = "coerce"
    )
    future_deathdate_count = (
        converted_deathdates > converted_reference_date
    ).sum()
    print(f"\nFuture deathdates: {future_deathdate_count}")
    return bool(future_deathdate_count==0)
#-------------------------------------------------------------------------------------------------------
def validate_patients(df, reference_date):
    required_columns_valid = validate_patient_required_columns(df)

    if not required_columns_valid:
        return False

    patient_id_not_null_valid = validate_patient_id_not_null(df)

    if not patient_id_not_null_valid:
        return False

    patient_id_unique_valid = validate_patient_id_unique(df)

    if not patient_id_unique_valid:
        return False

    birthdate_convertible_valid = (
        validate_patient_birthdate_convertible(df)
    )

    if not birthdate_convertible_valid:
        return False

    birthdate_not_future_valid = (
        validate_patient_birthdate_not_future(
            df,
            reference_date,
        )
    )

    if not birthdate_not_future_valid:
        return False

    deathdate_convertible_valid = (
        validate_patient_deathdate_convertible(df)
    )

    if not deathdate_convertible_valid:
        return False

    deathdate_not_before_birthdate_valid = (
        validate_patient_deathdate_not_before_birthdate(df)
    )

    if not deathdate_not_before_birthdate_valid:
        return False

    deathdate_not_future_valid = (
        validate_patient_deathdate_not_future(
            df,
            reference_date,
        )
    )

    if not deathdate_not_future_valid:
        return False

    return True
#------------------------------------------------------------------------------------
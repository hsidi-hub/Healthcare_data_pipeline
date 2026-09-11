import pandas as pd
from python.profiling.validators import(
validate_required_column,
validate_patient_required_columns,
validate_patient_id_not_null,
validate_patient_id_unique,
validate_patient_birthdate_convertible,
validate_patient_birthdate_not_future,
validate_patient_deathdate_convertible,
validate_patient_deathdate_convertible,
validate_patient_deathdate_not_before_birthdate,
validate_patient_deathdate_not_future,
validate_patients,
    
)

def test_required_column_returns_true_when_column_exists():
    test_df = pd.DataFrame(
    {
        "Id": ["A1", "A2"]
    }
)   
    result = validate_required_column(test_df,"Id")
    assert result is True


def test_required_column_returns_false_when_column_is_missing():
   test_df = pd.DataFrame(
       {
           "Id": ["A1", "A2"]
       }
   )   
   result = validate_required_column(test_df,"BIRTHDATE")
   assert result is False

def test_patient_required_columns_returns_tru_when_all_exist():
    test_df = pd.DataFrame(
           {
               "Id": ['3'],
               "BIRTHDATE":[5],
               "DEATHDATE":[7]
           }
       )   
    result=validate_patient_required_columns(test_df)
    assert result is True

def test_patient_required_columns_returns_false_when_one_is_missing():
    test_df = pd.DataFrame(
               {
                   "Id": ['3'],
                   "BIRTHDATE":["2000-01-01"],
                   
               }
           )   
    result=validate_patient_required_columns(test_df)
    assert result is False

#=======================================================================================
def test_patient_id_not_null_returns_true_when_all_ids_exist():
     test_df = pd.DataFrame(
                   {
                       "Id": ["3","2"]
                       
                       
                   }
               )   

     result = validate_patient_id_not_null(test_df)
     assert result is True
#===============================================================================================

def test_patient_id_not_null_returns_false_when_an_id_is_missing():
   
     test_df = pd.DataFrame(
                   {
                       "Id": ["A1", None, "A3"]
                       
                       
                   }
               )   

     result = validate_patient_id_not_null(test_df)
     assert result is False
#=================================================================================================
def test_patient_id_unique_returns_true_when_all_ids_are_unique():
    test_df = pd.DataFrame(
                       {
                           "Id": ["A1", "A3"]
                           
                           
                       }
                   )   
    
    result = validate_patient_id_unique(test_df)
    assert result is True
#==================================================================================================
def test_patient_id_unique_returns_False_when_id_is_duplicated():
    test_df = pd.DataFrame(
                       {
                           "Id": ["A1", "A1","A3"]
                           
                           
                       }
                   )   
    
    result = validate_patient_id_unique(test_df)
    assert result is False
#====================================================================================================

def test_birthdate_convertible_returns_true_for_valid_dates():
     test_df = pd.DataFrame(
                           {
                               "BIRTHDATE": ["2000-05-10", "1985-12-20"]
                               
                               
                           }
                       )   
        
     result = validate_patient_birthdate_convertible(test_df)
     assert result is True
#=====================================================================================================
def test_birthdate_convertible_returns_False_for_invalid_dates():
     test_df = pd.DataFrame(
                           {
                               "BIRTHDATE": ["2000-05-10", "not-a-date"]
                               
                               
                           }
                       )   
        
     result = validate_patient_birthdate_convertible(test_df)
     assert result is False
#======================================================================================================
def test_birthdate_not_future_returns_true_for_past_dates():
     test_df = pd.DataFrame(
                               {
                                   "BIRTHDATE":["2000-05-10", "2020-01-01"]
                                   
                                   
                               }
                           )
     reference_date = "2026-01-01"   
     result = validate_patient_birthdate_not_future(test_df,  reference_date )
     assert result is True
#=======================================================================================================
def test_birthdate_not_future_returns_false_for_future_date():
    test_df = pd.DataFrame(
                                   {
                                       "BIRTHDATE":["2000-05-10", "2026-02-01"]
                                       
                                       
                                   }
                               )
    
    reference_date = "2026-01-01"   
    result = validate_patient_birthdate_not_future(test_df,  reference_date )
    assert result is False
#=========================================================================================================

def test_deathdate_convertible_allows_missing_values():
     test_df = pd.DataFrame(
         {
             "BIRTHDATE":["2000-05-10", "2026-02-01"],
             "DEATHDATE":["2020-05-10", None]
         }
    )

     result= validate_patient_deathdate_convertible(test_df)
     assert result is True
#===========================================================================================================
def test_deathdate_convertible_rejects_invalid_supplied_value():
    test_df = pd.DataFrame(
        {
            "BIRTHDATE":["2000-05-10", "2026-02-01"],
            "DEATHDATE":["2020-05-10", 'not-a-date']
        }
    )
    
    result= validate_patient_deathdate_convertible(test_df)
    assert result is False
#============================================================================================================
def test_deathdate_not_before_birthdate_returns_false_when_death_is_earlier():
    test_df = pd.DataFrame(
            {
                "BIRTHDATE":[
                    "2000-05-10", 
                    "2026-02-01"
                    ],
                "DEATHDATE":[
                    "2020-05-10", 
                    "2026-01-01"
                    ]
            }
        )

    result= validate_patient_deathdate_not_before_birthdate(test_df)
    assert result is False
#==========================================================================================================

def test_deathdate_not_future_returns_true_for_valid_or_missing_dates():
     reference_date = "2026-01-01"
     test_df = pd.DataFrame(
         {
             "DEATHDATE": ["2020-05-10", None]
         }
     )
     result= validate_patient_deathdate_not_future(test_df, reference_date)
     assert result is True
#=============================================================================================================

def test_deathdate_not_future_returns_false_for_future_date():
     reference_date = "2026-01-01"
     test_df = pd.DataFrame(
         {
           "DEATHDATE": ["2020-05-10", "2027-01-01"],

         }
     )
     result= validate_patient_deathdate_not_future(test_df, reference_date)
     assert result is False
#============================================================================================================
def test_validate_patients_returns_true_when_all_rules_pass():
    reference_date = "2026-01-01"

    test_df = pd.DataFrame(
        {
            "Id": [
                "A1",
                "A2",
            ],
            "BIRTHDATE": [
                "1980-05-10",
                "2000-02-15",
            ],
            "DEATHDATE": [
                "2020-06-01",
                None,
            ],
        }
    )

    result = validate_patients(
        test_df,
        reference_date,
    )

    assert result is True
#========================================================================================================
def test_validate_patients_returns_false_when_required_column_is_missing():
    reference_date = "2026-01-01"

    test_df = pd.DataFrame(
        {
            "Id": ["A1"],
            "BIRTHDATE": ["2000-05-10"],
        }
    )

    result = validate_patients(
        test_df,
        reference_date,
    )

    assert result is False

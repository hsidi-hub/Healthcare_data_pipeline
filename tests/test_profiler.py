import pandas as pd 
from python.profiling.profiler import profile_dataframe

# pytest automatically discovers functions whose names begin with test_
def test_profile_returns_correct_row_counts():
    test_df = pd.DataFrame(
    {
        "Id": ["A1", "A2", "A3"]
    }
    )
    result = profile_dataframe(test_df,"test_dataset")
    assert result["row_count"]==3


def test_profile_returns_correct_columns_counts():
    test_df = pd.DataFrame(
        {
            "Id": ["A1", "A2", "A3"],
            "NAMES":['DEL','ROB','DOG']
        }
        )
    result = profile_dataframe(test_df,"test_dataset")
    assert result["column_count"]==2

def test_profile_return_correct_dataset_name():
    test_df = pd.DataFrame(
        {
            "Id": ["A1", "A2", "A3"]
        }
        )
    result= profile_dataframe(test_df,"test_dataset")
    assert result['dataset_name']== "test_dataset"


def test_profile_returns_requested_distinct_count():
    test_df = pd.DataFrame(
        {
            "Id": [
                "A1",
                "A2",
                "A2",
            ]
        }
    )

    result = profile_dataframe(
        test_df,
        "Test dataset",
        distinct_count_columns=["Id"],
    )

    assert result["distinct_counts"]["Id"] == 2
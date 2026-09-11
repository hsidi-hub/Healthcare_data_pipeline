from pathlib import Path

import pandas as pd

from profiling.profiler import profile_dataframe
from profiling.validators import validate_patients


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PATIENT_FILE = PROJECT_ROOT / "data" / "raw" / "patients.csv"


patients_df = pd.read_csv(PATIENT_FILE)

profile_dataframe(
    patients_df,
    "Patients",
    distinct_count_columns=["Id"],
)

reference_date = pd.Timestamp.today().normalize()

patient_validation_result = validate_patients(
    patients_df,
    reference_date,
)

print(
    f"\nOverall patient validation passed: "
    f"{patient_validation_result}"
)
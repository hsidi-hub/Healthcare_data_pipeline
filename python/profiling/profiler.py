def profile_dataframe(
    df,
    dataset_name,
    distinct_count_columns=None,
):
    print(f"Dataset: {dataset_name}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("Column names:")
    for column in df.columns:
        print(column)

    print("Data types:")
    print(df.dtypes)

    missing_values = df.isna().sum()

    print("\nColumns with missing values:")
    print(missing_values[missing_values > 0])

    exact_duplicate_rows = df.duplicated().sum()
    print(f"Exact duplicate rows: {exact_duplicate_rows}")

    empty_columns_check = df.isna().all()

    completely_empty_columns = (
        empty_columns_check[empty_columns_check]
        .index
        .to_list()
    )

    print(
        f"Completely empty columns: "
        f"{completely_empty_columns}"
    )
    distinct_counts = {}
    if distinct_count_columns is not None:
        print("Distinct value counts:")

        for column_name in distinct_count_columns:
            distinct_count = df[column_name].nunique()
            distinct_counts[column_name] = int(distinct_count)
            print(
                f"{column_name}: "
                f"{distinct_count}"
            )

    return {
        "dataset_name": dataset_name,
        "row_count": df.shape[0],
        "column_count": df.shape[1],
        "distinct_counts": distinct_counts,
    }
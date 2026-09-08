import pandas as pd


def clean_dataset(df: pd.DataFrame):

    # Before Cleaning

    rows_before = len(df)
    duplicates_before = df.duplicated().sum()
    missing_before = df.isna().sum().sum()

    invalid_order_dates = 0
    invalid_ship_dates = 0
    invalid_postal_codes = 0
    invalid_sales = 0
    invalid_quantity = 0
    invalid_discount = 0
    invalid_profit = 0
    sales_outliers = 0

  
    # Remove Duplicate Rows
    

    df = df.drop_duplicates()

    # Remove Empty Order IDs


    df = df.dropna(subset=["Order ID"])


    # Convert Dates

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce",
    )

    invalid_order_dates = df["Order Date"].isna().sum()

    df = df.dropna(subset=["Order Date"])


    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        errors="coerce",
    )

    invalid_ship_dates = df["Ship Date"].isna().sum()

    df = df.dropna(subset=["Ship Date"])


    # Postal Code Validation


    df["Postal Code"] = pd.to_numeric(
        df["Postal Code"],
        errors="coerce",
    )

    invalid_postal_codes = df["Postal Code"].isna().sum()

    df = df.dropna(subset=["Postal Code"])

    df["Postal Code"] = df["Postal Code"].astype(int)


    # Numeric Column Validation


    numeric_columns = [
        "Sales",
        "Quantity",
        "Discount",
        "Profit",
    ]

    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        )

    invalid_sales = df["Sales"].isna().sum()
    invalid_quantity = df["Quantity"].isna().sum()
    invalid_discount = df["Discount"].isna().sum()
    invalid_profit = df["Profit"].isna().sum()

    df = df.dropna(subset=numeric_columns)


    # Remove Invalid Values


    df = df[df["Sales"] >= 0]

    df = df[df["Quantity"] > 0]

    df = df[
        (df["Discount"] >= 0)
        &
        (df["Discount"] <= 1)
    ]

    # Fill Missing Text Values

    text_columns = df.select_dtypes(include="object").columns

    df[text_columns] = df[text_columns].fillna("Unknown")

    # Detect Outliers (Do NOT Remove)


    sales_outliers = (df["Sales"] > 100000).sum()

   
    # After Cleaning
  

    rows_after = len(df)

    duplicates_after = df.duplicated().sum()

    missing_after = df.isna().sum().sum()

    report = {

        "rows_before": rows_before,

        "rows_after": rows_after,

        "duplicates_removed":
            duplicates_before - duplicates_after,

        "missing_fixed":
            missing_before - missing_after,

        "remaining_missing":
            missing_after,

        "remaining_duplicates":
            duplicates_after,

        "invalid_order_dates":
            invalid_order_dates,

        "invalid_ship_dates":
            invalid_ship_dates,

        "invalid_postal_codes":
            invalid_postal_codes,

        "invalid_sales":
            invalid_sales,

        "invalid_quantity":
            invalid_quantity,

        "invalid_discount":
            invalid_discount,

        "invalid_profit":
            invalid_profit,

        "sales_outliers":
            sales_outliers,

    }

    return df, report
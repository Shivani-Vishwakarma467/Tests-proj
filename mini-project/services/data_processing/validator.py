import pandas as pd

REQUIRED_COLUMNS = [
    "Order ID",
    "Order Date",
    "Ship Date",
    "Category",
    "Sub-Category",
    "Region",
    "State",
    "City",
    "Customer Name",
    "Segment",
    "Sales",
    "Profit",
    "Quantity",
    "Discount",
]


def validate_dataset(df: pd.DataFrame):

    missing_columns = []

    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            missing_columns.append(column)

    return missing_columns











































































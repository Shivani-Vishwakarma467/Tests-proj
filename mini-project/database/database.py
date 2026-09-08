import sqlite3

import pandas as pd

from config.config import DATABASE_PATH


def get_connection():

    return sqlite3.connect(DATABASE_PATH)


def save_dataframe(df: pd.DataFrame):

    conn = get_connection()

    df.to_sql(
        "retail_sales",
        conn,
        if_exists="replace",
        index=False,
    )

    conn.commit()

    conn.close()


def load_dataframe():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM retail_sales",
        conn,
    )

    conn.close()

    return df
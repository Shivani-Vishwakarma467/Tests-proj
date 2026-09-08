import pandas as pd


def top_products(df):

    return (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )


def top_customers(df):

    return (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )


def top_cities(df):

    return (
        df.groupby("City")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
        )
        .sort_values("Sales", ascending=False)
        .head(10)
        .reset_index()
    )


def top_states(df):

    return (
        df.groupby("State")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
        )
        .sort_values("Sales", ascending=False)
        .head(10)
        .reset_index()
    )


def profitable_products(df):

    return (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )


def loss_products(df):

    return (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values()
        .head(10)
        .reset_index()
    )
import pandas as pd


def business_insights(df: pd.DataFrame):

    insights = []

    # Highest Sales Category
    top_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"🏆 Highest Sales Category: **{top_category}**"
    )

    # Highest Profit Region
    top_region = (
        df.groupby("Region")["Profit"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"🌍 Most Profitable Region: **{top_region}**"
    )

    # Best Product
    product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"📦 Best Selling Product: **{product}**"
    )

    # Best Customer
    customer = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"👤 Highest Value Customer: **{customer}**"
    )

    # Average Discount
    insights.append(
        f"🏷 Average Discount: **{round(df['Discount'].mean()*100,2)}%**"
    )

    # Total Profit
    insights.append(
        f"💰 Total Profit: **${df['Profit'].sum():,.0f}**"
    )

    return insights
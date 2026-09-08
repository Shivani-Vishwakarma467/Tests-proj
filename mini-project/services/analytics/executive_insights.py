import pandas as pd



# Business Health Score


def business_health_score(df):

    score = 100

    # Profit Margin
    profit_margin = (df["Profit"].sum() / df["Sales"].sum()) * 100

    if profit_margin < 5:
        score -= 20
    elif profit_margin < 10:
        score -= 10

    # Average Discount
    avg_discount = df["Discount"].mean() * 100

    if avg_discount > 20:
        score -= 20
    elif avg_discount > 10:
        score -= 10

    # Loss Making Products
    loss_products = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .lt(0)
        .sum()
    )

    if loss_products > 20:
        score -= 15
    elif loss_products > 10:
        score -= 8

    score = max(score, 0)

    if score >= 90:
        status = "🟢 Excellent"

    elif score >= 75:
        status = "🟡 Good"

    elif score >= 60:
        status = "🟠 Average"

    else:
        status = "🔴 Poor"

    return score, status



# Executive Business Story


def business_story(df):

    sales = df["Sales"].sum()
    profit = df["Profit"].sum()
    orders = df["Order ID"].nunique()

    top_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    return f"""
The company generated **${sales:,.0f}** in revenue from **{orders:,} orders**.

The highest-performing category was **{top_category}**, contributing the largest share of sales.

Overall profit reached **${profit:,.0f}**, reflecting a healthy business performance.

The business should continue investing in high-performing categories while optimizing pricing and discount strategies to improve profitability.
"""



# Executive Recommendations


def management_recommendations(df):

    recommendations = []

  
    # Highest Sales Category
    

    best_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    recommendations.append(
        {
            "priority": "High",
            "title": "Increase Inventory",
            "recommendation": f"Increase inventory allocation for the **{best_category}** category.",
            "impact": "This category contributes the highest overall sales and offers the greatest revenue potential."
        }
    )


    # Lowest Profit Region

    worst_region = (
        df.groupby("Region")["Profit"]
        .sum()
        .idxmin()
    )

    recommendations.append(
        {
            "priority": "Medium",
            "title": "Improve Regional Performance",
            "recommendation": f"Review pricing and promotional strategies in the **{worst_region}** region.",
            "impact": "This region currently delivers the lowest profitability and presents the biggest improvement opportunity."
        }
    )

    # Discount Optimization
    

    avg_discount = df["Discount"].mean() * 100

    if avg_discount > 15:

        recommendations.append(
            {
                "priority": "Medium",
                "title": "Optimize Discount Strategy",
                "recommendation": "Reduce discount levels on low-margin products.",
                "impact": "Lower discount levels can improve overall profit margins without significantly affecting sales."
            }
        )

    return recommendations
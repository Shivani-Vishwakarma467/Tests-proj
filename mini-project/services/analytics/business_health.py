import pandas as pd


def business_health_score(df: pd.DataFrame):

    score = 100
    insights = []

    
    # Profit Margin
    

    profit_margin = (
        df["Profit"].sum() /
        max(df["Sales"].sum(), 1)
    ) * 100

    if profit_margin < 5:
        score -= 20
        insights.append("❌ Low Profit Margin")

    elif profit_margin < 10:
        score -= 10
        insights.append("🟡 Moderate Profit Margin")

    else:
        insights.append("✅ Profit Margin Healthy")

    
    # Average Discount
    

    avg_discount = df["Discount"].mean() * 100

    if avg_discount > 20:
        score -= 20
        insights.append("❌ High Discount")

    elif avg_discount > 10:
        score -= 10
        insights.append("🟡 Moderate Discount")

    else:
        insights.append("✅ Low Discount")

    
    # Loss Making Products

    loss_products = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .lt(0)
        .sum()
    )

    if loss_products > 20:
        score -= 15
        insights.append("❌ Too Many Loss Making Products")

    elif loss_products > 10:
        score -= 8
        insights.append("🟡 Moderate Loss Products")

    else:
        insights.append("✅ Low Loss Products")

    score = max(score, 0)

   
    # Status


    if score >= 90:
        status = "🟢 Excellent"

    elif score >= 75:
        status = "🟡 Good"

    elif score >= 60:
        status = "🟠 Average"

    else:
        status = "🔴 Poor"

    return {
        "score": score,
        "status": status,
        "insights": insights,
    }
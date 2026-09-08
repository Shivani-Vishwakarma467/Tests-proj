import streamlit as st
from database.database import load_dataframe
from logs.logger import logger

from services.analytics.executive_insights import (
    business_health_score,
    business_story,
    management_recommendations,
)


def show_reports():

    df = load_dataframe()

    logger.info("Executive Reports page opened.")


    # Page Header
    

    st.title("📈 Executive Reports")
    st.caption("Business performance summary for management.")

    st.divider()

   
    # Business Health Score
    

    score, status = business_health_score(df)

    logger.info(
    f"Business Health Score Generated | Score: {score} | Status: {status}"
)

    st.subheader("🏥 Business Health Score")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.metric("Score", f"{score}/100")

    with col2:
        st.success(status)

    st.divider()


    # Executive KPIs
    

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "💰 Total Sales",
        f"${df['Sales'].sum():,.0f}"
    )

    c2.metric(
        "📈 Total Profit",
        f"${df['Profit'].sum():,.0f}"
    )

    c3.metric(
        "📦 Orders",
        df["Order ID"].nunique()
    )

    c4.metric(
        "👥 Customers",
        df["Customer ID"].nunique()
    )

    st.divider()


    # Executive Recommendations
  

    st.subheader("🎯 Executive Recommendations")

    recommendations = management_recommendations(df)

    logger.info(
    f"Generated {len(recommendations)} Executive Recommendations"
)

    for rec in recommendations:

        message = f"""
### {rec['title']}

**Recommendation**

{rec['recommendation']}

**Business Impact**

{rec['impact']}
"""

        if rec["priority"] == "High":
            st.error(message)
        else:
            st.warning(message)

    st.divider()

    # Category Performance

    st.subheader("📦 Category Performance")

    category = (
        df.groupby("Category")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique"),
        )
        .reset_index()
    )

    st.dataframe(
        category,
        use_container_width=True,
        hide_index=True,
    )

    logger.info("Category Performance Report Generated")

    st.divider()


    # Region Performance
  

    st.subheader("🌍 Region Performance")

    region = (
        df.groupby("Region")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique"),
        )
        .reset_index()
    )

    st.dataframe(
        region,
        use_container_width=True,
        hide_index=True,
    )

    logger.info("Region Performance Report Generated")

    st.divider()

   
    # Segment Performance
    

    st.subheader("👥 Segment Performance")

    segment = (
        df.groupby("Segment")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique"),
        )
        .reset_index()
    )

    st.dataframe(
        segment,
        use_container_width=True,
        hide_index=True,
    )

    logger.info("Segment Performance Report Generated")

    st.divider()

    
    # Top Products & Top Customers
   

    left, right = st.columns(2)

    with left:

        st.subheader("🏆 Top Products")

        top_products = (
            df.groupby("Product Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        st.dataframe(
            top_products,
            use_container_width=True,
            hide_index=True,
        )

    with right:

        st.subheader("👤 Top Customers")

        top_customers = (
            df.groupby("Customer Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        st.dataframe(
            top_customers,
            use_container_width=True,
            hide_index=True,
        )

        logger.info("Top 10 Products Report Generated")

    st.divider()

  
    # Executive Business Story


    st.subheader("📖 Executive Business Story")

    st.info(
        business_story(df)
    )

    logger.info("Executive Business Story Generated")

    st.divider()

    # Download Report
 

    csv = df.to_csv(index=False).encode("utf-8")

    download = st.download_button(
        "⬇ Download Executive Report",
        csv,
        "Retail_Executive_Report.csv",
        "text/csv",
        use_container_width=True,
    )

    if download:
        logger.info("Executive Report Download")
import streamlit as st
import pandas as pd

from components.header import show_header
from database.database import load_dataframe
from logs.logger import logger

from services.analytics.filters import apply_filters
from services.analytics.insights import business_insights
from components.kpi_card import kpi_card
from services.analytics.kpi import (
    calculate_kpis,
    format_money,
)

from services.analytics.charts import (
    monthly_sales_chart,
    category_sales_chart,
    region_sales_chart,
    segment_chart,
    profit_trend_chart,
    top10_products,
    top10_customers,
)

from services.analytics.analytics_reports import (
    top_products,
    top_customers,
    top_cities,
    top_states,
    profitable_products,
    loss_products,
)
from services.analytics.business_health import business_health_score


def show_dashboard():
    logger.info("Dashboard Opened")

    show_header()

   
    # Load Dataset

    if "df" in st.session_state:
        df = st.session_state["df"]
    else:
        df = load_dataframe()
        logger.info(f"Dataset Loaded | Rows: {len(df)}")

    st.success(
        f"✅ Dataset Loaded Successfully • {len(df):,} Records"
    )

   
    # Apply Filters

    df = apply_filters(df)

    st.caption(f"Showing {len(df):,} records")

    if df.empty:
        st.warning("⚠ No records found for the selected filters.")
        st.stop()

    
    # Status Cards

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"Dataset Loaded : {len(df):,} records")

    with col2:
        st.success("Retail Analytics Dashboard Ready")

    st.divider()

    st.header("📊 Business Overview")

# KPIs


    kpi = calculate_kpis(df)

    row1 = st.columns(4)

    with row1[0]:
        kpi_card(
           "💰 Total Sales",
           format_money(kpi["total_sales"]),
           kpi["sales_delta"],
        )

    with row1[1]:
        kpi_card(
           "📈 Total Profit",
           format_money(kpi["total_profit"]),
           kpi["profit_delta"],
        )

 

    with row1[2]:
        kpi_card(
           "📦 Orders",
           f"{kpi['total_orders']:,}",
           kpi["orders_delta"],
        )

    with row1[3]:
        kpi_card(
           "👥 Customers",
           f"{kpi['customers']:,}",
           kpi["customers_delta"],
        )


    row2 = st.columns(3)

    with row2[0]:
        kpi_card(
           "🛒 Products",
           f"{kpi['products']:,}",
           kpi["products_delta"],
        )

    with row2[1]:
        kpi_card(
           "📦 Quantity",
           f"{kpi['quantity']:,}",
           kpi["quantity_delta"],
        )

    with row2[2]:
        kpi_card(
           "🏷 Average Discount",
           f"{kpi['avg_discount']}%",
           kpi["discount_delta"],
        )

    st.divider()

    st.header("🏥 Business Health Score")

    health = business_health_score(df)

    col1, col2 = st.columns([1, 2])

    with col1:

        st.metric(
            "Health Score",
            f"{health['score']}/100"
        )

        st.progress(
            health["score"] / 100
        )

        st.markdown(
            f"### {health['status']}"
        )

        with col2:

            for item in health["insights"]:
                st.success(item)

    st.divider()

    st.subheader("💡 Business Insights")

    for insight in business_insights(df):

        st.info(insight)

    st.divider()

   
    # Charts
   

    st.header("📈 Sales Analytics")

    left, right = st.columns(2)

    with left:
        period = st.segmented_control(
            "View",
            ["Daily","Weekly","Monthly"],
            default="Monthly",
        )

        st.plotly_chart(
            monthly_sales_chart(df, period), 
            use_container_width=True,
        )


    with right:
        st.plotly_chart(
            category_sales_chart(df),
            use_container_width=True,
        )

    st.divider()

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            region_sales_chart(df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            segment_chart(df),
            use_container_width=True,
        )

    st.divider()

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            profit_trend_chart(df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            top10_products(df),
            use_container_width=True,
        )

    st.divider()

    st.plotly_chart(
        top10_customers(df),
        use_container_width=True,
    )

    st.divider()

    
    # Reports
   

    st.header("📋 Detailed Business Reports")

    filtered_df = df.copy()  

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏆 Top Products")
        st.dataframe(
            top_products(filtered_df),
            use_container_width=True,
            hide_index=True,
        )

    with col2:
        st.subheader("👤 Top Customers")
        st.dataframe(
            top_customers(filtered_df),
            use_container_width=True,
            hide_index=True,
        )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌍 Top Cities")
        st.dataframe(
            top_cities(filtered_df),
            use_container_width=True,
            hide_index=True,
        )

    with col2:
        st.subheader("🗺 Top States")
        st.dataframe(
            top_states(filtered_df),
            use_container_width=True,
            hide_index=True,
        )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💰 Most Profitable Products")
        st.dataframe(
            profitable_products(filtered_df),
            use_container_width=True,
            hide_index=True,
        )

    with col2:
        st.subheader("📉 Loss Making Products")
        st.dataframe(
            loss_products(filtered_df),
            use_container_width=True,
            hide_index=True,
        )

    st.divider()

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    download = st.download_button(
        "⬇ Export Filtered Dataset",
        csv,
        "Filtered_Data.csv",
        "text/csv",
    )

    if download:
        logger.info("Filtered Dataset Exported")
    
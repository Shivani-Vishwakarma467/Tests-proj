import streamlit as st


def show_home():

    st.title("📊 Retail KPI Dashboard")

    st.caption(
        "Enterprise Business Intelligence Platform for Retail Analytics"
    )

    st.divider()

    st.markdown(
        """
## 👋 Welcome

Retail KPI Dashboard is an end-to-end analytics platform designed to help
businesses transform raw retail sales data into actionable insights.

The application automatically validates, cleans and stores the uploaded
dataset before generating interactive dashboards and executive reports.
"""
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✨ Key Features")

        st.success("📂 Upload CSV / Excel Dataset")

        st.success("🧹 Automatic Data Cleaning")

        st.success("🗄 SQLite Data Storage")

        st.success("📈 Interactive KPI Dashboard")

        st.success("📊 Executive Reports")

        st.success("📥 Export Reports")

    with col2:

        st.subheader("🚀 Workflow")

        st.info("1️⃣ Upload Dataset")

        st.info("2️⃣ Validate Data")

        st.info("3️⃣ Clean Dataset")

        st.info("4️⃣ Store in Database")

        st.info("5️⃣ Explore Dashboard")

        st.info("6️⃣ Generate Reports")

    st.divider()

    st.subheader("📌 Modules")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("📂 Upload", "ETL Pipeline")

    with c2:
        st.metric("📈 Dashboard", "Live KPIs")

    with c3:
        st.metric("📊 Reports", "Business Insights")

    st.divider()

    st.info(
        "👈 Use the navigation menu on the left to start exploring the application."
    )
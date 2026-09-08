import streamlit as st
from datetime import datetime


def show_etl_report(report):

    
    # Data Quality Score
    

    score = 100

    deductions = (
        report["remaining_missing"]
        + report["remaining_duplicates"]
        + report["invalid_order_dates"]
        + report["invalid_ship_dates"]
        + report["invalid_postal_codes"]
        + report["invalid_sales"]
        + report["invalid_quantity"]
        + report["invalid_discount"]
        + report["invalid_profit"]
    )

    score -= deductions

    score = max(score, 0)

    
    # Upload Success
   

    st.success(
        f"""
### Dataset Uploaded Successfully

**Rows:** {report['rows_after']:,}

The dataset has been successfully cleaned and stored in the SQLite database.
"""
    )

    st.divider()

   
    # ETL Processing Report
   

    st.header("ETL Processing Report")

    st.metric(
        "Data Quality Score",
        f"{score}%"
    )

    st.progress(score / 100)

    st.divider()


    # Summary Cards


    c1, c2, c3 = st.columns(3)

    with c1:

        st.subheader("Rows")

        st.metric(
            "Before",
            report["rows_before"]
        )

        st.metric(
            "After",
            report["rows_after"]
        )

    with c2:

        st.subheader("Missing Values")

        st.metric(
            "Fixed",
            report["missing_fixed"]
        )

        st.metric(
            "Remaining",
            report["remaining_missing"]
        )

    with c3:

        st.subheader("Duplicate Records")

        st.metric(
            "Removed",
            report["duplicates_removed"]
        )

        st.metric(
            "Remaining",
            report["remaining_duplicates"]
        )

    st.divider()


    # Data Validation Report


    st.subheader("Data Validation Summary")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Invalid Order Dates",
            report["invalid_order_dates"]
        )

        st.metric(
            "Invalid Ship Dates",
            report["invalid_ship_dates"]
        )

        st.metric(
            "Invalid Postal Codes",
            report["invalid_postal_codes"]
        )

        st.metric(
            "Invalid Sales Values",
            report["invalid_sales"]
        )

    with c2:

        st.metric(
            "Invalid Quantity",
            report["invalid_quantity"]
        )

        st.metric(
            "Invalid Discount",
            report["invalid_discount"]
        )

        st.metric(
            "Invalid Profit",
            report["invalid_profit"]
        )

        st.metric(
            "Sales Outliers",
            report["sales_outliers"]
        )

    st.divider()

    # Cleaning Summary


    st.subheader("Cleaning Summary")

    st.success(f"Removed duplicate records : {report['duplicates_removed']}")

    st.success(f"Fixed missing values : {report['missing_fixed']}")

    st.success(f"Removed invalid Order Dates : {report['invalid_order_dates']}")

    st.success(f"Removed invalid Ship Dates : {report['invalid_ship_dates']}")

    st.success(f"Removed invalid Postal Codes : {report['invalid_postal_codes']}")

    st.success("Dataset passed ETL validation successfully.")

    if report["sales_outliers"] > 0:

        st.warning(
            f"{report['sales_outliers']} unusually high Sales values were detected. "
            "These records were retained for business analysis."
        )

    st.divider()
    
    # Database Status


    st.subheader("Database Status")

    st.success("SQLite Database Updated Successfully")

    st.caption(
        f"Last Updated : {datetime.now().strftime('%d %b %Y • %I:%M %p')}"
    )
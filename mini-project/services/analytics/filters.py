import streamlit as st
import pandas as pd

from logs.logger import logger


def apply_filters(df):

    df = df.copy()

    # Convert Order Date
    

    try:
        df["Order Date"] = pd.to_datetime(
            df["Order Date"],
            errors="coerce",
        )

        df = df.dropna(subset=["Order Date"])

    except Exception as e:
        logger.exception(e)
        st.sidebar.error("❌ Invalid Order Date column.")
        return df
    
    # Filters Title

    st.sidebar.markdown("---")
    st.sidebar.header("🔎 Filters")


    selected_regions = st.sidebar.multiselect(
        "🌍 Region",
        options=sorted(df["Region"].dropna().unique()),
        default=[],
        key="region_filter",
    )

    

    selected_categories = st.sidebar.multiselect(
        "📦 Category",
        options=sorted(df["Category"].dropna().unique()),
        default=[],
        key="category_filter",
    )
    

    selected_segments = st.sidebar.multiselect(
        "👥 Segment",
        options=sorted(df["Segment"].dropna().unique()),
        default=[],
        key="segment_filter",
    )

    # Date Range

    min_date = df["Order Date"].min().date()
    max_date = df["Order Date"].max().date()

    date_range = st.sidebar.date_input(
        "📅 Order Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if not isinstance(date_range, tuple) or len(date_range) != 2:
        placeholder = st.empty()

        with placeholder.container():
            st.header("📊 Business Overview")

            c1, c2, c3, c4 = st.columns(4)

            for c in [c1, c2, c3, c4]:
                with c:
                    st.metric("Loading...", "—")

            st.divider()

            st.header("📈 Sales Analytics")
            st.info("Loading dashboard...")

        st.stop()
        

    start_date, end_date = date_range


    selected_orders = st.sidebar.multiselect(
       "📦 Order ID",
       options=sorted(df["Order ID"].dropna().unique()),
       default=[],
       key="order_filter",
    )


    selected_customer_ids = st.sidebar.multiselect(
       "🆔 Customer ID",
       options=sorted(df["Customer ID"].dropna().unique()),
       default=[],
       key="customerid_filter",
    )


    selected_customer_names = st.sidebar.multiselect(
       "👤 Customer Name",
       options=sorted(df["Customer Name"].dropna().unique()),
       default=[],
       key="customer_filter",
    )


    selected_products = st.sidebar.multiselect(
       "📦 Product Name",
       options=sorted(df["Product Name"].dropna().unique()),
       default=[],
       key="product_filter",
    )


    selected_ship_modes = st.sidebar.multiselect(
       "🚚 Ship Mode",
       options=sorted(df["Ship Mode"].dropna().unique()),
       default=[],
       key="ship_filter",
    )
    

    selected_subcategories = st.sidebar.multiselect(
      "📂 Sub-Category",
      options=sorted(df["Sub-Category"].dropna().unique()),
      default=[],
      key="subcategory_filter",
    )


    selected_cities = st.sidebar.multiselect(
        "🏙 City",
        options=sorted(df["City"].dropna().unique()),
        default=[],
        key="city_filter",
    )


    selected_states = st.sidebar.multiselect(
        "🗺 State",
        options=sorted(df["State"].dropna().unique()),
        default=[],
        key="state_filter",
    )

    # Clear Filters

    def clear_filters():

        st.session_state.region_filter = []
        st.session_state.category_filter = []
        st.session_state.segment_filter = []

        st.session_state.order_filter = []
        st.session_state.customerid_filter = []
        st.session_state.customer_filter = []
        st.session_state.product_filter = []
        st.session_state.ship_filter = []
        st.session_state.subcategory_filter = []
        st.session_state.city_filter = []
        st.session_state.state_filter = []

        st.rerun()

    st.sidebar.button(
        "🗑 Clear Filters",
        use_container_width=True,
        on_click=clear_filters,
    )

    # Apply Filters

    if selected_regions:
        df = df[df["Region"].isin(selected_regions)]

    if selected_categories:
        df = df[df["Category"].isin(selected_categories)]

    if selected_segments:
        df = df[df["Segment"].isin(selected_segments)]

    df = df[
        (df["Order Date"].dt.date >= start_date)
        &
        (df["Order Date"].dt.date <= end_date)
    ]

    if selected_orders:
        df = df[df["Order ID"].isin(selected_orders)]

    if selected_customer_ids:
        df = df[df["Customer ID"].isin(selected_customer_ids)]

    if selected_customer_names:
        df = df[df["Customer Name"].isin(selected_customer_names)]

    if selected_products:
        df = df[df["Product Name"].isin(selected_products)]

    if selected_ship_modes:
        df = df[df["Ship Mode"].isin(selected_ship_modes)]

    if selected_subcategories:
        df = df[df["Sub-Category"].isin(selected_subcategories)]

    if selected_cities:
        df = df[df["City"].isin(selected_cities)]

    if selected_states:
        df = df[df["State"].isin(selected_states)]


    logger.info(
    f"Filters | "
    f"Region:{selected_regions} | "
    f"Category:{selected_categories} | "
    f"Segment:{selected_segments} | "
    f"Customer:{selected_customer_names} | "
    f"Product:{selected_products}"
)

    return df
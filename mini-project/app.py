import streamlit as st
from streamlit_option_menu import option_menu
from logs.logger import logger

from config.config import (
    APP_TITLE,
    APP_ICON,
    PAGE_LAYOUT,
)
from components.help_dialog import show_help
# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=PAGE_LAYOUT,
    initial_sidebar_state="expanded",
)

logger.info("Application Started")

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("📊 Retail Analytics")
st.sidebar.caption("Business Intelligence Platform")
st.sidebar.divider()

with st.sidebar:

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Dashboard",
            "Upload Data",
            "Reports",
        ],
        icons=[
            "house",
            "speedometer2",
            "cloud-upload",
            "bar-chart",
        ],
        default_index=0,
        styles={
            "container": {
                "padding": "5px",
                "background-color": "#FFFFFF",
                "border": "1px solid #E5E7EB",
                "border-radius": "12px",
            },
            "icon": {
                "color": "#60A5FA",
                "font-size": "18px",
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "padding": "12px",
                "margin": "5px",
                "border-radius": "10px",
                "color": "#374151",
                "--hover-color": "#EFF6FF",
            },
            "nav-link-selected": {
                "background-color": "#2563EB",
                "color": "white",
            },
        },
    )

# --------------------------------------------------
# Help
# --------------------------------------------------

st.sidebar.divider()

with st.sidebar.expander("❓ Help", expanded=False):

    st.write("New to the dashboard?")

    if st.button(
        "🚀 Quick Tour",
        use_container_width=True,
    ):
        show_help()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

if selected == "Home":

    from views.home import show_home

    show_home()

elif selected == "Dashboard":

    from views.dashboard import show_dashboard

    show_dashboard()

elif selected == "Upload Data":

    from views.upload import show_upload_page

    show_upload_page()

elif selected == "Reports":

    from views.reports import show_reports

    show_reports()
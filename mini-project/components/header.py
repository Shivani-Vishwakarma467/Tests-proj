import streamlit as st
from datetime import datetime


def show_header():

    col1, col2 = st.columns([6, 1])

    with col1:
        st.title("📊 Retail Analytics Platform")
        st.caption("Business Intelligence Dashboard")

    with col2:
        st.caption("Updated")
        st.write(datetime.now().strftime("%d %b %Y"))

    st.divider()
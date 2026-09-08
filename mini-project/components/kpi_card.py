import streamlit as st


def kpi_card(title, value, delta):

    st.metric(
        label=title,
        value=value,
        delta=f"{delta:.1f}% MoM",
        delta_color="normal",
    )
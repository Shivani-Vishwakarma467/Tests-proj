import streamlit as st


def show_dataframe(df):

    st.subheader("Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True,
        height=450,
    )
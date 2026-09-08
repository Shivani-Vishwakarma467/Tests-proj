import streamlit as st


def upload_box():

    return st.file_uploader(
        "📂 Upload Dataset",
        type=[
            "csv",
            "xlsx",
            "xls",
        ],
    )
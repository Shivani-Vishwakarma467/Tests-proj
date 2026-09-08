import streamlit as st


def dataset_metrics(df):

    cols = st.columns(4)

    metrics = [

        ("📄 Rows", len(df)),

        ("📑 Columns", len(df.columns)),

        ("⚠ Missing", int(df.isna().sum().sum())),

        ("🗂 Duplicates", int(df.duplicated().sum()))

    ]

    for col, (label, value) in zip(cols, metrics):

        with col:

            st.metric(label, value)
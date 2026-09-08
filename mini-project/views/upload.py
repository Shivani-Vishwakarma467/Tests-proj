import streamlit as st

from components.uploader import upload_box
from components.metrics import dataset_metrics
from components.dataframe import show_dataframe
from components.etl_report import show_etl_report
from logs.logger import logger

from services.data_processing.loader import load_dataset
from services.data_processing.validator import validate_dataset
from services.data_processing.cleaner import clean_dataset

from database.database import save_dataframe


def show_upload_page():

# Check Existing Session


    if "df" in st.session_state:

        df = st.session_state["df"]
        report = st.session_state.get("etl_report")

        st.title("📂 Upload Retail Dataset")

        st.success("A dataset is already loaded into the application.")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Rows", f"{len(df):,}")

        with c2:
            st.metric("Columns", len(df.columns))

        st.divider()

        if st.button(
            "📂 Upload New Dataset",
            use_container_width=True,
        ):

            del st.session_state["df"]

            if "etl_report" in st.session_state:
                del st.session_state["etl_report"]

            st.rerun()

        st.divider()
  
        if report is not None:
            show_etl_report(report)

        st.divider()

        st.subheader("📊 Dataset Summary")
        dataset_metrics(df)

        st.divider()

        show_dataframe(df)
    
        return

    
    # Page Header

    st.title("📂 Upload Retail Dataset")

    st.caption(
        "Upload your retail sales dataset for automated ETL processing."
    )

    st.divider()

    st.info("""
### 📁 Supported File Types

• CSV (.csv)

• Excel (.xlsx)

The uploaded dataset will automatically:

✅ Validate required columns

✅ Clean missing values

✅ Remove duplicate records

✅ Store data into SQLite Database

✅ Prepare Dashboard Analytics
""")

    st.divider()

   
    # Upload Box
  

    uploaded_file = upload_box()

    if uploaded_file is None:
        return

    try:

        # Load Dataset


        df = load_dataset(uploaded_file)

        st.success(
            f"""
### ✅ File Uploaded Successfully

**File Name:** {uploaded_file.name}

Your dataset is now being validated and prepared.
"""
        )

        logger.info(f"Dataset Uploaded: {uploaded_file.name}")

        # Validate Dataset


        missing_columns = validate_dataset(df)

        if missing_columns:

            logger.warning(
                f"Dataset Validation Failed | Missing Columns: {missing_columns}"
            )

            st.error("❌ Invalid Dataset")

            st.write("The following required columns are missing:")

            for column in missing_columns:
                st.write(f"• {column}")

            st.stop()

        # Clean Dataset
  

        with st.spinner("🔄 Processing Dataset..."):

            df, report = clean_dataset(df)

        logger.info(
            f"ETL Completed | Before:{report['rows_before']} | After:{report['rows_after']}"
        )

        # Save Dataset


        st.session_state["df"] = df
        st.session_state["etl_report"] = report

        save_dataframe(df)

        logger.info("SQLite Database Updated Successfully")

        st.success(
            f"""
### 🎉 Dataset Ready

✅ Successfully stored into SQLite Database

📄 Rows : {len(df):,}

📑 Columns : {len(df.columns)}

The dataset is now ready for Dashboard Analytics.
"""
        )

        # ETL Report
    

        show_etl_report(report)

        st.divider()

    
        # Dataset Summary
    

        st.subheader("📊 Dataset Summary")

        dataset_metrics(df)

        st.divider()

        # Dataset Preview


        show_dataframe(df)

        st.divider()

        # Download Clean Dataset

        csv = df.to_csv(index=False).encode("utf-8")

        download = st.download_button(
            label="📥 Download Cleaned Dataset",
            data=csv,
            file_name="Cleaned_Retail_Dataset.csv",
            mime="text/csv",
            use_container_width=True,
        )

        if download:
            logger.info("Cleaned Dataset Downloaded")

    except Exception as e:

        logger.exception(e)

        st.error("❌ Something went wrong while processing the dataset.")


    st.divider()


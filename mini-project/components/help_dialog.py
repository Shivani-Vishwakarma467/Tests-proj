import streamlit as st


@st.dialog("👋 Welcome to Retail Analytics")
def show_help():

    st.markdown("""
## Getting Started

Welcome to the **Retail Analytics Dashboard**.

### Step 1
📂 Upload your retail dataset.

### Step 2
📊 Open Dashboard to view KPIs and charts.

### Step 3
📑 Generate Executive Reports.

### Step 4
🔎 Use Filters to analyze specific Regions, Categories and Segments.

### Step 5
⬇ Export the filtered dataset anytime.

---

Enjoy exploring your data!
""")

    if st.button("Start Exploring 🚀", use_container_width=True):
        st.rerun()
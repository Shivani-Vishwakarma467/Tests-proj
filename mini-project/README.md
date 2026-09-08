# Retail KPI Dashboard

A modern Business Intelligence Dashboard built using **Python**, **Streamlit**, **Pandas**, **SQLite**, and **Plotly** for analyzing retail sales data.

The application performs complete ETL (Extract, Transform, Load) operations, stores cleaned data into SQLite, generates interactive dashboards, business insights, executive reports, and management recommendations.

---

# Project Overview

This project helps businesses analyze retail sales performance through interactive visualizations and automated reporting.

It allows users to:

- Upload retail datasets
- Clean and validate data automatically
- Store processed data into SQLite
- Analyze KPIs
- Filter dashboard dynamically
- View executive insights
- Generate business reports
- Export cleaned datasets
- Track application logs

---

# Features

## Upload Module

- Upload CSV files
- Upload Excel files
- Automatic Dataset Validation
- Required Column Validation
- Missing Value Handling
- Duplicate Removal
- SQLite Storage
- Clean Dataset Download

---

## ETL Processing

The application automatically performs:

- Data Cleaning
- Missing Value Removal
- Duplicate Removal
- Column Validation
- Data Profiling
- Data Quality Score
- ETL Processing Report

---

## Interactive Dashboard

The Dashboard includes:

### KPI Cards

- Total Sales
- Total Profit
- Orders
- Customers
- Products
- Quantity Sold
- Average Discount

Each KPI includes:

- Month-over-Month Growth
- Dynamic Color Indicators
- Trend Status

---

### Dashboard Charts

Interactive charts include:

- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Sales by Segment
- Top Products
- Top Customers

Built using:

- Plotly
- Streamlit

---

## Dynamic Filters

Users can filter the dashboard by:

- Region
- Category
- Segment
- Order Date
- Order ID
- Customer ID
- Customer Name
- Product Name
- Ship Mode

All charts and KPIs update automatically.

---

## Business Insights

Automatically generated insights include:

- Highest Sales Category
- Most Profitable Region
- Best Customer Segment
- Highest Revenue Products

---

## Executive Reports

The Reports page contains:

### Business Health Score

Business performance is evaluated based on:

- Profit Margin
- Discount Percentage
- Overall Business Performance

Health Status:

- Excellent
- Good
- Average
- Poor

---

### Executive KPIs

Management summary includes:

- Total Sales
- Total Profit
- Orders
- Customers

---

### Management Recommendations

Automatically generated recommendations based on data analysis.

Examples include:

- Increase inventory for top-selling categories
- Improve pricing strategy in underperforming regions
- Reduce discount percentage
- Expand marketing in profitable regions

Each recommendation includes:

- Priority Level
- Recommendation
- Business Justification

---

### Category Performance

Displays:

- Sales
- Profit
- Orders

for each category.

---

### Region Performance

Displays:

- Sales
- Profit
- Orders

for each region.

---

### Segment Performance

Displays:

- Sales
- Profit
- Orders

for each customer segment.

---

### Top Products

Displays the highest revenue-generating products.

---

### Top Customers

Displays the highest spending customers.

---

### Executive Business Story

Automatically generates a management summary including:

- Revenue
- Orders
- Top Category
- Profit Summary
- Business Performance

---

# Project Structure

```text
Retail-KPI-Dashboard
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│
├── components/
│   ├── dataframe.py
│   ├── etl_report.py
│   ├── header.py
│   ├── help_dialog.py
│   ├── kpi_card.py
│   ├── metrics.py
│   ├── theme.py
│   └── uploader.py
│
├── config/
│
├── database/
│   └── database.py
│
├── logs/
│   ├── application.log
│   └── logger.py
│
├── services/
│   ├── analytics/
│   │   ├── charts.py
│   │   ├── executive_insights.py
│   │   ├── filters.py
│   │   ├── insights.py
│   │   ├── kpi.py
│   │   └── analytics_reports.py
│   │
│   └── data/
│       ├── cleaner.py
│       ├── loader.py
│       ├── profiler.py
│       └── validator.py
│
└── views/
    ├── dashboard.py
    ├── home.py
    ├── reports.py
    └── upload.py
```

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| Database | SQLite |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| Logging | Python Logging |
| Version Control | Git, GitHub |

---

# Application Workflow

```text
Dataset Upload
      │
      ▼
Dataset Validation
      │
      ▼
Data Cleaning
      │
      ▼
SQLite Storage
      │
      ▼
Dashboard Analytics
      │
      ▼
Business Insights
      │
      ▼
Executive Reports
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/Retail-KPI-Dashboard.git
```

Navigate to the project directory

```bash
cd Retail-KPI-Dashboard
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# Screenshots

You can include screenshots of:

- Home Page
- Upload Module
- ETL Processing Report
- Interactive Dashboard
- Executive Reports

---

# Future Enhancements

- PDF Report Generation
- Excel Report Export
- User Authentication
- Cloud Deployment
- AI-based Sales Forecasting
- Predictive Analytics
- Scheduled Report Generation
- Email Report Automation
- Dark Mode Support

---

# Author

**Voora Tejaswini**

B.Tech – Computer Science & Data Science

Python | Data Analytics | SQL | Streamlit | Machine Learning

---

# License

This project is developed for educational and portfolio purposes.

---

# Acknowledgements

This project was developed using the following open-source technologies:

- Python
- Streamlit
- Pandas
- SQLite
- Plotly

Thanks to the open-source community for providing the tools and libraries used in this project.
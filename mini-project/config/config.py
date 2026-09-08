

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DATA_DIR = BASE_DIR / "data"


EXPORT_DIR = BASE_DIR / "exports"


DATABASE_DIR = BASE_DIR / "database"


ASSETS_DIR = BASE_DIR / "assets"


DATASET_NAME = "superstore.csv"
DATASET_PATH = DATA_DIR / DATASET_NAME

DATABASE_NAME = "retail.db"
DATABASE_PATH = DATABASE_DIR / DATABASE_NAME


APP_TITLE = "📊 Retail KPI Dashboard"

APP_SUBTITLE = (
    "Enterprise Sales Analytics Dashboard built using "
    "Python, Streamlit, Pandas, SQLite and Plotly."
)

APP_ICON = "📊"

PAGE_LAYOUT = "wide"


PRIMARY_COLOR = "#2563EB"

SUCCESS_COLOR = "#16A34A"

WARNING_COLOR = "#F59E0B"

DANGER_COLOR = "#DC2626"

BACKGROUND_COLOR = "#F8FAFC"


REQUIRED_COLUMNS = [
    "Row ID",
    "Order ID",
    "Order Date",
    "Ship Date",
    "Ship Mode",
    "Customer ID",
    "Customer Name",
    "Segment",
    "Country",
    "City",
    "State",
    "Postal Code",
    "Region",
    "Product ID",
    "Category",
    "Sub-Category",
    "Product Name",
    "Sales",
    "Quantity",
    "Discount",
    "Profit",
]
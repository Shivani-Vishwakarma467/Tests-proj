from config.config import DATASET_PATH
from services.data_processing.loader import load_dataset

df = load_dataset(DATASET_PATH)

print(df.head())

print("\nRows:", len(df))
print("Columns:", len(df.columns))
from pathlib import Path

import pandas as pd
from streamlit.runtime.uploaded_file_manager import UploadedFile


def load_dataset(file):

    """
    Loads CSV or Excel files.

    Supports:
    - Local Path
    - UploadedFile (Streamlit)
    """

    if isinstance(file, UploadedFile):

        if file.name.endswith(".csv"):

            encodings = [
                "utf-8",
                "latin1",
                "cp1252",
            ]

            for encoding in encodings:

                try:
                    file.seek(0)
                    return pd.read_csv(file, encoding=encoding)

                except UnicodeDecodeError:
                    continue

            raise ValueError("Unsupported CSV Encoding")

        elif file.name.endswith((".xlsx", ".xls")):

            file.seek(0)
            return pd.read_excel(file)

    # Local File

    file = Path(file)

    if file.suffix == ".csv":

        encodings = [
            "utf-8",
            "latin1",
            "cp1252",
        ]

        for encoding in encodings:

            try:
                return pd.read_csv(file, encoding=encoding)

            except UnicodeDecodeError:
                continue

        raise ValueError("Unsupported CSV Encoding")

    elif file.suffix in [".xlsx", ".xls"]:

        return pd.read_excel(file)

    raise ValueError("Unsupported File")
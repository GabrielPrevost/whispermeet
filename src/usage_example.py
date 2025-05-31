from pathlib import Path
from typing import Dict, List

import pandas as pd


class DataProcessor:
    """Basic data processing utility class."""

    def __init__(self, input_path: Path):
        self.input_path = input_path

    def read_csv(self) -> pd.DataFrame:
        """Read CSV file from input path."""
        return pd.read_csv(self.input_path)

    @staticmethod
    def calculate_stats(data: pd.DataFrame) -> Dict[str, float]:
        """Calculate basic statistics for numeric columns."""
        numeric_cols = data.select_dtypes(include=["float64", "int64"]).columns
        return {
            col: {"mean": data[col].mean(), "std": data[col].std()}
            for col in numeric_cols
        }

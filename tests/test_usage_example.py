from pathlib import Path

import pandas as pd
import pytest

from src.usage_example import DataProcessor

# This fixture provides a small sample DataFrame for testing.
@pytest.fixture
def sample_df():
    return pd.DataFrame({"numeric": [1, 2, 3, 4, 5], "text": ["a", "b", "c", "d", "e"]})

def test_calculate_stats(sample_df):
    # This creates a DataProcessor instance to test its methods.
    processor = DataProcessor(Path("dummy/path"))

    # This calls 'calculate_stats' on the sample DataFrame.
    stats = processor.calculate_stats(sample_df)

    # These assertions confirm numeric columns are processed,
    # their mean is correct, and text columns are ignored.
    assert "numeric" in stats
    assert abs(stats["numeric"]["mean"] - 3.0) < 1e-10
    assert "text" not in stats

def test_read_csv(tmp_path):
    # This test ensures that CSV files are read correctly into DataFrames.
    test_file = tmp_path / "test.csv"
    pd.DataFrame({"a": [1, 2, 3]}).to_csv(test_file, index=False)

    # This creates a test CSV file and initializes the DataProcessor with it.
    processor = DataProcessor(test_file)
    df = processor.read_csv()

    # These checks confirm the DataFrame is read correctly from CSV.
    assert len(df) == 3
    assert "a" in df.columns

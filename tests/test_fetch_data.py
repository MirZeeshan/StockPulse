"""
Tests for the data fetching functionality.
"""

import os
import sys
import pandas as pd

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data.fetch_data import fetch_stock_data


def test_fetch_stock_data():
    """Test that we can fetch stock data successfully."""
    ticker = "AAPL"
    df = fetch_stock_data(ticker, period="1mo", save=False)

    # Check that we got some data
    assert len(df) > 0

    # Check that the dataframe has the expected columns
    expected_columns = ["date", "open", "high", "low", "close", "volume"]
    assert all(col in df.columns.str.lower() for col in expected_columns)

    print("Fetch data test passed!")


if __name__ == "__main__":
    test_fetch_stock_data()

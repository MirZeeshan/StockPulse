"""
Module for fetching stock data from various sources.
"""

import os
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta


def fetch_stock_data(ticker, period="5y", interval="1d", save=True):
    """
    Fetch historical stock data using Yahoo Finance.

    Args:
        ticker (str): Stock ticker symbol
        period (str): Data period (e.g., '1d', '5d', '1mo', '3mo', '1y', '5y', 'max')
        interval (str): Data interval (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m',
                        '1h', '1d', '5d', '1wk', '1mo', '3mo')
        save (bool): Whether to save the data to a CSV file

    Returns:
        pd.DataFrame: Historical stock data
    """
    print(f"Fetching data for {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)

    # Reset index to make Date a column
    df = df.reset_index()

    # Basic data cleaning
    df.columns = [col.lower() for col in df.columns]

    if save:
        # Create data directory if it doesn't exist
        os.makedirs("data/raw", exist_ok=True)

        # Save to CSV
        file_path = f"data/raw/{ticker}_{interval}_{period}.csv"
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")

    return df


def main():
    """Main function to fetch data for a list of tickers."""
    # Example usage
    tickers = ["SPY"]  # Start with S&P 500 ETF

    for ticker in tickers:
        df = fetch_stock_data(ticker)
        print(f"Retrieved {len(df)} rows of data for {ticker}")
        print(df.head())


if __name__ == "__main__":
    main()

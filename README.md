# Stock Price Prediction Model

A machine learning project that predicts stock price movements using historical data and technical indicators.

## Project Overview

This project uses Python to build, train, and evaluate predictive models for stock prices. It implements:
- Data collection from Yahoo Finance
- Exploratory data analysis with visualization
- Feature engineering using technical indicators
- Machine learning models including regression and deep learning approaches
- Model evaluation and hyperparameter tuning
- Interactive visualizations of predictions

## Setup and Installation

### Using Docker (Recommended)

```bash
# Build and run the Docker container
docker-compose up -d

# Run Jupyter notebook
docker-compose exec stock-prediction jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

### Manual Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Fetch historical stock data:
   ```bash
   python -m src.data.fetch_data
   ```

2. Run exploratory data analysis:
   ```bash
   jupyter notebook notebooks/01_eda.ipynb
   ```

## Project Structure

```
stock_prediction_project/
├── data/
│   ├── raw/             # Original data
│   └── processed/       # Processed datasets
├── notebooks/
├── src/
│   ├── data/            # Data loading and processing
│   ├── features/        # Feature engineering
│   ├── models/          # Model training and prediction
│   └── visualization/   # Data visualization
├── tests/               # Unit tests
├── .github/workflows/   # CI/CD configuration
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker services configuration
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

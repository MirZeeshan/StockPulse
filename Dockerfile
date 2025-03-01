FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set up a non-root user
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

# Default command
CMD jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

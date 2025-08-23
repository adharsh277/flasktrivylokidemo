FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Ensure Python outputs are sent straight to logs
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create log directory
RUN mkdir -p /var/log && touch /var/log/flask_app.log

# Copy application code
COPY app.py .

# Expose Flask port
EXPOSE 5000

# Start app
CMD ["python", "app.py"]

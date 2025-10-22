# Use official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy application files
COPY game.py requirements.txt test_game.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command when container runs
CMD ["python", "game.py"]



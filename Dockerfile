# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy your entire Portfolio folder content to /app
COPY . /usr/share/nginx/html

# Install dependencies
# (Make sure you have requirements.txt inside Portfolio folder)
RUN pip install --no-cache-dir -r requirements.txt

# Expose port your Flask app will run on (usually 5000)
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

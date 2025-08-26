FROM python:3.11-slim

WORKDIR /app

# Copy only the files you need
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the rest of your app
COPY . .

EXPOSE 8080
CMD ["python", "app.py"]  # Replace with your actual entry point

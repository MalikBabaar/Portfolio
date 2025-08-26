FROM python:3.8-slim

WORKDIR /app

# Copy only requirements file first to leverage Docker cache
COPY requirements.txt .

# Install python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app source code
COPY . .

# Expose the port your app listens on (change if needed)
EXPOSE 8080

# Command to run your app (replace app.py with your entry point)
CMD ["python", "app.py"]

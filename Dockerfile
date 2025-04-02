# Use the official Python 3.11 image as a base
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose a port (Render dynamically assigns the PORT, so we will set it in CMD)
EXPOSE 10000

# Run the Flask app using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:10000", "app:app"]

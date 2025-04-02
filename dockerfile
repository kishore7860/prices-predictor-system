# Use an official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port (if it's a web app)
EXPOSE 5000

# Run the app (change if needed)
CMD ["python", "app.py"]

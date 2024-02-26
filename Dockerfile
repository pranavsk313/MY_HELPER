# Use the official Python image from Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for app.py and port 5001 for app1.py
EXPOSE 5000
EXPOSE 5001

# Set up configuration files
COPY config.json /app
COPY helper.sql /app

# Define the command to run the Flask applications
CMD ["python", "app.py"]

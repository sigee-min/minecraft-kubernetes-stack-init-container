# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the Python script into the container at /app
COPY init_container.py /app/

# Install any needed packages specified in requirements.txt
RUN pip install requests

# Define environment variable
ENV PLUGIN_URLS=""

# Run init_container.py when the container launches
CMD ["python", "init_container.py"]

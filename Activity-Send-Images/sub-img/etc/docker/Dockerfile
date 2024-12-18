# Use a slim Python 3.12 base image that already includes Python
FROM python:3.12-slim

# Set the working directory for "/app" inside the container
# This means that all subsequent commands will be executed inside the /app directory
WORKDIR /app

# Copy the 'sub-img.py' script into the '/app' directory in the container
COPY sub-img.py .

# Copy the 'requirements.txt' file into the '/app' directory in the container
COPY requirements.txt .

# Install Python dependencies specified in the 'requirements.txt' file
RUN pip install -r requirements.txt

# Set the default command to run the 'sub-img.py' script when the container starts
CMD ["python", "sub-img.py"]

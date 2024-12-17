# Creating Images Docker

Objective: Send and receive images using the Pub/Sub model with a RabbitMQ broker.

## 1 Create the Dockerfile

First, create a file called Dockerfile. This file defines how your Docker image will be built.

Dockerfile Example:
```
# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the application
CMD ["python", "app.py"]

```
## 2 Prepare the environment

Make sure all required files (like app.py, requirements.txt) are in the same directory as the Dockerfile.

## 3 Build the Image

Run the command to build the Docker image:

```
docker build -t nome-da-imagem:v1 .
```
Note: If you are uploading the image to Docker Hub, use the same name as the repository created.

## Check the Created Image

List the images to confirm that the image was created:

```
docker images
```
## Run a Container Using the Image
Create and launch a container based on the created image:
```
docker run image-name
```







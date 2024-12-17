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

## 4 Check the Created Image

List the images to confirm that the image was created:

```
docker images
```
## 5 Run a Container Using the Image
Create and launch a container based on the created image:
```
docker run image-name
```
# Docker Hub

## 1 Login in
```
docker login
```

## 2 Upload New Version to Docker Hub
```
docker push usuario123/meu-app:2.0
```

## 3 Use the Image
Now your image will be publicly available on Docker Hub and can be used on any machine with the command:
```
docker pull usuario123/meu-app:2.0
```

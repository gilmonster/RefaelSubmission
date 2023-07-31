# Use an official Python runtime as the base image
FROM python:3.9

# Install CMake
RUN apt-get update && apt-get install -y cmake

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project code to the working directory
COPY . .

# Set the full path to the CMake executable within the container using ARG
ARG cmake_path="C:\\Program Files\\CMake\\bin"
ENV PATH="${cmake_path}:${PATH}"

# Set the command to run when the container starts
CMD ["python", "DevelopmentScript.py"]

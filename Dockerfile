# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project code to the working directory
COPY . .

# Set the command to run when the container starts
CMD ["python", "DevelopmentScript.py"]

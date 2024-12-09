FROM python:3.10-slim

# Create and set working directory
RUN mkdir /CTF
WORKDIR /CTF

# Copy dependencies and install system packages
COPY requirements.txt .
RUN pip install -r requirements.txt 

# Copy the rest of the application
COPY . .

# Ensure scripts are executable
RUN chmod +x docker/app.sh
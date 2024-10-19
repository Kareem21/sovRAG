# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



## If using GPU, base it on a CUDA-compatible image
# FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04

# # Install any additional requirements for GPU inference
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     libgl1-mesa-glx && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # Add NVIDIA support
# ENV NVIDIA_VISIBLE_DEVICES all
# ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

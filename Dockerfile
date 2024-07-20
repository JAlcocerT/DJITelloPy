# Use an official Python runtime as a parent image - https://hub.docker.com/layers/library/python/3.9.19-slim-bullseye/images/sha256-76536676b48862b2f37d39cf6849b01f322eaa84d80fec3c354f24236025414e?context=explore
FROM python:3.9.19-slim-bullseye
# python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required system libraries
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements-examples.txt
#RUN pip install djitellopy==1.5 opencv-python==4.4.0.46 pygame==2.0.1 numpy==1.26.0

# Run your Python script when the container launches
#CMD ["python", "your_script.py"]


#docker build -t djitellopy .
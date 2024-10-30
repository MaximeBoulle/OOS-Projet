# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /

# Copy the requirements file
COPY ./requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=$PYTHONPATH:/generated

# Expose the gRPC port
EXPOSE 50051

# Command to start your gRPC server
CMD ["python", "grpc_server.py"]
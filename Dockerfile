# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY server.py .

# Install Flask
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the server
CMD ["python", "server.py"]


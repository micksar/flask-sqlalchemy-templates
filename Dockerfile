# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install any needed packages specified in requirements.txt and other packages before that
RUN apt-get update && \
    apt-get install -y libmariadb-dev && \
    apt-get install -y build-essential

RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port that the app will run on
EXPOSE 5000

# Define a healthcheck that tests if the app is up
HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl --fail http://localhost:5000/health || exit 1

# Run the command to start the app when the container starts up
CMD [ "python3", "App.py"]

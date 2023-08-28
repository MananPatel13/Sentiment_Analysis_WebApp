# Use an official Python runtime as a parent image
FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /web_app

# Set the working directory in the container
WORKDIR /web_app

# Copy the current directory contents into the container at /web_app
COPY . /web_app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
# EXPOSE 8000

# Define environment variables
ENV DJANGO_SETTINGS_MODULE=web_app.settings

# Run the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

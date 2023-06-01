# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . .

# Expose the port that Django runs on
EXPOSE 5000

# Define the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]

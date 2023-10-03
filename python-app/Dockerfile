# Use an official Python image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Install Flask and other dependencies
RUN pip install Flask==2.2 Flask-SQLAlchemy==3.0 psycopg2-binary==2.9.1

# Copy your project files into the container
COPY . .

# Expose the port your Flask app will run on
EXPOSE 5000

# Command to run your Flask app
CMD ["python", "app.py"]


# Use a base image with your application dependencies
FROM node:14

# Install Supervisor and cron
RUN apt-get update && apt-get install -y supervisor cron && \
    apt-get clean

# Create a directory for your applications
WORKDIR /app

# Copy app3 files and install dependencies
COPY package.json /app/
COPY package-lock.json /app/
RUN npm install

# Copy the rest of app3 files
COPY a1.js /app/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 3003 (if your application uses this port)
EXPOSE 3003

# Start Supervisor when the container starts, and also start cron
CMD ["supervisord", "-n"]


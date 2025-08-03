#!/bin/bash

# Backend Startup Script for EC2 Deployment
# Save this as start_backend.sh and make it executable: chmod +x start_backend.sh

echo "=== Flask Backend Startup Script ==="

# Update system
echo "Updating system packages..."
sudo yum update -y

# Install Python 3 and pip
echo "Installing Python 3 and pip..."
sudo yum install python3 python3-pip -y

# Install required Python packages
echo "Installing Flask and dependencies..."
pip3 install flask flask-cors gunicorn

# Navigate to backend directory
cd /home/ec2-user/Backend

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=production

# Start the Flask application with Gunicorn
echo "Starting Flask application on port 5000..."
echo "Backend will be available at: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4):5000"

# For development (single threaded)
# python3 app.py

# For production (multi-threaded with Gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 app:app --daemon

echo "Backend started successfully!"
echo "Health check: curl http://localhost:5000/health"
echo "API endpoints available at: http://localhost:5000/api/users"

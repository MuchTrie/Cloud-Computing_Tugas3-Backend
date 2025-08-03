# Deployment Configuration for EC2

## Backend Configuration (app.py)

# For production deployment on EC2, modify the last lines of app.py:

if __name__ == '__main__':
    # For production deployment
    app.run(host='0.0.0.0', port=5000, debug=False)

## Environment Variables (create .env file if needed)
FLASK_ENV=production
FLASK_DEBUG=False

## EC2 Security Group Rules
# Inbound Rules:
# - HTTP (80) from 0.0.0.0/0
# - HTTPS (443) from 0.0.0.0/0  
# - Custom TCP (5000) from frontend server IP or 0.0.0.0/0
# - SSH (22) from your IP

## Backend Server Commands
# Install Python and pip
sudo yum update -y
sudo yum install python3 python3-pip -y

# Install requirements
pip3 install flask flask-cors

# Run application
python3 app.py

# Or use gunicorn for production:
pip3 install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

## Frontend Configuration
# Update the API_BASE_URL in script.js to point to backend server:
# const API_BASE_URL = 'http://BACKEND_SERVER_IP:5000';

## Frontend Server Commands  
# Install nginx
sudo yum update -y
sudo yum install nginx -y

# Start nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# Copy files to nginx directory
sudo cp -r /path/to/frontend/* /var/www/html/

# Or use Python simple server for testing:
cd /path/to/frontend
python3 -m http.server 80

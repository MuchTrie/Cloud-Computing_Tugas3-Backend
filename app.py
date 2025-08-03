from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)

# Simple CORS setup for development
CORS(app)

# Path to data file
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

def load_data():
    """Load data from JSON file"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": [], "meta": {"total_users": 0, "last_updated": "", "data_source": ""}}
    except json.JSONDecodeError:
        return {"users": [], "meta": {"total_users": 0, "last_updated": "", "data_source": ""}}

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Flask REST API Server - Tugas 3",
        "status": "running",
        "backend_url": "http://13.210.70.244:5000",
        "available_endpoints": [
            "/api/users - Get all users",
            "/api/users/<id> - Get user by ID", 
            "/health - Health check"
        ]
    })

@app.route('/api/users', methods=['GET'])
def get_all_users():
    """Get all users"""
    data = load_data()
    return jsonify({
        "status": "success",
        "data": data["users"],
        "meta": data["meta"]
    })

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """Get user by ID"""
    data = load_data()
    user = next((u for u in data["users"] if u["id"] == user_id), None)
    
    if user:
        return jsonify({
            "status": "success",
            "data": user
        })
    else:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

@app.route('/api/users/city/<string:city>', methods=['GET'])
def get_users_by_city(city):
    """Get users by city"""
    data = load_data()
    users = [u for u in data["users"] if u["city"].lower() == city.lower()]
    
    return jsonify({
        "status": "success",
        "data": users,
        "count": len(users),
        "filter": f"city = {city}"
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Flask REST API - Tugas 3",
        "backend_server": "13.210.70.244:5000",
        "message": "Backend berjalan dengan baik"
    })

if __name__ == '__main__':
    # Development mode untuk tugas
    print("="*50)
    print("🚀 TUGAS 3 - BACKEND FLASK API")
    print("="*50)
    print("Server akan berjalan di: http://13.210.70.244:5000")
    print("Health check: http://13.210.70.244:5000/health")
    print("API users: http://13.210.70.244:5000/api/users")
    print("="*50)
    app.run(host='0.0.0.0', port=5000, debug=True)

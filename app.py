from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)

# Konfigurasi CORS untuk production
CORS(app, 
     origins="*",  # Allow all origins
     methods=['GET', 'POST', 'OPTIONS'],
     allow_headers=['Content-Type', 'Authorization', 'Access-Control-Allow-Origin'],
     supports_credentials=True)

# Load data dari JSON file
def load_data():
    """Load data dari file JSON"""
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": [], "meta": {"total_users": 0, "error": "Data file not found"}}
    except json.JSONDecodeError:
        return {"users": [], "meta": {"total_users": 0, "error": "Invalid JSON format"}}

# Load data saat aplikasi start
DATA = load_data()
USERS = DATA.get('users', [])
META = DATA.get('meta', {})

@app.route('/')
def home():
    """API Info endpoint"""
    response = jsonify({
        "message": "🇮🇩 Backend Flask API - Data Pengguna Indonesia",
        "status": "active",
        "server_info": {
            "host": "13.210.70.244",
            "port": 5000,
            "environment": "production"
        },
        "data_info": META,
        "endpoints": {
            "GET /": "API Information",
            "GET /api/users": "Get all users",
            "GET /api/users/<id>": "Get user by ID (1-8)"
        },
        "usage_examples": {
            "all_users": "http://13.210.70.244:5000/api/users",
            "user_by_id": "http://13.210.70.244:5000/api/users/1"
        }
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/users', methods=['GET'])
def get_all_users():
    """Get all users endpoint"""
    response = jsonify({
        "status": "success",
        "message": "Data berhasil diambil",
        "data": USERS,
        "total": len(USERS),
        "meta": META
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """Get user by ID endpoint"""
    user = next((user for user in USERS if user["id"] == user_id), None)
    
    if user:
        response = jsonify({
            "status": "success",
            "message": f"Data {user['name']} berhasil ditemukan",
            "data": user
        })
    else:
        response = jsonify({
            "status": "error",
            "message": f"Pengguna dengan ID {user_id} tidak ditemukan",
            "available_ids": [user["id"] for user in USERS]
        })
        response.status_code = 404
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

# Add OPTIONS handler for preflight requests
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = jsonify({})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response

if __name__ == '__main__':
    print("🚀 Starting Flask Backend Server...")
    print(f"📊 Loaded {len(USERS)} users from data.json")
    print("🌐 API tersedia di: http://13.210.70.244:5000")
    print("📋 Endpoints:")
    print("   GET / - API Information")
    print("   GET /api/users - All users") 
    print("   GET /api/users/<id> - User by ID")
    print("🔗 Frontend dapat akses via public IP")
    print("=" * 50)
    
    # Production configuration
    app.run(
        debug=False,  # Disable debug untuk production
        host='0.0.0.0', 
        port=5000,
        threaded=True  # Enable threading untuk multiple requests
    )

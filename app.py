from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)

# Konfigurasi CORS
CORS(app, origins="*")  # Allow all origins untuk simplicity

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
    return jsonify({
        "message": "🇮🇩 Backend Flask API - Data Pengguna Indonesia",
        "status": "active",
        "data_info": META,
        "endpoints": {
            "GET /": "API Information",
            "GET /api/users": "Get all users",
            "GET /api/users/<id>": "Get user by ID (1-8)"
        },
        "usage_examples": {
            "all_users": f"{request.host_url}api/users",
            "user_by_id": f"{request.host_url}api/users/1"
        }
    })

@app.route('/api/users', methods=['GET'])
def get_all_users():
    """Get all users endpoint"""
    return jsonify({
        "status": "success",
        "message": "Data berhasil diambil",
        "data": USERS,
        "total": len(USERS),
        "meta": META
    })

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """Get user by ID endpoint"""
    user = next((user for user in USERS if user["id"] == user_id), None)
    
    if user:
        return jsonify({
            "status": "success",
            "message": f"Data {user['name']} berhasil ditemukan",
            "data": user
        })
    else:
        return jsonify({
            "status": "error",
            "message": f"Pengguna dengan ID {user_id} tidak ditemukan",
            "available_ids": [user["id"] for user in USERS]
        }), 404

if __name__ == '__main__':
    print("🚀 Starting Flask Backend Server...")
    print(f"📊 Loaded {len(USERS)} users from data.json")
    print("🌐 API tersedia di: http://localhost:5000")
    print("📋 Endpoints:")
    print("   GET / - API Information")
    print("   GET /api/users - All users") 
    print("   GET /api/users/<id> - User by ID")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)

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
        "available_endpoints": [
            "/api/users - Get all users",
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

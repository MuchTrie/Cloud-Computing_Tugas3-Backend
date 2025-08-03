from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)

# Configure CORS with specific settings for production
CORS(app, origins=['*'], allow_headers=['Content-Type', 'Authorization'], methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])

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

def save_data(data):
    """Save data to JSON file"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Flask REST API Server",
        "status": "running",
        "endpoints": {
            "GET /": "API information",
            "GET /api/users": "Get all users",
            "GET /api/users/<id>": "Get user by ID",
            "GET /api/users/city/<city>": "Get users by city",
            "GET /api/users/job/<job>": "Get users by job",
            "POST /api/users": "Create new user",
            "PUT /api/users/<id>": "Update user by ID",
            "DELETE /api/users/<id>": "Delete user by ID"
        }
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
        "count": len(users)
    })

@app.route('/api/users/job/<string:job>', methods=['GET'])
def get_users_by_job(job):
    """Get users by job/pekerjaan"""
    data = load_data()
    users = [u for u in data["users"] if job.lower() in u["pekerjaan"].lower()]
    
    return jsonify({
        "status": "success",
        "data": users,
        "count": len(users)
    })

@app.route('/api/users', methods=['POST'])
def create_user():
    """Create new user"""
    try:
        new_user = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'age', 'city', 'pekerjaan', 'hobi']
        for field in required_fields:
            if field not in new_user:
                return jsonify({
                    "status": "error",
                    "message": f"Missing required field: {field}"
                }), 400
        
        data = load_data()
        
        # Generate new ID
        new_id = max([u["id"] for u in data["users"]], default=0) + 1
        new_user["id"] = new_id
        
        # Add new user
        data["users"].append(new_user)
        data["meta"]["total_users"] = len(data["users"])
        
        # Save data
        if save_data(data):
            return jsonify({
                "status": "success",
                "message": "User created successfully",
                "data": new_user
            }), 201
        else:
            return jsonify({
                "status": "error",
                "message": "Failed to save user"
            }), 500
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error creating user: {str(e)}"
        }), 500

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user by ID"""
    try:
        update_data = request.get_json()
        data = load_data()
        
        # Find user
        user_index = next((i for i, u in enumerate(data["users"]) if u["id"] == user_id), None)
        
        if user_index is None:
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404
        
        # Update user data
        for key, value in update_data.items():
            if key != "id":  # Don't allow ID updates
                data["users"][user_index][key] = value
        
        # Save data
        if save_data(data):
            return jsonify({
                "status": "success",
                "message": "User updated successfully",
                "data": data["users"][user_index]
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Failed to update user"
            }), 500
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error updating user: {str(e)}"
        }), 500

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete user by ID"""
    try:
        data = load_data()
        
        # Find and remove user
        user_index = next((i for i, u in enumerate(data["users"]) if u["id"] == user_id), None)
        
        if user_index is None:
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404
        
        deleted_user = data["users"].pop(user_index)
        data["meta"]["total_users"] = len(data["users"])
        
        # Save data
        if save_data(data):
            return jsonify({
                "status": "success",
                "message": "User deleted successfully",
                "data": deleted_user
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Failed to delete user"
            }), 500
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error deleting user: {str(e)}"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Flask REST API",
        "timestamp": "2025-08-03",
        "server_ip": "13.210.70.244"
    })

# Add error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found",
        "code": 404
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error", 
        "message": "Internal server error",
        "code": 500
    }), 500

if __name__ == '__main__':
    # For production deployment on EC2
    print("Starting Flask API server...")
    print("Server will be available at: http://13.210.70.244:5000")
    print("Health check: http://13.210.70.244:5000/health")
    print("API endpoints: http://13.210.70.244:5000/api/users")
    app.run(host='0.0.0.0', port=5000, debug=False)

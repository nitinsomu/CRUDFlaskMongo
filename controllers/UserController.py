from flask import jsonify, request
from bson import ObjectId, json_util
from werkzeug.security import generate_password_hash
from models.User import User

def get_all_users(mongo):
    users = mongo.db.users.find()
    return jsonify([User.serialize(user) for user in users]), 200

def get_user_by_id(mongo, user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(User.serialize(user)), 200

def create_user(mongo):
    data = request.json
    if not all(key in data for key in ("name", "email", "password")):
        return jsonify({"error": "Missing fields"}), 400
    hashed_password = generate_password_hash(data["password"])
    user = {"name": data["name"], "email": data["email"], "password": hashed_password}
    result = mongo.db.users.insert_one(user)
    return jsonify({"id": str(result.inserted_id)}), 201

def update_user(mongo, user_id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    result = mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})
    if result.matched_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User updated successfully"}), 200

def delete_user(mongo, user_id):
    result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200

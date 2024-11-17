from flask import Blueprint
from controllers.UserController import get_all_users, get_user_by_id, create_user, update_user, delete_user

def create_user_bp(mongo):
    user_bp = Blueprint("user_bp", __name__)

    @user_bp.route("/", methods=["GET"])
    def get_users():
        return get_all_users(mongo)

    @user_bp.route("/<user_id>", methods=["GET"])
    def get_user(user_id):
        return get_user_by_id(mongo, user_id)

    @user_bp.route("/", methods=["POST"])
    def add_user():
        return create_user(mongo)

    @user_bp.route("/<user_id>", methods=["PUT"])
    def edit_user(user_id):
        return update_user(mongo, user_id)

    @user_bp.route("/<user_id>", methods=["DELETE"])
    def remove_user(user_id):
        return delete_user(mongo, user_id)

    return user_bp

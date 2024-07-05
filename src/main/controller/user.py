import logging
from flask import Blueprint, jsonify, request
from main.service.user import UserService


class UserController:
    def __init__(self):
        # services
        self.user_service = UserService()

        # blueprint
        self.user_blueprint = Blueprint("user", __name__)

        # routes
        self.user_blueprint.route("/user/login", methods=["POST"])(self.login)
        self.user_blueprint.route("/user", methods=["POST"])(self.add_user)

        # logger
        self.logger = logging.getLogger(__name__)

    def login(self):
        try:
            data = request.get_json()
            email = data.get("email")
            password = data.get("password")
            user = self.user_service.user_exists(email, password)

            if user:
                return (
                    jsonify(
                        {
                            "name": user.name,
                            "username": user.username,
                            "role": user.role,
                            "branch": user.branch,
                            "password": user.password,
                            "email": user.email,
                            "zone": user.zone,
                        }
                    ),
                    200,
                )
            else:
                return jsonify({"message": "Invalid username or password"}), 401
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return jsonify({"error": str(e)}), 500

    def add_user(self):
        try:
            data = request.get_json()
            self.user_service.add_user(data)
            return jsonify({"message": "User added successfully"}), 200
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return jsonify({"error": str(e)}), 500

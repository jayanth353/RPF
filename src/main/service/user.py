import logging
import uuid
from main.app import db
from main.model.user import User


class UserService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def user_exists(self, email, password):
        try:
            user = User.query.filter_by(email=email, password=password).first()
            return user
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            raise e

    def add_user(self, data):
        try:
            name = data.get("name")
            username = data.get("username")
            password = data.get("password")
            role = data.get("role")
            branch = data.get("branch")
            zone = data.get("zone")
            email = data.get("email")
            new_user = User(
                name=name,
                username=username,
                password=password,
                role=role,
                branch=branch,
                zone=zone,
                email=email,
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            raise e

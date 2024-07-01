import logging
import uuid
from main.app import db
from main.model.user import User


class UserService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def user_exists(self, username, password):
        try:
            user = User.query.filter_by(username=username, password=password).first()
            return user
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            raise e
       
    def add_user(self,data):
        try:
            name = data.get("name")
            username = data.get("username")
            password = data.get("password")
            role = data.get("role")
            branch = data.get("branch")
            new_user = User(name=name,username=username,password=password,role=role,branch=branch)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            raise e

            
            
import os
from main.app import app, db


if __name__ == "__main__":
    with app.app_context():
        from main.controller.user import UserController
        from main.controller.entry import EntryController

        user_controller = UserController()
        entry_controller = EntryController()
        app.register_blueprint(user_controller.user_blueprint)
        app.register_blueprint(entry_controller.entry_blueprint)
        from main.model import user, entry

        db.create_all()
    if os.getenv("FLASK_ENV") == "development":
        app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=True)

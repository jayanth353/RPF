import logging
from flask import Blueprint, jsonify, request
from main.service.entry import EntryService


class EntryController:
    def __init__(self):
        # services
        self.entry_service = EntryService()

        # blueprint
        self.entry_blueprint = Blueprint("entry", __name__)

        # routes
        self.entry_blueprint.route("/entry", methods=["POST"])(self.add_entry)
        self.entry_blueprint.route("/entry", methods=["GET"])(self.get_all_entries)
        self.entry_blueprint.route("/entry/filter", methods=["POST"])(
            self.get_entries_by_date_range
        )

        # logger
        self.logger = logging.getLogger(__name__)

    def add_entry(self):
        try:
            data = request.get_json()
            entries = data["entries"]
            for entry in entries:
                self.entry_service.add_entry(
                    name=entry["name"],
                    details=entry["details"],
                    gd_number=entry["gd_number"],
                    zone=entry["zone"],
                )
            return jsonify({"message": "Added successfully"}), 401
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return jsonify({"error": str(e)}), 500

    def get_all_entries(self):
        try:
            entries = self.entry_service.get_all_entries()
            return jsonify({"entries": entries}), 200
        except Exception as e:
            self.logger.error(f"An error occurred while fetching entries: {e}")
            return jsonify({"error": str(e)}), 500

    def get_entries_by_date_range(self):
        try:
            data = request.get_json()
            start_date = data.get("start_date")
            end_date = data.get("end_date")

            entries = self.entry_service.get_entries_by_date_range(start_date, end_date)

            return jsonify({"filtered_entries": entries}), 200
        except Exception as e:
            self.logger.error(
                f"An error occurred while fetching entries by date range: {e}"
            )
            return jsonify({"error": str(e)}), 500

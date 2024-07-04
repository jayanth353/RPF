import logging
import uuid
from main.app import db
from main.model.entry import Entry
from datetime import datetime


class EntryService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def add_entry(self, details, name, gd_number, zone):
        try:
            new_entry = Entry(
                name=name, details=details, gd_number=gd_number, zone=zone
            )
            db.session.add(new_entry)
            db.session.commit()
            return new_entry
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            raise e

    def get_all_entries(self):
        try:
            entries = Entry.query.all()
            entries_list = []
            for entry in entries:
                entries_list.append(
                    {
                        "id": entry.id,
                        "name": entry.name,
                        "gd_number": entry.gd_number,
                        "details": entry.details,
                        "date": entry.date,
                        "zone": entry.zone,
                    }
                )
            return entries_list
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            raise e

    def get_entries_by_date_range(self, start_date, end_date):
        try:
            # Convert start_date and end_date from MM-DD-YYYY format to datetime objects
            start_datetime = datetime.strptime(start_date, "%d-%m-%Y")
            end_datetime = datetime.strptime(end_date, "%d-%m-%Y")

            # Query entries within the date range
            entries = Entry.query.filter(
                Entry.date.between(start_datetime, end_datetime)
            ).all()
            entries_list = []
            for entry in entries:
                entries_list.append(
                    {
                        "id": entry.id,
                        "name": entry.name,
                        "gd_number": entry.gd_number,
                        "details": entry.details,
                        "zone": entry.zone,
                        "date": entry.date,
                    }
                )
            return entries_list
        except Exception as e:
            self.logger.error(
                f"An error occurred while fetching entries by date range: {e}"
            )
            raise e

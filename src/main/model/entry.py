from main.app import db, ma
from datetime import datetime


# Entry Model
class Entry(db.Model):
    __tablename__ = "Entry"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gd_number = db.Column(db.Integer)
    name = db.Column(db.String(250), nullable=False)
    details = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return "<Entry %r>" % self.name

    def __init__(self, name, details, gd_number):
        self.name = name
        self.details = details
        self.gd_number = gd_number
        self.date = datetime.now()


# Entry Schema
class EntrySchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "details", "gd_number", "date")


# Init Schema
entry_schema = EntrySchema()

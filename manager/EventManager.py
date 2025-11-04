import csv
from model.event import Event
from model.subscription import Subscription
from model.member import Member
from interface.StorageInterface import StorageInterface
# ---------------- Event Manager ----------------
class EventManager:
    def __init__(self, storage):
        self.storage = storage

    def load_events(self, filename):
        data = self.storage.load(filename)
        return [
            Event(
                name=row['event_name'],
                description=row['description'],
                date=row['event_date'],
                organizer=row['organizer'],
                participants=row['participants'].split(',') if row['participants'] else []
            )
            for row in data
        ]


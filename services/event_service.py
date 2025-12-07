# services/event_service.py

from services.CSVStorage import CSVStorage
from observer.subject import SubjectMixin
from model.event import Event


class EventFactory:
    @staticmethod
    def create_event(name, description, date, organizer, participants):
        return Event(
            name=name,
            description=description,
            date=date,
            organizer=organizer,
            participants=participants
        )


class EventService(SubjectMixin):
    def __init__(self):
        super().__init__()
        self.storage = CSVStorage()
        self.events_file = "events.csv"

    def get_all_events(self):
        data = self.storage.load(self.events_file)
        events = []
        for row in data:
            try:
                participants = row['participants'].split(',') if row.get('participants') else []
                event = EventFactory.create_event(
                    name=row['event_name'],
                    description=row['description'],
                    date=row['event_date'],
                    organizer=row['organizer'],
                    participants=participants
                )
                events.append(event)
            except:
                continue
        return events

    def add_event(self, name, description, date, organizer):
        event_data = {
            'event_name': name,
            'description': description,
            'event_date': date,
            'organizer': organizer,
            'participants': ''
        }
        fieldnames = ['event_name', 'description', 'event_date', 'organizer', 'participants']
        result = self.storage.save(self.events_file, fieldnames, event_data)

        if result:
            self.notify({
                "event": "event_created",
                "name": name,
                "organizer": organizer
            })
        return result

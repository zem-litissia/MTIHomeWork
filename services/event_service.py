from model.event import Event
from services.CSVStorage import CSVStorage

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

class EventService:
    def __init__(self):
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

            except Exception as e:
                print(f"Erreur traitement événement: {e}")
                continue
        
        return events

    def add_event(self, name, description, date, organizer):
        try:
            event_data = {
                'event_name': name,
                'description': description,
                'event_date': date,
                'organizer': organizer,
                'participants': ''
            }
            
            fieldnames = ['event_name', 'description', 'event_date', 'organizer', 'participants']
            
            return self.storage.save(self.events_file, fieldnames, event_data)
            
        except Exception as e:
            print(f"Erreur add_event: {e}")
            return False

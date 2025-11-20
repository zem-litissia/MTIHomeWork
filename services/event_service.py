# services/event_service.py
from models.event import Event
from .CSVStorage import CSVStorage

EVENTS_FILE = "data/events.csv"

class EventService:
    @staticmethod
    def get_all_events():
        data = CSVStorage.load(EVENTS_FILE)
        events = []
        for row in data:
            # Utiliser les bons noms de colonnes selon votre CSV
            event_name = row.get('event_name') or row.get('name', '')
            event_date = row.get('event_date') or row.get('date', '')
            participants = row.get('participants', '')
            
            events.append(Event(
                name=event_name,
                description=row.get('description', ''),
                date=event_date,
                organizer=row.get('organizer', ''),
                participants=participants.split(',') if participants else []
            ))
        return events

    @staticmethod
    def add_event(name, description, date, organizer):
        try:
            # Préparer les données
            event_data = {
                'event_name': name,
                'description': description,
                'event_date': date,
                'organizer': organizer,
                'participants': ''
            }
            
            # Définir les noms de colonnes
            fieldnames = ['event_name', 'description', 'event_date', 'organizer', 'participants']
            
            # Sauvegarder
            success = CSVStorage.save(EVENTS_FILE, fieldnames, event_data)
            
            if success:
                print(f"Événement {name} ajouté avec succès!")
            else:
                print(f"Erreur lors de l'ajout de l'événement {name}")
                
            return success
            
        except Exception as e:
            print(f"Erreur dans add_event: {e}")
            return False
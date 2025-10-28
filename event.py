class Event:
    def __init__(self, name, description, date, organizer, participants=None):
        self.name = name
        self.description = description
        self.date = date
        self.organizer = organizer
        # Si une liste de participants est fournie (depuis CSV), on l’utilise
        # Sinon, on crée une liste vide
        self.participants = participants if participants else []

    def add_participant(self, member):
        """Ajoute un participant à la liste (peut être un nom ou un objet Member)."""
        # Si on reçoit un objet Member, on enregistre juste son nom
        if hasattr(member, "full_name"):
            self.participants.append(member.full_name)
        else:
            self.participants.append(str(member))

    def list_participants(self):
        """Retourne la liste des participants."""
        return self.participants

    def display_info(self):
        """Retourne une description lisible de l'événement."""
        return f"{self.name} — {self.date} — Organisé par {self.organizer} ({len(self.participants)} participants)"

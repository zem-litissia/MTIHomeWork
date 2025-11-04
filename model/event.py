# models/event.py
from interface.Organizable import Organizable
from interface.Registrable import  Registrable
class Event(Organizable, Registrable):
    def __init__(self, name, description, date, organizer, participants=None):
        self.name = name
        self.description = description
        self.date = date
        self.organizer = organizer
        self.participants = participants or []

    def schedule(self):
        print(f"Scheduling event: {self.name} on {self.date}")

    def register_member(self, member):
        self.participants.append(member.full_name if hasattr(member, "full_name") else str(member))

    def describe(self):
        return f"{self.name} — {self.date} — Organized by {self.organizer}"


# Classes that extend Event (OCP principle)
class Trip(Event):
    def __init__(self, name, description, date, organizer, destination):
        super().__init__(name, description, date, organizer)
        self.destination = destination

    def describe(self):
        return f"Trip to {self.destination} — {self.date}"

class Meeting(Event):
    def __init__(self, name, description, date, organizer, topic):
        super().__init__(name, description, date, organizer)
        self.topic = topic

    def describe(self):
        return f"Meeting about {self.topic} — {self.date}"

class Competition(Event):
    def __init__(self, name, description, date, organizer, prize):
        super().__init__(name, description, date, organizer)
        self.prize = prize

    def describe(self):
        return f"Competition: {self.name} — Prize: {self.prize}"

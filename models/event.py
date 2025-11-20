# models/event.py

class Event:
    def __init__(self, name, description, date, organizer, participants=None):
        self.name = name
        self.description = description
        self.date = date
        self.organizer = organizer
        self.participants = participants or []

    def register_member(self, member):
        self.participants.append(member)

    def describe(self):
        return f"{self.name} — {self.date} — Organized by {self.organizer}"


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
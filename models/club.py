# models/club.py

class Club:
    def __init__(self, name, leader=None):
        self.name = name
        self.members = []
        self.events = []
        self.trainings = []
        self.subscriptions = []
        self.leader = leader

    def summary(self):
        return {
            "name": self.name,
            "members": len(self.members),
            "events": len(self.events),
            "trainings": len(self.trainings),
            "subscriptions": len(self.subscriptions)
        }
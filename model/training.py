# models/training.py

class TrainingSession:
    def __init__(self, topic, trainer, date):
        self.topic = topic
        self.trainer = trainer
        self.date = date
        self.participants = []

    def add_participant(self, member):
        self.participants.append(member)

    def list_participants(self):
        return [m.full_name for m in self.participants]
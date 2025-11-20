import csv
from .member import Member
from .event import Event
from .training import TrainingSession
from .subscription import Subscription

# club.py
class Club:
    def __init__(self, name):
        self.name = name
        self.member = []
        self.event = []
        self.training = []
        self.subscriptions = []
        self.leader = None


    def summary(self):
        print(f"\ Club: {self.name}")
        print(f" Members: {len(self.member)}")
        print(f" Events: {len(self.event)}")
        print(f" Trainings: {len(self.training)}")
        print(f" Subscriptions: {len(self.subscriptions)}\n")

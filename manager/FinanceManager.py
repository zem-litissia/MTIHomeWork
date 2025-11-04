import csv
from model.event import Event
from model.subscription import Subscription
from model.member import Member
from interface.StorageInterface import StorageInterface
# ---------------- Finance Manager ----------------
class FinanceManager:
    def __init__(self, storage):
        self.storage = storage

    def load_subscriptions(self, filename):
        data = self.storage.load(filename)
        return [
            Subscription(
                member_id=int(row['member_id']),
                amount=row['amount'],
                date=row['date'],
                status=row['status']
            )
            for row in data
        ]

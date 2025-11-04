import csv
from model.event import Event
from model.subscription import Subscription
from model.member import Member
from interface.StorageInterface import StorageInterface
# ---------------- Member Repository ----------------
class MemberRepository:
    def __init__(self, storage):
        self.storage = storage

    def load_members(self, filename):
        data = self.storage.load(filename)
        return [
            Member(
                full_name=row['full_name'],
                email=row['email'],
                phone=row['phone'],
                address=row['address'],
                join_date=row['join_date'],
                skills=row['skills'].split(','),
                interests=row['interests'].split(','),
                subscription_status=row['subscription_status']
            )
            for row in data
        ]
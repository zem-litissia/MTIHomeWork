import csv
from model.event import Event
from model.subscription import Subscription
from model.member import Member
from interface.StorageInterface import StorageInterface
# ---------------- CSV Storage ----------------
class CSVStorage(StorageInterface):
    def load(self, filename):
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

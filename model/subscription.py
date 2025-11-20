# models/subscription.py
from interface.Payable import Payable
class Subscription(Payable):
    def __init__(self, member_id, amount, date, status):
        self.member_id = member_id
        self.amount = float(amount)
        self.date = date
        self.status = status

    def process_payment(self):
        self.status = "Paid"
        print(f"Payment processed for member {self.member_id}")

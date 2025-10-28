class Subscription:
    def __init__(self, member_id, amount, date, status):
        self.member_id = member_id
        self.amount = float(amount)
        self.date = date
        self.status = status

    def mark_as_paid(self):
        self.status = "Paid"

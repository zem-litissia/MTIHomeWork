from services.CSVStorage import CSVStorage
from observer.subject import SubjectMixin
from model.subscription import Subscription

class SubscriptionService(SubjectMixin):
    def __init__(self):
        super().__init__()
        self.storage = CSVStorage()
        self.subscriptions_file = "subscriptions.csv"

    def get_all_subscriptions(self):
        data = self.storage.load(self.subscriptions_file)
        subscriptions = []
        for row in data:
            try:
                subscriptions.append(Subscription(
                    member_id=int(row['member_id']),
                    amount=float(row['amount']),
                    date=row['date'],
                    status=row['status']
                ))
            except:
                continue
        return subscriptions

    def add_subscription(self, member_id, amount, date, status="pending"):
        subscription_data = {
            'member_id': member_id,
            'amount': amount,
            'date': date,
            'status': status
        }
        fieldnames = ['member_id', 'amount', 'date', 'status']
        result = self.storage.save(self.subscriptions_file, fieldnames, subscription_data)

        if result:
            self.notify({
                "event": "subscription_created",
                "member_id": member_id,
                "amount": amount
            })
        return result

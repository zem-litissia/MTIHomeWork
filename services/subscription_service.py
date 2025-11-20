# services/subscription_service.py
from model.subscription import Subscription
from services.CSVStorage import CSVStorage

class SubscriptionService:
    def __init__(self):
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
            except Exception as e:
                print(f"Erreur traitement abonnement: {e}")
                continue
        
        return subscriptions

    def add_subscription(self, member_id, amount, date, status="pending"):
        try:
            subscription_data = {
                'member_id': member_id,
                'amount': amount,
                'date': date,
                'status': status
            }
            
            fieldnames = ['member_id', 'amount', 'date', 'status']
            
            return self.storage.save(self.subscriptions_file, fieldnames, subscription_data)
            
        except Exception as e:
            print(f"Erreur add_subscription: {e}")
            return False
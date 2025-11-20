# services/subscription_service.py
from models.subscription import Subscription
from .CSVStorage import CSVStorage

SUBSCRIPTIONS_FILE = "data/subscriptions.csv"

class SubscriptionService:
    @staticmethod
    def get_all_subscriptions():
        data = CSVStorage.load(SUBSCRIPTIONS_FILE)
        subscriptions = []
        for row in data:
            subscriptions.append(Subscription(
                member_id=int(row['member_id']),
                amount=float(row['amount']),
                date=row['date'],
                status=row['status']
            ))
        return subscriptions

    @staticmethod
    def add_subscription(member_id, amount, date, status="pending"):
        try:
            # Préparer les données
            subscription_data = {
                'member_id': member_id,
                'amount': amount,
                'date': date,
                'status': status
            }
            
            # Définir les noms de colonnes
            fieldnames = ['member_id', 'amount', 'date', 'status']
            
            # Sauvegarder
            success = CSVStorage.save(SUBSCRIPTIONS_FILE, fieldnames, subscription_data)
            
            if success:
                print(f"Abonnement pour le membre {member_id} ajouté avec succès!")
            else:
                print(f"Erreur lors de l'ajout de l'abonnement pour le membre {member_id}")
                
            return success
            
        except Exception as e:
            print(f"Erreur dans add_subscription: {e}")
            return False
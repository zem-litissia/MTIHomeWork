from services.member_service import MemberService
from services.event_service import EventService
from services.subscription_service import SubscriptionService
from observer.email_notifier import EmailNotifier

class ClubFacade:
    def __init__(self):
        self.member_service = MemberService()
        self.event_service = EventService()
        self.subscription_service = SubscriptionService()

        
        email_notifier = EmailNotifier()
        self.member_service.attach(email_notifier)
        self.event_service.attach(email_notifier)
        self.subscription_service.attach(email_notifier)

  
    def register_member(self, **kwargs):
        return self.member_service.add_member(**kwargs)

    def get_members(self):
        return self.member_service.get_all_members()

    # Event methods
    def create_event(self, **kwargs):
        return self.event_service.add_event(**kwargs)

    def get_events(self):
        return self.event_service.get_all_events()

    # Subscription methods
    def add_subscription(self, **kwargs):
        return self.subscription_service.add_subscription(**kwargs)

    def get_subscriptions(self):
        return self.subscription_service.get_all_subscriptions()

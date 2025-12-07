from services.event_service import EventService
from services.member_service import MemberService
from services.subscription_service import SubscriptionService

class ClubFacade:
    def __init__(self):
        self.event_service = EventService()
        self.member_service = MemberService()
        self.subscription_service = SubscriptionService()

    def create_event(self, name, description, date, organizer):
        return self.event_service.add_event(name, description, date, organizer)

    def register_member(self, full_name, email, phone, address, join_date, skills, interests, subscription_status):
        return self.member_service.add_member(
            full_name, email, phone, address, join_date, skills, interests, subscription_status
        )

    def add_subscription(self, member_id, amount, date, status="pending"):
        return self.subscription_service.add_subscription(member_id, amount, date, status)

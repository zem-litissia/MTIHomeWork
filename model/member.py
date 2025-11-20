# models/member.py

class Member:
    def __init__(self, full_name, email, phone, address, join_date, skills, interests, subscription_status, member_id=None):
        self.id = member_id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.skills = skills if skills else []
        self.interests = interests if interests else []
        self.subscription_status = subscription_status
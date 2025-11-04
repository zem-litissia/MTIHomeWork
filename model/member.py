# models/member.py
class Member:
    def __init__(self, full_name, email, phone, address, join_date, skills, interests, subscription_status):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.skills = skills
        self.interests = interests
        self.subscription_status = subscription_status

    def display_info(self):
        return f"{self.full_name} | {self.email} | Skills: {', '.join(self.skills)} | Status: {self.subscription_status}"

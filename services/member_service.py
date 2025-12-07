from services.CSVStorage import CSVStorage
from observer.subject import SubjectMixin
from model.member import Member

class MemberService(SubjectMixin):
    def __init__(self):
        super().__init__()
        self.storage = CSVStorage()
        self.members_file = "members.csv"

    def get_all_members(self):
        data = self.storage.load(self.members_file)
        members = []
        for row in data:
            try:
                members.append(Member(
                    full_name=row['full_name'],
                    email=row['email'],
                    phone=row['phone'],
                    address=row['address'],
                    join_date=row['join_date'],
                    skills=row['skills'].split(',') if row.get('skills') else [],
                    interests=row['interests'].split(',') if row.get('interests') else [],
                    subscription_status=row.get('subscription_status', 'pending'),
                    member_id=int(row['student_id'])
                ))
            except:
                continue
        return members

    def add_member(self, full_name, email, phone, address, join_date, skills, interests, subscription_status):
        members = self.get_all_members()
        new_id = max([m.id for m in members]) + 1 if members else 1

        member_data = {
            'student_id': new_id,
            'full_name': full_name,
            'email': email,
            'phone': phone,
            'address': address,
            'join_date': join_date,
            'subscription_status': subscription_status,
            'skills': ','.join(skills),
            'interests': ','.join(interests)
        }
        fieldnames = ['student_id', 'full_name', 'email', 'phone', 'address', 'join_date', 'subscription_status', 'skills', 'interests']
        result = self.storage.save(self.members_file, fieldnames, member_data)

        if result:
            self.notify({
                "event": "member_created",
                "full_name": full_name,
                "email": email
            })
        return result

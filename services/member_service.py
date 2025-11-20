# services/member_service.py
from model.member import Member
from services.CSVStorage import CSVStorage

class MemberService:
    def __init__(self):
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
            except Exception as e:
                print(f"Erreur traitement membre: {e}")
                continue
        
        return members

    def add_member(self, full_name, email, phone, address, join_date, skills, interests, subscription_status):
        try:
            # Générer un nouvel ID
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
            
            return self.storage.save(self.members_file, fieldnames, member_data)
            
        except Exception as e:
            print(f"Erreur add_member: {e}")
            return False
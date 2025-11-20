# services/member_service.py
from models.member import Member
from .CSVStorage import CSVStorage

MEMBERS_FILE = "data/members.csv"

class MemberService:
    @staticmethod
    def get_all_members():
        data = CSVStorage.load(MEMBERS_FILE)
        members = []
        for row in data:
            # Gérer les cas où certaines colonnes pourraient manquer
            skills = row.get('skills', '')
            interests = row.get('interests', '')
            
            members.append(Member(
                full_name=row['full_name'],
                email=row['email'],
                phone=row['phone'],
                address=row['address'],
                join_date=row['join_date'],
                skills=skills.split(',') if skills else [],
                interests=interests.split(',') if interests else [],
                subscription_status=row.get('subscription_status', 'pending'),
                member_id=int(row['student_id'])
            ))
        return members

    @staticmethod
    def add_member(full_name, email, phone, address, join_date, skills, interests, subscription_status):
        try:
            # Générer un nouvel ID
            members = MemberService.get_all_members()
            existing_ids = [m.id for m in members]
            new_id = max(existing_ids) + 1 if existing_ids else 1
            
            # Préparer les données
            member_data = {
                'student_id': new_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'address': address,
                'join_date': join_date,
                'subscription_status': subscription_status,
                'skills': ','.join([s.strip() for s in skills]) if skills else '',
                'interests': ','.join([i.strip() for i in interests]) if interests else ''
            }
            
            # Définir les noms de colonnes
            fieldnames = ['student_id', 'full_name', 'email', 'phone', 'address', 'join_date', 'subscription_status', 'skills', 'interests']
            
            # Sauvegarder
            success = CSVStorage.save(MEMBERS_FILE, fieldnames, member_data)
            
            if success:
                print(f"Membre {full_name} ajouté avec succès!")
            else:
                print(f"Erreur lors de l'ajout du membre {full_name}")
                
            return success
            
        except Exception as e:
            print(f"Erreur dans add_member: {e}")
            return False

    @staticmethod
    def get_next_member_id():
        """Obtenir le prochain ID disponible"""
        members = MemberService.get_all_members()
        if not members:
            return 1
        return max(member.id for member in members) + 1
import csv
from member import Member
from event import Event
from training import TrainingSession
from subscription import Subscription

class Club:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.events = []
        self.trainings = []
        self.subscriptions = []
        self.leader = None

    def load_members(self, filename):
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                member = Member(
                    full_name=row['full_name'],
                    email=row['email'],
                    phone=row['phone'],
                    address=row['address'],
                    join_date=row['join_date'],
                    skills=row['skills'].split(',') if row['skills'] else [],
                    interests=row['interests'].split(',') if row['interests'] else [],
                    subscription_status=row['subscription_status']
                )
                self.members.append(member)

    def load_events(self, filename):
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.events.append(
                    Event(
                        name=row['event_name'],
                        description=row['description'],
                        date=row['event_date'],
                        organizer=row['organizer'],
                        participants=row['participants'].split(',') if row['participants'] else []
                    )
                )

    def load_subscriptions(self, filename):
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.subscriptions.append(
                    Subscription(
                        member_id=int(row['member_id']),
                        amount=row['amount'],
                        date=row['date'],
                        status=row['status']
                    )
                )

    def summary(self):
        print(f"Scientific Club: {self.name}")
        print(f"Leader: {self.leader.full_name if self.leader else 'Not assigned'}")
        print(f"Members: {len(self.members)} | Events: {len(self.events)} | Trainings: {len(self.trainings)} | Subscriptions: {len(self.subscriptions)}")

    def generate_html(self, filename="club_dashboard.html"):
        """Generate an HTML dashboard with all club information (no separation between paid/pending)."""

        html = ["<html><head><meta charset='utf-8'><style>",
                "body { font-family: Arial, sans-serif; margin: 30px; }",
                "h1, h2 { color: #2c3e50; }",
                "table { border-collapse: collapse; width: 90%; margin-bottom: 40px; }",
                "th, td { border: 1px solid #999; padding: 8px; text-align: left; }",
                "th { background-color: #f2f2f2; }",
                "</style></head><body>"]

        html.append(f"<h1>{self.name} — Dashboard</h1>")

        # --- Table 1 : Members ---
        html.append("<h2>👥 Members</h2>")
        html.append("<table><tr><th>Full Name</th><th>Email</th><th>Phone</th><th>Address</th><th>Skills</th><th>Interests</th><th>Status</th></tr>")
        for m in self.members:
            html.append(f"<tr><td>{m.full_name}</td><td>{m.email}</td><td>{m.phone}</td>"
                        f"<td>{m.address}</td><td>{', '.join(m.skills)}</td>"
                        f"<td>{', '.join(m.interests)}</td><td>{m.subscription_status}</td></tr>")
        html.append("</table>")

        # --- Table 2 : Events ---
        html.append("<h2>📅 Events</h2>")
        html.append("<table><tr><th>Event Name</th><th>Description</th><th>Date</th><th>Organizer</th><th>Participants</th></tr>")
        for e in self.events:
            html.append(f"<tr><td>{e.name}</td><td>{e.description}</td>"
                        f"<td>{e.date}</td><td>{e.organizer}</td>"
                        f"<td>{', '.join(e.participants)}</td></tr>")
        html.append("</table>")

        # --- Table 3 : Subscriptions ---
        html.append("<h2>💰 Subscriptions</h2>")
        html.append("<table><tr><th>Member ID</th><th>Amount</th><th>Date</th><th>Status</th></tr>")
        for s in self.subscriptions:
            html.append(f"<tr><td>{s.member_id}</td><td>{s.amount}</td>"
                        f"<td>{s.date}</td><td>{s.status}</td></tr>")
        html.append("</table>")

        html.append("</body></html>")

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(html))
        print(f"✅ Dashboard generated: {filename}")

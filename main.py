# main.py
import csv
from model.club import Club
from model.training import TrainingSession
from manager.CSVStorage import CSVStorage
from manager.MemberRepository import MemberRepository
from manager.EventManager import EventManager
from manager.FinanceManager import FinanceManager
from manager.HTMLGenerator import HTMLGenerator
# Create storage
storage = CSVStorage()

# Load data using the managers
member_repo = MemberRepository(storage)
members = member_repo.load_members("data/members.csv")

event_manager = EventManager(storage)
events = event_manager.load_events("data/events.csv")

finance_manager = FinanceManager(storage)
subscriptions = finance_manager.load_subscriptions("data/subscriptions.csv")

# Generate HTML dashboard
html_gen = HTMLGenerator(
    name="Scientific Club",
    members=members,
    events=events,
    subscriptions=subscriptions
)

html_gen.generate_html("outp/club_dashboard.html")

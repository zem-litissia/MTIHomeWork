from flask import Flask, render_template, request, jsonify, redirect, url_for
from controllers.member_controller import MemberController
from controllers.event_controller import EventController
from controllers.subscription_controller import SubscriptionController
from services.CSVStorage import CSVStorage
from services.MemberRepository import MemberRepository
from services.EventManager import EventManager
from services.FinanceManager import FinanceManager
import os

app = Flask(__name__)

# Initialize services
storage = CSVStorage()
member_repo = MemberRepository(storage)
event_manager = EventManager(storage)
finance_manager = FinanceManager(storage)

# Initialize controllers
member_controller = MemberController(member_repo)
event_controller = EventController(event_manager)
subscription_controller = SubscriptionController(finance_manager)

@app.route('/')
def dashboard():
    members = member_controller.get_all_members()
    events = event_controller.get_all_events()
    subscriptions = subscription_controller.get_all_subscriptions()
    
    # Calculate statistics
    total_members = len(members)
    paid_members = len([m for m in members if m.subscription_status == 'paid'])
    total_events = len(events)
    total_revenue = sum(s.amount for s in subscriptions if s.status == 'paid')
    
    return render_template('dashboard.html',
                         members=members,
                         events=events,
                         subscriptions=subscriptions,
                         total_members=total_members,
                         paid_members=paid_members,
                         total_events=total_events,
                         total_revenue=total_revenue)

@app.route('/members')
def members():
    members_list = member_controller.get_all_members()
    return render_template('members.html', members=members_list)

@app.route('/events')
def events():
    events_list = event_controller.get_all_events()
    return render_template('events.html', events=events_list)

@app.route('/subscriptions')
def subscriptions():
    subscriptions_list = subscription_controller.get_all_subscriptions()
    members_list = member_controller.get_all_members()
    
    # Combine subscription data with member names
    subscription_data = []
    for sub in subscriptions_list:
        member = next((m for m in members_list if hasattr(m, 'student_id') and m.student_id == sub.member_id), None)
        member_name = member.full_name if member else f"Member {sub.member_id}"
        subscription_data.append({
            'subscription': sub,
            'member_name': member_name
        })
    
    return render_template('subscriptions.html', 
                         subscriptions=subscription_data,
                         total_subscriptions=len(subscriptions_list))

@app.route('/api/members/<int:member_id>/update_status', methods=['POST'])
def update_member_status(member_id):
    new_status = request.json.get('status')
    if member_controller.update_member_status(member_id, new_status):
        return jsonify({'success': True, 'message': 'Status updated successfully'})
    return jsonify({'success': False, 'message': 'Member not found'})

@app.route('/api/subscriptions/<int:member_id>/process_payment', methods=['POST'])
def process_payment(member_id):
    if subscription_controller.process_payment(member_id):
        return jsonify({'success': True, 'message': 'Payment processed successfully'})
    return jsonify({'success': False, 'message': 'Subscription not found'})

if __name__ == '__main__':
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    app.run(debug=True)
<<<<<<< HEAD
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from services.member_service import MemberService
from services.event_service import EventService
from services.subscription_service import SubscriptionService
import os
import datetime

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete_ici'  # Pour les messages flash

# ==========================
# Dashboard
# ==========================
@app.route('/')
def dashboard():
    try:
        members = MemberService.get_all_members()
        events = EventService.get_all_events()
        subscriptions = SubscriptionService.get_all_subscriptions()
        
        total_members = len(members)
        total_events = len(events)
        total_subscriptions = len([s for s in subscriptions if s.status.lower() == 'paid'])
        
        return render_template(
            'dashboard.html',
            total_members=total_members,
            total_events=total_events,
            total_subscriptions=total_subscriptions
        )
    except Exception as e:
        flash(f"Erreur lors du chargement du dashboard: {str(e)}", "error")
        return render_template('dashboard.html', total_members=0, total_events=0, total_subscriptions=0)

# ==========================
# Members
# ==========================
@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'POST':
        try:
            full_name = request.form['full_name']
            email = request.form['email']
            phone = request.form['phone']
            address = request.form['address']
            join_date = request.form['join_date']
            skills = request.form['skills'].split(',') if request.form['skills'] else []
            interests = request.form['interests'].split(',') if request.form['interests'] else []
            subscription_status = request.form.get('subscription_status', 'pending')

            success = MemberService.add_member(
                full_name, email, phone, address, join_date, skills, interests, subscription_status
            )
            
            if success:
                flash(f"Membre {full_name} ajouté avec succès!", "success")
            else:
                flash(f"Erreur lors de l'ajout du membre {full_name}", "error")
                
        except Exception as e:
            flash(f"Erreur: {str(e)}", "error")
        
        return redirect('/members')

    try:
        members_list = MemberService.get_all_members()
        return render_template('members.html', members=members_list)
    except Exception as e:
        flash(f"Erreur lors du chargement des membres: {str(e)}", "error")
        return render_template('members.html', members=[])

# ==========================
# Events
# ==========================
@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form.get('description', '')
            date = request.form['date']
            organizer = request.form.get('organizer', '')

            success = EventService.add_event(name, description, date, organizer)
            
            if success:
                flash(f"Événement {name} ajouté avec succès!", "success")
            else:
                flash(f"Erreur lors de l'ajout de l'événement {name}", "error")
                
        except Exception as e:
            flash(f"Erreur: {str(e)}", "error")
        
        return redirect('/events')

    try:
        events_list = EventService.get_all_events()
        return render_template('events.html', events=events_list)
    except Exception as e:
        flash(f"Erreur lors du chargement des événements: {str(e)}", "error")
        return render_template('events.html', events=[])

# ==========================
# Subscriptions
# ==========================
@app.route('/subscriptions', methods=['GET', 'POST'])
def subscriptions():
    if request.method == 'POST':
        try:
            member_name = request.form['member']
            amount = float(request.form.get('amount', 0))
            status = request.form.get('status', 'pending')
            
            members = MemberService.get_all_members()
            member = next((m for m in members if m.full_name == member_name), None)
            
            if member:
                date = datetime.datetime.now().strftime("%Y-%m-%d")
                success = SubscriptionService.add_subscription(member.id, amount, date, status)
                
                if success:
                    flash(f"Abonnement pour {member_name} ajouté avec succès!", "success")
                else:
                    flash(f"Erreur lors de l'ajout de l'abonnement pour {member_name}", "error")
            else:
                flash(f"Membre {member_name} non trouvé!", "error")
                
        except Exception as e:
            flash(f"Erreur: {str(e)}", "error")
        
        return redirect('/subscriptions')

    try:
        subscriptions_list = SubscriptionService.get_all_subscriptions()
        members_list = MemberService.get_all_members()
        
        subscription_data = []
        for sub in subscriptions_list:
            member = next((m for m in members_list if m.id == sub.member_id), None)
            member_name = member.full_name if member else f'Membre {sub.member_id}'
            subscription_data.append({
                'subscription': sub,
                'member_name': member_name
            })
        
        return render_template('subscriptions.html', subscriptions=subscription_data, members=members_list)
    except Exception as e:
        flash(f"Erreur lors du chargement des abonnements: {str(e)}", "error")
        return render_template('subscriptions.html', subscriptions=[], members=[])

# ==========================
# Run Flask
# ==========================
if __name__ == '__main__':
    # Créer le dossier data s'il n'existe pas
    os.makedirs('data', exist_ok=True)
    app.run()
=======
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
>>>>>>> 441c8e0b1a2062db3b3825af7fced7bf66446367

from flask import Blueprint, render_template, request, redirect, url_for
from ..services.ClubFacade import ClubFacade

bp = Blueprint('members', __name__, url_prefix='/members')
facade = ClubFacade()

@bp.route('/')
def list_members():
    members = facade.member_service.get_all_members()
    return render_template('members.html', members=members)

@bp.route('/add', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        join_date = request.form['join_date']

        skills = request.form['skills'].split(',')
        interests = request.form['interests'].split(',')

        subscription_status = request.form.get('subscription_status', 'pending')

        facade.register_member(
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            join_date=join_date,
            skills=skills,
            interests=interests,
            subscription_status=subscription_status
        )

        return redirect(url_for('members.list_members'))

    return render_template('add_member.html')

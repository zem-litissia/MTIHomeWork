from flask import Blueprint, render_template, request, redirect, url_for
from ..services.ClubFacade import ClubFacade

bp = Blueprint('finance', __name__, url_prefix='/finance')
facade = ClubFacade()

@bp.route('/')
def list_subscriptions():
    subscriptions = facade.subscription_service.get_all_subscriptions()
    return render_template('subscriptions.html', subscriptions=subscriptions)

@bp.route('/add', methods=['GET', 'POST'])
def add_subscription():
    if request.method == 'POST':
        member_id = request.form['member_id']
        amount = float(request.form['amount'])
        date = request.form['date']
        status = request.form.get('status', "pending")

        facade.add_subscription(
            member_id=member_id,
            amount=amount,
            date=date,
            status=status
        )

        return redirect(url_for('finance.list_subscriptions'))

    return render_template('add_subscription.html')

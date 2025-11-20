from flask import Blueprint, render_template, request, redirect, url_for
from ..models.subscription import Subscription
from ..storage.csv_storage import CSVStorage

bp = Blueprint('finance', __name__, url_prefix='/finance')

@bp.route('/')
def list_subscriptions():
    subscriptions = CSVStorage.load_subscriptions()
    return render_template('subscriptions.html', subscriptions=subscriptions)

@bp.route('/add', methods=['GET', 'POST'])
def add_subscription():
    if request.method == 'POST':
        member_id = request.form['member_id']
        amount = float(request.form['amount'])
        date = request.form['date']
        type_ = request.form['type']
        subscription = Subscription(member_id=member_id, amount=amount, date=date, type_=type_)
        CSVStorage.save_subscription(subscription)
        return redirect(url_for('finance.list_subscriptions'))
    return render_template('add_subscription.html')

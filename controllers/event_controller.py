from flask import Blueprint, render_template, request, redirect, url_for
from ..models.event import Event
from ..storage.csv_storage import CSVStorage

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/')
def list_events():
    events = CSVStorage.load_events()
    return render_template('events.html', events=events)

@bp.route('/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        name = request.form['name']
        type_ = request.form['type']
        date = request.form['date']
        event = Event(name=name, type_=type_, date=date)
        CSVStorage.save_event(event)
        return redirect(url_for('events.list_events'))
    return render_template('add_event.html')


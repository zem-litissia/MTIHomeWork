from flask import Blueprint, render_template, request, redirect, url_for
from ..services.ClubFacade import ClubFacade

bp = Blueprint('events', __name__, url_prefix='/events')
facade = ClubFacade()

@bp.route('/')
def list_events():
    events = facade.event_service.get_all_events()
    return render_template('events.html', events=events)

@bp.route('/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        date = request.form['date']
        organizer = request.form['organizer']

        facade.create_event(
            name=name,
            description=description,
            date=date,
            organizer=organizer
        )

        return redirect(url_for('events.list_events'))

    return render_template('add_event.html')

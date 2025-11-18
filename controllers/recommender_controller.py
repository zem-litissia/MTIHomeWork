from flask import Blueprint, render_template
from ..storage.csv_storage import CSVStorage

bp = Blueprint('recommender', __name__, url_prefix='/recommend')

@bp.route('/')
def recommend():
    members = CSVStorage.load_members()
    events = CSVStorage.load_events()
    recommendations = []

    for member in members:
        suitable_events = [e for e in events if set(member.skills) & set(getattr(e, 'skills_required', []))]
        recommendations.append((member.name, suitable_events))

    return render_template('recommendations.html', recommendations=recommendations)

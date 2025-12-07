from flask import Blueprint, render_template
from ..services.ClubFacade import ClubFacade

bp = Blueprint('recommender', __name__, url_prefix='/recommend')
facade = ClubFacade()

@bp.route('/')
def recommend():
    recommendations = facade.recommender_service.recommend()
    return render_template('recommendations.html', recommendations=recommendations)

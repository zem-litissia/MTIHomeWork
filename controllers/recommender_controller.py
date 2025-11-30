from flask import Blueprint, render_template
from ..services.recommender_service import RecommenderService

bp = Blueprint('recommender', __name__, url_prefix='/recommend')

@bp.route('/')
def recommend():
    recommendations = RecommenderService.recommend()
    return render_template('recommendations.html', recommendations=recommendations)

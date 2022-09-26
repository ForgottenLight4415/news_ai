from flask import Blueprint
from .extensions import newsapi

api = Blueprint('api', __name__)

@api.route('/')
def api_index():
    return "<p>API endpoint</p>"

@api.route('/top-headlines')
def get_headlines():
    return newsapi.top_headlines(endpoint="api")

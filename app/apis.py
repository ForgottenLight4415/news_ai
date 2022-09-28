from collections import OrderedDict
from flask import Blueprint, request
from .extensions import newsapi

api = Blueprint('api', __name__)

@api.route('/')
def api_index():
    return "<p>API endpoint</p>"

@api.route('/top-headlines')
def get_headlines():
    args = request.args
    category = args.get("category")
    language = args.get("language")
    country = args.get("country")
    return newsapi.top_headlines(category=category, language=language, country=country, endpoint="api")

@api.route('/get-categories')
def get_categories():
    categories = OrderedDict()
    categories['categories'] = [
        'business',
        'entertainment',
        'general',
        'health'
        'science',
        'sports',
        'technology'
    ]

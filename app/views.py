from flask import Blueprint, render_template, request
from .extensions import newsapi

main = Blueprint('main', __name__)

@main.route('/')
def main_index():
    args = request.args
    category = args.get("category") 
    language = args.get("language") or "en"
    country = args.get("country")
    return render_template('index.html', headlines=newsapi.top_headlines(category=category, language=language, country=country))
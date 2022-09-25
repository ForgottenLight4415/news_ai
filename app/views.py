from flask import Blueprint, render_template
from .extensions import newsapi

main = Blueprint('main', __name__)

@main.route('/')
def main_index():
    return render_template('index.html', headlines=newsapi.top_headlines())
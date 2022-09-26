from flask_sqlalchemy import SQLAlchemy
from app.api.v1.controllers import news_api_controller

db = SQLAlchemy()

newsapi = news_api_controller.NewsApiContentProvider()
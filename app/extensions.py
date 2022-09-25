from flask_sqlalchemy import SQLAlchemy
from app.api.v1.controllers import news_api

db = SQLAlchemy()

newsapi = news_api.NewsApiContentProvider()
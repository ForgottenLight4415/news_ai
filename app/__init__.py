from flask import Flask

from .extensions import db
from .views import main

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/news_ai'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    with app.app_context():
        from .models import User
        db.create_all()
    
    app.register_blueprint(main)
    return app

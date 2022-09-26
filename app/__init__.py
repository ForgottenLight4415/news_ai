import pathlib
from flask import Flask
from dotenv import dotenv_values

from .extensions import db, newsapi
from .views import main
from .apis import api

def create_app():
    app = Flask(__name__)

    secret_env_path = str(pathlib.Path().resolve()) + "\\app\\.env"
    public_env_path = str(pathlib.Path().resolve()) + "\\app\\.flaskenv"
    config = dotenv_values(secret_env_path)
    config.update(dotenv_values(public_env_path))
    
    app.config['SQLALCHEMY_DATABASE_URI'] = config["SQLALCHEMY_DATABASE_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config["SQLALCHEMY_TRACK_MODIFICATIONS"]

    db.init_app(app)
    newsapi.init_client(config['NEWS_API_KEY'])
    
    with app.app_context():
        from .models import User
        db.create_all()
    
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')
    return app

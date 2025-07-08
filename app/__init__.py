from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)

    from app.routes import routes_bp
    from app.auth import auth_bp

    app.register_blueprint(routes_bp)
    app.register_blueprint(auth_bp)

    return app

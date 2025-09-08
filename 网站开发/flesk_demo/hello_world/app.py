import flask
from sqlalchemy.testing import db

from routes import main
from config import Config


def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(
        main.main_bp
    )
    with app.app_context():
        db.create_all()
    return app


if __name__ == '__main__':
    create_app().run()

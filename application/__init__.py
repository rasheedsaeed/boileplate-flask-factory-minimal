from flask import Flask

def create_app():
    """Initialize core application."""
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    with app.app_context():
        # do stuff here
        return app 

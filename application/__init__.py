from flask import Flask

def create_app():
    """Initialize core application."""
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    with app.app_context():
        # Import blueprints
        from .apps.JSP101 import routes as jsp_routes

        # Register blueprints
        app.register_blueprint(jsp_routes.jsp_bp)

        return app
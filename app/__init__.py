# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import views
    from .views import app as views
    app.register_blueprint(views)

    return app

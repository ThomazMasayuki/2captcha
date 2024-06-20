from flask import Flask
from routes.twocaptcha_routes import add_routes

def create_app():
    app = Flask(__name__)
    add_routes(app)
    return app
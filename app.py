from flask import Flask
from flask_cors import CORS

from routes import register_endpoints
from settings import app_config


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(app_config)
    register_endpoints(app)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')


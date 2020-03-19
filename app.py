from flask import Flask

from api.api_client import ApiClient
from routes import register_endpoints
from settings import Config

api_client = ApiClient()
api_client.get_traffic_status()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_endpoints(app)
    return app


app = create_app()

if __name__ == '__main__':
    app.run()


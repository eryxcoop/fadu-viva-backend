from endpoints.test.routes import test


def register_endpoints(app):
    app.register_blueprint(test, url_prefix='/api/')

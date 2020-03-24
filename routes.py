from endpoints.routes.routes import routes


def register_endpoints(app):
    app.register_blueprint(routes, url_prefix='/api/')

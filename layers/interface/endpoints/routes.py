from layers.interface.endpoints import routes
from layers.interface.endpoints.controllers import GetStatus, UpdateTrafficStatus, UpdateBusesGPS

routes.add_url_rule('get-status', view_func=GetStatus.as_view('get-status'))
routes.add_url_rule('update-traffic-status', view_func=UpdateTrafficStatus.as_view('update-traffic-status'))
routes.add_url_rule('update-buses-gps', view_func=UpdateBusesGPS.as_view('update-buses-gps'))

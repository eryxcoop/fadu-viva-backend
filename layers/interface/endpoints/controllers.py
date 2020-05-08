import json

from flask.views import MethodView

from layers.domain.place.places import FADU, AV_LUGONES
from layers.interface.services.services_provider import ServicesProvider
from layers.interface.status_response_presenter import StatusResponsePresenter


class APIController(MethodView):
    pass


class GetStatus(APIController):
    def get(self):
        services_provider = ServicesProvider()
        daylight_brightness = services_provider.get_daylight_brightness()
        traffic_status = services_provider.get_traffic_status_of(AV_LUGONES)
        arriving_buses, departing_buses = services_provider.get_arriving_and_departing_buses_to(FADU)

        status_response_presenter = StatusResponsePresenter(traffic_status=traffic_status,
                                                            arriving_buses=arriving_buses,
                                                            departing_buses=departing_buses,
                                                            daylight_brightness=daylight_brightness)

        response = {
            'object': status_response_presenter.present(),
            'errors': []
        }
        return json.dumps(response)


class UpdateTrafficStatus(APIController):
    def get(self):
        services_provider = ServicesProvider()
        services_provider.update_traffic_status_of(place=AV_LUGONES, expiration=60)
        return 'OK'  # fixme


class UpdateBusesGPS(APIController):
    def get(self):
        services_provider = ServicesProvider()
        services_provider.update_arriving_and_departing_buses_to(place=FADU, expiration=60)
        return 'OK'  # fixme

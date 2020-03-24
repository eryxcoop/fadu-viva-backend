import json

from api.api_client import ApiClient
from layers.domain.places import FADU
from layers.domain.traffic_configuration.traffic_configuration import TrafficConfiguration
from . import routes


@routes.route('traffic-status', methods=['GET'])
def get_traffic_status():
    api_client = ApiClient()
    fadu_traffic_configuration = TrafficConfiguration(
        latitude=FADU["latitude"],
        longitude=FADU["longitude"],
        radius=FADU["radius"]
    )

    traffic_response = api_client.get_traffic_status(fadu_traffic_configuration)
    return json.dumps({
        'object': {
            'status': traffic_response.get_status_for(
                main_street=FADU["main_street"],
                first_crossing_street=FADU["first_crossing_street"],
                second_crossing_street=FADU["second_crossing_street"]
            )
        },
        'errors': []
    })

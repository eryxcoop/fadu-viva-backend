import json

from layers.domain.places import FADU
from layers.domain.traffic_configuration.traffic_configuration import TrafficConfiguration
from layers.interface.endpoints import routes
from layers.interface.services.requesters.cache_requester import RequesterUpdatingCachedResults, \
    RequesterUsingCachedResults
from layers.interface.services.traffic_status.api_client import TrafficStatusApiClient
from layers.interface.status_response_presenter import StatusResponsePresenter


@routes.route('get-status', methods=['GET'])
def get_status():
    traffic_status_api_client = TrafficStatusApiClient(requester=RequesterUsingCachedResults(expiration=30))
    fadu_traffic_configuration = TrafficConfiguration(
        latitude=FADU["latitude"],
        longitude=FADU["longitude"],
        radius=FADU["radius"]
    )

    traffic_response = traffic_status_api_client.get_traffic_status(fadu_traffic_configuration)
    status_response_presenter = StatusResponsePresenter(
        traffic_status=traffic_response.get_status_for(
            main_street=FADU["main_street"],
            first_crossing_street=FADU["first_crossing_street"],
            second_crossing_street=FADU["second_crossing_street"]
        )
    )
    response = {
        'object': status_response_presenter.present(),
        'errors': []
    }
    return json.dumps(response)


@routes.route('update-traffic-status-cached-result', methods=['GET'])
def update_traffic_status_cached_result():
    traffic_status_api_client = TrafficStatusApiClient(requester=RequesterUpdatingCachedResults(expiration=30))
    fadu_traffic_configuration = TrafficConfiguration(
        latitude=FADU["latitude"],
        longitude=FADU["longitude"],
        radius=FADU["radius"]
    )

    traffic_status_api_client.get_traffic_status(fadu_traffic_configuration)
    return 'OK'  # fixme

from layers.interface.services.traffic_status.responses.get_traffic_status_successful_response import \
    GetTrafficStatusSuccessfulResponse
from settings import app_config


class TrafficStatusApiClient:
    TRAFFIC_API_BASE_URL = 'https://traffic.ls.hereapi.com/traffic/6.2/flow.json'
    WEATHER_API_BASE_URL = 'api.openweathermap.org/data/2.5/weather'

    def __init__(self, requester):
        self._requester = requester

    def get_traffic_status(self, traffic_configuration):
        latitude = traffic_configuration.latitude()
        longitude = traffic_configuration.longitude()
        radius = traffic_configuration.radius()

        query_params = {
            'apiKey': app_config.HERE_API_KEY,
            'prox': f'{latitude},{longitude},{radius}'
        }

        json_response = self._requester.call(self.TRAFFIC_API_BASE_URL, query_params)
        traffic_status_response = GetTrafficStatusSuccessfulResponse(json_response)
        return traffic_status_response

    def get_todays_weather(self):
        pass

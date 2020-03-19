from api.requesters.base import Requester
from api.responses.get_traffic_status_successful import GetTrafficStatusSuccessful


class ApiClient:
    TRAFFIC_API_BASE_URL = 'https://traffic.ls.hereapi.com/traffic/6.2/flow.json'
    WEATHER_API_BASE_URL = 'api.openweathermap.org/data/2.5/weather'

    def __init__(self):
        self._requester = Requester()

    def get_traffic_status(self):
        fadu_latitude = '-34.543535'
        fadu_longitude = '-58.446340'
        zoom = '200'

        query_params = {
            'apiKey': "DRHQ1rruBXNyjozHG71CBFCvQXDYlz9h0BAVItNUTu0",
            'prox': "{},{},{}".format(fadu_latitude, fadu_longitude, zoom)
        }

        json_response = self._requester.call(self.TRAFFIC_API_BASE_URL, query_params)
        traffic_status_response = GetTrafficStatusSuccessful(json_response)
        print(traffic_status_response.get_status_for(main_street="Avenida Int Cantilo",
                                                     first_crossing_street="Avenida Int Güiraldes",
                                                     second_crossing_street="Avenida G Udaondo"))

    def get_todays_weather(self):
        pass

from layers.interface.services.buses_gps.responses.get_buses_gps_successful_response import \
    BusesGPSSuccessfulResponse
from settings import app_config


class BusesGPSApiClient:
    API_BASE_URL = 'https://apitransporte.buenosaires.gob.ar/colectivos/vehiclePositionsSimple'

    def __init__(self, requester):
        self._requester = requester

    def get_buses_live_position(self):
        query_params = {
            'client_id': app_config.BSAS_TRANSPORT_API_CLIENT_ID,
            'client_secret': app_config.BSAS_TRANSPORT_API_SECRET,
        }

        json_response = self._requester.call(self.API_BASE_URL, query_params)
        return BusesGPSSuccessfulResponse(json_response)

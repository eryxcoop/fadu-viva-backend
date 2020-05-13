from datetime import datetime, timedelta, timezone

from layers.domain.traffic_configuration.traffic_configuration import TrafficConfiguration
from layers.interface.requester.cache_requester import RequesterUsingCachedResults, RequesterUpdatingCachedResults
from layers.interface.services.buses_gps.api_client import BusesGPSApiClient
from layers.interface.services.daylight_brightness.api_client import BuenosAiresDaylightBrightnessApiClient
from layers.interface.services.traffic_status.api_client import TrafficStatusApiClient


class ServicesProvider:
    def get_daylight_brightness(self):
        buenos_aires_time = datetime.now(tz=timezone(offset=-timedelta(hours=3))).time()
        return BuenosAiresDaylightBrightnessApiClient().get_daylight_brightness_for(time_=buenos_aires_time)

    def get_traffic_status_of(self, place):
        return self._traffic_status_of(place, RequesterUsingCachedResults())

    def update_traffic_status_of(self, place, expiration):
        return self._traffic_status_of(place, RequesterUpdatingCachedResults(expiration))

    def get_arriving_and_departing_buses_to(self, place):
        return self._arriving_and_departing_buses_to(place, RequesterUsingCachedResults())

    def update_arriving_and_departing_buses_to(self, place, expiration):
        return self._arriving_and_departing_buses_to(place, RequesterUpdatingCachedResults(expiration))

    def _traffic_status_of(self, place, requester):
        traffic_status_api_client = TrafficStatusApiClient(requester)
        traffic_configuration = TrafficConfiguration(latitude=place.latitude(),
                                                     longitude=place.longitude(),
                                                     radius=place.radius())
        traffic_response = traffic_status_api_client.get_traffic_status(traffic_configuration)
        traffic_status = traffic_response.get_status_for(main_street=place.main_street(),
                                                         first_crossing_street=place.first_crossing_street(),
                                                         second_crossing_street=place.second_crossing_street())
        return traffic_status

    def _arriving_and_departing_buses_to(self, place, requester):
        buses_gps_api_client = BusesGPSApiClient(requester)
        buses_gps_response = buses_gps_api_client.get_buses_live_position()
        return buses_gps_response.arriving_buses_to(place), buses_gps_response.departing_buses_to(place)

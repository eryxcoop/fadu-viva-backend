from layers.domain.bus.base import Bus, BusPositionVector, BusEndingStop
from layers.domain.geo_coordinate.base import GeoCoordinate
from layers.domain.place.base import Place


class BusesGPSSuccessfulResponse:
    def __init__(self, json_response):
        self._json_response = json_response
        self._buses_position_vector = self._buses_position_vector_from_json_response(json_response)

    def arriving_buses_to(self, place: Place):
        return [bus_position_vector.bus().name() for bus_position_vector in self._buses_position_vector
                if bus_position_vector.is_arriving(place)]

    def departing_buses_to(self, place: Place):
        return [bus_position_vector.bus().name() for bus_position_vector in self._buses_position_vector
                if bus_position_vector.is_departing(place)]

    def _buses_position_vector_from_json_response(self, json_response):
        """
            json_response:
                [{
                    "id": "10691",
                    "route_short_name": "28C",
                    "agency_id": 3,
                    "agency_name": "D.O.T.A. S.A. DE TRANSPORTE AUTOMOTOR",
                    "latitude": -34.60194,
                    "longitude": -58.370285,
                    "speed": 8.333333,
                    "route_id": "84",
                    "trip_headsign": "a La Salada - Bº Hernández"
                    "direction": 0,
                    "timestamp": 1585926128,
                },]
        """
        buses_position_vector = []
        for json_bus_vector in json_response:
            bus_name = ''.join(c for c in json_bus_vector['route_short_name'] if c.isnumeric())  # regex quien te conoce
            latitude = json_bus_vector['latitude']
            longitude = json_bus_vector['longitude']
            route_id = json_bus_vector['route_id']
            direction = json_bus_vector['direction']

            bus_position_vector = BusPositionVector(bus=Bus(bus_name),
                                                    geo_coordinate=GeoCoordinate(latitude, longitude),
                                                    ending_stop=BusEndingStop(route_id, direction))

            buses_position_vector.append(bus_position_vector)
        return buses_position_vector

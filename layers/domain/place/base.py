from layers.domain.geo_coordinate.base import GeoCoordinateCircleArea, GeoCoordinate


# FIXME: too much responsibility
class Place:
    def __init__(self, latitude, longitude, radius, main_street='', first_crossing_street='', second_crossing_street='',
                 bus_ending_stops=None) -> None:

        if bus_ending_stops is None:
            bus_ending_stops = []

        self._geo_area = GeoCoordinateCircleArea(center=GeoCoordinate(latitude, longitude), radius_in_meters=radius)
        self._main_street = main_street
        self._first_crossing_street = first_crossing_street
        self._second_crossing_street = second_crossing_street
        self._bus_ending_stops = bus_ending_stops

    def latitude(self):
        return self._geo_area.latitude()

    def longitude(self):
        return self._geo_area.longitude()

    def radius(self):
        return self._geo_area.radius()

    def main_street(self):
        return self._main_street

    def first_crossing_street(self):
        return self._first_crossing_street

    def second_crossing_street(self):
        return self._second_crossing_street

    def contains_geo_coordinate(self, geo_coordinate):
        return self._geo_area.contains(geo_coordinate)

    def contains_bus_stop(self, bus_stop):
        return any(bus_stop.is_the_same_stop(ending_stop) for ending_stop in self._bus_ending_stops)

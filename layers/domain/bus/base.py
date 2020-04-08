from layers.domain.geo_coordinate.base import GeoCoordinate


class Bus:
    def __init__(self, name) -> None:
        self._name = name

    def name(self):
        return self._name


class BusEndingStop:
    def __init__(self, route_id, direction) -> None:
        self._route_id = route_id
        self._direction = direction

    def route_id(self):
        return self._route_id

    def direction(self):
        return self._direction

    def is_the_same_stop(self, bus_stop) -> bool:
        return self.route_id() == bus_stop.route_id() and self.direction() == bus_stop.direction()


class BusPositionVector:
    def __init__(self, bus: Bus, geo_coordinate: GeoCoordinate, ending_stop: BusEndingStop) -> None:
        self._bus = bus
        self._geo_coordinate = geo_coordinate
        self._ending_stop = ending_stop

    def geo_coordinate(self):
        return self._geo_coordinate

    def ending_stop(self):
        return self._ending_stop

    def bus(self):
        return self._bus

    def is_arriving(self, place):
        return place.contains_geo_coordinate(self.geo_coordinate()) and place.contains_bus_stop(self.ending_stop())

    def is_departing(self, place):
        return place.contains_geo_coordinate(self.geo_coordinate()) and not place.contains_bus_stop(self.ending_stop())

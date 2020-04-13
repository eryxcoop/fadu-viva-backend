import math


class GeoCoordinate:
    def __init__(self, latitude, longitude) -> None:
        self._latitude = latitude
        self._longitude = longitude

    def __repr__(self):
        return f'({self._latitude}, {self._longitude})'

    def latitude(self):
        return self._latitude

    def longitude(self):
        return self._longitude

    def distance_in_meters_from(self, another_geo_coordinate):
        return self._haversine_in_meters(another_geo_coordinate)

    def _haversine_in_meters(self, another_geo_coordinate):
        earth_radius = 6371

        lat1, lon1, lat2, lon2 = [math.radians(self.latitude()),
                                  math.radians(self.longitude()),
                                  math.radians(another_geo_coordinate.latitude()),
                                  math.radians(another_geo_coordinate.longitude())]

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        distance = c * earth_radius

        distance_in_meters = distance * 1000
        return distance_in_meters


class GeoCoordinateCircleArea:
    def __init__(self, center: GeoCoordinate, radius_in_meters) -> None:
        self._center = center
        self._radius_in_meters = radius_in_meters

    def radius(self):
        return self._radius_in_meters

    def center(self) -> GeoCoordinate:
        return self._center

    def latitude(self):
        return self.center().latitude()

    def longitude(self):
        return self.center().longitude()

    def contains(self, geo_coordinate: GeoCoordinate) -> bool:
        return self.center().distance_in_meters_from(geo_coordinate) <= self._radius_in_meters

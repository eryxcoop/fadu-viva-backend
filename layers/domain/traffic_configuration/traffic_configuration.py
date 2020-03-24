class TrafficConfiguration:
    def __init__(self, latitude, longitude, radius):
        """
        :param latitude:
        :param longitude:
        :param radius: in meters
        """

        self._latitude = latitude
        self._longitude = longitude
        self._radius = radius

    def latitude(self):
        return self._latitude

    def longitude(self):
        return self._longitude

    def radius(self):
        return self._radius

from datetime import time

from layers.interface.services.daylight_brightness.time_interval import TimeInterval, TimeIntervals, \
    TimeIntervalBrightnessMap


# TODO this should be replaced by a real service
class BuenosAiresDaylightBrightnessApiClient:
    """
    refer: https://www.timeanddate.com/sun/argentina/buenos-aires
    """

    def __init__(self) -> None:
        daylight = TimeInterval(time(7, 34), time(18, 5))
        civil_twilight = TimeIntervals(TimeInterval(time(7, 8), time(7, 33)), TimeInterval(time(18, 6), time(18, 31)))
        nautical_twilight = TimeIntervals(TimeInterval(time(6, 37), time(7, 7)),
                                          TimeInterval(time(18, 32), time(19, 1)))
        astronomical_twilight = TimeIntervals(TimeInterval(time(6, 8), time(6, 36)),
                                              TimeInterval(time(19, 2), time(19, 31)))
        night = TimeIntervals(TimeInterval(time(0, 0), time(6, 7)), TimeInterval(time(19, 32), time(23, 59)))

        self._interval_brightness_mapping = [
            TimeIntervalBrightnessMap(time_interval=daylight, brightness=10),
            TimeIntervalBrightnessMap(time_interval=civil_twilight, brightness=8),
            TimeIntervalBrightnessMap(time_interval=nautical_twilight, brightness=6),
            TimeIntervalBrightnessMap(time_interval=astronomical_twilight, brightness=3),
            TimeIntervalBrightnessMap(time_interval=night, brightness=0),
        ]

    def get_daylight_brightness_for(self, time_):
        """
        :returns a number between 0 and 10, where 0 is total darkness and 10 is full brightness
        """
        for interval_brightness_map in self._interval_brightness_mapping:
            if interval_brightness_map.contains(time_):
                return interval_brightness_map.brightness()

        raise Exception(f'No time interval for time: {time_}')

class TimeInterval:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def contains(self, time_):
        return self._start <= time_ <= self._end


class TimeIntervals:
    def __init__(self, *time_intervals):
        self._time_intervals = time_intervals

    def contains(self, time_):
        return any(interval.contains(time_) for interval in self._time_intervals)


class TimeIntervalBrightnessMap:
    def __init__(self, time_interval, brightness):
        self._time_interval = time_interval
        self._brightness = brightness

    def contains(self, time_):
        return self._time_interval.contains(time_)

    def brightness(self):
        return self._brightness
class StatusResponsePresenter:
    def __init__(self, traffic_status, arriving_buses, departing_buses):
        self._traffic_status = traffic_status
        self._arriving_buses = arriving_buses
        self._departing_buses = departing_buses

    def present(self):
        return {
            "services": {
                "traffic": {
                    "status": self._traffic_status
                },
                "buses": {
                    "arriving": self._arriving_buses,
                    "departing": self._departing_buses,
                },
            }
        }

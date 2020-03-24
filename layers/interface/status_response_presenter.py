class StatusResponsePresenter:
    def __init__(self, traffic_status):
        self._traffic_status = traffic_status

    def present(self):
        return {
            "services": {
                "traffic": {
                    "status": self._traffic_status
                }
            }
        }

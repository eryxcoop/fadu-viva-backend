import json

from api.api_client import ApiClient
from . import test


@test.route('traffic-status', methods=['GET'])
def get_traffic_status():
    api_client = ApiClient()
    return json.dumps({'status': api_client.get_traffic_status()})


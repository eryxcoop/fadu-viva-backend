import json
from . import test


@test.route('/endpoint-de-prueba', methods=['GET'])
def users_list():
    return json.dumps({'prueba': 'Prueba123'})


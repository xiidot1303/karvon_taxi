from app.services import *
from config import YANDEX_API_KEY, YANDEX_CLIENT_ID
from app.resources.yandex_api_data import *

headers = {'Content-type': 'application/json',  # Определение типа данных
        'Accept': 'text/plain',
        'X-Client-ID': f'taxi/park/{YANDEX_CLIENT_ID}',
        'X-API-Key': YANDEX_API_KEY,
        'Accept-Language': 'en',
        }

url_body = "https://fleet-api.taxi.yandex.net"

def get_drivers_list():
    url = url_body + "/v1/parks/driver-profiles/list"
    data = dirvers_list_data
    try:
        response, header = send_request(url, data, headers, type='post')
        return response['driver_profiles']
    except:
        return {}
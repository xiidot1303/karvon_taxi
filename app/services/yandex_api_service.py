from app.services import *
from config import YANDEX_API_KEY, YANDEX_CLIENT_ID
from app.resources.yandex_api_data import *
from app.services.transaction_category_service import get_transaction_category_id_by_name
from datetime import datetime

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

def create_transaction(amount, driver_profile_id, payment="payme"):
    url = url_body + "/v2/parks/driver-profiles/transactions"
    category_id = get_transaction_category_id_by_name(payment)
    description = f"by {payment}"
    data = create_transaction_data(amount, category_id, description, driver_profile_id)
    request_headers = headers
    token = generate_idempotency_token()
    request_headers['X-Idempotency-Token'] = token
    response, status = send_request(url, data, request_headers, type="post")
    return status

def get_transaction_category_list():
    url = url_body + "/v2/parks/transactions/categories/list"
    data = category_list_data
    response, status = send_request(url, data, headers, type="post")
    return response

def get_last_order_of_driver(driver_id):
    url = url_body + '/v1/parks/orders/list'
    data = order_history_data(driver_id)
from datetime import datetime, date, timedelta
import requests, json
import string, random

def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def datetime_now():
    now = datetime.now()
    return now

def time_now():
    now = datetime.now()
    return now.time()

def today():
    today = date.today()
    return today

def send_request(url, data=None, headers=None, type='get'):
    if type == 'get':
        response = requests.get(url, params=data, headers=headers)
        content = json.loads(response.content)
        status = response.status_code
    else:
        response = requests.post(url, json=data, headers=headers)
        content = json.loads(response.content)
        status = response.status_code

    return content, status

def generate_idempotency_token(length=32):
    # Generate a random string of ASCII characters
    characters = string.ascii_letters + string.digits
    idempotency_token = ''.join(random.choice(characters) for _ in range(length))
    return idempotency_token
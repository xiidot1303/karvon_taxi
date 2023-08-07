import requests
import base64
from config import PLAYMOBILE_LOGIN, PLAYMOBILE_PASSWORD

session = requests.Session()
login = PLAYMOBILE_LOGIN
password = PLAYMOBILE_PASSWORD
session.auth = (login, password)

url = "https://send.smsxabar.uz/broker-api/send"

def send_sms_by_newsletters(newsletters):
    credentials = f"{login}:{password}"
    credentials_base64 = base64.b64encode(credentials.encode()).decode()
    headers = {'Content-type': 'application/json',  # Определение типа данных
            'Accept': 'text/plain', 
            "Authorization": f"Basic {credentials_base64}"
            }

    data = {
        "messages": [
            {
            "recipient": newsletter.phone[1:],
            "message-id": f"a{newsletter.id}",
                "sms": {
                    "originator": "Karvontaxi",
                    "content": {
                        "text": newsletter.text
                    }
                }
            }
            for newsletter in newsletters
        ]
    } 

    response = requests.post(url, json=data, headers=headers)
    # response = session.post(url, data=data, headers=headers)

    return response.status_code
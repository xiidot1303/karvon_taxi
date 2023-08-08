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
    for newsletter in newsletters:
        data = {
            "messages": [
                {
                "recipient": driver.phone[1:],
                "message-id": f"a{newsletter.id}",
                    "sms": {
                        "originator": "Karvontaxi",
                        "content": {
                            "text": generate_text(newsletter.text, driver)
                        }
                    }
                }
                for driver in newsletter.get_drivers
            ]
        } 
        response = requests.post(url, json=data, headers=headers)
    # response = session.post(url, data=data, headers=headers)
    return response.status_code

def generate_text(text, driver):
    text = text.replace("**ism", driver.full_name)
    if driver.balance > 6000:
        text = text.replace("**balans", str(driver.balance))
    else: 
        text = text.replace("**balans", "")
    text = text.replace("**pozivnoy", str(driver.callsign))
    return text



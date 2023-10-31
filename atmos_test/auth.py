import requests
from dotenv import load_dotenv
import os
import base64

load_dotenv(os.path.join(".env"))

login = os.environ.get("ATMOS_CONSUMER_KEY")
password = os.environ.get("ATMOS_CONSUMER_SECRET")

auth_string = f"{login}:{password}".encode()
auth_bytes = base64_bytes = base64.b64encode(auth_string)
auth_key = auth_bytes.decode()

headers = {
    'Authorization': auth_key
}

url = "https://api.atmos.uz/token?grant_type=client_credentials"

r = requests.post(url, headers=headers)
print(r.content.decode())


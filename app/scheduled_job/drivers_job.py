from app.services.yandex_api_service import get_drivers_list, get_last_order_of_driver
from app.services.driver_service import update_or_create_driver, all_drivers, update_last_order_of_driver
from datetime import datetime
from time import sleep

def update_drivers():
    driver_profiles = get_drivers_list()
    for driver in driver_profiles:
        # get main values list
        account = driver["accounts"][0]
        car = driver["car"] if "car" in driver else {}
        current_status = driver["current_status"]
        profile = driver["driver_profile"]
        # get values account
        balance = account["balance"]
        balance = int(float(balance))
        # last_transaction_date = account["last_transaction_date"] if "last_transaction_date" in account else None
        last_transaction_date = None
        # get values car
        callsign = car["callsign"] if "callsign" in car else ""
        # get values status
        status = current_status["status"]
        # get values profile
        profile_id = profile["id"]
        first_name = profile["first_name"] if "first_name" in profile else ""
        last_name = profile["last_name"] if "last_name" in profile else ""
        phone = profile["phones"][0] if profile["phones"] else ''
        # turn to datetime object
        last_transaction = datetime.strptime(
            last_transaction_date, 
            "%Y-%m-%dT%H:%M:%S.%f%z"
            ).replace(tzinfo=None) if last_transaction_date else None
        # last_transaction = last_transaction.replace(tzinfo=None)
        # try:
        #     last_order = get_last_order_of_driver(profile_id)
        # except:
        #     last_order = None
        # sleep(0.5)
        # create or update drivers
        update_or_create_driver(
            profile_id, first_name, last_name,
            phone, status, callsign,
            last_transaction, balance, None
        )

def update_last_order_of_drivers():
    drivers = all_drivers()
    for driver in drivers:
        try:
            last_order = get_last_order_of_driver(driver.profile_id)
        except Exception as ex:
            last_order = None
            print(ex)
        update_last_order_of_driver(driver, last_order)
        sleep(2)
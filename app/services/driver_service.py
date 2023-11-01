from app.services import *
from app.models import Driver

def all_drivers():
    return Driver.objects.all()

def update_or_create_driver(
    profile_id, first_name, last_name, phone,
    status, callsign, last_transaction, balance
):
    driver, created = Driver.objects.get_or_create(profile_id=profile_id)
    driver.first_name = first_name
    driver.last_name = last_name
    driver.phone = phone
    driver.status = status
    driver.callsign = callsign
    driver.last_transaction = last_transaction
    driver.balance = balance
    # driver.last_order = last_order
    driver.save()
    return driver

def get_driver_by_callsign(callsign):
    try:
        driver = Driver.objects.get(callsign=str(callsign))
        return driver
    except:
        return None
    
def update_last_order_of_driver(driver: Driver, last_order):
    driver.last_order = last_order
    driver.save()
    return
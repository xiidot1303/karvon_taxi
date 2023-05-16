from app.services import *
from payment.models import Payme_transaction as Trans
from payment.utils import time_ts

def get_or_create_transaction(payme_trans_id, driver, amount, time, create_time) -> Trans:
    obj, created = Trans.objects.get_or_create(payme_trans_id=payme_trans_id)
    if created:
        obj.driver = driver
        obj.amount = amount
        obj.time = time
        obj.create_time = create_time
        obj.state = 1
        obj.save()
    return obj

def get_transaction_by_payme_trans_id(id):
    try:
        obj = Trans.objects.get(payme_trans_id=id)
        return obj
    except:
        return None

def perform_transaction(obj: Trans):
    obj.state = 2
    obj.perform_time = time_ts()
    obj.save()
    return

def cancel_transaction(obj: Trans, state: int, reason: int):
    obj.state = state
    obj.reason = reason
    obj.cancel_time = time_ts()
    obj.save()
    return

def filter_transactions_by_createtime_period(from_, to):
    return Trans.objects.filter(create_time__range = (from_, to))
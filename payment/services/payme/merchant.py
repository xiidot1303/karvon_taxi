from app.services.driver_service import get_driver_by_callsign
from payment.resources.payme_responses import Errors, Results
from payment.utils import time_ts
from payment.services.payme.transaction import *

def CheckPerformTransaction(amount, callsign):
    if driver:=get_driver_by_callsign(callsign):
        name = f"{driver.last_name} {driver.first_name}"
        return Results.CHECKPERFORM_TRANSACTION(name, driver.phone), None
    else:
        return None, Errors.USER_NOT_FOUND
    
def CreateTransaction(id, time, amount, callsign):
    if driver:=get_driver_by_callsign(callsign):
        if time_ts() - time >= 43200000:
            return {}, Errors.CANNOT_PERFORM_OPERATION
        trans_obj = get_or_create_transaction(id, driver,amount, time_ts(), time)
        create_time = trans_obj.create_time
        trans_id = str(trans_obj.id)
        state = trans_obj.state
        return Results.CREATE_TRANSACTION(create_time, trans_id, state), None
    else:
        return None, Errors.USER_NOT_FOUND

def PerformTransaction(id):
    if trans_obj:=get_transaction_by_payme_trans_id(id):
        # check transactio  status
        if trans_obj.state == 1:
            # check time out
            if time_ts() - trans_obj.create_time >= 43200000:
                cancel_transaction(trans_obj, -1, 4)
                return {}, Errors.CANNOT_PERFORM_OPERATION
            # end transaction
            perform_transaction(trans_obj)
            # change driver yandex balance
            # -----
        else:
            if trans_obj.state != 2:
                return None, Errors.CANNOT_PERFORM_OPERATION

        # success return
        trans_id = str(trans_obj.id)
        perform_time = trans_obj.perform_time
        state = trans_obj.state
        return Results.PERFORM_TRANSACTION(trans_id, perform_time, state), None
    else:
        return None, Errors.TRANSACTION_NOT_FOUND

def CancelTransaction(id, reason):
    if trans_obj:=get_transaction_by_payme_trans_id(id):
        if trans_obj.state == 1:
            cancel_transaction(trans_obj, -1, reason)
        elif trans_obj.state == 2:
            return None, Errors.CANNOT_CANCEL_TRANSACTION
        # success return
        trans_id = str(trans_obj.id)
        cancel_time = trans_obj.cancel_time
        state = trans_obj.state
        return Results.CANCEL_TRANSACTION(trans_id, cancel_time, state), None
    else:
        return None, Errors.TRANSACTION_NOT_FOUND
    
def CheckTransaction(id):
    if trans_obj:=get_transaction_by_payme_trans_id(id):
        result = Results.CHECK_TRANSACTION(
            trans_obj.create_time, trans_obj.perform_time,
            trans_obj.cancel_time, str(trans_obj.id),
            trans_obj.state, trans_obj.reason
        )
        return result, None
    else:
        return None, Errors.TRANSACTION_NOT_FOUND
    
def GetStatement(from_, to):
    transactions = filter_transactions_by_createtime_period(from_, to)
    return Results.GET_STATEMENT(transactions), None
from sms.models import *
from sms.services.playmobile_service import *

def send_newsletters():
    # filter unsent newsletters
    newsletters = Newsletter.objects.filter(status = 0)
    # send sms
    send_sms_by_newsletters(newsletters)
    # update newsletter status
    newsletters.update(status = 1)

def alert_drivers():
    alerts = Alert_by_last_order.objects.all()
    for alert in alerts:
        # get drivers by last order days
        
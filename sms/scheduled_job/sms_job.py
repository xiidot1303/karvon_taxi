from sms.models import *
from app.models import Driver
from sms.services.playmobile_service import *
from datetime import datetime, timedelta

def send_newsletters():
    # filter unsent newsletters
    newsletters = Newsletter.objects.filter(status = 0)
    # send sms
    send_sms_by_newsletters(newsletters) if newsletters else None
    # update newsletter status
    newsletters.update(status = 1)

def alert_drivers():
    alerts = Alert_by_last_order.objects.all()
    for alert in alerts:
        # get drivers by last order days
        since = alert.since
        date_since = datetime.now() - timedelta(days=since)
        if since:
            drivers = Driver.objects.filter(last_order__lte=date_since)
        else:  
            drivers = Driver.objects.filter(last_order=None)
        # create newsletters for drivers
        for driver in drivers:
            Newsletter.objects.create(
                driver = driver,
                text = alert.text
            )


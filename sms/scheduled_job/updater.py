from apscheduler.schedulers.background import BackgroundScheduler
from sms.scheduled_job.sms_job import *

class jobs:
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(send_newsletters, 'interval', minutes=5)
    scheduler.add_job(alert_drivers, 'interval', days=2)
from apscheduler.schedulers.background import BackgroundScheduler
from app.scheduled_job import drivers_job

class jobs:
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(drivers_job.update_drivers, 'interval', minutes=10)

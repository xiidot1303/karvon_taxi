from apscheduler.schedulers.background import BackgroundScheduler
from app.scheduled_job import drivers_job, transaction_job

class jobs:
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(drivers_job.update_drivers, 'interval', minutes=10)
    scheduler.add_job(transaction_job.update_categories, 'interval', minutes=5)

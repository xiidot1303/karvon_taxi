from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from app.scheduled_job import drivers_job, transaction_job

class jobs:
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    scheduler.add_job(drivers_job.update_drivers, 'interval', minutes=10)
    scheduler.add_job(drivers_job.update_last_order_of_drivers, 'interval', minutes=60)
    scheduler.add_job(transaction_job.update_categories, 'interval', minutes=5)

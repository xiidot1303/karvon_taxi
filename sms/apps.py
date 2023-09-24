from django.apps import AppConfig
import os

class sms(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sms'
    def ready(self):
        # run_once = os.environ.get('CMDLINERUNNER_RUN_ONCE_SMS')
        # if run_once is not None:
        #     return
        # os.environ['CMDLINERUNNER_RUN_ONCE_SMS'] = 'True'
        from sms.scheduled_job.updater import jobs
        jobs.scheduler.start()
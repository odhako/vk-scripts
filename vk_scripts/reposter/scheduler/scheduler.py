from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
# from django.utils import timezone
# from django_apscheduler.models import DjangoJobExecution
import sys
from ..modules.vk_api_code import repost_test


# This is the function you want to schedule - add as many
# as you want and then register them in the start() function below
# def deactivate_expired_accounts():
#     today = timezone.now()
#     ...
#     # get accounts, expire them, etc.
#     ...


def print_console():
    print('60 seconds passed...')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # run this job every 24 hours
    # scheduler.add_job(deactivate_expired_accounts,
    #                   'interval',
    #                   hours=24,
    #                   name='clean_accounts',
    #                   jobstore='default')

    # scheduler.add_job(print_console,
    #                   'interval',
    #                   seconds=60,
    #                   id='60_sec',
    #                   replace_existing=True)
    scheduler.add_job(repost_test,
                      'cron',
                      hour="10,11,12,13,14,15,16,17,18,19,20,21,22",
                      id='1_hour_repost',
                      replace_existing=True,
                      misfire_grace_time=7200,
                      jitter=120)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)

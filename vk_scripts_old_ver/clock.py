from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


# scheduler = BackgroundScheduler()
#
#
# @scheduler.scheduled_job('interval', seconds=10)
# def timed_job():
#     print('This job is run every ten seconds.')
#
#
# @scheduler.scheduled_job('cron', hour="10,21")
# def morning():
#     print('This job is run every morning at 10:00 and 21:00.')
#
#
# # Edit this to change time of repost
# @scheduler.scheduled_job('cron', hour=17, minute=10)
# def time():
#     repost()
#
#
# def start():
#     scheduler.start()


def print_console():
    print('Ten seconds passed...')


def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(print, 'interval', seconds=10, args=[datetime.now()])
    scheduler.add_job(print_console, 'interval', seconds=10)
    # scheduler.add_job(print, 'cron', hour=16, minute=46, args=['Post_going_here'])
    # scheduler.add_job(repost_test, 'cron', hour=9, minute=15)
    scheduler.start()

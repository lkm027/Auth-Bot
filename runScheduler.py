from datetime import datetime
import time
import os

from send_message import send_groupme_message
from re_add_members import get_list_of_kicked_users

from apscheduler.schedulers.blocking import BlockingScheduler

def run_scheduler():
    print( "Running Scheduler" )
    get_list_of_kicked_users()

scheduler = BlockingScheduler()
scheduler.add_job( run_scheduler, "interval", days = 1 )
print( "Starting scheduler")
scheduler.start()

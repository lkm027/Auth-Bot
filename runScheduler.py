from datetime import datetime
import time
import os

from rq import Queue
from worker import conn
://github.com/git-mad/Tap-Game.gitrint( "Running scheduler")

from send_message import send_groupme_message
from re_add_members import get_list_of_kicked_users

from apscheduler.schedulers.blocking import BlockingScheduler

def run_scheduler():
    print( "Running Scheduler" )
    get_list_of_kicked_users()

scheduler = BlockingScheduler()o
q = Queue( connection = conn )

def get_working():
    q.enqueue( run_scheduler )

# enqueue right away once
scheduler.add_job( get_working )
scheduler.add_job( run_scheduler, "interval", days = 1 )
print( "Starting scheduler")
scheduler.start()

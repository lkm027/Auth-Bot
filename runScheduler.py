from datetime import datetime
import time
import os

from send_message import send_groupme_message

from apscheduler.schedulers.blocking import BlockingScheduler

def hello():
    send_groupme_message( "Hello from the scheduler" )

scheduler = BlockingScheduler()
scheduler.add_job( hello, "interval", minutes = 1 )
scheduler.start()

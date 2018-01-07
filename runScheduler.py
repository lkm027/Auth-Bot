from datetime import datetime
import time
import os

from send_message import send_groupme_message
from re_add_members import get_list_of_kicked_users

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job( get_list_of_kicked_users, "interval", minutes = 1 )
scheduler.start()

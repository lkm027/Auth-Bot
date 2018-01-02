import db.db_requests as db_requests
from send_message import send_groupme_message

def drop_all_members():
    db_requests.drop_all_members()
    send_groupme_message( "All members dropped successfully." )

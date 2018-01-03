import db.db_requests as db_requests
from send_message import send_groupme_message

def make_admin( member_name ):
    db_requests.make_member_admin( member_name )
    send_groupme_message( member_name + " you have been promoted to admin!" )

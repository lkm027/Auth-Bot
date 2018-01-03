import db.db_requests as db_requests
from send_message import send_groupme_message

def make_admin( member_name ):
    if( db_requests.make_member_admin( member_name ) ):
        send_groupme_message( member_name + " you have been promoted to admin!" )
    else:
        send_groupme_message( member_name + " is not a member of this group." )

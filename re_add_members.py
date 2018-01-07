from datetime import date

from send_message import send_groupme_message
import db.db_requests as db_requests
from pardon import add_member_back_to_group

def get_list_of_kicked_users():
    current_date = str( date.today() )
    db_requests.get_kicked_members( current_date )

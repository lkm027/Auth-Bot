from datetime import date

from send_message import send_groupme_message
import db.db_requests as db_requests
from pardon import add_member_back_to_group

def get_list_of_kicked_users():
    print( "Getting list of kicked users" )
    current_date = str( date.today() )
    kicked_members = db_requests.get_kicked_members( current_date )
    if( len( kicked_members ) > 0 ):
        for member in kicked_members:
            add_member_back( member )

def add_member_back( member_name ):
    add_member_back_to_group( member_name )
    db_requests.remove_member_kick_date( member_name )


get_list_of_kicked_users()

import emoji
import requests
import json
import os

from datetime import *

from send_message import send_groupme_message
import db.db_requests as db_requests

KICK_WARNING = 3
LENGTH_OF_KICK = 3

def add_warning_to_member( member_id, member_name ):
    db_requests.add_new_warning_to_member( member_id )
    warnings_count = db_requests.get_warnings_count_by_id( member_id )
    send_groupme_message( emoji.emojize( member_name + ", you will be kicked on your 3rd warning. Please do not post again.\n:police_car_light: Your warning count: " + str( warnings_count ) + " :police_car_light:" ) )
    if( warnings_count == KICK_WARNING ):
        kick_member_by_user_id( member_id )

def kick_member_by_user_id( user_id ):
    member_id = db_requests.get_member_member_id( user_id )
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )
    url      = "https://api.groupme.com/v3/groups/" + group_id + "/members/" + member_id + "/remove"

    requests.post( url, data = json.dumps( {} ) , headers = headers )

def kick_member_by_name( member_name ):
    user_id = db_requests.get_member_user_id( member_name )
    return_date = get_kick_date()
    db_requests.set_kick_date_for_member( user_id, return_date )
    kick_member_by_user_id( user_id )

def get_kick_date():
    current_date  = date.today()
    return_date = str( current_date )
    # kick_duration = timedelta( days = LENGTH_OF_KICK )
    # return_date   = current_date + kick_duration
    return return_date

import emoji
import requests
import json
import os

from send_message import send_groupme_message
import db.db_requests as db_requests

KICK_WARNING = 3

def add_warning_to_member( member_id, member_name ):
    db_requests.add_new_warning_to_member( member_id )
    warnings_count = db_requests.get_warnings_count_by_id( member_id )
    send_groupme_message( emoji.emojize( member_name + ", you will be kicked on your 3rd warning. Please do not post again.\n:police_car_light: Your warning count: " + str( warnings_count ) + " :police_car_light:" ) )
    if( warnings_count == KICK_WARNING ):
        kick_member( member_id )

def kick_member( member_id ):
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )
    url      = "https://api.groupme.com/v3/groups/" + group_id + "/members/" + member_id + "/remove"

    requests.post( url, data = json.dumps( {} ) , headers = headers )

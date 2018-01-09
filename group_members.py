import requests
import json
import os

from send_message import send_groupme_message
import db.db_requests as db_requests

def update_members_list():
    members = get_members_list()
    update_table( members )

    send_groupme_message( "Retrieved all group members" )

    return True

def update_table( members ):
    for member in members:
        member_id = member["user_id"]
        member_name = member["nickname"]
        member_membership_id = member["id"]
        if( not db_requests.check_if_member_exists_by_id( member_id ) ):
            # When the first update is called we want to automatically make the owner an admin
            db_requests.save_member_to_db( member_name, member_id, member_membership_id )
    send_groupme_message( "Members successfully updated." )

def get_members_list():
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )

    # Grab a list of the current users in the group
    r = requests.get( "https://api.groupme.com/v3/groups/" + group_id, data = json.dumps( {} ), headers = headers )

    response = r.json()
    members = response['response']['members']

    return members


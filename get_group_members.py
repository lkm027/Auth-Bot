import requests
import json
import os

from send_message import send_groupme_message

def get_members():
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )

    r = requests.get( "https://api.groupme.com/v3/groups/" + group_id, data = json.dumps( {} ), headers = headers )

    members = r.json()
    send_groupme_message( members['response']['members'][0]['nickname'] )

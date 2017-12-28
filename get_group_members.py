import requests
import json
import os

def get_members():
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )

    r = requests.get( "https://api.groupme.com/v3/groups/" + group_id, data = json.dumps( {} ), headers = headers )
    print( r.members )
    print( r.text[0] )
    members = r.text["response"]["members"]
    print( members[0]["nickname"] )

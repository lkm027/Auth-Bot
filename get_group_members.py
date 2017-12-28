import request
import json
import os

def get_members():
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )

    request = requests.post( "https://api.groupme.com/v3/groups/" + group_id, data = json.dumps( {} ), headers = headers )
    members = request.text.members
    print( members )

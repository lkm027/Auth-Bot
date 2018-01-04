from send_message import send_groupme_message
import db.db_requests as db_requests

PARDON_NUMBER = 2

def pardon( member_name ):
    if( db_requests.check_if_member_exists_by_name( member_name ) ):
        # db_requests.remove_warning_from_member( member_name )
        # warnings_count = db_requests.get_warnings_count_by_name( member_name )

        # If a member is pardoned and their warning count is one below the kick, add them back to the group
        # if( warnings_count == PARDON_NUMBER ):
        add_member_back_to_group( member_name )

        # send_groupme_message( "Congrats " + member_name + "! You have been pardon by the almighty overlords. Your current warning count: " + str( warnings_count ) + "." )

def add_member_back_to_group( member_name ):
    member_id = db_requests.get_member_user_id( member_id )
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )
    url      = "https://api.groupme.com/v3/groups/" + group_id + "/members/add"
    data     = {
                "members" :
                [
                    {
                        "user_id" : member_id,
                        "nickname" : member_name
                    }
                ]
            }

    r = requests.get( url, data = json.dumps( data ), headers = headers )

    # response = r.json()
    # members = response['response']['members']

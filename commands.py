from send_message import send_groupme_message
from group_members import check_and_add_members_if_none_exist

def check_all_commands( command ):
    # Remove the auth bot call from our command
    words = str.split( command )
    words.pop( 0 )
    words.pop( 0 )
    command = "".join( words )

    command.lower()
    print( command )
    return {
            "retrieve members" : retrieve_members()
            }.get( command, send_groupme_message( "That command does not exist" ) )

def retrieve_members():
    check_and_add_members_if_none_exist()


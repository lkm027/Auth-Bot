import emoji

from send_message import send_groupme_message
from group_members import update_members_list, check_if_member_table_exists
from pardon import pardon
from db_requests import is_member_admin

def check_all_commands( command, member ):
    if( not is_member_admin( member ) ):
        return
    # Remove the auth bot call from our command
    words = str.split( command )
    words.pop( 0 )
    words.pop( 0 )
    command = " ".join( words )

    command.lower()

    # Check our list of commands
    if( command == "update members" ):
        update_members()
    elif( "pardon" in command ):
        words = str.split( command )
        words.pop(0)
        member = " ".join( words )
        pardon_member( member )
    else:
        send_groupme_message( "That command does not exist" )

# Retrieves all members in a group and stores them within our db
def update_members():
    update_members_list()

def pardon_member( member ):
    pardon( member )

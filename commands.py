from send_message import send_groupme_message
from group_members import check_and_add_members_if_none_exist
from pardon import pardon

import emoji

def check_all_commands( command ):
    # Remove the auth bot call from our command
    words = str.split( command )
    words.pop( 0 )
    words.pop( 0 )
    command = " ".join( words )

    command.lower()

    # Check our list of commands
    if( command == "retrieve members" ):
        retrieve_members()
    elif( command == "pardon" ):
        words = str.split( command )
        words.pop(0)
        member = " ".join( words )
        pardon_member( member )
    else:
        send_groupme_message( "That command does not exist" )

# Retrieves all members in a group and stores them within our db
def retrieve_members():
    check_and_add_members_if_none_exist()

def pardon_member( member ):
    pardon( member )

import emoji

from send_message import send_groupme_message
from group_members import update_members_list
from pardon import pardon
import drop_members as drop_members

def check_all_commands( command, member ):
    # Remove the auth bot call from our command
    words = str.split( command )
    words.pop( 0 )
    words.pop( 0 )
    command = " ".join( words )

    command = command.lower()

    # Check our list of commands
    if( command == "update members" ):
        update_members()
    elif( "pardon" in command ):
        words = str.split( command )
        words.pop(0)
        member = " ".join( words )
        pardon_member( member )
    elif( command == "remove all members" ):
        drop_all_members()
    else:
        send_groupme_message( "That command does not exist" )

# Retrieves all members in a group and stores them within our db
def update_members():
    update_members_list()

# Drops all members in our table.
# All current members in the group will then be readded immediatelly following.
def drop_all_members():
    drop_members.drop_all_members()

def pardon_member( member ):
    pardon( member )

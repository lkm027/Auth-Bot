import emoji

from send_message import send_groupme_message
from group_members import update_members_list
from add_warning import kick_member_by_name
from pardon import pardon
import drop_members as drop_members
import make_admin as make_admin

def check_all_commands( command, member ):
    # Remove the auth bot call from our command
    words = str.split( command )
    words.pop( 0 )
    words.pop( 0 )
    command = " ".join( words )

    # command = command.lower()

    # Check our list of commands
    if( command == "update members" ):
        update_members()
    elif( "pardon" in command ):
        member = get_command_name( command )
        pardon_member( member )
    elif( command == "remove all members" ):
        drop_all_members()
    elif( "promote" in command ):
        member = get_command_name( command )
        promote( member )
    elif( "kick" in command ):
        member = get_command_name( command )
        kick_member( member )
    else:
        send_groupme_message( "That command does not exist" )

# Retrieves all members in a group and stores them within our db
def update_members():
    update_members_list()

# Drops all members in our table.
# All current members in the group will then be readded immediatelly following.
def drop_all_members():
    drop_members.drop_all_members()

# Remove a warning from a user
def pardon_member( member ):
    pardon( member )

# promote user to be an admin
def promote( member ):
    make_admin.make_admin( member )

def kick_member( member ):
    kick_member_by_name( member )

# Assumption is that there is only one word before the name and none after
def get_command_name( command ):
    pos = command.find( "@" )
    # if the user is not specified with @
    if( pos == -1 ):
        words = str.split( command )
        words.pop( 0 )
        member = " ".join( words )
    else:
        pos = pos + 1
        command = command[pos:]
        print( command )
        words = str.split( command )
        member = " ".join( words )
    return member

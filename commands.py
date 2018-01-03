import emoji

from send_message import send_groupme_message
from group_members import update_members_list
from pardon import pardon
import drop_members as drop_members
import make_admin as make_admin

def check_all_commands( command, member ):
    # Remove the auth bot call from our command
    print( command )
    words = str.split( command )
    words.pop( 0 )
    words.pop( 0 )
    command = " ".join( words )
    print( command )

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

# Assumption is that there is only one word before the name and none after
def get_command_name( command ):
    pos = command.find( "@" )
    command = command[pos:]
    print( command )
    words = str.split( command )
    words.pop(0)
    words[0] = words[0][1:]
    member = " ".join( words )
    print( command )
    return member

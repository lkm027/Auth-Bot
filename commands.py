from send_message import send_groupme_message
from group_members import check_and_add_members_if_none_exist

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
    elif( command == "salt" ):
        salt()
    elif( command == "utf" ):
    else:
        send_groupme_message( "That command does not exist" )

# Retrieves all members in a group and stores them within our db
def retrieve_members():
    check_and_add_members_if_none_exist()

def salt():
    send_groupme_message( "https://media.giphy.com/media/3o7P4F86TAI9Kz7XYk/giphy.gif" )

def utf():
    send_groupme_message( u'\1F60d' )

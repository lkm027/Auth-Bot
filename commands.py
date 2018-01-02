import emoji

from db_connection import get_db_connection
from send_message import send_groupme_message
from group_members import update_members_list, check_if_member_table_exists
from pardon import pardon

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

def is_member_admin( member ):
    # This should only be called if we haven't created a table yet. This allows anyone to create a command while no table exists.
    # TODO The table check and creation could probably be exported to occur right when the bot starts up to prevent multiple calls
    if( not check_if_member_table_exists() ):
        return True
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where nickname='" + member + "';" )
    rows = cursor.fetchall()
    if( rows[0][0] != 0 ):
        cursor.execute( "SELECT * FROM tb_members where nickname='" + member + "';" )
        rows = cursor.fetchall()
        is_admin = rows[0][3]
        if( is_admin ):
            return True
        return False
    else:
        print( "The user before does not exist within the database." )
    cursor.close()
    conn.close()

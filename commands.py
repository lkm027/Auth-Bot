import os
import psycopg2
import emoji

from urllib import parse

from send_message import send_groupme_message
from group_members import check_and_add_members_if_none_exist
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
    if( command == "retrieve members" ):
        retrieve_members()
    elif( "pardon" in command ):
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

def is_member_admin( member ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where nickname='" + member + "';" )
    rows = cursor.fetchall()
    if( rows[0][0] != 0 ):
        cursor.execute( "SELECT * FROM tb_members where nickname='" + member + "';" )
        rows = cursor.fetchall()
        rows[0][3] = is_admin
        if( is_admin ):
            return True
        return False
    else:
        print( "The user before does not exist within the database." )
    cursor.close()
    conn.close()

def get_db_connection():
    try:
        parse.uses_netloc.append("postgres")
        url = parse.urlparse(os.environ["DATABASE_URL"])

        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

        return conn

    except Exception as e:
        print( "Could not establish a connection with the database." )
        print( e )

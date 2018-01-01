import os
import psycopg2

from urllib import parse

from send_message import send_groupme_message

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

def pardon( member ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where nickname='" + member + "';" )
    rows = cursor.fetchall()
    if( rows[0][0] != 0 ):
        cursor.execute( "SELECT * FROM tb_members where nickname='" + member + "';" )
        rows = cursor.fetchall()
        rows[0][3] = is_admin
        if( is_admin ):
            remove_warning_from_member( member )
    else:
        print( "The user before does not exist within the database." )
    cursor.close()
    conn.close()

def remove_warning_from_member( member ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE nickname='" + member + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][5] - 1
    cursor.execute( "UPDATE tb_members set warnings=" + str( warnings_count ) + " where nickname='" + member + "';" )

    send_groupme_message( "Congrats " + member + "! You have been pardon by the almighty overlords. Your current warning count: " + str( warnings_count ) + "." )
    conn.commit()
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

import requests
import json
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
        remove_warning_from_member( member )
    else:
        print( "The user before does not exist within the database." )
    cursor.close()
    conn.close()

def remove_warning_from_member( member ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][5] - 1
    cursor.execute( "UPDATE tb_members set warnings=" + str( warnings_count ) + " where user_id='" + member_id + "';" )

    send_groupme_message( member_name + ", you will be kicked on your 3rd warning. Please do not post again. Your current warning count: " + str( warnings_count ) + "." )
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

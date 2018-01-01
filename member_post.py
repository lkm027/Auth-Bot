import os
import psycopg2
import emoji

from urllib import parse

from send_message import send_groupme_message

def check_if_member_is_admin( member_id ):
    if( not check_if_member_table_exists() ):
        return
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    if( not rows[0][3] ):
        return False
    return True

def add_warning_to_member( member_id, member_name ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][5] + 1
    cursor.execute( "UPDATE tb_members set warnings=" + str( warnings_count ) + " where user_id='" + member_id + "';" )

    send_groupme_message( emoji.emojize( member_name + ", you will be kicked on your 3rd warning. Please do not post again.\n:police_car_light: Your warning count: " + str( warnings_count ) + " :police_car_light:" ) )
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

def check_if_member_table_exists():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( """SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables
                        WHERE table_schema = 'public'
                        AND table_name = 'tb_members' );""" )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    if( not rows[0][0] ):
        return False

    return True

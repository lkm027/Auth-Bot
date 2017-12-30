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

def check_and_add_members_if_none_exist():
    if( not check_if_member_table_exists() ):
        create_members_table()
    if( is_group_members_table_empty() ):
        get_members_and_add_to_table()

    send_groupme_message( "Retrieved all group members" )

    return True


def get_members_and_add_to_table():
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )

    # Grab a list of the current users in the group
    r = requests.get( "https://api.groupme.com/v3/groups/" + group_id, data = json.dumps( {} ), headers = headers )

    response = r.json()
    members = response['response']['members']

    # Iterate through each person currently in the group and add them to our members table
    for member in members:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute( "INSERT INTO tb_members( nickname, user_id, is_admin, kicked, warnings ) VALUES ( " + "'" + member['nickname'] + "'" + ", " + member['user_id'] + ", False, NULL, 0 );" )
        cursor.execute( insert_statement )
        cursor.close()
        conn.commit()
        conn.close()

def create_members_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( """CREATE TABLE tb_members
                        ( id SERIAL PRIMARY KEY,
                          nickname TEXT,
                          user_id VARCHAR(80),
                          is_admin BOOLEAN,
                          kicked DATE,
                          warnings INTEGER );""" )

    cursor.close()
    conn.commit()
    conn.close()

def is_group_members_table_empty():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM tb_members")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    if( rows[0][0] == 0 ):
        return True

    return False

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

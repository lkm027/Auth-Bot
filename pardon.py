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

def find_member( person ):
    conn = get_db_connection()

    members = get_group_members()
    for member in members:


def get_group_members():
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )

    # Grab a list of the current users in the group
    r = requests.get( "https://api.groupme.com/v3/groups/" + group_id, data = json.dumps( {} ), headers = headers )

    response = r.json()
    members = response['response']['members']

    return members

    # Iterate through each person currently in the group and add them to our members table
    for member in members:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute( "INSERT INTO tb_members( user_id, is_admin, kicked, warnings ) VALUES ( " + member['user_id'] + ", False, NULL, 0 );" )
        cursor.close()
        conn.commit()
        conn.close()

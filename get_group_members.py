import requests
import json
import os
import psycopg2

from send_message import send_groupme_message
from urllib import parse

def get_members():
    headers = {
            "X-Access-Token" : os.getenv( "USER_ID" ),
            "Content-type"   : "application/json"
            }

    group_id = os.getenv( "GROUPME_GROUP_ID" )

    r = requests.get( "https://api.groupme.com/v3/groups/" + group_id, data = json.dumps( {} ), headers = headers )

    response = r.json()
    members = response['response']['members']

    is_group_members_table_empty()
    check_if_member_table_exists()

    for member in members:
        send_groupme_message( member['nickname'] )

def is_group_members_table_empty():
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

        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM EXAMPLE")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        if( rows[0][0] == 0 ):
            return false

        return true

    except Exception as e:
        print( "Connecting to db failed for some reason" )
        print( e )

def check_if_member_table_exists():
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

        cursor = conn.cursor()
        cursor.execute( """SELECT EXISTS (
                            SELECT 1 FROM information_schema.tables
                            WHERE table_schema = 'public'
                            AND table_name = 'members' );""" )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        print( rows[0] )

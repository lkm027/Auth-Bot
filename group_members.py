import requests
import json

from send_message import send_groupme_message
from db_connection import get_db_connection()

def update_members_list():
    if( not check_if_member_table_exists() ):
        create_members_table()
    members = get_members_list()
    update_table( members )

    send_groupme_message( "Retrieved all group members" )

    return True

def update_table( members ):
    conn = get_db_connection()
    cursor = conn.cursor()
    for member in members:
        member_id = member["user_id"]
        member_name = member["nickname"]
        cursor.execute( "SELECT COUNT(*) FROM tb_members where user_id='" + member_id + "';" )
        rows = cursor.fetchall()
        count = rows[0][0]
        if( count == 0 ):
            # When the first update is called we want to automatically make the owner an admin
            if( os.getenv( "OWNER" ) == member['nickname'] ):
                cursor.execute( "INSERT INTO tb_members( nickname, user_id, is_admin, kicked, warnings ) VALUES ( " + "'" + member['nickname'] + "'" + ", " + member['user_id'] + ", True, NULL, 0 );" )
            else:
                cursor.execute( "INSERT INTO tb_members( nickname, user_id, is_admin, kicked, warnings ) VALUES ( " + "'" + member['nickname'] + "'" + ", " + member['user_id'] + ", False, NULL, 0 );" )
    conn.commit()
    cursor.close()
    conn.close()

    send_groupme_message( "Members successfully updated." )

def get_members_list():
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

# def is_group_members_table_empty():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT count(*) FROM tb_members")
#     rows = cursor.fetchall()
#     cursor.close()
#     conn.close()

#     if( rows[0][0] == 0 ):
#         return True

#     return False

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

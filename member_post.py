import emoji

from send_message import send_groupme_message
from db_connection import get_db_connection

def check_if_member_is_admin( member_id ):
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

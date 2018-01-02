from db_connection import get_db_connection
from send_message import send_groupme_message

def pardon( member ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where nickname='" + member + "';" )
    rows = cursor.fetchall()
    if( rows[0][0] != 0 ):
        cursor.execute( "SELECT * FROM tb_members where nickname='" + member + "';" )
        rows = cursor.fetchall()
        is_admin = rows[0][3]
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

from db_connection import get_db_connection

def check_if_member_exists_by_name( member_name ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where nickname='" + member_name + "';" )
    rows = cursor.fetchall()
    if( rows[0][0] != 0 ):
        return True
    else:
        return False
    cursor.close()
    conn.close()

def change_member_name( name_before, name_after ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "UPDATE tb_members set nickname='" + name_after + "' WHERE nickname='" + name_before + "';" )
    cursor.close()
    conn.commit()
    conn.close()

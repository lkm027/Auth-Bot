import os

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

def check_if_member_exists_by_id( member_id ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    count = rows[0][0]
    if( count != 0 ):
        return True
    return False

def change_member_name( name_before, name_after ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "UPDATE tb_members set nickname='" + name_after + "' WHERE nickname='" + name_before + "';" )
    cursor.close()
    conn.commit()
    conn.close()

def is_member_admin( member_id ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    if( rows[0][0] != 0 ):
        cursor.execute( "SELECT * FROM tb_members where user_id='" + member_id + "';" )
        rows = cursor.fetchall()
        is_admin = rows[0][3]
        if( is_admin ):
            return True
        return False
    else:
        print( "Request user was not within the database" )
    cursor.close()
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

def save_member_to_db( member_name, member_id ):
    conn = get_db_connection()
    cursor = conn.cursor()
    if( os.getenv( "OWNER" ) == member_name ):
        cursor.execute( "INSERT INTO tb_members( nickname, user_id, is_admin, kicked, warnings ) VALUES ( " + "'" + member_name + "'" + ", " + member_id + ", True, NULL, 0 );" )
    else:
        cursor.execute( "INSERT INTO tb_members( nickname, user_id, is_admin, kicked, warnings ) VALUES ( " + "'" + member_name + "'" + ", " + member_id + ", False, NULL, 0 );" )
    conn.commit()
    cursor.close()
    conn.close()

def add_warning_to_member( member_id ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][5] + 1
    cursor.execute( "UPDATE tb_members set warnings=" + str( warnings_count ) + " where user_id='" + member_id + "';" )

    conn.commit()
    cursor.close()
    conn.close()

def remove_warning_from_member( member_name ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE nickname='" + member_name + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][5] - 1
    cursor.execute( "UPDATE tb_members set warnings=" + str( warnings_count ) + " where nickname='" + member_name + "';" )

    conn.commit()
    cursor.close()
    conn.close()

def get_warnings_count_by_id( member_id ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][5]
    cursor.close()
    conn.close()
    return warnings_count

def get_warnings_count_by_name( member_name ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE nickname='" + member_name + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][5]
    cursor.close()
    conn.close()
    return warnings_count

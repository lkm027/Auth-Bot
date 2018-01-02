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

def is_member_admin( member ):
    # This should only be called if we haven't created a table yet. This allows anyone to create a command while no table exists.
    # TODO The table check and creation could probably be exported to occur right when the bot starts up to prevent multiple calls
    if( not check_if_member_table_exists() ):
        return True
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where nickname='" + member + "';" )
    rows = cursor.fetchall()
    if( rows[0][0] != 0 ):
        cursor.execute( "SELECT * FROM tb_members where nickname='" + member + "';" )
        rows = cursor.fetchall()
        is_admin = rows[0][3]
        if( is_admin ):
            return True
        return False
    else:
        print( "The user before does not exist within the database." )
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
    if( os.getenv( "OWNER" ) == member['nickname'] ):
        cursor.execute( "INSERT INTO tb_members( nickname, user_id, is_admin, kicked, warnings ) VALUES ( " + "'" + member['nickname'] + "'" + ", " + member['user_id'] + ", True, NULL, 0 );" )
    else:
        cursor.execute( "INSERT INTO tb_members( nickname, user_id, is_admin, kicked, warnings ) VALUES ( " + "'" + member['nickname'] + "'" + ", " + member['user_id'] + ", False, NULL, 0 );" )
    conn.commit()
    cursor.close()
    conn.close()

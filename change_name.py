import os

from db_connection import get_db_connection

def change_name( name_before, name_after ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where nickname='" + name_before + "';" )
    rows = cursor.fetchall()
    if( rows[0][0] != 0 ):
        change_db_name_entry( name_before, name_after )
    else:
        print( "The user before does not exist within the database." )
    cursor.close()
    conn.close()

def change_db_name_entry( name_before, name_after ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "UPDATE tb_members set nickname='" + name_after + "' WHERE nickname='" + name_before + "';" )
    cursor.close()
    conn.commit()
    conn.close()

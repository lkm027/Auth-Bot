import os

import db.db_connection as db_conn

def check_if_member_exists_by_name( member_name ):
    conn = db_conn.get_db_connection()
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
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    count = rows[0][0]
    if( count != 0 ):
        return True
    return False

def change_member_name( name_before, name_after ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "UPDATE tb_members set nickname='" + name_after + "' WHERE nickname='" + name_before + "';" )
    cursor.close()
    conn.commit()
    conn.close()

# Check if the given member is an admin within the group
def is_member_admin( member_id ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members where user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    if( rows[0][0] != 0 ):
        cursor.execute( "SELECT * FROM tb_members where user_id='" + member_id + "';" )
        rows = cursor.fetchall()
        is_admin = rows[0][4]
        if( is_admin ):
            return True
        return False
    else:
        print( "Request user was not within the database" )
    cursor.close()
    conn.close()

def create_members_table():
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( """CREATE TABLE tb_members
                        ( id SERIAL PRIMARY KEY,
                          nickname TEXT,
                          user_id VARCHAR(80),
                          member_id VARCHAR(80),
                          is_admin BOOLEAN,
                          kicked DATE,
                          warnings INTEGER );""" )

    cursor.close()
    conn.commit()
    conn.close()

def check_if_member_table_exists():
    conn = db_conn.get_db_connection()
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

# Check if there exist any members in our table
def members_are_in_db():
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT COUNT(*) FROM tb_members;" )
    rows = cursor.fetchall()
    count = rows[0][0]
    if( count != 0 ):
        return True
    return False

# Add another member entry into our db
def save_member_to_db( member_name, user_id, member_id ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    if( os.getenv( "OWNER" ) == member_name ):
        cursor.execute( "INSERT INTO tb_members( nickname, user_id, member_id, is_admin, kicked, warnings ) VALUES ( " + "'" + member_name + "'" + ", " + user_id + ", " + member_id + ", True, NULL, 0 );" )
    else:
        cursor.execute( "INSERT INTO tb_members( nickname, user_id, member_id, is_admin, kicked, warnings ) VALUES ( " + "'" + member_name + "'" + ", " + user_id + ", " + member_id + ", False, NULL, 0 );" )
    conn.commit()
    cursor.close()
    conn.close()

def add_new_warning_to_member( member_id ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][6] + 1
    cursor.execute( "UPDATE tb_members set warnings=" + str( warnings_count ) + " where user_id='" + member_id + "';" )

    conn.commit()
    cursor.close()
    conn.close()

def remove_warning_from_member( member_name ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE nickname='" + member_name + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][6] - 1
    cursor.execute( "UPDATE tb_members set warnings=" + str( warnings_count ) + " where nickname='" + member_name + "';" )

    conn.commit()
    cursor.close()
    conn.close()

def get_warnings_count_by_id( member_id ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE user_id='" + member_id + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][6]
    cursor.close()
    conn.close()
    return warnings_count

def get_warnings_count_by_name( member_name ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE nickname='" + member_name + "';" )
    rows = cursor.fetchall()
    warnings_count = rows[0][6]
    cursor.close()
    conn.close()
    return warnings_count

# Delete all members from our members table
def drop_all_members():
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "DELETE FROM tb_members;" )
    conn.commit()
    cursor.close()
    conn.close()

def make_member_admin( member_name ):
    if( not check_if_member_exists_by_name( member_name ) ):
        return False
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "UPDATE tb_members set is_admin=True WHERE nickname='" + member_name + "';" )
    conn.commit()
    cursor.close()
    conn.close()
    return True

def get_member_user_id( member_name ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members where nickname='" + member_name + "';" )
    rows = cursor.fetchall()
    user_id = rows[0][2]
    return user_id

def get_member_member_id( user_id ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members where user_id='" + user_id + "';" )
    rows = cursor.fetchall()
    member_id = rows[0][3]
    return member_id

# year month date
def set_kick_date_for_member( user_id, date ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "UPDATE tb_members set kicked='" + date + "' where user_id='" + user_id + "';" )
    conn.commit()
    cursor.close()
    conn.close()

def get_kicked_members( current_date ):
    conn = db_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members where kicked <= '" + current_date + "';" )
    kicked_users = cursor.fetchall()
    kicked_names = []
    print( "Printing names" )
    for member in kicked_users:
        kicked_names.append( member[1] )
    cursor.close()
    conn.close()
    print( kicked_names )

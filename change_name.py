import os
import psycopg2

from urllib import parse

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
    cursor.commit()
    cursor.close()
    conn.close()

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

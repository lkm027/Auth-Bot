import os
import psycopg2

from urllib import parse

def check_if_member_is_admin( member ):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM tb_members WHERE nickname='" + member + "';" )
    rows = cursor.fetchall()
    print( rows[0] )
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

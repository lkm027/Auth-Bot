import os
import json
import psycopg2

from urllib import parse
from flask import Flask, request

from send_message import send_groupme_message

app = Flask(__name__)

@app.route( '/', methods=['POST'] )
def webhook():
    data = request.get_json()

    # We don't want to reply do ourselves!
    if( data['name'] != 'Auth Bot'):
        if( data["text"] == "Get members" ):
            send_message( "Not yet peasant" )

    return "ok", 200


# try:
#     parse.uses_netloc.append("postgres")
#     url = parse.urlparse(os.environ["DATABASE_URL"])

#     conn = psycopg2.connect(
#         database=url.path[1:],
#         user=url.username,
#         password=url.password,
#         host=url.hostname,
#         port=url.port
#     )

#     cursor = conn.cursor()
#     cursor.execute("""SELECT * FROM EXAMPLE""")
#     rows = cursor.fetchall()
#     for row in rows:
#         send_groupme_message( row[1] )
# except Exception as e:
#     send_message( e )

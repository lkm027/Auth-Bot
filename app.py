import os
import json
import psycopg2

from flask import Flask, request
from group_members import check_and_add_members_if_none_exist


app = Flask(__name__)

@app.route( '/', methods=['POST'] )
def webhook():
    data = request.get_json()

    # We don't want to reply do ourselves!
    if( data['name'] != 'Auth Bot'):
        if( data["text"] == "Add members" ):
            check_and_add_members_if_none_exist()

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

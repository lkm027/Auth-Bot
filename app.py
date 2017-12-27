import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

# @app.route( '/', methods=['POST'] )
# def webhook():
#     data = request.get_json()

#     # We don't want to reply do ourselves!
#     if( data['name'] != 'Auth Bot'):
#         send_message( 'Hey' )

#     return "ok", 200

def send_message( msg ):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
            'bot_id' : os.getenv( 'GROUPME_BOT_ID'),
            'text'   : msg,
            }
    request = Request( url, urlencode( data ).encode() )
    json = urlopen( request ).read().decode()


send_message( 'Hello, I am a new bot' )

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
#         send_message( row[1] )
# except Exception as e:
#     send_message( e )

import json

from flask import Flask, request
# from urllib import parse
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import os
# import psycopg2

app = Flask(__name__)

# @app.route( '/', methods=['POST'] )
# def webhook():
#     data = request.get_json()

#     # We don't want to reply do ourselves!
#     if( data['name'] != 'Real bot'):
#         phrase = data['text']
#         location = check_if_im_is_used_and_get_position( phrase )
#         if( location == -1 ):
#             location = check_if_i_am_is_used_and_get_position( phrase )
#         if( location is not -1 ):
#             words = str.split( phrase )
#             if( location + 1 < len( words ) ):
#                 if( location + 2 < len( words ) ):
#                     check_if_words_can_be_repeated( words[ location + 1 ], words[ location + 2 ] )
#                 else:
#                     check_if_words_can_be_repeated( words[ location + 1 ], '' )

#     return "ok", 200

def send_message( msg ):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
            'bot_id' : os.getenv( 'GROUPME_BOT_ID'),
            'text'   : msg,
            }
    request = Request( url, urlencode( data ).encode() )
    json = urlopen( request ).read().decode()

print( "Hello I am here" )
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

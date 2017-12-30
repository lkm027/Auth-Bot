import os
import json
import psycopg2

from flask import Flask, request

from commands import check_all_commands

app = Flask(__name__)

@app.route( '/', methods=['POST'] )
def webhook():
    data = request.get_json()

    # We don't want to reply do ourselves!
    if( data['name'] != os.getenv( "BOT_NAME" ) ):
        words = str.split( data["text"] )
        print( words[0] )
        print( words[1] )
        if( words[0].lower() == "@Auth" and words[1].lower() == "Bot" ):
            check_all_commands( data["text"] )

    return "ok", 200

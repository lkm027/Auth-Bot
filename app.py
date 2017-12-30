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
        if( words[0].lower() == "@auth" and words[1].lower() == "bot" ):
            check_all_commands( data["text"] )

    if( data['name'] == "GroupMe" ):
        phrase = data["text"]
        if( "changed name to" in phrase ):
            words = str.split( phrase )
            last_index = 0
            for index, word in enumerate( words ):
                if( word == "changed" ):
                    last_index = index
                    break
            name_before_change = " ".join( words[:last_index] )
            print( name_before_change )


    return "ok", 200

import os
import json
import psycopg2

from flask import Flask, request

from commands import check_all_commands
# from change_name import change_name

app = Flask(__name__)

@app.route( '/', methods=['POST'] )
def webhook():
    data = request.get_json()

    # We don't want to reply do ourselves!
    if( data['name'] != os.getenv( "BOT_NAME" ) ):
        words = str.split( data["text"] )
        if( words[0].lower() == "@auth" and words[1].lower() == "bot" ):
            check_all_commands( data["text"] )

    # As of now this path is only if someone changes their name. We want to update their name in our db so that we can easily find them later
    if( data['name'] == "GroupMe" ):
        phrase = data["text"]
        if( "changed name to" in phrase ):
            words = str.split( phrase )
            last_index = 0
            for index, word in enumerate( words ):
                if( word == "changed" ):
                    changed_index = index
                    break
            to_index = changed_index + 3
            name_before_change = " ".join( words[:changed_index] )
            name_after_change  = " ".join( words[to_index:] )
            change_name( name_before_change, name_after_change )

    return "ok", 200

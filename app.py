import os
import json
import psycopg2

from flask import Flask, request

from commands import check_all_commands
from change_name import change_name_if_it_exists
from member_post import add_warning_to_member
from db_requests import check_if_member_table_exists, create_members_table, is_member_admin
from group_members import update_members_list

app = Flask(__name__)

@app.route( '/', methods=['POST'] )
def webhook():

    # We should first check if our table exists before doing anything
    if( not check_if_member_table_exists() ):
        create_members_table()
        update_members_list()

    data = request.get_json()

    # We don't want to reply do ourselves!
    if( data['name'] != os.getenv( "BOT_NAME" ) and not data["name"] == "GroupMe" ):

        # Add warning to user if they are not an admin
        if( not is_member_admin( data['user_id'] ) ):
            add_warning_to_member( data['user_id'], data['name'] )

        words = str.split( data["text"] )
        if( words[0].lower() == "@auth" and words[1].lower() == "bot" ):
            check_all_commands( data["text"], data["name"] )
    # While this operation is currently not necesarry, I am going to keep it for now. It can, however be sped up and optimized
    # TODO Optimize this method to not worry about the user's original name. All we really need is their user_id and the name they change to.
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
            change_name_if_it_exists( name_before_change, name_after_change )

    return "ok", 200

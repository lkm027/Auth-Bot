from send_message import send_groupme_message
from group_members import check_and_add_members_if_none_exist

def check_all_commands( command ):
    command.lower()
    return {
            "retrieve members" : retrieve_members()
            }.get( command, send_groupme_message( "That command does not exist" )

def retrieve_members():
    check_and_add_members_if_none_exist()


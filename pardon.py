from send_message import send_groupme_message
import db.db_requests

def pardon( member_name ):
    if( db_requests.check_if_member_exists_by_name( member_name ) ):
        db_requests.remove_warning_from_member( member_name )
        db_requests.warnings_count = get_warnings_count_by_name( member_name )
        send_groupme_message( "Congrats " + member_name + "! You have been pardon by the almighty overlords. Your current warning count: " + str( warnings_count ) + "." )

from send_message import send_groupme_message
from db_requests import check_if_member_exists_by_name, remove_warning_from_member, get_warnings_count_by_name

def pardon( member_name ):
    if( check_if_member_exists_by_name( member_name ) ):
        remove_warning_from_member( member_name )
        warnings_count = get_warnings_count_by_name( member_name )
        send_groupme_message( "Congrats " + member_name + "! You have been pardon by the almighty overlords. Your current warning count: " + str( warnings_count ) + "." )

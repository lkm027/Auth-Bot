import emoji

from send_message import send_groupme_message
import db.db_requests

def add_warning_to_member( member_id, member_name ):
    db_requests.add_new_warning_to_member( member_id )
    db_requests.warnings_count = get_warnings_count_by_id( member_id )
    send_groupme_message( emoji.emojize( member_name + ", you will be kicked on your 3rd warning. Please do not post again.\n:police_car_light: Your warning count: " + str( warnings_count ) + " :police_car_light:" ) )

import db.db_requests

def change_name_if_it_exists( name_before, name_after ):
    if( db_requests.check_if_member_exists_by_name( name_before ) ):
        db_requests.change_member_name( name_before, name_after )

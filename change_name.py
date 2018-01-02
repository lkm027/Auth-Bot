import os

from db_requests import check_if_member_exists_by_name, change_member_name

def change_name_if_it_exists( name_before, name_after ):
    if( check_if_member_exists_by_name( name_before ) ):
        change_member_name( name_before, name_after )

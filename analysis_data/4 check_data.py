# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from utils import read_PKL, save_PKL, check_data, attr_to_float

if __name__ == '__main__':
    G, M, E, R, V = read_PKL(G=True, M=True, E=True, R=True, V=True)
    for D in [G, M, E, R, V]:
        check_data(D)

"""Out[0]
{'state': <class 'int'>, 'category': <class 'int'>, 'description': <class 'int'>, 'rating': <class 'float'>, 'join_mode': <class 'int'>, 'created': <class 'float'>, 'lat': <class 'float'>, 'topics': <class 'list'>, 'members': <class 'float'>, 'organizer': <class 'str'>, 'group_photo': <class 'bool'>, 'lon': <class 'float'>, 'has_description': <class 'bool'>, 'timezone': <class 'int'>, 'rsvp_id_list': <class 'list'>, 'member_list': <class 'list'>, 'event_list': <class 'list'>}
set()

{'photo': <class 'bool'>, 'state': <class 'int'>, 'joined': <class 'float'>, 'lat': <class 'float'>, 'topics': <class 'list'>, 'lang': <class 'int'>, 'country': <class 'int'>, 'other_services': <class 'int'>, 'visited': <class 'float'>, 'lon': <class 'float'>, 'bio': <class 'int'>, 'has_bio': <class 'bool'>, 'has_other_services': <class 'bool'>, 'rsvp_id_list': <class 'list'>, 'group_list': <class 'list'>, 'event_list': <class 'list'>}
set()

{'venue': <class 'str'>, 'description': <class 'int'>, 'event_hosts': <class 'list'>, 'maybe_rsvp_count': <class 'float'>, 'waitlist_count': <class 'float'>, 'updated': <class 'float'>, 'group': <class 'str'>, 'yes_rsvp_count': <class 'float'>, 'created': <class 'float'>, 'headcount': <class 'float'>, 'utc_offset': <class 'float'>, 'time': <class 'float'>, 'photo_url': <class 'bool'>, 'rating_average': <class 'float'>, 'rating_count': <class 'float'>, 'why': <class 'int'>, 'has_why': <class 'bool'>, 'has_description': <class 'bool'>, 'how_to_find_us': <class 'int'>, 'has_how_to_find_us': <class 'bool'>, 'duration': <class 'float'>, 'rsvp_limit': <class 'float'>, 'fee_amount': <class 'float'>, 'fee_accepts': <class 'int'>, 'fee_currency': <class 'int'>, 'fee_required': <class 'int'>, 'rsvp_id_list': <class 'list'>, 'tallies_no': <class 'float'>, 'tallies_waitlist': <class 'float'>, 'tallies_yes': <class 'float'>, 'tallies_maybe': <class 'float'>, 'member_list': <class 'list'>}
{'event_hosts', 'venue'}

{'response': <class 'int'>, 'mtime': <class 'float'>, 'event': <class 'str'>, 'comments': <class 'int'>, 'group': <class 'str'>, 'created': <class 'float'>, 'member_photo': <class 'bool'>, 'member': <class 'str'>, 'guests': <class 'float'>, 'has_comments': <class 'bool'>}
set()

{'state': <class 'int'>, 'lat': <class 'float'>, 'repinned': <class 'bool'>, 'country': <class 'int'>, 'lon': <class 'float'>}
set()
"""

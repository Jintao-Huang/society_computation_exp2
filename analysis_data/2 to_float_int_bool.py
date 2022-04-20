# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from utils import attr_to_bool, attr_to_float, attr_to_len, \
    read_PKL, attr_to_int, default_using_median, remove_attr, save_PKL

ALL = {"M", "G", "E", "R", "V"}
TASK = ALL

if "M" in TASK:
    M = read_PKL(M=True)
    attr_to_bool(M, ["photo"])
    attr_to_len(M, ["bio", "other_services"])
    attr_to_float(M, ["joined", "lat", "visited", "lon"])
    attr_to_int(M, ["hometown", "state", "country", "city", "lang"])
    # topics
    save_PKL(M=M)

if "G" in TASK:
    G = read_PKL(G=True)
    remove_attr(G, ["city"])  # 100-1000
    attr_to_bool(G, ["group_photo"])
    attr_to_len(G, ["description"])
    attr_to_float(G, ["rating", "created", "lat", "members", "lon"])
    attr_to_int(G, ["timezone", "category", "state", "join_mode",
                    "visibility", "country"])
    # topics, organizer
    save_PKL(G=G)

if "E" in TASK:
    E = read_PKL(E=True)
    attr_to_bool(E, ["photo_url"])
    remove_attr(E, ["fee_label", "fee_description"])  # 100-1000
    default_using_median(E, ["duration"])
    attr_to_float(E, ["rsvp_limit"], [1000])
    attr_to_float(E, ["fee_amount", "maybe_rsvp_count", "waitlist_count", "updated", "yes_rsvp_count",
                      "created", "headcount", "utc_offset", "time", "rating_average", "rating_count"])
    attr_to_len(E, ["why", "description", "how_to_find_us"])
    attr_to_int(E, ["fee_accepts", "fee_currency", "fee_required", "visibility", "status"])
    # venue, event_hosts, group
    save_PKL(E=E)

if "R" in TASK:
    R = read_PKL(R=True)
    attr_to_bool(R, ["member_photo"])
    attr_to_len(R, ["comments"])
    attr_to_float(R, ["tallies_waitlist", "tallies_maybe", "tallies_no", "tallies_yes",
                      "mtime", "created", "guests"])
    attr_to_int(R, ["response"])
    # venue, event, group, member
    save_PKL(R=R)

if "V" in TASK:
    V = read_PKL(V=True)
    attr_to_bool(V, ["repinned"])
    attr_to_float(V, ["lat", "lon"])
    attr_to_int(V, ["state", "city", "country"])
    save_PKL(V=V)


"""Out[0]
hometown: 5220, remove
state: 91
country: 87
city: 2006, remove
lang: 6
exist_ok? y/ny
File exist, covered

timezone: 2
category: 34
state: 7
join_mode: 3
visibility: 1, remove
country: 1, remove
exist_ok? y/ny
File exist, covered

fee_accepts: 4
fee_currency: 6
fee_required: 3
visibility: 1, remove
status: 1, remove
exist_ok? y/ny
File exist, covered

response: 3
exist_ok? y/ny
File exist, covered

state: 36
city: 1255, remove
country: 9
exist_ok? y/ny
File exist, covered
"""
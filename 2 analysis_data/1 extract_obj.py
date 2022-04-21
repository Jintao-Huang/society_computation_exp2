# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

"""OBJ
M:
1. 'self': remove
2. 'other_services': len
3. 'photo': bool
4. 'topics': List[id]


G:
1. 'category': id
2. 'organizer': id
3. 'group_photo': bool
4. 'topics': List[id]


E:
1. 'rating': 2*float
2. 'fee': *解开
3 'event_hosts': List[id]
4. 'venue': id
5. 'group': id

R:
1. 'tallies'. 4*float
2. 'venue'. id
3. 'event'. id
4. 'group'. id
5. 'member_photo'. bool
6. 'member'. id
"""

from utils import read_PKL, save_PKL, attr_to_bool, attr_to_len, remove_attr, count_key, \
    topics_to_idlist, attr_to_id, eventhosts_to_idlist, unzip_attr, print_dict

ALL = {"M", "G", "E", "R", "V"}
TASK = ALL

# M:
# 1. 'self': remove
# 2. 'other_services': len
# 3. 'photo': bool
# 4. 'topics': List[id]
if "M" in TASK:
    M = read_PKL(M=True)
    remove_attr(M, ["self", "name", "id", "link"])
    attr_to_len(M, ["bio", "other_services"])
    attr_to_bool(M, ["photo"])
    topics_to_idlist(M)
    cnt, obj_set = count_key(M)
    print(obj_set)
    print_dict(cnt)
    save_PKL(M=M)

# G:
# 1. 'category': id
# 2. 'organizer': id
# 3. 'group_photo': bool
# 4. 'topics': List[id]
if "G" in TASK:
    G = read_PKL(G=True)
    attr_to_id(G, "category")
    attr_to_id(G, "organizer", "member_id")
    attr_to_len(G, ["description"])
    attr_to_bool(G, ["group_photo"])
    remove_attr(G, ["who", "name", "id", "link", "urlname"])
    topics_to_idlist(G)
    cnt, obj_set = count_key(G)
    print(obj_set)
    print_dict(cnt)
    save_PKL(G=G)

# E:
# 1. 'rating': 2*float
# 2. 'fee': *解开
# 3 'event_hosts': List[id]
# 4. 'venue': id
# 5. 'group': id
if "E" in TASK:
    E = read_PKL(E=True)
    unzip_attr(E, "rating")
    unzip_attr(E, "fee")
    eventhosts_to_idlist(E)
    attr_to_id(E, "venue", "id")
    attr_to_id(E, "group", "id")
    #
    attr_to_len(E, ["why", "description", "how_to_find_us"])
    attr_to_bool(E, ["photo_url"])
    remove_attr(E, ["event_url", "id", "name"])
    #
    cnt, obj_set = count_key(E)
    print(obj_set)
    print_dict(cnt)
    save_PKL(E=E)

# R:
# 1. 'tallies'. 4*float
# 2. 'venue'. id
# 3. 'event'. id
# 4. 'group'. id
# 5. 'member_photo'. bool
# 6. 'member'. id
if "R" in TASK:
    R = read_PKL(R=True)
    unzip_attr(R, "tallies")
    attr_to_id(R, "venue", "id")
    attr_to_id(R, "event", "id")
    attr_to_id(R, "group", "id")
    attr_to_id(R, "member", "member_id")
    #
    attr_to_bool(R, ["member_photo"])
    attr_to_len(R, ["comments"])
    remove_attr(R, ["rsvp_id"])
    #
    cnt, obj_set = count_key(R)
    print(obj_set)
    print_dict(cnt)
    save_PKL(R=R)

if "V" in TASK:
    V = read_PKL(V=True)
    remove_attr(V, ["name", "id", "address_1", "address_2", "address_3", "phone", "zip", "id"])
    attr_to_bool(V, ["repinned"])
    #
    cnt, obj_set = count_key(V)
    print(obj_set)
    print_dict(cnt)
    save_PKL(V=V)

"""Out[0]
set()
len(cnt): 15
cnt[hometown]=27204
cnt[state]=82303
cnt[country]=82748
cnt[city]=82748
cnt[photo]=82770
cnt[joined]=82770
cnt[lat]=82770
cnt[topics]=82770
cnt[lang]=82770
cnt[other_services]=82770
cnt[visited]=82770
cnt[lon]=82770
cnt[bio]=82770
cnt[has_bio]=82770
cnt[has_other_services]=82770

exist_ok? y/ny
File exist, covered

set()
len(cnt): 17
cnt[timezone]=77
cnt[category]=782
cnt[state]=783
cnt[description]=783
cnt[rating]=783
cnt[join_mode]=783
cnt[created]=783
cnt[lat]=783
cnt[visibility]=783
cnt[topics]=783
cnt[members]=783
cnt[country]=783
cnt[organizer]=783
cnt[group_photo]=783
cnt[city]=783
cnt[lon]=783
cnt[has_description]=783

exist_ok? y/ny
File exist, covered

set()
len(cnt): 30
cnt[duration]=5180
cnt[fee_label]=15062
cnt[fee_accepts]=15062
cnt[fee_currency]=15062
cnt[fee_description]=15062
cnt[fee_amount]=15062
cnt[fee_required]=15062
cnt[rsvp_limit]=26812
cnt[venue]=66179
cnt[event_hosts]=83430
cnt[status]=93512
cnt[description]=93512
cnt[maybe_rsvp_count]=93512
cnt[waitlist_count]=93512
cnt[updated]=93512
cnt[group]=93512
cnt[yes_rsvp_count]=93512
cnt[created]=93512
cnt[visibility]=93512
cnt[headcount]=93512
cnt[utc_offset]=93512
cnt[time]=93512
cnt[photo_url]=93512
cnt[rating_average]=93512
cnt[rating_count]=93512
cnt[why]=93512
cnt[has_why]=93512
cnt[has_description]=93512
cnt[how_to_find_us]=93512
cnt[has_how_to_find_us]=93512

exist_ok? y/ny
File exist, covered

set()
len(cnt): 15
cnt[venue]=545043
cnt[tallies_waitlist]=765316
cnt[tallies_maybe]=765316
cnt[tallies_no]=765316
cnt[tallies_yes]=765316
cnt[response]=765317
cnt[mtime]=765317
cnt[event]=765317
cnt[comments]=765317
cnt[group]=765317
cnt[created]=765317
cnt[member_photo]=765317
cnt[member]=765317
cnt[guests]=765317
cnt[has_comments]=765317

exist_ok? y/ny
File exist, covered

set()
len(cnt): 6
cnt[state]=14089
cnt[city]=14094
cnt[country]=14099
cnt[lat]=14108
cnt[repinned]=14108
cnt[lon]=14108

exist_ok? y/ny
File exist, covered
"""

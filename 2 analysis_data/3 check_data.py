# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# 分析字段的数量:
# int: ont_hot; bool, float: 不变.
from typing import Dict
from utils import read_PKL, count_key, print_dict

ALL = {"M", "G", "E", "R", "T", "V"}
TASK = ALL

if "M" in TASK:
    M = read_PKL(M=True)  # type: Dict
    cnt, obj_set = count_key(M)
    print(f"len(M): {len(M)}")
    print(f"obj_set: {obj_set}")
    print_dict(cnt)

if "G" in TASK:
    G = read_PKL(G=True)  # type: Dict
    cnt, obj_set = count_key(G)
    print(f"obj_set: {obj_set}")
    print(f"len(G): {len(G)}")
    print_dict(cnt)

if "E" in TASK:
    E = read_PKL(E=True)  # type: Dict
    cnt, obj_set = count_key(E)
    print(f"obj_set: {obj_set}")
    print(f"len(E): {len(E)}")
    print_dict(cnt)

if "R" in TASK:
    R = read_PKL(R=True)  # type: Dict
    cnt, obj_set = count_key(R)
    print(f"obj_set: {obj_set}")
    print(f"len(R): {len(R)}")
    print_dict(cnt)

if "T" in TASK:
    T = read_PKL(T=True)  # type: Dict
    cnt, obj_set = count_key(T)
    print(f"obj_set: {obj_set}")
    print(f"len(T): {len(T)}")
    print_dict(cnt)

if "V" in TASK:
    V = read_PKL(V=True)  # type: Dict
    cnt, obj_set = count_key(V)
    print(f"obj_set: {obj_set}")
    print(f"len(V): {len(V)}")
    print_dict(cnt)


"""Out[0]
len(M): 82770
obj_set: set()
len(cnt): 13
cnt[photo]=82770
cnt[state]=82770
cnt[joined]=82770
cnt[lat]=82770
cnt[topics]=82770
cnt[lang]=82770
cnt[country]=82770
cnt[other_services]=82770
cnt[visited]=82770
cnt[lon]=82770
cnt[bio]=82770
cnt[has_bio]=82770
cnt[has_other_services]=82770

obj_set: set()
len(G): 783
len(cnt): 14
cnt[state]=783
cnt[category]=783
cnt[description]=783
cnt[rating]=783
cnt[join_mode]=783
cnt[created]=783
cnt[lat]=783
cnt[topics]=783
cnt[members]=783
cnt[organizer]=783
cnt[group_photo]=783
cnt[lon]=783
cnt[has_description]=783
cnt[timezone]=783

obj_set: set()
len(E): 93512
len(cnt): 26
cnt[venue]=66179
cnt[event_hosts]=83430
cnt[description]=93512
cnt[maybe_rsvp_count]=93512
cnt[waitlist_count]=93512
cnt[updated]=93512
cnt[group]=93512
cnt[yes_rsvp_count]=93512
cnt[created]=93512
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
cnt[duration]=93512
cnt[rsvp_limit]=93512
cnt[fee_amount]=93512
cnt[fee_accepts]=93512
cnt[fee_currency]=93512
cnt[fee_required]=93512

obj_set: set()
len(R): 765317
len(cnt): 15
cnt[venue]=545043
cnt[response]=765317
cnt[mtime]=765317
cnt[event]=765317
cnt[comments]=765317
cnt[group]=765317
cnt[created]=765317
cnt[member_photo]=765317
cnt[member]=765317
cnt[guests]=765317
cnt[tallies_waitlist]=765317
cnt[tallies_maybe]=765317
cnt[tallies_no]=765317
cnt[tallies_yes]=765317
cnt[has_comments]=765317

obj_set: set()
len(T): 18114
len(cnt): 3
cnt[id]=18114
cnt[urlkey]=18114
cnt[name]=18114

obj_set: set()
len(V): 14108
len(cnt): 5
cnt[state]=14108
cnt[lat]=14108
cnt[repinned]=14108
cnt[country]=14108
cnt[lon]=14108
"""
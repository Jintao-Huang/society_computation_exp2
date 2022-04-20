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
cnt[lang]=504. int
cnt[other_services]=12762. int
cnt[has_other_services]=12762. bool 
cnt[bio]=14790. int
cnt[has_bio]=14790. bool
cnt[topics]=53085. List
cnt[photo]=62128. bool
cnt[state]=82303. int
cnt[lat]=82747. float
cnt[lon]=82747. float
cnt[country]=82748. int
cnt[joined]=82770. float
cnt[visited]=82770. float

obj_set: set()
len(G): 783
len(cnt): 14
cnt[timezone]=77. int
cnt[join_mode]=102. int
cnt[state]=228. int
cnt[group_photo]=746. bool
cnt[rating]=767. float
cnt[description]=776. int
cnt[has_description]=776. bool
cnt[category]=782. int
cnt[created]=783. float
cnt[lat]=783. float
cnt[topics]=783. List
cnt[members]=783. float
cnt[organizer]=783. -
cnt[lon]=783. float

obj_set: set()
len(E): 93512
len(cnt): 26
cnt[waitlist_count]=2333. float
cnt[why]=5355. float
cnt[has_why]=5355. bool
cnt[fee_amount]=15062. float
cnt[fee_accepts]=15062. int
cnt[fee_currency]=15062. int
cnt[fee_required]=15062. int
cnt[maybe_rsvp_count]=25121. float
cnt[photo_url]=28450. bool
cnt[how_to_find_us]=43810. float
cnt[has_how_to_find_us]=43810. bool
cnt[headcount]=55030. float
cnt[rating_average]=65212. float
cnt[rating_count]=65212. float
cnt[venue]=66179. -
cnt[event_hosts]=83430. List
cnt[description]=90825. float
cnt[has_description]=90825. bool
cnt[updated]=93512. float
cnt[group]=93512. -
cnt[yes_rsvp_count]=93512. float
cnt[created]=93512. float
cnt[utc_offset]=93512. float
cnt[time]=93512. float
cnt[duration]=93512. float
cnt[rsvp_limit]=93512. float

obj_set: set()
len(R): 765317
len(cnt): 15
cnt[tallies_waitlist]=0. float
cnt[guests]=47877. float
cnt[comments]=139402. float
cnt[has_comments]=139402. bool
cnt[tallies_maybe]=209735. float
cnt[response]=443487. int
cnt[venue]=545043. -
cnt[member_photo]=667529. bool
cnt[tallies_no]=738322. float
cnt[tallies_yes]=765316. float
cnt[mtime]=765317. float
cnt[event]=765317. -
cnt[group]=765317. -
cnt[created]=765317. float
cnt[member]=765317. -

obj_set: set()
len(T): 18114
len(cnt): 3
cnt[id]=18114
cnt[urlkey]=18114
cnt[name]=18114

obj_set: set()
len(V): 14108
len(cnt): 5
cnt[repinned]=562. bool
cnt[state]=14089. int
cnt[lat]=14095. float
cnt[lon]=14095. float
cnt[country]=14099. int
"""
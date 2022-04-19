# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# 分析字段的数量:
# int: ont_hot; bool, float: 不变.
from typing import Dict
from utils import read_PKL, count_key, print_dict

ALL = {"M", "G", "E", "R", "T", "V"}
TASK = {"T", "V"}

if "M" in TASK:
    M = read_PKL(M=True)  # type: Dict
    cnt, obj_set = count_key(M)
    print(f"len(M): {len(M)}")
    print(f"obj_set: {obj_set}")
    print_dict(cnt)

"""Out[0]. 这里不进行归一化处理. 后面统一处理.
len(M): 82770
obj_set: set()
len(cnt): 13
cnt[other_services]=12762. float
cnt[bio]=14790. float
cnt[hometown]=27204. int
cnt[topics]=53085. List->int
cnt[photo]=62128. bool
cnt[state]=82303. int
cnt[country]=82748. int
cnt[city]=82748. int
cnt[joined]=82770. float
cnt[lat]=82770. float
cnt[lang]=82770. int
cnt[visited]=82770. float
cnt[lon]=82770. float
"""

if "G" in TASK:
    G = read_PKL(G=True)  # type: Dict
    cnt, obj_set = count_key(G)
    print(f"obj_set: {obj_set}")
    print(f"len(G): {len(G)}")
    print_dict(cnt)

# note: str one_hot时的大小写.
"""Out[1]. 
obj_set: set()
len(G): 783
len(cnt): 16
cnt[timezone]=77. int
cnt[group_photo]=746. bool
cnt[description]=776. float
cnt[category]=782. int
cnt[state]=783. int
cnt[rating]=783. float
cnt[join_mode]=783. int
cnt[created]=783. float
cnt[lat]=783. float
cnt[visibility]=783. int
cnt[topics]=783. List -> int
cnt[members]=783. float
cnt[country]=783. int
cnt[organizer]=783. -
cnt[city]=783. int
cnt[lon]=783. float
"""

if "E" in TASK:
    E = read_PKL(E=True)  # type: Dict
    cnt, obj_set = count_key(E)
    print(f"obj_set: {obj_set}")
    print(f"len(E): {len(E)}")
    print_dict(cnt)

"""Out[2]
obj_set: set()
len(E): 93512
len(cnt): 27
cnt[duration]=5180. float
cnt[why]=5355. float
cnt[fee_label]=15062. int
cnt[fee_accepts]=15062. int
cnt[fee_currency]=15062. int
cnt[fee_description]=15062. int
cnt[fee_amount]=15062. float
cnt[fee_required]=15062. int
cnt[rsvp_limit]=26812. float
cnt[photo_url]=28450. bool
cnt[how_to_find_us]=43810. float
cnt[venue]=66179. -
cnt[event_hosts]=83430. -
cnt[description]=90825. float
cnt[status]=93512. int
cnt[maybe_rsvp_count]=93512. float
cnt[waitlist_count]=93512. float
cnt[updated]=93512. float
cnt[group]=93512. -
cnt[yes_rsvp_count]=93512. float
cnt[created]=93512. float
cnt[visibility]=93512. int
cnt[headcount]=93512. float
cnt[utc_offset]=93512. float
cnt[time]=93512. float
cnt[rating_average]=93512. float
cnt[rating_count]=93512. float
"""

if "R" in TASK:
    R = read_PKL(R=True)  # type: Dict
    cnt, obj_set = count_key(R)
    print(f"obj_set: {obj_set}")
    print(f"len(R): {len(R)}")
    print_dict(cnt)

"""Out[3]
obj_set: set()
len(R): 765317
len(cnt): 14
cnt[comments]=139402. float
cnt[venue]=545043. -
cnt[member_photo]=667529. bool
cnt[tallies_waitlist]=765316. float
cnt[tallies_maybe]=765316. float
cnt[tallies_no]=765316. float
cnt[tallies_yes]=765316. float
cnt[response]=765317. float
cnt[mtime]=765317. float
cnt[event]=765317. -
cnt[group]=765317. -
cnt[created]=765317. float
cnt[member]=765317. -
cnt[guests]=765317. float
"""

#################


if "T" in TASK:
    T = read_PKL(T=True)  # type: Dict
    cnt, obj_set = count_key(T)
    print(f"obj_set: {obj_set}")
    print(f"len(T): {len(T)}")
    print_dict(cnt)
"""Out[4]. one_hot
obj_set: set()
len(T): 18114
len(cnt): 3
...ignored
"""

if "V" in TASK:
    V = read_PKL(V=True)  # type: Dict
    cnt, obj_set = count_key(V, {"address_3"})
    print(f"obj_set: {obj_set}")
    print(f"len(V): {len(V)}")
    print_dict(cnt)

"""Out[5]
obj_set: set()
len(V): 14108
len(cnt): 6
cnt[repinned]=562. bool
cnt[state]=14089. int
cnt[city]=14094. int
cnt[country]=14099. int
cnt[lat]=14108. float
cnt[lon]=14108. float
"""

# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# 分析字段的数量:
# intuition: Member中含bio的人, 更希望去交流, 更希望参加活动和社交. 将一些难以处理的字段(str等)变为bool,int,float类型.
from typing import Dict
from utils import read_PKL, count_key, print_dict

ALL = {"M", "G", "E", "R", "T", "V", "C"}
TASK = ALL

if "M" in TASK:
    M = read_PKL(M=True)  # type: Dict
    cnt, obj_set = count_key(M)
    print(f"obj_set: {obj_set}")
    print(f"len(M): {len(M)}")
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

if "C" in TASK:
    C = read_PKL(C=True)  # type: Dict
    cnt, obj_set = count_key(C)
    print(f"obj_set: {obj_set}")
    print(f"len(C): {len(C)}")
    print_dict(cnt)

"""Out[0]
obj_set: {'photo', 'self', 'topics', 'other_services'}
len(M): 82770
len(cnt): 17
cnt[other_services]=12762
cnt[bio]=14790
cnt[hometown]=27204
cnt[topics]=53085
cnt[photo]=62128
cnt[state]=82303
cnt[country]=82748
cnt[city]=82748
cnt[self]=82770
cnt[joined]=82770
cnt[lat]=82770
cnt[name]=82770
cnt[lang]=82770
cnt[id]=82770
cnt[link]=82770
cnt[visited]=82770
cnt[lon]=82770

obj_set: {'organizer', 'group_photo', 'topics', 'category'}
len(G): 783
len(cnt): 21
cnt[timezone]=77
cnt[group_photo]=746
cnt[description]=776
cnt[category]=782
cnt[state]=783
cnt[who]=783
cnt[rating]=783
cnt[join_mode]=783
cnt[created]=783
cnt[lat]=783
cnt[visibility]=783
cnt[topics]=783
cnt[name]=783
cnt[id]=783
cnt[members]=783
cnt[country]=783
cnt[organizer]=783
cnt[urlname]=783
cnt[city]=783
cnt[link]=783
cnt[lon]=783

obj_set: {'group', 'venue', 'rating', 'fee', 'event_hosts'}
len(E): 93512
len(cnt): 24
cnt[duration]=5180
cnt[why]=5355
cnt[fee]=15062
cnt[rsvp_limit]=26812
cnt[photo_url]=28450
cnt[how_to_find_us]=43810
cnt[venue]=66179
cnt[event_hosts]=83430
cnt[description]=90825
cnt[status]=93512
cnt[maybe_rsvp_count]=93512
cnt[waitlist_count]=93512
cnt[updated]=93512
cnt[rating]=93512
cnt[group]=93512
cnt[yes_rsvp_count]=93512
cnt[created]=93512
cnt[visibility]=93512
cnt[name]=93512
cnt[id]=93512
cnt[headcount]=93512
cnt[utc_offset]=93512
cnt[time]=93512
cnt[event_url]=93512

obj_set: {'tallies', 'member', 'event', 'group', 'venue', 'member_photo'}
len(R): 765317
len(cnt): 12
cnt[comments]=139402
cnt[venue]=545043
cnt[member_photo]=667529
cnt[tallies]=765316
cnt[response]=765317
cnt[mtime]=765317
cnt[event]=765317
cnt[group]=765317
cnt[created]=765317
cnt[rsvp_id]=765317
cnt[member]=765317
cnt[guests]=765317

obj_set: set()
len(T): 18114
len(cnt): 3
cnt[id]=18114
cnt[urlkey]=18114
cnt[name]=18114

obj_set: set()
len(V): 14108
len(cnt): 13
cnt[address_3]=6
cnt[address_2]=1324
cnt[phone]=4813
cnt[zip]=13501
cnt[state]=14089
cnt[city]=14094
cnt[address_1]=14096
cnt[name]=14098
cnt[country]=14099
cnt[lat]=14108
cnt[repinned]=14108
cnt[id]=14108
cnt[lon]=14108

obj_set: set()
len(C): 33
len(cnt): 3
cnt[shortname]=33
cnt[id]=33
cnt[name]=33
"""

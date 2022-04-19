# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# 分析字段的数量:
# intuition: Member中含bio的人, 更希望去交流, 更希望参加活动和社交. 将一些难以处理的字段(str等)变为bool,int,float类型.
from typing import Dict
from utils import read_PKL, count_key, print_dict

ALL = {"M", "G", "E", "R", "T", "V"}
TASK = {"V"}

if "M" in TASK:
    M = read_PKL(M=True)  # type: Dict
    cnt, obj_set = count_key(M)
    print(f"len(M): {len(M)}")
    print(f"obj_set: {obj_set}")
    print_dict(cnt)

"""Out[0]. 这里不进行归一化处理. 后面统一处理.
obj_set: {'topics', 'other_services', 'photo', 'self'}
len(M): 82770
len(cnt): 17
cnt[other_services]=12762. float. 转为len. itt: 其他账户链接越多, 积极性要高
cnt[bio]=14790. float. 改为len. itt: 写的越多, 积极性要高
cnt[hometown]=27204. one_hot(0: None)
cnt[topics]=53085. one_hot
cnt[photo]=62128. bool.
cnt[state]=82303. one_hot(0: None)
cnt[country]=82748. one_hot(0: None)
cnt[city]=82748. one_hot(0: None)
cnt[self]=82770. ignored
cnt[joined]=82770. float
cnt[lat]=82770. float
cnt[name]=82770. ignored
cnt[lang]=82770. one_hot
cnt[id]=82770. ignored
cnt[link]=82770. ignored
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
obj_set: {'topics', 'group_photo', 'organizer', 'category'}
len(G): 783
len(cnt): 21
cnt[timezone]=77. one_hot(0: None)
cnt[organizer_id]=687. one_hot(0: None)
cnt[group_photo]=746. bool
cnt[description]=776. len. 
cnt[category]=782. one_hot
cnt[state]=783. one_hot
cnt[who]=783. ignored
cnt[rating]=783. float
cnt[join_mode]=783. one_hot
cnt[created]=783. float
cnt[lat]=783. float
cnt[visibility]=783. int
cnt[topics]=783. one_hot
cnt[name]=783. ignored
cnt[id]=783. ignored
cnt[members]=783. float
cnt[country]=783. one_hot
cnt[urlname]=783. ignored
cnt[city]=783. one_hot
cnt[link]=783. ignored
cnt[lon]=783. float
"""

if "E" in TASK:
    E = read_PKL(E=True)  # type: Dict
    cnt, obj_set = count_key(E)
    print(f"obj_set: {obj_set}")
    print(f"len(E): {len(E)}")
    print_dict(cnt)

"""Out[2]
obj_set: {'event_hosts', 'venue', 'rating', 'group', 'fee'}
len(E): 93512
len(cnt): 24
cnt[duration]=5180. float
cnt[why]=5355. len
cnt[fee]=15062. 
cnt[rsvp_limit]=26812. float
cnt[photo_url]=28450. bool
cnt[how_to_find_us]=43810. len
cnt[venue]=66179.
cnt[event_hosts]=83430. 
cnt[description]=90825. len
cnt[status]=93512. one hot
cnt[maybe_rsvp_count]=93512. float
cnt[waitlist_count]=93512. float
cnt[updated]=93512. float
cnt[rating]=93512. 
cnt[group]=93512. 
cnt[yes_rsvp_count]=93512. float
cnt[created]=93512. float
cnt[visibility]=93512. one hot
cnt[name]=93512. ignored
cnt[id]=93512. ignored
cnt[headcount]=93512. float
cnt[utc_offset]=93512. float
cnt[time]=93512. float
cnt[event_url]=93512. ignored
"""

if "R" in TASK:
    R = read_PKL(R=True)  # type: Dict
    cnt, obj_set = count_key(R)
    print(f"obj_set: {obj_set}")
    print(f"len(R): {len(R)}")
    print_dict(cnt)

"""Out[3]
obj_set: {'tallies', 'venue', 'event', 'group', 'member_photo', 'member'}
len(R): 765317
len(cnt): 12
cnt[comments]=139402. len
cnt[venue]=545043.
cnt[member_photo]=667529. bool
cnt[tallies]=765316. 4*float
cnt[response]=765317. one_hot
cnt[mtime]=765317: float
cnt[event]=765317.
cnt[group]=765317.
cnt[created]=765317: float
cnt[rsvp_id]=765317. ignored
cnt[member]=765317. 
cnt[guests]=765317: float
"""

#################


if "T" in TASK:
    T = read_PKL(T=True)  # type: Dict
    cnt, obj_set = count_key(T)
    print(f"obj_set: {obj_set}")
    print(f"len(T): {len(T)}")
    for k, v in cnt.items():  # type: str, int
        print(f"cnt[{k}]={v}")
    print()
"""Out[4]
obj_set: set()
len(T): 18114
len(cnt): 3
cnt[id]=18114. ignored
cnt[urlkey]=18114. ignored
cnt[name]=18114. ignored
"""

if "V" in TASK:
    V = read_PKL(V=True)  # type: Dict
    cnt, obj_set = count_key(V, {"address_3"})
    print(f"obj_set: {obj_set}")
    print(f"len(V): {len(V)}")
    for k, v in cnt.items():  # type: str, int
        print(f"cnt[{k}]={v}")
    print()

"""Out[5]
obj_set: set()
len(V): 14108
len(cnt): 13
cnt[address_3]=6. ignored
cnt[address_2]=1324. ignored
cnt[phone]=4813. ignored
cnt[zip]=13501. ignored
cnt[state]=14089. one hot
cnt[city]=14094. one hot
cnt[address_1]=14096. ignored
cnt[name]=14098. one hot
cnt[country]=14099. one hot
cnt[lat]=14108. float
cnt[repinned]=14108. bool
cnt[id]=14108. ignored
cnt[lon]=14108. float
"""

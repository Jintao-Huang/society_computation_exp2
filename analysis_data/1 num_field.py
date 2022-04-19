# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# 分析字段的数量:
# intuition: Member中含bio的人, 更希望去交流, 更希望参加活动和社交. 将一些难以处理的字段(str等)变为bool,int,float类型.
from typing import Dict
from utils import read_GMER
from collections import defaultdict

TASK = {"E"}


def count_key(D: Dict, debug=None):
    debug = debug or set()
    cnt = defaultdict(int)
    for k, d in D.items():
        for k2 in d.keys():
            # Debug
            if k2 in debug:
                print()
            #
            cnt[k2] += bool(d[k2])  # except None
    cnt = {k: cnt[k] for k in sorted(cnt, key=lambda k: cnt[k])}
    return cnt


if "M" in TASK:
    M = read_GMER(M=True)  # type: Dict
    print(f"M的数量: {len(M)}")
    cnt = count_key(M)
    for k, v in cnt.items():  # type: str, int
        print(f"cnt[{k}]={v}")

"""Out[0]. 这里不进行归一化处理. 后面统一处理.
M的数量: 82770
cnt[other_services]=12762. float. 转为len(other_services). itt: 其他账户链接越多, 积极性要高
cnt[bio]=14790. float. 改为len(bio). itt: 写的越多, 积极性要高
cnt[hometown]=27204. one_hot(0: None)
cnt[topics]=53085. one_hot
cnt[photo]=62128. bool.
cnt[state]=82303. one_hot(0: None)
cnt[country]=82748. one_hot(0: None)
cnt[city]=82748. one_hot(0: None)
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
    G = read_GMER(G=True)  # type: Dict
    print(f"G的数量: {len(G)}")
    cnt = count_key(G)
    for k, v in cnt.items():  # type: str, int
        print(f"cnt[{k}]={v}")


# note: str one_hot时的大小写.
"""Out[1]. 
G的数量: 783
cnt[timezone]=77. one_hot(0: None)
cnt[organizer_id]=687. one_hot(0: None)
cnt[group_photo]=746. bool
cnt[description]=776. len(description). 
cnt[category]=782. one_hot
cnt[state]=783. one_hot
cnt[who]=783. ignored
cnt[rating]=783. float
cnt[join_mode]=783. one_hot
cnt[created]=783. float
cnt[lat]=783. float
cnt[visibility]=783. float
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
    E = read_GMER(E=True)  # type: Dict
    print(f"E的数量: {len(E)}")
    cnt = count_key(E, debug={"duration", "why", "fee", "rsvp_limit"})
    for k, v in cnt.items():  # type: str, int
        print(f"cnt[{k}]={v}")


"""Out[2]
E的数量: 93512
cnt[duration]=5180
cnt[why]=5355
cnt[fee]=15062
cnt[rsvp_limit]=26812
cnt[photo_url]=28450
cnt[how_to_find_us]=43810
cnt[tallies]=64466
cnt[rsvp_ids]=64467
cnt[venue]=66179
cnt[event_hosts]=83430
cnt[description]=90825
cnt[status]=93512
cnt[maybe_rsvp_count]=93512
cnt[waitlist_count]=93512
cnt[updated]=93512
cnt[rating]=93512
cnt[yes_rsvp_count]=93512
cnt[created]=93512
cnt[visibility]=93512
cnt[name]=93512
cnt[id]=93512
cnt[headcount]=93512
cnt[utc_offset]=93512
cnt[time]=93512
cnt[event_url]=93512
cnt[group_id]=93512
"""
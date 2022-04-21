# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
1G:
2. Member_id List[~ok]
3. Event_id List[~ok]
4. RSVP_id List[~ok]
5. Topic_id List[ok]
- Organizer_id(2. M)

2M:
1. Group_id List[~ok]
3. Event_id List[~ok]
4. RSVP_id List[~ok]
5. Topic_id List[ok]
- Organize_Group(1. G)

3E:
1. Group_id[ok]
2. Member_id List[~ok]
4. RSVP_id List[~ok]
6. V_id[ok]
- Event_hosts_id List(M)

4R:
1. Member_id[ok]
2. Group_id[ok]
3. Event_id[ok]
6. V_id[ok]

5T: one hot
1. Group_id List[x]
2. Member_id List[x]

6V: unzip
3. Event_id List
4. RSVP_id List
"""

from typing import Dict, List
from collections import defaultdict
from utils import read_PKL, save_PKL
import logging


def add_list_from_D(SD, add_DD: List, id_attr_names: List, add_attr_name: str):
    # no V
    mappers = [defaultdict(list) for _ in range(len(add_DD))]
    for mapper, id_attr_name in zip(mappers, id_attr_names):
        for k, d in SD.items():  # type: str, Dict
            m_id = d[id_attr_name]
            mapper[m_id].append(k)

    for D, mapper in zip(add_DD, mappers):
        for k, d in D.items():
            d[add_attr_name] = list(set(mapper[k]))


def add_list_from_R(R, G, M, E):
    # no V
    gm_mapper = defaultdict(list)
    mg_mapper = defaultdict(list)
    me_mapper = defaultdict(list)
    em_mapper = defaultdict(list)

    for k, r in R.items():
        g = r["group"]
        e = r["event"]
        m = r["member"]
        gm_mapper[g].append(m)
        em_mapper[e].append(m)
        mg_mapper[m].append(g)
        me_mapper[m].append(e)

    for k, g in G.items():
        g["member_list"] = list(set(gm_mapper[k]))

    for k, m in M.items():
        m["group_list"] = list(set(mg_mapper[k]))
        m["event_list"] = list(set(me_mapper[k]))
    for k, e in E.items():
        e["member_list"] = list(set(em_mapper[k]))


def R_move_to_E(R, E):
    # 产生ok. 不需要跑
    # no_total = set()
    # for k, d in E.items():
    #     r_id_list = d["rsvp_id_list"]
    #     mapper = {}
    #     no = no_total.copy()  # 不能move
    #     for r_id in r_id_list:
    #         r = R[r_id]
    #         for k, v in r.items():
    #             if k in no:
    #                 continue
    #             if k not in mapper:
    #                 mapper[k] = v
    #             elif v != mapper[k]:
    #                 no.add(k)
    #                 mapper.pop(k)
    #     no_total |= no
    # ok = set(R[next(iter(R))].keys()) - no_total
    # print(ok)

    ok = {'tallies_yes', 'venue', 'tallies_no', 'tallies_waitlist', 'tallies_maybe'}  # 'event', 'group'
    for k, d in E.items():
        r_id_list = d["rsvp_id_list"]
        if len(r_id_list) == 0:
            r = {"tallies_yes": 0., 'tallies_no': 0., 'venue': None, 'tallies_waitlist': 0., 'tallies_maybe': 0.}
        else:
            r = R[r_id_list[0]]
        # modify e
        for k in ok:
            if k in d:
                if r[k] is not None and r[k] != d[k]:
                    logging.warning("...")
            else:
                d[k] = r[k] if k in r else None

        # remove attr in r
        for r_id in r_id_list:
            r = R[r_id]  # type: Dict
            for k in ok:
                if k in r:
                    r.pop(k)


if __name__ == '__main__':
    G, M, E, R = read_PKL(G=True, M=True, E=True, R=True)
    add_list_from_D(R, [M, G, E], ["member", "group", "event"], "rsvp_id_list")
    R_move_to_E(R, E)
    add_list_from_R(R, G, M, E)
    add_list_from_D(E, [G], ["group"], "event_list")
    save_PKL(G=G, M=M, E=E, R=R)

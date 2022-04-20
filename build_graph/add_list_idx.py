# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
1G:
2. Member_id List
3. Event_id List
5. Topic_id List[ok]
- Organizer_id(2. M)

2M:
1. Group_id List
3. Event_id List
4. RSVP_id List
5. Topic_id List[ok]
- Organize_Group(1. G)

3E:
1. Group_id
2. Member_id List
4. RSVP_id List
6. V_id[ok]
- Event_hosts_id List(M)

4R:
1. Member_id[ok]
2. Group_id[ok]
3. Event_id[ok]
6. V_id[ok]

5T: one hot
1. Group_id List
2. Member_id List

6V: unzip
3. Event_id List
4. RSVP_id List
"""

"""
R:
  M: List
  G: List
  E: List
  V: List
"""
from typing import Dict
from collections import defaultdict
from utils import read_PKL, save_PKL

TASK = {"R"}


def add_list_from_R(R, M, G, E):
    # no V
    M_mapper, G_mapper, E_mapper = defaultdict(list), defaultdict(list), defaultdict(list)
    for k, d in R.items():  # type: str, Dict
        m_id = d["member"]
        g_id = d["group"]
        e_id = d["event"]
        M_mapper[k].append(m_id)
        G_mapper[k].append(g_id)
        E_mapper[k].append(e_id)




def R_move_to_E():
    pass


if "R" in TASK:
    G, M, E, R, V = read_PKL(G=True, M=True, E=True, R=True, V=True)
    add_list_from_R(R, M, G, E)

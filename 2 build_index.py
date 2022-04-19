# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from config import PKL_PATH
from utils import read_from_pickle, read_PKL, save_PKL, check_islist
from typing import Dict, List, Callable
import logging

# intuition: O(N) -> O(1)复杂度
TASK = {"Post"}
ALL = {"Pre", "GME", "R", "T", "V", "C", "Post"}

def build_idx(D: List, get_item: Callable[[Dict], Dict], id_attr="id"):
    ans = {}
    for tmp in D:
        item = get_item(tmp)
        id_ = item[id_attr]
        if id_ in ans:
            logging.warning(id_)
        ans[id_] = item
    return ans


#
if "Pre" in TASK:
    # test PKL
    obj = read_from_pickle(PKL_PATH)
    for k in obj.keys():
        print(k, len(obj[k]))
    # Group 783
    # Memeber 82770
    # PastEvent 93512
    # RSVPs 65128

if "GME" in TASK:
    # 为G, M, E建立索引.
    obj = read_from_pickle(PKL_PATH)
    #
    G = build_idx(obj["Group"], lambda tmp: tmp["content"]["item"])
    save_PKL(G=G)
    #
    M = build_idx(obj["Memeber"], lambda tmp: tmp["content"]["member"])
    save_PKL(M=M)
    #
    E = build_idx(obj["PastEvent"], lambda tmp: tmp["content"]["item"])
    save_PKL(E=E)


def build_R_idx(R: List):
    ans = {}
    for tmp in R:
        items = tmp["content"]["results"]["items"]
        items = check_islist(items)
        tmp["content"]["results"]["items"] = items
        for tmp2 in items:
            item = tmp2["item"]
            id_ = item["rsvp_id"]
            if id_ in ans:
                logging.warning(id_)
            ans[id_] = item
    return ans


if "R" in TASK:
    # 为R建立索引
    obj = read_from_pickle(PKL_PATH)
    R = build_R_idx(obj["RSVPs"])
    save_PKL(R=R)


def build_T_idx(M: Dict, G: Dict):
    T = {}
    for D in [M, G]:
        for v in D.values():
            ts = v["topics"]
            ts = check_islist(ts)
            for tmp in ts:
                t = tmp["topics_item"]
                id_ = t["id"]
                if id_ not in T:
                    T[id_] = t
    return T


if "T" in TASK:
    M, G = read_PKL(M=True, G=True)
    T = build_T_idx(M, G)
    save_PKL(T=T)


def build_VC_idx(DD: List, attr_name):
    ans = {}
    for D in DD:
        for v in D.values():
            if attr_name not in v:
                continue
            attr = v[attr_name]
            id_ = attr["id"]
            if id_ not in ans:
                ans[id_] = attr
    return ans


if "V" in TASK:
    E, R = read_PKL(E=True, R=True)
    V = build_VC_idx([E, R], "venue")
    save_PKL(V=V)

if "C" in TASK:
    G = read_PKL(G=True)
    C = build_VC_idx([G], "category")
    save_PKL(C=C)

if "Post" in TASK:
    # test PKL
    G, M, E, R, T, V, C = read_PKL(True, True, True, True, True, True, True)
    for x in [G, M, E, R, T, V, C]:
        print(len(x))
    # 783
    # 82770
    # 93512
    # 765317
    # 18114
    # 14108

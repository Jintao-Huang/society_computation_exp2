# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from config import PKL_PATH
from utils import read_from_pickle, read_GMER, save_GMER
import logging
from typing import Dict, List, Callable

# intuition: O(N) -> O(1)复杂度
TASK = {"Post"}  # 0..3


def build_idx(D: List, get_item: Callable[[Dict], Dict], id_attr="id"):
    ans = {}
    for tmp in D:
        item = get_item(tmp)
        id_ = item[id_attr]
        if id_ in ans:
            logging.warning(id_)
        ans[id_] = item
    return ans


def build_R_idx(D: List, get_items: Callable[[Dict], Dict],
                get_item: Callable[[Dict], Dict], id_attr="id"):
    ans = {}
    for tmp in D:
        items = get_items(tmp)
        if items is None:
            items = []
        if isinstance(items, dict):  # fix bug
            items = [items]
        for tmp2 in items:
            item = get_item(tmp2)
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
    save_GMER(G=G)
    #
    M = build_idx(obj["Memeber"], lambda tmp: tmp["content"]["member"])
    save_GMER(M=M)
    #
    E = build_idx(obj["PastEvent"], lambda tmp: tmp["content"]["item"])
    save_GMER(E=E)
    #

    print("task 1 finished")

if "R" in TASK:
    # 为R建立索引
    obj = read_from_pickle(PKL_PATH)
    R = build_R_idx(obj["RSVPs"],
                    lambda tmp: tmp["content"]["results"]["items"],
                    lambda tmp2: tmp2["item"], "rsvp_id")
    save_GMER(R=R)
    print("task 2 finished")

if "Post" in TASK:
    # test GMER
    G, M, E, R = read_GMER(True, True, True, True)
    for x in [G, M, E, R]:
        print(len(x))
    # 783
    # 82770
    # 93512
    # 765317

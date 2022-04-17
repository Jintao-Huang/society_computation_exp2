# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from config import PKL_PATH, G_PKL_PATH, E_PKL_PATH, M_PKL_PATH, R_PKL_PATH
from utils import read_from_pickle, save_to_pickle, read_GMER
import logging

TASK = {3}

#
if __name__ == '__main__' and 0 in TASK:
    # test PKL
    obj = read_from_pickle(PKL_PATH)
    for k in obj.keys():
        print(k, len(obj[k]))
    # Group 783
    # Memeber 82770
    # PastEvent 93512
    # RSVPs 65128

if __name__ == '__main__' and 1 in TASK:
    # 为G, M, E建立索引.
    """
    1. E中存在str id
    2. G, M, E 不存在重复id
    
    """
    obj = read_from_pickle(PKL_PATH)
    #
    G = {}
    for g in obj["Group"]:
        id_ = int(g['content']['item']['id'])
        if id_ in G:
            logging.warning("id `%d` occurs many times in G" % id_)
        G[id_] = g['content']['item']
    save_to_pickle(G, G_PKL_PATH)
    del obj["Group"], G, g  # save memory
    M = {}
    for m in obj["Memeber"]:
        id_ = int(m['content']['member']['id'])
        if id_ in M:
            logging.warning("id `%d` occurs many times in M" % id_)
        M[id_] = m['content']['member']
    save_to_pickle(M, M_PKL_PATH)
    del obj["Memeber"], M, m
    #
    E = {}
    for e in obj["PastEvent"]:
        id_ = e['content']['item']['id']
        try:
            id_ = int(e)
        except ValueError:
            logging.warning("str id `%s` occurs in E" % id_)
        if id_ in E:
            logging.warning("id `%d` occurs many times in E" % id_)
        E[id_] = e['content']['item']
    save_to_pickle(E, E_PKL_PATH)
    print("task 1 finished")

if __name__ == '__main__' and 2 in TASK:
    # 为R建立索引
    """
    1. R不存在重复id
    """
    obj = read_from_pickle(PKL_PATH)
    R = {}
    for r in obj["RSVPs"]:
        items = r['content']['results']['items']
        if items is None:
            continue
        if not isinstance(items, list):  # len == 1
            items = [items]
        for item in items:
            id_ = int(item['item']['rsvp_id'])
            if id_ in R:
                logging.warning("%d occur many times in R" % id_)
            R[id_] = item
    save_to_pickle(R, R_PKL_PATH)
    print("task 2 finished")

if __name__ == '__main__' and 3 in TASK:
    # test GMER
    G, M, E, R = read_GMER(True, True, True, True)
    for x in [G, M, E, R]:
        print(len(x))
    # 783
    # 82770
    # 93512
    # 765317

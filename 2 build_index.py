# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from config import PKL_PATH
from utils import read_from_pickle, read_GMER, save_GMER
import logging
from typing import Dict

# intuition: O(N) -> O(1)复杂度
TASK = {"Post"}  # 0..3

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
    """
    1. E中存在str id
    2. G, M, E 不存在重复id
    
    """
    obj = read_from_pickle(PKL_PATH)
    #
    G = {}
    for g in obj["Group"]:
        g = g['content']['item']
        id_ = g['id']
        if id_ in G:
            logging.warning("id `%s` occurs many times in G" % id_)
        G[id_] = g
    save_GMER(G=G)
    del obj["Group"], G  # save memory
    M = {}
    for m in obj["Memeber"]:
        m = m['content']['member']
        id_ = m['id']
        if id_ in M:
            logging.warning("id `%s` occurs many times in M" % id_)
        M[id_] = m
    save_GMER(M=M)
    del obj["Memeber"], M
    #
    E = {}
    for e in obj["PastEvent"]:
        e = e['content']['item']
        id_ = e['id']
        if id_ in E:
            logging.warning("id `%s` occurs many times in E" % id_)
        E[id_] = e
    save_GMER(E=E)
    print("task 1 finished")

if "R" in TASK:
    # 为R建立索引
    """
    1. R不存在重复id
    2. 每个event只有一个RSVPs
    """
    obj = read_from_pickle(PKL_PATH)
    E = read_GMER(E=True)
    R = {}
    for r in obj["RSVPs"]:
        items = r['content']['results']['items']
        if items is None:
            continue
        if not isinstance(items, list):  # len == 1
            items = [items]
        if len(items) == 0:
            continue
        rsvp_ids = []
        event_id = items[0]['item']["event"]["id"]
        if "tallies" not in items[0]["item"]:
            tallies = None
        else:
            tallies = items[0]["item"]
        e = E[event_id]  # type: Dict
        for item in items:
            item = item['item']
            id_ = item['rsvp_id']
            item.pop("tallies")
            if item["event"]["id"] != event_id:
                logging.warning('item["event"]["id"] != event_id, %s', id_)
            if tallies and tallies != item["tallies"]:
                logging.warning('tallies != item["event"]["id"]', id_)
            if id_ in R:
                logging.warning("%s occur many times in R" % id_)
            R[id_] = item
            rsvp_ids.append(id_)
        e["tallies"] = tallies
        if "rsvp_ids" in e:
            e["rsvp_ids"] += rsvp_ids
            logging.warning('"rsvp_ids" in e, %s', e["id"])
        else:
            e["rsvp_ids"] = rsvp_ids

    save_GMER(R=R)
    save_GMER(E=E)
    print("task 2 finished")

# C:\Users\29715\AppData\Local\Programs\Python\Python39\python.exe "D:/programming/python/pycharm/course/society_computation_exp2/2 build_index.py"
# task 1 finished
# WARNING:root:"rsvp_ids" in e, 102416522
# WARNING:root:"rsvp_ids" in e, 102630842
# WARNING:root:"rsvp_ids" in e, 103381842
# WARNING:root:"rsvp_ids" in e, 103461802
# WARNING:root:"rsvp_ids" in e, 103663842
# WARNING:root:"rsvp_ids" in e, 103675042
# WARNING:root:"rsvp_ids" in e, 105741752
# WARNING:root:"rsvp_ids" in e, 106957632
# WARNING:root:"rsvp_ids" in e, 111028392
# WARNING:root:"rsvp_ids" in e, 113317172
# WARNING:root:"rsvp_ids" in e, 117189582
# WARNING:root:"rsvp_ids" in e, 13551091
# WARNING:root:"rsvp_ids" in e, 13701966
# WARNING:root:"rsvp_ids" in e, 14358834
# WARNING:root:"rsvp_ids" in e, 14417719
# WARNING:root:"rsvp_ids" in e, 14417719
# WARNING:root:"rsvp_ids" in e, 14451822
# WARNING:root:"rsvp_ids" in e, 14451868
# WARNING:root:"rsvp_ids" in e, 14451884
# WARNING:root:"rsvp_ids" in e, 14457300
# WARNING:root:"rsvp_ids" in e, 15525245
# WARNING:root:"rsvp_ids" in e, 15603004
# WARNING:root:"rsvp_ids" in e, 16011906
# WARNING:root:"rsvp_ids" in e, 16235767
# WARNING:root:"rsvp_ids" in e, 24704851
# WARNING:root:"rsvp_ids" in e, 41157472
# WARNING:root:"rsvp_ids" in e, 41157472
# WARNING:root:"rsvp_ids" in e, 42682532
# WARNING:root:"rsvp_ids" in e, 48753832
# WARNING:root:"rsvp_ids" in e, 50659132
# WARNING:root:"rsvp_ids" in e, 54047632
# WARNING:root:"rsvp_ids" in e, 65270582
# WARNING:root:"rsvp_ids" in e, 69073242
# WARNING:root:"rsvp_ids" in e, 70308852
# WARNING:root:"rsvp_ids" in e, 73703392
# WARNING:root:"rsvp_ids" in e, 74979712
# WARNING:root:"rsvp_ids" in e, 76032852
# WARNING:root:"rsvp_ids" in e, 76034482
# WARNING:root:"rsvp_ids" in e, 77229092
# WARNING:root:"rsvp_ids" in e, 80097982
# WARNING:root:"rsvp_ids" in e, 80979692
# WARNING:root:"rsvp_ids" in e, 82103842
# WARNING:root:"rsvp_ids" in e, 84231452
# WARNING:root:"rsvp_ids" in e, 87982382
# WARNING:root:"rsvp_ids" in e, 88083632
# WARNING:root:"rsvp_ids" in e, 89590252
# WARNING:root:"rsvp_ids" in e, 93115762
# WARNING:root:"rsvp_ids" in e, 97820432
# WARNING:root:"rsvp_ids" in e, 98911382
# task 2 finished

if "POST" in TASK:
    # test GMER
    G, M, E, R = read_GMER(True, True, True, True)
    for x in [G, M, E, R]:
        print(len(x))
    # 783
    # 82770
    # 93512
    # 765317

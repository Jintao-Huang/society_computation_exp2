# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from collections import defaultdict
from typing import Dict, Set, Callable, List, Union, Any


def count_key(D: Dict, debug: Set[str] = None):
    cnt = defaultdict(int)
    obj_set = set()
    for k, d in D.items():
        for k2 in d.keys():
            # Debug
            if debug and k2 in debug:
                print()
            if bool(d[k2]) and not isinstance(d[k2], (list, str, int, float)):  # 含bool
                obj_set.add(k2)
            #
            cnt[k2] += bool(d[k2])  # except None
    cnt = {k: cnt[k] for k in sorted(cnt, key=lambda k: cnt[k])}
    return cnt, obj_set


def remove_attr(D: Dict, attr_names: Set[str]) -> None:
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name in d:
                d.pop(attr_name)


def attr_to_len(D: Dict, attr_names: Set[str]) -> None:
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name in d:
                x = d.pop(attr_name)
                if x is None:
                    d[attr_name] = 0
                else:
                    d[attr_name] = len(x)


def attr_to_id(D: Dict, attr_name: str, id_attr_name: str = "id"):
    for k, d in D.items():  # type: str, Dict
        if attr_name not in d or d[attr_name] is None:
            continue
        d[attr_name] = d[attr_name][id_attr_name]


def topics_to_idlist(D: Dict):
    for k, d in D.items():  # type: str, Dict
        if "topics" not in d:
            continue
        ts = d["topics"]
        ts = check_islist(ts)
        t_list = []
        for t in ts:
            t_id = t["topics_item"]["id"]
            t_list.append(t_id)
        d["topics"] = t_list


def eventhosts_to_idlist(D: Dict):
    for k, d in D.items():  # type: str, Dict
        if "event_hosts" not in d:
            continue
        ts = d["event_hosts"]
        ts = check_islist(ts)
        t_list = []
        for t in ts:
            t_id = t["event_hosts_item"]["member_id"]
            t_list.append(t_id)
        d["event_hosts"] = t_list


def attr_to_bool(D: Dict, attr_names: Set[str]) -> None:
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name in d:
                x = d.pop(attr_name)
                if x == "False":
                    x = False
                d[attr_name] = bool(x)


def unzip_attr(D: Dict, attr_name: str):
    for k, d in D.items():  # type: str, Dict
        if attr_name not in d:
            continue
        attr = d.pop(attr_name)  # type: Dict
        for k2, x in attr.items():
            d[attr_name + "_" + k2] = x


def check_islist(items: Union[List, Any]) -> List:
    if items is None:
        items = []
    elif isinstance(items, dict):
        items = [items]
    return items


def print_dict(cnt: Dict) -> None:
    print(f"len(cnt): {len(cnt)}")
    for k, v in cnt.items():  # type: str, int
        print(f"cnt[{k}]={v}")
    print()

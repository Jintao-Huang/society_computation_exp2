# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from collections import defaultdict
from typing import Dict, List, Union, Any, Set
import logging


def count_key(D: Dict, debug: List[str] = None):
    cnt = defaultdict(int)
    obj_set = set()
    for k, d in D.items():
        for k2 in d.keys():
            # Debug
            if debug and k2 in debug:
                print()
            if d[k2] is not None and not isinstance(d[k2], (list, str, int, float)):  # bool是int的子类
                obj_set.add(k2)
            if d[k2] is not None:
                cnt[k2] += 1  # except None
    cnt = {k: cnt[k] for k in sorted(cnt, key=lambda k: cnt[k])}
    return cnt, obj_set


def remove_attr(D: Dict, attr_names: List[str]) -> None:
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name in d:
                d.pop(attr_name)


def attr_to_len(D: Dict, attr_names: List[str]) -> None:
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name in d:
                x = d[attr_name]
                if x is None:
                    d[attr_name] = 0
                elif not isinstance(x, (int, float)):
                    d[attr_name] = len(x)
            else:
                d[attr_name] = 0
            d[attr_name] = float(d[attr_name])
            d["has_" + attr_name] = bool(d[attr_name])


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


def attr_to_bool(D: Dict, attr_names: List[str]) -> None:
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name in d:
                x = d[attr_name]
                if x == "False":
                    x = False
                d[attr_name] = bool(x)
            else:
                d[attr_name] = False


def attr_to_float(D: Dict, attr_names: List[str], defaults: List[float] = None) -> None:
    if defaults is None:
        defaults = [0.] * len(attr_names)
    for k, d in D.items():  # type: str, Dict
        for attr_name, default in zip(attr_names, defaults):
            if attr_name in d:
                d[attr_name] = float(d[attr_name])
            else:
                if default is None:
                    logging.warning(k)
                d[attr_name] = float(default)


def default_using_median(D: Dict, attr_names: List[str]) -> None:
    mapper = defaultdict(list)
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name in d and d[attr_name] is not None:
                if isinstance(d[attr_name], (int, str)):
                    d[attr_name] = float(d[attr_name])
                mapper[attr_name].append(d[attr_name])
    median = {}
    for k, v in mapper.items():
        median[k] = sum(v) / len(v)

    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name not in d or d[attr_name] is None:
                d[attr_name] = median[attr_name]


def attr_to_int(D: Dict, attr_names: List[str]) -> None:
    n_mapper = {attr_name: 1 for attr_name in attr_names}
    mapper = defaultdict(dict)
    have_None = {attr_name: False for attr_name in attr_names}
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name not in d:
                have_None[attr_name] = True
                continue
            x = d[attr_name]
            if isinstance(x, str):
                x = x.lower()
            if x not in mapper[attr_name]:
                mapper[attr_name][x] = n_mapper[attr_name]
                n_mapper[attr_name] += 1
    # remove
    for attr_name in n_mapper.keys():
        if not have_None[attr_name]:
            n_mapper[attr_name] -= 1
        num = n_mapper[attr_name]
        if num == 1 or num > 1000:
            attr_names.remove(attr_name)
            remove_attr(D, [attr_name])
            print(f"{attr_name}: {num}, remove")
        elif 100 < num <= 1000:
            logging.warning(f"{attr_name}: {num}")
        else:
            print(f"{attr_name}: {num}")

    #
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name not in d:
                d[attr_name] = 0
                continue
            x = d[attr_name]
            if isinstance(x, str):
                x = x.lower()
            d[attr_name] = mapper[attr_name][x]
            if not have_None[attr_name]:
                d[attr_name] -= 1


def unzip_attr(D: Dict, attr_name: str):
    for k, d in D.items():  # type: str, Dict
        if attr_name not in d:
            continue
        attr = d.pop(attr_name)  # type: Dict
        for k2, x in attr.items():
            d[attr_name + "_" + k2] = x


def unzip_venue(D: Dict, V: Dict):
    attr_name = "venue"
    for k, d in D.items():  # type: str, Dict
        if attr_name in d:
            attr = d.pop(attr_name)  # type: Dict
        else:
            attr = None
        if attr is None:
            v = {"state": None, "lon": None, "lat": None, "repinned": None, "country": None}
            d["has_" + attr_name] = False
        else:
            v = V[attr]
            d["has_" + attr_name] = True
        for k2, x in v.items():
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


def get_all_key(D: Dict) -> Dict:
    keys = {}
    for d in D.values():  # type: Dict
        for attr_name in d.keys():
            if attr_name not in keys:
                keys[attr_name] = type(d[attr_name])
    return keys


def check_data(D: Dict):
    keys = get_all_key(D)
    attrs = set()
    for d in D.values():  # type: Dict
        for attr_name in keys:
            if attr_name not in d or type(d[attr_name]) != keys[attr_name]:
                attrs.add(attr_name)

    print(keys)
    print(attrs)
    print()


def move_E_to_G(E, G, attr_names):
    ge_mapper = defaultdict(lambda: defaultdict(list))
    for k, e in E.items():
        g_id = e["group"]
        for attr_name in attr_names:
            ge_mapper[g_id][attr_name].append(e[attr_name])
    for k, g in G.items():
        v = ge_mapper[k]
        for k2, v2 in v.items():
            if len(v2) == 0:
                v[k2] = 0
            else:
                v[k2] = sum(v2) / len(v2)
            if k2 in g:
                logging.warning("...")
            g[k2] = v[k2]


def handle_organizer_event_hosts(M, G, E):
    is_organizer = defaultdict(int)
    is_event_hosts = defaultdict(int)
    for k, g in G.items():
        organizer = g["organizer"]
        is_organizer[organizer] += 1
    for k, e in E.items():
        if 'event_hosts' not in e:
            event_hosts = []
        else:
            event_hosts = e["event_hosts"]
        for eh in event_hosts:
            is_event_hosts[eh] += 1
    for k, m in M.items():
        m["is_organizer"] = is_organizer[k]
        m["is_event_hosts"] = is_event_hosts[k]


import time


def convert_datetime(D: Dict, attr_names: List[str]) -> None:
    for k, d in D.items():  # type: str, Dict
        for attr_name in attr_names:
            if attr_name in d:
                lt = time.localtime(int(d[attr_name] / 1000))
                y, m, day, yd, wd = lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_yday, lt.tm_wday
                d.pop(attr_name)
                d[attr_name + "_y"] = y
                d[attr_name + "_m"] = m
                d[attr_name + "_d"] = day
                d[attr_name + "_yd"] = yd
                d[attr_name + "_wd"] = wd
            else:
                print()

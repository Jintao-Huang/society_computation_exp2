# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from xml.etree import ElementTree as ET
import os
from typing import Dict, List, Union, Optional


def simplify(list_with_dict: List[Dict]) -> Optional[Dict]:
    # save memory
    """若List[Dict]中, 各个Dict的key不重复, 则简化为Dict"""
    # e.g. [{"item": ...}, {"item": ...}]  # 不简化
    # e.g. [{"id": ...}, {"name", ...}] 简化为{"id": ..., "name", ...}
    ans = {}
    for d in list_with_dict:
        if len(d) != 1:
            raise ValueError("The len of dict in list_with_dict != 1")
        k = next(iter(d))
        if k in ans:
            return None
        ans[k] = d[k]
    return ans


def tree_to_dict(n: ET.Element, ans: Dict[str, Union[List, Dict, str]], ignore_error=False) -> None:
    child = []
    if not ignore_error:
        if len(n.attrib) > 0:
            raise ValueError("This function does not process attribution")
        if not (n.tail is None or n.tail.isspace()):
            raise ValueError("This function does not process tail")
    for c in n:
        item = {}
        tree_to_dict(c, item, ignore_error)
        child.append(item)
    if not ignore_error:
        if len(child) != 0 and not (n.tail is None or n.tail.isspace()):
            raise ValueError("This function does not process text on non-leaf nodes")

    if len(child) == 0:  # leaf nodes
        child = n.text
    else:
        c = simplify(child)  # simplify
        if c is not None:
            child = c
    ans[n.tag] = child


def xml_to_dict(fpath: str, ignore_error=False) -> Dict:
    tree = ET.parse(fpath)  # type: ET.ElementTree
    root = tree.getroot()  # type: ET.Element
    fname = os.path.basename(fpath)
    ans = {"fname": fname, "content": {}}
    tree_to_dict(root, ans["content"], ignore_error)
    return ans


if __name__ == '__main__':
    # test example
    from config import DATASET_DIR

    example = os.path.join(DATASET_DIR, "RSVPs 11313977.xml")
    obj = xml_to_dict(example)
    print(obj)

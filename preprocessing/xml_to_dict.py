# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from xml.etree import ElementTree as ET
import os
from typing import Dict


def tree_to_dict(n: ET.Element, ans: Dict, ignore_error=False) -> None:
    child = {}
    if not ignore_error:
        if len(n.attrib) > 0:
            raise ValueError("This function does not process attribution")
        if not (n.tail is None or n.tail.isspace()):
            raise ValueError("This function does not process tail")
    for c in n:
        tree_to_dict(c, child, ignore_error)
    if not ignore_error:
        if len(child) != 0 and not (n.tail is None or n.tail.isspace()):
            raise ValueError("This function does not process text on non-leaf nodes")
    if len(child) == 0:  # leaf nodes
        child = n.text
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
    example = os.path.join(DATASET_DIR, "Group 570.xml")
    print(xml_to_dict(example))

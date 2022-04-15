# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from xml.etree import ElementTree as ET
import os
from typing import Dict
from config import DATASET_DIR


def tree_to_dict(n: ET.Element, ignore_error=True) -> Dict:
    # call: xml_to_dict(root)
    if not ignore_error and (len(n.attrib) > 0 or n.tail is not None):
        raise ValueError("This function does not handle attribution and tail")
    ans = {}
    for c in n:
        ans.update(tree_to_dict(c, ignore_error))
    if not ignore_error and len(ans) != 0 and n.text is not None:
        raise ValueError("This function does not process text on non-leaf nodes")
    if len(ans) == 0:  # leaf nodes
        ans = n.text
    return {n.tag: ans}


def xml_to_dict(fname: str, ignore_error=True) -> Dict:
    tree = ET.parse(fname)  # type: ET.ElementTree
    root = tree.getroot()  # type: ET.Element
    return tree_to_dict(root, ignore_error)


if __name__ == '__main__':
    # test example
    example = os.path.join(DATASET_DIR, "Group 570.xml")
    print(xml_to_dict(example))

# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from config import JSON_PATH
import json
from typing import Dict

if __name__ == '__main__':
    with open(JSON_PATH, "r") as f:
        obj = json.load(f)  # type: Dict
    for k in obj.keys():
        print(k, len(obj[k]))

    """Out[0]
    Group 783
    Memeber 82770
    PastEvent 93512
    RSVPs 65128
    """
